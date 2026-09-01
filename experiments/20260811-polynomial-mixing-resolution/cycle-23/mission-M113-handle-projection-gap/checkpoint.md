# M113 halfway checkpoint: a connected local incidence reduction

Date: 2026-08-12 UTC.

## 1. Scope and status

The auxiliary target is

```text
X_d={w=(t_1,...,t_(2d)): eval(w)=id, support(w) connected}, d>=2,
pi_d=Unif(X_d).
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The base and lift are exactly M104's

```text
P_d=I/2+[1/(4D)] sum_(i=1)^D(R_i+R_i^(-1)), D=2d-1,
tilde_pi(w,j)=1/[|X_d| ell(w)],
L((w,j),(w',j'))=P_d(w,w')/ell(w').
```

This checkpoint proves an exact stationary-flow reduction and qualitative
connectivity of its new local key chain.  It does **not** prove a polynomial
gap for that chain, `beta(d)`, `gamma_1(d)`, or the full heat-bath chain.
Classification H is not used.

## 2. Exact holding/cut-refresh projection

Let `kappa(w,j)=(j,p,Q_L,Q_R)` be M104's key and write `w incident kappa`
when its unique cut with the key's `j` realizes `kappa`.  Put

```text
S_kappa=sum_(w incident kappa) 1/ell(w).
```

**PROVED.**  The exact projected stationary mass is

```text
bar_pi(kappa)=S_kappa/|X_d|.                         (C.1)
```

Extract only the explicit holding `I/2` in `P_d`.  Conditional on holding,
the lift keeps `w` and refreshes its cut uniformly in `J(w)`.  After doubling
this half-kernel to a Markov kernel `G_d` on keys,

```text
G_d(kappa,lambda)=
  [1/S_kappa] sum_(w incident kappa,lambda) 1/ell(w)^2,       (C.2)
Q_G(kappa,lambda)=
  [1/|X_d|] sum_(w incident kappa,lambda) 1/ell(w)^2.         (C.3)
```

Rows sum to one and (C.3) is symmetric.  Equivalently, under the joint law

```text
Pr(W=w,K=kappa(w,j))=1/[|X_d|ell(w)],                (C.4)
```

`W` is uniform on `X_d`, `K|W` is uniform over the central cuts, and `G_d`
is the two-block Gibbs update `K -> W -> K'`.  Therefore

```text
beta(d)=gap(bar L) >= (1/2) gap(G_d).                 (C.5)
```

Physical signed-Hurwitz transitions contribute additional nonnegative
Dirichlet flow and are not needed for (C.5).  Compression also gives the
trivial circular inequality `beta(d)>=gamma_1(d)`; it is not used here.

## 3. Realizable keys are decorated connected unicycles

Let `Cyc(p)` be the cycle partition of `p`.  A tuple
`(p,Q_L,Q_R)` is a realizable central key exactly when:

1. `Q_L` and `Q_R` coarsen `Cyc(p)`;
2. the bipartite multigraph with vertices `Q_L union Q_R` and one edge per
   `p`-cycle is connected and unicyclic;
3. `j=d+|Q_R|-|Q_L|`.

**PROVED.**  Necessity is M97's accepted incidence theorem plus the side
genus equations.  Conversely, connected-unicyclic gives
`c(p)=|Q_L|+|Q_R|`.  A block `C` then needs exactly
`|C|+c(p_C)-2` factors.  Such a connected factorization exists
elementarily: factor each permutation cycle minimally, then append adjacent
squares along a tree joining the cycles.  Interleave the block words on each
side.  Their total lengths are

```text
d+c(p)-2|Q_L|=d+|Q_R|-|Q_L|=j,
d+c(p)-2|Q_R|=2d-j.
```

The fixed connected incidence graph makes the concatenated support connected,
so the constructed word realizes the key.

## 4. Exact adjacent-cut overlap and a local raw chain

Let `kappa=(j,p,Q_L,Q_R)` and
`lambda=(j+1,p',Q'_L,Q'_R)` be realizable.  Write `join(Q,t)` for the support
partition obtained by adding transposition `t` to a word with support `Q`.

**PROVED adjacent compatibility and overlap.**  The two cells share a word
exactly when

```text
t=p^(-1)p' is a transposition,
Q'_L=join(Q_L,t),
Q_R=join(Q'_R,t).                                    (C.6)
```

In that event every common word has the unique form `u,t,v'`, and M104's
side sets give the literal bijection

```text
C_kappa intersect C_lambda = U_kappa x {t} x V_lambda,
|C_kappa intersect C_lambda|=|U_kappa||V_lambda|.     (C.7)
```

Indeed `eval(t v')=t p'^(-1)=p^(-1)`, and the support joins in (C.6) are
exactly the two old-side partitions.  Conversely a common word forces all
of (C.6).

The move has exactly two incidence forms.  If `t` joins two `p`-cycles,
those cycles lie in distinct `Q_L` blocks, `p'=pt` joins them,
`Q'_L` merges those blocks, and `Q'_R=Q_R`.  If `t` cuts one `p`-cycle,
then `Q'_L=Q_L`, while `Q'_R` splits the old right block so that adjoining
the support edge `t` recovers `Q_R`.  These are respectively a left
coagulation and right fragmentation; reversal exchanges the two.

Let

```text
Z_inc=sum_kappa |C_kappa|=sum_w ell(w),
rho(kappa)=|C_kappa|/Z_inc.
```

Define the local adjacent-incidence chain `A_d` by its off-diagonal flows

```text
Q_A(kappa,lambda)=
  |C_kappa intersect C_lambda|/(2 Z_inc)              (C.8)
```

for compatible `|j(lambda)-j(kappa)|=1`, with all remaining row mass held.
Each word has at most two adjacent central cuts, so (C.8) is a valid
reversible Markov chain.  Combining `1<=ell<=D`,
`|X_d|<=Z_inc<=D|X_d|`, and (C.1)--(C.3) gives

```text
D^(-1) <= d bar_pi/d rho <= D,
Q_G(kappa,lambda) >= (2/D^2) Q_A(kappa,lambda),
gap(G_d) >= (2/D^3) gap(A_d),
beta(d) >= gap(A_d)/D^3.                              (C.9)
```

Thus a polynomial gap for `A_d` is sufficient for the exact handle-cell
projection gap.  Unlike `bar L`, `A_d` uses only adjacent cut shifts; its
state space, mass, and every off-diagonal flow have the combinatorial formulas
above.  M104's exact side counts make (C.7)--(C.8) evaluable without summing
over hidden component lengths.

More explicitly, the classical genus-zero simple-Hurwitz formula gives, for
a block `B` containing `c_B` cycles of `p`,

```text
|F(B,p_B,k_B)|
 = k_B! |B|^(c_B-3)
   product_(p-cycle a subset B) |a|^|a|/(|a|-1)!.
```

After both side interleavings cancel the `k_B!` factors,

```text
|C_kappa|=j!(2d-j)!
 product_(B in Q_L union Q_R)|B|^(c_B-3)
 product_(p-cycle a)[|a|^|a|/(|a|-1)!]^2.            (C.10)
```

The final product is independent of how the cycles are grouped.  Thus every
local coagulation/fragmentation probability is an explicit factorial and
block-size ratio; no hidden-word count remains in `A_d`.

There is a proved matroid skeleton at fixed `p`.  Let the `c=c(p)` cycles be
vertices, take red and blue copies of every edge of `K_c`, let `M` be the
direct sum of the two colored graphic matroids, and let `N` be the graphic
matroid of the doubled multigraph after forgetting colors (parallel red/blue
edges retained).  Every flat of `N` consists of all colored edges internal to
blocks of a vertex partition, hence is also a flat of `M`; thus `N` is a
quotient of `M`.  The first Higgs lift has

```text
r_H(X)=min(r_M(X),r_N(X)+1).
```

Its rank-`c` bases are exactly the colored size-`c` edge sets for which each
color class is a forest and the uncolored union is connected.  Contracting
the red and blue forest components gives precisely a connected-unicyclic
bipartite incidence graph.  Thus each fixed-`p` incidence key is a marginal
of this Higgs-lift matroid basis family.

**UNRESOLVED lift compatibility.**  Transition (C.6) changes `p` by joining
or cutting cycle atoms.  Its two Higgs-lift ground sets therefore have
different vertex sets, so one ordinary basis exchange on a fixed ground set
cannot literally be the full `A_d` move.  To invoke the accepted
strongly-log-concave down--up gap one still needs one global augmentation
whose exchange implements atom coagulation/fragmentation and has marginal
(C.10), or a polynomial stationary-flow comparison across the variable
ground sets.  The fixed-`p` skeleton alone has no off-diagonal `A_d` move and
does not prove a gap.

## 5. Universal qualitative connectivity of `A_d`

**PROVED.**  The adjacent key graph is connected for every `d>=2`.

First suppose `p` has a nontrivial cycle.  Pick `x` on that cycle and put
`t=(x,p^(-1)(x))`; then `p'=pt` splits off the singleton cycle `{x}`.  Keep
`Q_L` fixed and split the `Q_R` block containing that cycle into `{x}` and
its complement.  The new singleton incidence edge is a leaf; replacing the
old edge by the leaf plus the residual cycle edge preserves connectedness and
unicyclicity.  Conditions (C.6) hold, so this is an `A_d` edge increasing
`j` by one.  Repeating makes `p=id`.

Now `p=id` implies `|Q_L|+|Q_R|=d`.  If `|Q_L|>1`, connectedness forces some
right vertex to meet two distinct left vertices.  Choose singleton cycle
labels `x,y` on those two edges and put `t=(x,y)`.  Multiplying by `t` merges
the cycles and merging their two left vertices contracts the incidence path
through their common right vertex; the graph remains connected unicyclic.
This is one adjacent edge.  A singleton-splitting edge as in the preceding
paragraph then restores `p=id`, lowers `|Q_L|` by one, and raises `|Q_R|` by
one.  Iteration reaches

```text
kappa_e=(2d-2,id,{[d]}, {{endpoints(e)} and all other singletons}). (C.11)
```

For `d>=3`, all extreme keys are connected.  If `e={x,y}` and `z` is outside
`e`, the intermediate key with `p=(x,z)`, one left block, and right block
`{x,y,z}` (all remaining right blocks singleton) has leaf-splitting edges to
both `kappa_{x,y}` and `kappa_{y,z}`.  The graph of two-subsets under one-label
replacement is connected.  At `d=2` there is only the singleton key.

This proof uses an extreme family only to establish reachability.  It is not
a canonical-path congestion argument and supplies no quantitative gap.

## 6. Exact finite falsification audit

`projection_audit.py` independently enumerates `d<=4`.  Current completed
facts before the adjacent-chain rerun are:

| `d` | keys | components of `G_d` | `gap(G_d)` | `beta(d)` |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 9 | 1 | 0.0896143806 | 0.1461033961 |
| 4 | 101 | 1 | 0.0980244430 | 0.1288510552 |

All stationary-flow and reversibility residuals are at floating summation
scale.  These are exact enumerations followed by numerical diagonalization;
they only falsify reducibility and normalization errors at these sizes.

## 7. First standalone open lemma

> **LOCAL UNICYCLE INCIDENCE GAP.**  For the connected adjacent-cut key chain
> `A_d` defined by (C.6)--(C.8) on decorated connected-unicyclic incidence
> keys, prove `gap(A_d)>=d^{-O(1)}` for every `d>=3`.

By (C.9), this implies `beta(d)>=d^{-O(1)}`.  The next work will audit local
count ratios and try a non-hub comparison on leaf split/merge moves.  A proof
must control stationary mass and congestion; polynomial diameter and the
finite spectra are insufficient.
