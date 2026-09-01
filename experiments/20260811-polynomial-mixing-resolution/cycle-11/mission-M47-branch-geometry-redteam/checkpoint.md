# M47 halfway checkpoint: branch locality fails in both directions

Date: 2026-08-11.  This is a genuine halfway checkpoint, not a terminal
claim.  The target is the uniform global identity-bridge law and the original
lazy `K`; permutations compose as `(pq)(x)=p(q(x))`.

## 1. Common outside-forest lemma (proved)

Let `w,w' in F_N` differ only in a length-`r` interval and let the two blocks
have the same ordered product.  Every prefix before the interval is identical,
and every prefix from the end of the interval onward is identical.  Hence all
factors outside the interval have the same join/cut status in `w,w'`, and the
same outside join edges occur in both prefix join trees.

If the old interval contains `k` joins, its height change is `2k-r`.  The new
interval has the same endpoint heights and the same length, hence also exactly
`k` joins.  Removing those `k` old tree edges leaves a common forest with
exactly `k+1` components.  The old and new interval join edges are two
spanning-tree completions of this forest.  In particular `k<=r`, but the
forest components may have order `Theta(N)`.

This strengthens the inherited statement that at most `r` tree edges change.
It also identifies the obstruction: reconnecting even three macroscopic
components can change global branch geometry macroscopically.

## 2. Exact `H4` macroscopic-diameter jump (proved)

Put `N=3s`, `s>=2`, and let `T` be the path on `1,...,3s`.  Delete

```text
a=(s,s+1),  b=(2s,2s+1).
```

The remaining forest has the three path components
`A=[1,s]`, `B=[s+1,2s]`, and `C=[2s+1,3s]`.  Choose a vertex `z` in the
middle third of `B`, and put

```text
c=(s,z),  d=(z,2s+1).
```

Then `T'=T-{a,b}+{c,d}` is a spanning tree, `deg_T'(z)=4`, and

```text
diam(T)=3s-1,
diam(T')<=2s+2,
```

so the diameter changes by at least `s-3=Theta(N)`.

Make a paired identity word from the edges of `T`, ordering the two designated
edge-squares consecutively as

```text
(a,a,b,b).
```

Replace this block by `(c,c,d,d)` and leave every other edge-square fixed.
Both blocks have product identity; both full words lie in `F_N`; their prefix
join trees are exactly `T,T'`.  This is one literal `H4` outcome of the
original chain.  If

```text
E_N=F_4(id)=M^2+18 binom(N,3)+12 binom(N,4),
M=binom(N,2),
```

then this specified transition has probability

```text
1/[6(m-3)E_N] >= 1/[6(m-3)M^4]                       (2.1)
```

for `N>=3,m=2N-2`, because `|R_m|=3`.  The formula for `E_N` follows by
squaring the two-transposition factor counts: `M` factorizations of `id`,
three of each of the `2 binom(N,3)` oriented 3-cycles, and two of each of the
`3 binom(N,4)` double transpositions.

Thus diameter, centroid balance, and largest-branch thresholds do **not** have
an `O(1)` internal shell under `r<=5`, despite the `r`-edge common-forest
bound.  This makes a locality-only Terminal-B proof invalid.

## 3. Pointwise Hurwitz action is false (exact finite refutation)

Complete enumeration of `F_4` finds the path word

```text
(01),(23),(01),(02),(23),(03)                         (3.1)
```

with no oriented adjacent Hurwitz move whose new prefix join tree is not a
path.  For `N=4`, having a path is equivalent to having a perfectly balanced
tree edge, so (3.1) also has zero adjacent-Hurwitz exit from that cut.

The enumeration checks all `|F_4|=6!*4=2880` states.  At `N=5`, the paired
path word

```text
(12)^2,(02)^2,(34)^2,(04)^2                          (3.2)
```

is another zero-Hurwitz-exit state.  The `N=5` enumeration checks all
`8!*5^2=1,008,000` states.  These are counterexamples only to a pointwise
Hurwitz shortcut.  They are not full-`K` traps: for example an identity
four-block in (3.2) can be refreshed to another pair of squares that produces
a branching spanning tree, with probability bounded as in (2.1).

## 4. Exact branch-layer falsification

At `N=5`, the rooted-largest-branch statistic

```text
L_0(T)=max{|C|: C is a component of T-{0}}
```

has exact `F_5` layer sizes

```text
L_0:       1       2       3       4
count:  8,856 192,744 286,440 519,960.
```

They are unimodal but not log-concave because

```text
286440^2 < 192744*519960.
```

Hence ordinary log-concavity cannot supply a universal polynomial median
shell for a rooted pendant-branch threshold.  The diameter, centroid-balance,
and edge-balance layers happen to be unimodal/log-concave through `N=5`; this
finite pass proves nothing asymptotic.

The same run recovers the nonuniform join-tree marginal.  At `N=5`, the
factorization-fiber weights per labeled tree are exactly `8856` for a star,
`8254` for the degree-3 shape, and `7808` for a path.  Thus even a correct
uniform-Cayley branch estimate cannot simply be substituted for the actual
law.

## 5. Current exact frontier

The strongest clean candidate is the extreme-diameter cut

```text
P_N={w in F_N:T_join(w) is a labeled path}.
```

It has conditional mass `2136/2880` at `N=4` and `468480/1008000` at
`N=5`.  The finite zero-Hurwitz witnesses and the macroscopic `H4` jump show
that neither a pointwise Hurwitz bound nor a thin-shell upper bound is valid.
The remaining standalone proposition is:

> **PATH-TREE FULL-K ACTION.**  There are universal `c>0,C<infinity` such
> that for all `N>=6`,
> `Q_K(P_N,P_N^c)/pi(P_N)>=c(Nm)^(-C)` at `m=2N-2`.

This source-normalized inequality already implies the two-sided conductance
bound because `min(pi(P_N),pi(P_N^c))<=pi(P_N)`; no unproved smaller-side
orientation is hidden.  Proving it requires an aggregate count of genuine
`H3/H4/H5` branch-changing outcomes under the nonuniform join-tree fiber law.

## 6. Exact artifacts and commands

The deterministic harness is `branch_geometry_falsifier.py`; it has no random
seed and records Python `3.12.3`, commands, conventions, and tested claims.

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch_geometry_falsifier.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch-N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch_geometry_falsifier.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch-N5.json
```

Finite passes are used only to refute the named pointwise and log-concavity
claims.  No finite conductance trend is extrapolated.
