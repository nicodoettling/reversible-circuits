# Independent referee report: M10 constant-loss two-block bridge recursion

## 1. Exact frozen claim and conventions

Use `(pq)(x)=p(q(x))`.  Let `P_N` be the uniform law on the
`M=binom(N,2)` transpositions and `Q_N=P_N^2` on `A_N`.  A length-`n`
microfactorized `Q_N` bridge is a length-`2n` transposition word grouped into
ordered pairs, with every pair label retained.  Let

```text
H_n=sum_(j=1)^(n-1)(I-H_j),
B=(1/(n-1))sum_(j=1)^(n-1)H_j,
```

where `H_j` is the exact aligned four-transposition heat bath.  Let
`Lambda_N(l;u,v)` be the Hamiltonian Poincare constant of a feasible
length-`l` bridge from `u` to `v`, and `Lambda_N(l)` its minimum over feasible
endpoints.

The frozen theorem asserts that some integer
`s_*(N)<=C_*N log(N+1)` gives, with `b=s_*+1`, for every `N>=3` and
`n>=b+2`, a shorter integer `L` such that

```text
L-b <=(n-b)/2,
Lambda_N(n)>=Lambda_N(L)/3.                            (1)
```

Consequently, for `a=log_2 3`,

```text
Lambda_N(n;e,e)
 >=(1/3)(n-b)^(-a) min_(2<=l<=b+1) Lambda_N(l),         (2)
gap(B)=Lambda_N(n;e,e)/(n-1),                          (3)
gap(K_(N,2n))>=gap(B)/12.                              (4)
```

The theorem is a nonterminal reduction: the base constants through
`O(N log N)` remain quantitatively open.

## 2. Full audit

### 2.1 Microfactorized bridge law

For a paired increment `y`, the number `a_N(y)` of ordered transposition
factorizations is

```text
a_N(e)=M,
a_N(y)=3  for a specified 3-cycle,
a_N(y)=2  for a specified double transposition.
```

Thus `Q_N(y)=a_N(y)/M^2`.  Marginalizing a uniform transposition-word bridge
over its pair products produces density proportional to the product of the
`Q_N` increments; conditional on those increments, the ordered pair labels
are independent and uniform.  No labels are collapsed in the later
conditional expectations.

### 2.2 Diaconis--Shahshahani parity and pointwise translation

The primary source is P. Diaconis and M. Shahshahani, "Generating a Random
Permutation with Random Transpositions," *Z. Wahrscheinlichkeitstheorie
verw. Gebiete* **57** (1981), 159--179,
[doi:10.1007/BF00535487](https://doi.org/10.1007/BF00535487).  Its law `T`
has mass `1/N` at the identity and `2/N^2` at each transposition.  Lemma 14,
equation (3.1), bounds variation by the square root of

```text
sum_(lambda != trivial) d_lambda^2 z_lambda^(2s),
z_lambda=1/N+(N-1)r_lambda/N.                          (5)
```

The Section 3 partition-zone estimates bound the sum itself by a universal
constant times `e^{-4c}` at
`s=(N/2)log N+cN`.  Thus choosing a fixed universal `c` makes (5), not merely
its square root, at most `1/16`.

For `Q_N^s=P_N^{2s}` and even `g`, Fourier inversion gives

```text
(N!/2)Q_N^s(e,g)-1
 =(1/2)sum_(lambda not trivial,sign)
       d_lambda r_lambda^(2s) chi_lambda(g).            (6)
```

The trivial and sign terms each contribute one half.  Conjugate partitions
have equal dimensions and characters on `A_N`, opposite `r_lambda`, and can
be paired; a self-conjugate partition has `r_lambda=0`.  Choosing the member
with nonnegative ratio gives `0<=r_lambda<=z_lambda`, and
`|chi_lambda(g)|<=d_lambda`, so the absolute value of (6) is bounded by (5).
Translation invariance handles all `x,y`.  The positive majorant (5)
decreases at later times.  For `3<=N<=10`, irreducibility and the holding
mass `Q_N(e)>0` give the finite closure and allow enlargement of one universal
constant.  Therefore the asserted uniform pointwise relative estimate and
`s_*(N)=O(N log(N+1))` are correctly normalized.

### 2.3 Arbitrary endpoint tilts

For `K(x,y)=g_N^{-1}(1+delta_xy)`, `|delta_xy|<=epsilon`, and
`mu(x,y)` proportional to `alpha(x)K(x,y)beta(y)`, direct marginalization
gives

```text
dmu/d(mu_X times mu_Y)
 =(1+delta_xy)(1+d)/[(1+d_x)(1+e_y)].                  (7)
```

This remains valid when `alpha` or `beta` has zeros, on the resulting
marginal support.  Each average `d,d_x,e_y` lies in
`[-epsilon,epsilon]`.  The sharp upper deviation of (7) from one is
`4epsilon/(1-epsilon)^2`; the lower deviation is smaller.  The frozen proof's
relaxed bound

```text
(4epsilon+2epsilon^2)/(1-epsilon)^2
```

is therefore safe.  At `epsilon=1/16` it is `22/75`, while the sharp value is
`64/225`.  Inserting `(7)-1` into the covariance of centered unit-variance
functions and applying Cauchy--Schwarz bounds maximal correlation by the same
quantity.  Sparse arbitrary endpoint weights introduce no minimum-mass loss.

### 2.4 Tail correlation and projection spectrum

Choose `s` from `{s_*,s_*+1}` with the parity of `n`, put
`t=(n-s)/2`, and `L=t+s`.  The two outside tails determine `X_t` and `X_L`,
respectively.  After all middle paths and all pair labels are marginalized,
their boundary law has exactly the tilted form (7), with

```text
alpha(x)=Q_N^t(u,x),
K(x,y)=Q_N^s(x,y),
beta(y)=Q_N^t(y,v).
```

Symmetry makes both outer weights probability measures.  Bridge
factorization gives the Markov chain

```text
left tail -> X_t -> X_L -> right tail.
```

Conversely, each boundary is a function of its tail.  The two data-processing
inequalities therefore show that tail and boundary maximal correlations are
equal, including all microfactor labels.

The interval heat baths are orthogonal conditional-expectation projections
`P_1,P_2`.  On a principal-angle plane with correlation `c`, their average
has eigenvalues `(1+c)/2` and `(1-c)/2`.  Since `rho<=22/75<1`, the common
range on centered functions is trivial.  Hence

```text
gap((P_1+P_2)/2)=(1-rho)/2
 >=53/150>1/3.                                         (8)
```

No square root or extra factor two is missing.

### 2.5 Hamiltonian domination and scan normalization

The first length-`L` interval contains sites `1,...,L-1`, and the second
contains `t+1,...,n-1`.  Their union is all sites because `t+1<=L`; each site
occurs once or twice.  Since every `I-H_j` is positive semidefinite,

```text
H_n >=(1/2)(H_I1+H_I2).                                (9)
```

Conditioning on any outside configuration gives a feasible length-`L`
subbridge, so the worst-endpoint definition yields

```text
H_Ir>=Lambda_N(L)(I-P_r).
```

Combining this with (8)--(9) proves (1).  The comparison is entirely in the
continuous-time Hamiltonian: it does not divide by the number of sites at
each recursive scale.

### 2.6 Affine recursion algebra and endpoints

The parity choice makes `t` integral.  Since `s<=b` and `n>=b+2`,

```text
t>=1,  2<=L<n,  L-b=(n+s-2b)/2<=(n-b)/2.              (10)
```

Iterating (10) stops at a feasible length in `[2,b+1]` after at most
`ceil(log_2(n-b))` levels.  With `a=log_2 3`,

```text
3^(-ceil(log_2(n-b)))
 >=(1/3)(n-b)^(-a),                                    (11)
```

which proves (2).  The frozen report's phrase "the excess is at least
halved" should editorially read "the excess is at most halved"; its displayed
inequality and iteration are correct.

### 2.7 Conversion to `B` and `K`

From the definitions,

```text
I-B=H_n/(n-1),
```

so (3) is exact.  For `m=2n>=6`, the lazy full chain gives each length-four
window coefficient `1/[6(m-3)]`, whereas `B` gives each of its `n-1`
aligned windows coefficient `1/(n-1)`.  Dropping every nonaligned and every
`r=3,5` Dirichlet contribution gives

```text
E_K >=[(n-1)/(6(m-3))]E_B
     =[(m-2)/(12(m-3))]E_B
     >=E_B/12.                                         (12)
```

Thus (4) is correct.  At `m=4`, `H_(1,4)` is a whole-word heat bath with
full-`K` coefficient `1/4`; that boundary is correctly handled separately.

### 2.8 Attempted counterexamples

The deterministic harness sampled sparse and dense endpoint weights and
adversarial corner values `delta_xy in {+-1/16}`.  It also built the two
conditional-expectation projections explicitly and exhaustively checked the
integer recursion over the recorded ranges.  No counterexample appeared.
This is only falsification evidence; Sections 2.2--2.7 are the proof.

The standard-representation construction with overlap `floor(sqrt(N))`
does not contradict the theorem.  Its covariance is
`((N-3)/(N-1))^(2 floor(sqrt(N))) ->1`; the theorem deliberately chooses
overlap `Theta(N log N)`, after the pointwise threshold.

## 3. Probability, runtime, path length, and congestion accounting

- Pointwise middle-kernel error: at most `1/16` after
  `s_*(N)=O(N log(N+1))` Q-steps.
- Maximal correlation: at most `22/75`; two-block gap at least `53/150`,
  relaxed to `1/3`.
- Hamiltonian loss: exactly at most `3` per affine-geometric level.
- Number of levels: at most `ceil(log_2(n-b))`.
- Random scan: exactly one final factor `1/(n-1)`.
- Full-chain comparison: exact coefficient `(m-2)/[12(m-3)]`, relaxed to
  `1/12`.
- The interval projections are analytic conditionals, not claimed
  efficiently implementable transitions.  No path length or congestion is
  hidden in this reduction.  A real four-letter heat bath has inherited
  polynomial per-step cost.

## 4. Dependencies

- **Cited and independently checked:** Diaconis--Shahshahani Lemma 14,
  equation (3.1), and the Section 3 partition-zone collection, with the
  walk/exponent/parity translation in Section 2.2.
- **Proved in the frozen report and independently rederived:** bridge
  microfactorization, tilt density, maximal correlation, projection-angle
  spectrum, Hamiltonian comparison, recursion, and all scan factors.
- **Inherited proved:** exact local heat-bath reversibility and polynomial
  implementation; the direct `K`-to-aligned-`B` Dirichlet comparison.
- **New inherited correction:** arbitrary-product aligned-`H_4` fibers are
  qualitatively connected by the arbitrary-product Hurwitz classification.
  This removes reducibility as a base-fiber concern but supplies no
  quantitative base gap.
- **Empirical dependency:** none.

## 5. First unproved standalone proposition

> **BASE-SCALE FIXED-ENDPOINT GAP.** There exist universal `c>0,C<infinity`
> such that for every `N>=3`, every `2<=l<=s_*(N)+2`, and every feasible
> `u,v in A_N`, the full microfactorized aligned local Hamiltonian satisfies
> `Lambda_N(l;u,v)>=c(Nl)^(-C)`.

Qualitative irreducibility is now available.  The missing statement is the
uniform quantitative lower bound for all endpoints and all base lengths
through `O(N log N)`.

## 6. Strongest self-attack

The reduction magnifies the worst base endpoint: a single family of
polynomially small or smaller base gaps controls every longer bridge through
`Lambda_N(l)`.  Pointwise smoothing of the middle overlap cannot lower-bound
those short endpoint gaps.  Neither qualitative connectivity, polynomial
diameter, nor the fixed-length `l=3,4` bounds closes the growing base window.
Thus accepting this theorem must not be read as evidence that the remaining
base proposition is true.

Two nonblocking wording corrections are advisable: use the monotone positive
majorant (5), not the signed Fourier sum itself, when discussing later times;
and replace "at least halved" by "at most halved."  Neither changes a displayed
inequality or conclusion.

## 7. Calibration

- `N=2`: singleton; outside the recursion.
- Grouped `n=1` (`m=2`): no aligned site and excluded.
- Grouped `n=2` (`m=4`): whole-word `H_4`; handled separately.
- `S_3,m=4` and `S_4,m=4`: whole-word counts 27 and 120 are consistent.
- `S_4,m=6`: 3,936 words and 17 pure-Hurwitz components do not conflict with
  connected aligned heat baths.
- Parity is retained through `Q=P^2`, the trivial/sign pair in (6), and the
  parity choice of `s`.
- Arbitrary sparse endpoint tilts are explicitly allowed in (7).
- Near-minimal/doubled-tree words and the failed length-two local simulation
  are not used.
- The standard mode refutes sublinear-overlap constant angle only; it is
  consistent with the claimed `O(N log N)` overlap.

## 8. Artifacts and reproduction

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/counterexample_audit.py
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/results.json
experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/report.md
```

Reproduce with:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/counterexample_audit.py \
  --samples 20000 --max-sstar 80 --max-excess 5000 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M10-referee/results.json
```

Seed `20260811`; Python `3.12.3`; NumPy `1.26.4`.  The run checked 20,000
tilted laws and 399,920 recursion instances, with zero failures.  Maximum
projection-formula error was `7.22e-16`.

## 9. Verdict and numbered objections

**ACCEPT.**

Numbered objections: none.

This accepts only the frozen nonterminal reduction and its constants.  It
does not accept the open base-scale gap proposition or Terminal A.
