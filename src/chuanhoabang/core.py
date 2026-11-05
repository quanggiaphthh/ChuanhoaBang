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
import re
import tempfile
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from lxml import etree

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"
POLICY_VERSION = "V17.5.1/USER-ORIENTATION-001"
MAX_UNCOMPRESSED = 60 * 1024 * 1024
MAX_ENTRY = 25 * 1024 * 1024
MAX_RATIO = 150
HEADER_HINTS = ("stt", "họ tên", "họ và tên", "nội dung", "nhiệm vụ", "đơn vị", "chỉ tiêu",
                "kết quả", "thời gian", "ngày", "số", "kinh phí", "ghi chú", "trách nhiệm",
                "tiến độ", "sản phẩm", "chủ trì", "phối hợp", "tên", "thành tiền")
LAYOUT_HINTS = ("cộng hòa xã hội", "độc lập - tự do", "đảng ủy", "đảng bộ", "nơi nhận", "người ký", "tổng giám đốc")
DANGEROUS_IN_TABLE = [".//w:sdt", ".//w:ins", ".//w:del", ".//w:moveFrom", ".//w:moveTo",
                      ".//w:fldChar", ".//w:instrText", ".//w:drawing", ".//w:pict",
                      ".//w:object", ".//w:altChunk", ".//w:hyperlink",
                      ".//w:trPrChange", ".//w:tcPrChange", ".//w:tblPrChange",
                      ".//w:fldSimple", ".//w:commentReference", ".//w:commentRangeStart",
                      ".//w:commentRangeEnd", ".//w:customXml", ".//w:smartTag",
                      ".//w:subDoc", ".//w:contentPart", ".//w:bookmarkStart",
                      ".//w:bookmarkEnd", ".//w:permStart", ".//w:permEnd"]


class TableError(ValueError):
    """Unsafe or unsupported document/table operation."""


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
            return raw, settings, names
    except (BadZipFile, OSError, RuntimeError) as exc:
        raise TableError("INVALID_OR_UNREADABLE_ZIP") from exc


def _tables(root):
    # Includes body tables inside wrappers; nested ones are reported as unsupported.
    return root.xpath(".//w:body//w:tbl", namespaces=NS)


def _geometry(root):
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
    cols = sect.find(W + "cols")
    try:
        if cols is not None and int(cols.get(W + "num", "1")) != 1:
            return {"status": "GEOMETRY_UNKNOWN", "reason": "MULTICOLUMN_SECTION", "sections": 1}
    except (ValueError, TypeError):
        return {"status": "GEOMETRY_UNKNOWN", "reason": "INVALID_TEXT_COLUMNS", "sections": 1}
    return {"status": "STRUCTURAL", "available_twips": width, "page_width_twips": page_width,
            "orientation": "LANDSCAPE" if page_width > page_height else "PORTRAIT", "sections": 1}


def _protected(settings: bytes, names: list[str], root):
    reasons = []
    if any(n.startswith("_xmlsignatures/") for n in names):
        reasons.append("SIGNED_OPC_PACKAGE")
    if "word/vbaProject.bin" in names:
        reasons.append("MACRO_CONTENT_NOT_SUPPORTED")
    if settings:
        s = _xml(settings)
        p = s.find(".//" + W + "documentProtection")
        if p is not None and p.get(W + "enforcement", "0") in ("1", "true", "on"):
            reasons.append("DOCUMENT_PROTECTED")
        if s.find(".//" + W + "trackRevisions") is not None:
            reasons.append("TRACK_CHANGES_ENABLED")
    if root.xpath(".//w:ins | .//w:del | .//w:moveFrom | .//w:moveTo", namespaces=NS):
        reasons.append("TRACKED_CHANGES_PRESENT")
    return reasons


def _text(cell):
    return " ".join("".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()
                    for p in cell.xpath("./w:p", namespaces=NS)).strip()


def _details(tbl, idx, geom, locks):
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
    if any(x in header_str for x in LAYOUT_HINTS):
        reasons.append("POSSIBLE_LAYOUT_TABLE")
    elif len(rows) < 2 or sum(bool(x) for x in header) < 2 or not any(x in header_str for x in HEADER_HINTS):
        reasons.append("UNCONFIRMED_DATA_TABLE")
    tblpr = tbl.find(W + "tblPr")
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
    return {"index": idx, "status": status, "reasons": sorted(set(reasons)), "rows": len(rows),
            "columns": len(widths), "grid_twips": widths, "header": header,
            "table_sha256": digest(etree.tostring(tbl, method="c14n")),
            "pagination_diagnostics": pagination,
            "overflow_declared": bool(widths and geom.get("available_twips") and
                sum(widths) > geom["available_twips"])}


def audit(path):
    raw, settings, names = _package(path)
    root = _xml(raw)
    geometry = _geometry(root)
    locks = _protected(settings, names, root)
    tables = [_details(tbl, i, geometry, locks) for i, tbl in enumerate(_tables(root))]
    return {"file": str(Path(path)), "input_sha256": digest(Path(path).read_bytes()),
            "policy": POLICY_VERSION, "geometry": geometry, "global_locks": locks,
            "table_count": len(tables), "tables": tables, "word_render": "NOT_RUN"}


def _load_fonts(regular_file, bold_file):
    if not regular_file:
        raise TableError("TNR_FONT_FILE_REQUIRED")
    try:
        from PIL import ImageFont, features
        if not features.check("raqm"):
            raise TableError("LIBRAQM_SHAPING_UNAVAILABLE")
        regular = ImageFont.truetype(str(regular_file), 100, layout_engine=ImageFont.Layout.RAQM)
        if regular.getname()[0].casefold() != "times new roman":
            raise TableError("FONT_IS_NOT_TIMES_NEW_ROMAN")
        bold = None
        if bold_file:
            bold = ImageFont.truetype(str(bold_file), 100, layout_engine=ImageFont.Layout.RAQM)
            if bold.getname()[0].casefold() != "times new roman":
                raise TableError("BOLD_FONT_IS_NOT_TIMES_NEW_ROMAN")
        return regular, bold
    except (OSError, AttributeError) as exc:
        raise TableError("UNREADABLE_TNR_FONT") from exc


def _runs(cell):
    if len(cell.xpath("./w:p", namespaces=NS)) != 1:
        raise TableError("MULTI_PARAGRAPH_CELL_REQUIRES_REVIEW")
    all_runs = cell.xpath("./w:p/w:r", namespaces=NS)
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
        fonts = rpr.find(W + "rFonts") if rpr is not None else None
        size = rpr.find(W + "sz") if rpr is not None else None
        b = rpr.find(W + "b") if rpr is not None else None
        italic = rpr.find(W + "i") if rpr is not None else None
        if fonts is None or size is None or fonts.get(W + "ascii", "").casefold() != "times new roman" or \
            fonts.get(W + "hAnsi", "").casefold() != "times new roman":
            raise TableError("UNRESOLVED_EFFECTIVE_FONT")
        if size.get(W + "val") not in ("26", "28"):
            raise TableError("FONT_SIZE_NOT_13_OR_14")
        if italic is not None and italic.get(W + "val", "1") not in ("0", "false", "off"):
            raise TableError("ITALIC_FACE_NOT_IMPLEMENTED")
        bold = b is not None and b.get(W + "val", "1") not in ("0", "false", "off")
        normalized.append((runtext, int(size.get(W + "val")) / 2, bold))
    if not normalized:
        raise TableError("EMPTY_CELL_REQUIRES_REVIEW")
    return normalized


def _cell_measures(cell, fonts):
    chunks = _runs(cell)
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


def _estimate_lines(chunks, inner_twips):
    if inner_twips < 1:
        return 999999
    count = 1
    used = 0
    for content, pt, face in chunks:
        tokens = re.findall(r"\S+|\s+", content)
        for token in tokens:
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


def propose(path, table_index, font_regular=None, font_bold=None):
    base = audit(path)
    if not isinstance(table_index, int) or table_index < 0 or table_index >= base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    info = base["tables"][table_index]
    result = {"input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": info["table_sha256"], "policy": POLICY_VERSION,
              "baseline_twips": info["grid_twips"], "candidate_twips": None,
              "decision": "REVIEW_REQUIRED", "evidence": "SOURCE_XML", "reasons": list(info["reasons"]),
              "word_render": "NOT_RUN", "content_modified": False}
    if info["status"] != "SUPPORTED":
        return result
    if base["geometry"]["status"] != "STRUCTURAL":
        result["reasons"].append("GEOMETRY_UNKNOWN")
        return result
    try:
        fonts = _load_fonts(font_regular, font_bold)
        tbl = _tables(_xml(_package(path)[0]))[table_index]
        matrix = [[_cell_measures(c, fonts) for c in row.xpath("./w:tc", namespaces=NS)]
                  for row in tbl.xpath("./w:tr", namespaces=NS)]
    except TableError as exc:
        result["reasons"].append(str(exc))
        return result
    padding = 150  # ~2.65mm combined horizontal padding; conservative estimate, not exact effective style.
    current = info["grid_twips"]
    n = len(current)
    usable = base["geometry"]["available_twips"]
    floors = [max(160, max(_width(token, pt, f) for r in matrix for content, pt, f in r[c]
                           for token in (re.findall(r"\S+", content) or [""])) + padding)
              for c in range(n)]
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
        for row in matrix:
            wrapped += max(_estimate_lines(cell, widths[col] - padding) for col, cell in enumerate(row))
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
                         "padding_twips_assumed": padding}
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


def _without_width(tbl, *, allow_first_row_header=False, allow_height_rule=False):
    node = copy.deepcopy(tbl)
    for xp in ("./w:tblGrid", "./w:tblPr/w:tblW", "./w:tblPr/w:tblLayout", ".//w:tcPr/w:tcW"):
        for e in node.xpath(xp, namespaces=NS):
            e.getparent().remove(e)
    if allow_height_rule:
        # Compare all original row height values; only hRule may change.
        for height in node.xpath("./w:tr/w:trPr/w:trHeight", namespaces=NS):
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


def _assert_safe(old_data, new_data, index, *, allow_first_row_header=False, allow_height_rule=False):
    old = _xml(old_data)
    new = _xml(new_data)
    ot, nt = _tables(old), _tables(new)
    if len(ot) != len(nt) or not 0 <= index < len(ot):
        raise TableError("TABLE_INVENTORY_CHANGED")
    if _without_width(ot[index], allow_first_row_header=allow_first_row_header,
                      allow_height_rule=allow_height_rule) != \
            _without_width(nt[index], allow_first_row_header=allow_first_row_header,
                           allow_height_rule=allow_height_rule):
        raise TableError("TARGET_NON_WIDTH_CONTENT_CHANGED")
    # Replace the same target table in both trees and compare the entire rest of the XML.
    for root, tbl in ((old, ot[index]), (new, nt[index])):
        tbl.getparent().replace(tbl, etree.Element(W + "tbl"))
    if etree.tostring(old, method="c14n") != etree.tostring(new, method="c14n"):
        raise TableError("NON_TARGET_DOC_CHANGED")


def propose_header(path, table_index):
    """Propose repeating an existing, clearly identified first data-table row.

    This is opt-in. It never adds or changes text and never claims the renderer
    actually repeated the row. It declines manual page breaks and complex tables.
    """
    base = audit(path)
    if not isinstance(table_index, int) or not 0 <= table_index < base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    table = base["tables"][table_index]
    result = {"operation": "SET_REPEAT_HEADER_FIRST_ROW", "policy": POLICY_VERSION,
              "input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": table["table_sha256"], "decision": "REVIEW_REQUIRED",
              "reasons": list(table["reasons"]), "evidence": "SOURCE_XML",
              "word_render": "NOT_RUN", "content_modified": False}
    if table["status"] != "SUPPORTED":
        return result
    raw, _, _ = _package(path)
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


def propose_unclip_row_height(path, table_index):
    """Explicit, auditable exact-to-atLeast row-height proposal.

    A structural risk mitigation, NOT proof of clipping or improved pages.
    Other paragraph line spacing and row split properties are untouched.
    """
    base = audit(path)
    if not isinstance(table_index, int) or not 0 <= table_index < base["table_count"]:
        raise TableError("TABLE_INDEX_OUT_OF_RANGE")
    table = base["tables"][table_index]
    result = {"operation": "EXACT_ROW_HEIGHT_TO_AT_LEAST", "policy": POLICY_VERSION,
              "input_sha256": base["input_sha256"], "table_index": table_index,
              "table_sha256": table["table_sha256"], "decision": "REVIEW_REQUIRED",
              "reasons": list(table["reasons"]), "evidence": "SOURCE_XML",
              "word_render": "NOT_RUN", "content_modified": False, "row_indices": []}
    if table["status"] != "SUPPORTED":
        return result
    raw, _, _ = _package(path)
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


def apply(path, proposal, output, font_regular=None, font_bold=None):
    src = Path(path)
    dst = Path(output)
    if src.resolve() == dst.resolve() or dst.exists():
        raise TableError("OUTPUT_MUST_BE_NEW_PATH")
    if not isinstance(proposal, dict) or proposal.get("decision") != "PROPOSE_APPLY":
        raise TableError("PROPOSAL_NOT_APPLICABLE")
    operation = proposal.get("operation") or "OPTIMIZE_WIDTH"
    if operation not in ("OPTIMIZE_WIDTH", "SET_REPEAT_HEADER_FIRST_ROW", "EXACT_ROW_HEIGHT_TO_AT_LEAST"):
        raise TableError("UNSUPPORTED_PROPOSAL_OPERATION")
    header_operation = operation == "SET_REPEAT_HEADER_FIRST_ROW"
    height_operation = operation == "EXACT_ROW_HEIGHT_TO_AT_LEAST"
    if header_operation:
        actual = propose_header(src, proposal.get("table_index"))
    elif height_operation:
        actual = propose_unclip_row_height(src, proposal.get("table_index"))
    else:
        actual = propose(src, proposal.get("table_index"), font_regular, font_bold)
    compare = ("input_sha256", "table_sha256", "table_index", "policy", "decision", "reasons")
    if header_operation:
        compare += ("operation",)
    elif height_operation:
        compare += ("operation", "row_indices")
    else:
        compare += ("candidate_twips",)
    if any(actual.get(k) != proposal.get(k) for k in compare):
        raise TableError("STALE_OR_MODIFIED_PROPOSAL")
    raw, settings, names = _package(src)
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
                 allow_first_row_header=header_operation, allow_height_rule=height_operation)
    dst.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(suffix=".docx", prefix=".chuanhoabang-", dir=str(dst.parent))
    os.close(fd)
    try:
        with ZipFile(src, "r") as zin, ZipFile(temp_path, "w") as zout:
            for entry in zin.infolist():
                data = new_raw if entry.filename == "word/document.xml" else zin.read(entry.filename)
                zout.writestr(entry, data)
        out_raw, out_settings, out_names = _package(temp_path)
        if names != out_names or settings != out_settings:
            raise TableError("OPC_PACKAGE_CHANGED")
        _assert_safe(raw, out_raw, actual["table_index"],
                     allow_first_row_header=header_operation, allow_height_rule=height_operation)
        with ZipFile(src) as zi, ZipFile(temp_path) as zo:
            if any(zi.read(name) != zo.read(name) for name in names if name != "word/document.xml"):
                raise TableError("NON_DOCUMENT_PART_CHANGED")
        os.replace(temp_path, dst)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
    return {"decision": "APPLIED", "output": str(dst), "output_sha256": digest(dst.read_bytes()),
            "input_sha256": actual["input_sha256"],
            "operation": operation,
            "changed_properties": (["tblHeader"] if header_operation else ["trHeight.hRule"]
                                   if height_operation else ["tblGrid", "tblW", "tblLayout", "tcW"]),
            "content_integrity": "PASS", "non_target_package_parts": "PASS", "word_render": "NOT_RUN",
            "width_proposal_evidence": actual["evidence"], "table_index": actual["table_index"]}
