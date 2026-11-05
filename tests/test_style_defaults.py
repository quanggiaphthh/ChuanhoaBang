"""Limited style resolver: docDefaults + Normal, never pretend full Word cascade."""
import pytest
from docx import Document
from docx.shared import Pt

from chuanhoabang import propose
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


def test_run_level_tnr_overrides_non_tnr_normal(tmp_path, fake_metrics):
    source = document_fixture(tmp_path, normal_font="Arial", direct=True)
    p = propose(source, 0, font_regular=fake_metrics)
    assert p["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    assert p["evidence"] == "FONT_METRIC_ESTIMATE"
