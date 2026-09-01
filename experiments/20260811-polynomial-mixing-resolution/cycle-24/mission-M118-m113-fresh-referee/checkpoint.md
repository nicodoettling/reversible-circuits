# M118 checkpoint: M113 fresh audit

Date: 2026-08-12 UTC.

## Provisional decision

```text
ACCEPT is supported; no material numbered objection has survived audit.
```

This is a scope-reduced, nonterminal acceptance of M113's exact projection
reduction and named obstructions.  It is not evidence for the open polynomial
gap of the local incidence chain.

## Frozen integrity

The assigned M113 hashes match:

```text
295c6d50b70117915cc99d9ebe6e1e88cbfab258a404db66a0b1543ea01cfe47  report.md
64cf3bb48baca3022690cb72c5afc458e3fbf8e514b56612c099b7f9b1e0b6bf  freeze_manifest.md
```

`sha256sum -c SHA256SUMS` returns `OK` for every M113 payload.  Every upstream
M97/M101/M104/M110 digest recorded in M113's manifest also matches.

## Proof audit completed

- Re-derived `bar_pi(kappa)=S_kappa/|X_d|` and the exact holding/cut-refresh
  Gibbs flow.  The holding mass is exactly one half of the projected kernel,
  so `beta>=gap(G)/2` is correctly normalized.
- Re-derived validity and reversibility of `A_d`.  The inequalities
  `Q_G>=2D^-2 Q_A` and `bar_pi<=D rho` give
  `gap(G)>=2D^-3 gap(A)` and hence `beta>=D^-3 gap(A)`; the measure comparison
  is used in the correct direction.
- Checked realizable-key necessity and constructive sufficiency, adjacent
  overlap, the join/cut dichotomy, and the simple-Hurwitz cell count.
- Checked the connectivity reduction to `p=id`, the two-step decrease of
  `|Q_L|`, communication of all extreme keys, and the `d=2` singleton.
- Verified the first-Higgs-lift rank formula and basis characterization.
- Reconstructed the weighted and untilted `d=4` derivative Hessians exactly.
  Their determinants are respectively `8294400` and `1/82944`; zero trace and
  nonsingularity force inertia `(2,2)`.
- Re-derived the balanced split formula and binomial aggregate lower bound.

## Independent computation

`independent_audit.py` imports no predecessor mission code.  Exhaustive
`d=2,3,4` enumeration found no missing or extra combinatorial keys, no cell
formula failure, no Cartesian-cell failure, no adjacent overlap failure, no
move-type failure, and one connected key graph in each case.  It reproduces:

| d | keys | gap(A) | gap(G) | beta |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 9 | 0.1414353635 | 0.0896143806 | 0.1461033961 |
| 4 | 101 | 0.1254163084 | 0.0980244430 | 0.1288510552 |

The fixed-p Higgs basis counts are `1,18,378` for `c=2,3,4`.  The finite
two-sided singleton-split-or-reverse minima are `1/4` and `1/3` at `d=3,4`,
with no zero-rate key.  These facts are proof calibration only.

## Remaining scope

Write and freeze the final referee report.  Do not attack the unresolved
`gap(A_d)>=d^{-O(1)}` lemma in this mission.
