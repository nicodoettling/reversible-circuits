# M264 freeze manifest

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M261'S STRICT EXACT PBV REDUCTION.
PBV, FD-BOUND, MINORITY SIGN, FCL1, GAP, MIXING, AND TERMINAL REMAIN OPEN.
```

M261's immutable `SHA256SUMS` digest is
`b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b`,
and all nine named payloads pass. The referee independently reconstructed
the completion coefficient, endpoint sign/index and bound, M91 two-channel
Abel normalization, FD/PBV scale equivalence, and pointwise affine split.

The deterministic no-M261-import checker passed exact `k=3,5`
falsification tests and supplied a `J=2` witness proving that the accepted
`X_D,Y_D` component-size/run-count profile does not determine `E_ell`.
Finite values were not promoted to PBV or a sign theorem.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `check_pbv_reduction.py`
- `results.txt`
- `final_report.md`
- this `freeze_manifest.md`

`SHA256SUMS` inventories every file above and excludes itself.

## Scope firewall

This artifact proves no PBV, FD, minority-sign, FCL1, comparison, spectral
gap, polynomial mixing, or Terminal statement. It makes no claim about the
global identity-word law or the lazy exact `{3,4,5}` heat-bath chain.
