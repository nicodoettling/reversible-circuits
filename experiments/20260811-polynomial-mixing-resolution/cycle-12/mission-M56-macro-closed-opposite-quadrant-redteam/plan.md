# M56 plan: opposite mixed-quadrant full-`K` red team

## Exact target

For `(pq)(x)=p(q(x))`, `N>=4`, `m=2N-2`, and the literal lazy exact
`{3,4,5}` chain, study

```text
Z_(N,q,r)={w in F_N:ell(T_J(w))<q and b(T_J(w))>=r},
2<=q<=N-1, 1<=r<=floor(N/2).
```

Either prove inverse-polynomial two-sided conductance for both nontrivial
macro-closed cuts `F_N^c union Z` and `F_N^c union (F_N minus Z)`, with exact
global orientation and complete `H3,H4,H5` flow accounting, or construct a
literal Terminal-B family.

## Proposed deletion/insertion scheme

Let `W=F_N minus Z` and
`Lambda_N=binom(2N-2,2)(N-1)^2`.

- Deletion sends `Z` into `{ell<q,b>=r-1}`.  Restore a tight base by choosing
  a global tree leaf inside a smaller side of a balance witness and attaching
  the new leaf there.  Leaf count stays fixed and the smaller side grows by
  one.
- Deletion sends `W={ell>=q or b<r}` into
  `{ell>=q-1 or b<r}`.  If balance is low, centroid attachment preserves it;
  otherwise attach at a nonleaf to restore the leaf threshold.
- Fix the new label, insert the marked square in every gap, and use the exact
  padded `H3` refresh into `F_N^c`.

## Critical lemma to audit

Every side of a tree edge contains a global tree leaf: choose a vertex
farthest from the bridge endpoint within that side.  If the side is a
singleton, its bridge endpoint is itself a global leaf; otherwise a farthest
vertex is not the bridge endpoint and has global degree one.

This supplies the simultaneous tight insertion even at `r=2` and at the even
endpoint `r=N/2`.

## Bounded falsification and limitation

An exact `N<=8` shape audit will test both deletion inequalities and every
claimed attachment.  Finite success is falsification only.  Even a universal
quadrant theorem will not control a bounded rectangle, a fixed joint-profile
cell, or arbitrary subsets within a cell.

## Supersession notice

The coordinator reported after creation that M56 was already assigned to the marked-root-history lane. This planning file is retained append-only and is **SUPERSEDED WITHOUT EXECUTION**. The opposite-quadrant work continues as M57 under `cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/`.
