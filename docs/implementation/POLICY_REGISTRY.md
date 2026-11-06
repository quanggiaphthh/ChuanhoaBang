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
the narrow size policy. A source review on 06/11/2026 checked the cited primary
text excerpts: the official Government Gazette copy of ND30, printed page 27,
Appendix I, Part I, Section II, item 6(e), states 13–14 pt for document text;
the official HD05 PDF, Appendix 2, row 6, lists 14–15 pt. ND30 and HD05 remain
reference-only; the registry marks legal currentness `NOT_ASSESSED` and does not
claim the excerpts establish complete or currently effective legal presets.
ND30 permits 13 or 14 pt for this project measurement scope. HD05 lists 14–15
pt for document text, while project rule `V16-FONT-02` selects 14 pt for table
width measurement and forbids automatically lowering it. These are eligibility
limits for measurement, not font-size corrections.

A legal-currentness recheck on 06/11/2026 did not change that status. The
[Ministry of Justice national legal database entry for ND30](https://vbpl.moj.gov.vn/bonoivu/Pages/vbpq-toanvan.aspx?ItemID=141142&dvid=320)
was represented in the search index as “Còn hiệu lực”, but the index reported
its page as last crawled four months earlier and the live record could not be
opened during this review. Treat this only as stale, dated index evidence. The
[official HD05 catalogue record](https://dangcongsan.vn/vanphongtrunguong/van-ban-cua-dang/huong-dan-so-05-hd-vptw-ngay-27-5-2026-cua-van-phong-trung-uong-dang-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang.html?categoryId=3000525)
was available on the review date and confirms its issue and effective dates;
it has no current-status field. A current catalogue listing alone does not
establish that the instrument has not since been changed or withdrawn. Both
profile records therefore remain `currentness: NOT_ASSESSED`,
`verified_legal_presets: false`, and `profile_status: REFERENCE_ONLY`.

Rule `TABLE-ROLE-SOURCE-CLASSIFICATION-001` adds source-only role candidates to
body-table audits and proposals: `NESTED`, `OFFICIAL_FORM_CANDIDATE`,
`LAYOUT_CANDIDATE`, `DATA_CANDIDATE`, or `UNKNOWN`. Each label carries evidence
codes, `authority: NOT_ESTABLISHED`, and `edit_gate: TABLE_STATUS_AND_OPERATION_RULES`.
Text markers can suggest a layout or official-form candidate, but do not verify
legal status. The role field does not grant edit permission; existing table
status, proposal decision, and operation-specific checks still govern changes.

Rule `TABLE-ROLE-STORY-SOURCE-CLASSIFICATION-001` reports the same candidates
for header, footer, footnote, and endnote story tables in audit output. Story
ownership remains source-derived, all non-body tables remain `REVIEW_REQUIRED`,
and none enters the body table index or gains edit permission.

Rule `NESTED-PARENT-CELL-SOURCE-LOCATION-001` adds the immediate parent cell's
zero-based row/cell location when the source XML table-row-cell chain resolves.
Malformed or unsupported topology is reported as `UNRESOLVED`; the locator is
not an effective ownership determination and grants no edit permission. Body
proposals carry the parent table/cell metadata, and `apply` checks it against a
fresh proposal before changing the DOCX.

For a width proposal, JSON and Markdown copy the metric scope, source rule ID,
allowed sizes, project selection rationale, and the registry's official source
records (`instrument`, URLs, and exact locator) into `profile_constraints`.
The proposal checker compares this metadata again during `apply`, so a changed
profile constraint, source URL, excerpt-review status, or citation makes the
proposal stale. The source records support traceability; they do not change
`profile_status: REFERENCE_ONLY` or turn `profile_rules_applied` on.

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

Audit reports `cell_grid_spans` as zero-based logical grid starts and span counts
for each physical cell when the XML mapping is unambiguous. A cell with a direct
`w:vMerge` marker also reports `vertical_merge: RESTART` or `CONTINUE` (an
omitted value is the OOXML continue form). `VERTICAL-MERGE-CHAIN-SOURCE-VALIDATION-001`
adds a source-only `vertical_merge_chain_validation` status. It checks that each
direct `CONTINUE` marker follows a marker in the immediately preceding row with
the same logical grid start and span; orphan continuations and overlapping but
misaligned ranges are `INVALID`. If cell-to-grid mapping is unresolved, the
chain result is `UNRESOLVED`. A `VALID` result does not establish Word rendering
or permit vertical-merge edits; these tables stay `REVIEW_REQUIRED` for every
proposal. Horizontal-merge tables also stay `REVIEW_REQUIRED` for width
proposals. Only the existing width-neutral header-repeat and row-height
operations accept valid horizontal spans; omitted cells, malformed spans or
merge markers, and nested tables remain unsupported. Marker semantics follow
Microsoft's [VerticalMerge.Val documentation](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge.val?view=openxml-3.0.1); this check compares local source grid ranges only.

`GRID-OMISSION-SOURCE-MAPPING-001` maps each physical cell after applying a
row's direct `w:gridBefore` count and verifies that its cells plus
`w:gridAfter` account for the declared table grid. Missing counts mean zero;
malformed, duplicate, nested, or grid-inconsistent declarations leave the
mapping unresolved. The report exposes nonzero counts as `row_grid_omissions`
in audit/proposal JSON and Markdown. Tables using omitted grid cells remain
`REVIEW_REQUIRED` for every edit. Microsoft's [GridBefore](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.gridbefore?view=openxml-3.0.1)
and [GridAfter](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.gridafter?view=openxml-3.0.1)
documentation defines the counts as skipped leading and trailing grid columns;
this mapper fails closed on conflicting declarations rather than relying on
Word's conflict recovery.

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
