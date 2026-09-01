# M186 freeze manifest

Freeze date: 2026-08-13 UTC.

## Decision

```text
STRICT EXACT CRITICAL-BOREL/ABEL AND SIGNED-PREFIX REDUCTION.
THE COMPLETE J=1 CONDITIONAL CHARGE IS O(1/n).
J=2/PCR, SCBR, BIR, BR, PCS-BOUND, AND ALL DOWNSTREAM CLAIMS REMAIN UNRESOLVED.
```

## Frozen dependency gate

Before derivation, every accepted checksum manifest passed for M91,
M94/M100, M102/M105, M155/M159, M161/M166, M168/M171, M174/M178, and
M180/M182. No predecessor was edited.

## Frozen M186 artifacts

- `plan.md`
- `checkpoint.md`
- `component_boundary_reduction.md`
- `component_abel_check.py`
- `component_abel_results.json`
- `results.json`
- `report.md`
- this `freeze_manifest.md`
- `SHA256SUMS`

## Proved content

- Exact combined critical-Borel chord formula `(CB)` for `M_1(d),M_2(d)`.
- Exact component-valued Abel identity `(BA-C)` retaining both channels,
  triangle/double kind, ordered collisions, and two-run boundary effects.
- Exact `J=1` laws `rho_A,rho_B`, including same-run and cross-run chords,
  and the conditional `O(1/k)=O(1/n)` charge bound.
- Exact full-channel summation-by-parts identity `(SBP)` and
  `M_1(1)=O(1/n)`.
- Strict remaining coefficient lemmas `(PCR)` and `(WPCR)`; both are
  explicitly unresolved.

## Validation

- Deterministic standard-library exact checker capped at `k=3,5`; all
  coefficient, Abel, face-law, and formal summation-by-parts assertions pass.
- The complete coefficients match frozen M180 at both calibration ranks.
- Python AST and both JSON files parse; repository whitespace and cache
  hygiene checks pass.

## Scope and fresh-audit request

No channelwise final absolute split, finite-sign inference, broad shell or
quotient computation, `k=7`, FD/FCL1/direct-L1, H0/gap, mixing, or Terminal
