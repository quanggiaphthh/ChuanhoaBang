# Runtime policy registry

The machine-readable registry ships with the Python package at
[`src/chuanhoabang/POLICY_REGISTRY.json`](../../src/chuanhoabang/POLICY_REGISTRY.json)
and is the runtime source for the policy version and supported profile names.

`ND30` and `HD05` are currently **reference-only** profile contexts. Their legal
presets are not verified and the engine does not apply profile-specific rules.
Reports mark the selected profile and set `profile_rules_applied` to `false`;
this is not a claim of ND30/HD05 compliance.
