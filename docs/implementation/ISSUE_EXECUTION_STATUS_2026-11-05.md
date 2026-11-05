# ChuanhoaBang — Issue execution status (05/11/2026)

**Baseline:** main 13be13e0d34ee7f603a2bdd24e84493d7cae4c33  
**Implementation:** PR [#17](https://github.com/quanggiaphthh/ChuanhoaBang/pull/17), branch `feat/offline-docx-table-core-v01`.  
**Latest verified code:** PR commit [`e5ebef948fc38445c4be4cbad90503f1b6590603`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/e5ebef948fc38445c4be4cbad90503f1b6590603), [GitHub Actions run 42099184995](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42099184995): **88/88 PASS** on Ubuntu/Python 3.10, 3.11, 3.12, 3.13 and Windows/Python 3.12. Each target installed the app and hash-pinned runtime wheelhouse in a fresh environment using `pip --no-index --require-hashes`, then passed CLI/DOCX audit smoke. An independent Ubuntu/Python 3.12 runner reproduced the canonical wheel SHA-256 `87905000018f721ebf85952021c8a91d86edc0e373e1e6abc10e6c8f55c94282`. Target-specific artifacts `chuanhoabang-offline-*-e5322ecebe3a040d5440145d1e0b42c7c595c765` and the preview wheel are retained until 19/11/2026. Word/WPS and source fixtures remain unverified.

> This is a technical preview. All issues remain open until their acceptance criteria are fully met and work is merged as appropriate. Not a production release.

## Issue-by-issue evidence

| Issue | Current delivery | Still required | State |
|---|---|---|---|
| [#1](https://github.com/quanggiaphthh/ChuanhoaBang/issues/1) ADR/capability | ADR evaluates Python OOXML / WordVN / .NET; WordVN repo inspected | Review/update final integration choice when editor exists | PARTIAL |
| [#2](https://github.com/quanggiaphthh/ChuanhoaBang/issues/2) policies | Packaged runtime registry; ND30/HD05 selection and proposal binding; sourced profile-specific width-metric size gate; orientation safety | Complete verified profile presets, authority classification, and legal rule coverage | PARTIAL |
| [#3](https://github.com/quanggiaphthh/ChuanhoaBang/issues/3) fixtures | Fixture inventory and provenance notes; local/Drive search did not locate originals; 118-case synthetic evidence contains 0 DOCX fixtures | Obtain original checksum-verified F01–F08 & V15 binaries | BLOCKED_PARTIAL |
| [#4](https://github.com/quanggiaphthh/ChuanhoaBang/issues/4) OPC reader | Read-only body inventory plus separate part/hash inventory for header/footer/footnote/endnote tables; direct section references resolved with ambiguous IDs fail closed | Resolve inherited story ownership and broader document fixtures/source validation | PARTIAL |
| [#5](https://github.com/quanggiaphthh/ChuanhoaBang/issues/5) classification | Layout/lock/complex refusal, 7 negative markup cases, table-wide marker scan with Unicode dash normalization | Formal sample corpus, robust table semantics, authority validation | PARTIAL |
| [#6](https://github.com/quanggiaphthh/ChuanhoaBang/issues/6) geometry | Single-section geometry, orientation/text-column gates, gutter subtraction, mirrored-margin plus gutter fail closed, diagnostics and bounded paragraph-style inheritance | Actual per-column width resolution, nested/story ownership, remaining style cascade and Word page-position evidence | PARTIAL |
| [#7](https://github.com/quanggiaphthh/ChuanhoaBang/issues/7) glyphs | Optional local Pillow/RAQM; supported style chain and regular/bold/italic face metadata gates | Licensed genuine TNR face validation, Unicode shaping evidence | BLOCKED_PARTIAL |
| [#8](https://github.com/quanggiaphthh/ChuanhoaBang/issues/8) width | Bounded optimizer on rectangular tables; no automatic landscape | Real font/renderer validation and historical fixture comparison | PARTIAL |
| [#9](https://github.com/quanggiaphthh/ChuanhoaBang/issues/9) patch | Operation-specific OOXML whitelist; stale proposal guard; non-target parts/path safety; post-write validation cleanup; atomic no-overwrite publish if a destination appears concurrently | Broader DOCX interoperability, release/update rollback and remaining merge/review cases | PARTIAL |
| [#10](https://github.com/quanggiaphthh/ChuanhoaBang/issues/10) CLI/API | Public Python API and CLI audit/propose/explicit apply; JSON and Markdown; no-overwrite; canonical wheel and manifest installed/smoke-tested across five environments | End-to-end user document acceptance | PARTIAL |
| [#11](https://github.com/quanggiaphthh/ChuanhoaBang/issues/11) pages | Repeat first header, exact→atLeast opt-in; supports valid horizontal gridSpan-only for paging; LO synthetic smoke | Conditional row split, Word Print Layout acceptance | PARTIAL |
| [#12](https://github.com/quanggiaphthh/ChuanhoaBang/issues/12) complex | Narrow support for horizontal gridSpan paging; refuse vMerge/nested/merged AutoFit | Constraint-solving AutoFit for merged tables, broader topology/Word tests | PARTIAL |
| [#13](https://github.com/quanggiaphthh/ChuanhoaBang/issues/13) regression | GitHub Actions 88 PASS across 5 environments incl archive/profile/geometry/rollback/classifier/story-ownership guards and hash-verified canonical wheel | Original F01–F08/V15 plus target renderer cases | PARTIAL |
| [#14](https://github.com/quanggiaphthh/ChuanhoaBang/issues/14) Word/WPS QA | LibreOffice secondary smoke; [repeatable Microsoft Word protocol](../verification/WORD_ACCEPTANCE_PROTOCOL.md) | Independent Microsoft Word and WPS evidence on supported fixtures | NOT_RUN |
| [#15](https://github.com/quanggiaphthh/ChuanhoaBang/issues/15) WordVN | GitHub `quanggiaphthh/WordVN` main inspected: only README | Editor importer/exporter, selection/Undo API must exist before adapter | BLOCKED |
| [#16](https://github.com/quanggiaphthh/ChuanhoaBang/issues/16) release | Locked runtime/test dependencies; exact build backend pins; source/lock/artifact manifests; target-specific offline wheelhouses with hash-enforced `--no-index` installs across 5 environments; separate-runner wheel SHA match; versioned `0.1.0.dev0` preview note | Official tag/release, release/update rollback, Word/WPS acceptance, original fixtures, remaining security/compatibility gates | PARTIAL |

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
