# M54 plan: macro-closed mixed-quadrant red team

## Exact target

Use `(pq)(x)=p(q(x))`, `N>=4`, `m=2N-2`, and the literal lazy
`{3,4,5}` exact same-product heat-bath chain `K`.  On the minimal connected
macro `F_N`, define

```text
X_(N,q,r)={w:ell(T_J(w))>=q and b(T_J(w))<r},
2<=q<=N-1, 1<=r<=floor(N/2).
```

Prove a universal inverse-polynomial two-sided conductance bound, with exact
global orientation and all block-length flow retained, for each nontrivial
cut

```text
F_N^c union X_(N,q,r),
F_N^c union (F_N minus X_(N,q,r)),
```

or construct a literal Terminal-B family.

## Proposed counting route

Let `Y_N=F_N minus X_N` and
`Lambda_N=binom(2N-2,2)(N-1)^2`.

1. Leaf deletion sends `X_N(q,r)` into
   `{ell>=q-1,b<r}` and sends `Y_N(q,r)` into
   `{ell<q or b>=r-1}`.
2. Restore `X` by attaching the new leaf at a centroid.  A centroid is a
   nonleaf, so leaf count rises, while every old edge balance is unchanged.
3. Restore `Y`: if `ell<q`, attach at a leaf and preserve leaf count; if
   `ell>=q,b>=r`, any attachment preserves balance; if
   `ell>=q,b=r-1`, attach inside a smaller balance-witness side.  At the even
   endpoint `r=N/2`, the base split `r-1,r` becomes `r,r`.
4. Insert the marked adjacent square at any gap and use the exact padded
   `H3` refresh into `F_N^c`, with probability
   `1/[6(m-2)D_N]`, `D_N=(3N^2+N-12)/2`.
5. Divide source counts by the literal global mass of the complementary
   profile side, not by conditional mass in `F_N`.

## Named falsification checks

An exact `N<=8` audit will test both deletion inequalities and attachment
existence on every stored unlabeled join-tree shape and feasible threshold.
It is bounded falsification only.  The main possible obstruction is a tight
balance witness whose smaller side cannot accept a leaf without crossing the
leaf boundary; here that issue occurs on the complement side where leaf count
is already high, so it should be harmless.

## Expected limitation

Even success controls only one mixed quadrant.  It will not imply expansion
inside a fixed joint-profile cell, an arbitrary profile subset, or a global
Poincare inequality.

## Supersession notice

This planning file was created before the coordinator reported that M54 was already assigned to the root-mean-lift referee. It is retained append-only for traceability and is **SUPERSEDED WITHOUT EXECUTION**. The mixed-quadrant lane continues at `cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/`.
