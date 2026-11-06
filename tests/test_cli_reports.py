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
        "non_body_story_table_count": 2,
        "non_body_story_tables": [
            {
                "part": "word/header1.xml",
                "story_types": ["header"],
                "story_table_index": 0,
                "table_id": "word/header1.xml#table=0:outer1234",
                "parent_table_id": None,
                "table_sha256": "a" * 64,
                "owner_status": "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED",
                "section_references": [{
                    "section_index": 0,
                    "story_type": "header",
                    "reference_type": "first",
                    "activation": {
                        "status": "ENABLED", "control": "w:titlePg",
                        "evidence": "SOURCE_XML_ONLY",
                    },
                }],
                "status": "REVIEW_REQUIRED",
                "reason": "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX",
            },
            {
                "part": "word/header1.xml",
                "story_types": ["header"],
                "story_table_index": 1,
                "table_id": "word/header1.xml#table=1:child1234",
                "parent_table_id": "word/header1.xml#table=0:outer1234",
                "table_sha256": "b" * 64,
                "owner_status": "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED",
                "section_references": [{
                    "section_index": 0,
                    "story_type": "header",
                    "reference_type": "default",
                }],
                "first_even_inheritance_candidates": [{
                    "section_index": 1,
                    "story_type": "header",
                    "reference_type": "even",
                    "inherited_from_section_index": 0,
                    "activation": {
                        "status": "ENABLED", "control": "w:evenAndOddHeaders",
                        "evidence": "SOURCE_XML_ONLY",
                    },
                }],
                "status": "REVIEW_REQUIRED",
                "reason": "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX",
            },
        ],
    })
    assert "| non_body_story_table_count | 2 |" in report
    assert "## Bảng trong header/footer/footnote/endnote" in report
    assert "Story type" in report
    assert "| header |" in report
    assert "word/header1.xml" in report
    assert "word/header1.xml#table=0:outer1234" in report
    assert "word/header1.xml#table=1:child1234" in report
    assert "Parent table ID" in report
    assert "a" * 64 in report
    assert "DIRECT_REFERENCES_FOUND_INHERITANCE_UNRESOLVED" in report
    assert "section 0 header/default" in report
    assert "section 0 header/first (source activation ENABLED; w:titlePg; SOURCE_XML_ONLY)" in report
    assert "possible inherited section 1 header/even from section 0 " \
           "(section activation ENABLED; w:evenAndOddHeaders; SOURCE_XML_ONLY)" in report

    note_report = render_markdown({
        "non_body_story_tables": [{
            "part": "word/footnotes.xml",
            "story_types": ["footnotes"],
            "story_table_index": 0,
            "table_id": "word/footnotes.xml#table=0:note1234",
            "parent_table_id": None,
            "table_sha256": "c" * 64,
            "owner_status": "SECTION_RELATIONSHIP_NOT_RESOLVED",
            "section_references": [],
            "note_reference": {
                "note_type": "footnote",
                "note_id": "1",
                "status": "BODY_REFERENCE_FOUND",
                "body_reference_count": 1,
                "reference_scope": "WORD_DOCUMENT_BODY_XML_ONLY",
                "evidence": "SOURCE_XML_ONLY",
            },
            "status": "REVIEW_REQUIRED",
            "reason": "NON_BODY_STORY_NOT_IN_EDITABLE_TABLE_INDEX",
        }],
    })
    assert "Reference evidence" in note_report
    assert "footnote id 1 BODY_REFERENCE_FOUND" in note_report
    assert "body_reference_count=1" in note_report
    assert "WORD_DOCUMENT_BODY_XML_ONLY" in note_report
    assert "SOURCE_XML_ONLY" in note_report


def test_markdown_render_distinguishes_declared_grid_and_word_widths():
    report = render_markdown({
        "table_count": 1,
        "tables": [{
            "index": 0,
            "table_id": "body:0:abc123",
            "parent_table_id": None,
            "status": "SUPPORTED",
            "rows": 1,
            "columns": 2,
            "grid_twips": [1000, 2000],
            "reasons": [],
            "width_evidence": {
                "table_preferred": {
                    "status": "DECLARED", "type": "pct", "raw_value": "5000", "twips": None,
                },
                "cell_preferred": [[
                    {"status": "DECLARED", "type": "dxa", "raw_value": "1000", "twips": 1000},
                    {"status": "DECLARED", "type": "pct", "raw_value": "2500", "twips": None},
                ]],
                "grid_sum_twips": 3000,
                "word_rendered": "NOT_RUN",
            },
        }],
    })

    assert "## Width evidence (OOXML declarations; not Word measurements)" in report
    assert "tblW preferred" in report
    assert "grid=[1000, 2000] twips; sum=3000 twips" in report
    assert "pct:5000" in report
    assert "r0c0=dxa:1000 twips" in report
    assert "r0c1=pct:2500" in report
    assert "NOT_RUN" in report


def test_markdown_render_exposes_cell_padding_matrix_and_assumption():
    report = render_markdown({
        "table_count": 1,
        "tables": [{
            "index": 0,
            "table_id": "body:0:abc123",
            "parent_table_id": None,
            "status": "SUPPORTED",
            "rows": 2,
            "columns": 2,
            "grid_twips": [1000, 2000],
            "reasons": [],
            "width_evidence": {
                "table_preferred": {"status": "ABSENT"},
                "cell_preferred": [],
                "grid_sum_twips": 3000,
                "cell_padding": {
                    "status": "RESOLVED",
                    "basis": "EXPLICIT_DXA_AND_DEFAULT_ASSUMPTION",
                    "assumed_default_twips": 240,
                    "twips_by_row": [[700, 240], [240, 240]],
                },
                "word_rendered": "NOT_RUN",
            },
        }],
    })

    assert "Cell padding evidence" in report
    assert "status=RESOLVED" in report
    assert "basis=EXPLICIT_DXA_AND_DEFAULT_ASSUMPTION" in report
    assert "fallback=240 twips" in report
    assert "per-cell twips: r0=[700, 240]; r1=[240, 240]" in report


def test_markdown_render_exposes_unresolved_table_style_padding():
    report = render_markdown({
        "table_count": 1,
        "tables": [{
            "index": 0,
            "table_id": "body:0:abc123",
            "parent_table_id": None,
            "status": "SUPPORTED",
            "rows": 2,
            "columns": 2,
            "grid_twips": [1000, 2000],
            "reasons": [],
            "width_evidence": {
                "table_preferred": {"status": "ABSENT"},
                "cell_preferred": [],
                "grid_sum_twips": 3000,
                "cell_padding": {
                    "status": "UNRESOLVED",
                    "reason": "TABLE_STYLE_CASCADE_NOT_SUPPORTED",
                },
                "word_rendered": "NOT_RUN",
            },
        }],
    })

    assert "status=UNRESOLVED" in report
    assert "TABLE_STYLE_CASCADE_NOT_SUPPORTED" in report
    assert "fallback=not used" in report


def test_markdown_render_identifies_resolved_table_style_margin_source():
    report = render_markdown({
        "table_count": 1,
        "tables": [{
            "index": 0,
            "table_id": "body:0:abc123",
            "parent_table_id": None,
            "status": "SUPPORTED",
            "rows": 1,
            "columns": 1,
            "grid_twips": [1000],
            "reasons": [],
            "width_evidence": {
                "table_preferred": {"status": "ABSENT"},
                "cell_preferred": [],
                "grid_sum_twips": 1000,
                "cell_padding": {
                    "status": "RESOLVED",
                    "basis": "TABLE_STYLE_DXA",
                    "assumed_default_twips": None,
                    "twips_by_row": [[156]],
                    "table_style": {
                        "status": "RESOLVED",
                        "style_id": "TableGrid",
                        "based_on_chain": ["TableNormal", "TableGrid"],
                        "margin_source_style_id": "TableNormal",
                        "horizontal_margin_twips": {"left": 72, "right": 84},
                        "margin_used": True,
                    },
                },
                "word_rendered": "NOT_RUN",
            },
        }],
    })

    assert "table style=TableGrid" in report
    assert "margin source=TableNormal (left=72, right=84 twips)" in report
    assert "chain=TableNormal -> TableGrid" in report
    assert "style margin used=yes" in report


def test_markdown_render_exposes_conservative_column_width_bound():
    report = render_markdown({
        "geometry": {
            "status": "STRUCTURAL",
            "orientation": "PORTRAIT",
            "sections": 1,
            "page_text_width_twips": 16000,
            "available_twips": 7500,
            "available_width_scope": "EQUAL_WIDTH_COLUMN_LOWER_BOUND",
            "column_count": 2,
            "column_gap_twips": 1000,
        },
        "word_render": "NOT_RUN",
    })

    assert "## Geometry evidence" in report
    assert "EQUAL_WIDTH_COLUMN_LOWER_BOUND" in report
    assert "7500 twips" in report
    assert "2" in report
    assert "1000 twips" in report
    assert "NOT_RUN" in report


def test_markdown_render_exposes_custom_column_geometry():
    report = render_markdown({
        "geometry": {
            "status": "STRUCTURAL",
            "orientation": "PORTRAIT",
            "sections": 1,
            "page_text_width_twips": 16000,
            "column_count": 3,
            "custom_column_widths_twips": [6000, 3500, 5000],
            "custom_column_spacing_after_twips": [500, 700, None],
            "available_width_scope": "CUSTOM_COLUMN_MINIMUM_LOWER_BOUND",
            "available_twips": 3500,
        },
        "word_render": "NOT_RUN",
    })

    assert "CUSTOM_COLUMN_MINIMUM_LOWER_BOUND" in report
    assert "6000 twips, 3500 twips, 5000 twips" in report
    assert "500 twips, 700 twips, UNSPECIFIED" in report
    assert "3500 twips" in report
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
