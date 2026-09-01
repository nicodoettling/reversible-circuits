# Halfway checkpoint: a uniform all-genus square ratio

## Conventions and scope

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Put `M=binom(N,2)`.  The chain is the exact lazy random-scan
same-product heat bath with `R_m={3,4,5}` in the regime below (`m>=6`), so a
specified `H_3` output from a specified window has probability

```text
1/[2 |R_m| (m-2) D_N],
D_N=(3N^2+N-12)/2 <= 4M.
```

This checkpoint proves a uniform adjacent-genus estimate that was missing
from the sparse analysis.  It reduces every component-count threshold for
`m>2(N-1)` to one exact enumerative proposition, component-layer
unimodality.  Unimodality is not asserted here.

## 1. A convolution-ratio lemma

Let `a=(a_j)_{j>=0}` and `b=(b_j)_{j>=0}` be nonnegative sequences.  If

```text
a_j <= R_a a_{j-1},   b_j <= R_b b_{j-1}    (j>=1),
```

then their convolution `c_n=sum_{j=0}^n a_j b_{n-j}` satisfies

```text
c_n <= (R_a+R_b)c_{n-1}.                                (1.1)
```

Indeed, bound the summands with `j>=1` by lowering `j` in `a`, and bound the
single `j=0` summand by lowering its index in `b`.  Iteration gives the sum
of the ratio constants for any finite convolution.  Zeros cause no problem.

## 2. Universal connected Hurwitz ratio

For a fixed labeled `d`-set, let `C_g(d)` be the number of connected identity
transposition words of length

```text
k=2(d-1)+2g,
```

and put `a_{g,d}=C_g(d)/k!`.  Then, for every `d>=2,g>=1`,

```text
a_{g,d}/a_{g-1,d} <= d^3/12.                            (2.1)
```

The cited input is Dubrovin--Yang--Zagier, *Classical Hurwitz numbers and
related combinatorics*, Proposition 1, equation (13):
<https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
Their `h_{g,d}` is the cover count divided by `k!`; multiplying by `d!`
turns it into the fixed-labeled-sheet factorization count `a_{g,d}`.  This
factor is independent of `g`, so their positive recurrence applies without
changing any ratio.  The normalization is independently checked by
`C_0(2)=1,C_0(3)=24,C_0(4)=2880`.

Here is the full deduction.  In DYZ equation (13), set `ell=j+1`.  For each
ordered split `d_1+d_2=d`, its contribution to `a_{g,d}` is, up to a positive
constant independent of `g`, the coefficient of `x^g` in

```text
A_{d_1}(x) A_{d_2}(x) B_{d_1,d_2}(x),
A_q(x)=sum_{h>=0} a_{h,q}x^h,
B_{d_1,d_2}(x)=sum_{j>=0}
 d_1^(2j+3)d_2^2 x^j/(2j+2)!.
```

The last sequence has consecutive ratio

```text
B_{j}/B_{j-1}=d_1^2/[(2j+2)(2j+1)] <= d_1^2/12
```

for `j>=1`.  (Equivalently, with indices starting at `ell=1`, the first
ratio is `d_1^2/(4*3)`.)  Define `R_1=0`, since degree one has only its
genus-zero term.  Inductively in `d`, (1.1) says that every ordered-split
contribution has ratio at most

```text
R_{d_1}+R_{d_2}+d_1^2/12.
```

If `R_q<=q^3/12` for `q<d`, then

```text
d_1^3+d_2^3+d_1^2 <= (d_1+d_2)^3=d^3,
```

because the omitted cross term is `3d_1d_2d>=d_1^2`.  The sum over ordered
splits obeys the same common ratio bound.  This proves (2.1).

## 3. Every exact macro partition has polynomial square mass

Fix an exact support partition `P`, including isolates, and let its
nontrivial block sizes be `v_1,...,v_b`.  If `E_P(m)` is its number of exact
identity words, then

```text
E_P(m)/m!
 = [z^G] product_i A_{v_i}(z),
G=m/2-N+|P|.                                             (3.1)
```

This is exactly the inherited independent-component/color-interleaving
factorization; isolates contribute no factors.  Applying (1.1) and (2.1),

```text
[z^G]product_i A_{v_i}
 <= (sum_i v_i^3/12)[z^(G-1)]product_i A_{v_i}
 <= (N^3/12)[z^(G-1)]product_i A_{v_i}.                  (3.2)
```

Consequently, whenever `G>=1`,

```text
E_P(m)/E_P(m-2) <= m(m-1)N^3/12.                        (3.3)
```

At a fixed adjacent position, inserting `tt` into a shorter exact-`P` word
is injective jointly in that word and the internal transposition `t`:
deleting the designated pair recovers both.  Therefore (3.3) is also the
uniform fixed-position deletion-preserving square estimate that fixed-genus
formulas could not supply.

## 4. Exact boundary flow and conditional threshold theorem

Let `W_c(N,m)=sum_{|P|=c}E_P(m)`.  Assume `N>=3` and even
`m>2(N-1)`, equivalently `m>=2N`.  All layers `1<=c<=N-1` are feasible.
For a threshold `c_0 in {1,...,N-2}`, put `c_*=c_0+1`.

For every exact partition `P` with `c_*` components let

```text
e(P)=sum_{B in P} binom(|B|,2),   x(P)=M-e(P).
```

Since a length-`m-2` word exists, `e(P)>=1`; since `c_*>=2`,
`x(P)>=N-1`.  For each shorter exact-`P` word, choose an internal `t` and a
cross-component `s`, insert `tt` in positions one and two, and use the actual
first `H_3` window to replace `(t,t,c)` by `(s,s,c)`.  The source remains in
layer `c_*` after deletion of the designated square; the target merges
exactly two components and lies in layer `c_0`.  Every tuple is recovered by
deletion and by its first two factors.  Hence the full stationary boundary
flow satisfies

```text
Q_K({c<=c_0},{c>=c_*})
 >= [1/Z_m] [1/(2|R_m|(m-2)D_N)]
      sum_{|P|=c_*} E_P(m-2)e(P)x(P).                    (4.1)
```

There is no unrecorded block, window, laziness, fiber, insertion, or
multiplicity factor in (4.1).  By (3.3), `|R_m|=3`, and `D_N<=4M`, the
average downward rate from the entire boundary layer is

```text
Q_K({c=c_*},{c=c_0})/pi({c=c_*})
 >= 1/[N^4 m(m-1)(m-2)].                                (4.2)
```

Now suppose only that `(W_1,...,W_{N-1})` is unimodal.  If a mode is at or
below `c_0`, then `W_{c_*}` is the largest term of the upper tail.  If a mode
is at or above `c_*`, then every term of the lower tail is at most
`W_{c_*}`.  In either orientation,

```text
W_{c_*} >= min{sum_{c<=c_0}W_c, sum_{c>=c_*}W_c}/N.      (4.3)
```

Combining (4.2)--(4.3) proves the conditional, two-sided statement

```text
Phi_pm({c<=c_0}) >= 1/[N^5 m(m-1)(m-2)].                (4.4)
```

This covers the entire intermediate window and the prior dense window, with
an exponent independent of surplus, conditional on one named proposition:

> **COMPONENT-LAYER UNIMODALITY.** For every `N>=3` and even `m>=4`, the
> positive sequence `W_c(N,m)` on its feasible component-count interval is
> unimodal.

The proposition is exact and finite for each pair, but remains unproved
uniformly.  Standard total-positivity shortcuts are not currently available:
the companion audit exhibits a negative coefficient in a natural `2x2`
exponential-Riordan minor.

## 5. Finite falsification status

The deterministic exact harness found no failure of (2.1) through
`d<=20,k<=160`; the largest observed fraction of the proved bound was
`0.15234375`, at `(d,k)=(4,8)`.  Separate exact arithmetic found no
component-layer log-concavity failure through `N<=22,m<=220`, and exact
Sturm checks found real negative roots in selected largest cases.  These
finite results test normalization and could falsify the named propositions;
they are not their proofs.

Reproduction commands appear in `report.md`.
