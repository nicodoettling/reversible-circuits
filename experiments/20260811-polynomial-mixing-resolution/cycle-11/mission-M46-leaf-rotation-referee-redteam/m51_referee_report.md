# Fresh referee report on M51 degree-profile thresholds

Date: 2026-08-11.  Frozen bundle audited:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/
  mission-M51-original-k-degree-profile-redteam/report.md
SHA-256 919349e3f7ea32eb6f7524a7b22e5679d27a271378c4ff31b2fee9d4c935c62e
```

Convention: `(pq)(x)=p(q(x))`; factor tuples multiply left-to-right.  The
kernel is the literal half-lazy uniform `{3,4,5}` same-product heat bath, and
stationary masses below are global masses on `Omega(N,2N-2)`.

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The accepted scoped result is that, for every `N>=4` and
`2<=q<=N-1`, both

```text
{w in F_N: number of leaves of T_J(w)>=q},
{w in F_N: maximum degree of T_J(w)>=q}
```

have `Phi_pm^K>=1/(24N^7)`.  This rejects two original-`K` scalar threshold
bottlenecks; it is not a gap theorem or Terminal A/B.

## Critical audit

### 1. Leaf deletion and threshold layer: accepted

M51 restates the M49 strand-deletion proof, including exactly two null
increments, output in `F_(N-1)`, join tree `T-v`, and at most `(N-1)^2`
lifts for fixed deleted label/output/null positions.  I accepted that proof
separately in `m49_referee_report.md`.

For a leaf `v` with neighbor `u`,

```text
ell(T-v)=ell(T)-1+1{deg_T(u)=2}.
```

Thus every tree in the `ell>=q` cut maps into the base `ell>=q-1` cut,
giving

```text
J_N(q)<=N binom(m,2)(N-1)^2 J_(N-1)(q-1).
```

The layer indexing remains correct at `q=2` and at `q=N-1`.

### 2. Reverse leaf insertion, including the star: accepted

A base tree on `N-1` vertices with exactly `q-1` leaves has exactly
`N-q` nonleaves.  Attaching the new leaf to any of them raises the leaf
count to `q`.  If the base has at least `q` leaves, attaching anywhere
preserves membership, and M51 selects a deterministic set of `N-q` labels.
These two cases give exactly `N-q` selected attachments for every word in
`J_(N-1)(q-1)`.

After insertion of the adjacent square in any of `m-1` gaps, the new label
occurs only in that square.  Hence attachment, gap, and base word are
recoverable, and

```text
|S_L|=(N-q)(m-1)J_(N-1)(q-1)
```

has no overlap correction.  When `q=N-1`, the base threshold is the star
layer with `N-2` leaves, `N-q=1`, and the unique selected nonleaf is its
center; insertion produces the `N`-vertex star.

### 3. Maximum-degree deletion and reservoir: accepted

Deleting a leaf reduces every old degree by at most one, so

```text
Delta(T-v)>=Delta(T)-1
```

and the identical deletion multiplicity gives

```text
A_N(q)<=N binom(m,2)(N-1)^2 A_(N-1)(q-1).
```

If the base maximum is exactly `q-1`, attachment to a deterministic
maximum-degree vertex raises it to `q`.  If it is already at least `q`, any
deterministic attachment preserves membership.  One attachment and each of
the `m-1` gaps therefore give the injective reservoir

```text
|S_D|=(m-1)A_(N-1)(q-1).
```

At `q=N-1`, the only base layer is again a star, and the selected vertex is
its center.  Thus the maximum-degree claim genuinely uses the same square
mechanism but the correct one-attachment count; no leaf-count multiplicity
is silently reused.

### 4. Literal original-`K` exit and orientation: accepted

The marked-square `H3` refresh is exactly the one audited for M49.  Its
specified outcome removes the new label and exits `F_N`; its probability is

```text
p_N=1/[6(m-2)D_N^3],
D_N^3=(3N^2+N-12)/2.
```

This includes half-laziness, the factor `1/3` for choosing block length,
the `m-2` windows, and the full conditional triple fiber.  `H4,H5` are
retained as nonnegative flow.

All source and cut counts share the exact global denominator
`|Omega(N,m)|`, and

```text
min(pi(C),pi(C^c))<=pi(C)
```

is the only mass orientation used.  The exact certified source fractions
are

```text
2(N-q)/[Nm(N-1)^2]  for leaf count,
2/[Nm(N-1)^2]       for maximum degree.
```

Multiplying by `p_N` proves the displayed exact bounds.  With
`N-q>=1`, `m,m-2<=2N`, and `D_N^3<=2N^2`, both are at least
`1/(24N^7)`.

### 5. Boundary cases and finite falsification: accepted

Paired star words witness all source cuts, and `(12)^m` lies in every global
complement.  For `N=4,q=3`, the base `F_3` star layer has 24 words; one
center attachment and five gaps give exactly 120 marked sources.  The same
count applies to both endpoint statistics.  My independent rerun of the
exact threshold consequence audit passes all 20 leaf and 20 maximum-degree
rows for `4<=N<=8`.  This finite check is a falsifier only.

## Strongest self-attack and scope

Every certified transition leaves `F_N`.  Enlarging the cut to contain
`F_N^c` seals the entire reservoir.  The theorem does not control arbitrary
subsets inside one degree layer, joint degree profiles, surplus length, or
any macro-closed cut.  It therefore cannot be iterated into a global
Poincare inequality.

## Reproduction

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M51-original-k-degree-profile-redteam/leaf_threshold_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output /tmp/m46-m51-leaf-threshold-rerun.json
```

The rerun used Python 3.12.3, exact integers, no seed, and no nonstandard
dependency.
