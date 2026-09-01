# M58 halfway checkpoint

## Stronger theorem under audit

Rectangles are not the true boundary of the argument.  Let `A` be an
arbitrary subset of the labeled trees on `[N]`; no relabeling invariance,
monotonicity, or consistency across `N` is assumed.  Put

```text
R_A={w in F_N:T_J(w) in A}.
```

Both nontrivial cuts

```text
F_N^c union R_A,
F_N^c union (F_N minus R_A)
```

have the preliminary exact bound

```text
Phi_pm>=1/[3Nm(N-1)^2(m-2)D_N]>=1/(24N^7),
D_N=(3N^2+N-12)/2.                                  (1)
```

Thus every fixed profile cell, bounded profile rectangle, diagonal shape
union, centroid event, diameter event, and arbitrary labeled join-tree event
is covered at once.

## Valid attachment pairs

For each possible new/deleted label `v`, define

```text
P_v(A)={(z,u):z is in F on label set [N] minus {v},
                 u !=v,
                 T_J(z)+{v,u} is in A}.
```

Choose one tree leaf `v` from every `w in R_A`, strand-delete it, and record
the output word `z`, its former tree neighbor `u`, and the two null positions.
The recorded `(z,u)` belongs to `P_v(A)`.  For fixed
`v,z,u,null positions`, M49's insertion-coordinate fiber has size at most
`(N-1)^2`; recording `u` only reduces that fiber.  Therefore

```text
|R_A|<=binom(m,2)(N-1)^2 sum_v |P_v(A)|.             (2)
```

No stationary tree law or shape enumeration enters (2).

## Reverse sources and collision accounting

For every `(z,u) in P_v(A)` and each of the `m-1` gaps of `z`, insert the
adjacent square `(v,u)^2`.  The first factor joins fixed `v`, the second cuts
it back, and the remaining prefixes agree with `z`; the new join tree is
exactly `T_J(z)+{v,u}` and hence lies in `A`.

For fixed `v`, a source has at most one representation: its only two
`v`-incident factors identify the adjacent square, `u`, the gap, and `z`.
A source can have representations for several different leaf labels, but at
most `N` of them.  Hence the number of distinct sources satisfies

```text
|S_A|>=(m-1)sum_v |P_v(A)|/N.                        (3)
```

Choose one representation deterministically for every distinct source before
assigning its transition, so no boundary flow is counted twice.  Combining
(2) and (3),

```text
|S_A|/|R_A|>=2/[Nm(N-1)^2].                          (4)
```

Apply the identical construction to the complementary tree family `A^c`.

## Exact full-chain exit

For the chosen representation, pad the square by a neighboring base
transposition `a` and refresh

```text
((vu),(vu),a)->(f,f,a)
```

or the left-padded endpoint version, with `f` chosen on the labels other than
`v`.  The target omits `v`, belongs to `F_N^c`, and occurs with exact
probability `1/[6(m-2)D_N]`.  Literal global mass of the complementary
tree-saturated side or `R_A` orients each macro-closed cut.  Every unused
`H3` and all `H4,H5` terms remain nonnegative.  This proves (1) once the pair
multiplicity audit is accepted.

## Self-audit and finite calibration

- Every target tree has a leaf, so a nonempty family has a nonempty valid-pair
  sum.
- The deleted leaf's old neighbor is uniquely defined and reconstructs the
  target join tree.
- Distinct source representations for a fixed label are impossible because
  that label appears exactly twice and adjacently.
- The M49 exact `N=4,5` strand audits already verify the stronger underlying
  word deletion/lift statement; new shape enumeration would only retest a
  tautological leaf deletion/reattachment.
- For `S_4,m=6`, this covers every subset of the 16 labeled tree fibers, not
  only the two leaf/balance shape classes.  Exact global orientation still
  uses `|Omega|=3936`, `|F_4|=2880`.

## First gap after this theorem

Membership in `R_A` is constant across the entire word fiber over a join
tree.  The first uncovered cuts vary inside one or more fixed join-tree
fibers.  A natural next proposition is a polynomial mean-lift/internal-flow
bound for functions with zero conditional mean on each join-tree fiber.
