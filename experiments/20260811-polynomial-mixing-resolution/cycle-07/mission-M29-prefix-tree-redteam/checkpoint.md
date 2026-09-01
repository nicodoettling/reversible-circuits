# M29 halfway checkpoint: exact locality, and two failed shortcuts

This is a genuine halfway checkpoint.  It freezes the deterministic full-`K`
locality calculation and two exact counterexamples before the final cut
audit.  No Terminal-B claim is made.

## 1. Full-window prefix locality (proved)

Use `(pq)(x)=p(q(x))`.  Suppose a length-`r` block
`a_1...a_r` is replaced by `b_1...b_r` with the same ordered product.  At
the `k`-th internal prefix, `1<=k<=r-1`, the two block prefixes are each
products of `k` transpositions, while equality of total products also writes
their relative permutation as a product of `2(r-k)` transpositions.  For the
transposition Cayley metric,

```text
d(a_1...a_k,b_1...b_k)<=2 min(k,r-k).                  (1.1)
```

The height `h_j=N-cycles(X_j)` is distance from the identity in this metric.
All prefixes before the block and from the block endpoint onward agree, so

```text
|Delta h_(i+k-1)|<=2 min(k,r-k),
|Delta area|<=sum_(k=1)^(r-1)2 min(k,r-k).
```

For `r=3,4,5`, the exact displayed area bounds are respectively

```text
4, 8, 12.                                               (1.2)
```

Thus every full-`K` update changes Dyck area by at most `12` and maximum or
fixed-time height by at most `4`.  At most the `r` join/cut steps inside the
window can change.  Therefore peak count changes by at most `r+1`, the join
tree changes in at most `r` deleted and `r` added edges, leaf count changes
by at most `4r`, and maximum join-tree degree changes by at most `r`.

For an area threshold

```text
A_q={w in F_N: Area(w)<=q},
S_q={w in F_N:q-11<=Area(w)<=q},
```

every boundary transition either starts in `S_q` or leaves the full-support
macro `F_N`.  Consequently the exact full-chain flow obeys the useful but
one-sided reduction

```text
Q_K(A_q,A_q^c)
 <=pi(S_q)+sum_(w in A_q)pi(w)K(w,F_N^c).              (1.3)
```

For a Terminal-B proof, both terms in (1.3) must be superpolynomial relative
to the correctly oriented mass.  For an anti-bottleneck theorem, one needs a
lower shell/action estimate; locality alone gives neither.

## 2. Exact N=5 refutation of the naïve area-unimodality route

The deterministic Hurwitz-orbit enumeration checks the exact cardinality

```text
|F_5|=8!*5^2=1,008,000.
```

On the feasible parity lattice, the area layers at areas
`4,6,8,10,12,14,16` have exact counts

```text
3000, 23400, 60600, 132840, 207600, 205560, 375000.    (2.1)
```

Thus they are neither unimodal nor log-concave: after the strict drop from
area 12 to 14, the mountain layer at 16 rises to 375000.  This is an exact
finite counterexample to using universal area-layer unimodality as the shell
theorem.  It is not evidence of asymptotic slow mixing.  Peak, maximum-height,
midpoint-height, join-tree-leaf, and maximum-degree layers remain unimodal and
log-concave through this one finite case only.

The earlier `N=4` result is recovered exactly.  Structural parity zeros are
removed before testing log-concavity, avoiding a false counterexample.

## 3. Exact N=6 refutation of pointwise macro escape

A second tempting shortcut was to lower-bound every subset of `F_N` through
a pointwise one-step escape from full support.  Exact enumeration gives
positive macro exit for every state at `N=3,4`; the complete `N=5` orbit also
has, for every state, a vertex cut whose crossing factors lie in some interval
of length at most five.  That pattern stops at `N=6`.

Starting from a paired spanning-tree word and applying exact project Hurwitz
bijections with fixed seed `290731` produces after 45 moves the word

```text
(01),(24),(03),(02),(35),(15),(34),(23),(04),(05).     (3.1)
```

The harness independently verifies that (3.1) has ordered product identity
and connected support.  More strongly, deleting **any** five consecutive
factors leaves a connected support graph.  Every legal `r<=5` window is
contained in such a length-five interval.  Factors outside an updated window
are unchanged and already connect all six labels, so every possible exact
same-product block outcome remains full-support connected.  Hence

```text
K_(6,10)(w,F_6^c)=0.                                   (3.2)
```

This is a rigorous bounded counterexample to universal pointwise macro
escape, not to irreducibility and not to polynomial mixing.  It also shows
why the inherited averaged removable-square certificate cannot control an
arbitrary area/tree subset by itself.

## 4. Resource audit

Duchi--Poulalhon--Schaeffer, Proposition 1 and Theorem 4, biject minimal
transitive identity factorizations with indexed increasing quadrangulations
and then Hurwitz trees.  Their Proposition 3 is an `N`-to-one correspondence
between `(Cayley tree, permutation)` pairs and Hurwitz trees, yielding a
perfect uniform sampler and the count `(2N-2)!N^(N-3)`.  The paper gives no
statement identifying the prefix Dyck path with a uniform Catalan path, no
join-tree marginal, and no local heat-bath/flip intertwining.  Exact `N=4`
counts already show the project join tree is not uniform.

Féray--Louf--Thévenin's fixed-genus scaling theorem concerns factorizations
of a long cycle, not minimal transitive factorizations of the identity, so it
does not supply the missing shell law here.

## 5. Exact remaining implication

> **WEIGHTED MINIMAL-EXCURSION SHELL/ACTION.**  There are universal
> `c>0,C<infinity` such that for every sufficiently large `N`, every
> conditional median threshold chosen from Dyck area, midpoint height,
> maximum height, peak count, or join-tree leaf count has full-`K` boundary
> at least `cN^{-C}` times its smaller global stationary side.

Even the area-only case is open.  A proof must jointly control the weighted
shell and the internal action plus macro exits; ordinary Catalan or uniform
Cayley-tree estimates cannot be substituted.

## 6. Artifacts and exact commands so far

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/exact_peak_tree_layers.py \
  --N 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/layers_N5.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/random_cut_span_search.py \
  --N 6 --steps 200000 --seed 290731 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/cut_span_N6_seed290731.json
```

Python is 3.12.3; the orbit enumeration is deterministic with no stochastic
seed, while the witness search records fixed seeds.  A reported witness is
exact; only nonfinding is empirical.

