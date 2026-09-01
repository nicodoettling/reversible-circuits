# M256 freeze manifest

Date: 2026-08-14 UTC.

## Verdict

```text
PROVED CONDITIONAL ON FULL DV:
  full WPCR => SCBR => BR <=> BIR => PCS-bound.

EXACT STOP:
  FCL1 and A_k(1,1)=O(1) additionally require FD-bound
  or M168's exact minority-sign substitute.

NO GAP, MIXING, OR TERMINAL CLAIM.
```

The theorem is uniform for odd `k>=3`, with `n=3k` and
`m=(n-1)/2`. Its target is the balanced first fixed cell of the auxiliary
uniform minimal-long-cycle factorization law and nonlazy cyclic rank-two
kernel, not the global identity bridge or its `{3,4,5}` heat-bath chain.

## Immutable gate

Every declared checksum entry in M168/M171, M174/M178, M180/M182,
M186/M189, M192/M195, M217/M222, M235/M238, M239/M246, M248/M249, and
M252/M253 passes. The supplementary M161/M166 payload and freeze-manifest
hashes pass for the exact `A_k(1,1)`--`FCL1` equivalence. Exact digests and
the historical-manifest qualification are in `dependency_audit.md`. No
dependency was edited.

## Checker

Exact command from repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-69/mission-M256-conditional-response-chain/algebra_checker.py
```

Python `3.12.3`; standard library only; deterministic; `seed=null`. All
reported rows pass. The checker tests finite exact algebra and normalization
only; it makes no DV/TAV, FD, or asymptotic attempt.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `dependency_audit.md`
- `chain_proof.md`
- `algebra_checker.py`
- `algebra_results.json`
- `report.md`
- `fresh_audit_request.md`
- `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest and inventories every file
listed above; it excludes itself. M256 edited no file outside its owned
mission directory. Fresh independent audit is required before coordinator
promotion.
