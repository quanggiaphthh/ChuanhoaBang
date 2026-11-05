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


def test_markdown_render_exposes_non_body_story_table_inventory():
    report = render_markdown({
        "table_count": 1,
        "non_body_story_table_count": 1,
        "non_body_story_tables": [{
            "part": "word/header1.xml",
            "story_table_index": 0,
            "table_sha256": "a" * 64,
            "owner_status": "SECTION_RELATIONSHIP_NOT_RESOLVED",
            "status": "REVIEW_REQUIRED",
            "reason": "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX",
        }],
    })
    assert "| non_body_story_table_count | 1 |" in report
    assert "## Bảng trong header/footer/footnote/endnote" in report
    assert "word/header1.xml" in report
    assert "a" * 64 in report
    assert "SECTION_RELATIONSHIP_NOT_RESOLVED" in report


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


def test_markdown_report_cannot_overwrite_docx_or_proposal(tmp_path, capsys):
    source = tmp_path / "sample.docx"
    doc = Document()
    table = doc.add_table(rows=2, cols=2)
    for row, values in zip(table.rows, (("STT", "Nội dung"), ("0012", "Dữ liệu"))):
        for cell, value in zip(row.cells, values):
            cell.text = value
    doc.save(source)
    before = source.read_bytes()
    proposal_file = tmp_path / "proposal.json"
    assert main(["propose-header", str(source), "--table", "0", "--output",
                 str(proposal_file), "--report-md", str(proposal_file)]) == 2
    assert not proposal_file.exists()
    assert main(["audit", str(source), "--report-md", str(source)]) == 2
    assert source.read_bytes() == before
    assert main(["propose-header", str(source), "--table", "0",
                 "--output", str(proposal_file)]) == 0
    proposal_before = proposal_file.read_bytes()
    target = tmp_path / "output.docx"
    assert main(["apply", str(source), "--proposal", str(proposal_file),
                 "--output", str(target), "--report-md", str(target)]) == 2
    assert not target.exists()
    assert proposal_file.read_bytes() == proposal_before
