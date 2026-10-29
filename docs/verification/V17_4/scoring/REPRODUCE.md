# Reproduce audit

**Three input ZIP files** (not embedded to avoid inadvertently publishing the private scoring key):

1. `ChuanhoaBang_V17_4_Evaluation_Report_Results.zip` — user-supplied Antigravity results.
2. `ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip` — post-lock V17.3 SPEC key, not expert gold.
3. `ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip` — prompt-only source archive.

In Python 3.9+:

```sh
python reproduce_v174_audit.py --results ChuanhoaBang_V17_4_Evaluation_Report_Results.zip --private ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip --public ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip --output result.json
```

Expected: 128 records, 64 reversed pairs, 59 consistent pairs, MANDATORY 63/68, RECOMMENDED 14/14, CONDITIONAL 13/30, ABSTAIN 1/16. Five checks return true and `public_zip_sha256_match` returns false due to observed package digest mismatch; this must be investigated, not suppressed. The constituent input JSONL digest is verified.

Do not give this package or any private-key package to a blind evaluator.