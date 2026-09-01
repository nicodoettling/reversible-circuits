# M27 halfway checkpoint

Date: 2026-08-11. Status: nonterminal proof progress.

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are read
left-to-right.  Write `d(h)=N-#cycles(h)` and

```text
g = l-d(h)/2.
```

Thus a raw length-`2l` factorization of `h` has exactly `g` split steps and
`2l-g` join steps when followed from the identity.

## 1. A rigorous bounded-surplus additive-mode bound

Let `I_i=1{p(X_i)=e}` and `S=sum_i I_i` under the uniform microbridge
`Omega_l(h)`.  Deleting every square microcoordinate deletes two equal
adjacent transpositions without changing the endpoint.  The remaining word
has length `2(l-S)`, so reflection length gives

```text
S <= g                                                   (1.1)
```

pointwise.  Centrality of the two-transposition increment law makes the
`I_i` exchangeable.  Put `p=E I_1` and, when `0<p<1`, let `rho` be the
correlation of `I_1,I_2`.  Since `S^2<=gS`,

```text
Var(S) <= E[S](g-E[S]),
rho <= [(g-1)-(l-1)p]/[(l-1)(1-p)] <= (g-1)/(l-1).     (1.2)
```

The square event is invariant under endpoint conjugation, so this is a real
scalar block in the exact M16 Gram decomposition.  Its largest additive
Gram eigenvalue is therefore at most

```text
max{g/l, 1/(l-1)}.                                     (1.3)
```

If `p=0` the mode is absent; variation inside the identity-product lift fiber
is a microfiber mode with exact eigenvalue `1/l`.  Hence every bounded-`g`
square mode is `O(1/l)`.  This does not control arbitrary product-class or
label-incidence modes.

## 2. Minimal long-cycle sector: two exact ideal chains

Let the endpoint be a long cycle on `n` labels, let `r=n-1=2l`, and consider
its reduced transposition factorizations.  These are maximal chains of
`NC_n`.  Stanley's edge-label map is a bijection from these chains to parking
functions of length `r`; Pollak's observation identifies those parking
functions with

```text
Z_n^r / <(1,...,1)>.
```

On this quotient, choose one coordinate uniformly and resample it uniformly
in `Z_n`.  This is well-defined independently of the representative.  Gauge
the last coordinate to zero.  The first `r-1` update choices are ordinary
independent coordinate heat baths on `Z_n^(r-1)`; the last choice is a common
uniform translation.  Discarding the latter nonnegative Dirichlet form gives

```text
gap(D_quot) >= 1/r.                                    (2.1)
```

Thus an ideal polynomial-gap chain exists with exact uniform stationary law
and `O(r log r)` direct sampling cost.  The unresolved step is its local-flow
comparison to rank/Hurwitz or aligned-H4 moves.

There is nevertheless a proved restricted comparison.  Let

```text
L_n = (r-1)^(-1) sum_(i=1)^(r-1) G_i,
```

where `G_i` is the exact same-product heat bath on raw transpositions
`i,i+1`.  A rank-two interval in `NC_n` has two or three middle elements.
Under Stanley's parking labels, the adjacent-coordinate transposition swaps
the two states in a two-element interval; in a three-element interval it
fixes the special state and swaps the other two.  Consequently, on every
fixed parking-entry multiset `beta`, the rejected-exit restriction obeys

```text
E_(L_n^beta) >= (2/3) E_(S_adj^beta),
gap(L_n^beta)
 >= (2/3)[1-cos(pi/r)]/(r-1).                          (2.2)
```

Here `S_adj=I/2+[2(r-1)]^(-1)sum_i sigma_i`, and its multiset quotient has
gap at least the path-interchange gap displayed in (2.2).  A nontrivial
`L_n` edge changes two raw factors.  It is an outcome of an aligned H4
window after fixing the other two padding factors.  The H4 fiber has size at
most `M^4`, and the exact scan rates imply, conservatively,

```text
E_(B_l^beta) >= M^(-4) E_(L_n^beta),
gap(B_l^beta)
 >= [2/(3M^4)] [1-cos(pi/r)]/(r-1)
 >= 4/[3M^4 r^2(r-1)].                                (2.3)
```

This proves polynomial mixing inside every parking-multiset orbit, including
rare multisets.  It does not mix the orbits.

The exact stationary mass of a sorted parking multiset with multiplicities
`m_1,...,m_r` is

```text
bar_pi(beta)=r!/[n^(n-2) product_a m_a!].              (2.4)
```

The remaining minimal-cycle implication is therefore the stationary-flow
projection on these multisets (or an equivalent polynomial-congestion flow
from `D_quot`).  The accepted JSTV projection/restriction theorem would then
combine that projection gap with (2.2), with at most a universal-factor loss
after half-lazification.

## 3. Why the immediate spanning-tree transfers fail

### 3.1 The raw factorization graph is not strongly Rayleigh

Exact exhaustive enumeration for the even endpoint `(1 2 3 4 5)` gives 125
reduced factorizations but only 55 raw edge sets, of weights 1 through 5.
For raw edges `e={0,1}` and `f={2,4}`,

```text
P(e,f present)=24/125,
P(e present)P(f present)=(64/125)(36/125),
24*125-64*36=696>0.                                   (3.1)
```

Thus the raw tree projection is not even pairwise negatively correlated and
cannot be strongly Rayleigh.  This is model-compatible and extends to an
infinite family: take the disjoint endpoint consisting of this 5-cycle and
`l-2` disjoint 3-cycles.  Its defect is `2l`; minimal factorizations are
constant-count interleavings of independent component factorizations, so the
5-cycle marginal and (3.1) persist for every `l>=2`.

### 3.2 Stanley's uniform-tree bijection is asymptotically nonlocal

For every `n>=4`, define two reduced words for the long cycle:

```text
w_n=((0,1),(1,2),(2,n-1),(2,n-2),...,(2,3)),
v_n=((0,2),(0,1),(2,n-1),(2,n-2),...,(2,3)).           (3.2)
```

The first two products agree, so the words differ by one rank/Hurwitz move.
Directly applying Stanley's tree construction gives

```text
T(w_n)={(0,1),(1,2)} union {(2,j):3<=j<n},
T(v_n)={(0,1),(0,2)} union {(1,j):3<=j<n}.             (3.3)
```

Their edge-set symmetric difference is `2(n-2)`.  With the standard
smallest-leaf Pruefer convention their codes are

```text
(1,2,2,...,2)  and  (0,1,1,...,1),                    (3.4)
```

at Hamming distance `n-2`.  Hence neither a local rank move nor an adjacent
Hurwitz move is a one-edge basis exchange or one-coordinate Pruefer move
under this genuine uniform-tree bijection.  The finite scripts verify the
construction and bijectivity at `n=4,5`; equations (3.2)--(3.4) are the
universal proof.  This refutes direct one-step domination, not the possibility
of a randomized polynomial-congestion simulation in the reverse direction.

## 4. Exact current frontier

The uniform claim `mu_l^*<=A/l` remains neither proved nor refuted.  The
square sector satisfies it at bounded surplus, but the maximal correlation
can lie in another product-level direction.

The smallest new minimal-sector proposition is:

> **PARKING-MULTISET PROJECTION.**  The stationary-flow projection of the
> half-lazy rank-two heat-bath `L_n` onto coordinate-permutation orbits of
> parking functions has gap at least `n^{-C}` for a universal `C`.

Equivalently, it suffices to route the quotient-coordinate refresh chain
`D_quot` through rank-two heat-bath edges with polynomial path length and
congestion.  The orbit restrictions are already polynomial by (2.2).  A
fixed tree-exchange or Pruefer-refresh transition has preimages at polynomial
Hurwitz diameter, but diameter alone gives no recoverable-flow congestion;
the global relabeling in (3.3) is the precise obstacle to a one-step transfer.

This proposition would close the minimal long-cycle stratum, not yet every
surplus and arbitrary endpoint in the base-scale theorem.

## Sources and computation

- Richard P. Stanley, *Parking Functions and Noncrossing Partitions*, EJC
  4(2) (1997), Theorem 3.1, Proposition 4.1, and the paragraph after
  Proposition 3.2:
  https://www.combinatorics.org/ojs/index.php/eljc/article/download/v4i2r20/pdf
- Nima Anari, Shayan Oveis Gharan, and Alireza Rezaei, *Monte Carlo Markov
  Chain Algorithms for Sampling Strongly Rayleigh Distributions and
  Determinantal Point Processes*, Theorems 1.1, 2.3, 2.4:
  https://arxiv.org/abs/1602.05242
- Yuval H. Khachatryan-Raziel, *On the center of the Hurwitz graph*,
  Theorem 2.3.3 and Observations 5.1.4--5.1.5:
  https://arxiv.org/abs/1508.02620

Exact commands are recorded for the final report.  All scripts are
deterministic with null seed and test named universal transfer claims only.
