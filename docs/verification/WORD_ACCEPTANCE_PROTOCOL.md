# Microsoft Word acceptance protocol

**Purpose:** repeatable L2 visual acceptance for a versioned ChuanhoaBang candidate. This file is a procedure and report template, not a test result.

**Current status (05/11/2026):** `NOT_RUN`. The current executor is Linux, has no `winword` executable, and only has LibreOffice. LibreOffice/WPS output cannot be recorded as Microsoft Word acceptance. The original F01–F08 DOCX files are also unavailable in this repository.

## Required environment record

Record these values before opening a fixture:

| Field | Required value |
|---|---|
| Test operator / reviewer | Names or stable identifiers |
| OS | Edition, version, build, architecture |
| Microsoft Word | Product, version, full build number, update channel, 32/64-bit |
| Local fonts | Times New Roman regular/bold face names, file SHA-256, and licensing/source confirmation; do not copy font files into this repository |
| Page/render settings | Paper size, orientation, printer/driver, duplex setting, and Word PDF export settings |
| ChuanhoaBang | Commit SHA, package version, policy registry version, command/API used |
| Input | Fixture ID, source URL/provenance, SHA-256, authority/profile, lock/signature state |
| Proposal/output | Proposal SHA-256, output SHA-256, selected profile, and decision |

Use the same computer, Word build, installed fonts, printer, and page settings for the baseline and candidate. If Word repairs the file, asks to recover content, or substitutes a required font, mark the case `FAIL` or `NOT_RUN` with the observed reason; do not continue as if the original package was rendered unchanged.

## Procedure per fixture

1. Verify the input SHA-256 against the fixture manifest. Keep the input read-only and store the proposal and output as separate files.
2. Open the baseline input in desktop Microsoft Word. Record any repair, compatibility, font substitution, or protected-document notices. Check **Print Layout** and note the page count before changing anything.
3. Open the candidate output in the same Word installation. Confirm the candidate opens without repair. Check the affected table on every page it occupies and inspect the adjacent pages for layout changes.
4. Compare baseline and candidate at the same zoom and Print Layout settings. Export both to PDF using Word only if the test record identifies that exact Word build and export path. Save screenshots of the relevant pages; a PDF from another renderer is a separate result.
5. Recheck text, numbers, formulas, row/column order, merged cells, captions, signatures, page orientation, headers/footers, page numbers, and non-target content against the source. Word appearance does not replace the automated DOCX/OPC invariant checks.
6. Record each gate separately as `PASS`, `FAIL`, `NOT_RUN`, or `UNVERIFIED`. Include the exact page/row/cell and evidence filename for every failure or uncertainty.
7. A second reviewer checks the evidence and hashes. Do not turn a missing fixture, absent font, or absent Word installation into a pass.

## Visual acceptance checks

| Gate | Check | Pass condition |
|---|---|---|
| L0 | Data and topology | Automated structural checks pass; Word shows no missing, duplicated, reordered, or altered content |
| L1 | Authority and geometry | Profile/authority has independent support; page/column bounds and orientation are permitted; no font shrink or unrequested orientation change |
| L2-A | Horizontal layout | Table and borders remain within the intended text area; no clipped columns or unintended scaling |
| L2-B | Text flow | No clipped glyphs, hidden lines, unexpected overlap, or unreadable wrapping at the recorded zoom/print settings |
| L2-C | Pagination | Header repetition, row breaks, blank pages, captions, signatures, and page numbering match the case expectation |
| L2-D | Scope | Non-target tables, sections, headers/footers, and surrounding text remain visually unchanged except for recorded pagination effects |

`PASS` is case-specific. A case that has no suitable source fixture or expected result is `NOT_RUN`, not `PASS`. A Word visual pass establishes only the observed rendering for the recorded environment; it does not certify legal compliance for every ND30/HD05 document or Word build.

## Evidence bundle

Store an acceptance bundle outside the repository unless the fixture owner permits publication. Include:

- environment record and test date;
- source, proposal, and output SHA-256 values;
- fixture provenance/license and expected decision;
- automated L0/L1 report and exact test command;
- Word screenshots and optional Word-exported baseline/candidate PDFs;
- per-gate results, deviations, reviewer, and final case decision.

Suggested record:

```yaml
fixture_id: F01
source_sha256: NOT_RUN
proposal_sha256: NOT_RUN
output_sha256: NOT_RUN
profile: ND30
word_product_build: NOT_RUN
os_build: NOT_RUN
font_faces_and_sha256: NOT_RUN
automated_l0_l1: NOT_RUN
word_render: NOT_RUN
visual_gates: NOT_RUN
evidence_files: []
reviewer: NOT_RUN
case_decision: NOT_RUN
limitations: "No Microsoft Word run is represented by this template."
```

## Release interpretation

- Missing Microsoft Word, unavailable original fixtures, unresolved font identity, or missing required screenshots means Word acceptance is `NOT_RUN` or `UNVERIFIED`.
- LibreOffice and WPS results remain separate renderer evidence. They cannot change `word_render` to `WORD_RENDER_VERIFIED`.
- Do not claim v1.0 Word acceptance from synthetic fixtures, a structural test suite, or this protocol alone.
