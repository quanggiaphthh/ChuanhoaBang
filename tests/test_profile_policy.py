"""Profile context stays explicit without claiming unverified legal presets."""
import json
from importlib.resources import files

import pytest
from docx import Document

from chuanhoabang import TableError, apply, audit, propose_header


def _document(path):
    document = Document()
    table = document.add_table(rows=2, cols=2)
    for row, values in zip(table.rows, (("STT", "Nội dung"), ("0012", "Nhiệm vụ"))):
        for cell, value in zip(row.cells, values):
            cell.text = value
    document.save(path)
    return path


def test_audit_records_selected_profile_as_reference_only(tmp_path):
    source = _document(tmp_path / "profile.docx")

    result = audit(source, profile="ND30")

    assert result["profile"] == "ND30"
    assert result["profile_status"] == "REFERENCE_ONLY"
    assert result["profile_rules_applied"] is False


def test_policy_registry_is_packaged_and_profiles_remain_unverified():
    registry_file = files("chuanhoabang").joinpath("POLICY_REGISTRY.json")
    policy = json.loads(registry_file.read_text(encoding="utf-8"))

    assert policy["profiles"]["ND30"]["verified_legal_presets"] is False
    assert policy["profiles"]["HD05"]["verified_legal_presets"] is False


def test_proposal_profile_is_checked_again_before_apply(tmp_path):
    source = _document(tmp_path / "profile.docx")
    proposal = propose_header(source, 0, profile="ND30")

    assert proposal["decision"] == "PROPOSE_APPLY"
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(source, proposal, tmp_path / "wrong-profile.docx", profile="HD05")
    assert not (tmp_path / "wrong-profile.docx").exists()


def test_cli_audit_reports_selected_profile(tmp_path, capsys):
    from chuanhoabang.cli import main

    source = _document(tmp_path / "profile.docx")
    assert main(["audit", str(source), "--profile", "HD05"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["profile"] == "HD05"
    assert result["profile_status"] == "REFERENCE_ONLY"


def test_wrong_profile_name_is_rejected_before_docx_read(tmp_path):
    with pytest.raises(TableError, match="UNKNOWN_PROFILE"):
        audit(tmp_path / "missing.docx", profile="CUSTOM")
