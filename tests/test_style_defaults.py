"""Bounded style resolution with fail-closed handling of unresolved cascades."""
import pytest
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt

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


def test_audit_does_not_claim_cell_padding_resolved_for_table_style(tmp_path):
    source = document_fixture(tmp_path, table_style=True)

    report = audit(source)["tables"][0]
    padding = report["width_evidence"]["cell_padding"]

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
