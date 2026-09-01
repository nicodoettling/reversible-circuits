# M133 halfway checkpoint

Date: 2026-08-13 UTC.

## Status

The universal ordinary log-concavity inequality and DEFECT NO-VALLEY remain
unresolved.  A strict structural step has been proved: M125's subtractive
connected extraction can be replaced on its required unicycle diagonal by a
fully positive, canonical unique-cycle recurrence.

For fixed indexed cycle atoms, every ordered pair of partitions on the
connected diagonal has a bipartite incidence multigraph with `E=V`, hence a
unique even cycle.  Put the least-labelled core edge first and take its left
core neighbour second.  This selects a unique orientation and removes all
cycle symmetry factors, including the two-parallel-edge core.  Each off-core
component is a tree attached to one core vertex.  Recursively, at a planted
vertex one partitions the remaining edge set into child branches, chooses the
unique child edge incident to the root in each branch, applies the positive
block weight to the resulting incident set, and alternates colour.  The
resulting recurrence uses additions and products of positive rational weights
only.

The proof is the canonical unique-cycle decomposition and its inverse; finite
checks are only audits.  `positive_unicycle_audit.py` independently compares
the recurrence with literal ordered pairs of set partitions and currently has
zero mismatches for all 37 integer cycle types through total label size seven.
The core-profile extension through `d=8` also has zero reconstruction failures.

## Falsification status

The frozen weakest ordinary log-concavity ratio at `d=22,r=7` is about
`1.01180537`.  A targeted exact evaluator avoids the expensive irrelevant
low-cycle types and gives:

```text
d=23, r=7: 1.00806970271
d=24, r=8: 1.00625245219
d=25, r=8: 1.00342080614
d=26, r=9: 1.00237055991
```

All remain strictly above one, but the trend makes an eventual counterexample
a live possibility.  These are exact finite facts only.  The stress scan is
capped at `d=26`; no sign is extrapolated beyond it.

Separating the positive expansion by core length gives individually
log-concave finite core profiles through `d=8`, with no failure yet.  This too
is only a falsification check; sums of log-concave profiles need not be
log-concave without an additional synchronized-ratio or total-positivity
statement.

## First remaining lemma

Write `H_k[d,c]` for the exact positive contribution whose unique bipartite
incidence core has `k` edges (`k` even).  A sufficient, explicit next route is
to prove core-profile ratio control strong enough that

```text
(sum_k H_k[d,c])^2
  >= (sum_k H_k[d,c-1])(sum_k H_k[d,c+1]).
```

Termwise log-concavity alone is not asserted sufficient.  If the targeted
scan finds a negative exact margin, the priority changes to freezing the
minimal counterexample and testing the strictly weaker no-valley property.

No spectral-gap or terminal claim follows from the checkpoint.
