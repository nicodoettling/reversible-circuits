# M132 halfway checkpoint

Date: 2026-08-13 UTC.

## Strongest result at halfway

The natural one-schedule-per-two-label-contour-metadata proposal is
**REFUTED at `d=4`** by an exact paired-source invariant, even after retaining
a fixed polynomial number of scalar contour fields.

For adjacent value index `i=1`, put

```text
x =((12),(13),(13),(12),(34),(34)),
y =((12),(13),(13),(34),(12),(34)).
```

The independent DPS reconstruction gives

```text
tau_1(x)=((12),(23),(13),(24),(23),(34)),
tau_1(y)=((12),(23),(13),(34),(24),(34)).
```

Both sources have the same canonical Cayley tree
`{(1,2),(1,3),(2,4)}` and permutations

```text
pi_x=(3,2,1,4,6,5),     pi_y=(3,2,1,5,6,4).
```

Swapping values `1,2` produces the displayed targets. The sources have the
same tested descriptor consisting of:

- the exact two affected physical factors;
- the two hairy-edge black/white endpoints;
- the oriented first/second black endpoints of the two faces;
- the two directed hairy-boundary traversal positions for each edge; and
- for each label, counts of distance-one/distance-three closures, first and
  last global closure times, and the distance-three closure time.

Nevertheless, the coordinatewise factor pairs of `(x,y)` generate a subgroup
of `S_4 x S_4` of order `96`, while the coordinatewise target pairs generate
one of order `288`. A common signed braid would preserve this literal
subgroup, so no fixed schedule works for both sources.

The source group is `(V_4 x V_4) Diag(S_4)`: diagonal transpositions generate
`Diag(S_4)`, and the off-diagonal pair yields a double transposition in one
coordinate. The target group is `(A_4 x A_4) Diag(S_4)`, equal to the
parity-diagonal subgroup: an off-diagonal pair yields a 3-cycle in one
coordinate. Their orders are respectively `16*24/4=96` and
`144*24/12=288`.

## Exact finite calibration

At `d=3`, complete action-image data reproduce the accepted five-schedule
minimum. The new canonical shortest-path library has seven schedules and a
five-class greedy cover for `i=1` (seven for `i=2,3`); it is only a finite
upper bound. At `d=4`, the enriched polynomial contour summary has between
`2717` and `2782` observed keys on `2880` physical sources, depending on `i`,
yet every `i` has an incompatible size-two key class.

## Scope and next step

This is a rigorous obstruction to the named metadata selector, not an
asymptotic lower bound on the number of schedules. A valid schedule class
must be pairwise compatible under the generated-subgroup test, so a future
proof needs a polynomial coloring/compression theorem for that compatibility
relation. Recording the complete two-label closure histories has raw
`d^{O(d)}` possibilities, and the full contour word has `d^{O(d^2)}`
possibilities; neither is a polynomial schedule key without new compression.

Next: make the `d=3` metadata statements exhaustive in the script, freeze the
hand proof and exact `d=4` certificates, and state scheduled/compressed source
recovery and the factor-`d` root quotient conditionally on any future
polynomial compatibility coloring.
