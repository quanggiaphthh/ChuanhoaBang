"""Policy-file syntax and obvious authority/format safety assertions."""
import json
from pathlib import Path


def test_policy_machine_readable():
    policy = json.loads((Path(__file__).resolve().parents[1] / "docs/implementation/POLICY_REGISTRY.json").read_text("utf-8"))
    rules = policy["rules"]
    ids = [r["id"] for r in rules]
    assert len(ids) == len(set(ids))
    assert "USER-ORIENTATION-001" in ids
    assert "FONT-PROFILE-001" in ids
    for rule in rules:
        assert all(k in rule for k in ("authority", "scope", "preconditions", "severity", "safe_action",
                                      "requires_approval", "evidence_level", "postconditions"))
    assert policy["profiles"]["ND30"]["verified_legal_presets"] is False
    assert policy["profiles"]["HD05"]["verified_legal_presets"] is False
