# Fresh referee report on M49 symmetric branch balance

Date: 2026-08-11.  Frozen bundle audited:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/
  mission-M49-symmetric-branch-balance/report.md
SHA-256 a809459cb1babfa445776d922fc1fa733eb905e1a4bdff6c15fb4f0d9f33dcdc
```

Convention: `(pq)(x)=p(q(x))`; tuple products are left-to-right.  The
kernel is the exact half-lazy uniform `{3,4,5}` same-product heat bath.  I
audited M49 independently of the auxiliary parking/plane-tree results.

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The accepted scoped statement is: for every `N>=4`, `m=2N-2`, and
`1<=q<=floor(N/2)`, the literal global cut

```text
B_(N,q)={w in F_N:max_(e in T_J(w)) min(|C_e|,N-|C_e|)>=q}
```

satisfies

```text
Q_K(B_(N,q),B_(N,q)^c)
 /min{pi(B_(N,q)),pi(B_(N,q)^c)} >=1/(96N^6).
```

This is an original-`K` anti-bottleneck theorem, not Terminal A or B.

## Audit of the critical steps

### 1. Strand deletion and the two null increments: accepted

Erasing `v` from a permutation cycle is compatible with right
multiplication exactly as M49's tables (2.5)--(2.6) state.  A factor avoiding
`v` projects to the same transposition.  A factor `(v,x)` projects either to
the identity (insertion coordinate `bottom` or `x`) or to `(a,x)`, where `a`
is the current predecessor of `v`.

If `v` is a leaf of the prefix join tree, its first incident factor is its
unique support join, occurs while `v` is fixed, and is therefore a null
increment.  Every other join-tree edge avoids `v` and survives.  Hence the
non-null increments have connected support on the remaining `N-1` labels
and telescope to the identity.  Such a word has length at least `2N-4`:
there are at least `N-2` support joins, each a permutation-cycle join, and
an equal number of cycle cuts is needed to return to identity.  The number
of null increments is positive and even, while the old length is `2N-2`.
It is consequently exactly two, and deleting them gives a member of
`F_(N-1)`.

No projected internal factor becomes a new support join.  After the unique
join at `v`, deleting leaf `v` leaves its prefix join-tree component
connected; for a projected `(a,x)`, both endpoints lie in that component.
Thus the output join tree is literally `T_J(w)-v`.

### 2. Fixed-position lift multiplicity: accepted

Fix the deleted label, output word, and the two null locations.  Before the
first null the insertion coordinate is `bottom`; that null chooses one of
`N-1` initial coordinates.  Between the nulls, a projected support join is
forced to lift as the same transposition: the alternative `v`-incident lift
would make a second join-tree edge at `v`.

At a projected cycle cut, one history has at most two descendants.  When it
branches, their insertion coordinates lie in the two distinct cycles just
created.  Descendants of one initial coordinate remain in pairwise distinct
permutation cycles.  They all lie in one evolving support component; a
support join adds another component and cannot merge two descendant cycles,
and a later internal factor cannot be a cycle join because a minimal
`F_(N-1)` word has exactly its `N-2` support/cycle joins.  A cut only splits
one cycle.  There are at most `N-1` cycles, hence at most `N-1` descendants
per initial coordinate and at most `(N-1)^2` lifts.  At the second null the
factor is forced to `(v,a)` and returns the coordinate to `bottom`; every
later lift is forced.  Invalid branches were only overcounted.

### 3. Threshold deletion and the even endpoint: accepted

For `q<N/2`, a witnessing edge has a side of size at least `q+1`; a leaf on
that side other than the bridge endpoint can be deleted while retaining a
`q,q`-or-larger split.  For `N=2q`, a perfectly balanced edge is unique,
neither bridge endpoint is a leaf, and deleting any tree leaf leaves that
edge split `q-1,q`.  Since `q-1` is the maximum possible balance on
`2q-1` vertices, the output lies in the exact endpoint layer.  These facts
give the two count inequalities with

```text
L_N=binom(2N-2,2)(N-1)^2.
```

The endpoint reservoir is also correctly indexed: take a base tree in the
maximum `q-1` layer, orient a deterministic `q-1,q` edge, and attach the new
leaf to any of the `q-1=(N-2)/2` labels on its smaller side.  The old edge
becomes `q,q`.

### 4. Root-square reservoir and source injectivity: accepted

Inserting `(v,u),(v,u)` in any of the `m-1` gaps of a base word produces a
minimal connected identity word.  The new label occurs exactly in that
adjacent square, so the source recovers its base word, attachment label, and
gap.  Off the endpoint this yields

```text
(N-1)(m-1)H_(N-1)(q)
```

distinct sources; at the endpoint it yields

```text
(q-1)(m-1)H_(N-1)(q-1).
```

Adding a leaf cannot decrease the smaller-side size of an old edge, so the
off-endpoint sources all remain in the threshold cut.

### 5. Literal `H3` exit and all normalizations: accepted

Use the window beginning with the square, except at the final gap where the
window ends with it.  Replacing

```text
(vu),(vu),a by f,f,a,
```

or its left-padded version preserves ordered block product and removes every
factor incident to `v`; the target is a global identity word outside `F_N`.
For a transposition product `a`, the exact triple-fiber size is

```text
D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.
```

The three terms correspond to first factor equal to, sharing one endpoint
with, or disjoint from `a`.  The specified transition probability is exactly

```text
1/2 * 1/3 * 1/(m-2) * 1/D_N =1/[6(m-2)D_N].
```

Thus the half-laziness, uniform choice among all three block lengths, all
`m-2` `H3` windows, and conditional-fiber normalization are present.  The
`H4,H5` contributions are retained as nonnegative flow; they are not being
discarded in an upper-bound argument.

### 6. Global stationary orientation and constants: accepted

All counts are divided by the literal global `|Omega(N,2N-2)|`.  The proof
uses only

```text
min(pi(B),pi(B^c))<=pi(B),
```

so it is valid whichever side is smaller.  The source fractions are exactly

```text
2/[Nm(N-1)]                         (q<N/2),
(N-2)/[Nm(N-1)^2]                   (N=2q).
```

Multiplication by the `H3` probability gives M49's (1.4)--(1.5).  The
coarse inequalities `m,m-2<=2N`, `D_N<=2N^2`, and `N-2>=N/2` give
`1/(24N^6)` off the endpoint and `1/(96N^6)` at it.

### 7. Boundary and finite calibration: accepted

The path-tree paired-square word makes every stated threshold nonempty; the
disconnected word `(12)^m` is in the global complement.  The theorem starts
at `N=4`, where a base-label transposition `f` always exists and
`R_m={3,4,5}`.  My independent reruns reproduced:

```text
N=4: |F_N|=2880, max fixed-position fiber 8<=9,
     balance layers 744,2136, endpoint failures 0;
N=5: |F_N|=1008000, max fixed-position fiber 13<=16,
     balance layers 44280,963720, preserving-leaf failures 0.
```

These are bounded falsifiers only; the acceptance rests on the universal
argument above.

## Dependencies and self-attack

The proof uses only the standard minimal-word join/cut count and exact
heat-bath stationarity, both re-derived where needed.  It does not import the
parking-tree stationary law.  Its strongest limitation is structural: every
certified edge leaves the minimal connected sector.  An enlarged cut which
contains the missing-label targets, an internal refinement of a balance
layer, or a surplus-length cut can seal all these exits.  Hence acceptance
does not imply a global gap.

## Reproduction

I reran, with output in `/tmp`:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 4 --output /tmp/m46-m49-strand-N4-rerun.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 5 --output /tmp/m46-m49-strand-N5-rerun.json
```

Python was 3.12.3; the calculation is deterministic and has no nonstandard
dependency.
