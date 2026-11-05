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
