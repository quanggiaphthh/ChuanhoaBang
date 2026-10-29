# CHUANHOABANG V17.4 — ANTIGRAVITY: 128 INDEPENDENT NO-RENDER MODEL JUDGMENTS

## ROLE AND SCOPE

You are an ORCHESTRATOR, not the judge whose reasoning will be scored. Use the **attached ZIP `ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip`**. The ZIP deliberately contains **no gold labels, answer key, prior pilot model outputs or V17.3 scoring metadata**. Never fetch those materials for the evaluator. If a private key is offered later, access it only in a separate scoring phase **after all model responses have been finalized and checksummed**.

This is an evaluation of the ChuanhoaBang V17.4 table-quality specification under **Times New Roman 13–14 pt, no document/image/PDF rendering**. Do not develop a Word formatter, change the source table data, change GitHub, or claim legal or visual certification. An observed result is a **model-based pilot** until independent prompt neutrality and independent expert gold labels have been established.

## PHASE 0 — INPUT AUDIT AND ISOLATION

1. Unpack the attached ZIP in a clean workspace. Read `README_ATTACH_THIS_ONLY.md`, `02_ORCHESTRATOR/EXPERIMENT_PROTOCOL.md` and public manifest. Run `python 02_ORCHESTRATOR/verify_public_inputs.py` with the workspace set to the ZIP root. Confirm 128 unique IDs, exactly TNR, size 13/14, payload SHA-256 and absence of gold-key files.
2. There are 64 source pairs, each presented in both option orders; **do not assume that opaque item IDs reveal pairing**. The exact secret mapping is not included in the evaluator package. Do not try to reconstruct a secret key to peek at the expected answers.
3. Inspect `option_1` and `option_2` for explicit evaluative cues. Some current prompts may leak which variant is poor. Preserve the original text and record flags; if no genuinely independent neutral rewrite and quality review is available, mark `PROMPT_NEUTRALITY_UNVERIFIED` and treat all results as **exploratory/model-based pilot**, not formal blind validation. Do not rewrite option contents silently: such edits can change the experiment.
4. Create a separate evaluator context or stateless model API path. The evaluator sees **only** the per-item `01_EVALUATOR_ONLY` fields plus `01_EVALUATOR_ONLY/EVALUATOR_SYSTEM_PROMPT.md`; it must not see this master prompt, other cases, any prior answers, pilot reports, or scoring keys. No AB+BA pair in one model context.
5. Record the actual model service, exact model/version (not a marketing nickname alone), temperature, seed if supported, limits, locale, timestamp and processing environment. If there is no ability to invoke a model independently with per-item calls, **do not simulate model outputs**: mark `MODEL_EVALUATION_BLOCKED`.

## PHASE 1 — REAL JUDGMENTS (IF EXECUTION IS AVAILABLE)

6. Submit all **128 inputs as 128 separate inference calls**, ideally separated into independently scheduled waves, without passing previous completions into subsequent requests. The two orders are already present in the input list; do not derive the pair keys inside evaluator requests. A/B reversal consistency can be calculated after scoring access is granted.
7. Ask the model to output one strict JSON object with `item_id`, `decision` (`OPTION_1|OPTION_2|CONDITIONAL|ABSTAIN`), `reason`, `evidence_codes` (array), `unknown_measurements` (array), `uncertainty` (`LOW|MEDIUM|HIGH`), and `response_status` (`COMPLETED|INVALID_OUTPUT|ERROR`). Output must be based solely on the item. Infer the outcome **from table content and design constraints**, never from words implying that an option is already better/worse.
8. Record **raw request, raw model response, parsed output, latency/error, actual model ID and run ID for every call**. Do not substitute rule-based heuristics or examples for model responses. If responses are malformed, keep their raw contents and mark `INVALID_OUTPUT`; no improving retries based on score. System-level retry for transport failure may be logged separately.
9. If all calls succeed, save `responses_128.jsonl` with unique IDs and the original decisions, plus `run_manifest.json` and `raw_requests_responses.jsonl`. **Lock all responses** (SHA-256 + timestamp + immutable copy) before opening scoring references.

## PHASE 2 — SCORING / INDEPENDENCE CONDITIONS

10. Before private keys are supplied, run the public integrity/coverage checks only. The private after-lock ZIP is a separate artifact; **do not attach it to this prompt or let the evaluator read it**.
11. If and only if raw responses have been locked, use the separately supplied `PRIVATE_Scoring_After_Lock` bundle in a different scoring context, and run `python v174_runner.py score --responses PATH_TO_RESPONSES_128.jsonl` from its root. This scorer compares the responses against **V17.3 authored SPEC labels only**. Report `SPEC_CONCORDANCE_ONLY_NOT_VALIDATED_ACCURACY`, not expert gold accuracy. Use pair-ID mapping in private package to assess A/B vs B/A consistency.
12. Report separate numerator/denominator for mandatory error, conditional cases, abstention, soft preference, and pair-order stability. Invalid/missing outputs must be counted and explained, never silently discarded. Do not set quality/beauty thresholds or claim a 90% pass standard without independent expert calibration.
13. Formal blind validation is **BLOCKED** until an independent specialist has neutralized/checked option wording and independent human gold labels have been adjudicated without access to V17.3 labels. Model-to-model agreement is not a substitute for independent expert gold. Font width in the current examples is illustrative, not confirmed using TNR glyph measurements; Unicode line-break opportunities are not Word-rendered line breaks.

## STOP CONDITIONS

Stop or downgrade to `BLOCKED`/`UNVERIFIED` if any answer key or pilot report reached an evaluator, inputs were modified without audit, evaluator state leaked across cases, raw responses or model versions are missing, API access is absent, or the 128-item set is incomplete. Do not generate synthetic predictions to fill missing responses.

## FINAL DELIVERABLES (NO GITHUB CHANGES)

- `inputs_sha256.txt` and `run_manifest.json` with model fingerprint/configuration, prompt and evaluator instruction checksums
- `raw_requests_responses.jsonl` (128 raw calls if all executed), `responses_128.jsonl` (structured predictions), `execution_qa.json`
- `scoring/spec_score_report.json`, `scoring/pair_order_consistency.csv` when after-lock secret mapping becomes available; otherwise `SCORING_BLOCKED.md`
- `VALIDATION_REPORT.md` with exact executed vs blocked counts, cue-leakage risk, no-render limits and evidence labels
- `WORKBOOK_PROFILE_INTEGRATION.md` concise factual handoff: 13–14 pt only, source preservation, distinguish `RULE_INFERRED`, `FONT_METRIC_ESTIMATE`, `VISUAL_NOT_VERIFIED`, `EXPERT_GOLD_NOT_OBTAINED`.

**Never claim formal independent blind validation simply because 128 model calls were completed.**