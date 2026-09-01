# Fresh referee report on M52 macro-closed profile thresholds

Date: 2026-08-11.  Frozen bundle audited:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/
  mission-M52-macro-closed-tree-profile-redteam/report.md
SHA-256 6d157387016e8cc126380e45d3f2d80390ddf338fb6991724073b6ae5cf0db7e
```

Convention: `(pq)(x)=p(q(x))`; factor tuples multiply left-to-right.  The
kernel is the literal half-lazy uniform `{3,4,5}` same-product heat bath, and
`pi` is uniform on global `Omega(N,2N-2)`.

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The accepted scoped statement is: for every `N>=4`, both placements of
`F_N^c` in every nontrivial prefix-join-tree leaf-count or edge-balance
threshold have `Phi_pm^K>=1/(24N^7)`.  This rules out these macro-closed
scalar cuts; it is not Terminal A/B.

## Critical audit

### 1. Low-tail strand deletion: accepted

For leaves,

```text
ell(T-v)=ell(T)-1+1{deg_T(neighbor(v))=2}<=ell(T).
```

Thus a state with `ell<q` deletes into the same low threshold on `N-1`
vertices.  For edge balance, every surviving edge changes from a split
`a,N-a` to `a-1,N-a` when the deleted leaf is on the `a` side, and

```text
min(a-1,N-a)<=min(a,N-a).
```

The removed leaf edge disappears, so `b(T-v)<=b(T)`.  Combining either fact
with the accepted strand fiber
`Lambda_N=binom(m,2)(N-1)^2` gives exactly

```text
l_N^s(q)<=N Lambda_N l_(N-1)^s(q).
```

This remains valid at leaf `q=N-1` and the maximum balance threshold.

### 2. Canonical low reservoirs: accepted

Every base tree has a canonical leaf.  Attaching the new label to that old
leaf makes the old leaf degree two and the new vertex a leaf, so the total
leaf count is unchanged.

For balance, choose a canonical centroid `u` of the base tree.  For every old
edge, its side not containing `u` is contained in one centroid branch and
has size at most half the old tree.  Adding the new leaf on the `u` side
therefore leaves that edge's smaller-side size exactly unchanged.  The new
edge has balance one, while every nontrivial old tree already has balance at
least one.  Hence total edge balance is exactly unchanged.

In each case there is one selected attachment and `m-1` square-insertion
gaps.  The new label occurs only in the square, so base, attachment, and gap
are recoverable.  Thus

```text
|S_low^s|=(m-1)l_(N-1)^s(q)
```

with no overlap loss, and the deletion inequality gives the exact source
ratio

```text
|S_low^s|/l_N^s(q)>=2/[Nm(N-1)^2].
```

### 3. Both global mass orientations: accepted

For the `+` placement, the complement is literally the low set and has mass
`l_q^s/Z_N`.  The certified transition is written from that complement into
`F_N^c`, which lies in the macro-closed side.  Reversibility gives
`Q(A,A^c)=Q(A^c,A)`, and

```text
min(pi(A),pi(A^c))<=l_q^s/Z_N.
```

For the `-` placement, the complement is the high set of mass `h_q^s/Z_N`;
the M49/M51 high reservoir similarly refreshes into `F_N^c`, and
`min mass<=h_q^s/Z_N`.  No assumption on whether `pi(F_N)` or either closed
side is above one half is made.  The character-content formula for `Z_N` is
correct but is only needed to display exact finite masses, not for the
universal inequality.

### 4. High-side sources and endpoints: accepted

For leaf count, deletion lowers the statistic by at most one, and the exact
reverse reservoir has `N-q` selected attachments per base in the `q-1`
tail.  This includes `q=2` and `q=N-1` (the base star, with one center
attachment).

For balance with `q<N/2`, the M49 threshold-preserving deletion and all
`N-1` leaf attachments give the stated source ratio.  When `N=2q`, deletion
lands in the maximum base layer `q-1`; a canonical `q-1,q` edge has a
smaller side with exactly `q-1=(N-2)/2` attachment labels, and each makes the
old edge perfectly balanced.  The endpoint factor and resulting
`1/(96N^6)>=1/(24N^7)` bound are therefore correct.  Odd `N` has no separate
endpoint because `floor(N/2)<N/2`.

### 5. Literal transition and complete block accounting: accepted

The marked-square refresh has exact specified probability

```text
p_N=1/[6(m-2)D_N],
D_N=(3N^2+N-12)/2.
```

It includes half-laziness, uniform choice among block sizes, all `m-2`
triple windows, and the exact conditional fiber.  Replacing the square by a
base-label square preserves ordered block product and removes the new label,
so the target lies in global `Omega` and in `F_N^c`.

For a macro-closed threshold, a boundary transition either has exactly one
endpoint in `F_N` or has both endpoints in `F_N` and crosses the scalar
profile threshold.  Transitions with both endpoints in `F_N^c` cannot cross
because all of `F_N^c` lies on one side.  Hence M52's six-term decomposition
into `H3/H4/H5` times macro/internal is exhaustive.  The certificate uses
one nonnegative `H3` macro term; every other triple outcome, all internal
crossings, and all `H4,H5` flow remain present.  This is legitimate for a
lower-flow theorem.

### 6. Constants and finite calibration: accepted

The low source ratio times `p_N` is

```text
1/[3Nm(N-1)^2(m-2)D_N]>=1/(24N^7).
```

The high leaf, ordinary balance, and even-endpoint expressions reproduce
the stated `N^-7`, `N^-6`, and endpoint bounds.  At `N=4`, exact masses
indeed show that orientation cannot be guessed: leaf `q=3` has closed-side
mass `75/164`, while balance `q=2` has `133/164`.  My independent rerun
passes all 24 low-tail rows and the exact character masses through `N=8`.
This is a bounded falsifier only.

## Strongest self-attack and scope

The theorem controls two scalar profile families but still uses one-label
exits.  A joint leaf/balance profile can exclude both canonical low
attachments, and arbitrary within-layer or surplus-length cuts remain
untouched.  No internal Poincare inequality for `F_N` follows.

## Reproduction

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M52-macro-closed-tree-profile-redteam/macro_closed_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output /tmp/m46-m52-macro-closed-rerun.json
```

The rerun used Python 3.12.3, exact integers/rationals, no seed, and no
nonstandard dependency.
