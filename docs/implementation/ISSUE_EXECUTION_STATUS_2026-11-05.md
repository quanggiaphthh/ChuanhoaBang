# ChuanhoaBang — Issue execution status (06/11/2026)

**Baseline:** main 13be13e0d34ee7f603a2bdd24e84493d7cae4c33  
**Implementation:** PR [#17](https://github.com/quanggiaphthh/ChuanhoaBang/pull/17), branch `feat/offline-docx-table-core-v01`.  
**Latest verified code:** PR commit [`ad7e120c1f4cb865f0d17ff4333428933ff0f8b4`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/ad7e120c1f4cb865f0d17ff4333428933ff0f8b4), [GitHub Actions run 42169656269](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42169656269): all six jobs succeeded; **210/210 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; each target passed hash-enforced offline install, CLI/DOCX audit smoke, and wheel smoke. The preview manifest records canonical and same-run rebuilt wheel SHA-256 `d3f7825941d68bf2ecf823cf6a1c8472cb0fe06300b699472712dc7277bbdf13`. Direct border, layout, direction, cell-spacing, border-space, and border-size declarations are reported in body/story audits; effective border geometry, layout, direction, spacing, and Word rendering remain `NOT_RESOLVED`/`NOT_RUN`. Word/WPS and original fixtures remain unavailable; profile legal currentness remains `NOT_ASSESSED`. Preview artifact `chuanhoabang-preview-58962bd54f4c724fef6548a314024760f994b038` expires 20/11/2026.

> This is a technical preview. All issues remain open until their acceptance criteria are fully met and work is merged as appropriate. Not a production release.

## Issue-by-issue evidence

| Issue | Current delivery | Still required | State |
|---|---|---|---|
| [#1](https://github.com/quanggiaphthh/ChuanhoaBang/issues/1) ADR/capability | ADR evaluates Python OOXML / WordVN / .NET; WordVN repo inspected | Review/update final integration choice when editor exists | PARTIAL |
| [#2](https://github.com/quanggiaphthh/ChuanhoaBang/issues/2) policies | Packaged runtime registry; ND30/HD05 selection and proposal binding; sourced profile-specific width-metric size gate; proposal JSON/Markdown carry rationale and official source URL/locator; cited ND30/HD05 primary-source excerpts and legal-currentness recheck recorded 06/11/2026, with currentness still NOT_ASSESSED; orientation, markup-compatibility, protection-state, unsupported-package-content, Unicode line-break, versioned cell-margin, grid/vertical-merge source validation, matched role-marker, `TABLE-BORDER-SOURCE-EVIDENCE-001`, `TABLE-LAYOUT-SOURCE-EVIDENCE-001`, `TABLE-DIRECTION-SOURCE-EVIDENCE-001`, `TABLE-CELL-SPACING-SOURCE-EVIDENCE-001`, `TABLE-BORDER-GEOMETRY-GATE-001`, and `TABLE-BORDER-SIZE-GATE-001` policies (run 42169656269, 210 tests) | Complete verified profile presets, currentness/authority classification, and legal rule coverage | PARTIAL |
| [#3](https://github.com/quanggiaphthh/ChuanhoaBang/issues/3) fixtures | Fixture inventory and provenance notes; local/Drive search did not locate originals; latest verified GitHub suite has 210 tests; original DOCX fixture count remains 0 | Obtain original checksum-verified F01–F08 & V15 binaries | BLOCKED_PARTIAL |
| [#4](https://github.com/quanggiaphthh/ChuanhoaBang/issues/4) OPC reader | Read-only body/story inventory; source-local table IDs, nested parent links and hashes plus zero-based parent row/cell locators when source topology resolves; direct section references plus same-type default and active first/even inheritance candidates; all four non-body story types follow internal relationships and custom parts expose their type; note tables include same-type document-body reference counts and duplicate/invalid/missing-ID states; valid horizontal/vertical source markers, valid `gridBefore`/`gridAfter` rows, and vertical continuation range checks expose source-only logical-grid mapping and diagnostics; direct border, layout, direction, cell-spacing, border-space, and border-size declarations are reported for body/story tables with source coordinates; run 42169656269 passed 210/210 | Validate grid mapping and vertical chains against original fixtures; resolve ownership candidates and Word-effective inheritance/rendering | PARTIAL |
| [#5](https://github.com/quanggiaphthh/ChuanhoaBang/issues/5) classification | Layout/lock/complex refusal, MCE, permission-range, document-protection, signed-package and macro-part review gates, table-wide marker scan, source-evidence role candidates and fixed-vocabulary matched markers for body/story tables (run 42158558757, 184 tests across five targets), plus nested parent-cell source locators (run 42157549045); candidates/locators do not establish authority, effective story ownership, or edit permission | Formal sample corpus to measure false negatives, legal-authority validation, and broader table semantics | PARTIAL |
| [#6](https://github.com/quanggiaphthh/ChuanhoaBang/issues/6) geometry | Single-section geometry, gutter/orientation gates, equal/custom-column lower bounds, bounded paragraph-style inheritance, distinct `tblW`/`tcW`/`tblGrid` evidence, direct dxa margin resolution, bounded table-style baseline margin chain, and direct `w:tblLayout`, `w:bidiVisual`, `w:tblCellSpacing`, border `w:space`, and border `w:sz` evidence; active RTL order, nonzero/ambiguous cell spacing, and nonzero/ambiguous border geometry block width proposals (run 42169656269, 210/210) | Resolve conditional/effective style cascade, actual table-to-column placement, nested/story ownership, remaining style cascade, and Word page-position evidence | PARTIAL |
| [#7](https://github.com/quanggiaphthh/ChuanhoaBang/issues/7) glyphs | Optional local Pillow/RAQM; supported style chain and face metadata gates; nonbreaking spaces stay unbroken in the metric estimate | Licensed genuine TNR face validation, full Unicode line-break/shaping evidence | BLOCKED_PARTIAL |
| [#8](https://github.com/quanggiaphthh/ChuanhoaBang/issues/8) width | Bounded optimizer on rectangular tables; active `w:bidiVisual`, nonzero cell spacing, unresolved spacing declarations, and nonzero/ambiguous direct border `w:space`/`w:sz` fail closed; no automatic landscape (run 42169656269, 210/210) | Real font/renderer validation and historical fixture comparison | PARTIAL |
| [#9](https://github.com/quanggiaphthh/ChuanhoaBang/issues/9) patch | Operation-specific OOXML whitelist; stale proposal guard includes package locks and `table_layout_evidence`, `table_direction_evidence`, `table_cell_spacing_evidence`, and `border_geometry_evidence` with direct border size declarations; non-target parts/path safety; post-write validation cleanup; atomic no-overwrite publish; byte-identical repeated apply returns `NO_OP_VALID`; run 42169656269 passed 210/210 | Broader DOCX interoperability, release/update rollback, power-loss durability and remaining merge/review cases | PARTIAL |
| [#10](https://github.com/quanggiaphthh/ChuanhoaBang/issues/10) CLI/API | Public Python API and CLI audit/propose/explicit apply; JSON/Markdown include cell padding, table style, story ownership candidates, note linkage, profile evidence, logical-grid diagnostics, nested parent locations, direct border/layout/direction/cell-spacing/border-space/border-size evidence in body/story audits and proposals; run 42169656269 passed 210/210; omitted-cell and vertical edits remain blocked | End-to-end user document acceptance | PARTIAL |
| [#11](https://github.com/quanggiaphthh/ChuanhoaBang/issues/11) pages | Repeat first header, exact→atLeast opt-in; supports valid horizontal gridSpan-only for paging; omitted-cell rows and vertical-merge tables remain refused; LO synthetic smoke | Conditional row split, Word Print Layout acceptance | PARTIAL |
| [#12](https://github.com/quanggiaphthh/ChuanhoaBang/issues/12) complex | Source-only horizontal cell-to-grid spans, vertical `vMerge` markers and continuation-to-restart range checks, plus validated `gridBefore`/`gridAfter` omission mapping; Word-effective rendering remains unverified; all vertical/omitted-cell edits remain blocked; width-neutral paging is supported only for valid horizontal spans; width optimization waits for licensed TNR and Word geometry gates | Broader topology and Word tests | PARTIAL |
| [#13](https://github.com/quanggiaphthh/ChuanhoaBang/issues/13) regression | GitHub Actions run 42169656269: 210 PASS across 5 environments incl archive/profile/geometry/rollback/classifier/story-ownership/protection/signature/macro/stale-apply/Unicode width guards, direct layout/direction/cell-spacing/border-space/border-size evidence and refusal, source preservation across width patch, CLI body/story reporting, repeat-apply idempotence, offline install, and canonical wheel rebuild | Original F01–F08/V15 plus target renderer cases | PARTIAL |
| [#14](https://github.com/quanggiaphthh/ChuanhoaBang/issues/14) Word/WPS QA | LibreOffice secondary smoke; [repeatable Microsoft Word protocol](../verification/WORD_ACCEPTANCE_PROTOCOL.md) | Independent Microsoft Word and WPS evidence on supported fixtures | NOT_RUN |
| [#15](https://github.com/quanggiaphthh/ChuanhoaBang/issues/15) WordVN | GitHub `quanggiaphthh/WordVN` main inspected: only README | Editor importer/exporter, selection/Undo API must exist before adapter | BLOCKED |
| [#16](https://github.com/quanggiaphthh/ChuanhoaBang/issues/16) release | Locked runtime/test dependencies; exact build backend pins; source/lock/artifact manifests; target-specific offline wheelhouses with hash-enforced `--no-index` installs across 5 environments; versioned `0.1.0.dev0` preview note; [run 42169656269](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42169656269) passed 210/210; canonical and same-run rebuilt wheel SHA-256 `d3f7825941d68bf2ecf823cf6a1c8472cb0fe06300b699472712dc7277bbdf13` | Official tag/release, release/update rollback, power-loss durability, Word/WPS acceptance, original fixtures, remaining security/compatibility gates | PARTIAL |

## Delivered changes beyond original PR bootstrap

- Safety fail-closed against additional OOXML fields, comments, bookmarks, permission ranges, wrapped content, plus **7 regressions**.
- Corrected GitHub workflow to run the *entire focused test directory*, not just two legacy test modules.
- Added human-readable Markdown reports to CLI, with strict collision checks for DOCX, proposal JSON, input and Markdown report paths.
- Added negative regression coverage for report conflicts; **49 focused tests PASS**.
- Reduced CI duplication: push main / PR / optional manual dispatch, rather than double-running push and PR on a feature branch.
- Added a locked runtime/test graph and a canonical preview-wheel build. CI repeats the build, records a SHA-256 manifest, and tests the same artifact on all supported environments.
- Added fail-closed mirrored-margin/gutter geometry handling and a post-write validation rollback regression.
- Layout/signature hints now fail closed when found in any table row; DOCX publication fails closed if another process creates the requested output after initial validation.
- `audit` now counts and hashes tables in header/footer/footnotes/endnotes separately from body table indices; the CLI Markdown report exposes these stories and preserves their unsupported status.
- Explicit header/footer relationship IDs now map to zero-based section indices and reference types. Duplicate IDs, unreferenced parts, and inherited linkage remain unresolved; tests cover first/second sections and the unreferenced/ambiguous cases.
- Body and non-body story inventories assign deterministic IDs from their scope/index/table hash and link nested tables to their immediate parent ID; the existing body index remains the `--table` selector.
- The release workflow now emits target-specific runtime wheelhouses with a per-wheel SHA-256 manifest; fresh `pip --no-index` installs and a separate-runner canonical-wheel rebuild are release checks.
- The wheelhouse install requirements pin the application wheel and every runtime wheel by SHA-256; CI installs with both `--no-index` and `--require-hashes`.

## Release decision

**NO-GO for v1.0/official Word acceptance.**  
**GO for continued development of technical preview in PR #17.**

The absence of licensed Times New Roman validation, original corpus, Word/WPS evidence, WordVN editor API, and merged/nested implementation is **not** a code-review shortcut or a successful test. No issue automatically closes merely because a related subcomponent exists.

## Next minimum-value execution

1. Get genuine local Times New Roman measurements and run paired candidate/baseline on real fixture DOCX when available.
2. Build verified fixture inventory and test normal vs locked/complex/multi-page cases.
3. Expand merged-cell width optimizer only after licensed font/Word geometry gates hold; current gridSpan support is restricted to non-width paging operations.
4. Run official Microsoft Word and WPS compatibility acceptance before v1.0.
5. Build a thin WordVN adapter when WordVN's own editor API is implemented; do not create a duplicate editor.

## Tiến độ bổ sung — đặc tả sửa an toàn cho bảng gộp

- **CB-09:** cấm thay đổi width trong bản vá header/height, chỉ cho thay `hRule` tại row_indices được chỉ định; bổ sung 6 negative/positive tests.
- **CB-11/CB-12:** hỗ trợ `gridSpan` ngang hợp lệ cho lặp tiêu đề đầu và `exact→atLeast`; **không** sửa width của bảng gộp. Gộp dọc, nested và malformed grid vẫn REVIEW.
- **CB-13:** 43/43 CI PASS trên test synthetic sau thay đổi (commit `dfe9c4c9c3d84d7d42f735600fdcea3eb51dbb67`).
- **Tình trạng issue:** chưa tự động đóng #9/#11/#12/#13; đều mới đạt phạm vi kiểm thử cấu trúc, chưa hoàn thành yêu cầu nghiệm thu Word và corpus thật.

## Bổ sung CB-06/07 — inherited styles (05/11/2026)

- Đọc `docDefaults` và style paragraph mặc định `Normal` khi run chưa khai báo trực tiếp font/cỡ, không suy diễn toàn bộ Word style cascade.
- Paragraph-style chain có `basedOn` tường minh tới default style được giải trong subset; chuỗi cycle/thiếu cha, character/table style, theme font và hiệu ứng style chưa hỗ trợ trả `REVIEW_REQUIRED`; không ép font, không dùng fallback ngầm.
- 6 ca synthetic style mới, tổng **49/49 CI PASS** tại [run 42044532089](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42044532089).
- Kiểm thử dùng metric font giả lập để kiểm logic, **không** phải TNR thật và không nghiệm thu Word.

## CB-02 follow-up — packaged profile provenance

- `POLICY_REGISTRY.json` is now package data and supplies the runtime policy version and accepted profile identifiers; documentation points to that single registry.
- `audit`, `propose`, `propose-header`, `propose-unclip`, and `apply` accept `ND30`/`HD05`. Reports mark them `REFERENCE_ONLY` and `profile_rules_applied: false`; this records user context without claiming legal compliance.
- `apply` rechecks the proposal profile and rejects a profile mismatch. Unknown profiles fail before reading the DOCX.
- Local verification at profile-context commit `7ab5805`: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/` — **54 PASS** on Python 3.12. Wheel build and isolated-target install smoke passed; packaged registry and `python -m chuanhoabang --help` were available. GitHub Actions run [42070003513](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42070003513) then completed **54 PASS** on Python 3.11.
- Profile-specific authority verification, genuine Times New Roman, original F01–F08 fixtures, Microsoft Word/WPS rendering, and v1.0 acceptance remain **NOT_RUN / BLOCKED** as recorded above.

## CB-06/07 follow-up — explicit paragraph-style inheritance

- Added a bounded `basedOn` resolver for paragraph styles that explicitly reach the document's default paragraph style; inherited `docDefaults` and run properties are then used by the existing metric path.
- Missing/cyclic parents, character styles, table styles, theme fonts, inherited bold/italic toggles, and other unsupported run properties remain `REVIEW_REQUIRED`.
- Targeted style regressions: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/test_style_defaults.py` — **9 PASS**; full suite `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/` — **57 PASS** on Python 3.12. GitHub Actions run [42071774558](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42071774558) completed **57 PASS** on Python 3.11. Metrics are synthetic; genuine TNR and Word rendering remain **NOT_RUN**.

## CB-06 follow-up — page orientation declaration consistency

- Geometry audit now checks explicit `w:pgSz/@w:orient` against the page dimensions. Invalid or conflicting declarations produce `GEOMETRY_UNKNOWN` and leave optimization at `REVIEW_REQUIRED`.
- Regression: portrait dimensions declared as landscape fail closed. Full local suite `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/` — **58 PASS** on Python 3.12; GitHub Actions run [42072958614](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42072958614) completed **58 PASS** on Python 3.11.

## CB-07 follow-up — font-face metadata gate

- `_load_fonts` now rejects a bold/italic face in the regular slot and requires a bold, non-italic face in the bold slot. Family/style metadata is a guard only; it does not establish font licensing or authenticity.
- Six synthetic metadata regressions and full local suite: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/` — **64 PASS** on Python 3.12. GitHub Actions run [42074053917](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42074053917) completed **64 PASS** on Python 3.11. Genuine licensed TNR shaping and Word rendering remain **NOT_RUN**.

## CB-10 follow-up — wheel packaging smoke

- CI now builds the project wheel, installs it with `--no-deps --no-index` into a separate target, then imports from that target outside the checkout.
- The smoke checks that the packaged `POLICY_REGISTRY.json` is present, the public profiles are `('ND30', 'HD05')`, and `python -m chuanhoabang --help` runs from the installed wheel.
- Manual local wheel build/install smoke passed, and GitHub Actions run [42074935268](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42074935268) completed **PASS** for build, isolated install, packaged policy/profile assertions, CLI help, and the full **64-test** suite. This does not replace end-to-end acceptance on a user document or Word rendering.

## CB-04/16 follow-up — compressed archive size guard

- `_package` rejects a DOCX archive larger than 64 MiB before opening it with `ZipFile`; existing entry-size, total-uncompressed-size, entry-count, duplicate-name, and compression-ratio checks remain in place.
- A synthetic regression lowers the configured limit and asserts the ZIP reader is never invoked. Targeted test **1 PASS** and full local suite **65 PASS** on Python 3.12. GitHub Actions run [42076213808](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42076213808) completed **65/65 PASS** on Python 3.11.

## CB-02 follow-up — profile-specific width-metric size scope

- The packaged registry now records official ND30/HD05 source URLs and locators, project selection rules, and a separately versioned `PROFILE-METRIC-SIZE-001` rule. ND30 width measurement accepts declared TNR 13/14 pt; HD05 accepts 14 pt under V16-FONT-02. The official HD05 text lists 14–15 pt; this project selects 14 pt for this metric scope.
- `propose --profile` discloses `profile_constraints`; an unsupported size returns `REVIEW_REQUIRED` with `FONT_SIZE_OUTSIDE_PROFILE_METRIC_SCOPE`. Font properties are not changed, and proposals are rechecked against the same constraint before apply. Full legal presets remain unverified and `profile_rules_applied` stays false.
- Local full suite: **71/71 PASS** on Python 3.12. GitHub Actions run [42079350961](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42079350961): **71/71 PASS** on Python 3.11; wheel build/install, packaged registry/profile check, and installed CLI smoke **PASS**.
- Synthetic metrics only. Genuine licensed TNR measurements and Microsoft Word acceptance are **NOT_RUN**; CB-02 remains **PARTIAL**.

## CB-06 follow-up — non-default text-column geometry

- `TEXT-COLUMN-GEOMETRY-001` rejects sections with more than one text column and sections containing an explicit one-column width override. Invalid `w:equalWidth` values also produce `GEOMETRY_UNKNOWN`; the optimizer no longer substitutes page-wide text width for an unknown column width.
- Regressions cover multi-column, explicit one-column width, malformed equal-width declarations, and orientation conflicts. Focused local core/policy/profile groups: **39 PASS** on Python 3.12.
- GitHub Actions run [42080478277](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42080478277) on commit `bac4cd4`: **74/74 PASS** on Python 3.11; wheel build/install and packaged-registry/CLI smoke **PASS**.
- This is a structural geometry gate, not a resolved column-width measurement. Microsoft Word rendering remains **NOT_RUN**; CB-06 remains **PARTIAL**.

## CB-10/13/16 follow-up — cross-platform package smoke

- CI now runs all 74 tests and builds/installs the wheel on Ubuntu with Python 3.10–3.13 and Windows with Python 3.12. The isolated-wheel smoke checks packaged profile data and runs both CLI help and a Vietnamese DOCX audit.
- First Windows attempt [42082268672](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42082268672) **FAIL**: the CLI wrote a Unicode arrow through a non-UTF-8 Windows console. `cli.main` now configures UTF-8 output; rerun [42082752442](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42082752442) passed all 5 environments, **74/74** each.
- Runtime/test dependencies are locked, build backend versions are exact, and the CI preview artifact passed a same-run repeat-build hash check. Independent-builder reproducibility, rollback, original DOCX fixtures, genuine licensed TNR, Microsoft Word, and WPS acceptance remain **NOT_RUN / UNAVAILABLE**. CB-10, CB-13, and CB-16 remain **PARTIAL**.

## CB-14 follow-up — Microsoft Word manual protocol

- Added [WORD_ACCEPTANCE_PROTOCOL.md](../verification/WORD_ACCEPTANCE_PROTOCOL.md) with the required Word/build/font/fixture record, per-gate visual checks, evidence bundle, and report template.
- The protocol is **NOT_RUN** evidence. The current executor is Linux, has no `winword` executable, and cannot produce Microsoft Word Print Layout proof. LibreOffice evidence remains a separate renderer result.

## CB-10/13/16 follow-up — canonical preview artifact (05/11/2026)

- CI run [42086960094](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42086960094) built the preview wheel on Ubuntu/Python 3.12 with uv 0.13.4, `setuptools==80.9.0`, and `wheel==0.45.1`. Two builds from the same commit and `SOURCE_DATE_EPOCH` matched byte-for-byte.
- The build job wrote a manifest with source/lock hashes, tool versions, wheel SHA-256, smoke checks, and `microsoft_word_acceptance: NOT_RUN`; the wheel and manifest are retained as Actions artifact `chuanhoabang-preview-959f62b0a72b96c55f65f21e29cafd372978cbda` until 19/11/2026. Wheel SHA-256: `dae3b95213860ea238dca079dfdee55ee00d1fff2234405deca04cfd3254f189`.
- All five matrix environments downloaded and verified that exact wheel against the manifest, installed it without network/dependency resolution, and passed the packaged registry, CLI help, Vietnamese DOCX audit smoke, and **74/74 tests**.
- This proves same-job rebuild repeatability and cross-platform use of one candidate. Independent clean-builder reproducibility, release/update rollback, Microsoft Word/WPS, and original-fixture acceptance remain **NOT_RUN**. Issues remain open and PR #17 remains draft.

## CB-06 follow-up — mirrored margins with gutter (05/11/2026)

- Audit now reads `w:mirrorMargins` from `word/settings.xml`. When mirrored margins and nonzero `w:pgMar/@w:gutter` are both enabled, geometry is `GEOMETRY_UNKNOWN` with `MIRRORED_GUTTER_GEOMETRY_UNSUPPORTED`; invalid on/off values also fail closed. Explicit `false`/`0` is recognized, and ordinary gutter width remains subtracted from `available_twips`.
- Three regressions cover enabled, disabled, and invalid setting values. Local suite **78/78 PASS**; GitHub Actions [42088771669](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42088771669) **78/78 PASS** across five environments. Full page-side and Word Print Layout evidence remain **NOT_RUN**; CB-06 remains partial.

## CB-09 follow-up — rollback after output validation failure (05/11/2026)

- A regression injects a failure at the second invariant check, after the candidate ZIP is written. The source remains byte-identical, the output path remains absent, and the temporary `.docx` is removed.
- Local full suite **78/78 PASS**; CI [42088771669](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42088771669) **78/78 PASS** on all five environments. This verifies validation-failure cleanup; release/update rollback and power-loss behavior remain **NOT_RUN**.

## CB-05/09 follow-up — table-wide classification and no-clobber publication (05/11/2026)

- CB-05 regression placed `Nơi nhận` in a trailing row after a plausible data header. It failed before the fix because only the first row was scanned; classifier now scans all table cells and returns `POSSIBLE_LAYOUT_TABLE` / `REVIEW_REQUIRED`.
- CB-09 regression created a destination during the second, post-write invariant check. The old `os.replace` path overwrote it. Publication now uses an atomic same-directory hard link; an existing destination raises `OUTPUT_MUST_BE_NEW_PATH`, preserves both the existing file and the source, and cleans the temporary file.
- Test-first check: each new regression failed before its fix and passed after it. Local full suite **80/80 PASS**. GitHub Actions [42090475384](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42090475384) **80/80 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12. Both issue scopes remain partial; broad classifier corpus, target-renderer proof, filesystem crash durability, and release/update rollback remain unverified.

## CB-04 follow-up — non-body story table inventory (05/11/2026)

- `audit` inventories tables in `word/headerN.xml`, `word/footerN.xml`, `word/footnotes.xml`, and `word/endnotes.xml` separately from editable body indices. Each entry includes its source part, story-local index, canonical table hash, and `REVIEW_REQUIRED`.
- CLI Markdown reports expose these entries and state that they cannot be passed as `--table`; the DOCX remains read-only. Header/footer regressions verify body indices do not shift and the source stays byte-identical.
- Local full suite **83/83 PASS**. GitHub Actions [42092032457](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42092032457) **83/83 PASS** on all five environments. At this point direct story ownership was not yet resolved; CB-04 remained partial.

## CB-04 follow-up — direct story-to-section references (05/11/2026)

- Header/footer part relationships in `word/_rels/document.xml.rels` are matched to direct `w:headerReference` / `w:footerReference` entries in active body section properties. Inventory entries record zero-based section index, story type, and default/first/even reference type.
- The parser rejects ambiguous duplicate relationship IDs for ownership mapping; an unreferenced part stays `SECTION_RELATIONSHIP_NOT_RESOLVED`. Inherited header/footer linkage is not inferred, and all non-body tables remain `REVIEW_REQUIRED` and excluded from apply.
- Regressions cover direct header/footer links, two distinct section indices, unreferenced parts, duplicate relationship IDs, body-index stability, and byte-identical source. Local full suite **86/86 PASS**; GitHub Actions [42093667353](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42093667353) **86/86 PASS** on five environments. Inheritance and original fixture validation remain unverified; CB-04 remains partial.

## CB-05 follow-up — Unicode punctuation in layout markers (05/11/2026)

- Layout text is NFKC-normalized and common Unicode dash characters are normalized before matching existing official-layout hints. This catches “Độc lập – Tự do – Hạnh phúc” and em-dash variants even in trailing rows after a data-looking header.
- Two new regression variants failed before the fix and pass afterward with `POSSIBLE_LAYOUT_TABLE` / `REVIEW_REQUIRED`. Local full suite **88/88 PASS**; GitHub Actions [42094491029](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42094491029) **88/88 PASS** on all five environments. This remains a heuristic safety improvement, not formal semantic classification; CB-05 stays partial.

## CB-16 follow-up — offline wheelhouses and independent rebuild (05/11/2026)

- Commit `5911fe4` added a target-specific runtime wheelhouse for Linux/Python 3.10–3.13 and Windows/Python 3.12. Each bundle contains the canonical app wheel, hash-checked binary runtime wheels, exported locked requirements, and a target/install manifest. A fresh virtual environment installs from the wheelhouse using `pip --no-index`, then runs CLI help and a Vietnamese DOCX audit/report smoke.
- First CI attempt [42097131878](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42097131878) **FAIL** only on Windows because Git checkout line endings changed the working-tree hash of `uv.lock`. Commit `fb79b21` changed the comparison to the committed Git blob; rerun [42097567245](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42097567245) passed the full **88/88** suite and offline install check in all five environments.
- Commit `9c03311` added a second-runner reproducibility comparison. [Run 42097921605](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42097921605) passed **88/88** on each environment; the independent Ubuntu/Python 3.12 runner rebuilt the canonical wheel with the same SHA-256 `a3c83990a8ae5448e0d119e3c3b6bb195fc004e6e872a69691b51665d1961f43`. Offline artifacts for Linux/Python 3.10–3.13 and Windows/Python 3.12 expire **19/11/2026**. This closes the tested offline-install and independent-rebuild subgates, not CB-16: release/update rollback, power-loss behavior, Word/WPS, licensed TNR, and original fixture gates remain **NOT_RUN / UNAVAILABLE**.
- Commit `e5ebef9` made the offline installer enforce every package hash at install time, including the app wheel, using `--require-hashes`. [Run 42099184995](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42099184995) passed **88/88** and the hash-enforced offline install on all five environments; the independent runner rebuilt the wheel with SHA-256 `87905000018f721ebf85952021c8a91d86edc0e373e1e6abc10e6c8f55c94282`. Target artifacts expire **19/11/2026**. The preview changelog entry is recorded in [CHANGELOG.md](../../CHANGELOG.md); no formal tag/release exists. CB-16 remains **PARTIAL** pending rollback, Word/WPS, licensed TNR, and original fixture gates.

## CB-04 follow-up — stable inventory identity and nested parents (05/11/2026)

- `audit` now emits a deterministic source-local `table_id` based on scope/index/hash for body and non-body story tables, plus `parent_table_id` for nested tables. Existing body `index` values and `--table` behavior are unchanged; header/footer/story tables remain read-only.
- Regressions cover nested body and header tables, unique/repeat-stable IDs, immediate parent links, Markdown report visibility, and byte-identical source input. Local suite: **90/90 PASS**. GitHub Actions [42101113025](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42101113025): **90/90 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12, with offline hash-install and independent wheel rebuild checks also passing.
- This closes the tested inventory-ID/parent subgate; inherited header/footer ownership and validation against original DOCX fixtures remain **UNVERIFIED / NOT_RUN**. CB-04 remains **PARTIAL**.

## CB-06 follow-up — preferred width declarations vs table grid (05/11/2026)

- Commit [50bb26e](https://github.com/quanggiaphthh/ChuanhoaBang/commit/50bb26e535d37c4a988b34e85e32cba1ac952d8c) adds JSON/Markdown `width_evidence`: table `tblW`, each physical cell `tcW`, the summed `tblGrid` widths, and an explicit `word_rendered: NOT_RUN` status. Only valid `dxa` declarations are reported in twips; percentage and automatic widths keep their raw OOXML values.
- Invalid or ambiguous table/cell width declarations now make the table `REVIEW_REQUIRED` and retain the raw source value/status for diagnosis. Tests cover percentage vs twips declarations, grid-vs-preferred distinction, invalid `tblW`/`tcW`, and Markdown rendering.
- Local full suite: **94/94 PASS**. GitHub Actions [42103226907](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42103226907): **94/94 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12, with hash-enforced offline installs and independent wheel rebuild also PASS. Wheel SHA-256: `c4c1c641f87c4aa0b2f6cf2ac3b1bc54bfdc4f7743ac74e71050d5143ab20809`.
- This improves source-width diagnostics; it does not resolve column placement, calculate rendered Word width, or prove page fit. Per-column geometry and Word page-position acceptance remain **NOT_RUN**; CB-06 remains **PARTIAL**.

## CB-06 follow-up — equal-width text-column lower bound (05/11/2026)

- Commit [bb14a7a](https://github.com/quanggiaphthh/ChuanhoaBang/commit/bb14a7ae0fb9cace7084b3b9c2a0ef92e43b3cf1) resolves a conservative source-XML width bound for equal-width columns with explicit count and spacing: `(page text width - spacing × (count - 1)) // count`. The optimizer now compares the table grid with this per-column bound rather than the whole page text width.
- Missing/malformed/negative spacing, custom or unequal columns, explicit column children, duplicate column settings, and nonpositive geometry remain `GEOMETRY_UNKNOWN`. JSON and Markdown identify `EQUAL_WIDTH_COLUMN_LOWER_BOUND`; no Word fit is inferred.
- Regressions cover exact bound/overflow, missing and invalid spacing, page source immutability, and Markdown visibility. Local suite: **98/98 PASS**. GitHub Actions [42105076601](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42105076601): **98/98 PASS** on all five environments; hash-enforced offline installs and independent canonical-wheel rebuild also PASS.
- This closes the equal-column structural subgate only. Unequal/custom column resolution, real Word page positions, and full style cascade remain **UNVERIFIED / NOT_RUN**; CB-06 remains **PARTIAL**.

## CB-05 follow-up — compatibility branches and protection markers (05/11/2026)

- Commit [94fcbe1](https://github.com/quanggiaphthh/ChuanhoaBang/commit/94fcbe14c65446f83fbe11b776eb33fadfa7ba61) makes any `mc:AlternateContent` in `word/document.xml` a body-table review lock; the reader does not silently select a `Choice` or discard a `Fallback` branch.
- Commit [07976ee](https://github.com/quanggiaphthh/ChuanhoaBang/commit/07976eed2718bd80e754ec106e2131ce789d5535) blocks body-table proposals when any `w:permStart`/`w:permEnd` is present, since permission-range scope and caller identity are unresolved. Enforced, invalid, or duplicate `w:documentProtection` declarations fail closed.
- Test-first regressions cover a permission range surrounding the table outside its XML subtree, invalid/duplicate enforcement, and an alternate-content branch around a table. At that checkpoint, the suite was **118/118 PASS**; GitHub Actions [42109979396](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42109979396) passed all five OS/Python targets, hash-enforced offline installs, and independent wheel rebuild (SHA-256 `cc0f98da2234c7c3e929dc71c97cbbed704f0b0518818457a26a9b257a142323`).
- This is a bounded fail-closed gate, not a complete semantic classifier. `mc:AlternateContent` branch resolution, permission identity/scope resolution, and formal document-corpus validation remain **UNVERIFIED**; CB-05 remains **PARTIAL**.

## CB-05 follow-up — signed package and macro markers (05/11/2026)

- Runtime already refused OPC packages containing members under `_xmlsignatures/` or `word/vbaProject.bin`; commit [39412ba](https://github.com/quanggiaphthh/ChuanhoaBang/commit/39412ba893f275c79d8bb808b5252414d0a81a7a) adds direct synthetic regressions for both reason codes, verifies proposal paths stay `REVIEW_REQUIRED`, and confirms audit leaves package bytes unchanged. Commit [22eacf6](https://github.com/quanggiaphthh/ChuanhoaBang/commit/22eacf638d6d4b3f80e593185d70250be049eddd) also verifies `apply` rejects a proposal created before a lock marker is added, with no published output.
- Local focused suite: **11/11 PASS**. Full suite: **120/120 PASS**. GitHub Actions [42113088679](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42113088679) passed **120/120** on each of Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; hash-enforced offline installs and independent wheel rebuild passed.
- These tests detect package-part markers only; they do not validate signature cryptography or establish macro behavior. Real signed/macro DOCX fixtures remain **UNAVAILABLE / NOT_RUN**; CB-05 remains **PARTIAL**.

## CB-02 follow-up — versioned unsupported package gate (05/11/2026)

- Commit [1cf12e6](https://github.com/quanggiaphthh/ChuanhoaBang/commit/1cf12e6c7c1bad6fd77324ff40e052d00995af84) adds registry rule `UNSUPPORTED-PACKAGE-CONTENT-001` for signature and VBA macro package-part markers and includes it in the policy version, so proposals disclose the updated policy identity.
- `tests/test_policy.py` now requires the rule in the packaged registry; it failed before the rule was added and passed afterward. The full suite is **120/120 PASS** in [run 42113088679](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42113088679) across all five environments. Complete ND30/HD05 presets and legal authority coverage remain **PARTIAL**.

## CB-09 follow-up — stale apply after package marker changes (05/11/2026)

- Commit [22eacf6](https://github.com/quanggiaphthh/ChuanhoaBang/commit/22eacf638d6d4b3f80e593185d70250be049eddd) extends signature/macro-marker regressions: it creates a valid proposal first, then adds a protected package member and verifies `apply` raises `STALE_OR_MODIFIED_PROPOSAL`, leaves the source bytes intact, and does not publish an output.
- Local full suite: **120/120 PASS**. GitHub Actions [42113088679](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42113088679): **120/120 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12, including offline installs and independent wheel rebuild. Filesystem crash durability and update rollback remain **NOT_RUN**; CB-09 remains **PARTIAL**.

## CB-04 follow-up — same-type default story inheritance candidates (05/11/2026)

- Commit [ad77e1f](https://github.com/quanggiaphthh/ChuanhoaBang/commit/ad77e1fb7a030936ac63a7c98921bb7d3addf98b) makes read-only inventory report a possible inherited `default` header/footer link when a later section omits that reference. A subsequent explicit reference to a different story part stops the candidate chain.
- JSON exposes `default_inheritance_candidates`; Markdown labels them as possible links from a prior section. The tables stay `REVIEW_REQUIRED` and outside `--table`. `first`/`even`, Word-effective page ownership, and footnotes/endnotes ownership are not inferred.
- Regressions cover linked headers and footers, a later explicit override, Markdown visibility, byte-identical input, and a direct `first` header that is not an inherited `default` candidate. Local full suite: **123/123 PASS**. GitHub Actions [42115640491](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42115640491): **123/123 PASS** on all five targets, with offline install and independent wheel rebuild PASS. Default candidates remain unconfirmed ownership; first/even page story resolution remains open. CB-04 remains **PARTIAL**.

## CB-07 follow-up — nonbreaking whitespace in metric estimates (05/11/2026)

- Commit [e4eb5fe](https://github.com/quanggiaphthh/ChuanhoaBang/commit/e4eb5fed3bdaa39c82f2250d7493fe89ba821e99) keeps U+00A0 NBSP, U+180E MVS, U+2007 figure space, and U+202F narrow NBSP inside unbreakable text tokens. Ordinary whitespace still permits line wrapping.
- Regressions use a deterministic fake metric face to exercise only tokenization. They do not represent licensed Times New Roman or Word. The estimate is a partial guard, not a complete Unicode UAX #14 line-breaking algorithm; genuine TNR, full shaping, and Word page acceptance remain **NOT_RUN**. CB-07 remains **BLOCKED_PARTIAL**.
- GitHub Actions [42109979396](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42109979396) passed **118/118** tests on all five targets; offline install and independent wheel rebuild also passed.

## CB-06 follow-up — explicit custom text-column bounds (05/11/2026)

- Commit [8ce2426](https://github.com/quanggiaphthh/ChuanhoaBang/commit/8ce24268e4dafd49212cb97d9a4230ca204eaf71) supports `w:equalWidth="0"` when `w:num` matches the explicit `w:col` elements, each column declares a positive `w:w`, inter-column spacing is explicit and nonnegative, and the declared widths fit inside the section text area. Invalid, incomplete, overcommitted, implicit-default, and mismatched geometry remains `GEOMETRY_UNKNOWN`.
- The audit preserves each custom column width/spacing in JSON and Markdown. With placement unknown, `available_twips` is the narrowest declared column, a conservative bound for any possible column placement. Word-rendered width and fit remain `NOT_RUN`.
- Test-first regressions failed against the old unsupported behavior, then passed after the implementation. Local full suite: **110/110 PASS**. GitHub Actions [42107367344](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42107367344): **110/110 PASS** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12, with hash-enforced offline install and independent wheel rebuild PASS. Canonical wheel SHA-256: `7cf7b19459f12a2acd3bf746b8e919b51f3364f399fb1425b2f7b7ef9efa59c6`; preview and five offline artifacts expire **19/11/2026**.
- The source-geometry subgate now covers equal and explicit unequal columns on synthetic fixtures. Actual table-to-column placement, other layout/style constraints, and real Word page-position evidence remain **UNVERIFIED / NOT_RUN**; CB-06 remains **PARTIAL**.

## CB-06 follow-up — table position and cell-margin resolution (05/11/2026)

- Commit [bf0716e](https://github.com/quanggiaphthh/ChuanhoaBang/commit/bf0716ef553beeeebca33cf8df4b0fb05c9b3b87) adds regressions proving floating `tblpPr` tables and nonzero `tblInd` tables remain `REVIEW_REQUIRED`; width, header-repeat, and row-height proposal paths all refuse them without changing source bytes.
- Commit [51ec157](https://github.com/quanggiaphthh/ChuanhoaBang/commit/51ec15754f96468e34b389a4ee1da5d596dcd045) adds policy `CELL-MARGIN-GEOMETRY-001`; initial test-first coverage found that explicit margins were ignored and introduced a review gate.
- Commit [754d05f](https://github.com/quanggiaphthh/ChuanhoaBang/commit/754d05fe2e322502bc6b2df537c25a38960ddf41) resolves direct left/right `dxa` margins at table level and direct cell overrides. Audit exposes the per-cell padding matrix; the width estimator uses that matrix. Unsupported units or unresolved declarations remain review-only.
- Local full suite: **129/129 PASS**. GitHub Actions [42119947056](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42119947056): **129/129 PASS** on all five targets, including hash-enforced offline installs and independent wheel rebuild SHA-256 `b1890d8ed918b26d5d36ffbf306f24eff1f5c6a7396bda3fd24a01181bff59f9`.
- At commit `754d05f`, effective table-style margin cascade was not resolved; when no direct horizontal margin was present, width metrics used `padding_twips_assumed=150`. The next follow-up versions this estimate as 240 twips. Neither estimate has Word validation. Actual table-column placement and Word page-position evidence remain **NOT_RUN**, so CB-06 stays **PARTIAL**.

## CB-02 / CB-06 follow-up — versioned undeclared-margin estimate (05/11/2026)

- Commit [a2a17e6](https://github.com/quanggiaphthh/ChuanhoaBang/commit/a2a17e6a1db75b571e3a625970f8d7db39277c4f) adds `CELL-MARGIN-DEFAULT-BUDGET-001` to the packaged policy registry. Width metrics use 240 twips total (120 twips per side, approximately 2.12 mm) when a cell has no resolved direct horizontal margin pair. The report exposes this as `padding_twips_assumed`; direct resolved dxa values remain separate.
- The budget rounds above the V15 internal horizontal-padding suggestion. It is a project estimator assumption only; it does not resolve table-style inheritance, establish Word's effective margins, or prove rendered fit. Audit and proposal reports return a null assumed value when all cells have explicit margins.
- Local full suite: **130/130 PASS**. GitHub Actions [42121418712](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42121418712): **130/130 PASS** on all five targets, including hash-enforced offline installs. The independent Ubuntu/Python 3.12 runner reproduced canonical wheel SHA-256 `3ba75b1466aabb63b4eebe7345d87b5f0a9cd4adb052ebd26e20a67b2a3e1092`. Artifacts `chuanhoabang-offline-*-9030a40d15ba2d2d7768297c36ad831306874123` and `chuanhoabang-preview-9030a40d15ba2d2d7768297c36ad831306874123` expire 19/11/2026.
- Effective style-margin cascade, actual table-column placement, and Word page-position evidence remain **NOT_RUN**; CB-06 stays **PARTIAL**.

## CB-06 follow-up — report only applied margin assumptions (05/11/2026)

- Commit [8ed68d8](https://github.com/quanggiaphthh/ChuanhoaBang/commit/8ed68d87b0c393c65dd3ae6165ff656cae08498b) sets `assumed_default_twips` / `padding_twips_assumed` to null when every cell's left/right padding is explicit. The 240-twip budget remains reported and used only for cells that need fallback; mixed explicit/fallback tables expose both the per-cell matrix and the assumption.
- Test-first regression reproduced the misleading 240 value on both all-explicit cases, then passed after the fix. Local full suite: **131/131 PASS**. GitHub Actions [42122426612](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42122426612): **131/131 PASS** on all five targets, with hash-enforced offline installs and independent Ubuntu/Python 3.12 rebuild SHA-256 `8cc962427e8f71b75af59f2bcff1745c9d784ba4f02dfe94d086125a908a8ecd`. Artifacts `chuanhoabang-offline-*-aa1a26ed951781c86f1167e9b3a717dba8deaad2` and `chuanhoabang-preview-aa1a26ed951781c86f1167e9b3a717dba8deaad2` expire 19/11/2026.
- This narrows audit wording only. It does not resolve table-style margin cascade or change Word acceptance status.

## CB-02 / CB-06 follow-up — mark table-style padding unresolved (05/11/2026)

- Commit [65ccd82](https://github.com/quanggiaphthh/ChuanhoaBang/commit/65ccd82a52d66ca5acc03371653679a8ad010ca0) adds policy `CELL-MARGIN-STYLE-CASCADE-001`. When a table references `w:tblStyle`, audit reports `width_evidence.cell_padding.status=UNRESOLVED` with reason `TABLE_STYLE_CASCADE_NOT_SUPPORTED` and omits the effective `twips_by_row` matrix. Width proposals already refuse that cascade; non-width proposals retain their own gates.
- Local full suite: **132/132 PASS**. GitHub Actions [42123763885](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42123763885): **132/132 PASS** on all five targets, with hash-enforced offline installs and independent Ubuntu/Python 3.12 rebuild SHA-256 `18e379ca8680630309f8cd41fd9c9577815dda3715d4de6e32017a07d6f11b15`. Artifacts `chuanhoabang-offline-*-42d01c4849a1c6595be562d049bef922320fb88c` and `chuanhoabang-preview-42d01c4849a1c6595be562d049bef922320fb88c` expire 19/11/2026.
- This explicitly reports the unresolved style cascade; it does not implement style inheritance or change Word acceptance status.

## CB-06 / CB-10 follow-up — expose padding evidence in Markdown (05/11/2026)

- Commit [c389258](https://github.com/quanggiaphthh/ChuanhoaBang/commit/c389258dc64b3e476e7bb64f8b5fa3e8a48817b6) adds cell-padding evidence to the Markdown width table: status, unresolved reason, basis, fallback use, and per-cell values where resolved. Tables with `w:tblStyle` remain unresolved.
- Test-first regressions failed before the renderer change and pass afterward. Local full suite: **134/134 PASS**. GitHub Actions [42124851578](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42124851578): **134/134 PASS** on all five targets, including offline hash installs and independent wheel rebuild SHA-256 `55a43aad42c4fd9fbbbb78b578cc298417a524310d2dcf3ef7aecd6689440ca8`. Artifacts `chuanhoabang-offline-*-ee82a21a3345f6eabc520b72f71fb3a5f48761e0` and preview artifact expire 19/11/2026.
- This improves report visibility only; it does not resolve effective Word style margins or establish Word rendering.

## CB-02 / CB-06 / CB-10 / CB-13 follow-up — bounded table-style margin evidence (05/11/2026)

- Commit `59d3da3` adds a conservative source-XML resolver for table-style horizontal margins. It follows an unambiguous table-style `basedOn` chain and accepts only complete left/right `dxa` pairs in `tblPr/tblCellMar`; direct table margins override the style baseline, and direct cell margins override the corresponding side.
- JSON and Markdown identify the table style, base-to-derived chain, style that provides the margin pair, whether the pair contributes to the per-cell matrix, and fallback use. With no resolved direct or supported style margin, the versioned 240-twip estimator remains visible.
- Conditional table-style margins, style-level `tcMar`, unknown/missing/cyclic chains, and partial or malformed style pairs remain `UNRESOLVED`. Width proposals continue to refuse every table style because table-style typography is still unresolved. The style baseline is source evidence only; Microsoft Word/WPS layout remains **NOT_RUN**.
- Test-first regressions cover base-style inheritance, direct table/cell precedence, conditional/cyclic refusal, fallback disclosure, and Markdown provenance. GitHub Actions [run 42128033502](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42128033502) passed **140/140** on all five targets, with hash-enforced offline installs. Independent canonical wheel SHA-256: `349ab7247bce3817d5eb927f1b9c006928f7bd3483492ec68b3ad02a2b30425b`. Artifacts `chuanhoabang-offline-*-606ab707ee6f71481ca79c351ad0966040708ff8` and preview expire **19/11/2026**.

## CB-09 / CB-10 / CB-13 / CB-16 follow-up — idempotent repeated apply (05/11/2026)

- Commit `b6a9f52` adds policy `APPLY-OUTPUT-IDEMPOTENT-001`. `apply` still revalidates the proposal against the current source and rebuilds/revalidates the complete candidate. If the requested destination already contains a regular, non-symlink file with byte-identical contents, it leaves that file untouched and returns `NO_OP_VALID` with `OUTPUT_MATCHES_VALIDATED_PROPOSAL`.
- Different existing outputs, directories/special files, and symlink destinations continue to return `OUTPUT_MUST_BE_NEW_PATH`; a path created during validation is still protected by atomic no-overwrite publication. Temporary candidates are cleaned on success or rejection.
- The new test reproduced the prior rejection before the change and verifies repeated apply, different-output preservation, source preservation and temp cleanup. Full local suite: **142/142 PASS**. GitHub Actions [run 42129232635](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42129232635) passed **142/142** on all five targets, with hash-enforced offline installs and independent wheel SHA-256 `6a6922a432638c5329103ac51497cfa66476a80ed37e952fbda28d3d131e6287`. Artifacts `chuanhoabang-offline-*-a3c98c4d4182497963b9553a2681feddafe1cb14` and preview expire **19/11/2026**.
- This verifies repeat-apply no-op and no-overwrite behavior for tested filesystems. It does not establish power-loss durability, release/update rollback, or Microsoft Word/WPS acceptance; CB-09 and CB-16 remain **PARTIAL**.

## CB-04 / CB-13 / CB-16 follow-up — relationship-linked custom header/footer parts (05/11/2026)

- Commit [`5b179f1`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/5b179f1af3f65526bcbdaa25963ae28e3586277e) makes `audit` discover internal header/footer relationships to custom-named parts, resolving the same target path for inventory and section-reference ownership. Standard numbered header/footer plus footnotes/endnotes discovery is preserved.
- Targets outside the package, malformed URI targets, external/unknown target modes, and ambiguous relationship IDs do not assign an owner. Custom story tables remain read-only, `REVIEW_REQUIRED`, and excluded from body indices and apply.
- Test-first regressions cover custom header/footer names, byte-identical source preservation, malformed URI handling, and unknown relationship modes. Local full suite: **146/146 PASS**. GitHub Actions [run 42131914049](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42131914049) passed **146/146** on five targets with hash-enforced offline installs; independent Ubuntu/Python 3.12 canonical wheel SHA-256: `753a9e336568466b508d44efaf3033a86646ac06e294bcc206515d43db28d8af`. Artifacts `chuanhoabang-offline-*-b151496a065ce5ca09d6bfd49244b5d9a1a566af` and preview expire **19/11/2026**.
- Effective first/even ownership, nonstandard footnotes/endnotes part names, original fixture validation, and Word/WPS acceptance remain unresolved or NOT_RUN; CB-04 remains **PARTIAL**.

## CB-04 / CB-10 / CB-13 / CB-16 follow-up — custom note parts and visible story type (06/11/2026)

- Commit [`9d55856`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/9d55856540cc218d37c9d6bfec1d9ac6a53a3d08) follows internal document relationships for all four inventoried non-body story types: header, footer, footnotes and endnotes. Custom-named note parts are now read-only inventory entries; JSON and Markdown show the story type even when the part name is not standard.
- External or malformed targets, unsupported relationship modes, and ambiguous header/footer relationship IDs remain unresolved. Non-body story tables still do not enter body indices and cannot be selected for apply. Source bytes are preserved by regression tests.
- Test-first coverage creates custom-named footnote/endnote parts, verifies story type and read-only inventory, and checks Markdown labels. Local full suite: **148/148 PASS**. GitHub Actions [run 42133659528](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42133659528) passed **148/148** on all five targets with hash-enforced offline installs; independent Ubuntu/Python 3.12 canonical wheel SHA-256: `469f91db5df4a251da576b4aa353f62ff82c8d6e9476850a3861880046402833`. Artifacts `chuanhoabang-offline-*-96cd928e4f585d3048101f97944e0bf805882f43` and preview expire **20/11/2026**.
- Word-effective first/even page ownership, original fixture validation, and Word/WPS acceptance remain unresolved or NOT_RUN; CB-04 remains **PARTIAL**.

## CB-04 / CB-10 / CB-13 / CB-16 follow-up — first/even source activation (06/11/2026)

- Commit [`fdd7880`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/fdd7880531dfc0ba419bc523f7dab299afc89001) reports a direct `first` reference's `w:titlePg` state and a direct `even` reference's `w:evenAndOddHeaders` state. JSON and Markdown expose `ENABLED`, `DISABLED`, or `UNKNOWN`, the control element, and `SOURCE_XML_ONLY`; absent controls are disabled while duplicate controls or malformed values are unknown.
- The report still treats these as source references only. It does not infer Word-effective ownership/inheritance or enable changes to non-body stories. Tables remain `REVIEW_REQUIRED`, read-only, and excluded from body table indices.
- Test-first regressions cover enabled and disabled first-page source controls, missing/off/on/invalid/duplicate even-page settings, Markdown visibility, and byte-identical source preservation. Local full suite: **154/154 PASS**. GitHub Actions [run 42135220681](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42135220681) passed **154/154** on all five targets with hash-enforced offline installs; independent Ubuntu/Python 3.12 canonical wheel SHA-256: `7692a8a73c73b2b8df61ae9034d2003b032549847136ee118ab2447a451bd466`. Artifacts `chuanhoabang-offline-*-becbd75c79e277f55e69b265517d44cc3c88bb29` and preview expire **20/11/2026**.
- Microsoft Word/WPS acceptance and validation against original fixtures remain NOT_RUN; effective first/even ownership remains unresolved and CB-04 remains **PARTIAL**.

## CB-04 / CB-10 / CB-13 / CB-16 follow-up — possible first/even inheritance (06/11/2026)

- Commit [`71f147f`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/71f147f13831e432781cf1f55ab24fb2d72f45de) adds read-only, same-type inheritance candidates when a valid active prior-section reference exists, the current section's corresponding control is enabled, and its reference is omitted. Candidates keep the source and target section indices and include target section activation evidence.
- The source rule follows Microsoft's [Open XML `headerReference` guidance](https://learn.microsoft.com/en-us/office/open-xml/word/how-to-replace-the-header-in-a-word-processing-document) and [MS-OE376 titlePg behavior](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/2b3b0cd7-b7e6-47a9-aad0-be5dd1fcf316). This is structural candidate evidence, not a Microsoft Word run, rendering check, or confirmation of effective ownership. Non-body tables remain `REVIEW_REQUIRED` and read-only.
- Test-first regressions cover header/footer first/even candidates, inactive first-page sections, Markdown visibility, and source-byte preservation. Local full suite: **158/158 PASS**. GitHub Actions [run 42136989071](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42136989071) passed **158/158** on all five targets with hash-enforced offline installs; independent Ubuntu/Python 3.12 canonical wheel SHA-256: `b3f6d300f817c9aa76156a299203cdf4c050bdb638ecdb7b02e8e1957509445e`. Artifacts `chuanhoabang-offline-*-5749080603f4217d4805c8abbaba85876e0379b2` and preview expire **20/11/2026**.
- Original fixture validation and Microsoft Word/WPS acceptance remain NOT_RUN; CB-04 remains **PARTIAL**.

## CB-04 / CB-10 / CB-13 / CB-16 follow-up — note definition/reference IDs (06/11/2026)

- Commit [`ee6f13d`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/ee6f13d0fc9c2434d59bf4ac3933a1bf3c69bcea) adds read-only linkage evidence for tables nested in footnote/endnote definitions. It identifies the containing note ID, counts same-type `footnoteReference`/`endnoteReference` elements in the main document body XML, and returns `BODY_REFERENCE_FOUND`, `NO_BODY_REFERENCE_FOUND`, `AMBIGUOUS_NOTE_ID`, `UNKNOWN_NOTE_ID`, or `NOTE_CONTAINER_MISSING` as appropriate.
- The identifier relationship follows Microsoft's [Open XML reference ID](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnotereferencetype.id?view=openxml-3.0.1) and [separator ID](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnoteseparatorreferencetype.id?view=openxml-3.0.1) documentation. `NO_BODY_REFERENCE_FOUND` is scoped to `WORD_DOCUMENT_BODY_XML_ONLY`; it does not claim absence in other stories or effective Word display. Tables stay `REVIEW_REQUIRED` and are not editable through the body table index.
- Regressions cover both note types, repeated body references, no body match, duplicate IDs, malformed IDs, missing note containers, Markdown evidence, and source-byte preservation. Local suite: **163/163 PASS**. GitHub Actions [run 42139101587](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42139101587) passed all five matrix targets with hash-enforced offline installs and CLI/wheel smoke. An independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `0250e2d16b6968ecf8eef3e97adc0a4046974aa7e8fb83d7fac1738411cde6e1`. Artifacts `chuanhoabang-offline-*-5b45f0f8738107271068f83607cd80c87efe142c` and preview expire **20/11/2026**.
- Original fixture validation and Microsoft Word/WPS acceptance remain NOT_RUN; CB-04 remains **PARTIAL**.

## CB-02 / CB-10 / CB-13 / CB-16 follow-up — profile metric source evidence (06/11/2026)

- Commit [`1465722`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/1465722f58add25df576d4985eeea492eb1b3a30) adds the metric scope, source rule ID, eligible sizes, project selection rationale, and official source URLs/locators to `profile_constraints` in JSON and Markdown width proposals. `apply` rechecks these fields against the selected packaged profile. The registry is deep-copied so mutating a returned proposal cannot alter packaged policy data.
- Regressions cover the evidence fields, source locator in Markdown, defensive copying, and rejection when proposal constraint evidence is changed. Local full suite: **164/164 PASS**. GitHub Actions [run 42140650308](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42140650308) passed on all five targets with hash-enforced offline installs and CLI/wheel smoke. An independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `143082ee36d5c0fb6f38e39464a05a05be6a5bb91b92e9384ce566bae308f692`; artifacts `chuanhoabang-offline-*-4b00609c824f62149eaa9adc04b96a9243ddb3a8` and preview expire **20/11/2026**.
- Citation traceability does not verify the complete ND30/HD05 legal presets: status remains `REFERENCE_ONLY`, `profile_rules_applied: false`, and CB-02/10/13/16 remain **PARTIAL**. Original F01–F08 validation, genuine licensed TNR, and Microsoft Word/WPS acceptance remain NOT_RUN or unavailable.

## CB-04 / CB-10 / CB-11 / CB-12 / CB-13 / CB-16 follow-up — source-only horizontal grid spans (06/11/2026)

- Commit [`b8b20c8`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/b8b20c8318341cf071aa8690242916a1a0dae494) reports each valid horizontal `gridSpan` cell’s zero-based logical-grid start and span count in audit/proposal JSON and Markdown. Mapping is read-only XML source evidence; merged width proposals remain `REVIEW_REQUIRED`. Valid horizontal spans are accepted only by the existing width-neutral header-repeat and exact→atLeast row-height operations; `vMerge`, malformed or incomplete grids, and nested tables remain unsupported.
- Test-first regressions cover valid multi-span mapping, Markdown visibility, proposal refusal, malformed/vertical spans, and preservation of width-neutral operations. Local suite: **164/164 PASS**. GitHub Actions [run 42144166384](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42144166384) passed all five targets with hash-enforced offline installs and CLI/wheel smoke. An independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `7f269282e3e226dc601b7792da171c66029c77b92ff1b8669f550e9a58750fc1`; artifacts `chuanhoabang-offline-*-7cc9d20875a091b4eddb4a42eca5f67f03d97526` and preview expire **20/11/2026**.
- This does not enable merged-width optimization or establish Word geometry. The licensed-TNR/Word-geometry gate, original fixture validation, and Microsoft Word/WPS acceptance remain unavailable or **NOT_RUN**; related issues remain **PARTIAL**.

## CB-02 / CB-10 / CB-13 / CB-16 follow-up — primary-source excerpt review (06/11/2026)

- The cited ND30 size text was checked in the official Government Gazette copy: Công báo số 283 + 284, printed page 27, Phụ lục I, Phần I, Mục II, khoản 6 điểm e (13–14 pt). The official HD05 PDF was checked at Phụ lục 2, hàng 6 “Nội dung văn bản” (14–15 pt). These locators match the profile metric provenance already carried by proposals.
- Registry records now expose `source_review.status: PRIMARY_SOURCE_EXCERPT_CHECKED` and the review date. `currentness: NOT_ASSESSED` is explicit. The text check does not establish that either instrument remains in force, verify every rule, or change `verified_legal_presets: false`, `profile_status: REFERENCE_ONLY`, or `profile_rules_applied: false`.
- ND30 Gazette source: https://congbao.chinhphu.vn/tai-ve-van-ban-so-30-2020-nd-cp-30858-30246?format=pdf. HD05 official text: https://tulieuvankien.dangcongsan.vn/upload/2006988/20260529/HD_05_VPTW_e1550.pdf.
- At the excerpt review, the Ministry of Justice legal-status page returned HTTP 502; the opened Gazette record gives promulgation and effective dates, not current status.
- A legal-currentness recheck on 06/11/2026 found the official Ministry of Justice national database search-index entry labels ND30 “Còn hiệu lực”, but the result reported a four-month-old crawl and the live status page remained inaccessible. The official HD05 catalogue record was available that day and confirms issue/effective dates, but exposes no current-status field. A catalogue listing does not prove that no later amendment or withdrawal occurred. Keep both registry values `currentness: NOT_ASSESSED`, both profiles `REFERENCE_ONLY`, and both `verified_legal_presets: false`. Sources: [ND30 national legal database entry](https://vbpl.moj.gov.vn/bonoivu/Pages/vbpq-toanvan.aspx?ItemID=141142&dvid=320) · [HD05 official catalogue record](https://dangcongsan.vn/vanphongtrunguong/van-ban-cua-dang/huong-dan-so-05-hd-vptw-ngay-27-5-2026-cua-van-phong-trung-uong-dang-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang.html?categoryId=3000525).
- Commit [`215719c`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/215719ca8068eef3759d375a291875e4ba6ed760) adds and tests this provenance. Targeted local command `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/test_profile_policy.py tests/test_cli_reports.py`: **22 passed**. GitHub Actions [run 42146173732](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42146173732): **164/164 PASS** across five targets; independent Ubuntu/Python 3.12 wheel SHA-256 `4638fe3658e2fc2fc1ac28eaee564ba008d3f2c66b85cb8e699e9675b2a571aa`. Artifacts expire 20/11/2026.

## CB-04 / CB-10 / CB-12 / CB-13 / CB-16 follow-up — source-only vertical-merge markers (06/11/2026)

- Commit [`1bbc6da`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/1bbc6da42557ddb444c4c45c607706deca07c089) adds local `vMerge` state (`RESTART`/`CONTINUE`) to each source-mapped cell in `cell_grid_spans`. Invalid values keep the mapping unresolved. No vertical continuation-chain validation or vertical-merge editing is enabled.
- Marker semantics follow Microsoft's [VerticalMerge.Val](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge.val?view=openxml-3.0.1) and [VerticalMerge](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge?view=openxml-3.0.1) documentation. The latter also describes a grid-column consistency condition that this source-only marker report does not validate.
- Test-first focused file: **5 passed**; local full suite: **165 passed**. GitHub Actions [run 42147976513](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42147976513) passed 165/165 on all five targets. The independent Ubuntu/Python 3.12 wheel SHA-256 is `21d4b0ac6deb48f6a2baddd8516dcfb33782489557f080d09d8efb30745ab670`; artifacts `chuanhoabang-offline-*-9fa1dbb704229bf85fd8b520708892a876fed30d` expire **20/11/2026**.
- Width proposals and all vertical-merge operations remain `REVIEW_REQUIRED`; only valid horizontal `gridSpan` spans retain the prior width-neutral header/row-height allowance. Original fixture and Word/WPS acceptance remain pending.

## CB-04 / CB-10 / CB-12 / CB-13 / CB-16 follow-up — source-only row grid omissions (06/11/2026)

- Audit maps valid direct `w:gridBefore`/`w:gridAfter` counts to logical cell columns and reports nonzero per-row counts as `row_grid_omissions` in audit/proposal JSON and Markdown. Missing counts mean zero; malformed, duplicate, nested, or grid-inconsistent declarations keep `cell_grid_spans` unresolved.
- Every table with omitted grid cells remains `REVIEW_REQUIRED`; existing width-neutral paging edits are refused for these tables. Tests cover a valid leading/trailing omission pair, contradictory/out-of-range counts, malformed values, Markdown evidence, and proposal refusal.
- Local focused file: **10 passed**; local full suite: **170/170 PASS**. GitHub Actions [run 42150370005](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42150370005) passed all six jobs and 170/170 tests across five targets. The independent Ubuntu/Python 3.12 rebuild matched wheel SHA-256 `452731c38b1e6c248dfc866bb41188607baa7bd4bdff0228d06210c334fe0636`; artifacts expire **20/11/2026**.
- This adds source-only logical-grid mapping; it does not permit omitted-cell edits or validate rendered layout. Microsoft Word/WPS, licensed TNR, and original F01–F08 fixture validation remain **NOT_RUN** or unavailable; CB-04/10/12/13/16 remain **PARTIAL**.

## CB-04 / CB-10 / CB-12 / CB-13 / CB-16 follow-up — source-only vertical-merge chain checks (06/11/2026)

- Audit and proposal JSON/Markdown now report `vertical_merge_chain_validation` when `vMerge` markers are present. A direct `CONTINUE` must follow an immediately preceding `RESTART`/`CONTINUE` on the exact same logical grid range; orphan or overlapping-but-misaligned continuations are `INVALID`, and unresolved cell mapping is `UNRESOLVED`.
- Regression coverage includes a valid chain, an orphan continuation, a continuation range mismatch, unresolved malformed marker, and continued refusal of vertical-merge edits. Focused file: **12 passed**; local full suite: **172/172 PASS**. GitHub Actions [run 42152170192](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42152170192) passed all six jobs and 172/172 tests across five targets. The independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `fb0771049574c11fefa27df1ab6b4a39b2aef5840799355280eacb648ac16f49`; artifacts expire **20/11/2026**.
- These source checks do not confirm Word-effective merge rendering, change table content, or enable vertical-merge edits. Microsoft Word/WPS, licensed TNR, and original F01–F08 fixture validation remain **NOT_RUN** or unavailable; CB-04/10/12/13/16 remain **PARTIAL**.

## CB-05 follow-up — non-body story role candidates (06/11/2026)

- Audit JSON and Markdown now report the same source-only role candidates for header, footer, footnote, and endnote tables as body-table audit output. Non-body tables remain `REVIEW_REQUIRED`, outside body table indices, and without an effective ownership or edit-authority claim.
- Focused local verification: story-table core cases **4 passed**; CLI report and policy groups **13 passed**; `git diff --check` and policy JSON parse **PASS**. Commit [9d4c0dd](https://github.com/quanggiaphthh/ChuanhoaBang/commit/9d4c0dd3123b1fe9c336f09f28232f18b107e033), CI [run 42156267563](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42156267563): all six jobs passed and **182/182 tests PASS** across five targets. The independent Ubuntu/Python 3.12 wheel SHA-256 was `876e941306266bf28c9cb35d3d118d1791c4d8fcbf561e5f80bb67f93de7a415`; preview artifact `chuanhoabang-preview-b4dc47dd0f720f73e95d0d06d5611b9092f5c1be` expires 20/11/2026.
- This CI run includes body and non-body role candidate reporting and predates the parent-cell locator below. Word/WPS and original fixtures remain `NOT_RUN`/unavailable; CB-05 remains `PARTIAL`.

## CB-04/05 follow-up — nested parent-cell source locator (06/11/2026)

- Nested table records now identify the immediate parent table row and cell by zero-based indexes in `parent_cell_location` when the source XML table-row-cell chain resolves. Body proposals carry the parent table and cell fields and `apply` rechecks them. Unsupported topology reports `UNRESOLVED` with a reason; the locator does not claim effective ownership or enable edits.
- Local `tests/test_core.py`: **109 passed**, including nested inventory, stale-proposal binding, and malformed-topology refusal; CLI report and policy groups: **14 passed**; `git diff --check` and policy JSON parse **PASS**. GitHub Actions [run 42157549045](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42157549045) passed all six jobs and **184/184 tests** across five targets. The independent Ubuntu/Python 3.12 wheel SHA-256 matched `5a98a3a6f8e5e1da38a479f9c3c8017307e95b37b35a6f574979c416fdae92a1`; preview artifact `chuanhoabang-preview-0c9d55f29fc1d846dbe7adc0ed90b584d97ce1ea` expires 20/11/2026.

## CB-05 follow-up — matched generic marker terms (06/11/2026)

- Role candidates now list exact terms matched from the fixed layout/form hint vocabulary or recognized header hints. The evidence list never copies arbitrary table cell text. No authority or edit gate changes.
- Local `tests/test_core.py`: **109 passed**; CLI report and policy groups: **14 passed**; `git diff --check` and policy JSON parse **PASS**. Actions [run 42158558757](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42158558757) completed with all six jobs and **184/184 PASS**.

## CB-04/10/13/16 follow-up — direct border source evidence (06/11/2026)

- Audit records direct table and cell border declarations for body and non-body story tables, with zero-based cell positions. Unsupported/duplicate edge, attribute, container, or non-element nodes produce `UNRESOLVED`; style/theme inheritance remains `NOT_RESOLVED`; Word rendering remains `NOT_RUN`. Audit is read-only and the source DOCX byte sequence is preserved.
- Markdown includes the same table and cell declaration evidence for reviewers. Local focused regressions: **6 passed**; full local suite: **189 passed**. Preview artifact `chuanhoabang-preview-7cab25df4794eec6f533901916811cbf0e26a382` expires 20/11/2026.
