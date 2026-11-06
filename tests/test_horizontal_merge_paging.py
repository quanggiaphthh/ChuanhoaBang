"""G4 narrow support: only horizontal gridSpan, only safe pagination properties."""
from zipfile import ZipFile

import pytest
from docx import Document
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.shared import Pt
from lxml import etree

from chuanhoabang import audit, propose, propose_header, propose_unclip_row_height, apply
from chuanhoabang import core


def fixture(tmp_path, mode="horizontal", exact=False):
    document = Document()
    table = document.add_table(rows=3, cols=3)
    for ri, values in enumerate([
        ("STT", "Nội dung", "Ghi chú"),
        ("0012", "Nội dung đã gộp", "Đang xử lý"),
        ("0", "Công việc hoàn thành", "Hoàn thành"),
    ]):
        for cell, txt in zip(table.rows[ri].cells, values):
            cell.text = txt
    if mode == "horizontal":
        table.cell(1, 0).merge(table.cell(1, 1))
    elif mode == "vertical":
        table.cell(1, 0).merge(table.cell(2, 0))
    if exact:
        table.rows[1].height = Pt(6)
        table.rows[1].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    path = tmp_path / "source.docx"
    document.save(path)
    return path


def _table_text(path):
    with ZipFile(path) as z:
        xml = core._xml(z.read("word/document.xml"))
    return [n.text for n in core._tables(xml)[0].xpath(".//w:t", namespaces=core.NS)]


def test_hmerge_header_is_safe_but_width_optimizer_stays_blocked(tmp_path):
    path = fixture(tmp_path)
    original_bytes = path.read_bytes()
    original_text = _table_text(path)
    table_info = audit(path)["tables"][0]
    assert "MERGED_OR_OMITTED_CELLS" in table_info["reasons"]
    assert table_info["status"] == "REVIEW_REQUIRED"
    assert table_info["cell_grid_spans"][1] == [
        {"start_column": 0, "span": 2}, {"start_column": 2, "span": 1},
    ]
    from chuanhoabang.cli import render_markdown
    markdown = render_markdown(audit(path))
    assert "Cell grid spans / vertical merge markers (source XML)" in markdown
    assert '"start_column":0' in markdown
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"
    header = propose_header(path, 0)
    assert header["decision"] == "PROPOSE_APPLY"
    assert "HORIZONTAL_GRIDSPAN_PAGING_ONLY" in header["reasons"]
    dest = tmp_path / "header.docx"
    applied = apply(path, header, dest)
    assert applied["changed_properties"] == ["tblHeader"]
    assert path.read_bytes() == original_bytes
    assert _table_text(dest) == original_text
    with ZipFile(dest) as z:
        root = core._xml(z.read("word/document.xml"))
    table = core._tables(root)[0]
    assert table.xpath("./w:tr[2]/w:tc[1]/w:tcPr/w:gridSpan/@w:val", namespaces=core.NS) == ["2"]
    assert table.xpath("./w:tr[1]/w:trPr/w:tblHeader/@w:val", namespaces=core.NS) == ["1"]
    assert propose_header(dest, 0)["decision"] == "NO_OP_VALID"


def test_hmerge_height_rule_only_and_preserves_spans(tmp_path):
    path = fixture(tmp_path, exact=True)
    original_text = _table_text(path)
    prop = propose_unclip_row_height(path, 0)
    assert prop["decision"] == "PROPOSE_APPLY"
    assert prop["row_indices"] == [1]
    output = tmp_path / "unclipped.docx"
    report = apply(path, prop, output)
    assert report["changed_properties"] == ["trHeight.hRule"]
    assert _table_text(output) == original_text
    with ZipFile(output) as z:
        root = core._xml(z.read("word/document.xml"))
    table = core._tables(root)[0]
    assert table.xpath("./w:tr[2]/w:trPr/w:trHeight/@w:hRule", namespaces=core.NS) == ["atLeast"]
    assert table.xpath("./w:tr[2]/w:tc[1]/w:tcPr/w:gridSpan/@w:val", namespaces=core.NS) == ["2"]


def test_vertical_merge_reports_source_markers_but_stays_review_required(tmp_path):
    path = fixture(tmp_path, mode="vertical", exact=True)
    table_info = audit(path)["tables"][0]
    assert table_info["cell_grid_spans"] == [
        [
            {"start_column": 0, "span": 1},
            {"start_column": 1, "span": 1},
            {"start_column": 2, "span": 1},
        ],
        [
            {"start_column": 0, "span": 1, "vertical_merge": "RESTART"},
            {"start_column": 1, "span": 1},
            {"start_column": 2, "span": 1},
        ],
        [
            {"start_column": 0, "span": 1, "vertical_merge": "CONTINUE"},
            {"start_column": 1, "span": 1},
            {"start_column": 2, "span": 1},
        ],
    ]
    assert table_info["status"] == "REVIEW_REQUIRED"
    assert "MERGED_OR_OMITTED_CELLS" in table_info["reasons"]
    from chuanhoabang.cli import render_markdown
    assert '"vertical_merge":"RESTART"' in render_markdown(audit(path))
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_malformed_vertical_merge_marker_does_not_produce_grid_mapping(tmp_path):
    path = fixture(tmp_path, mode="vertical")
    with ZipFile(path) as z:
        parts = [(info, z.read(info.filename)) for info in z.infolist()]
    with ZipFile(path, "w") as z:
        for info, data in parts:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                marker = root.xpath(
                    ".//w:body/w:tbl/w:tr[2]/w:tc[1]/w:tcPr/w:vMerge",
                    namespaces=core.NS,
                )[0]
                marker.set(core.W + "val", "join")
                data = etree.tostring(root)
            z.writestr(info, data)
    assert audit(path)["tables"][0]["cell_grid_spans"] is None
    assert propose_header(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_invalid_horizontal_grid_span_fails_closed(tmp_path):
    path = fixture(tmp_path)
    with ZipFile(path) as z:
        parts = [(info, z.read(info.filename)) for info in z.infolist()]
    with ZipFile(path, "w") as z:
        for info, data in parts:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                span = root.xpath(".//w:body/w:tbl/w:tr[2]/w:tc[1]/w:tcPr/w:gridSpan", namespaces=core.NS)[0]
                span.set(core.W + "val", "7")
                data = etree.tostring(root)
            z.writestr(info, data)
    assert audit(path)["tables"][0]["cell_grid_spans"] is None
    assert propose_header(path, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(path, 0)["decision"] == "REVIEW_REQUIRED"
