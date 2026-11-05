# ChuanhoaBang — Issue execution status (05/11/2026)

**Baseline:** main 13be13e0d34ee7f603a2bdd24e84493d7cae4c33  
**Implementation:** PR [#17](https://github.com/quanggiaphthh/ChuanhoaBang/pull/17), branch `feat/offline-docx-table-core-v01`.  
**Latest verified before this document:** commit `f0120ece92f4355ac7ba51fdc13a2017149a8c9e`, [GitHub CI](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42016482690): **SUCCESS**; prior exact test count **33 PASS** on the same focused `tests/` suite.

> This is a technical preview. All issues remain open until their acceptance criteria are fully met and work is merged as appropriate. Not a production release.

## Issue-by-issue evidence

| Issue | Current delivery | Still required | State |
|---|---|---|---|
| [#1](https://github.com/quanggiaphthh/ChuanhoaBang/issues/1) ADR/capability | ADR evaluates Python OOXML / WordVN / .NET; WordVN repo inspected | Review/update final integration choice when editor exists | PARTIAL |
| [#2](https://github.com/quanggiaphthh/ChuanhoaBang/issues/2) policies | V17.5.1 registry; structural orientation protection | Full profile authority/schema tests and executable rule binding | PARTIAL |
| [#3](https://github.com/quanggiaphthh/ChuanhoaBang/issues/3) fixtures | Fixture inventory and provenance notes | Obtain original checksum-verified F01–F08 & V15 binaries | BLOCKED_PARTIAL |
| [#4](https://github.com/quanggiaphthh/ChuanhoaBang/issues/4) OPC reader | Read-only audit and table inventory; ZIP safety guards | Broader document fixtures and source validation | PARTIAL |
| [#5](https://github.com/quanggiaphthh/ChuanhoaBang/issues/5) classification | Layout/lock/complex refusal and 7 extra negative markup cases | Formal sample corpus, robust table semantics, authority validation | PARTIAL |
| [#6](https://github.com/quanggiaphthh/ChuanhoaBang/issues/6) geometry | Single-section geometry and diagnostics | Full style cascade/gutter/columns/nested context | PARTIAL |
| [#7](https://github.com/quanggiaphthh/ChuanhoaBang/issues/7) glyphs | Optional local Pillow/RAQM; blocks if unavailable | Licensed genuine TNR face validation, Unicode shaping evidence | BLOCKED_PARTIAL |
| [#8](https://github.com/quanggiaphthh/ChuanhoaBang/issues/8) width | Bounded optimizer on rectangular tables; no automatic landscape | Real font/renderer validation and historical fixture comparison | PARTIAL |
| [#9](https://github.com/quanggiaphthh/ChuanhoaBang/issues/9) patch | Whitelisted OOXML patch, stale proposal guard, non-target parts, path safety | Edge DOCX interoperability and merge/review | PARTIAL |
| [#10](https://github.com/quanggiaphthh/ChuanhoaBang/issues/10) CLI | audit/propose/explicit apply; JSON and Markdown; no-overwrite | Clean packaging/install and end-to-end user document acceptance | PARTIAL |
| [#11](https://github.com/quanggiaphthh/ChuanhoaBang/issues/11) pages | Repeat first header, exact→atLeast opt-in; LO synthetic smoke | Conditional row split, Word Print Layout acceptance | PARTIAL |
| [#12](https://github.com/quanggiaphthh/ChuanhoaBang/issues/12) complex | Detect/decline merged and nested | Supported merged subset, topology tests | NOT_IMPLEMENTED |
| [#13](https://github.com/quanggiaphthh/ChuanhoaBang/issues/13) regression | GitHub Actions 33 PASS, incl 7 markup and 3 output collision cases | Original F01–F08/V15 plus target renderer cases | PARTIAL |
| [#14](https://github.com/quanggiaphthh/ChuanhoaBang/issues/14) Word/WPS QA | LO secondary smoke documents | Independent Microsoft Word and WPS evidence | NOT_RUN |
| [#15](https://github.com/quanggiaphthh/ChuanhoaBang/issues/15) WordVN | GitHub `quanggiaphthh/WordVN` main inspected: only README | Editor importer/exporter, selection/Undo API must exist before adapter | BLOCKED |
| [#16](https://github.com/quanggiaphthh/ChuanhoaBang/issues/16) release | Release gate document, CI | Clean package and Word acceptance, security/compatibility gates | NOT_READY |

## Delivered changes beyond original PR bootstrap

- Safety fail-closed against additional OOXML fields, comments, bookmarks, permission ranges, wrapped content, plus **7 regressions**.
- Corrected GitHub workflow to run the *entire focused test directory*, not just two legacy test modules.
- Added human-readable Markdown reports to CLI, with strict collision checks for DOCX, proposal JSON, input and Markdown report paths.
- Added negative regression coverage for report conflicts; **33 focused tests PASS**.
- Reduced CI duplication: push main / PR / optional manual dispatch, rather than double-running push and PR on a feature branch.

## Release decision

**NO-GO for v1.0/official Word acceptance.**  
**GO for continued development of technical preview in PR #17.**

The absence of licensed Times New Roman validation, original corpus, Word/WPS evidence, WordVN editor API, and merged/nested implementation is **not** a code-review shortcut or a successful test. No issue automatically closes merely because a related subcomponent exists.

## Next minimum-value execution

1. Get genuine local Times New Roman measurements and run paired candidate/baseline on real fixture DOCX when available.
2. Build verified fixture inventory and test normal vs locked/complex/multi-page cases.
3. Add supported merged-cell subset **only after** bounded width and data-preservation gates hold.
4. Run official Microsoft Word and WPS compatibility acceptance before v1.0.
5. Build a thin WordVN adapter when WordVN's own editor API is implemented; do not create a duplicate editor.
