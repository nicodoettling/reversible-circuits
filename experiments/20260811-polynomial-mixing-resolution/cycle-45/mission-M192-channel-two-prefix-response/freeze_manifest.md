# M192 freeze manifest

Freeze date: 2026-08-13 UTC.

## Decision

```text
STRICT EXACT J=2 SHARED-ENDPOINT/DISJOINT-PROFILE REDUCTION.
DV, DE, CONDITIONAL J=2 PREFIX, PCR/WPCR, AND ALL DOWNSTREAM CLAIMS REMAIN OPEN.
```

## Immutable dependency gate

Every artifact in the accepted M180, M182, M186, and M189 checksum manifests
passed before derivation. No predecessor was edited.

## Frozen M192 artifacts

- `plan.md`
- `checkpoint.md`
- `j2_prefix_reduction.md`
- `j2_prefix_check.py`
- `j2_prefix_results.json`
- `results.json`
- `report.md`
- this `freeze_manifest.md`
- `SHA256SUMS`

## Proved content

- Exact shared-endpoint coefficients `gamma_L,gamma_F` and total triangle
  masses.
- Complete shared-endpoint prefix contribution `O(1/k)` with collisions
  retained.
- Exact disjoint-pair Abel identity with nonzero endpoint
  `-6(k-1)/[k(2k-1)(2k-3)]`.
- Uniform signed disjoint cumulative bound `|E_u|=O(sqrt(u)/k)`.
- Strict remaining profile lemmas `(DV)` and `(DE)`.

## Validation and scope

The deterministic standard-library checker is capped at exact `k=3,5,7`;
all assertions pass and every reported diagnostic is finite-only. Python AST
and both JSON files parse; nine report fields, whitespace, and cache hygiene
pass.

No attempt to prove `(DV)`, `(DE)`, or `(PCR)` after the cap; no broad
quotient computation, final channelwise absolute split, PCS/FCL1/direct-L1,
H0/gap, mixing, or Terminal inference. Request a fresh immutable audit of the
Cayley convolution, gamma denominators, triangle masses, disjoint Abel
endpoint/sign, `(EW)`, and exact sufficiency of `(DV)+(DE)`.
