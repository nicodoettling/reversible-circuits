# M174 freeze manifest

Freeze date: 2026-08-13 UTC.

## Decision

```text
STRICT REDUCTION; PCS-BOUND UNRESOLVED.
```

The exact PC response is reduced to a rooted-tree/cycle-index boundary
coefficient. Constant and affine component terms, including the exact signed
triangle/double kind transfer, are discharged. The first unproved statement
is `(BR)`: the combined two-channel signed boundary coefficient
`eta(B_k)=O(1)`.

## Frozen artifacts

- `plan.md`
- `checkpoint.md`
- `proof.md`
- `pcs_channel_calibration.py`
- `pcs_channel_exact.json`
- `results.json`
- `report.md`
- this `freeze_manifest.md`
- `SHA256SUMS`

## Validation

- Frozen predecessor checksum manifests named in the plan passed before use.
- Exact ordered-lift calibration was limited to odd `k=3,5,7`.
- Frozen fixed-cell signed sums matched exactly at all three values.
- `J=0` common cancellation, `J=1` zero kind transfer, and the exact `J=2`
  triangle/double transfer formula were asserted over `Fraction`.
- Python source passes `ast.parse`; JSON artifacts parse; `git diff --check`
  passes; no `.pyc` or `__pycache__` remains.
- Final repository status for the owned path contains only this new M174
  directory. M169 and all predecessor/coordinator paths remained immutable.

## Scope and review request

No FD-bound, broad quotient matrix, shell scan, finite-sign promotion,
direct-L1/H0/gap, mixing, or Terminal inference is included. Request a fresh
independent referee for the exact `U,V` decorations, affine constants
`L_T=0,L_D=-2`, closed kind-transfer formula, and equivalence of `(BR)` with
PCS-bound.
