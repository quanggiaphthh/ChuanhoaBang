"""Human-readable Markdown reports are separate from real DOCX/Word acceptance."""
from pathlib import Path

from docx import Document
from docx.shared import Pt

from chuanhoabang.cli import main, render_markdown


def test_markdown_render_has_real_line_breaks():
    report = render_markdown({
        "decision": "REVIEW_REQUIRED", "word_render": "NOT_RUN",
        "reasons": ["FONT_UNVERIFIED"], "table_index": 0})
    assert report.startswith("# ChuanhoaBang")
    assert "\\n" not in report
    assert "\n## Lý do / cảnh báo\n" in report
    assert "FONT_UNVERIFIED" in report
    assert "NOT_RUN" in report


def test_cli_audit_report_md_is_created_and_never_overwritten(tmp_path, capsys):
    source = tmp_path / "test.docx"
    doc = Document()
    table = doc.add_table(rows=2, cols=2)
    for row, values in zip(table.rows, (("STT", "Nội dung"), ("0012", "Bảo toàn"))):
        for cell, text in zip(row.cells, values):
            cell.text = ""
            run = cell.paragraphs[0].add_run(text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
    doc.save(source)
    before = source.read_bytes()
    report = tmp_path / "report.md"
    assert main(["audit", str(source), "--report-md", str(report)]) == 0
    body = report.read_text(encoding="utf-8")
    assert "0012" not in body  # report describes metadata, not user content
    assert "## Bảng được phát hiện" in body
    assert "NOT_RUN" in body
    assert source.read_bytes() == before
    assert main(["audit", str(source), "--report-md", str(report)]) == 2
    assert source.read_bytes() == before
    assert report.read_text(encoding="utf-8") == body
