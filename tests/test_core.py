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


def test_audit_read_only_and_header(tmp_path):
    path = fixture_docx(tmp_path)
    before = path.read_bytes()
    result = audit(path)
    assert result["table_count"] == 1
    assert result["tables"][0]["status"] == "SUPPORTED"
    assert result["geometry"]["orientation"] == "PORTRAIT"
    assert result["word_render"] == "NOT_RUN"
    assert path.read_bytes() == before


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


def test_merged_is_not_auto_formatted(tmp_path):
    path = fixture_docx(tmp_path, merged=True)
    result = audit(path)
    assert "MERGED_OR_OMITTED_CELLS" in result["tables"][0]["reasons"]
    assert propose(path, 0)["decision"] == "REVIEW_REQUIRED"


def test_protected_document_blocks(tmp_path):
    path = fixture_docx(tmp_path, protected=True)
    assert "DOCUMENT_PROTECTED" in audit(path)["global_locks"]
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


def test_width_patch_preserves_whole_document_and_source(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    meta = audit(path)["tables"][0]
    base = meta["grid_twips"]
    candidate = [base[0] + 200, base[1] - 400, base[2] + 200]
    assert min(candidate) > 0
    proposal = {"input_sha256": audit(path)["input_sha256"], "table_sha256": meta["table_sha256"],
                "table_index": 0, "policy": core.POLICY_VERSION, "decision": "PROPOSE_APPLY",
                "candidate_twips": candidate, "evidence": "MOCK_TEST_ONLY"}
    # Isolate the patch/invariant writer from actual font shaping in this test.
    monkeypatch.setattr(core, "propose", lambda *a, **k: proposal)
    source_hash = core.digest(path.read_bytes())
    target = tmp_path / "formatted.docx"
    report = apply(path, proposal, target)
    assert report["decision"] == "APPLIED"
    assert report["content_integrity"] == "PASS"
    assert report["word_render"] == "NOT_RUN"
    assert core.digest(path.read_bytes()) == source_hash
    original = Document(path)
    result = Document(target)
    before = [[c.text for c in r.cells] for r in original.tables[0].rows]
    after = [[c.text for c in r.cells] for r in result.tables[0].rows]
    assert before == after
    assert after[1][0] == "0012"
    assert after[2][0] == "0"
    with pytest.raises(TableError, match="OUTPUT_MUST_BE_NEW_PATH"):
        apply(path, proposal, target)


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


def test_proposal_modification_and_invalid_zip_are_rejected(tmp_path, monkeypatch):
    path = fixture_docx(tmp_path)
    meta = audit(path)["tables"][0]
    fake = {"input_sha256": audit(path)["input_sha256"], "table_sha256": meta["table_sha256"],
            "table_index": 0, "policy": core.POLICY_VERSION, "decision": "PROPOSE_APPLY",
            "candidate_twips": meta["grid_twips"], "evidence": "MOCK_TEST_ONLY"}
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
            "decision": "PROPOSE_APPLY", "candidate_twips": list(base["grid_twips"]), "evidence": "MOCK_TEST_ONLY"}
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
    (2, False, None, "MULTICOLUMN_SECTION"),
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
