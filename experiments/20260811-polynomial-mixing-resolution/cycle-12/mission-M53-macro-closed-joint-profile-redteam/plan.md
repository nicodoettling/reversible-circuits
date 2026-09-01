# M53 plan: macro-closed joint tree-profile red team

## Objective

Work with permutations composed by `(pq)(x)=p(q(x))`, words evaluated as
`t_1...t_m`, `N>=4`, and `m=2N-2`.  Let `F_N` be the minimal connected
full-support identity macro.  For its prefix join tree `T_J(w)`, write
`ell(T)` for the number of tree leaves and

```text
b(T)=max_(e in E(T)) min{|C_e|,N-|C_e|}.
```

For feasible thresholds define

```text
J_(N,q,r)={w in F_N: ell(T_J(w))>=q and b(T_J(w))>=r}.
```

The exact target is to prove an inverse-polynomial two-sided conductance
bound for each of the two macro-closed original-`K` cuts

```text
F_N^c union J_(N,q,r),
F_N^c union (F_N minus J_(N,q,r)),
```

or construct a literal Terminal-B family after accounting for global mass and
all `H3,H4,H5` flow.

## Kernel and accounting

The reviewed chain is

```text
K=(1/2)I+(1/6) sum_(s=3)^5 (1/(m-s+1)) sum_i H_(i,s),
```

where each heat bath is uniform on the exact same-product transposition
fiber.  The proof will retain the full Dirichlet flow and may lower-bound it
by an explicitly counted `H3` subflow.  For a transposition block product,

```text
D_N=|F_3(a)|=(3N^2+N-12)/2.
```

## Proposed proof route

1. Reuse, with a complete statement, the leaf-strand deletion map: deleting
   a join-tree leaf produces a word in `F_(N-1)` and has fixed-position lift
   multiplicity at most `(N-1)^2`.
2. Prove deletion inequalities for both the joint upper set and its
   complement.  Leaf deletion lowers `ell` and `b` by at most one and cannot
   increase either statistic.
3. Construct a simultaneous high-profile insertion.  If both constraints
   are tight, attach the new leaf to the bridge endpoint on the smaller side
   of a balance witness; prove this endpoint is a nonleaf except in the sole
   star corner, where the target joint set is empty.
4. Construct a low-complement insertion by splitting into `ell<q` and
   `ell>=q,b<r`: attach at a leaf in the first case and at a centroid in the
   second.
5. Insert the corresponding adjacent square at any gap and refresh it with a
   padded exact `H3` move to leave `F_N`.  Divide by the literal global
   `|Omega(N,m)|` and orient using the exact complement profile mass.
6. Build an exact `N<=8` shape-weight audit only to falsify the two deletion
   inequalities and insertion-existence lemma.  Finite success will not be
   used as the universal proof.

## Expected failure modes

- A base tree simultaneously tight at `ell=q-1,b=r-1` may have no nonleaf on
  a smaller witness side.
- Attaching at a centroid may preserve balance but accidentally leave the
  wrong joint-complement side.
- Summing deletion labels or square sources may hide a multiplicity factor.
- The globally smaller side need not be the conditionally smaller profile
  side because `F_N^c` has substantial mass.
- A result for these two scalar intersections still does not control an
  arbitrary refinement inside one joint layer or prove a global gap.

## Computation metadata

The exact audit, if used, is deterministic (`seed=null`), records Python and
repository commit metadata, and has no nonstandard dependency.  Its named
falsification targets are the deletion inequalities and simultaneous
attachment existence, not asymptotic mixing.
