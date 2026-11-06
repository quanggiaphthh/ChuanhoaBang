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

For a width proposal, JSON and Markdown copy the metric scope, source rule ID,
allowed sizes, project selection rationale, and the registry's official source
records (`instrument`, URLs, and exact locator) into `profile_constraints`.
The proposal checker compares this metadata again during `apply`, so a changed
profile constraint or citation makes the proposal stale. The source records
support traceability; they do not change `profile_status: REFERENCE_ONLY` or
turn `profile_rules_applied` on.

Rule `TEXT-COLUMN-GEOMETRY-001` (registry revision `TEXT-COLUMN-GEOMETRY-003`)
supports explicit equal-width columns and explicit `equalWidth=0` custom
columns. Custom columns require a matching count, positive `w:w` values,
explicit nonnegative spacing between adjacent columns, and a combined width
within the section text area. When the table's column placement is unknown,
`available_twips` uses the narrowest declared column as a conservative bound
for any possible placement; the report also retains each source width and
spacing. Missing or malformed values and ambiguous sections remain
`GEOMETRY_UNKNOWN`. None of these source-derived bounds is a Word-rendered
measurement.

The custom-column interpretation follows Microsoft's
[equalWidth](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.columns.equalwidth?view=openxml-3.0.1)
and [column spacing](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.columns.space?view=openxml-3.0.1)
documentation. Microsoft documents Word's default of `equalWidth=true` when
omitted and its requirement that a false `equalWidth` column count match the
child `col` count in [MS-OI29500](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oi29500/ef7027d4-e05d-473b-8777-dcc2aee91935).

The registry also carries `MARKUP-COMPATIBILITY-001` and
`PROTECTION-STATE-001`. Any `mc:AlternateContent` in `word/document.xml` keeps
body tables in review because the runtime does not choose among compatibility
branches. Any `w:permStart`/`w:permEnd` markers block body-table proposals because
the runtime does not resolve permission ranges against the caller's identity.
An enforced, malformed, or duplicate `w:documentProtection` declaration also
blocks proposals. See Microsoft's [AlternateContent extension
rules](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-docx/ec34035b-0da9-4849-a064-e4e57d1e7245), [permission
markers](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.permstart?view=openxml-3.0.1),
and [documentProtection enforcement](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oi29500/e12d2773-e2d0-45bf-b1c2-b8f0548e156d).

Registry rule `UNSUPPORTED-PACKAGE-CONTENT-001` blocks proposals when the OPC
member list contains a conventional `_xmlsignatures/` part or
`word/vbaProject.bin`. This is a fail-closed presence check; it does not
validate signature cryptography or execute macros. Synthetic marker-part
regressions cover both signals.

`UNICODE-LINEBREAK-001` covers only a conservative metric-estimate guard: U+00A0,
U+180E, U+2007, and U+202F stay grouped with adjacent text. The tokenizer is
not a complete Unicode line-breaking implementation or a Word renderer; see
[Unicode UAX #14](https://unicode.org/reports/tr14/).
