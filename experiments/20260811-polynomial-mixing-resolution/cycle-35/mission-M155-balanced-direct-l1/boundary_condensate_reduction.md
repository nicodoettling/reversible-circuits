# Boundary-condensate reduction for balanced direct L1

Date: 2026-08-13.

Status: Propositions 1--3 and Corollary 4 below are **proved** from the
accepted M73/M91/M94 colored-composition and posterior identities.  The
score-growth alternative `(BCL)` is **unresolved**.  In particular, this note
does not prove or refute the balanced direct-L1 estimate.

## 1. Scope, convention, and exact score

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
Let `n=3k`, with odd `k>=3`, let `h=(0 1 ... n-1)`, and retain the uniform
minimal length-`n-1` factorization law of `h` and M73's nonlazy cyclic
rank-two quotient kernel `bar K`.  Put

```text
A_k=(0,k,2k),                B_k=(0,1)(k,2k).
```

For a quotient target orbit `O`, define the complete signed two-step score

```text
z_k(O)=[bar K^2(O_B,O)-bar K^2(O_A,O)]/bar pi(O).     (1.1)
```

M94's accepted exact convolution is

```text
z_k(O_t)=1/[c_n R_n^2 beta_3(t)]
 sum_(s in X_n) a(s)d_k(s)Q_t(s)/beta_3(s),           (1.2)
```

where `d_k` is the complete `B-A` first-row contrast, already combining both
M91 channels, and `Q_t` averages the complete second row over the literal
target orbit.  Thus every score below contains all intermediate triangle and
double strata before the absolute value is taken.  In particular, the
reduction below does not use the invalid generic-bulk replacement identified
by M102/M105.

The exact direct-L1 identity is

```text
2 TV(bar K^2(O_A,.),bar K^2(O_B,.))
   =E_barpi |z_k|.                                    (1.3)
```

## 2. Exact separated-color disintegration

Write

```text
tau(r)=r^(r-1)/r!,       b_r=e^(-r)tau(r),
Gamma_n=n(n-3)!e^n/n^(n-2).
```

The accepted double-orbit parameterization says that every double orbit has
exactly four colored positive-composition encodings, two separated and two
nested.  A separated encoding with positive gaps `(x,y,z,w)` has residual
cycle sizes `(x,z,y+w)`.  Every odd-`n` double orbit has size `n`, and its
stationary mass is

```text
2 n(n-3)! tau(x)tau(z)tau(y+w)/n^(n-2).               (2.1)
```

Fix `a,b>=1`, put `c=n-a-b`, and suppose `c>=2`.  Let

```text
C^S_(n;a,b)={(a,y,b,c-y;S): 1<=y<=c-1}.              (2.2)
```

This is a set of colored encodings, not a claim that its members are
distinct quotient orbits.  Give every encoding one quarter of its orbit's
mass.  Define

```text
W_n(a,b)=sum_(e in C^S_(n;a,b)) bar pi(O_e)/4,

A_k(a,b)=1/(c-1) sum_(y=1)^(c-1)
                k^2 |z_k(O_(a,y,b,c-y;S))|.           (2.3)
```

### Proposition 1 (proved: exact boundary-cell weight)

For every admissible `n,a,b`,

```text
W_n(a,b)=(c-1) Gamma_n b_a b_b b_c/2.                (2.4)
```

Moreover, writing `D` for double targets and `T` for triangle targets,

```text
k^2 E_barpi[|z_k| 1_D]
       =2 sum_(a,b>=1; a+b<=n-2) W_n(a,b)A_k(a,b),   (2.5)

2k^2 TV
       =k^2 E_barpi[|z_k|1_T]
        +2 sum_(a,b)W_n(a,b)A_k(a,b).                 (2.6)
```

#### Proof

Equation `(2.1)` divided by four is the mass assigned to one colored
encoding.  It is independent of `y` on `(2.2)`.  Summing its `c-1` values
and replacing every `tau(r)` by `e^r b_r` proves `(2.4)`.

Every double orbit occurs in exactly two separated encodings.  Therefore
the quarter-weighted sum of any nonnegative orbit function over all
separated encodings is exactly one half of its stationary expectation on
double orbits.  Apply this to `|z_k|`, partition the separated encodings by
`(a,b)=(x,z)`, and use `(2.3)--(2.4)` to obtain `(2.5)`.  Add the triangle
part of `(1.3)` to obtain `(2.6)`.  No sign or triangle inequality is used
inside the score.  QED.

### Proposition 2 (proved: product-Borel boundary condensation)

For each fixed `a,b>=1`, along odd `n=3k -> infinity`,

```text
W_n(a,b) -> (1/2)b_a b_b.                            (2.7)
```

For every odd `n>=5`, the total separated quarter-mass is exactly

```text
sum_(a,b)W_n(a,b)=(n-3)/(2n),                        (2.8)
```

so the limiting mass is `1/2`.  More precisely, the probability measure
obtained by dividing `W_n` by `(n-3)/(2n)` converges in total variation on
`N^2` to the law of two independent critical-Borel variables.

#### Proof

Stirling gives

```text
Gamma_n~sqrt(2 pi n),        b_(n-a-b)~(2 pi)^(-1/2)n^-3/2.
```

Since `c-1~n`, equation `(2.4)` proves `(2.7)`.  Equation `(2.8)` follows
without asymptotics: separated encodings contribute two of the four
encodings of every double orbit, and the accepted total double mass is
`(n-3)/n`.  Finally `sum_(r>=1)b_r=1`; hence the pointwise limiting masses in
`(2.7)` sum to the limiting total `1/2`.  Pointwise convergence of
nonnegative masses together with convergence of total masses (the discrete
Scheffe lemma) proves total-variation convergence after normalization.  QED.

## 3. The logarithmic summability threshold

For `D>=1`, put

```text
H_D=sum_(1<=a,b<=D)b_a b_b min(a,b).                 (3.1)
```

### Proposition 3 (proved: critical harmonic divergence)

One has

```text
H_D=(2/pi)log D+O(1).                                (3.2)
```

In particular `H_D -> infinity`.

#### Proof

The layer-cake identity gives

```text
H_D=sum_(r=1)^D [sum_(j=r)^D b_j]^2.                 (3.3)
```

Stirling with remainder gives

```text
b_j=(2 pi)^(-1/2)j^-3/2+O(j^-5/2).
```

Uniform summation for `1<=r<=D` yields

```text
sum_(j=r)^D b_j
 =sqrt(2/pi)(r^-1/2-D^-1/2)+O(r^-3/2+D^-3/2).
```

Squaring and summing, the `r^-1` term contributes `(2/pi)log D`; the
cross term and `D^-1` term have bounded sums, as do all remainder terms.
This proves `(3.2)`.  QED.

### Corollary 4 (proved conditional implication: linear-min growth refutes L1)

Suppose there is a constant `lambda>0` such that, for every fixed pair
`a,b>=1`, along the subsequence of odd integers `k>=3` (for which the cell is
automatically admissible once `3k>=a+b+2`),

```text
liminf_(k odd -> infinity) A_k(a,b)
     >=lambda min(a,b).                              (BLM)
```

Then

```text
liminf_(k odd -> infinity)
 k^2 TV(bar K^2(O_A,.),bar K^2(O_B,.))=infinity,    (3.4)
```

so the proposed direct `O(k^-2)` estimate is false.

#### Proof

Fix `D`.  Once `3k>=2D+2`, retain only the nonnegative terms
`1<=a,b<=D` in `(2.6)`.  Proposition 2 and the elementary finite-sum
liminf inequality give

```text
liminf_(k odd) 2k^2 TV
 >=sum_(a,b<=D)b_a b_b liminf_(k odd) A_k(a,b)
 >=lambda H_D.                                       (3.5)
```

Let `D` tend to infinity and use Proposition 3.  QED.

The same proof only needs `(BLM)` on any set of fixed pairs for which the
weighted series diverges.

A quantitative strengthening exposes the natural logarithmic alternative.
If there are `lambda>0` and `0<theta<1` such that, for all sufficiently
large odd `k` and all `1<=a,b<=floor(k^theta)`,

```text
A_k(a,b)>=lambda min(a,b),                           (UBL)
```

then

```text
TV(bar K^2(O_A,.),bar K^2(O_B,.))
       >=c_(lambda,theta) log(k)/k^2.                (3.6)
```

Indeed `a+b=o(n)` uniformly on this square, so `(c-1)Gamma_n b_c` is bounded
below by an absolute positive constant for all large `k`.  Equations
`(2.4),(2.6)` then dominate a constant times `H_floor(k^theta)`, and
Proposition 3 gives `(3.6)`.  This conditional lower bound would refute the
assigned constant-`O(k^-2)` lemma, but not a logarithmic upper bound.

There is also an exact positive counterpart.  By `(2.6)`, the direct
`O(k^-2)` estimate is equivalent to the joint pair of bounds

```text
sup_(k odd>=3) k^2 E_barpi[|z_k|1_T] < infinity,
sup_(k odd>=3) sum_(a,b)W_(3k)(a,b)A_k(a,b)<infinity. (3.7)
```

Thus any proof must prevent the boundary-condensate mechanism.  A convenient
but stronger route on every fixed-cell region is a nonnegative envelope
`J(a,b)` with

```text
limsup_k A_k(a,b)<=J(a,b),
sum_(a,b)b_a b_b J(a,b)<infinity,                    (3.8)
```

together with uniform integrability for the actual finite-`n` weights
`W_(3k)` and the triangle bound in `(3.7)`.  The summable limiting envelope
alone is not sufficient: when `c=n-a-b` is small, `W_n/(b_ab_b)` need not be
uniformly bounded.  Condition `(3.8)` is therefore not claimed necessary or
sufficient without the stated tail control, whereas `(3.7)` is exact and
`(BLM)` is a complete rigorous refutation route.

The explicitly weaker standalone target is

```text
k^2 E_barpi[|z_k|1_T]
 +2 sum_(a,b)W_(3k)(a,b)A_k(a,b) <=C log(2+k).       (BCL-log)
```

By `(2.6)`, `(BCL-log)` is exactly the balanced-family upper bound
`TV=O(log k/k^2)`.  Even if `(UBL)` made the sharp constant bound false, this
weaker scale could survive.  If an analogue of `(BCL-log)` held uniformly on
every strict endpoint-sharing edge, M80's diameter-at-most-four routing would
give `delta(bar K^2)=O(log n/n^2)`.  Self-adjointness would then give every
nonconstant eigenvalue `|kappa|=O(sqrt(log n)/n)`, retaining polynomial decay
in M73's H0 coordinate-Gram step.  This is a conditional consequence of a
*uniform all-edge* logarithmic theorem, not a conclusion from the balanced
family alone and not a full bridge or identity-chain gap theorem.

## 4. Exact remaining lemma and relation to earlier obstructions

> **BOUNDARY-CELL SCORE DICHOTOMY `(BCL)` (unresolved).**  Evaluate the
> exact, channel-combined score `(1.2)` on the separated cells `(2.2)`.
> Either prove the exact boundedness in `(3.7)`, for example through a
> uniformly integrable envelope of the form `(3.8)`, prove the weaker
> `(BCL-log)`, or prove `(BLM)`/`(UBL)` on a weighted-divergent family of
> pairs.

This is strictly more structured than the original target: `(a,b)` have an
exact product-Borel limiting law, the nuisance split `y` is averaged only
after the full signed posterior convolution, and the exact positive decision
threshold is `(3.7)`.  It also explains a possible logarithmic loss:
critical Borel variables satisfy `E[min(B_1,B_2)]=infinity` exactly at the
harmonic boundary.

M102/M105 do not decide `(BCL)`.  Their nonintegrable collision face lies
inside the intermediate sum defining each `z_k`; it is therefore retained,
along with every exact small-component and lower-support term, before the
absolute value and `y` average in `(2.3)`.  No claim is made that triangles
are the complete matching counterterm.

## 5. Scope and strongest self-attack

- **Proved:** exact separated-cell disintegration, product-Borel boundary
  condensation, harmonic divergence, and the implication `(BLM)` => failure
  of direct `O(k^-2)`.
- **Exact finite validation:** the colored-cell weight and its total-mass
  identity were checked over `Fraction` for `k=3,5,7,9`.
- **Finite evidence only:** retained M94 shell profiles at `k=7,9` have an
  approximately harmonic `k^2` absolute-mass profile.  They neither prove
  `(BLM)` nor establish a score limit.
- **Unresolved:** `(BCL)`, `(BLM)`, direct L1, `(BD)`, `(BA2)`, the general
  strict-edge estimate, H0, every bridge/identity-chain gap, and both
  Terminals.

The strongest self-attack is that `A_k(a,b)` is an absolute average of a
fully signed convolution; its limiting growth is precisely the hard part.
The product-Borel law alone gives no lower bound on that score.  In
particular, the minimal cells such as `(a,b)=(1,1)` could have bounded or
vanishing `A_k`, and the retained minimum-residual shell data aggregate many
colors and cells and therefore do not test `(BLM)`.  Opposite signs in the
intermediate collision and lower-support strata are already combined inside
`z_k` and may cancel at every fixed cell.  Thus this is a strict decision
reduction and a genuine counter-obstruction to linear-min score control, not
a refutation of the chain estimate.

Boundary cases: `k=1`, even `k`, other odd `n`, identity endpoints, `m=0,2`,
and `N=2` are outside this balanced minimal-long-cycle statement.
