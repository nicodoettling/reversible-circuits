# M51 halfway checkpoint

## Candidate theorem

Let `ell(T)` be the number of leaves and

```text
L_(N,q)={w in F_N:ell(T_J(w))>=q},  2<=q<=N-1.
```

The current proof gives, for every `N>=4`,

```text
Phi_pm^K(L_(N,q))
 >=(N-q)/[3N(2N-2)(N-1)^2(2N-4)D_N]
 >=1/(24N^7),
D_N=(3N^2+N-12)/2.                                  (C.1)
```

This is a full original-`K` lower-flow statement, not a conclusion imported
from the auxiliary plane-tree/parking chain.

## Count mechanism

Write

```text
J_N(q)=|L_(N,q)|,
L_N^del=binom(2N-2,2)(N-1)^2.
```

The M49 strand-deletion proof is statistic-free: for any prefix-join-tree
leaf `v`, erasing `v` from every prefix permutation gives exactly two null
steps, a base word in `F_(N-1)` with join tree `T-v`, and at most
`L_N^del` preimages per fixed deleted label and base word after summing null
positions.

Deleting a tree leaf changes leaf count by

```text
ell(T-v)=ell(T)-1+1{the neighbor of v has degree 2}.
```

Thus every word with at least `q` leaves deletes to a word with at least
`q-1` leaves.  Choosing one leaf and summing over its `N` possible labels
gives

```text
J_N(q)<=N L_N^del J_(N-1)(q-1).                     (C.2)
```

Conversely, fix the new label `v=N`.  If a base tree has exactly `q-1`
leaves, it has exactly

```text
(N-1)-(q-1)=N-q
```

nonleaves; attaching `v` to any one raises the leaf count to `q`.  If the
base has at least `q` leaves, every attachment preserves membership, so
choose any canonical `N-q` attachment labels.  In each of the `m-1` gaps,
insert the adjacent square `(v,u)^2`.  These states are distinct and give

```text
|S_(N,q)|=(N-q)(m-1)J_(N-1)(q-1).                   (C.3)
```

The extreme threshold `q=N-1` is included: the base is a star with one
nonleaf, and attachment at its center produces a larger star.

## Exact flow and orientation

One padded `H3` refresh removes the new label with exact probability

```text
p_N=1/[6(m-2)D_N].                                   (C.4)
```

The target is outside `F_N`, hence outside the cut.  With global uniform
stationarity,

```text
Q_K(L,L^c)=Q3+Q4+Q5>=pi(S_(N,q))p_N,
min(pi(L),pi(L^c))<=pi(L)=J_N(q)/|Omega(N,m)|.
```

Equations (C.2)--(C.4) give the first inequality in (C.1).  The second uses
`N-q>=1`, `m<=2N`, `m-2<=2N`, and `D_N<=2N^2`.

## Remaining checks

1. Exact-check (C.2) against weighted leaf layers through the available
   `N=8` fixed-tree dynamic program.
2. Re-audit source uniqueness and the `q=N-1` star endpoint.
3. Freeze full calibrations, dependency labels, runtime, and self-attack.

If these checks pass, the scoped verdict will be `PROVED`; it remains
nonterminal because arbitrary degree-profile refinements and cuts enlarged
outside `F_N` are not controlled.

## Post-halfway upgrade: maximum-degree thresholds

The same deletion mechanism also controls a genuinely different degree
statistic.  If `Delta(T)` is maximum degree, deleting a leaf lowers `Delta`
by at most one.  Conversely, from a base tree with `Delta=q-1`, attach the
new leaf to a canonical maximum-degree vertex; from a base with `Delta>=q`,
any canonical attachment preserves the threshold.  Thus, with
`D_(N,q)={w in F_N:Delta(T_J(w))>=q}`,

```text
Phi_pm^K(D_(N,q))
 >=1/[3N(2N-2)(N-1)^2(2N-4)D_N]
 >=1/(24N^7),  2<=q<=N-1.
```

This includes the extreme star threshold and will be audited alongside the
leaf layers before the final report is frozen.
