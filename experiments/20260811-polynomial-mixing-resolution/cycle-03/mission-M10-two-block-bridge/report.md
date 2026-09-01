# Cycle 03 M10 report: constant-loss two-block Q-bridge recursion

## 1. Exact claim, quantifiers, and conventions

Use `(pq)(x)=p(q(x))`.  Let `P_N` be uniform on the
`M=binom(N,2)` transpositions and let `Q_N=P_N^2`, a symmetric aperiodic walk
on `A_N`.  Pair a length-`2n` word as
`Y_i=t_{2i-1}t_{2i}` and use prefixes `X_0=e`,
`X_i=Y_1...Y_i`, `X_n=e`.  The exact bridge law is proportional to

```text
product_i Q_N(X_{i-1}^{-1}X_i),                         (1.1)
```

including an independent uniform ordered-transposition microfactorization
of each increment.  If `a_N(y)=M^2Q_N(y)`, then

```text
a_N(e)=M,
a_N(y)=3 for a 3-cycle,
a_N(y)=2 for two disjoint transpositions.               (1.2)
```

Let `H_j=H_{2j-1,4}` and define the continuous-time local Hamiltonian and
nonlazy aligned random scan by

```text
mathcal H_n=sum_{j=1}^{n-1}(I-H_j),
B=(1/(n-1))sum_{j=1}^{n-1}H_j.                          (1.3)
```

For a length-`l` bridge from `u` to `v`, define
`Lambda_N(l;u,v)` as the best Poincare constant of the corresponding local
Hamiltonian relative to its full conditional variance, with value zero if
that fixed-endpoint chain is reducible.  Set

```text
Lambda_N(l)=min_{u,v:Q_N^l(u,v)>0} Lambda_N(l;u,v).      (1.4)
```

**Proved two-block recursion.**  There are universal `C_*<infinity` and
integers `s_*(N)<=C_*N log(N+1)` such that, with
`b_N=s_*(N)+1`, for every `N>=3` and every `n>=b_N+2`, one can choose an
integer `L<n` satisfying

```text
L-b_N<=(n-b_N)/2
```

for which

```text
Lambda_N(n)>=Lambda_N(L)/3.                             (1.5)
```

Consequently, with `a=log(3)/log(2)`,

```text
Lambda_N(n;e,e)
 >=(1/3)(n-b_N)^(-a)
   min_{2<=l<=b_N+1}Lambda_N(l)                         (1.6)
```

for `n>=b_N+2`.  This has one constant loss per affine-geometric scale and
does not pay a random-scan factor at every recursion level.

**Proved red-team limitation.**  A universal constant-angle version is
false for sublinear overlap: there is an explicit pinned identity-bridge
family with overlap `floor(sqrt(N))` and both outside tails of length `N^3`
whose two-block maximal correlation tends to one.

The recursion leaves the uniform fixed-endpoint base gap for
`l=O(N log N)` open.  Therefore these claims do not prove Terminal A or
Terminal B.

## 2. Full argument

### 2.1 Pointwise smoothing with parity retained

Write `g_N=|A_N|=N!/2`.  The needed overlap length satisfies

```text
max_{x,y in A_N}|g_NQ_N^s(x,y)-1|<=1/16
                                                        for s>=s_*(N). (2.1)
```

Here is the exact translation from the classical character estimate.  Let
`r_lambda` be the character ratio of a uniform transposition in the
`S_N` irreducible indexed by `lambda`, and put

```text
z_lambda=1/N+(N-1)r_lambda/N.                           (2.2)
```

This is the Fourier scalar of the with-replacement lazy transposition law
used by Diaconis--Shahshahani.  Since `Q_N^s=P_N^{2s}`, Fourier inversion on
`S_N`, followed by restriction to an even `g`, gives

```text
g_NQ_N^s(e,g)-1
 =(1/2)sum_{lambda notin {(N),(1^N)}}
       d_lambda r_lambda^(2s)chi_lambda(g).              (2.3)
```

The trivial and sign terms each contribute one half and together give the
uniform `A_N` term.  Conjugate partitions have equal dimension, opposite
`r_lambda`, and equal characters on `A_N`; self-conjugate partitions have
`r_lambda=0`.  From each remaining pair choose the member with
`r_lambda>=0`.  Since

```text
z_lambda-r_lambda=(1-r_lambda)/N>=0,
```

and `|chi_lambda(g)|<=d_lambda`, (2.3) is bounded in absolute value by

```text
sum_{chosen lambda}d_lambda^2z_lambda^(2s)
 <=sum_{lambda !=(N)}d_lambda^2|z_lambda|^(2s).          (2.4)
```

Diaconis--Shahshahani Lemma 14, equation (3.1), is precisely the relevant
Plancherel sum.  Their Section 3 estimates its partition zones in equations
(3.2), (3.3), (3.5), (3.7), and (3.13), then collects them at the end of the
proof of Theorem 1.  Those displayed estimates make (2.4) uniformly as small
as desired for `N>10` at

```text
s=(N/2)log N+cN
```

by choosing one universal `c`.  Choose it so that (2.4) is at most `1/16`.
For `3<=N<=10`, enlarge the universal constant: `Q_N(e)>0`, every 3-cycle
has positive `Q_N` mass, and 3-cycles generate `A_N`, so these finitely many
walks are irreducible and aperiodic.  Finally, the absolute sum in (2.3)
decreases at later times because all `Q_N` eigenvalues are
`r_lambda^2 in [0,1]`.  This proves (2.1) for an
`s_*(N)<=C_*Nlog(N+1)`.

This is not an inference from total-variation mixing.  The pointwise relative
bound follows from (2.3)--(2.4) and the Plancherel sum estimated inside the
source's proof.

### 2.2 Arbitrary endpoint tilts and maximal correlation

The next lemma is deliberately uniform over the endpoint weights.  Let

```text
K(x,y)=g_N^(-1)(1+delta_xy),       |delta_xy|<=epsilon<1,
mu(x,y)=alpha(x)K(x,y)beta(y)/Z,                         (2.5)
```

where `alpha,beta` are arbitrary probability measures, possibly with zeros.
Put

```text
d=E_{alpha x beta}delta,
d_x=E_beta delta_xy,
e_y=E_alpha delta_xy.
```

Direct marginalization gives

```text
dmu/d(mu_X x mu_Y)
 =(1+delta_xy)(1+d)/[(1+d_x)(1+e_y)].                   (2.6)
```

Every factor belongs to `[1-epsilon,1+epsilon]`; hence, on the marginal
support,

```text
((1-epsilon)/(1+epsilon))^2
 <=dmu/d(mu_X x mu_Y)
 <=((1+epsilon)/(1-epsilon))^2.                         (2.7)
```

The upper deviation from one is exactly
`4epsilon/(1-epsilon)^2`; the lower deviation is smaller.  In particular the
safe relaxed audit bound is

```text
|dmu/d(mu_X x mu_Y)-1|
 <=(4epsilon+2epsilon^2)/(1-epsilon)^2.                 (2.8)
```

If `f(X),g(Y)` are centered and have unit variance, insert the density in
their covariance and apply Cauchy--Schwarz under `mu_X x mu_Y`.  Thus their
maximal correlation is at most (2.8).  With `epsilon=1/16`,

```text
rho(X,Y)<=22/75<1/3.                                   (2.9)
```

The sharper direct value is `64/225`; only the safe value is used below.

### 2.3 The two interval projections

Fix any feasible length-`n` bridge from `u` to `v`, and assume
`n>=b_N+2`.  Choose

```text
s in {s_*(N),s_*(N)+1} with s congruent to n mod 2,
t=(n-s)/2>=1,
L=t+s=(n+s)/2<n.                                       (2.10)
```

Because `s<=b_N`,

```text
L-b_N<=(n-b_N)/2.                                      (2.11)
```

Take intervals

```text
I_1=[0,L],       I_2=[t,n],
```

and let `P_1,P_2` be their exact conditional heat baths, refreshing all
prefixes and all ordered-transposition microfactor labels inside the chosen
interval.  The range of `P_1` is the right-tail sigma-field after `L`; the
range of `P_2` is the left-tail sigma-field before `t`.

The left tail determines `X_t`, while the right tail and pinned endpoint
determine `X_L`.  Segment factorization of (1.1), together with the
conditional independence of the microfactorizations, gives

```text
left tail -> X_t -> X_L -> right tail.                  (2.12)
```

Since the two boundary variables are themselves functions of the two tails,
maximal-correlation data processing holds with equality.  The boundary joint
law is (2.5) with

```text
alpha(x)=Q_N^t(u,x),
K(x,y)=Q_N^s(x,y),
beta(y)=Q_N^t(y,v).                                    (2.13)
```

Both outer weights may be sparse; (2.9) still applies because only the middle
kernel needs (2.1).

For two orthogonal conditional-expectation projections, the principal-angle
decomposition gives the exact formula

```text
gap((P_1+P_2)/2)=(1-rho)/2.                             (2.14)
```

Indeed, on each nontrivial two-dimensional principal-angle plane the
eigenvalues are `(1+-rho_i)/2`.  Since `rho<1`, any common centered function
of the two tails would contradict the definition of maximal correlation, so
the intersection at eigenvalue one consists only of constants.  Equations
(2.9) and (2.14) give

```text
gap((P_1+P_2)/2)>=1/3.                                 (2.15)
```

### 2.4 Hamiltonian comparison and iteration

The interval Hamiltonians contain respectively the local sites

```text
{1,...,L-1},          {t+1,...,n-1}.
```

Their union is every site of `mathcal H_n`, and no site occurs more than
twice.  Therefore, as quadratic forms,

```text
mathcal H_n >=(1/2)(mathcal H_I1+mathcal H_I2).          (2.16)
```

On every fixed outside configuration, the definition (1.4) gives

```text
mathcal H_Ir>=Lambda_N(L)(I-P_r),       r=1,2.           (2.17)
```

This remains formally true if a subbridge is reducible, because then the
defined worst Poincare constant is zero.  Combining (2.15)--(2.17),

```text
mathcal H_n
 >=Lambda_N(L)[I-(P_1+P_2)/2],
Lambda_N(n;u,v)>=Lambda_N(L)/3.                         (2.18)
```

Taking the worst endpoints proves (1.5).  At each iteration the excess
`n-b_N` is at least halved.  If
`k=ceil(log_2(n-b_N))`, then

```text
3^(-k)>=(1/3)(n-b_N)^(-log_2 3),
```

which proves (1.6).  This is the promised constant loss per scale.

Finally,

```text
gap(B)=Lambda_N(n;e,e)/(n-1).                           (2.19)
```

The factor `n-1` is paid once, after the continuous-time recursion.  The
inherited exact comparison for `m=2n>=6` is

```text
gap(K_{N,2n})
 >=[(m-2)/(12(m-3))]gap(B)
 >=gap(B)/12.                                           (2.20)
```

Thus a polynomial base bound in Section 5 would complete this entire bridge
route to Terminal A, together with audited irreducibility and the separate
`m=4` whole-word argument.

### 2.5 Sublinear-overlap obstruction

For `N>=4`, the standard representation has uniform-transposition character
ratio

```text
r_std=(N-3)/(N-1),
```

so the corresponding `Q_N` eigenvalue is `q_std=r_std^2`.  Take the identity
bridge with both outside tails of length `t_N=N^3` and central overlap
`s_N=floor(sqrt(N))`.  The same Diaconis--Shahshahani sum estimates, now far
beyond cutoff, make

```text
Q_N^t(e,x)=g_N^(-1)(1+o(N^-2))
```

uniformly in `x`.  Hence the boundary joint law differs by relative
`o(N^-2)` from

```text
mu_0(x,y)=g_N^(-1)Q_N^s(x,y),                           (2.21)
```

whose marginals are uniform.  The standard character restricted to `A_N`
has uniform mean zero, variance one, and supremum at most `N-1`.  Testing it
in the maximal-correlation variational formula changes its covariance and
variance by `o(1)` under this perturbation.  Under (2.21), its normalized
covariance is exactly `q_std^s`.  Consequently

```text
rho_N
 >=((N-3)/(N-1))^(2 floor(sqrt(N)))-o(1)
 ->1.                                                   (2.22)
```

Thus the two-block gap tends to zero.  This rules out a constant-loss
recursion with every `o(N)` overlap.  It does not show slow mixing of `B`,
and one-way comparison (2.20) cannot turn it into a statement about slow K.

## 3. Rate, runtime, path length, and congestion accounting

- The continuous-time recursion loses exactly a factor at most `3` per
  affine-geometric scale.  It has at most `ceil(log_2(n-b_N))` levels.
- Random scan contributes exactly `1/(n-1)` once through (2.19).
- The full-chain comparison contributes at most `12` through (2.20); its
  unsimplified factor is `(m-2)/[12(m-3)]`.
- The block projections are analytic conditional expectations, not proposed
  transition simulations.  No large-block sampler runtime or comparison
  congestion is being hidden.
- No paths or multicommodity flow are used in the recursion.
- A real `B` step is one exact length-four same-product heat bath.  Existing
  exact enumeration uses at most `M^4` candidates, polynomial in `N`; the
  sharper project sampler is inherited.
- `short_overlap_support.py` is deterministic.  It explicitly enumerates
  `A_N`, so its worst-case runtime is factorial and it is only a bounded
  falsification harness.  The targeted `N=5,6,7`, one-step-tail/one-step-
  overlap runs found no disconnected boundary support.  This is finite
  evidence only and supplies no base gap.

## 4. Dependencies and status

- **Proved here:** the parity-aware conversion (2.3)--(2.4), the endpoint-
  tilt density and maximal-correlation bounds, exact two-projection angle,
  Hamiltonian comparison, affine recursion and iteration, and the sublinear-
  overlap obstruction.
- **Cited with hypotheses checked:** Diaconis--Shahshahani, Lemma 14,
  equation (3.1), the Section 3 zone estimates, and the end of the proof of
  Theorem 1 for the with-replacement lazy random-transposition Plancherel
  sum.  The different walk and `A_N` parity are translated explicitly in
  (2.2)--(2.4).
- **Proved inherited:** the exact microfactorized Q-bridge representation,
  positivity of the heat-bath average, aligned-chain irreducibility for the
  identity bridge, `gap(K)>=gap(B)/12`, and `gap(K_{N,4})>=1/4`.
- **Conditional/open:** the uniform fixed-endpoint base gap in Section 5.
  Inherited identity-bridge irreducibility does not prove arbitrary-endpoint
  subbridge irreducibility.
- **Exact finite evidence:** the short-overlap support outputs for
  `N=5,6,7`; they fail to falsify support connectivity only.  No theorem
  depends on them.
- **Empirical dependencies:** none in the proved recursion.

Primary source: P. Diaconis and M. Shahshahani, “Generating a Random
Permutation with Random Transpositions,” *Z. Wahrscheinlichkeitstheorie
verw. Gebiete* 57 (1981), 159--179,
[`10.1007/BF00535487`](https://doi.org/10.1007/BF00535487),
with a [primary PDF](https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis%2C%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf).

## 5. First unproved standalone proposition

> **BASE-SCALE FIXED-ENDPOINT GAP.**  Let `s_*(N)` be any threshold satisfying
> (2.1).  There are universal constants `c>0,C<infinity` such that, for every
> `N>=3`, every `2<=l<=s_*(N)+2`, and every
> `u,v in A_N` with `Q_N^l(u,v)>0`, the full microfactorized local Hamiltonian
> obeys
> `Lambda_N(l;u,v)>=c(Nl)^(-C)`.

The case `l=2` is a whole-interval heat bath and has `Lambda_N(2;u,v)=1`.
For larger `l`, the proposition includes qualitative irreducibility for every
fixed product, not merely for the identity bridge.

If this proposition holds, (1.6), (2.19), and (2.20) give a universal
inverse-polynomial gap for K.  Since `s_*(N)=O(Nlog N)`, its base factor is
still polynomially parameterized.  Logarithms can be absorbed into the final
universal exponent.

The different base comparison attempted here used two almost-whole blocks
with one-step outside tails.  Exact support enumeration found no disconnection
through `N=7`, but its transition weights can have ratios as small as products
of `Q` probabilities over `O(Nlog N)` steps.  A minimum-entry estimate is
therefore superpolynomial, and finite support connectivity does not establish
the required angle.  Fixed-target path theorems retain factorial dependence
on `|A_N|`; canonical identity-heavy routing has the inherited exponential hub
congestion.  No audited base comparison closes the proposition.

## 6. Strongest self-attack

The recurrence is a reduction, not a global gap proof.  Its worst-subinterval
constant deliberately becomes zero if even one feasible base endpoint fiber
is reducible.  The inherited irreducibility theorem for the pinned identity
bridge does not eliminate that possibility.  Even if all base fibers are
connected, neither polynomial diameter nor the finite support tests control
stationary edge capacities or congestion.

The Diaconis--Shahshahani input controls the unconditioned middle kernel, but
the endpoint-tilt lemma is what makes it useful for bridges; omitting that
step would be a genuine gap.  Conversely, the standard-mode construction
only rejects sublinear-overlap constant angles.  It is not a bottleneck for B,
and the r=3,5 terms of K could only make K faster.

## 7. Calibration

- Odd original `m`: the identity bridge is empty.  The grouped model uses
  `m=2n` only.
- `m=0`: singleton and outside the theorem.
- `N=2`, even `m`: singleton; the recursion starts at `N=3`.
- `m=2,N>=3`: excluded; grouped length one has no local site and retains
  unresolved microfactor labels.
- `m=4` (`n=2`): the original `H_{1,4}` is a whole-word heat bath with exact
  full-K coefficient `1/4`.  It is not replaced by the long-bridge recursion.
- `S_3,m=4` and `S_4,m=4`: the inherited counts are `27` and `120`; the
  whole-word argument applies.  In fact one Q step is uniform on `A_3`, while
  Q has full support on `A_4`, consistent with the smoothing statement.
- `S_4,m=6`: the inherited count is `3936`, with 17 pure-Hurwitz components;
  the aligned B chain is nevertheless exactly connected.  This finite fact
  is not promoted to the base proposition.
- Q is on `A_N`; `Q(e)=1/M` removes periodicity.  The trivial/sign pairing in
  (2.3) retains, rather than discards, parity.
- Every block heat bath and sigma-field includes the ordered-transposition
  microfactor labels.  Disjoint support components and color interleavings
  are not collapsed.
- Near-minimal doubled trees, parity summaries, length-two simulation, and a
  canonical hub are not used in the positive recursion.
- No asymptotic cut is claimed.  The sublinear-overlap mode accounts for its
  full bridge law but concerns an auxiliary block angle, not conductance of K.
- All polynomial statements use the declared parameters `N,m`, not `log N`.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-03/mission-M10-two-block-bridge/
```

Files:

```text
plan.md
checkpoint.md
short_overlap_support.py
support_N5_t1_s1.json
support_N6_t1_s1.json
support_N7_t1_s1.json
report.md
```

Reproduce the deterministic finite support audit from the repository root:

```text
python3 -m compileall experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/short_overlap_support.py
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/short_overlap_support.py --N 5 --tail 1 --overlap 1 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/support_N5_t1_s1.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/short_overlap_support.py --N 6 --tail 1 --overlap 1 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/support_N6_t1_s1.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/short_overlap_support.py --N 7 --tail 1 --overlap 1 --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M10-two-block-bridge/support_N7_t1_s1.json
```

Environment: Python `3.12.3`; deterministic; no random seed or nonstandard
dependency.  The universal claim the calculation could falsify is exactly
that every feasible short-overlap boundary support is connected.  The three
runs did not falsify it and are not used as proof.

## 9. Verdict

**PROVED**

This verdict is scoped to the assigned constant-loss large-overlap recursion
and its exact conversion factors.  The BASE-SCALE FIXED-ENDPOINT GAP remains
open, so the verdict is not Terminal A or Terminal B.
