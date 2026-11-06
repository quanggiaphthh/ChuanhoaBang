"""Focused L0/L1 tests. Test-only mock font is NOT TNR acceptance."""
import copy
import json
from pathlib import Path
from zipfile import ZipFile

import pytest
from docx import Document
from docx.shared import Cm, Pt
from lxml import etree

from chuanhoabang import audit, propose, apply, TableError
from chuanhoabang import core


def fixture_docx(tmp_path, *, merged=False, header=True, protected=False, multi_section=False):
    doc = Document()
    row0 = ("STT", "Nội dung", "Ghi chú") if header else ("A", "B", "C")
    table = doc.add_table(rows=3, cols=3)
    table.autofit = False
    for ri, row in enumerate((row0, ("0012", "Công việc rất quan trọng cần thực hiện", "Hoàn thành"),
                              ("0", "Kiểm tra văn bản hành chính", "Đang xử lý"))):
        for ci, txt in enumerate(row):
            cell = table.cell(ri, ci)
            cell.text = ""
            run = cell.paragraphs[0].add_run(txt)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
        # Deliberately skew the column proportions.
    for row in table.rows:
        for ci, width in enumerate((Cm(1.7), Cm(11.6), Cm(1.7))):
            row.cells[ci].width = width
    if merged:
        table.cell(1, 0).merge(table.cell(1, 1))
    if multi_section:
        doc.add_section()
    p = tmp_path / "sample.docx"
    doc.save(p)
    if protected:
        with ZipFile(p) as z:
            data = {i.filename: (i, z.read(i.filename)) for i in z.infolist()}
        settings_info, settings = data["word/settings.xml"]
        root = etree.fromstring(settings)
        etree.SubElement(root, core.W + "documentProtection", {core.W + "enforcement": "1"})
        data["word/settings.xml"] = (settings_info, etree.tostring(root))
        with ZipFile(p, "w") as z:
            for item, content in data.values():
                z.writestr(item, content)
    return p


def replace_docx_parts(path, replacements):
    with ZipFile(path) as source:
        entries = [(item, replacements.get(item.filename, source.read(item.filename)))
                   for item in source.infolist()]
    with ZipFile(path, "w") as target:
        for item, content in entries:
            target.writestr(item, content)


def test_audit_read_only_and_header(tmp_path):
    path = fixture_docx(tmp_path)
    before = path.read_bytes()
    result = audit(path)
    assert result["table_count"] == 1
    assert result["tables"][0]["status"] == "SUPPORTED"
    assert result["geometry"]["orientation"] == "PORTRAIT"
    assert result["word_render"] == "NOT_RUN"
    assert path.read_bytes() == before


def test_audit_reports_direct_table_and_cell_border_declarations(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_pr = table.find(core.W + "tblPr")
    table_borders = etree.SubElement(table_pr, core.W + "tblBorders")
    top = etree.SubElement(table_borders, core.W + "top")
    top.set(core.W + "val", "single")
    top.set(core.W + "sz", "8")
    top.set(core.W + "color", "FF0000")
    inside_h = etree.SubElement(table_borders, core.W + "insideH")
    inside_h.set(core.W + "val", "single")
    first_cell = table.find("./" + core.W + "tr/" + core.W + "tc")
    cell_pr = first_cell.find(core.W + "tcPr")
    cell_borders = etree.SubElement(cell_pr, core.W + "tcBorders")
    left = etree.SubElement(cell_borders, core.W + "left")
    left.set(core.W + "val", "single")
    left.set(core.W + "themeColor", "accent1")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    source_before = path.read_bytes()

    evidence = audit(path)["tables"][0]["border_evidence"]

    assert evidence["status"] == "SOURCE_DECLARATIONS_REPORTED"
    assert evidence["table_borders"] == [
        {"edge": "top", "attributes": {"val": "single", "sz": "8", "color": "FF0000"}},
        {"edge": "insideH", "attributes": {"val": "single"}},
    ]
    assert evidence["cell_borders"] == [{
        "row_index": 0,
        "cell_index": 0,
        "edges": [{"edge": "left", "attributes": {"val": "single", "themeColor": "accent1"}}],
    }]
    assert evidence["style_inheritance"] == "NOT_RESOLVED"
    assert evidence["word_render"] == "NOT_RUN"
    assert path.read_bytes() == source_before


def test_audit_reports_direct_story_table_borders(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    table = doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    borders = etree.SubElement(table._tbl.tblPr, core.W + "tblBorders")
    bottom = etree.SubElement(borders, core.W + "bottom")
    bottom.set(core.W + "val", "nil")
    doc.save(path)

    entry = audit(path)["non_body_story_tables"][0]

    assert entry["table_layout_evidence"]["status"] == "NO_DIRECT_DECLARATION"
    assert entry["border_evidence"]["status"] == "SOURCE_DECLARATIONS_REPORTED"
    assert entry["border_evidence"]["table_borders"] == [
        {"edge": "bottom", "attributes": {"val": "nil"}},
    ]
    assert entry["status"] == "REVIEW_REQUIRED"


def test_audit_reports_direct_table_layout_without_resolving_effective_type(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        root = core._xml(package.read("word/document.xml"))
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    layouts = table.xpath("./w:tblPr/w:tblLayout", namespaces=core.NS)
    if layouts:
        layout = layouts[0]
    else:
        layout = etree.SubElement(table.find(core.W + "tblPr"), core.W + "tblLayout")
    layout.set(core.W + "type", "fixed")
    replace_docx_parts(path, {"word/document.xml": etree.tostring(root)})

    evidence = audit(path)["tables"][0]["table_layout_evidence"]

    assert evidence == {
        "status": "DIRECT_DECLARATION_REPORTED",
        "declared_types": ["fixed"],
        "effective_type": "NOT_RESOLVED",
        "issues": [],
    }
    assert propose(path, 0)["table_layout_evidence"] == evidence


def test_audit_marks_unsupported_border_markup_unresolved(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_pr = table.find(core.W + "tblPr")
    borders = etree.SubElement(table_pr, core.W + "tblBorders")
    unknown_edge = etree.SubElement(borders, core.W + "diagonalInside")
    unknown_edge.set(core.W + "val", "single")
    top = etree.SubElement(borders, core.W + "top")
    top.set(core.W + "custom", "value")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    evidence = audit(path)["tables"][0]["border_evidence"]

    assert evidence["status"] == "UNRESOLVED"
    assert "UNSUPPORTED_BORDER_EDGE:table:diagonalInside" in evidence["issues"]
    assert "UNSUPPORTED_BORDER_ATTRIBUTE:table:top:custom" in evidence["issues"]


def test_audit_marks_non_element_border_nodes_unresolved(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    borders = etree.SubElement(table.find(core.W + "tblPr"), core.W + "tblBorders")
    borders.append(etree.Comment("unexpected metadata inside border declarations"))
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    evidence = audit(path)["tables"][0]["border_evidence"]

    assert evidence["status"] == "UNRESOLVED"
    assert "UNSUPPORTED_BORDER_EDGE:table:NON_ELEMENT_NODE" in evidence["issues"]


def test_audit_rejects_duplicate_table_layout_declarations(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_pr = table.find(core.W + "tblPr")
    for previous in table_pr.findall(core.W + "tblLayout"):
        table_pr.remove(previous)
    for value in ("fixed", "autofit"):
        layout = etree.SubElement(table_pr, core.W + "tblLayout")
        layout.set(core.W + "type", value)
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    table_report = audit(path)["tables"][0]

    assert table_report["table_layout_evidence"]["status"] == "UNRESOLVED"
    assert "DUPLICATE_TBL_LAYOUT_DECLARATION" in table_report["table_layout_evidence"]["issues"]
    assert "UNRESOLVED_TABLE_LAYOUT_DECLARATION" in table_report["reasons"]
    proposal = propose(path, 0)
    assert proposal["decision"] == "REVIEW_REQUIRED"
    assert proposal["table_layout_evidence"] == table_report["table_layout_evidence"]


def test_audit_rejects_unsupported_table_layout_type(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_pr = table.find(core.W + "tblPr")
    for previous in table_pr.findall(core.W + "tblLayout"):
        table_pr.remove(previous)
    layout = etree.SubElement(table_pr, core.W + "tblLayout")
    layout.set(core.W + "type", "auto")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    evidence = audit(path)["tables"][0]["table_layout_evidence"]

    assert evidence["status"] == "UNRESOLVED"
    assert "UNSUPPORTED_TBL_LAYOUT_TYPE:auto" in evidence["issues"]


def test_audit_labels_a_plausible_data_table_as_a_non_authoritative_candidate(tmp_path):
    path = fixture_docx(tmp_path)

    table = audit(path)["tables"][0]
    role = table["role_classification"]

    assert role["classification"] == "DATA_CANDIDATE"
    assert set(role["evidence"]) == {
        "MULTIROW_TABLE", "AT_LEAST_TWO_NONEMPTY_HEADER_CELLS", "RECOGNIZED_HEADER_HINT",
    }
    assert {"stt", "nội dung", "ghi chú"}.issubset(role["matched_markers"])
    assert role["markers_matched"] == len(role["matched_markers"])
    assert role["evidence_level"] == "SOURCE_XML_TEXT_AND_TOPOLOGY"
    assert role["authority"] == "NOT_ESTABLISHED"


def test_audit_labels_official_heading_text_as_a_review_only_form_candidate(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(1, 0).text = "Cộng hòa xã hội chủ nghĩa Việt Nam"
    doc.tables[0].cell(2, 0).text = "Độc lập – Tự do – Hạnh phúc"
    doc.save(path)

    table = audit(path)["tables"][0]

    assert table["role_classification"]["classification"] == "OFFICIAL_FORM_CANDIDATE"
    assert "OFFICIAL_FORM_TEXT_MARKER" in table["role_classification"]["evidence"]
    assert set(table["role_classification"]["matched_markers"]) == {
        "cộng hòa xã hội chủ nghĩa việt nam", "độc lập - tự do - hạnh phúc",
    }
    assert table["role_classification"]["markers_matched"] == 2
    assert table["status"] == "REVIEW_REQUIRED"
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_audit_labels_non_form_layout_text_as_a_layout_candidate(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(2, 2).text = "Nơi nhận: Lưu hồ sơ"
    doc.save(path)

    table = audit(path)["tables"][0]

    assert table["role_classification"]["classification"] == "LAYOUT_CANDIDATE"
    assert table["role_classification"]["evidence"] == ["LAYOUT_TEXT_HINT"]
    assert "nơi nhận" in table["role_classification"]["matched_markers"]
    assert table["status"] == "REVIEW_REQUIRED"


def test_audit_recognizes_common_vietnamese_layout_spelling_variant(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(2, 2).text = "Đảng uỷ Bộ Nội vụ"
    doc.save(path)

    table = audit(path)["tables"][0]

    assert table["role_classification"]["classification"] == "LAYOUT_CANDIDATE"
    assert "đảng uỷ" in table["role_classification"]["matched_markers"]
    assert "POSSIBLE_LAYOUT_TABLE" in table["reasons"]


def test_audit_labels_unclear_table_role_as_unknown(tmp_path):
    path = fixture_docx(tmp_path, header=False)

    table = audit(path)["tables"][0]

    assert table["role_classification"]["classification"] == "UNKNOWN"
    assert table["role_classification"]["authority"] == "NOT_ESTABLISHED"
    assert table["role_classification"]["matched_markers"] == []
    assert table["status"] == "REVIEW_REQUIRED"


def test_party_header_marker_is_an_official_form_candidate_and_forces_review(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(2, 0).text = "ĐẢNG CỘNG SẢN VIỆT NAM"
    doc.save(path)

    table = audit(path)["tables"][0]

    assert table["role_classification"]["classification"] == "OFFICIAL_FORM_CANDIDATE"
    assert "POSSIBLE_LAYOUT_TABLE" in table["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_role_evidence_is_bound_to_header_proposal_and_reported_after_apply(tmp_path):
    path = fixture_docx(tmp_path)
    proposal = core.propose_header(path, 0)
    assert proposal["decision"] == "PROPOSE_APPLY"
    assert proposal["role_classification"]["classification"] == "DATA_CANDIDATE"
    assert proposal["parent_table_id"] is None
    assert proposal["parent_cell_location"] is None

    altered = copy.deepcopy(proposal)
    altered["role_classification"]["classification"] = "OFFICIAL_FORM_CANDIDATE"
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(path, altered, tmp_path / "altered-role.docx")

    altered_marker = copy.deepcopy(proposal)
    altered_marker["role_classification"]["matched_markers"] = []
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(path, altered_marker, tmp_path / "altered-marker.docx")

    altered_scope = copy.deepcopy(proposal)
    altered_scope["parent_table_id"] = "body:9:forged-parent"
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(path, altered_scope, tmp_path / "altered-scope.docx")

    applied = apply(path, proposal, tmp_path / "header-role.docx")
    assert applied["role_classification"]["classification"] == "DATA_CANDIDATE"
    assert applied["parent_table_id"] is None
    assert applied["parent_cell_location"] is None


def test_audit_separates_declared_widths_from_grid_and_word_measurement(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    for column, width in zip(table.xpath("./w:tblGrid/w:gridCol", namespaces=core.NS),
                             (1000, 2000, 500)):
        column.set(core.W + "w", str(width))
    table_width = table.find(core.W + "tblPr/" + core.W + "tblW")
    table_width.set(core.W + "type", "pct")
    table_width.set(core.W + "w", "5000")
    for cell, (kind, value) in zip(table.xpath("./w:tr[1]/w:tc", namespaces=core.NS),
                                   (("dxa", "1000"), ("pct", "2500"), ("auto", "0"))):
        cell_width = cell.find(core.W + "tcPr/" + core.W + "tcW")
        cell_width.set(core.W + "type", kind)
        cell_width.set(core.W + "w", value)
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    width_evidence = audit(path)["tables"][0]["width_evidence"]

    assert width_evidence["grid_sum_twips"] == 3500
    assert width_evidence["table_preferred"] == {
        "status": "DECLARED", "type": "pct", "raw_value": "5000", "twips": None,
    }
    assert width_evidence["cell_preferred"][0] == [
        {"status": "DECLARED", "type": "dxa", "raw_value": "1000", "twips": 1000},
        {"status": "DECLARED", "type": "pct", "raw_value": "2500", "twips": None},
        {"status": "DECLARED", "type": "auto", "raw_value": "0", "twips": None},
    ]
    assert width_evidence["word_rendered"] == "NOT_RUN"


def test_audit_fails_closed_on_invalid_preferred_width_declarations(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_width = table.find(core.W + "tblPr/" + core.W + "tblW")
    table_width.set(core.W + "type", "dxa")
    table_width.set(core.W + "w", "not-a-width")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    table_report = audit(path)["tables"][0]

    assert table_report["status"] == "REVIEW_REQUIRED"
    assert "INVALID_PREFERRED_WIDTH_DECLARATION" in table_report["reasons"]
    assert table_report["width_evidence"]["table_preferred"] == {
        "status": "INVALID", "type": "dxa", "raw_value": "not-a-width", "twips": None,
    }


def test_audit_fails_closed_on_invalid_cell_width_declarations(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    cell_width = table.find("./" + core.W + "tr/" + core.W + "tc/" +
                            core.W + "tcPr/" + core.W + "tcW")
    cell_width.set(core.W + "type", "percent")
    cell_width.set(core.W + "w", "5000")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    table_report = audit(path)["tables"][0]

    assert table_report["status"] == "REVIEW_REQUIRED"
    assert "INVALID_PREFERRED_WIDTH_DECLARATION" in table_report["reasons"]
    assert table_report["width_evidence"]["cell_preferred"][0][0] == {
        "status": "INVALID", "type": "percent", "raw_value": "5000", "twips": None,
    }


def test_oversized_compressed_docx_is_rejected_before_archive_read(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    assert core.MAX_COMPRESSED_DOCX_BYTES == 64 * 1024 * 1024
    monkeypatch.setattr(core, "MAX_COMPRESSED_DOCX_BYTES", path.stat().st_size - 1, raising=False)
    monkeypatch.setattr(core, "ZipFile", lambda *_args, **_kwargs: pytest.fail("ZIP opened before size guard"))

    with pytest.raises(TableError, match="COMPRESSED_DOCX_SIZE_LIMIT"):
        audit(path)


def test_unknown_data_table_review(tmp_path):
    path = fixture_docx(tmp_path, header=False)
    result = audit(path)
    assert "UNCONFIRMED_DATA_TABLE" in result["tables"][0]["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_layout_marker_anywhere_in_table_forces_review(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(2, 2).text = "Nơi nhận: Lưu hồ sơ"
    doc.save(path)

    table = audit(path)["tables"][0]
    assert table["status"] == "REVIEW_REQUIRED"
    assert "POSSIBLE_LAYOUT_TABLE" in table["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


@pytest.mark.parametrize("marker", [
    "Độc lập – Tự do – Hạnh phúc",
    "Độc lập — Tự do — Hạnh phúc",
])
def test_official_slogan_with_typographic_dashes_forces_review(tmp_path, marker):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].cell(2, 2).text = marker
    doc.save(path)

    table = audit(path)["tables"][0]
    assert table["status"] == "REVIEW_REQUIRED"
    assert "POSSIBLE_LAYOUT_TABLE" in table["reasons"]


@pytest.mark.parametrize("story_name", ["header", "footer"])
def test_audit_reports_story_tables_without_body_indices(tmp_path, story_name):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    story = getattr(doc.sections[0], story_name)
    table = story.add_table(rows=1, cols=1, width=Cm(10))
    table.cell(0, 0).text = "Không chỉnh sửa ngoài phần nội dung"
    doc.save(path)
    source_before = path.read_bytes()

    report = audit(path)

    assert report["table_count"] == 1
    assert report["tables"][0]["index"] == 0
    assert report["non_body_story_table_count"] == 1
    entry = report["non_body_story_tables"][0]
    assert entry["part"] == f"word/{story_name}1.xml"
    assert entry["story_table_index"] == 0
    assert len(entry["table_sha256"]) == 64
    assert entry["owner_status"] == "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED"
    assert entry["section_references"] == [{
        "section_index": 0,
        "story_type": story_name,
        "reference_type": "default",
    }]
    assert entry["status"] == "REVIEW_REQUIRED"
    assert entry["reason"] == "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX"
    assert entry["role_classification"]["classification"] == "UNKNOWN"
    assert entry["role_classification"]["authority"] == "NOT_ESTABLISHED"
    assert path.read_bytes() == source_before


@pytest.mark.parametrize("story_name", ["header", "footer"])
def test_non_body_story_role_candidate_is_reported_without_edit_permission(tmp_path, story_name):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    story = getattr(doc.sections[0], story_name)
    table = story.add_table(rows=2, cols=3, width=Cm(15))
    for cell, value in zip(table.rows[0].cells, ("STT", "Nội dung", "Ghi chú")):
        cell.text = value
    for cell, value in zip(table.rows[1].cells, ("01", "Công việc", "Hoàn thành")):
        cell.text = value
    table.cell(1, 2).text = "Cộng hòa xã hội chủ nghĩa Việt Nam"
    doc.save(path)

    entry = audit(path)["non_body_story_tables"][0]

    assert entry["role_classification"]["classification"] == "OFFICIAL_FORM_CANDIDATE"
    assert "OFFICIAL_FORM_TEXT_MARKER" in entry["role_classification"]["evidence"]
    assert "cộng hòa xã hội chủ nghĩa việt nam" in entry["role_classification"]["matched_markers"]
    assert entry["role_classification"]["authority"] == "NOT_ESTABLISHED"
    assert entry["status"] == "REVIEW_REQUIRED"
    assert entry["reason"] == "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX"


def test_unreferenced_story_part_has_unresolved_owner(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    with ZipFile(path) as source_zip:
        entries = [(info, source_zip.read(info.filename)) for info in source_zip.infolist()]
    with ZipFile(path, "w") as target_zip:
        for info, data in entries:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                reference = root.xpath(".//w:sectPr/w:headerReference", namespaces=core.NS)[0]
                reference.getparent().remove(reference)
                data = etree.tostring(root, xml_declaration=True, encoding="UTF-8")
            target_zip.writestr(info, data)

    entry = audit(path)["non_body_story_tables"][0]
    assert entry["part"] == "word/header1.xml"
    assert entry["owner_status"] == "SECTION_RELATIONSHIP_NOT_RESOLVED"
    assert entry["section_references"] == []


@pytest.mark.parametrize("story_name", ["header", "footer"])
def test_custom_named_related_story_part_is_inventoried_read_only(tmp_path, story_name):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    story = getattr(doc.sections[0], story_name)
    story.add_table(rows=1, cols=1, width=Cm(10)).cell(0, 0).text = "Custom story table"
    doc.save(path)

    with ZipFile(path) as source_zip:
        entries = {item.filename: source_zip.read(item.filename) for item in source_zip.infolist()}
    original_part = f"word/{story_name}1.xml"
    custom_part = f"word/stories/custom-{story_name}.xml"
    entries[custom_part] = entries.pop(original_part)

    rels = core._xml(entries["word/_rels/document.xml.rels"])
    relationship = next(
        rel for rel in rels.xpath("./rel:Relationship", namespaces=core.REL_NS)
        if rel.get("Type", "").endswith(f"/{story_name}")
    )
    relationship.set("Target", f"stories/custom-{story_name}.xml")
    entries["word/_rels/document.xml.rels"] = etree.tostring(
        rels, xml_declaration=True, encoding="UTF-8"
    )

    content_types = core._xml(entries["[Content_Types].xml"])
    override = content_types.xpath(
        "./*[local-name()='Override' and @PartName=$name]", name=f"/{original_part}"
    )[0]
    override.set("PartName", f"/{custom_part}")
    entries["[Content_Types].xml"] = etree.tostring(
        content_types, xml_declaration=True, encoding="UTF-8"
    )
    with ZipFile(path, "w") as target_zip:
        for name, data in entries.items():
            target_zip.writestr(name, data)
    source_before = path.read_bytes()

    report = audit(path)

    assert report["non_body_story_tables"][0]["part"] == custom_part
    assert report["non_body_story_tables"][0]["section_references"] == [{
        "section_index": 0,
        "story_type": story_name,
        "reference_type": "default",
    }]
    assert report["non_body_story_tables"][0]["status"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == source_before


def test_malformed_internal_relationship_target_is_unresolved():
    assert core._relationship_target_part("//[") is None


@pytest.mark.parametrize(
    "story_type,body_reference_count,duplicate_id,note_id_value,has_container,expected_status",
    [
        ("footnotes", 1, False, "1", True, "BODY_REFERENCE_FOUND"),
        ("footnotes", 2, False, "1", True, "BODY_REFERENCE_FOUND"),
        ("endnotes", 1, False, "1", True, "BODY_REFERENCE_FOUND"),
        ("footnotes", 0, False, "1", True, "NO_BODY_REFERENCE_FOUND"),
        ("footnotes", 1, True, "1", True, "AMBIGUOUS_NOTE_ID"),
        ("footnotes", 1, False, "not-an-id", True, "UNKNOWN_NOTE_ID"),
        ("footnotes", 1, False, "1", False, "NOTE_CONTAINER_MISSING"),
    ],
)
def test_custom_named_note_part_is_inventoried_read_only(
        tmp_path, story_type, body_reference_count, duplicate_id, note_id_value, has_container,
        expected_status):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as source_zip:
        entries = {item.filename: source_zip.read(item.filename) for item in source_zip.infolist()}

    document = core._xml(entries["word/document.xml"])
    table = copy.deepcopy(document.xpath("./w:body/w:tbl", namespaces=core.NS)[0])
    story_root = etree.Element(core.W + story_type, nsmap={"w": core.NS["w"]})
    note_tag = "footnote" if story_type == "footnotes" else "endnote"
    etree.SubElement(story_root, core.W + note_tag, {
        core.W + "id": "-1", core.W + "type": "separator",
    })
    etree.SubElement(story_root, core.W + note_tag, {
        core.W + "id": "0", core.W + "type": "continuationSeparator",
    })
    if has_container:
        note_attributes = {core.W + "id": note_id_value}
        note = etree.SubElement(story_root, core.W + note_tag, note_attributes)
        note.append(table)
        if duplicate_id:
            duplicate = etree.SubElement(story_root, core.W + note_tag,
                                         {core.W + "id": note_id_value})
            etree.SubElement(duplicate, core.W + "p")
    else:
        story_root.append(table)
    if body_reference_count:
        body = document.find(core.W + "body")
        body_paragraph = etree.Element(core.W + "p")
        section_properties = body.find(core.W + "sectPr")
        if section_properties is None:
            body.append(body_paragraph)
        else:
            body.insert(body.index(section_properties), body_paragraph)
        for _ in range(body_reference_count):
            run = etree.SubElement(body_paragraph, core.W + "r")
            etree.SubElement(run, core.W + ("footnoteReference" if story_type == "footnotes"
                                             else "endnoteReference"),
                             {core.W + "id": "1"})
        entries["word/document.xml"] = etree.tostring(
            document, xml_declaration=True, encoding="UTF-8"
        )
    custom_part = f"word/stories/custom-{story_type}.xml"
    entries[custom_part] = etree.tostring(story_root, xml_declaration=True, encoding="UTF-8")

    relationship_root = core._xml(entries["word/_rels/document.xml.rels"])
    relationship_root.append(etree.Element(
        "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship",
        {
            "Id": f"rIdCustom{story_type.title()}",
            "Type": f"http://schemas.openxmlformats.org/officeDocument/2006/relationships/{story_type}",
            "Target": f"stories/custom-{story_type}.xml",
        },
    ))
    entries["word/_rels/document.xml.rels"] = etree.tostring(
        relationship_root, xml_declaration=True, encoding="UTF-8"
    )

    content_types = core._xml(entries["[Content_Types].xml"])
    etree.SubElement(
        content_types,
        "{http://schemas.openxmlformats.org/package/2006/content-types}Override",
        {
            "PartName": f"/{custom_part}",
            "ContentType": f"application/vnd.openxmlformats-officedocument.wordprocessingml.{story_type}+xml",
        },
    )
    entries["[Content_Types].xml"] = etree.tostring(
        content_types, xml_declaration=True, encoding="UTF-8"
    )
    with ZipFile(path, "w") as target_zip:
        for name, data in entries.items():
            target_zip.writestr(name, data)
    source_before = path.read_bytes()

    report = audit(path)
    notes = [item for item in report["non_body_story_tables"] if item["part"] == custom_part]

    assert len(notes) == 1
    assert notes[0]["story_types"] == [story_type]
    assert notes[0]["section_references"] == []
    assert notes[0]["status"] == "REVIEW_REQUIRED"
    assert notes[0]["reason"] == "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX"
    expected_note_id = note_id_value if has_container else None
    expected_reference_count = (
        body_reference_count if has_container and note_id_value == "1" else None
    )
    assert notes[0]["note_reference"] == {
        "note_type": "footnote" if story_type == "footnotes" else "endnote",
        "note_id": expected_note_id,
        "status": expected_status,
        "body_reference_count": expected_reference_count,
        "reference_scope": "WORD_DOCUMENT_BODY_XML_ONLY",
        "evidence": "SOURCE_XML_ONLY",
    }
    assert path.read_bytes() == source_before


def test_ambiguous_document_relationship_id_does_not_assign_story_owner(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    with ZipFile(path) as source_zip:
        entries = [(info, source_zip.read(info.filename)) for info in source_zip.infolist()]
    with ZipFile(path, "w") as target_zip:
        for info, data in entries:
            if info.filename == "word/_rels/document.xml.rels":
                root = core._xml(data)
                header_rel = root.xpath(
                    "./rel:Relationship[substring(@Type, string-length(@Type) - 5) = 'header']",
                    namespaces=core.REL_NS,
                )[0]
                duplicate = etree.Element(header_rel.tag, header_rel.attrib)
                duplicate.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer")
                duplicate.set("Target", "footer-missing.xml")
                root.append(duplicate)
                data = etree.tostring(root, xml_declaration=True, encoding="UTF-8")
            target_zip.writestr(info, data)

    entry = audit(path)["non_body_story_tables"][0]
    assert entry["owner_status"] == "SECTION_RELATIONSHIP_NOT_RESOLVED"
    assert entry["section_references"] == []


def test_unknown_relationship_target_mode_does_not_assign_story_owner(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    with ZipFile(path) as source_zip:
        entries = [(item, source_zip.read(item.filename)) for item in source_zip.infolist()]
    with ZipFile(path, "w") as target_zip:
        for item, data in entries:
            if item.filename == "word/_rels/document.xml.rels":
                root = core._xml(data)
                header_rel = next(
                    rel for rel in root.xpath("./rel:Relationship", namespaces=core.REL_NS)
                    if rel.get("Type", "").endswith("/header")
                )
                header_rel.set("TargetMode", "Unexpected")
                data = etree.tostring(root, xml_declaration=True, encoding="UTF-8")
            target_zip.writestr(item, data)

    entry = audit(path)["non_body_story_tables"][0]

    assert entry["owner_status"] == "SECTION_RELATIONSHIP_NOT_RESOLVED"
    assert entry["section_references"] == []


def test_multiple_sections_map_direct_story_references_to_correct_owner(tmp_path):
    from docx.enum.section import WD_SECTION

    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.sections[1].header.is_linked_to_previous = False
    doc.sections[1].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)

    report = audit(path)

    assert report["table_count"] == 1
    assert [(entry["part"], entry["section_references"]) for entry in report["non_body_story_tables"]] == [
        ("word/header1.xml", [{"section_index": 0, "story_type": "header", "reference_type": "default"}]),
        ("word/header2.xml", [{"section_index": 1, "story_type": "header", "reference_type": "default"}]),
    ]


@pytest.mark.parametrize("story_name", ["header", "footer"])
def test_linked_default_story_reports_inheritance_candidate_until_overridden(tmp_path, story_name):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    getattr(doc.sections[0], story_name).add_table(rows=1, cols=1, width=Cm(10))
    doc.add_section()
    doc.add_section()
    getattr(doc.sections[2], story_name).is_linked_to_previous = False
    getattr(doc.sections[2], story_name).add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    source_before = path.read_bytes()

    report = audit(path)
    stories = {entry["part"]: entry for entry in report["non_body_story_tables"]
               if entry["part"].startswith(f"word/{story_name}")}
    first_part, second_part = f"word/{story_name}1.xml", f"word/{story_name}2.xml"

    assert stories[first_part]["section_references"] == [
        {"section_index": 0, "story_type": story_name, "reference_type": "default"},
    ]
    assert stories[first_part]["default_inheritance_candidates"] == [
        {"section_index": 1, "story_type": story_name, "reference_type": "default",
         "inherited_from_section_index": 0},
    ]
    assert stories[first_part]["owner_status"] == \
        "DIRECT_AND_INHERITED_DEFAULT_CANDIDATES"
    assert stories[second_part]["section_references"] == [
        {"section_index": 2, "story_type": story_name, "reference_type": "default"},
    ]
    assert stories[second_part]["default_inheritance_candidates"] == []
    assert all(entry["status"] == "REVIEW_REQUIRED" for entry in stories.values())
    from chuanhoabang.cli import render_markdown
    markdown = render_markdown(report)
    assert f"possible inherited section 1 {story_name}/default from section 0" in markdown
    assert path.read_bytes() == source_before


def test_first_page_header_is_not_a_default_inheritance_candidate(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    section = doc.sections[0]
    section.different_first_page_header_footer = True
    section.first_page_header.add_table(rows=1, cols=1, width=Cm(10))
    doc.add_section()
    doc.save(path)
    with ZipFile(path) as package:
        document_xml = package.read("word/document.xml")
    document_root = core._xml(document_xml)
    sections = document_root.xpath(
        ".//w:body/w:sectPr | .//w:body//w:pPr/w:sectPr", namespaces=core.NS
    )
    assert len(sections) == 2
    for title_page in sections[1].xpath("./w:titlePg", namespaces=core.NS):
        sections[1].remove(title_page)
    replace_docx_parts(path, {"word/document.xml": etree.tostring(document_root)})
    source_before = path.read_bytes()

    report = audit(path)
    first_page = next(
        entry for entry in report["non_body_story_tables"]
        if any(reference["reference_type"] == "first"
               for reference in entry["section_references"])
    )

    assert first_page["section_references"] == [
        {"section_index": 0, "story_type": "header", "reference_type": "first",
         "activation": {"status": "ENABLED", "control": "w:titlePg",
                        "evidence": "SOURCE_XML_ONLY"}},
    ]
    assert first_page["default_inheritance_candidates"] == []
    assert first_page["first_even_inheritance_candidates"] == []
    assert first_page["status"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == source_before


def test_first_page_header_reports_disabled_source_activation_without_title_page_control(tmp_path):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    section = doc.sections[0]
    section.different_first_page_header_footer = True
    section.first_page_header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    with ZipFile(path) as package:
        document_xml = package.read("word/document.xml")
    root = core._xml(document_xml)
    title_page = root.xpath(".//w:sectPr/w:titlePg", namespaces=core.NS)
    assert len(title_page) == 1
    title_page[0].getparent().remove(title_page[0])
    replace_docx_parts(path, {"word/document.xml": etree.tostring(root)})
    source_before = path.read_bytes()

    report = audit(path)
    first_page = next(
        entry for entry in report["non_body_story_tables"]
        if any(reference["reference_type"] == "first"
               for reference in entry["section_references"])
    )

    assert first_page["section_references"][0]["activation"] == {
        "status": "DISABLED", "control": "w:titlePg", "evidence": "SOURCE_XML_ONLY",
    }
    assert first_page["default_inheritance_candidates"] == []
    assert path.read_bytes() == source_before


@pytest.mark.parametrize(
    ("control_mode", "expected_status"),
    [("missing", "DISABLED"), ("off", "DISABLED"), ("on", "ENABLED"),
     ("invalid", "UNKNOWN"), ("duplicate", "UNKNOWN")],
)
def test_even_header_reports_source_activation_state(tmp_path, control_mode, expected_status):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    doc.save(path)
    with ZipFile(path) as package:
        document_xml = package.read("word/document.xml")
        settings_xml = package.read("word/settings.xml")
    document_root = core._xml(document_xml)
    reference = document_root.xpath(".//w:sectPr/w:headerReference", namespaces=core.NS)[0]
    reference.set(core.W + "type", "even")
    settings_root = core._xml(settings_xml)
    controls = settings_root.xpath("./w:evenAndOddHeaders", namespaces=core.NS)
    for control in controls:
        settings_root.remove(control)
    if control_mode != "missing":
        value = {"off": "0", "on": "1", "invalid": "sometimes"}.get(control_mode)
        etree.SubElement(settings_root, core.W + "evenAndOddHeaders",
                         {} if value is None else {core.W + "val": value})
        if control_mode == "duplicate":
            etree.SubElement(settings_root, core.W + "evenAndOddHeaders", {core.W + "val": "1"})
    replace_docx_parts(path, {
        "word/document.xml": etree.tostring(document_root),
        "word/settings.xml": etree.tostring(settings_root),
    })
    source_before = path.read_bytes()

    report = audit(path)
    even_page = next(
        entry for entry in report["non_body_story_tables"]
        if any(reference["reference_type"] == "even"
               for reference in entry["section_references"])
    )

    assert even_page["section_references"][0]["activation"] == {
        "status": expected_status, "control": "w:evenAndOddHeaders",
        "evidence": "SOURCE_XML_ONLY",
    }
    assert even_page["default_inheritance_candidates"] == []
    assert even_page["status"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == source_before


@pytest.mark.parametrize(
    ("story_name", "reference_type"),
    [("header", "first"), ("footer", "first"),
     ("header", "even"), ("footer", "even")],
)
def test_active_first_even_references_report_possible_inheritance(tmp_path, story_name,
                                                                  reference_type):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    section = doc.sections[0]
    if reference_type == "first":
        section.different_first_page_header_footer = True
        story = getattr(section, f"first_page_{story_name}")
    else:
        story = getattr(section, story_name)
    story.add_table(rows=1, cols=1, width=Cm(10))
    doc.add_section()
    if reference_type == "first":
        doc.sections[1].different_first_page_header_footer = True
    doc.save(path)

    with ZipFile(path) as package:
        document_xml = package.read("word/document.xml")
        settings_xml = package.read("word/settings.xml")
    document_root = core._xml(document_xml)
    sections = document_root.xpath(
        ".//w:body/w:sectPr | .//w:body//w:pPr/w:sectPr", namespaces=core.NS
    )
    assert len(sections) == 2
    source_section, target_section = sections
    if reference_type == "even":
        default_reference = source_section.xpath(
            f"./w:{story_name}Reference[@w:type='default']", namespaces=core.NS
        )
        assert len(default_reference) == 1
        default_reference[0].set(core.W + "type", "even")
    source_reference = source_section.xpath(
        f"./w:{story_name}Reference[@w:type='{reference_type}']", namespaces=core.NS
    )
    assert len(source_reference) == 1
    for reference in target_section.xpath(
        f"./w:{story_name}Reference[@w:type='{reference_type}']", namespaces=core.NS
    ):
        target_section.remove(reference)
    settings_root = core._xml(settings_xml)
    if reference_type == "even":
        controls = settings_root.xpath("./w:evenAndOddHeaders", namespaces=core.NS)
        for control in controls:
            settings_root.remove(control)
        etree.SubElement(settings_root, core.W + "evenAndOddHeaders", {core.W + "val": "1"})
    replace_docx_parts(path, {
        "word/document.xml": etree.tostring(document_root),
        "word/settings.xml": etree.tostring(settings_root),
    })
    source_before = path.read_bytes()

    report = audit(path)
    part = f"word/{story_name}1.xml"
    entry = next(item for item in report["non_body_story_tables"] if item["part"] == part)
    control = "w:titlePg" if reference_type == "first" else "w:evenAndOddHeaders"
    activation = {"status": "ENABLED", "control": control, "evidence": "SOURCE_XML_ONLY"}

    assert entry["section_references"] == [{
        "section_index": 0, "story_type": story_name,
        "reference_type": reference_type, "activation": activation,
    }]
    assert entry["default_inheritance_candidates"] == []
    assert entry["first_even_inheritance_candidates"] == [{
        "section_index": 1, "story_type": story_name,
        "reference_type": reference_type, "inherited_from_section_index": 0,
        "activation": activation,
    }]
    assert entry["owner_status"] == "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED"
    assert entry["status"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == source_before


@pytest.mark.parametrize("scope", ["body", "header"])
def test_table_inventory_ids_and_parent_links_are_stable_and_read_only(tmp_path, scope):
    path = fixture_docx(tmp_path)
    doc = Document(path)
    if scope == "body":
        parent = doc.tables[0]
    else:
        parent = doc.sections[0].header.add_table(rows=1, cols=1, width=Cm(10))
    parent.cell(0, 0).add_table(rows=1, cols=1).cell(0, 0).text = "Nested child"
    doc.save(path)
    source_before = path.read_bytes()

    report = audit(path)
    if scope == "body":
        entries = report["tables"]
        parent_id = entries[0]["table_id"]
        assert report["table_count"] == 2
        assert entries[0]["parent_table_id"] is None
        child = entries[1]
        assert child["parent_table_id"] == parent_id
        assert child["parent_cell_location"] == {
            "status": "LOCATED_IN_SOURCE_XML",
            "parent_table_id": parent_id,
            "row_index": 0,
            "cell_index": 0,
            "evidence": "SOURCE_XML_TOPOLOGY",
        }
        assert "CONTAINS_NESTED_TABLE" in entries[0]["reasons"]
        assert "NESTED_OR_CONTENT_CONTROL_TABLE" in child["reasons"]
        assert entries[0]["role_classification"]["classification"] == "NESTED"
        assert child["role_classification"]["classification"] == "NESTED"
        review = core.propose_header(path, 1)
        assert review["decision"] == "REVIEW_REQUIRED"
        assert review["parent_table_id"] == parent_id
        assert review["parent_cell_location"] == child["parent_cell_location"]
    else:
        entries = report["non_body_story_tables"]
        parent_id = entries[0]["table_id"]
        assert [entry["story_table_index"] for entry in entries] == [0, 1]
        assert entries[0]["parent_table_id"] is None
        child = entries[1]
        assert child["parent_table_id"] == parent_id
        assert child["parent_cell_location"] == {
            "status": "LOCATED_IN_SOURCE_XML",
            "parent_table_id": parent_id,
            "row_index": 0,
            "cell_index": 0,
            "evidence": "SOURCE_XML_TOPOLOGY",
        }

    assert len({entry["table_id"] for entry in entries}) == len(entries)
    assert audit(path)["tables" if scope == "body" else "non_body_story_tables"] == entries
    assert path.read_bytes() == source_before


def test_nested_parent_cell_locator_fails_closed_when_source_cell_is_missing():
    parent = etree.Element(core.W + "tbl")
    child = etree.SubElement(parent, core.W + "tbl")

    assert core._parent_cell_location(child, "body:0:parent") == {
        "status": "UNRESOLVED",
        "reason": "PARENT_CELL_NOT_FOUND",
    }


def test_merged_is_not_auto_formatted(tmp_path):
    path = fixture_docx(tmp_path, merged=True)
    result = audit(path)
    assert "MERGED_OR_OMITTED_CELLS" in result["tables"][0]["reasons"]
    assert result["tables"][0]["cell_grid_spans"][1][0] == {
        "start_column": 0, "span": 2,
    }
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_protected_document_blocks(tmp_path):
    path = fixture_docx(tmp_path, protected=True)
    assert "DOCUMENT_PROTECTED" in audit(path)["global_locks"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


@pytest.mark.parametrize(("enforcements", "expected_reason"), [
    (["maybe"], "INVALID_DOCUMENT_PROTECTION_ENFORCEMENT"),
    (["0", "1"], "AMBIGUOUS_DOCUMENT_PROTECTION_SETTINGS"),
])
def test_invalid_or_ambiguous_document_protection_fails_closed(
        tmp_path, enforcements, expected_reason):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, settings_xml = data["word/settings.xml"]
    root = core._xml(settings_xml)
    for enforcement in enforcements:
        etree.SubElement(root, core.W + "documentProtection",
                         {core.W + "enforcement": enforcement})
    data["word/settings.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    report = audit(path)

    assert expected_reason in report["global_locks"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_multi_section_review(tmp_path):
    path = fixture_docx(tmp_path, multi_section=True)
    assert audit(path)["geometry"]["status"] == "GEOMETRY_UNKNOWN"


def test_propose_requires_actual_tnr_font(tmp_path):
    path = fixture_docx(tmp_path)
    result = propose(path, 0)
    assert result["decision"] == "REVIEW_REQUIRED"
    assert "TNR_FONT_FILE_REQUIRED" in result["reasons"]
    assert result["candidate_twips"] is None


@pytest.mark.parametrize("no_break_space", ["\u00a0", "\u180e", "\u2007", "\u202f"])
def test_line_estimate_does_not_break_nonbreaking_spaces(no_break_space):
    class FakeFont:
        def getlength(self, text):
            return len(text)

    face = FakeFont()

    bound_word = f"ab{no_break_space}cd"
    assert core._estimate_lines([(bound_word, 5, face)], 3) == 999999
    assert core._estimate_lines([("ab cd", 5, face)], 3) == 2


def test_width_patch_preserves_whole_document_and_source(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_layout = table.find("./" + core.W + "tblPr/" + core.W + "tblLayout")
    table_layout.set(core.W + "type", "autofit")
    table_borders = etree.SubElement(table.find(core.W + "tblPr"), core.W + "tblBorders")
    top = etree.SubElement(table_borders, core.W + "top")
    top.set(core.W + "val", "single")
    top.set(core.W + "sz", "8")
    top.set(core.W + "color", "0066CC")
    first_cell = table.find("./" + core.W + "tr/" + core.W + "tc")
    cell_borders = etree.SubElement(first_cell.find(core.W + "tcPr"), core.W + "tcBorders")
    left = etree.SubElement(cell_borders, core.W + "left")
    left.set(core.W + "val", "single")
    left.set(core.W + "space", "2")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    source_before = path.read_bytes()
    meta = audit(path)["tables"][0]
    border_evidence = meta["border_evidence"]
    base = meta["grid_twips"]
    candidate = [base[0] + 200, base[1] - 400, base[2] + 200]
    assert min(candidate) > 0
    proposal = {"input_sha256": audit(path)["input_sha256"], "table_sha256": meta["table_sha256"],
                "table_index": 0, "policy": core.POLICY_VERSION, "decision": "PROPOSE_APPLY",
                "candidate_twips": candidate, "evidence": "MOCK_TEST_ONLY",
                "role_classification": meta["role_classification"],
                "table_layout_evidence": meta["table_layout_evidence"]}
    # Isolate the patch/invariant writer from actual font shaping in this test.
    monkeypatch.setattr(core, "propose", lambda *a, **k: proposal)
    source_hash = core.digest(path.read_bytes())
    target = tmp_path / "formatted.docx"
    report = apply(path, proposal, target)
    assert report["decision"] == "APPLIED"
    assert report["content_integrity"] == "PASS"
    assert report["word_render"] == "NOT_RUN"
    assert report["table_layout_evidence"] == meta["table_layout_evidence"]
    assert report["table_layout_evidence"]["declared_types"] == ["autofit"]
    assert "tblLayout" in report["changed_properties"]
    assert path.read_bytes() == source_before
    assert core.digest(path.read_bytes()) == source_hash
    original = Document(path)
    result = Document(target)
    before = [[c.text for c in r.cells] for r in original.tables[0].rows]
    after = [[c.text for c in r.cells] for r in result.tables[0].rows]
    assert before == after
    assert after[1][0] == "0012"
    assert after[2][0] == "0"
    applied_table = audit(target)["tables"][0]
    assert applied_table["border_evidence"] == border_evidence
    assert applied_table["table_layout_evidence"] == {
        "status": "DIRECT_DECLARATION_REPORTED",
        "declared_types": ["fixed"],
        "effective_type": "NOT_RESOLVED",
        "issues": [],
    }
    repeated = apply(path, proposal, target)
    assert repeated["decision"] == "NO_OP_VALID"


def test_reapplying_same_proposal_to_identical_output_is_noop(tmp_path):
    from chuanhoabang import propose_header

    source = fixture_docx(tmp_path)
    source_before = source.read_bytes()
    proposal = propose_header(source, 0)
    target = tmp_path / "output" / "same-result.docx"

    first = apply(source, proposal, target)
    output_before = target.read_bytes()
    second = apply(source, proposal, target)

    assert first["decision"] == "APPLIED"
    assert second["decision"] == "NO_OP_VALID"
    assert second["reasons"] == ["OUTPUT_MATCHES_VALIDATED_PROPOSAL"]
    assert second["output_sha256"] == core.digest(output_before)
    assert target.read_bytes() == output_before
    assert source.read_bytes() == source_before
    assert list(target.parent.glob(".chuanhoabang-*.docx")) == []


def test_apply_does_not_replace_different_existing_output(tmp_path):
    from chuanhoabang import propose_header

    source = fixture_docx(tmp_path)
    source_before = source.read_bytes()
    proposal = propose_header(source, 0)
    target = tmp_path / "output" / "user-file.docx"
    target.parent.mkdir()
    sentinel = b"existing user output must remain unchanged"
    target.write_bytes(sentinel)

    with pytest.raises(TableError, match="OUTPUT_MUST_BE_NEW_PATH"):
        apply(source, proposal, target)

    assert source.read_bytes() == source_before
    assert target.read_bytes() == sentinel
    assert list(target.parent.glob(".chuanhoabang-*.docx")) == []


def test_post_write_validation_failure_rolls_back_output_and_temp_file(tmp_path, monkeypatch):
    from chuanhoabang import propose_header

    source = fixture_docx(tmp_path)
    source_before = source.read_bytes()
    proposal = propose_header(source, 0)
    assert proposal["decision"] == "PROPOSE_APPLY"
    target = tmp_path / "output" / "failed.docx"
    original_assert_safe = core._assert_safe
    validation_calls = 0

    def fail_after_temp_write(*args, **kwargs):
        nonlocal validation_calls
        validation_calls += 1
        if validation_calls == 2:
            raise TableError("INJECTED_OUTPUT_VALIDATION_FAILURE")
        return original_assert_safe(*args, **kwargs)

    monkeypatch.setattr(core, "_assert_safe", fail_after_temp_write)
    with pytest.raises(TableError, match="INJECTED_OUTPUT_VALIDATION_FAILURE"):
        apply(source, proposal, target)

    assert validation_calls == 2
    assert source.read_bytes() == source_before
    assert not target.exists()
    assert list(target.parent.glob(".chuanhoabang-*.docx")) == []


def test_apply_does_not_replace_output_created_during_validation(tmp_path, monkeypatch):
    from chuanhoabang import propose_header

    source = fixture_docx(tmp_path)
    source_before = source.read_bytes()
    proposal = propose_header(source, 0)
    target = tmp_path / "output" / "created-concurrently.docx"
    sentinel = b"concurrent output must not be overwritten"
    original_assert_safe = core._assert_safe
    validation_calls = 0

    def create_output_during_validation(*args, **kwargs):
        nonlocal validation_calls
        validation_calls += 1
        result = original_assert_safe(*args, **kwargs)
        if validation_calls == 2:
            target.write_bytes(sentinel)
        return result

    monkeypatch.setattr(core, "_assert_safe", create_output_during_validation)
    with pytest.raises(TableError, match="OUTPUT_MUST_BE_NEW_PATH"):
        apply(source, proposal, target)

    assert validation_calls == 2
    assert source.read_bytes() == source_before
    assert target.read_bytes() == sentinel
    assert list(target.parent.glob(".chuanhoabang-*.docx")) == []


def test_proposal_modification_and_invalid_zip_are_rejected(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    meta = audit(path)["tables"][0]
    fake = {"input_sha256": audit(path)["input_sha256"], "table_sha256": meta["table_sha256"],
            "table_index": 0, "policy": core.POLICY_VERSION, "decision": "PROPOSE_APPLY",
            "candidate_twips": meta["grid_twips"], "evidence": "MOCK_TEST_ONLY",
            "role_classification": meta["role_classification"]}
    monkeypatch.setattr(core, "propose", lambda *a, **k: fake)
    tampered = copy.deepcopy(fake)
    tampered["candidate_twips"][0] += 10
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(path, tampered, tmp_path / "target.docx")
    broken = tmp_path / "corrupted.docx"
    broken.write_bytes(b"PK-not-really-a-docx")
    with pytest.raises(TableError):
        audit(broken)


def test_cli_help_and_audit(tmp_path, capsys):
    from chuanhoabang.cli import main
    path = fixture_docx(tmp_path)
    assert main(["audit", str(path)]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["table_count"] == 1
    assert out["word_render"] == "NOT_RUN"


def test_orientation_preserved_on_patch(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as z:
        source = z.read("word/document.xml")
    base = audit(path)["tables"][0]
    prop = {"input_sha256": audit(path)["input_sha256"], "table_sha256": base["table_sha256"],
            "table_index": 0, "policy": core.POLICY_VERSION,
            "decision": "PROPOSE_APPLY", "candidate_twips": list(base["grid_twips"]),
            "evidence": "MOCK_TEST_ONLY", "role_classification": base["role_classification"],
            "table_layout_evidence": base["table_layout_evidence"]}
    monkeypatch.setattr(core, "propose", lambda *a, **k: prop)
    result_file = tmp_path / "new.docx"
    apply(path, prop, result_file)
    with ZipFile(result_file) as z:
        target = z.read("word/document.xml")
    assert etree.tostring(core._xml(source).find(".//" + core.W + "sectPr"), method="c14n") == \
        etree.tostring(core._xml(target).find(".//" + core.W + "sectPr"), method="c14n")


def test_no_automatic_landscape_from_overflow(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as z:
        data = {i.filename: (i, z.read(i.filename)) for i in z.infolist()}
    entry, xml = data["word/document.xml"]
    root = core._xml(xml)
    for col in root.xpath(".//w:tblGrid/w:gridCol", namespaces=core.NS):
        col.set(core.W + "w", "9000")
    data["word/document.xml"] = (entry, etree.tostring(root))
    with ZipFile(path, "w") as z:
        for entry, blob in data.values():
            z.writestr(entry, blob)
    result = audit(path)
    assert result["tables"][0]["overflow_declared"] is True
    assert result["geometry"]["orientation"] == "PORTRAIT"
    assert propose(path, 0)["candidate_twips"] is None


def test_conflicting_declared_page_orientation_requires_review(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename)) for item in package.infolist()}
    info, xml = data["word/document.xml"]
    root = core._xml(xml)
    page_size = root.find(".//" + core.W + "sectPr/" + core.W + "pgSz")
    page_size.set(core.W + "orient", "landscape")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for info, content in data.values():
            package.writestr(info, content)

    report = audit(path)

    assert report["geometry"]["status"] == "GEOMETRY_UNKNOWN"
    assert report["geometry"]["reason"] == "PAGE_ORIENTATION_CONFLICT"
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


@pytest.mark.parametrize(("column_count", "explicit_width", "equal_width", "reason"), [
    (1, True, None, "CUSTOM_TEXT_COLUMN_GEOMETRY_UNSUPPORTED"),
    (2, False, None, "COLUMN_SPACING_UNSPECIFIED"),
    (1, False, "maybe", "INVALID_TEXT_COLUMNS"),
])
def test_non_default_text_column_geometry_requires_review(
        tmp_path, column_count, explicit_width, equal_width, reason):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename)) for item in package.infolist()}
    info, xml = data["word/document.xml"]
    root = core._xml(xml)
    section = root.xpath(".//w:sectPr", namespaces=core.NS)[0]
    columns = section.find(core.W + "cols")
    if columns is None:
        columns = etree.SubElement(section, core.W + "cols")
    columns.attrib.pop(core.W + "space", None)
    columns.set(core.W + "num", str(column_count))
    if equal_width is not None:
        columns.set(core.W + "equalWidth", equal_width)
    if explicit_width:
        etree.SubElement(columns, core.W + "col",
                         {core.W + "w": "7000", core.W + "space": "300"})
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for info, content in data.values():
            package.writestr(info, content)

    report = audit(path)

    assert report["geometry"]["status"] == "GEOMETRY_UNKNOWN"
    assert report["geometry"]["reason"] == reason
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


@pytest.mark.parametrize("spacing", ["not-a-width", "-1"])
def test_equal_width_columns_reject_invalid_spacing(tmp_path, spacing):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    section = root.xpath(".//w:sectPr", namespaces=core.NS)[0]
    columns = section.find(core.W + "cols")
    if columns is None:
        columns = etree.SubElement(section, core.W + "cols")
    columns.set(core.W + "num", "2")
    columns.set(core.W + "equalWidth", "1")
    columns.set(core.W + "space", spacing)
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    geometry = audit(path)["geometry"]

    assert geometry["status"] == "GEOMETRY_UNKNOWN"
    assert geometry["reason"] == "INVALID_TEXT_COLUMN_SPACING"


def test_equal_width_columns_use_column_width_for_overflow_diagnostic(tmp_path):
    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    section = root.xpath(".//w:sectPr", namespaces=core.NS)[0]
    page_size = section.find(core.W + "pgSz")
    page_size.set(core.W + "w", "18000")
    page_size.set(core.W + "h", "24000")
    margins = section.find(core.W + "pgMar")
    margins.set(core.W + "left", "1000")
    margins.set(core.W + "right", "1000")
    margins.set(core.W + "gutter", "0")
    columns = section.find(core.W + "cols")
    if columns is None:
        columns = etree.SubElement(section, core.W + "cols")
    columns.set(core.W + "num", "2")
    columns.set(core.W + "equalWidth", "1")
    columns.set(core.W + "space", "1000")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    before = path.read_bytes()

    report = audit(path)

    assert report["geometry"]["status"] == "STRUCTURAL"
    assert report["geometry"]["available_twips"] == 7500
    assert report["geometry"]["available_width_scope"] == "EQUAL_WIDTH_COLUMN_LOWER_BOUND"
    assert report["geometry"]["column_count"] == 2
    assert report["geometry"]["column_gap_twips"] == 1000
    assert report["tables"][0]["overflow_declared"] is True
    assert path.read_bytes() == before


def configure_text_columns(path, *, num, equal_width, columns, parent_space=None):
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    section = root.xpath(".//w:sectPr", namespaces=core.NS)[0]
    section.find(core.W + "pgSz").set(core.W + "w", "18000")
    section.find(core.W + "pgSz").set(core.W + "h", "24000")
    margins = section.find(core.W + "pgMar")
    margins.set(core.W + "left", "1000")
    margins.set(core.W + "right", "1000")
    margins.set(core.W + "gutter", "0")
    settings = section.find(core.W + "cols")
    if settings is None:
        settings = etree.SubElement(section, core.W + "cols")
    settings.set(core.W + "num", str(num))
    if equal_width is None:
        settings.attrib.pop(core.W + "equalWidth", None)
    else:
        settings.set(core.W + "equalWidth", equal_width)
    if parent_space is None:
        settings.attrib.pop(core.W + "space", None)
    else:
        settings.set(core.W + "space", str(parent_space))
    for child in settings.findall(core.W + "col"):
        settings.remove(child)
    for column_width, spacing_after in columns:
        attrs = {}
        if column_width is not None:
            attrs[core.W + "w"] = str(column_width)
        if spacing_after is not None:
            attrs[core.W + "space"] = str(spacing_after)
        etree.SubElement(settings, core.W + "col", attrs)
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)


def test_explicit_unequal_columns_use_minimum_declared_width_as_safe_bound(tmp_path):
    path = fixture_docx(tmp_path)
    configure_text_columns(
        path, num=3, equal_width="0",
        columns=[(6000, 500), (3500, 700), (5000, None)], parent_space=12000)
    before = path.read_bytes()

    report = audit(path)

    geometry = report["geometry"]
    assert geometry["status"] == "STRUCTURAL"
    assert geometry["available_twips"] == 3500
    assert geometry["available_width_scope"] == "CUSTOM_COLUMN_MINIMUM_LOWER_BOUND"
    assert geometry["column_count"] == 3
    assert geometry["custom_column_widths_twips"] == [6000, 3500, 5000]
    assert geometry["custom_column_spacing_after_twips"] == [500, 700, None]
    assert report["tables"][0]["overflow_declared"] is True
    assert report["word_render"] == "NOT_RUN"
    assert path.read_bytes() == before


def test_explicit_single_column_width_is_a_source_derived_bound(tmp_path):
    path = fixture_docx(tmp_path)
    configure_text_columns(path, num=1, equal_width="0", columns=[(7000, None)])

    geometry = audit(path)["geometry"]

    assert geometry["status"] == "STRUCTURAL"
    assert geometry["available_twips"] == 7000
    assert geometry["available_width_scope"] == "CUSTOM_COLUMN_MINIMUM_LOWER_BOUND"
    assert geometry["custom_column_widths_twips"] == [7000]
    assert geometry["custom_column_spacing_after_twips"] == [None]


@pytest.mark.parametrize(("num", "columns", "reason"), [
    (2, [(6000, None), (3000, 0)], "CUSTOM_COLUMN_SPACING_UNSPECIFIED"),
    (2, [(None, 500), (3000, 0)], "CUSTOM_COLUMN_WIDTH_UNSPECIFIED"),
    (2, [(0, 500), (3000, 0)], "INVALID_CUSTOM_COLUMN_WIDTH"),
    (2, [("bad", 500), (3000, 0)], "INVALID_CUSTOM_COLUMN_WIDTH"),
    (2, [(6000, "bad"), (3000, 0)], "INVALID_CUSTOM_COLUMN_SPACING"),
    (2, [(6000, -1), (3000, 0)], "INVALID_CUSTOM_COLUMN_SPACING"),
    (2, [(9000, 500), (8000, 0)], "CUSTOM_TEXT_COLUMNS_EXCEED_PAGE_TEXT_WIDTH"),
    (3, [(6000, 500), (3000, 0)], "TEXT_COLUMN_COUNT_MISMATCH"),
])
def test_explicit_unequal_columns_fail_closed_on_incomplete_geometry(
        tmp_path, num, columns, reason):
    path = fixture_docx(tmp_path)
    configure_text_columns(path, num=num, equal_width="0", columns=columns)

    geometry = audit(path)["geometry"]

    assert geometry["status"] == "GEOMETRY_UNKNOWN"
    assert geometry["reason"] == reason
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_implicit_equal_width_does_not_interpret_custom_column_children(tmp_path):
    path = fixture_docx(tmp_path)
    configure_text_columns(
        path, num=2, equal_width=None,
        columns=[(6000, 500), (3000, 0)], parent_space=500)

    geometry = audit(path)["geometry"]

    assert geometry["status"] == "GEOMETRY_UNKNOWN"
    assert geometry["reason"] == "CUSTOM_TEXT_COLUMN_GEOMETRY_UNSUPPORTED"


@pytest.mark.parametrize(("marker", "attributes", "reason"), [
    ("tblpPr", {core.W + "horzAnchor": "page"}, "FLOATING_OR_ROTATED_CONTENT"),
    ("tblInd", {core.W + "w": "120", core.W + "type": "dxa"},
     "TABLE_INDENT_REQUIRES_REVIEW"),
])
def test_floating_or_indented_table_position_blocks_all_proposals(
        tmp_path, marker, attributes, reason):
    from chuanhoabang import propose_header, propose_unclip_row_height

    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    table_properties = table.find(core.W + "tblPr")
    etree.SubElement(table_properties, core.W + marker, attributes)
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    before = path.read_bytes()

    report = audit(path)["tables"][0]

    assert report["status"] == "REVIEW_REQUIRED"
    assert reason in report["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == before


@pytest.mark.parametrize(("table_margin", "cell_margin", "expected_padding", "min_first_width",
                         "expected_basis", "expected_assumed_padding"), [
    ({"left": 300, "right": 400}, None, [[700, 700, 700]] * 3, 1507,
     "EXPLICIT_DXA", None),
    ({"left": 100, "right": 100}, {"left": 400, "right": 300},
     [[700, 200, 200], [200, 200, 200], [200, 200, 200]], 1007,
     "EXPLICIT_DXA", None),
    (None, {"left": 300, "right": 400},
     [[700, 240, 240], [240, 240, 240], [240, 240, 240]], 1047,
     "EXPLICIT_DXA_AND_DEFAULT_ASSUMPTION", 240),
    (None, None, [[240, 240, 240]] * 3, 1047, "ASSUMED_DEFAULT", 240),
])
def test_cell_margin_geometry_feeds_width_metrics(
        tmp_path, monkeypatch, table_margin, cell_margin, expected_padding, min_first_width,
        expected_basis, expected_assumed_padding):
    class FakeFont:
        def getlength(self, text):
            return len(text) * 12

    from chuanhoabang import propose_header, propose_unclip_row_height

    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    first_body_text = table.xpath("./w:tr[2]/w:tc[1]//w:t", namespaces=core.NS)[0]
    first_body_text.text += " abcdefghijklmnopqrstuvwx"
    table_properties = table.find(core.W + "tblPr")
    if table_margin is not None:
        node = etree.SubElement(table_properties, core.W + "tblCellMar")
        for side, value in table_margin.items():
            etree.SubElement(node, core.W + side,
                             {core.W + "w": str(value), core.W + "type": "dxa"})
    if cell_margin is not None:
        first_cell = table.find("./" + core.W + "tr/" + core.W + "tc")
        cell_properties = first_cell.find(core.W + "tcPr")
        node = etree.SubElement(cell_properties, core.W + "tcMar")
        for side, value in cell_margin.items():
            etree.SubElement(node, core.W + side,
                             {core.W + "w": str(value), core.W + "type": "dxa"})
    column_widths = (900, 6400, 1100)
    for column, width in zip(table.xpath("./w:tblGrid/w:gridCol", namespaces=core.NS),
                             column_widths):
        column.set(core.W + "w", str(width))
    for row in table.xpath("./w:tr", namespaces=core.NS):
        cell_width = row.xpath("./w:tc[1]/w:tcPr/w:tcW", namespaces=core.NS)[0]
        cell_width.set(core.W + "w", str(column_widths[0]))
        cell_width.set(core.W + "type", "dxa")
    table_width = table.find(core.W + "tblPr/" + core.W + "tblW")
    table_width.set(core.W + "w", str(sum(column_widths)))
    table_width.set(core.W + "type", "dxa")
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    before = path.read_bytes()
    font_path = tmp_path / "synthetic-font.bin"
    font_path.write_bytes(b"not-a-font; metric loader is patched")
    monkeypatch.setattr(core, "_load_fonts", lambda *args: (FakeFont(), FakeFont()))

    report = audit(path)["tables"][0]
    proposal = propose(path, 0, font_regular=font_path, font_bold=font_path)

    assert report["status"] == "SUPPORTED"
    assert report["width_evidence"]["cell_padding"]["twips_by_row"] == expected_padding
    assert report["width_evidence"]["cell_padding"]["basis"] == expected_basis
    assert report["width_evidence"]["cell_padding"]["assumed_default_twips"] == expected_assumed_padding
    assert proposal["decision"] == "PROPOSE_APPLY"
    assert proposal["candidate_twips"][0] >= min_first_width
    assert proposal["metrics"]["padding_twips_by_cell"] == expected_padding
    assert proposal["metrics"]["padding_twips_assumed"] == expected_assumed_padding
    assert propose_header(path, 0)["decision"] == "PROPOSE_APPLY"
    assert propose_unclip_row_height(path, 0)["decision"] == "NO_OP_VALID"
    assert path.read_bytes() == before


@pytest.mark.parametrize(("owner", "margin_element"), [
    ("table", "tblCellMar"),
    ("cell", "tcMar"),
])
def test_unresolved_explicit_cell_margins_make_geometry_unknown(
        tmp_path, owner, margin_element):
    from chuanhoabang import propose_header, propose_unclip_row_height

    path = fixture_docx(tmp_path)
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}
    info, document_xml = data["word/document.xml"]
    root = core._xml(document_xml)
    table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    if owner == "table":
        properties = table.find(core.W + "tblPr")
    else:
        properties = table.find("./" + core.W + "tr/" + core.W + "tc/" + core.W + "tcPr")
    margins = etree.SubElement(properties, core.W + margin_element)
    etree.SubElement(margins, core.W + "left", {core.W + "w": "900", core.W + "type": "pct"})
    etree.SubElement(margins, core.W + "right", {core.W + "w": "900", core.W + "type": "dxa"})
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)
    before = path.read_bytes()

    report = audit(path)["tables"][0]

    assert report["status"] == "REVIEW_REQUIRED"
    assert "CELL_MARGIN_GEOMETRY_UNRESOLVED" in report["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert path.read_bytes() == before


@pytest.mark.parametrize(("mirror_value", "expected_reason"), [
    (None, "MIRRORED_GUTTER_GEOMETRY_UNSUPPORTED"),
    ("0", None),
    ("invalid", "INVALID_MIRROR_MARGINS_SETTING"),
])
def test_mirrored_margins_with_gutter_are_scoped_by_settings(
        tmp_path, mirror_value, expected_reason):
    path = fixture_docx(tmp_path)
    baseline_available = audit(path)["geometry"]["available_twips"]
    with ZipFile(path) as package:
        data = {item.filename: (item, package.read(item.filename))
                for item in package.infolist()}

    document_info, document_xml = data["word/document.xml"]
    document_root = core._xml(document_xml)
    page_margins = document_root.find(".//" + core.W + "sectPr/" + core.W + "pgMar")
    page_margins.set(core.W + "gutter", "720")
    data["word/document.xml"] = (document_info, etree.tostring(document_root))

    settings_info, settings_xml = data["word/settings.xml"]
    settings_root = core._xml(settings_xml)
    mirror_margins = etree.SubElement(settings_root, core.W + "mirrorMargins")
    if mirror_value is not None:
        mirror_margins.set(core.W + "val", mirror_value)
    data["word/settings.xml"] = (settings_info, etree.tostring(settings_root))
    with ZipFile(path, "w") as package:
        for item, content in data.values():
            package.writestr(item, content)

    report = audit(path)

    if expected_reason is not None:
        assert report["geometry"]["status"] == "GEOMETRY_UNKNOWN"
        assert report["geometry"]["reason"] == expected_reason
        assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"
    else:
        assert report["geometry"]["status"] == "STRUCTURAL"
        assert report["geometry"]["available_twips"] == baseline_available - 720


def test_header_repeat_proposal_applies_only_to_first_row(tmp_path):
    from chuanhoabang import propose_header
    path = fixture_docx(tmp_path)
    initial = path.read_bytes()
    prop = propose_header(path, 0)
    assert prop["decision"] == "PROPOSE_APPLY"
    assert prop["operation"] == "SET_REPEAT_HEADER_FIRST_ROW"
    result_file = tmp_path / "with-header.docx"
    applied = apply(path, prop, result_file)
    assert applied["changed_properties"] == ["tblHeader"]
    assert applied["word_render"] == "NOT_RUN"
    assert path.read_bytes() == initial
    parsed = core._xml(ZipFile(result_file).read("word/document.xml"))
    rows = parsed.xpath(".//w:body/w:tbl/w:tr", namespaces=core.NS)
    assert len(rows) == 3
    assert len(rows[0].xpath("./w:trPr/w:tblHeader[@w:val='1']", namespaces=core.NS)) == 1
    assert not rows[1].xpath("./w:trPr/w:tblHeader", namespaces=core.NS)
    assert audit(result_file)["tables"][0]["pagination_diagnostics"]["header_repeat_first_row"]
    assert propose_header(result_file, 0)["decision"] == "NO_OP_VALID"
    assert [[c.text for c in r.cells] for r in Document(path).tables[0].rows] == \
           [[c.text for c in r.cells] for r in Document(result_file).tables[0].rows]


def test_header_repeat_requires_known_data_table_unlocked(tmp_path):
    from chuanhoabang import propose_header
    assert propose_header(fixture_docx(tmp_path, header=False), 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(fixture_docx(tmp_path, protected=True), 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(fixture_docx(tmp_path, merged=True), 0)["decision"] == "PROPOSE_APPLY"


def test_header_repeat_tampered_and_stale_rejected(tmp_path):
    from chuanhoabang import propose_header
    doc = fixture_docx(tmp_path)
    proposal = propose_header(doc, 0)
    altered = dict(proposal, reasons=["POSSIBLE_LAYOUT_TABLE"])
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(doc, altered, tmp_path / "bad.docx")
    docx = Document(doc)
    docx.add_paragraph("changed after proposal")
    docx.save(doc)
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(doc, proposal, tmp_path / "stale.docx")


def test_cli_propose_header_and_apply(tmp_path, capsys):
    from chuanhoabang.cli import main
    source = fixture_docx(tmp_path)
    prop = tmp_path / "head-proposal.json"
    assert main(["propose-header", str(source), "--table", "0", "--output", str(prop)]) == 0
    assert json.loads(capsys.readouterr().out)["decision"] == "PROPOSE_APPLY"
    target = tmp_path / "result.docx"
    assert main(["apply", str(source), "--proposal", str(prop), "--output", str(target)]) == 0
    assert json.loads(capsys.readouterr().out)["changed_properties"] == ["tblHeader"]


def test_multiline_cell_does_not_enter_width_optimization_without_evidence(tmp_path, monkeypatch):
    doc = fixture_docx(tmp_path)
    word = Document(doc)
    word.tables[0].cell(1, 1).add_paragraph("another paragraph")
    word.save(doc)
    class FakeFont:
        def getlength(self, text):
            return len(text) * 4
    synthetic_font = tmp_path / "synthetic-font-placeholder.bin"
    synthetic_font.write_bytes(b"not-a-font; metric loader is patched")
    monkeypatch.setattr(core, "_load_fonts", lambda *args: (FakeFont(), FakeFont()))
    result = propose(doc, 0, font_regular=synthetic_font, font_bold=synthetic_font)
    assert result["decision"] == "REVIEW_REQUIRED"
    assert "MULTI_PARAGRAPH_CELL_REQUIRES_REVIEW" in result["reasons"]


def test_header_disabled_val_zero_can_be_enabled_without_duplicate(tmp_path):
    from chuanhoabang import propose_header
    doc = fixture_docx(tmp_path)
    with ZipFile(doc) as z:
        data = {i.filename: (i, z.read(i.filename)) for i in z.infolist()}
    info, xml = data["word/document.xml"]
    root = core._xml(xml)
    row = root.xpath(".//w:body/w:tbl/w:tr[1]", namespaces=core.NS)[0]
    trpr = etree.Element(core.W + "trPr")
    row.insert(0, trpr)
    etree.SubElement(trpr, core.W + "tblHeader", {core.W + "val": "0"})
    data["word/document.xml"] = (info, etree.tostring(root))
    with ZipFile(doc, "w") as z:
        for entry, blob in data.values():
            z.writestr(entry, blob)
    assert not audit(doc)["tables"][0]["pagination_diagnostics"]["header_repeat_first_row"]
    proposal = propose_header(doc, 0)
    assert proposal["decision"] == "PROPOSE_APPLY"
    dest = tmp_path / "header-true.docx"
    apply(doc, proposal, dest)
    root_after = core._xml(ZipFile(dest).read("word/document.xml"))
    nodes = root_after.xpath(".//w:body/w:tbl/w:tr[1]/w:trPr/w:tblHeader", namespaces=core.NS)
    assert len(nodes) == 1 and nodes[0].get(core.W + "val") == "1"


def test_width_proposal_does_not_reject_harmless_empty_runs(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    class FakeFont:
        def getlength(self, text):
            return len(text) * 4
    synthetic_font = tmp_path / "synthetic-font-placeholder.bin"
    synthetic_font.write_bytes(b"not-a-font; metric loader is patched")
    monkeypatch.setattr(core, "_load_fonts", lambda *args: (FakeFont(), FakeFont()))
    result = propose(path, 0, font_regular=synthetic_font, font_bold=synthetic_font)
    # This tests only the token/structure path; the placeholder is not a font.
    assert result["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    assert "NON_PLAIN_RUN" not in result["reasons"]
    assert result["word_render"] == "NOT_RUN"


def test_exact_height_relaxation_only_changes_row_rule(tmp_path):
    from chuanhoabang import propose_unclip_row_height
    from docx.enum.table import WD_ROW_HEIGHT_RULE
    path = fixture_docx(tmp_path)
    source = Document(path)
    source.tables[0].rows[1].height = Pt(6)
    source.tables[0].rows[1].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    source.save(path)
    before = path.read_bytes()
    prop = propose_unclip_row_height(path, 0)
    assert prop["decision"] == "PROPOSE_APPLY"
    assert prop["row_indices"] == [1]
    target = tmp_path / "height-at-least.docx"
    applied = apply(path, prop, target)
    assert applied["changed_properties"] == ["trHeight.hRule"]
    assert applied["word_render"] == "NOT_RUN"
    assert path.read_bytes() == before
    new = Document(target)
    assert new.tables[0].rows[1].height_rule == WD_ROW_HEIGHT_RULE.AT_LEAST
    assert new.tables[0].rows[1].height == Pt(6)
    assert [[c.text for c in r.cells] for r in source.tables[0].rows] == \
           [[c.text for c in r.cells] for r in new.tables[0].rows]
    assert propose_unclip_row_height(target, 0)["decision"] == "NO_OP_VALID"


def test_unclip_review_for_locked_or_complex_document(tmp_path):
    from chuanhoabang import propose_unclip_row_height
    assert propose_unclip_row_height(fixture_docx(tmp_path, protected=True), 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(fixture_docx(tmp_path, merged=True), 0)["decision"] == "NO_OP_VALID"


def test_height_unclip_proposal_is_immutable(tmp_path):
    from chuanhoabang import propose_unclip_row_height
    from docx.enum.table import WD_ROW_HEIGHT_RULE
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].rows[1].height = Pt(6)
    doc.tables[0].rows[1].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    doc.save(path)
    proposal = propose_unclip_row_height(path, 0)
    altered = copy.deepcopy(proposal)
    altered["row_indices"] = [0]
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(path, altered, tmp_path / "invalid.docx")


def test_cli_unclip_height(tmp_path, capsys):
    from chuanhoabang.cli import main
    from docx.enum.table import WD_ROW_HEIGHT_RULE
    path = fixture_docx(tmp_path)
    doc = Document(path)
    doc.tables[0].rows[1].height = Pt(6)
    doc.tables[0].rows[1].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    doc.save(path)
    proposal = tmp_path / "proposal.json"
    assert main(["propose-unclip", str(path), "--table", "0", "--output", str(proposal)]) == 0
    assert json.loads(capsys.readouterr().out)["decision"] == "PROPOSE_APPLY"
    target = tmp_path / "relaxed.docx"
    assert main(["apply", str(path), "--proposal", str(proposal), "--output", str(target)]) == 0
    assert json.loads(capsys.readouterr().out)["changed_properties"] == ["trHeight.hRule"]
