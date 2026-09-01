# M199 freeze manifest

Freeze date: 2026-08-13 UTC.

## Decision

Strict exact literal-profile reduction. `(IKBE)`, `(DV)`, `(DE)`,
conditional `J=2` prefix, and every downstream claim remain open.

## Frozen artifacts

`plan.md`, `checkpoint.md`, `double_profile_reduction.md`,
`double_profile_check.py`, `double_profile_results.json`, `results.json`,
`report.md`, this manifest, and `SHA256SUMS`.

## Proved content

- Per-placement denominator `R_*=2k-3`.
- Exact full B and A disjoint profile formulas, with untouched-cycle term.
- Literal four-part adjacent-split deletion/merge map.
- Precise standalone `(IKBE)` and its implication to `(DV)/(DE)`.

## Validation and audit request

All 540 exact assertions at `k=3,5,7,9` pass; finite-only. Request a fresh
immutable audit of `R_*`, B face orientation, A untouched mass, collision
retention, and the IKBE implication. No predecessor edit or downstream claim.
