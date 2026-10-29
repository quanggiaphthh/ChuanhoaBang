# SEND THIS ZIP TO ANTIGRAVITY — V17.4

**This is the ONLY ZIP to attach to the Antigravity orchestrator for the 128-item model run.**

1. Attach `ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip`.
2. Paste `02_ORCHESTRATOR/MASTER_PROMPT_ANTIGRAVITY.md` (also provided as a standalone `.md` file).
3. Allow Antigravity to inspect `02_ORCHESTRATOR` for setup, **but require evaluator calls to be fresh and to see only the one prompt record + `01_EVALUATOR_ONLY/EVALUATOR_SYSTEM_PROMPT.md`**.
4. Do not attach `ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip` at the same time. The private ZIP includes author-created answer labels and must be kept out of evaluator contexts until ALL 128 model responses have been sealed.
5. If no model invocation channel is available, Antigravity should report BLOCKED with exact prerequisites, not generate fake responses. If prompt wording remains answer-cue biased, call any runnable results a provisional model pilot, NOT independent blind validation.

Included in this public ZIP:
- `01_EVALUATOR_ONLY/prompts_128_blind_candidate.jsonl`: 128 opaque-input records, actual source V17.4 SHA preserved.
- `01_EVALUATOR_ONLY/EVALUATOR_SYSTEM_PROMPT.md`: neutral per-item evaluator instruction.
- `02_ORCHESTRATOR/MASTER_PROMPT_ANTIGRAVITY.md`: full orchestrator task prompt.
- `02_ORCHESTRATOR/EXPERIMENT_PROTOCOL.md`: collecting, isolation and scoring instructions.
- `02_ORCHESTRATOR/verify_public_inputs.py`: Python standard-library verification (not a model runner).
- `02_ORCHESTRATOR/WORKBOOK_PROFILE_HANDOFF.md`: safe summary to parallel profile/rule work.
- `manifest_public.json`: input checksums and tracked counts.

NO scoring key, gold template, generated responses, per-pair source metadata or pilot output is inside this ZIP.