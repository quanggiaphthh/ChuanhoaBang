"""Policy-file syntax and obvious authority/format safety assertions."""
import json
from importlib.resources import files


def test_policy_machine_readable():
    policy_file = files("chuanhoabang").joinpath("POLICY_REGISTRY.json")
    policy = json.loads(policy_file.read_text(encoding="utf-8"))
    rules = policy["rules"]
    ids = [r["id"] for r in rules]
    assert len(ids) == len(set(ids))
    assert "USER-ORIENTATION-001" in ids
    assert "FONT-PROFILE-001" in ids
    assert "PROFILE-METRIC-SIZE-001" in ids
    assert "TEXT-COLUMN-GEOMETRY-001" in ids
    assert "MARKUP-COMPATIBILITY-001" in ids
    assert "PROTECTION-STATE-001" in ids
    for rule in rules:
        assert all(k in rule for k in ("authority", "scope", "preconditions", "severity", "safe_action",
                                      "requires_approval", "evidence_level", "postconditions"))
    assert policy["profiles"]["ND30"]["verified_legal_presets"] is False
    assert policy["profiles"]["HD05"]["verified_legal_presets"] is False
