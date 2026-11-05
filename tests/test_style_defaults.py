"""Bounded style resolution with fail-closed handling of unresolved cascades."""
import pytest
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from lxml import etree
from zipfile import ZipFile

from chuanhoabang import audit, propose
from chuanhoabang import core


class SyntheticMetricFont:
    def getlength(self, text):
        # This fake metric only checks traversal and safety, NOT real TNR.
        return len(text) * 4


def document_fixture(tmp_path, *, normal_font="Times New Roman", named_style=False,
                     character_style=False, table_style=False, direct=False):
    doc = Document()
    doc.styles["Normal"].font.name = normal_font
    doc.styles["Normal"].font.size = Pt(14)
    table = doc.add_table(rows=3, cols=3)
    if table_style:
        table.style = "Table Grid"
    values = [("STT", "Nội dung", "Ghi chú"),
              ("0012", "Nội dung được kế thừa", "Đang xử lý"),
              ("0", "Kết quả hoàn thành", "Hoàn thành")]
    for row, cells in zip(table.rows, values):
        for cell, value in zip(row.cells, cells):
            cell.text = ""
            paragraph = cell.paragraphs[0]
            if named_style:
                paragraph.style = "Title"
            run = paragraph.add_run(value)
            if character_style:
                run.style = "Emphasis"
            if direct:
                run.font.name = "Times New Roman"
                run.font.size = Pt(14)
    path = tmp_path / "sample.docx"
    doc.save(path)
    return path


def rewrite_parts(path, updates):
    with ZipFile(path) as package:
        parts = [(item, updates.get(item.filename, package.read(item.filename)))
                 for item in package.infolist()]
    with ZipFile(path, "w") as package:
        for item, content in parts:
            package.writestr(item, content)


def set_style_margins(path, style_id, left, right):
    with ZipFile(path) as package:
        root = core._xml(package.read("word/styles.xml"))
    styles = root.xpath("./w:style[@w:type='table'][@w:styleId=$style_id]",
                        namespaces=core.NS, style_id=style_id)
    assert len(styles) == 1
    table_properties = styles[0].find(core.W + "tblPr")
    if table_properties is None:
        table_properties = etree.SubElement(styles[0], core.W + "tblPr")
    for margins in table_properties.findall(core.W + "tblCellMar"):
        table_properties.remove(margins)
    if left is not None or right is not None:
        margins = etree.SubElement(table_properties, core.W + "tblCellMar")
        for side, value in (("left", left), ("right", right)):
            if value is not None:
                etree.SubElement(margins, core.W + side,
                                 {core.W + "w": str(value), core.W + "type": "dxa"})
    rewrite_parts(path, {"word/styles.xml": etree.tostring(root)})


def add_conditional_style_margins(path):
    with ZipFile(path) as package:
        root = core._xml(package.read("word/styles.xml"))
    styles = root.xpath("./w:style[@w:type='table'][@w:styleId='TableGrid']",
                        namespaces=core.NS)
    assert len(styles) == 1
    conditional = etree.SubElement(styles[0], core.W + "tblStylePr",
                                   {core.W + "type": "firstRow"})
    cell_properties = etree.SubElement(conditional, core.W + "tcPr")
    margins = etree.SubElement(cell_properties, core.W + "tcMar")
    for side, value in (("left", 30), ("right", 40)):
        etree.SubElement(margins, core.W + side,
                         {core.W + "w": str(value), core.W + "type": "dxa"})
    rewrite_parts(path, {"word/styles.xml": etree.tostring(root)})


def make_table_style_cycle(path):
    with ZipFile(path) as package:
        root = core._xml(package.read("word/styles.xml"))
    styles = root.xpath("./w:style[@w:type='table'][@w:styleId='TableNormal']",
                        namespaces=core.NS)
    assert len(styles) == 1
    etree.SubElement(styles[0], core.W + "basedOn", {core.W + "val": "TableGrid"})
    rewrite_parts(path, {"word/styles.xml": etree.tostring(root)})


def set_direct_margins(path, *, table=None, first_cell_left=None):
    with ZipFile(path) as package:
        root = core._xml(package.read("word/document.xml"))
    table_node = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
    if table is not None:
        table_properties = table_node.find(core.W + "tblPr")
        margins = etree.SubElement(table_properties, core.W + "tblCellMar")
        for side, value in zip(("left", "right"), table):
            etree.SubElement(margins, core.W + side,
                             {core.W + "w": str(value), core.W + "type": "dxa"})
    if first_cell_left is not None:
        first_cell = table_node.find("./" + core.W + "tr/" + core.W + "tc")
        cell_properties = first_cell.find(core.W + "tcPr")
        margins = etree.SubElement(cell_properties, core.W + "tcMar")
        etree.SubElement(margins, core.W + "left",
                         {core.W + "w": str(first_cell_left), core.W + "type": "dxa"})
    rewrite_parts(path, {"word/document.xml": etree.tostring(root)})


@pytest.fixture
def fake_metrics(tmp_path, monkeypatch):
    synthetic_data = tmp_path / "synthetic-test-only-not-a-font.bin"
    synthetic_data.write_bytes(b"SYNTHETIC_NON_FONT_TEST_DATA")
    monkeypatch.setattr(core, "_load_fonts",
                        lambda *args: (SyntheticMetricFont(), SyntheticMetricFont()))
    return str(synthetic_data)


def test_normal_style_inheritance_enables_measured_candidate_path(tmp_path, fake_metrics):
    source = document_fixture(tmp_path)
    p = propose(source, 0, font_regular=fake_metrics, font_bold=fake_metrics)
    assert p["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    assert p["evidence"] == "FONT_METRIC_ESTIMATE"
    assert "UNRESOLVED_EFFECTIVE_FONT" not in p["reasons"]
    assert p["word_render"] == "NOT_RUN"


def test_non_tnr_normal_style_still_rejected(tmp_path, fake_metrics):
    source = document_fixture(tmp_path, normal_font="Arial")
    p = propose(source, 0, font_regular=fake_metrics)
    assert p["decision"] == "REVIEW_REQUIRED"
    assert "UNRESOLVED_EFFECTIVE_FONT" in p["reasons"]


@pytest.mark.parametrize("override", ["named_style", "character_style", "table_style"])
def test_unsupported_style_cascade_fails_closed(tmp_path, fake_metrics, override):
    source = document_fixture(tmp_path, **{override: True})
    p = propose(source, 0, font_regular=fake_metrics)
    assert p["decision"] == "REVIEW_REQUIRED"
    assert "STYLE" in " ".join(p["reasons"])


def test_table_style_conditional_margins_keep_cell_padding_unresolved(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    add_conditional_style_margins(source)

    report = audit(source)["tables"][0]
    padding = report["width_evidence"]["cell_padding"]

    assert padding["status"] == "UNRESOLVED"
    assert padding["reason"] == "TABLE_STYLE_CASCADE_NOT_SUPPORTED"
    assert "twips_by_row" not in padding


def test_audit_resolves_table_style_cell_margins_from_based_on_chain(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    set_style_margins(source, "TableGrid", None, None)
    set_style_margins(source, "TableNormal", 72, 84)

    report = audit(source)["tables"][0]
    padding = report["width_evidence"]["cell_padding"]

    assert padding["status"] == "RESOLVED"
    assert padding["basis"] == "TABLE_STYLE_DXA"
    assert padding["assumed_default_twips"] is None
    assert padding["twips_by_row"] == [[156, 156, 156]] * 3
    assert padding["table_style"] == {
        "status": "RESOLVED",
        "style_id": "TableGrid",
        "based_on_chain": ["TableNormal", "TableGrid"],
        "margin_source_style_id": "TableNormal",
        "horizontal_margin_twips": {"left": 72, "right": 84},
        "margin_used": True,
    }


def test_direct_table_and_cell_margins_override_table_style_margins(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    set_style_margins(source, "TableGrid", 135, 165)
    set_direct_margins(source, table=(200, 240), first_cell_left=300)

    report = audit(source)["tables"][0]
    padding = report["width_evidence"]["cell_padding"]

    assert padding["status"] == "RESOLVED"
    assert padding["basis"] == "EXPLICIT_DXA"
    assert padding["twips_by_row"] == [[540, 440, 440], [440, 440, 440],
                                       [440, 440, 440]]
    assert padding["table_style"]["margin_source_style_id"] == "TableGrid"
    assert padding["table_style"]["horizontal_margin_twips"] == {
        "left": 135, "right": 165,
    }
    assert padding["table_style"]["margin_used"] is False


def test_direct_cell_margin_overrides_one_side_of_table_style_baseline(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    set_style_margins(source, "TableGrid", 135, 165)
    set_direct_margins(source, first_cell_left=300)

    padding = audit(source)["tables"][0]["width_evidence"]["cell_padding"]

    assert padding["status"] == "RESOLVED"
    assert padding["basis"] == "TABLE_STYLE_AND_EXPLICIT_DXA"
    assert padding["twips_by_row"] == [[465, 300, 300], [300, 300, 300],
                                       [300, 300, 300]]
    assert padding["table_style"]["margin_used"] is True


def test_table_style_without_horizontal_margin_uses_reported_estimator_budget(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    set_style_margins(source, "TableGrid", None, None)
    set_style_margins(source, "TableNormal", None, None)

    padding = audit(source)["tables"][0]["width_evidence"]["cell_padding"]

    assert padding["status"] == "RESOLVED"
    assert padding["basis"] == "TABLE_STYLE_DEFAULT_ASSUMPTION"
    assert padding["assumed_default_twips"] == 240
    assert padding["twips_by_row"] == [[240, 240, 240]] * 3
    assert padding["table_style"]["margin_used"] is False


def test_table_style_based_on_cycle_keeps_cell_padding_unresolved(tmp_path):
    source = document_fixture(tmp_path, table_style=True)
    make_table_style_cycle(source)

    padding = audit(source)["tables"][0]["width_evidence"]["cell_padding"]

    assert padding["status"] == "UNRESOLVED"
    assert padding["reason"] == "TABLE_STYLE_CASCADE_NOT_SUPPORTED"
    assert "twips_by_row" not in padding


def test_run_level_tnr_overrides_non_tnr_normal(tmp_path, fake_metrics):
    source = document_fixture(tmp_path, normal_font="Arial", direct=True)
    p = propose(source, 0, font_regular=fake_metrics)
    assert p["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    assert p["evidence"] == "FONT_METRIC_ESTIMATE"


def test_named_paragraph_style_with_explicit_normal_parent_resolves(tmp_path, fake_metrics):
    source = document_fixture(tmp_path)
    doc = Document(source)
    style = doc.styles.add_style("ReportBody", WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = doc.styles["Normal"]
    for row in doc.tables[0].rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.style = style
    doc.save(source)

    result = propose(source, 0, font_regular=fake_metrics, font_bold=fake_metrics)

    assert result["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    assert result["evidence"] == "FONT_METRIC_ESTIMATE"


def test_named_paragraph_style_inheritance_cycle_is_reviewed(tmp_path, fake_metrics):
    source = document_fixture(tmp_path)
    doc = Document(source)
    first = doc.styles.add_style("CycleOne", WD_STYLE_TYPE.PARAGRAPH)
    second = doc.styles.add_style("CycleTwo", WD_STYLE_TYPE.PARAGRAPH)
    first.base_style = second
    second.base_style = first
    for row in doc.tables[0].rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.style = first
    doc.save(source)

    result = propose(source, 0, font_regular=fake_metrics, font_bold=fake_metrics)

    assert result["decision"] == "REVIEW_REQUIRED"
    assert "STYLE_BASED_ON_CYCLE" in result["reasons"]


def test_named_paragraph_style_without_normal_ancestor_is_reviewed(tmp_path, fake_metrics):
    source = document_fixture(tmp_path)
    doc = Document(source)
    style = doc.styles.add_style("DetachedBody", WD_STYLE_TYPE.PARAGRAPH)
    for row in doc.tables[0].rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.style = style
    doc.save(source)

    result = propose(source, 0, font_regular=fake_metrics, font_bold=fake_metrics)

    assert result["decision"] == "REVIEW_REQUIRED"
    assert "PARAGRAPH_STYLE_DEFAULT_NOT_INHERITED" in result["reasons"]
