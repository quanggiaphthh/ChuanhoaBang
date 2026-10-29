# V17.4 — Index after pilot and Antigravity audit (29/10/2026)

## Sources and status

- [Synthetic pilot](pilot/README_PILOT.md), [pilot summary](pilot/pilot_summary.json), [pilot code](pilot/run_v174_pilot.py). Baseline outputs are synthetic; not model inference.
- [Antigravity prompt](antigravity/MASTER_PROMPT_ANTIGRAVITY.md) and [attach-only instructions](antigravity/README_ATTACH_THIS_ONLY.md).
- [Independent file-based scoring audit](scoring/V17_4_INDEPENDENT_FILE_AUDIT_REPORT.md), [spec decisions](scoring/spec_scored_128.csv), [pair order check](scoring/paired_order_64.csv), [reproduction](scoring/REPRODUCE.md).
- Antigravity reported 128 response records, and audit found 59/64 A/B-consistent pairs, mandatory 63/68, conditional 13/30, abstain 1/16. These are **SPEC CONCORDANCE**, never independently validated expert accuracy.
- Model identity `gemini-3.8-flash-low / MODEL_PLACEHOLDER_M320` is reported by Antigravity logs but provider identity was not independently authenticated.
- At least 26/128 public inputs had potential cue leakage; blind-validation and human gold labels remain BLOCKED.

## Provenance and deliberately excluded artifacts

- Raw user-supplied execution archive `ChuanhoaBang_V17_4_Evaluation_Report_Results.zip`: SHA-256 `05144a2d6bcd3299da2847088aa2004715e70b4ba6e22e6eaa9387b37669ae73`; **not included** in repository (contains raw model payloads and local system path details; retaining separately avoids inadvertently publishing them).
- Private scoring archive `ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip`: SHA-256 `04cb5da80599cce0cd1da1a069ba1a0e48038043fc85b1335be06e13570cb767`; **not included** to preserve test-key isolation.
- The public ZIP package digest mismatch found in the audit remains OPEN; input JSONL constituent digest matched.
- The check-in is a research/spec/data snapshot, not a complete standalone rerun of original proprietary Antigravity calls or a formal blinded validation.
