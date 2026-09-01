# M134 halfway checkpoint

Date: 2026-08-13 UTC.

## Strongest finding

The fresh standard-library checker independently reproduces M132's decisive
`d=4,i=1` obstruction with no mismatch:

```text
canonical tree       {(1,2),(1,3),(2,4)}
pi_x                 (3,2,1,4,6,5)
pi_y                 (3,2,1,5,6,4)
full descriptor      equal field by field
source pair subgroup (V4 x V4)Diag(S4), order 96
target pair subgroup (A4 x A4)Diag(S4), order 288
```

The target subgroup is exactly the parity-diagonal subgroup. All four words
are in brute-enumerated `Z_4`, and the root-independent descended map gives
the displayed targets.

## Polynomial-range risk check

The potentially dangerous closure-history field is polynomial only because a
face label has at most one distance-three closure. The independent closure
implementation enforces that DPS quadrangle uniqueness and exhaustively sees
maximum one at `d=3,4`. With the distance-three field empty or singleton, the
safe fieldwise bound is indeed

```text
E^2 [d(d-1)]^4 B^4 (S+1)^10 = O(d^40).
```

For `d=2`, first/last closure values require the harmless empty marker; the
state space is a singleton.

## Complete finite recalibration

- Brute targets equal the fresh DPS images: `|Z_3|=24`, `|Z_4|=2880`, with
  exact root fibers `3` and `4` and zero descended-map collisions.
- Full descriptor class counts for adjacent indices `1,...,5` are exactly
  `2741,2717,2745,2782,2758`. Exhausting every within-class pair finds a
  subgroup conflict at every index; the displayed `i=1` pair is reproduced.
- For every `d=3` index: action image order `216`; conflict graph has 24
  vertices, 80 edges, clique/chromatic numbers `3/3`; one-schedule agreement
  maximum `6`; and the exact schedule-cover minimum is `5`.
- M132's raw capped searches mark every cap or first-certificate stop
  non-exhaustive. No capped non-finding is promoted in its report.

No material objection has emerged. Remaining work is the written scope audit,
final `ACCEPT/REJECT` decision, reproducibility checks, and freeze.
