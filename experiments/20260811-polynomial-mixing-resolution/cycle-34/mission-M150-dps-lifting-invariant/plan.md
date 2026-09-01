# M150 plan: DPS aligned Schur/lifting invariant

Date: 2026-08-13 UTC.

## Objective and exact scope

For a nonempty subfamily of one accepted M135 orbit-incidence matching, align
its source words `u^1,...,u^s` into factor tuples

```text
x_j=(u_j^1,...,u_j^s) in P_(d,s),  1<=j<=2d-2.
```

Formulate from an explicit central extension a lifting invariant that is
preserved by a common signed Hurwitz action. Determine whether this invariant
can distinguish the aligned source tuple from the aligned target tuple.

This is a necessity-only mission. It will not claim a common braid, a braid
diameter, a comparison, a spectral gap, or either terminal outcome.

## Accepted dependencies

- M135/M137: polynomial conflict coloring and exact matching-coset reduction.
- M141/M143: for `d>=5`, every nonempty matching subfamily has aligned source
  and target generated subgroup exactly `P_(d,s)`.
- M146/M148: the aligned factor conjugacy-class multiset is automatically
  constant in that regime.

No unchecked literature theorem will be imported. Any double-cover statement
used in the conclusion will be proved from an explicit presentation/cocycle.

## Work program

1. Define a concrete Pin/Schur central extension of `S_d`, including an
   auditable multiplication rule or presentation.
2. Define the reduced lifting invariant for the transposition class and prove
   exact invariance under signed Hurwitz moves.
3. Compute the class-centralizer commutators. Test whether disjoint
   transpositions kill the central kernel for `d>=4`.
4. Treat the boundary rank `d=3` separately and determine whether its surviving
   sign distinguishes any accepted M135 matching source/target subfamily.
5. Run deterministic bounded diagnostics at `d=3`, and at `d=5` if a compact
   representative-level check is feasible; cap all closure/enumeration.
6. Self-attack orientation, cover, quotient, product-one, signed-move, and
   subfamily-width assumptions. Freeze proof, checker, JSON, report, manifest,
   and hashes.

## Candidate outcomes

- `KEEP`: an exact lifting obstruction/refinement descriptor with polynomial
  range; or
- `KEEP NEGATIVE`: proof that the natural reduced Schur invariant is trivial or
  automatically equal on every relevant source/target pair.

