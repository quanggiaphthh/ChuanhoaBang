"""Profile context stays explicit without claiming unverified legal presets."""
import json
from importlib.resources import files

import pytest
from docx import Document
from docx.shared import Pt

from chuanhoabang import TableError, apply, audit, propose_header
from chuanhoabang import core


def _document(path):
    document = Document()
    table = document.add_table(rows=2, cols=2)
    for row, values in zip(table.rows, (("STT", "Nội dung"), ("0012", "Nhiệm vụ"))):
        for cell, value in zip(row.cells, values):
            cell.text = value
    document.save(path)
    return path


class SyntheticMetricFont:
    def getlength(self, text):
        return len(text) * 5


def _font_document(path, size_pt):
    document = Document()
    table = document.add_table(rows=3, cols=3)
    values = (("STT", "Nội dung", "Ghi chú"),
              ("0012", "Nhiệm vụ", "Đang làm"),
              ("0", "Kết quả", "Hoàn thành"))
    for row, cells in zip(table.rows, values):
        for cell, value in zip(row.cells, cells):
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            run.font.name = "Times New Roman"
            run.font.size = Pt(size_pt)
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
    assert policy["profiles"]["ND30"]["table_width_measurement"]["font_sizes_pt"] == [13, 14]
    assert policy["profiles"]["HD05"]["table_width_measurement"]["font_sizes_pt"] == [14]
    for profile in ("ND30", "HD05"):
        source = policy["profiles"][profile]["table_width_measurement"]["official_sources"][0]
        assert source["text_url"].startswith("https://")
        assert source["locator"]


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


def test_tampered_profile_metric_constraints_are_rejected_on_apply(tmp_path, monkeypatch):
    source = _document(tmp_path / "profile.docx")
    actual = {
        "input_sha256": "input", "table_sha256": "table", "table_index": 0,
        "policy": core.POLICY_VERSION, "decision": "PROPOSE_APPLY", "reasons": [],
        "candidate_twips": [1000, 1000], "profile": "HD05",
        "profile_status": "REFERENCE_ONLY", "profile_rules_applied": False,
        "profile_constraints": {
            "scope": "WIDTH_METRIC_ELIGIBILITY",
            "rule_id": "V16-FONT-02",
            "font_sizes_pt": [14],
            "selection_basis": core.POLICY_REGISTRY["profiles"]["HD05"][
                "table_width_measurement"]["selection_basis"],
            "official_sources": json.loads(json.dumps(core.POLICY_REGISTRY["profiles"]["HD05"][
                "table_width_measurement"]["official_sources"])),
        },
    }
    monkeypatch.setattr(core, "propose", lambda *_args, **_kwargs: actual)
    altered = {**actual, "profile_constraints": {**actual["profile_constraints"],
                                                 "font_sizes_pt": [13]}}
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(source, altered, tmp_path / "altered.docx", profile="HD05")
    assert not (tmp_path / "altered.docx").exists()
    without_constraints = dict(actual)
    without_constraints.pop("profile_constraints")
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(source, without_constraints, tmp_path / "missing-scope.docx", profile="HD05")
    assert not (tmp_path / "missing-scope.docx").exists()


@pytest.mark.parametrize(("profile", "size_pt", "supported", "rule_id", "font_sizes"), [
    ("ND30", 13, True, "V16-FONT-01", [13, 14]),
    ("ND30", 14, True, "V16-FONT-01", [13, 14]),
    ("HD05", 14, True, "V16-FONT-02", [14]),
    ("HD05", 13, False, "V16-FONT-02", [14]),
    ("HD05", 15, False, "V16-FONT-02", [14]),
])
def test_width_measurement_size_gate_is_profile_specific(
        tmp_path, monkeypatch, profile, size_pt, supported, rule_id, font_sizes):
    source = _font_document(tmp_path / "profile-font.docx", size_pt)
    font_file = tmp_path / "synthetic-font-metrics.bin"
    font_file.write_bytes(b"not-a-font; metrics are patched in the test")
    monkeypatch.setattr(core, "_load_fonts",
                        lambda *_args: (SyntheticMetricFont(), SyntheticMetricFont()))

    proposal = core.propose(source, 0, font_regular=font_file, profile=profile)

    assert proposal["profile_status"] == "REFERENCE_ONLY"
    assert proposal["profile_rules_applied"] is False
    assert proposal["profile_constraints"] == {
        "scope": "WIDTH_METRIC_ELIGIBILITY", "rule_id": rule_id,
        "font_sizes_pt": font_sizes,
        "selection_basis": core.POLICY_REGISTRY["profiles"][profile][
            "table_width_measurement"]["selection_basis"],
        "official_sources": core.POLICY_REGISTRY["profiles"][profile][
            "table_width_measurement"]["official_sources"],
    }
    original_source = core.POLICY_REGISTRY["profiles"][profile][
        "table_width_measurement"]["official_sources"][0]
    original_locator = original_source["locator"]
    proposal["profile_constraints"]["official_sources"][0]["locator"] = "tampered"
    assert original_source["locator"] == original_locator
    if supported:
        assert "FONT_SIZE_OUTSIDE_PROFILE_METRIC_SCOPE" not in proposal["reasons"]
        assert proposal["decision"] in ("NO_OP_VALID", "PROPOSE_APPLY")
    else:
        assert proposal["decision"] == "REVIEW_REQUIRED"
        assert "FONT_SIZE_OUTSIDE_PROFILE_METRIC_SCOPE" in proposal["reasons"]
        assert proposal["candidate_twips"] is None
