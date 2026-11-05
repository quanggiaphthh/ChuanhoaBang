"""Offline, conservative DOCX table-width optimizer.

This module is intentionally narrower than Word: it refuses unsupported OOXML.
A structural pass does not imply Microsoft Word layout acceptance.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import os
import posixpath
import re
import tempfile
import unicodedata
from importlib.resources import files as package_files
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from lxml import etree

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
}
W = "{" + NS["w"] + "}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
REL_NS = {"rel": "http://schemas.openxmlformats.org/package/2006/relationships"}
POLICY_REGISTRY = json.loads(
    package_files(__package__).joinpath("POLICY_REGISTRY.json").read_text(encoding="utf-8")
)
POLICY_VERSION = POLICY_REGISTRY["version"]
MAX_UNCOMPRESSED = 60 * 1024 * 1024
MAX_COMPRESSED_DOCX_BYTES = 64 * 1024 * 1024
MAX_ENTRY = 25 * 1024 * 1024
MAX_RATIO = 150
HEADER_HINTS = ("stt", "họ tên", "họ và tên", "nội dung", "nhiệm vụ", "đơn vị", "chỉ tiêu",
                "kết quả", "thời gian", "ngày", "số", "kinh phí", "ghi chú", "trách nhiệm",
                "tiến độ", "sản phẩm", "chủ trì", "phối hợp", "tên", "thành tiền")
LAYOUT_HINTS = ("cộng hòa xã hội", "độc lập - tự do", "đảng ủy", "đảng bộ", "nơi nhận", "người ký", "tổng giám đốc")
NO_BREAK_SPACE_CHARACTERS = frozenset(("\u00a0", "\u180e", "\u2007", "\u202f"))
LAYOUT_DASH_TRANSLATION = str.maketrans({
    char: "-" for char in "\u2010\u2011\u2012\u2013\u2014\u2212"
})
DANGEROUS_IN_TABLE = [".//w:sdt", ".//w:ins", ".//w:del", ".//w:moveFrom", ".//w:moveTo",
                      ".//w:fldChar", ".//w:instrText", ".//w:drawing", ".//w:pict",
                      ".//w:object", ".//w:altChunk", ".//w:hyperlink",
                      ".//w:trPrChange", ".//w:tcPrChange", ".//w:tblPrChange",
                      ".//w:fldSimple", ".//w:commentReference", ".//w:commentRangeStart",
                      ".//w:commentRangeEnd", ".//w:customXml", ".//w:smartTag",
                      ".//w:subDoc", ".//w:contentPart", ".//w:bookmarkStart",
                      ".//w:bookmarkEnd", ".//w:permStart", ".//w:permEnd"]
NON_BODY_STORY_PART = re.compile(r"^word/(?:header\d+|footer\d+|footnotes|endnotes)\.xml$")


class TableError(ValueError):
    """Unsafe or unsupported document/table operation."""


def available_profiles():
    """Return profile identifiers defined by the packaged policy registry."""
    return tuple(POLICY_REGISTRY["profiles"])


def _profile_context(profile):
    if profile is None:
        return {"profile": None, "profile_status": "NOT_SELECTED", "profile_rules_applied": False}
    if not isinstance(profile, str) or profile not in POLICY_REGISTRY["profiles"]:
        raise TableError("UNKNOWN_PROFILE")
    return {"profile": profile, "profile_status": "REFERENCE_ONLY", "profile_rules_applied": False}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _xml(data: bytes):
    if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper():
        raise TableError("XML_DTD_NOT_ALLOWED")
    try:
        return etree.fromstring(data, parser=etree.XMLParser(resolve_entities=False,
                 load_dtd=False, no_network=True, huge_tree=False, remove_blank_text=False))
    except (etree.XMLSyntaxError, ValueError) as exc:
        raise TableError("INVALID_XML") from exc


def _package(path: str | Path):
    path = Path(path)
    if path.suffix.lower() != ".docx" or not path.is_file():
        raise TableError("INPUT_MUST_BE_EXISTING_DOCX")
    try:
        if path.stat().st_size > MAX_COMPRESSED_DOCX_BYTES:
            raise TableError("COMPRESSED_DOCX_SIZE_LIMIT")
        with ZipFile(path) as z:
            items = z.infolist()
            names = [x.filename for x in items]
            if len(names) != len(set(names)) or len(names) > 3000:
                raise TableError("DUPLICATE_OR_TOO_MANY_ZIP_ENTRIES")
            if any(n.startswith("/") or "\\" in n or ".." in n.split("/") for n in names):
                raise TableError("UNSAFE_ZIP_PATH")
            total = 0
            for item in items:
                total += item.file_size
                if item.flag_bits & 0x1 or item.file_size > MAX_ENTRY or total > MAX_UNCOMPRESSED:
                    raise TableError("ENCRYPTED_OR_OVERSIZED_DOCX")
                if item.file_size and item.file_size / max(1, item.compress_size) > MAX_RATIO:
                    raise TableError("ZIP_RATIO_LIMIT")
            if not {"[Content_Types].xml", "word/document.xml", "_rels/.rels"}.issubset(names):
                raise TableError("INCOMPLETE_OPC_PACKAGE")
            raw = z.read("word/document.xml")
            settings = z.read("word/settings.xml") if "word/settings.xml" in names else b""
            story_parts = {item.filename: z.read(item.filename) for item in items
                           if NON_BODY_STORY_PART.fullmatch(item.filename)}
            document_rels_name = "word/_rels/document.xml.rels"
            document_rels = z.read(document_rels_name) if document_rels_name in names else b""
            return raw, settings, names, story_parts, document_rels
    except (BadZipFile, OSError, RuntimeError) as exc:
        raise TableError("INVALID_OR_UNREADABLE_ZIP") from exc


def _tables(root):
    # Includes body tables inside wrappers; nested ones are reported as unsupported.
    return root.xpath(".//w:body//w:tbl", namespaces=NS)


def _section_story_references(root, document_rels, story_parts):
    if not document_rels:
        return {}, {}
    relationship_root = _xml(document_rels)
    relationships = {}
    ambiguous_ids = set()
    for rel in relationship_root.xpath("./rel:Relationship", namespaces=REL_NS):
        relationship_id = rel.get("Id")
        if not relationship_id:
            continue
        if relationship_id in relationships:
            ambiguous_ids.add(relationship_id)
        else:
            relationships[relationship_id] = rel

    targets = {}
    for relationship_id, rel in relationships.items():
        if relationship_id in ambiguous_ids:
            continue
        story_type = rel.get("Type", "").rsplit("/", 1)[-1]
        external = rel.get("TargetMode", "Internal").casefold() == "external"
        if story_type not in ("header", "footer") or external:
            continue
        target = rel.get("Target", "")
        part = (posixpath.normpath(target.lstrip("/")) if target.startswith("/") else
                posixpath.normpath(posixpath.join("word", target)))
        if part in story_parts:
            targets[relationship_id] = (part, story_type)

    owners = {}
    inheritance_candidates = {}
    active_default = {}
    sections = root.xpath(".//w:body/w:sectPr | .//w:body//w:pPr/w:sectPr", namespaces=NS)
    for section_index, section in enumerate(sections):
        references = section.xpath("./w:headerReference | ./w:footerReference", namespaces=NS)
        defaults = {"header": [], "footer": []}
        for reference in references:
            tag_name = reference.tag.rsplit("}", 1)[-1]
            expected_story_type = tag_name.removesuffix("Reference")
            if expected_story_type not in defaults:
                continue
            reference_type = reference.get(W + "type", "default")
            relationship_id = reference.get(R + "id")
            relationship = targets.get(relationship_id) if relationship_id else None
            if relationship is not None and relationship[1] != expected_story_type:
                relationship = None
            if reference_type == "default":
                defaults[expected_story_type].append(relationship)
                continue
            if relationship is None:
                continue
            part, story_type = relationship
            owners.setdefault(part, []).append({
                "section_index": section_index,
                "story_type": story_type,
                "reference_type": reference_type,
            })

        for story_type, section_defaults in defaults.items():
            if not section_defaults:
                active = active_default.get(story_type)
                if active is not None:
                    part, source_section_index = active
                    inheritance_candidates.setdefault(part, []).append({
                        "section_index": section_index,
                        "story_type": story_type,
                        "reference_type": "default",
                        "inherited_from_section_index": source_section_index,
                    })
                continue
            if len(section_defaults) != 1 or section_defaults[0] is None:
                active_default.pop(story_type, None)
                continue
            part, resolved_story_type = section_defaults[0]
            owner = {
                "section_index": section_index,
                "story_type": resolved_story_type,
                "reference_type": "default",
            }
            owners.setdefault(part, []).append(owner)
            active_default[story_type] = (part, section_index)
    return owners, inheritance_candidates


def _non_body_story_tables(story_parts, section_references, inheritance_candidates):
    inventory = []
    for part, data in sorted(story_parts.items()):
        root = _xml(data)
        owners = section_references.get(part, [])
        candidates = inheritance_candidates.get(part, [])
        tables = root.xpath(".//w:tbl", namespaces=NS)
        table_hashes = [digest(etree.tostring(table, method="c14n")) for table in tables]
        table_ids = {
            table: f"{part}#table={index}:{table_hash[:16]}"
            for index, (table, table_hash) in enumerate(zip(tables, table_hashes))
        }
        for index, table in enumerate(tables):
            ancestors = table.xpath("ancestor::w:tbl", namespaces=NS)
            parent_id = table_ids.get(ancestors[-1]) if ancestors else None
            inventory.append({
                "part": part,
                "story_table_index": index,
                "table_id": table_ids[table],
                "parent_table_id": parent_id,
                "table_sha256": table_hashes[index],
                "owner_status": ("DIRECT_AND_INHERITED_DEFAULT_CANDIDATES" if owners and candidates else
                                 "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED" if owners else
                                 "INHERITED_DEFAULT_CANDIDATES_ONLY" if candidates else
                                 "SECTION_RELATIONSHIP_NOT_RESOLVED"),
                "section_references": owners,
                "default_inheritance_candidates": candidates,
                "status": "REVIEW_REQUIRED",
                "reason": "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX",
            })
    return inventory


def _mirror_margins_enabled(settings: bytes):
    if not settings:
        return False
    node = _xml(settings).find(W + "mirrorMargins")
    if node is None:
        return False
    value = node.get(W + "val")
    if value is None or value.casefold() in ("1", "true", "on"):
        return True
    if value.casefold() in ("0", "false", "off"):
        return False
    return None


def _geometry(root, settings=b""):
    sections = root.xpath(".//w:sectPr", namespaces=NS)
    if len(sections) != 1:
        return {"status": "GEOMETRY_UNKNOWN", "reason": "MULTI_OR_MISSING_SECTION", "sections": len(sections)}
    sect = sections[0]
    size = sect.find(W + "pgSz")
    mar = sect.find(W + "pgMar")
    if size is None or mar is None:
        return {"status": "GEOMETRY_UNKNOWN", "reason": "MISSING_PAGE_GEOMETRY", "sections": 1}
    try:
        page_width = int(size.get(W + "w"))
        page_height = int(size.get(W + "h"))
        left, right = int(mar.get(W + "left")), int(mar.get(W + "right"))
        gutter = int(mar.get(W + "gutter", "0"))
        width = page_width - left - right - gutter
        if min(page_width, page_height, width) <= 0:
            raise ValueError("nonpositive")
    except (ValueError, TypeError):
        return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_PAGE_GEOMETRY", "sections": 1}
    mirror_margins = _mirror_margins_enabled(settings)
    if mirror_margins is None:
        return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_MIRROR_MARGINS_SETTING", "sections": 1}
    if mirror_margins and gutter > 0:
        return {"status": "GEOMETRY_UNKNOWN",
                "reason": "MIRRORED_GUTTER_GEOMETRY_UNSUPPORTED", "sections": 1}
    orientation = "LANDSCAPE" if page_width > page_height else "PORTRAIT"
    declared_orientation = size.get(W + "orient")
    if declared_orientation is not None:
        if declared_orientation not in ("portrait", "landscape"):
            return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_PAGE_ORIENTATION", "sections": 1}
        if declared_orientation.upper() != orientation:
            return {"status": "GEOMETRY_UNKNOWN", "reason": "PAGE_ORIENTATION_CONFLICT", "sections": 1}
    cols_nodes = sect.findall(W + "cols")
    if len(cols_nodes) > 1:
        return {"status": "GEOMETRY_UNKNOWN", "reason": "AMBIGUOUS_TEXT_COLUMNS", "sections": 1}
    cols = cols_nodes[0] if cols_nodes else None
    column_count = 1
    column_gap = 0
    available_width = width
    width_scope = "PAGE_TEXT_AREA"
    custom_column_widths = None
    custom_column_spacing = None
    try:
        if cols is not None:
            column_count = int(cols.get(W + "num", "1"))
            if column_count < 1:
                return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_TEXT_COLUMNS", "sections": 1}
            equal_width = cols.get(W + "equalWidth", "1")
            if equal_width is None or equal_width.casefold() not in (
                    "1", "true", "on", "0", "false", "off"):
                return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_TEXT_COLUMNS", "sections": 1}
            has_explicit_columns = bool(cols.findall(W + "col"))
            equal_width_enabled = equal_width.casefold() in ("1", "true", "on")
            if not equal_width_enabled and has_explicit_columns:
                explicit_columns = cols.findall(W + "col")
                if len(explicit_columns) > 45:
                    return {"status": "GEOMETRY_UNKNOWN",
                            "reason": "INVALID_TEXT_COLUMNS", "sections": 1}
                if len(explicit_columns) != column_count:
                    return {"status": "GEOMETRY_UNKNOWN",
                            "reason": "TEXT_COLUMN_COUNT_MISMATCH", "sections": 1}
                custom_column_widths = []
                custom_column_spacing = []
                for column_index, column in enumerate(explicit_columns):
                    raw_column_width = column.get(W + "w")
                    if raw_column_width is None:
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "CUSTOM_COLUMN_WIDTH_UNSPECIFIED", "sections": 1}
                    try:
                        column_width = int(raw_column_width)
                    except (TypeError, ValueError):
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "INVALID_CUSTOM_COLUMN_WIDTH", "sections": 1}
                    if column_width <= 0:
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "INVALID_CUSTOM_COLUMN_WIDTH", "sections": 1}
                    raw_spacing = column.get(W + "space")
                    if raw_spacing is None:
                        if column_index < len(explicit_columns) - 1:
                            return {"status": "GEOMETRY_UNKNOWN",
                                    "reason": "CUSTOM_COLUMN_SPACING_UNSPECIFIED", "sections": 1}
                        column_spacing = None
                    else:
                        try:
                            column_spacing = int(raw_spacing)
                        except (TypeError, ValueError):
                            return {"status": "GEOMETRY_UNKNOWN",
                                    "reason": "INVALID_CUSTOM_COLUMN_SPACING", "sections": 1}
                        if column_spacing < 0:
                            return {"status": "GEOMETRY_UNKNOWN",
                                    "reason": "INVALID_CUSTOM_COLUMN_SPACING", "sections": 1}
                    custom_column_widths.append(column_width)
                    custom_column_spacing.append(column_spacing)
                if sum(custom_column_widths) + sum(
                        gap or 0 for gap in custom_column_spacing[:-1]) > width:
                    return {"status": "GEOMETRY_UNKNOWN",
                            "reason": "CUSTOM_TEXT_COLUMNS_EXCEED_PAGE_TEXT_WIDTH", "sections": 1}
                column_count = len(explicit_columns)
                available_width = min(custom_column_widths)
                width_scope = "CUSTOM_COLUMN_MINIMUM_LOWER_BOUND"
            elif not equal_width_enabled:
                return {"status": "GEOMETRY_UNKNOWN",
                        "reason": "CUSTOM_TEXT_COLUMN_GEOMETRY_UNSUPPORTED", "sections": 1}
            elif has_explicit_columns:
                return {"status": "GEOMETRY_UNKNOWN",
                        "reason": "CUSTOM_TEXT_COLUMN_GEOMETRY_UNSUPPORTED", "sections": 1}
            if column_count > 1:
                if equal_width_enabled:
                    raw_space = cols.get(W + "space")
                    if raw_space is None:
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "COLUMN_SPACING_UNSPECIFIED", "sections": 1}
                    try:
                        column_gap = int(raw_space)
                    except (TypeError, ValueError):
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "INVALID_TEXT_COLUMN_SPACING", "sections": 1}
                    if column_gap < 0:
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "INVALID_TEXT_COLUMN_SPACING", "sections": 1}
                    columns_width = width - column_gap * (column_count - 1)
                    available_width = columns_width // column_count
                    if columns_width <= 0 or available_width <= 0:
                        return {"status": "GEOMETRY_UNKNOWN",
                                "reason": "INVALID_TEXT_COLUMN_SPACING", "sections": 1}
                    width_scope = "EQUAL_WIDTH_COLUMN_LOWER_BOUND"
    except (ValueError, TypeError):
        return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_TEXT_COLUMNS", "sections": 1}
    geometry = {"status": "STRUCTURAL", "available_twips": available_width,
                "page_width_twips": page_width, "page_text_width_twips": width,
                "column_count": column_count, "column_gap_twips": column_gap,
                "available_width_scope": width_scope, "orientation": orientation, "sections": 1}
    if custom_column_widths is not None:
        geometry["custom_column_widths_twips"] = custom_column_widths
        geometry["custom_column_spacing_after_twips"] = custom_column_spacing
    return geometry


def _protected(settings: bytes, names: list[str], root):
    reasons = []
    if root.xpath(".//mc:AlternateContent", namespaces=NS):
        reasons.append("ALTERNATE_CONTENT_NOT_SUPPORTED")
    if root.xpath(".//w:permStart | .//w:permEnd", namespaces=NS):
        reasons.append("RANGE_PERMISSIONS_UNRESOLVED")
    if any(n.startswith("_xmlsignatures/") for n in names):
        reasons.append("SIGNED_OPC_PACKAGE")
    if "word/vbaProject.bin" in names:
        reasons.append("MACRO_CONTENT_NOT_SUPPORTED")
    if settings:
        s = _xml(settings)
        protections = s.findall(".//" + W + "documentProtection")
        if len(protections) > 1:
            reasons.append("AMBIGUOUS_DOCUMENT_PROTECTION_SETTINGS")
        elif protections:
            enforcement = protections[0].get(W + "enforcement", "0").casefold()
            if enforcement in ("1", "true", "on"):
                reasons.append("DOCUMENT_PROTECTED")
            elif enforcement not in ("0", "false", "off"):
                reasons.append("INVALID_DOCUMENT_PROTECTION_ENFORCEMENT")
        if s.find(".//" + W + "trackRevisions") is not None:
            reasons.append("TRACK_CHANGES_ENABLED")
    if root.xpath(".//w:ins | .//w:del | .//w:moveFrom | .//w:moveTo", namespaces=NS):
        reasons.append("TRACKED_CHANGES_PRESENT")
    return reasons


def _text(cell):
    return " ".join("".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()
                    for p in cell.xpath("./w:p", namespaces=NS)).strip()


def _normalize_layout_text(value):
    text = unicodedata.normalize("NFKC", value).casefold().translate(LAYOUT_DASH_TRANSLATION)
    text = re.sub(r"\s*-\s*", " - ", text)
    return " ".join(text.split())


def _declared_width(parent, tag):
    if parent is None:
        return {"status": "ABSENT", "type": None, "raw_value": None, "twips": None}
    nodes = parent.findall(tag)
    if not nodes:
        return {"status": "ABSENT", "type": None, "raw_value": None, "twips": None}
    if len(nodes) != 1:
        return {"status": "AMBIGUOUS", "type": None, "raw_value": None, "twips": None}
    node = nodes[0]
    width_type = node.get(W + "type", "auto")
    raw_value = node.get(W + "w")
    if width_type not in ("dxa", "pct", "auto", "nil"):
        return {"status": "INVALID", "type": width_type,
                "raw_value": raw_value, "twips": None}
    if width_type in ("dxa", "pct"):
        try:
            parsed = int(raw_value)
            if parsed < 0:
                raise ValueError("negative width")
        except (TypeError, ValueError):
            return {"status": "INVALID", "type": width_type,
                    "raw_value": raw_value, "twips": None}
        return {"status": "DECLARED", "type": width_type,
                "raw_value": raw_value, "twips": parsed if width_type == "dxa" else None}
    return {"status": "DECLARED", "type": width_type,
            "raw_value": raw_value, "twips": None}


def _table_style_definitions(path):
    """Read table-style definitions for the bounded cell-margin resolver."""
    with ZipFile(path) as package:
        if "word/styles.xml" not in package.namelist():
            return {}
        root = _xml(package.read("word/styles.xml"))
    styles = {}
    for style in root.xpath("./w:style[@w:type='table']", namespaces=NS):
        style_id = style.get(W + "styleId")
        if not style_id or style_id in styles:
            raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
        styles[style_id] = style
    return styles


def _cell_padding(tbl, rows, table_styles=None):
    """Resolve bounded direct/table-style dxa margins; otherwise use the estimate."""
    default_padding = next(
        rule["default_padding_twips"]
        for rule in POLICY_REGISTRY["rules"]
        if rule["id"] == "CELL-MARGIN-DEFAULT-BUDGET-001"
    )

    def margin_pair(node):
        allowed = {W + "top", W + "bottom", W + "left", W + "right"}
        if any(child.tag not in allowed for child in node):
            raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
        pair = {}
        for side in ("left", "right"):
            values = node.findall(W + side)
            if len(values) > 1:
                raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
            if not values:
                continue
            value = values[0]
            if value.get(W + "type") != "dxa" or value.get(W + "w") is None:
                raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
            try:
                twips = int(value.get(W + "w"))
            except (TypeError, ValueError):
                raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED") from None
            if twips < 0:
                raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
            pair[side] = twips
        return pair or None

    table_style_nodes = tbl.xpath("./w:tblPr/w:tblStyle", namespaces=NS)
    if len(table_style_nodes) > 1:
        raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
    has_table_style = bool(table_style_nodes)
    style_pair = None
    style_chain_ids = []
    margin_source_style_id = None
    table_style_id = None
    if has_table_style:
        table_style_id = table_style_nodes[0].get(W + "val")
        if not table_style_id or table_styles is None:
            raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
        seen = set()
        chain = []
        current_id = table_style_id
        while current_id:
            if current_id in seen:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            seen.add(current_id)
            style = table_styles.get(current_id)
            if style is None:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            chain.append(style)
            style_chain_ids.append(current_id)
            if style.xpath("./w:tblStylePr[.//w:tblCellMar or .//w:tcMar]",
                            namespaces=NS):
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            if style.xpath("./w:tcPr/w:tcMar | ./w:tblPr/w:tcMar",
                            namespaces=NS):
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            based_on_nodes = style.findall(W + "basedOn")
            if len(based_on_nodes) > 1:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            if not based_on_nodes:
                break
            current_id = based_on_nodes[0].get(W + "val")
            if not current_id:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
        for style in reversed(chain):
            style_table_properties = style.findall(W + "tblPr")
            if len(style_table_properties) > 1:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            if not style_table_properties:
                continue
            style_margin_nodes = style_table_properties[0].findall(W + "tblCellMar")
            if len(style_margin_nodes) > 1:
                raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
            if style_margin_nodes:
                pair = margin_pair(style_margin_nodes[0])
                if pair and set(pair) != {"left", "right"}:
                    raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
                if pair:
                    style_pair = pair
                    margin_source_style_id = style.get(W + "styleId")

    table_properties = tbl.find(W + "tblPr")
    table_nodes = table_properties.findall(W + "tblCellMar") if table_properties is not None else []
    if len(table_nodes) > 1:
        raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
    table_pair = margin_pair(table_nodes[0]) if table_nodes else None
    if table_pair and set(table_pair) != {"left", "right"}:
        raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")

    effective_table_pair = table_pair or style_pair
    style_pair_used = False
    padding_rows = []
    has_explicit_horizontal_margin = bool(table_pair)
    uses_default_assumption = False
    for row in rows:
        padding_row = []
        for cell in row.xpath("./w:tc", namespaces=NS):
            cell_properties = cell.find(W + "tcPr")
            cell_nodes = cell_properties.findall(W + "tcMar") if cell_properties is not None else []
            if len(cell_nodes) > 1:
                raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
            cell_pair = margin_pair(cell_nodes[0]) if cell_nodes else None
            if cell_pair:
                has_explicit_horizontal_margin = True
                if not effective_table_pair and set(cell_pair) != {"left", "right"}:
                    raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
                left = cell_pair.get("left", effective_table_pair.get("left")
                                     if effective_table_pair else None)
                right = cell_pair.get("right", effective_table_pair.get("right")
                                      if effective_table_pair else None)
                if left is None or right is None:
                    raise TableError("CELL_MARGIN_GEOMETRY_UNRESOLVED")
                padding_row.append(left + right)
                if style_pair and not table_pair and (
                        "left" not in cell_pair or "right" not in cell_pair):
                    style_pair_used = True
            elif effective_table_pair:
                padding_row.append(effective_table_pair["left"] + effective_table_pair["right"])
                if style_pair and not table_pair:
                    style_pair_used = True
            else:
                uses_default_assumption = True
                padding_row.append(default_padding)
        padding_rows.append(padding_row)
    if uses_default_assumption:
        if style_pair_used and has_explicit_horizontal_margin:
            basis = "TABLE_STYLE_AND_EXPLICIT_DXA_AND_DEFAULT_ASSUMPTION"
        elif style_pair_used:
            basis = "TABLE_STYLE_DXA_AND_DEFAULT_ASSUMPTION"
        elif has_explicit_horizontal_margin:
            basis = "EXPLICIT_DXA_AND_DEFAULT_ASSUMPTION"
        elif has_table_style:
            basis = "TABLE_STYLE_DEFAULT_ASSUMPTION"
        else:
            basis = "ASSUMED_DEFAULT"
    elif style_pair_used and has_explicit_horizontal_margin:
        basis = "TABLE_STYLE_AND_EXPLICIT_DXA"
    elif style_pair_used:
        basis = "TABLE_STYLE_DXA"
    elif has_explicit_horizontal_margin:
        basis = "EXPLICIT_DXA"
    elif has_table_style:
        basis = "TABLE_STYLE_DEFAULT_ASSUMPTION"
    else:
        basis = "ASSUMED_DEFAULT"
    result = {
        "status": "RESOLVED",
        "basis": basis,
        "assumed_default_twips": default_padding if uses_default_assumption else None,
        "twips_by_row": padding_rows,
    }
    if has_table_style:
        result["table_style"] = {
            "status": "RESOLVED",
            "style_id": table_style_id,
            "based_on_chain": list(reversed(style_chain_ids)),
            "margin_source_style_id": margin_source_style_id,
            "horizontal_margin_twips": style_pair,
            "margin_used": style_pair_used,
        }
    return result


def _details(tbl, idx, geom, locks, table_id, parent_table_id, table_hash,
             table_styles=None):
    rows = tbl.xpath("./w:tr", namespaces=NS)
    grid = tbl.xpath("./w:tblGrid/w:gridCol", namespaces=NS)
    widths = []
    try:
        widths = [int(x.get(W + "w")) for x in grid]
        if not widths or min(widths) <= 0:
            raise ValueError("no valid grid")
    except (ValueError, TypeError):
        widths = []
    reasons = list(locks)
    if geom["status"] != "STRUCTURAL":
        reasons.append(geom["reason"])
    try:
        cell_padding = _cell_padding(tbl, rows, table_styles)
    except TableError as exc:
        cell_padding = {"status": "UNRESOLVED", "reason": str(exc)}
        reasons.append(str(exc))
    tblpr = tbl.find(W + "tblPr")
    table_preferred = _declared_width(tblpr, W + "tblW")
    cell_preferred = [
        [_declared_width(cell.find(W + "tcPr"), W + "tcW")
         for cell in row.xpath("./w:tc", namespaces=NS)]
        for row in rows
    ]
    if (table_preferred["status"] in ("INVALID", "AMBIGUOUS") or
            any(width["status"] in ("INVALID", "AMBIGUOUS")
                for row in cell_preferred for width in row)):
        reasons.append("INVALID_PREFERRED_WIDTH_DECLARATION")
    if tbl.xpath("ancestor::w:tbl | ancestor::w:sdt", namespaces=NS):
        reasons.append("NESTED_OR_CONTENT_CONTROL_TABLE")
    if tbl.xpath(".//w:tbl", namespaces=NS):
        reasons.append("CONTAINS_NESTED_TABLE")
    if tbl.xpath(".//w:gridSpan | .//w:vMerge | .//w:gridBefore | .//w:gridAfter", namespaces=NS):
        reasons.append("MERGED_OR_OMITTED_CELLS")
    if tbl.xpath(".//w:tblpPr | .//w:textDirection", namespaces=NS):
        reasons.append("FLOATING_OR_ROTATED_CONTENT")
    if any(tbl.xpath(q, namespaces=NS) for q in DANGEROUS_IN_TABLE):
        reasons.append("COMPLEX_CONTENT_OR_TRACKED_CHANGES")
    if not widths or not rows or any(len(r.xpath("./w:tc", namespaces=NS)) != len(widths) for r in rows):
        reasons.append("NON_RECTANGULAR_OR_MISSING_GRID")
    header = [_text(c) for c in rows[0].xpath("./w:tc", namespaces=NS)] if rows else []
    header_str = " ".join(header).casefold()
    # Layout and signature markers often occur in trailing rows or the body,
    # after a plausible data-looking first row. Scan the whole table before
    # allowing any operation that assumes this is an ordinary data table.
    table_text = _normalize_layout_text(" ".join(
        _text(cell) for row in rows for cell in row.xpath("./w:tc", namespaces=NS)
    ))
    if any(x in table_text for x in LAYOUT_HINTS):
        reasons.append("POSSIBLE_LAYOUT_TABLE")
    elif len(rows) < 2 or sum(bool(x) for x in header) < 2 or not any(x in header_str for x in HEADER_HINTS):
        reasons.append("UNCONFIRMED_DATA_TABLE")
    ind = tblpr.find(W + "tblInd") if tblpr is not None else None
    if ind is not None and ind.get(W + "w", "0") not in ("0", None):
        reasons.append("TABLE_INDENT_REQUIRES_REVIEW")
    header_nodes = rows[0].xpath("./w:trPr/w:tblHeader", namespaces=NS) if rows else []
    header_enabled = bool(header_nodes and header_nodes[0].get(W + "val", "1") not in
                          ("0", "false", "off"))
    pagination = {"header_repeat_first_row": header_enabled,
                  "exact_height_rows": len(tbl.xpath("./w:tr/w:trPr/w:trHeight[@w:hRule='exact']", namespaces=NS)),
                  "exact_line_spacing_paragraphs": len(tbl.xpath(".//w:pPr/w:spacing[@w:lineRule='exact']", namespaces=NS)),
                  "split_prevention_rows": len(tbl.xpath("./w:tr/w:trPr/w:cantSplit", namespaces=NS))}
    status = "SUPPORTED" if not reasons else "REVIEW_REQUIRED"
    return {"index": idx, "table_id": table_id, "parent_table_id": parent_table_id,
            "status": status, "reasons": sorted(set(reasons)), "rows": len(rows),
            "columns": len(widths), "grid_twips": widths, "header": header,
            "table_sha256": table_hash,
            "width_evidence": {
                "table_preferred": table_preferred,
                "cell_preferred": cell_preferred,
                "grid_sum_twips": sum(widths) if widths else None,
                "cell_padding": cell_padding,
                "word_rendered": "NOT_RUN",
            },
            "pagination_diagnostics": pagination,
            "overflow_declared": bool(widths and geom.get("available_twips") and
                sum(widths) > geom["available_twips"])}


def audit(path, profile=None):
    profile_context = _profile_context(profile)
    raw, settings, names, story_parts, document_rels = _package(path)
    root = _xml(raw)
    geometry = _geometry(root, settings)
    locks = _protected(settings, names, root)
    body_tables = _tables(root)
    table_styles = None
    if any(table.xpath("./w:tblPr/w:tblStyle", namespaces=NS) for table in body_tables):
        try:
            table_styles = _table_style_definitions(path)
        except TableError:
            table_styles = None
    table_hashes = [digest(etree.tostring(table, method="c14n")) for table in body_tables]
    table_ids = {
        table: f"body:{index}:{table_hash[:16]}"
        for index, (table, table_hash) in enumerate(zip(body_tables, table_hashes))
    }
    tables = []
    for index, table in enumerate(body_tables):
        ancestors = table.xpath("ancestor::w:tbl", namespaces=NS)
        parent_id = table_ids.get(ancestors[-1]) if ancestors else None
        tables.append(_details(table, index, geometry, locks, table_ids[table], parent_id,
                               table_hashes[index], table_styles))
    section_references, inheritance_candidates = _section_story_references(
        root, document_rels, story_parts
    )
    story_tables = _non_body_story_tables(story_parts, section_references, inheritance_candidates)
    return {"file": str(Path(path)), "input_sha256": digest(Path(path).read_bytes()),
            "policy": POLICY_VERSION, **profile_context, "geometry": geometry,
            "global_locks": locks, "table_count": len(tables), "tables": tables,
            "non_body_story_table_count": len(story_tables),
            "non_body_story_tables": story_tables,
            "word_render": "NOT_RUN"}


def _load_fonts(regular_file, bold_file):
    if not regular_file:
        raise TableError("TNR_FONT_FILE_REQUIRED")
    try:
        from PIL import ImageFont, features
        if not features.check("raqm"):
            raise TableError("LIBRAQM_SHAPING_UNAVAILABLE")
        regular = ImageFont.truetype(str(regular_file), 100, layout_engine=ImageFont.Layout.RAQM)
        regular_family, regular_style = regular.getname()
        if regular_family.casefold() != "times new roman":
            raise TableError("FONT_IS_NOT_TIMES_NEW_ROMAN")
        regular_style_tokens = set(re.findall(r"[a-z]+", regular_style.casefold()))
        if not regular_style_tokens or {"bold", "italic"} & regular_style_tokens:
            raise TableError("TNR_REGULAR_FACE_REQUIRED")
        bold = None
        if bold_file:
            bold = ImageFont.truetype(str(bold_file), 100, layout_engine=ImageFont.Layout.RAQM)
            bold_family, bold_style = bold.getname()
            if bold_family.casefold() != "times new roman":
                raise TableError("BOLD_FONT_IS_NOT_TIMES_NEW_ROMAN")
            bold_style_tokens = set(re.findall(r"[a-z]+", bold_style.casefold()))
            if "bold" not in bold_style_tokens or "italic" in bold_style_tokens:
                raise TableError("TNR_BOLD_FACE_REQUIRED")
        return regular, bold
    except TableError:
        raise
    except (OSError, AttributeError, TypeError, ValueError) as exc:
        raise TableError("UNREADABLE_TNR_FONT") from exc


def _basic_run_props(rpr):
    """A deliberately small OOXML subset; unresolved theme fonts never pass as TNR."""
    props = {}
    if rpr is None:
        return props
    fonts = rpr.find(W + "rFonts")
    if fonts is not None:
        for field in ("ascii", "hAnsi"):
            explicit = fonts.get(W + field)
            theme = fonts.get(W + field + "Theme")
            if explicit is not None:
                props[field] = explicit
            elif theme is not None:
                props[field] = "UNRESOLVED_THEME_FONT"
    size = rpr.find(W + "sz")
    if size is not None:
        props["size"] = size.get(W + "val")
    for tag, name in (("b", "bold"), ("i", "italic")):
        elt = rpr.find(W + tag)
        if elt is not None:
            props[name] = elt.get(W + "val", "1") not in ("0", "false", "off")
    return props


def _style_defaults(path):
    """Read shared run defaults and paragraph styles for a bounded cascade resolver.

    Only explicit ``basedOn`` paragraph-style chains are resolved. Unsupported
    run properties, character/table styles, and theme fonts remain fail-closed.
    No font files are read from or distributed with DOCX.
    """
    with ZipFile(path) as package:
        if "word/styles.xml" not in package.namelist():
            return {"doc_defaults": {}, "paragraph_styles": {},
                    "default_paragraph_style_id": None}
        root = _xml(package.read("word/styles.xml"))
    run_defaults = root.xpath("./w:docDefaults/w:rPrDefault/w:rPr", namespaces=NS)
    if len(run_defaults) > 1:
        raise TableError("AMBIGUOUS_STYLE_DEFAULTS")
    props = _basic_run_props(run_defaults[0]) if run_defaults else {}
    styles = root.xpath("./w:style[@w:type='paragraph'][@w:default='1']", namespaces=NS)
    if len(styles) > 1:
        raise TableError("AMBIGUOUS_DEFAULT_PARAGRAPH_STYLE")
    paragraph_styles = {}
    for style in root.xpath("./w:style[@w:type='paragraph']", namespaces=NS):
        style_id = style.get(W + "styleId")
        if not style_id or style_id in paragraph_styles:
            raise TableError("AMBIGUOUS_PARAGRAPH_STYLE_ID")
        paragraph_styles[style_id] = style
    if styles:
        default_id = styles[0].get(W + "styleId")
    else:
        default_id = "Normal" if "Normal" in paragraph_styles else None
    return {"doc_defaults": props, "paragraph_styles": paragraph_styles,
            "default_paragraph_style_id": default_id}


def _paragraph_run_props(cell, style_context):
    paragraphs = cell.xpath("./w:p", namespaces=NS)
    paragraph_styles = paragraphs[0].xpath("./w:pPr/w:pStyle", namespaces=NS)
    if len(paragraph_styles) > 1:
        raise TableError("AMBIGUOUS_PARAGRAPH_STYLE")
    style_id = (paragraph_styles[0].get(W + "val") if paragraph_styles
                else style_context["default_paragraph_style_id"])
    props = dict(style_context["doc_defaults"])
    if style_id is None:
        return props

    styles = style_context["paragraph_styles"]
    seen = set()
    chain = []
    current_id = style_id
    while current_id:
        if current_id in seen:
            raise TableError("STYLE_BASED_ON_CYCLE")
        seen.add(current_id)
        style = styles.get(current_id)
        if style is None:
            raise TableError("PARAGRAPH_STYLE_NOT_FOUND")
        chain.append(style)
        based_on = style.find(W + "basedOn")
        if based_on is None:
            break
        current_id = based_on.get(W + "val")
        if not current_id:
            raise TableError("PARAGRAPH_STYLE_BASE_MISSING")

    default_id = style_context["default_paragraph_style_id"]
    if default_id and style_id != default_id and default_id not in seen:
        raise TableError("PARAGRAPH_STYLE_DEFAULT_NOT_INHERITED")

    supported = {W + "rFonts", W + "sz", W + "b", W + "i"}
    for style in reversed(chain):
        run_props = style.find(W + "rPr")
        if run_props is None:
            continue
        if any(child.tag not in supported for child in run_props):
            raise TableError("UNSUPPORTED_STYLE_RUN_PROPERTY")
        if run_props.find(W + "b") is not None or run_props.find(W + "i") is not None:
            raise TableError("STYLE_TOGGLE_CASCADE_NOT_SUPPORTED")
        props.update(_basic_run_props(run_props))
    return props


def _runs(cell, style_defaults=None, allowed_sizes=(26, 28), size_error="FONT_SIZE_NOT_13_OR_14"):
    if len(cell.xpath("./w:p", namespaces=NS)) != 1:
        raise TableError("MULTI_PARAGRAPH_CELL_REQUIRES_REVIEW")
    all_runs = cell.xpath("./w:p/w:r", namespaces=NS)
    allowed_sizes = {str(size) for size in allowed_sizes}
    if not all_runs:
        raise TableError("NON_PLAIN_TEXT_OR_EMPTY_CELL")
    normalized = []
    for run in all_runs:
        if run.xpath("./w:br | ./w:tab | ./w:sym | ./w:footnoteReference", namespaces=NS):
            raise TableError("NON_PLAIN_RUN")
        runtext = "".join(run.xpath("./w:t/text()", namespaces=NS))
        if not runtext:
            # python-docx and Word often keep harmless empty w:r elements.
            # Ignore those, but not runs containing unsupported non-text data.
            if any(child.tag != W + "rPr" for child in run):
                raise TableError("NON_PLAIN_RUN")
            continue
        rpr = run.find(W + "rPr")
        if rpr is not None and rpr.find(W + "rStyle") is not None:
            raise TableError("CHARACTER_STYLE_CASCADE_NOT_SUPPORTED")
        style_context = (style_defaults if style_defaults is not None else
                         {"doc_defaults": {}, "paragraph_styles": {},
                          "default_paragraph_style_id": None})
        props = _paragraph_run_props(cell, style_context)
        props.update(_basic_run_props(rpr))
        if props.get("ascii", "").casefold() != "times new roman" or \
                props.get("hAnsi", "").casefold() != "times new roman":
            raise TableError("UNRESOLVED_EFFECTIVE_FONT")
        if props.get("size") not in allowed_sizes:
            raise TableError(size_error)
        if props.get("italic", False):
            raise TableError("ITALIC_FACE_NOT_IMPLEMENTED")
        normalized.append((runtext, int(props["size"]) / 2, bool(props.get("bold", False))))
    if not normalized:
        raise TableError("EMPTY_CELL_REQUIRES_REVIEW")
    return normalized


def _cell_measures(cell, fonts, style_defaults=None, allowed_sizes=(26, 28),
                   size_error="FONT_SIZE_NOT_13_OR_14"):
    chunks = _runs(cell, style_defaults, allowed_sizes, size_error)
    measures = []
    for content, pt, is_bold in chunks:
        face = fonts[1] if is_bold else fonts[0]
        if face is None:
            raise TableError("BOLD_TNR_FONT_REQUIRED")
        # 100px font metric scales to physical pt at the given size (not a Word-render promise).
        measures.append((content, pt, face))
    return measures


def _width(text, pt, face):
    # Convert 100-unit font advance to document twips; never use len(text) * constant.
    return int(math.ceil(float(face.getlength(text)) * pt / 100 * 20))


def _line_tokens(content):
    """Split at breakable Unicode whitespace, keeping glue spaces with adjacent text."""
    tokens = []
    current = []
    is_breakable_space = None
    for character in content:
        breakable = character.isspace() and character not in NO_BREAK_SPACE_CHARACTERS
        if current and breakable != is_breakable_space:
            tokens.append("".join(current))
            current = []
        current.append(character)
        is_breakable_space = breakable
    if current:
        tokens.append("".join(current))
    return tokens


def _estimate_lines(chunks, inner_twips):
    if inner_twips < 1:
        return 999999
    count = 1
    used = 0
    for content, pt, face in chunks:
        for token in _line_tokens(content):
            if token.isspace() and used == 0:
                continue
            size = _width(token, pt, face)
            if size > inner_twips and not token.isspace():
                return 999999
            if used + size > inner_twips and not token.isspace():
                count += 1
                used = size
            elif used + size <= inner_twips:
                used += size
            else:
                used = 0
    return count


def propose(path, table_index, font_regular=None, font_bold=None, profile=None):
    base = audit(path, profile=profile)
    if not isinstance(table_index, int) or table_index < 0 or table_index >= base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    info = base["tables"][table_index]
    profile_constraints = None
    if profile is not None:
        metric_policy = POLICY_REGISTRY["profiles"][profile]["table_width_measurement"]
        profile_constraints = {"scope": metric_policy["scope"],
                               "rule_id": metric_policy["rule_id"],
                               "font_sizes_pt": metric_policy["font_sizes_pt"]}
    result = {"input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": info["table_sha256"], "policy": POLICY_VERSION,
              "profile": base["profile"], "profile_status": base["profile_status"],
              "profile_rules_applied": base["profile_rules_applied"],
              "baseline_twips": info["grid_twips"], "candidate_twips": None,
              "decision": "REVIEW_REQUIRED", "evidence": "SOURCE_XML", "reasons": list(info["reasons"]),
              "word_render": "NOT_RUN", "content_modified": False}
    if profile_constraints is not None:
        result["profile_constraints"] = profile_constraints
    if info["status"] != "SUPPORTED":
        return result
    if base["geometry"]["status"] != "STRUCTURAL":
        result["reasons"].append("GEOMETRY_UNKNOWN")
        return result
    try:
        fonts = _load_fonts(font_regular, font_bold)
        inherited_styles = _style_defaults(path)
        tbl = _tables(_xml(_package(path)[0]))[table_index]
        # Table-level conditional text formatting is not yet resolved. Refuse,
        # rather than accidentally measure typography using only Normal style.
        if tbl.xpath("./w:tblPr/w:tblStyle", namespaces=NS):
            raise TableError("TABLE_STYLE_CASCADE_NOT_SUPPORTED")
        allowed_sizes = ((26, 28) if profile_constraints is None else
                         tuple(size * 2 for size in profile_constraints["font_sizes_pt"]))
        size_error = ("FONT_SIZE_NOT_13_OR_14" if profile_constraints is None else
                      "FONT_SIZE_OUTSIDE_PROFILE_METRIC_SCOPE")
        matrix = [[_cell_measures(c, fonts, inherited_styles, allowed_sizes, size_error)
                   for c in row.xpath("./w:tc", namespaces=NS)]
                  for row in tbl.xpath("./w:tr", namespaces=NS)]
    except TableError as exc:
        result["reasons"].append(str(exc))
        return result
    padding = info["width_evidence"]["cell_padding"]
    padding_by_cell = padding["twips_by_row"]
    current = info["grid_twips"]
    n = len(current)
    usable = base["geometry"]["available_twips"]
    floors = [
        max(160, max(
            _width(token, pt, f) + padding_by_cell[row_index][c]
            for row_index, row in enumerate(matrix)
            for content, pt, f in row[c]
            for token in (re.findall(r"\S+", content) or [""])
        ))
        for c in range(n)
    ]
    if sum(floors) > usable:
        result["reasons"].append("NO_SAFE_FIT_BY_FONT_METRICS")
        result["evidence"] = "FONT_METRIC_ESTIMATE"
        return result
    # Do not widen a table just to fill the page; correct overflow only if necessary.
    target = min(sum(current), usable)
    if sum(floors) > target:
        target = sum(floors)
    def score(widths):
        wrapped = 0
        for row_index, row in enumerate(matrix):
            wrapped += max(_estimate_lines(cell, widths[col] - padding_by_cell[row_index][col])
                           for col, cell in enumerate(row))
        return wrapped
    # Ensure baseline floors before swapping, distribute remaining width proportionally.
    residual = target - sum(floors)
    weights = [max(1, current[c] - floors[c]) for c in range(n)]
    candidate = [floors[c] + residual * weights[c] // sum(weights) for c in range(n)]
    candidate[-1] += target - sum(candidate)
    # Bounded local pair search; optimize row bottlenecks rather than each column separately.
    step = 100
    for _ in range(15):
        best = score(candidate)
        improvement = None
        for i in range(n):
            for j in range(n):
                if i == j or candidate[i] - step < floors[i]:
                    continue
                trial = candidate.copy()
                trial[i] -= step
                trial[j] += step
                val = score(trial)
                if val < best:
                    best, improvement = val, trial
        if improvement is None:
            break
        candidate = improvement
    base_feasible = sum(current) <= usable and all(current[c] >= floors[c] for c in range(n))
    baseline_score = score(current) if base_feasible else None
    candidate_score = score(candidate)
    result["evidence"] = "FONT_METRIC_ESTIMATE"
    result["metrics"] = {"baseline_estimated_lines": baseline_score,
                         "candidate_estimated_lines": candidate_score,
                         "font_regular": Path(font_regular).name,
                         "font_regular_sha256": digest(Path(font_regular).read_bytes()),
                         "font_bold": Path(font_bold).name if font_bold else None,
                         "font_bold_sha256": digest(Path(font_bold).read_bytes()) if font_bold else None,
                         "padding_twips_assumed": padding["assumed_default_twips"],
                         "padding_twips_by_cell": padding_by_cell,
                         "padding_basis": padding["basis"]}
    if base_feasible and (candidate_score >= baseline_score or candidate == current):
        result["decision"] = "NO_OP_VALID"
        result["reasons"].append("BASELINE_NOT_WORSE")
    elif candidate_score >= 999999:
        result["reasons"].append("CANDIDATE_UNREADABLE")
    else:
        result["decision"] = "PROPOSE_APPLY"
        result["candidate_twips"] = candidate
        result["reasons"].append("ESTIMATED_IMPROVEMENT_OR_OVERFLOW_REDUCTION")
    return result


def _without_width(tbl, *, allow_width=True, allow_first_row_header=False, height_rows=()):
    """Canonical comparison with only explicitly authorized properties masked.

    Header/height patches must NOT ignore width changes. The height allowlist
    is row-scoped; unrelated row rules remain part of the integrity check.
    """
    node = copy.deepcopy(tbl)
    if allow_width:
        for xp in ("./w:tblGrid", "./w:tblPr/w:tblW", "./w:tblPr/w:tblLayout", ".//w:tcPr/w:tcW"):
            for e in node.xpath(xp, namespaces=NS):
                e.getparent().remove(e)
    rows = node.xpath("./w:tr", namespaces=NS)
    for ri in height_rows:
        if not isinstance(ri, int) or not 0 <= ri < len(rows):
            raise TableError("HEIGHT_ROW_SCOPE_INVALID")
        for height in rows[ri].xpath("./w:trPr/w:trHeight", namespaces=NS):
            height.attrib.pop(W + "hRule", None)
    if allow_first_row_header:
        # Only the first physical row is whitelisted for this operation.
        for h in node.xpath("./w:tr[1]/w:trPr/w:tblHeader", namespaces=NS):
            h.getparent().remove(h)
        for trpr in node.xpath("./w:tr[1]/w:trPr", namespaces=NS):
            if len(trpr) == 0 and not trpr.attrib and not (trpr.text or "").strip():
                trpr.getparent().remove(trpr)
    for e in node.xpath(".//w:tcPr | ./w:tblPr", namespaces=NS):
        if len(e) == 0 and not e.attrib and not (e.text or "").strip():
            e.getparent().remove(e)
    return etree.tostring(node, method="c14n")


def _apply_widths(root, idx, widths):
    tbl = _tables(root)[idx]
    grid = tbl.find(W + "tblGrid")
    for col, width in zip(grid.findall(W + "gridCol"), widths):
        col.set(W + "w", str(width))
    tblpr = tbl.find(W + "tblPr")
    if tblpr is None:
        tblpr = etree.Element(W + "tblPr")
        tbl.insert(0, tblpr)
    tw = tblpr.find(W + "tblW")
    if tw is None:
        tw = etree.Element(W + "tblW")
        tblpr.insert(0, tw)
    tw.set(W + "type", "dxa")
    tw.set(W + "w", str(sum(widths)))
    layout = tblpr.find(W + "tblLayout")
    if layout is None:
        layout = etree.Element(W + "tblLayout")
        tblpr.append(layout)
    layout.set(W + "type", "fixed")
    for row in tbl.findall(W + "tr"):
        for cell, width in zip(row.findall(W + "tc"), widths):
            tcpr = cell.find(W + "tcPr")
            if tcpr is None:
                tcpr = etree.Element(W + "tcPr")
                cell.insert(0, tcpr)
            tcw = tcpr.find(W + "tcW")
            if tcw is None:
                tcw = etree.Element(W + "tcW")
                tcpr.insert(0, tcw)
            tcw.set(W + "type", "dxa")
            tcw.set(W + "w", str(width))


def _assert_safe(old_data, new_data, index, *, allow_first_row_header=False,
                 allow_height_rule=False, height_rows=()):
    old = _xml(old_data)
    new = _xml(new_data)
    ot, nt = _tables(old), _tables(new)
    if len(ot) != len(nt) or not 0 <= index < len(ot):
        raise TableError("TABLE_INVENTORY_CHANGED")
    if allow_first_row_header and allow_height_rule:
        raise TableError("MULTIPLE_UNSAFE_OPERATIONS")
    if allow_height_rule and (not height_rows or len(set(height_rows)) != len(height_rows)):
        raise TableError("HEIGHT_ROW_SCOPE_INVALID")
    if height_rows and not allow_height_rule:
        raise TableError("UNEXPECTED_HEIGHT_SCOPE")
    filters = {"allow_width": not (allow_first_row_header or allow_height_rule),
               "allow_first_row_header": allow_first_row_header,
               "height_rows": height_rows if allow_height_rule else ()}
    if _without_width(ot[index], **filters) != _without_width(nt[index], **filters):
        raise TableError("TARGET_NON_WIDTH_CONTENT_CHANGED")
    # Replace the same target table in both trees and compare the entire rest of the XML.
    for root, tbl in ((old, ot[index]), (new, nt[index])):
        tbl.getparent().replace(tbl, etree.Element(W + "tbl"))
    if etree.tostring(old, method="c14n") != etree.tostring(new, method="c14n"):
        raise TableError("NON_TARGET_DOC_CHANGED")


def _paging_horizontal_span_only(raw, table_index, info):
    """Narrow exception: valid horizontal spans may use *non-width* paging patches.

    Width optimization remains blocked: spans require a separate constraint solver.
    Vertical merges, omitted cells, malformed grid sums, nested tables, locks,
    signatures, tracked content and unrecognized table roles remain blocked.
    """
    allowed = {"MERGED_OR_OMITTED_CELLS", "NON_RECTANGULAR_OR_MISSING_GRID"}
    reasons = set(info["reasons"])
    if "MERGED_OR_OMITTED_CELLS" not in reasons or not reasons.issubset(allowed):
        return False
    root = _xml(raw)
    table = _tables(root)[table_index]
    if table.xpath(".//w:vMerge | .//w:gridBefore | .//w:gridAfter | .//w:tbl", namespaces=NS):
        return False
    count = len(table.xpath("./w:tblGrid/w:gridCol", namespaces=NS))
    if count < 2:
        return False
    saw_merge = False
    for row in table.xpath("./w:tr", namespaces=NS):
        total = 0
        for cell in row.xpath("./w:tc", namespaces=NS):
            spans = cell.xpath("./w:tcPr/w:gridSpan", namespaces=NS)
            if len(spans) > 1:
                return False
            try:
                span = int(spans[0].get(W + "val")) if spans else 1
            except (ValueError, TypeError):
                return False
            if span <= 0 or span > count:
                return False
            total += span
            saw_merge |= span > 1
        if total != count:
            return False
    return saw_merge


def _allow_paging_only(path, table_index, info, result):
    """Restrict horizontal-merge override to operation-specific safe proposals."""
    if info["status"] == "SUPPORTED":
        return True
    raw, _, _, _, _ = _package(path)
    if not _paging_horizontal_span_only(raw, table_index, info):
        return False
    result["reasons"] = ["HORIZONTAL_GRIDSPAN_PAGING_ONLY"]
    return True


def propose_header(path, table_index, profile=None):
    """Propose repeating an existing, clearly identified first data-table row.

    This is opt-in. It never adds or changes text and never claims the renderer
    actually repeated the row. It declines manual page breaks and complex tables.
    """
    base = audit(path, profile=profile)
    if not isinstance(table_index, int) or not 0 <= table_index < base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    table = base["tables"][table_index]
    result = {"operation": "SET_REPEAT_HEADER_FIRST_ROW", "policy": POLICY_VERSION,
              "profile": base["profile"], "profile_status": base["profile_status"],
              "profile_rules_applied": base["profile_rules_applied"],
              "input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": table["table_sha256"], "decision": "REVIEW_REQUIRED",
              "reasons": list(table["reasons"]), "evidence": "SOURCE_XML",
              "word_render": "NOT_RUN", "content_modified": False}
    if not _allow_paging_only(path, table_index, table, result):
        return result
    raw, _, _, _, _ = _package(path)
    target = _tables(_xml(raw))[table_index]
    if target.xpath(".//w:br[@w:type='page'] | .//w:lastRenderedPageBreak", namespaces=NS):
        result["reasons"].append("MANUAL_OR_RENDERED_PAGE_BREAK_REVIEW")
        return result
    if table["pagination_diagnostics"]["header_repeat_first_row"]:
        result["decision"] = "NO_OP_VALID"
        result["reasons"].append("FIRST_HEADER_ALREADY_REPEATED")
        return result
    result["decision"] = "PROPOSE_APPLY"
    result["reasons"].append("EXPLICIT_HEADER_REPEAT_FOR_RECOGNIZED_DATA_TABLE")
    return result


def _apply_header(root, index):
    table = _tables(root)[index]
    first = table.find(W + "tr")
    if first is None:
        raise TableError("MISSING_HEADER_ROW")
    rowpr = first.find(W + "trPr")
    if rowpr is None:
        rowpr = etree.Element(W + "trPr")
        first.insert(0, rowpr)
    existing = rowpr.find(W + "tblHeader")
    if existing is not None:
        if existing.get(W + "val", "1") not in ("0", "false", "off"):
            raise TableError("FIRST_HEADER_ALREADY_REPEATED")
        existing.set(W + "val", "1")
        return
    header = etree.Element(W + "tblHeader")
    header.set(W + "val", "1")
    # WordprocessingML row-properties sequence: tblHeader follows trHeight
    # and precedes tblCellSpacing, jc, hidden. Do not reorder other properties.
    later = {W + "tblCellSpacing", W + "jc", W + "hidden", W + "tblHeader"}
    position = next((i for i, child in enumerate(rowpr) if child.tag in later), len(rowpr))
    rowpr.insert(position, header)


def propose_unclip_row_height(path, table_index, profile=None):
    """Explicit, auditable exact-to-atLeast row-height proposal.

    A structural risk mitigation, NOT proof of clipping or improved pages.
    Other paragraph line spacing and row split properties are untouched.
    """
    base = audit(path, profile=profile)
    if not isinstance(table_index, int) or not 0 <= table_index < base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    table = base["tables"][table_index]
    result = {"operation": "EXACT_ROW_HEIGHT_TO_AT_LEAST", "policy": POLICY_VERSION,
              "profile": base["profile"], "profile_status": base["profile_status"],
              "profile_rules_applied": base["profile_rules_applied"],
              "input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": table["table_sha256"], "decision": "REVIEW_REQUIRED",
              "reasons": list(table["reasons"]), "evidence": "SOURCE_XML",
              "word_render": "NOT_RUN", "content_modified": False, "row_indices": []}
    if not _allow_paging_only(path, table_index, table, result):
        return result
    raw, _, _, _, _ = _package(path)
    tbl = _tables(_xml(raw))[table_index]
    rows = tbl.xpath("./w:tr", namespaces=NS)
    for ri, row in enumerate(rows):
        height = row.xpath("./w:trPr/w:trHeight[@w:hRule='exact']", namespaces=NS)
        if len(height) > 1:
            result["reasons"].append("AMBIGUOUS_ROW_HEIGHT_PROPERTIES")
            return result
        if height:
            try:
                val = int(height[0].get(W + "val"))
                if val <= 0:
                    raise ValueError("invalid")
            except (TypeError, ValueError):
                result["reasons"].append("INVALID_EXACT_ROW_HEIGHT")
                return result
            result["row_indices"].append(ri)
    if not result["row_indices"]:
        result["decision"] = "NO_OP_VALID"
        result["reasons"].append("NO_EXACT_ROW_HEIGHT_FOUND")
    else:
        result["decision"] = "PROPOSE_APPLY"
        result["reasons"].append("EXPLICIT_ROW_HEIGHT_RELAXATION")
    return result


def _apply_unclip_row_heights(root, index, row_indices):
    rows = _tables(root)[index].xpath("./w:tr", namespaces=NS)
    for ri in row_indices:
        matches = rows[ri].xpath("./w:trPr/w:trHeight[@w:hRule='exact']", namespaces=NS)
        if len(matches) != 1:
            raise TableError("EXACT_ROW_HEIGHT_CHANGED")
        matches[0].set(W + "hRule", "atLeast")


def _publish_new_file(temp_path, destination):
    # os.replace() would clobber a path created after the initial existence
    # check. A same-directory hard link publishes the validated file atomically
    # and fails if any process created the destination in the meantime.
    try:
        os.link(temp_path, destination)
    except FileExistsError as exc:
        raise TableError("OUTPUT_MUST_BE_NEW_PATH") from exc
    os.unlink(temp_path)


def apply(path, proposal, output, font_regular=None, font_bold=None, profile=None):
    src = Path(path)
    dst = Path(output)
    if src.resolve() == dst.resolve() or dst.exists():
        raise TableError("OUTPUT_MUST_BE_NEW_PATH")
    if not isinstance(proposal, dict) or proposal.get("decision") != "PROPOSE_APPLY":
        raise TableError("PROPOSAL_NOT_APPLICABLE")
    selected_profile = proposal.get("profile") if profile is None else profile
    profile_context = _profile_context(selected_profile)
    if "profile" in proposal and proposal["profile"] != selected_profile:
        raise TableError("STALE_OR_MODIFIED_PROPOSAL")
    operation = proposal.get("operation") or "OPTIMIZE_WIDTH"
    if operation not in ("OPTIMIZE_WIDTH", "SET_REPEAT_HEADER_FIRST_ROW", "EXACT_ROW_HEIGHT_TO_AT_LEAST"):
        raise TableError("UNSUPPORTED_PROPOSAL_OPERATION")
    header_operation = operation == "SET_REPEAT_HEADER_FIRST_ROW"
    height_operation = operation == "EXACT_ROW_HEIGHT_TO_AT_LEAST"
    if header_operation:
        actual = propose_header(src, proposal.get("table_index"), profile=selected_profile)
    elif height_operation:
        actual = propose_unclip_row_height(src, proposal.get("table_index"), profile=selected_profile)
    else:
        actual = propose(src, proposal.get("table_index"), font_regular, font_bold,
                         profile=selected_profile)
    compare = ("input_sha256", "table_sha256", "table_index", "policy", "decision", "reasons")
    if header_operation:
        compare += ("operation",)
    elif height_operation:
        compare += ("operation", "row_indices")
    else:
        compare += ("candidate_twips",)
    if "profile" in proposal:
        compare += ("profile", "profile_status", "profile_rules_applied")
        if not header_operation and not height_operation and selected_profile is not None:
            compare += ("profile_constraints",)
    if any(actual.get(k) != proposal.get(k) for k in compare):
        raise TableError("STALE_OR_MODIFIED_PROPOSAL")
    raw, settings, names, _, _ = _package(src)
    old_root = _xml(raw)
    new_root = copy.deepcopy(old_root)
    if header_operation:
        _apply_header(new_root, actual["table_index"])
    elif height_operation:
        _apply_unclip_row_heights(new_root, actual["table_index"], actual["row_indices"])
    else:
        _apply_widths(new_root, actual["table_index"], actual["candidate_twips"])
    new_raw = etree.tostring(new_root, xml_declaration=True, encoding="UTF-8", standalone=True)
    _assert_safe(raw, new_raw, actual["table_index"],
                 allow_first_row_header=header_operation, allow_height_rule=height_operation,
                 height_rows=tuple(actual["row_indices"]) if height_operation else ())
    dst.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(suffix=".docx", prefix=".chuanhoabang-", dir=str(dst.parent))
    os.close(fd)
    try:
        with ZipFile(src, "r") as zin, ZipFile(temp_path, "w") as zout:
            for entry in zin.infolist():
                data = new_raw if entry.filename == "word/document.xml" else zin.read(entry.filename)
                zout.writestr(entry, data)
        out_raw, out_settings, out_names, _, _ = _package(temp_path)
        if names != out_names or settings != out_settings:
            raise TableError("OPC_PACKAGE_CHANGED")
        _assert_safe(raw, out_raw, actual["table_index"],
                     allow_first_row_header=header_operation, allow_height_rule=height_operation,
                     height_rows=tuple(actual["row_indices"]) if height_operation else ())
        with ZipFile(src) as zi, ZipFile(temp_path) as zo:
            if any(zi.read(name) != zo.read(name) for name in names if name != "word/document.xml"):
                raise TableError("NON_DOCUMENT_PART_CHANGED")
        _publish_new_file(temp_path, dst)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
    return {"decision": "APPLIED", "output": str(dst), "output_sha256": digest(dst.read_bytes()),
            "input_sha256": actual["input_sha256"],
            **profile_context,
            **({"profile_constraints": actual["profile_constraints"]}
               if "profile_constraints" in actual else {}),
            "operation": operation,
            "changed_properties": (["tblHeader"] if header_operation else ["trHeight.hRule"]
                                   if height_operation else ["tblGrid", "tblW", "tblLayout", "tcW"]),
            "content_integrity": "PASS", "non_target_package_parts": "PASS", "word_render": "NOT_RUN",
            "width_proposal_evidence": actual["evidence"], "table_index": actual["table_index"]}
