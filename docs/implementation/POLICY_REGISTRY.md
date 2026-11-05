# Runtime policy registry

The machine-readable registry ships with the Python package at
[`src/chuanhoabang/POLICY_REGISTRY.json`](../../src/chuanhoabang/POLICY_REGISTRY.json)
and is the runtime source for the policy version and supported profile names.

`ND30` and `HD05` remain **reference-only** profile contexts; their complete
legal presets are not verified. For width proposals only, the runtime reads each
profile's `table_width_measurement` limits from the registry and returns
`REVIEW_REQUIRED` when an effective run size falls outside that metric scope.
This check does not change font properties. Proposals disclose the checked scope
as `profile_constraints`; `profile_rules_applied: false` still means no complete
profile formatting preset has been applied. Neither field claims ND30/HD05
compliance.

The registry records the official source URLs and exact text locators used for
the narrow size policy. ND30 permits 13 or 14 pt for this project measurement
scope. HD05 lists 14–15 pt for document text, while project rule `V16-FONT-02`
selects 14 pt for table width measurement and forbids automatically lowering it.
These are eligibility limits for measurement, not font-size corrections.
