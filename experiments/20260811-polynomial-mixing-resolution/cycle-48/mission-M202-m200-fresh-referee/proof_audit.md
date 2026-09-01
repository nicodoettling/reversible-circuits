# M202 mathematical audit of M200

Date: 2026-08-13 UTC.

## 1. Reconstructed finite object

The fresh checker imports no predecessor Python. It reconstructs M181's two
`d=5` words in the order of patterns `0,1`, closes the signed Hurwitz orbit
under global-label canonicalization, and obtains 8,400 quotient states with
source IDs `(16,0)`. All fourteen action permutations exactly match the frozen
M191 action and all signed pairs are mutual inverses.

For each source coordinate and each root `r=0,...,4`, it relabels root `r` to
the distinguished DPS root, independently finds a Prüfer-tree/DPS descriptor,
applies each of the seven adjacent-value edits, and canonicalizes the target.
This yields exactly 70 coordinate root-edge rows. Combining the two roots for
the same edit yields all 175 simultaneous pair rows. Sorted pair targets
deduplicate into exactly 54 classes with the same IDs and full occurrence
lists as M196/M200.

## 2. Exact arbitrary-color quantifier

For `G=S_5` and `H=Stab_G(5)`, the global action on the connected minimal
sector is free; thus each global orbit splits into exactly `[G:H]=5` distinct
`H`-orbits. The five rooted representatives enumerate precisely these five
edges over each left source vertex.

A perfect-matching color has one edge over every left global orbit. Therefore,
over M181's two source vertices it selects roots `(r_0,r_1)`, hence one of the
25 simultaneous root-pair incidences for that edit. This does not rely on
coordinatewise membership: the M196 word attached to that row acts
diagonally and was replayed to the paired endpoint. M135 freezes no numerical
color assignment; normalizing colors by their roots over the first source
makes the second roots a permutation. Since all five possible second roots
are certified for every normalized edit/color row, the conclusion holds for
every arbitrary perfect-matching coloring.

## 3. Route replay and coverage

All 54 stored M196 full words replay from `(16,0)` to the independently
reconstructed target pair. Their occurrence classes cover all 175 root pairs,
with no uncovered class. The exact digests are

```text
packed Q5 action: 160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae
M196 results:     e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2
M200 incidence:   48b37502a45be316efe39728cee5cb3125c4cc3196b547cf3e90c923e87187f1.
```

The longest archived quotient certificate has length 22.

## 4. Full voltage and M175 endpoint implication

M181's exact `d=5` family uses patterns `[[0],[1]]` and voltage basis
representative `[0,1]`. Since `W_2=F_2^2/<(1,1)>` is one-dimensional and
`(0,1)` is not diagonal, every color's selected pair has `V_stab=W_2` by
M181's coordinatewise relabeling theorem.

M196's simultaneous route puts the matched quotient target in the source
component. For any fixed physical representatives and physical DPS targets,
M175 says the route-voltage set is the affine coset

```text
a_T(U,V)+V_stab.
```

Because `V_stab=W_2`, that coset contains zero. Hence some zero-relative-
voltage route to the fixed endpoints exists.

Crucially, this may require prepending a source-stabilizer loop to the stored
quotient route. M200 does not claim that its length-`<=22` quotient word itself
has zero voltage. Neither a correction length nor a corrected total length is
known, so no quantitative or polynomial route theorem follows.

## Numbered objections

None.

The accepted theorem is exact finite `d=5` for M181's width-two family only.
It has no all-`d`, arbitrary-subfamily, gap, mixing, or Terminal consequence.
