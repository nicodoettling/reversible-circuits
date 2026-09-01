# M200 theorem: every d=5 matching color has a routed full-voltage pair

Date: 2026-08-13 UTC.

## 1. Exact finite statement

Fix `d=5`, an adjacent DPS edit `1<=i<=7`, and any perfect-matching color
`M` in M135's orbit-incidence multigraph `B_(5,i)`. Let `q_0,q_1` be M181's
two constructed quotient points with block patterns `0,e_1`. Then the two
edges of `M` over `q_0,q_1` form M181's accepted width-two source subfamily,
its actual stabilizer-voltage space is all of `W_2`, and its paired matched
target tuple lies in the synchronized quotient component of `(q_0,q_1)`.

Consequently M181's conditional fixed-endpoint result applies: for every
choice of physical representatives of those two edges and their physical DPS
targets, a zero-relative-voltage quotient route exists. This is qualitative;
no length is assigned to the voltage-corrected route.

## 2. Exhaustive root parameterization

Put `G=S_5` and `H=Stab_G(5)`. The global conjugation action on the minimal
connected sector is free. Therefore every global orbit is the disjoint union
of exactly five `H`-orbits, parameterized by the five cosets of `H` in `G`.
M191/M198's root convention uses the transpositions exchanging root
`r in {0,...,4}` with the distinguished root 4, so its five root values are
exactly these five `H`-orbit edges, not a sample or a multiset with omissions.

For each edit and each of the two left source orbits, M200 extracts the target
global-orbit ID for every root. This gives exactly

```text
7 edits * 2 source orbits * 5 roots = 70
```

root-edge rows. For fixed `(i,r_0,r_1)`, the coordinate targets combine into
one simultaneous target pair. The 175 possible keys

```text
(i,r_0,r_1),  1<=i<=7,  0<=r_0,r_1<=4,
```

occur exactly once among M196's 54 deduplicated target classes. All 175 keys
carry a target-pair certificate ID, and direct replay of the corresponding
M196 word sends source IDs `(16,0)` to that exact pair.

## 3. Quantification over arbitrary matching colors

A perfect-matching color has exactly one edge over every left global orbit.
In particular, over `q_0` and `q_1` it selects roots `r_0(M)` and `r_1(M)`.
The selected two-edge subfamily therefore corresponds to the single
root-pair incidence

```text
(i,r_0(M),r_1(M)).
```

This is a simultaneous pair statement: M196's archived word acts diagonally
on both coordinates and reaches the paired target. It is not inferred from
two unrelated single-coordinate memberships.

M135 freezes no particular numerical edge coloring at `d=5`, so numerical
color names have no invariant root assignment. One may normalize any actual
coloring by labeling its colors with their five distinct roots above `q_0`;
the roots above `q_1` then form a permutation. The exhaustive 25-row table for
each edit covers every value of that permutation. Hence the theorem holds for
every actual M135 color and is independent of an arbitrary coloring choice.

## 4. Full voltage and endpoint implication

M181's exact `d=5` row has ordered patterns `[[0],[1]]` and voltage basis
representative `[0,1]`. Its coordinatewise relabeling argument transfers that
same nonzero class to whatever physical `H`-orbit representatives the color
selects. Since `dim W_2=1`, the pair has `V_stab=W_2`.

The simultaneous M196 certificate proves the matched quotient target is in
the source quotient component, discharging the sole hypothesis in M181
Section 7. M175's affine criterion then gives a zero-relative-voltage route to
the fixed physical endpoints after adding an appropriate source-stabilizer
loop.

The archived M196 word, of length at most 22 in this finite list, certifies
only the quotient route. It is not asserted to have zero voltage. No length
is proved for the added stabilizer correction or for the resulting corrected
route, and no polynomial-length conclusion follows.

## 5. Exact boundary

There are no uncovered target classes among the 175 incidences. The theorem is
only for M181's explicit width-two family at `d=5`. It does not prove arbitrary
matching-subfamily routing, an all-`d` route theorem, a quantitative route
bound, a spectral gap, mixing, or any Terminal conclusion.
