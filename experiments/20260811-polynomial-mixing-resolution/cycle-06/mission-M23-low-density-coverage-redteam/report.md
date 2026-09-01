# Cycle 06 M23 report: lower-density support thresholds rejected

## 1. Exact claim, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`; a word evaluates as `t_1...t_m`.
The target `pi` is uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and the exact chain is

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
   (1/(m-r+1)) sum_(i=1)^(m-r+1) H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

Let `X(w)` be the number of labels unused by all factors and define

```text
T_q={w:X(w)>=q},       1<=q<=N-2,
U=T_1.                                                 (1.2)
```

Let `A>=1` be the audited parity-aware pointwise random-transposition
constant specified in Section 2.1 and put

```text
B_*=32(A+1).                                          (1.3)
```

The new theorem is:

> **Lower-density coverage anti-bottleneck.**  For every `N>=3`, every even
> `m` satisfying
>
> ```text
> m-2>=B_*N log(N+1),                                 (1.4)
> ```
>
> and every `1<=q<=N-2`, `T_q` is nonempty and proper, is the exact smaller
> stationary side, and
>
> ```text
> Phi_pm^K(T_q)
> :=Q_K(T_q,T_q^c)/min{pi(T_q),pi(T_q^c)}
> >=q/[8(N-q-1)(m-2)D_N]
> >=1/(16mN^3),
> D_N=(3N^2+N-12)/2.                                  (1.5)
> ```

This strictly improves the M21 coverage threshold
`C_*=256(A+1)` by a factor eight.  In particular, it newly controls the
entire growing-surplus interval

```text
2+B_*N log(N+1)<=m<2+C_*N log(N+1),                   (1.6)
```

within the assigned regime.  It is a scoped cut rejection, not Terminal A
or Terminal B.

## 2. Full proof

### 2.1 Exact parity-aware return input

Let `P_n` be the nonlazy walk on `S_n` that multiplies by a uniform
transposition, and write

```text
p_n(j)=P_n^j(id,id).
```

For even `j`, Fourier inversion gives

```text
p_n(j)=(1/n!)sum_(lambda partition n)
               (f^lambda)^2 r_lambda^j.               (2.1)
```

All terms are nonnegative.  The trivial and sign terms prove

```text
p_n(j)>=2/n!.                                         (2.2)
```

The audited Diaconis--Shahshahani partition-zone estimate supplies a
universal `A>=1` such that, for every `n>=3` and every even
`j>=A n log(n+1)`,

```text
p_n(j)=[2/n!](1+u_n(j)),    0<=u_n(j)<=1/16,
```

and in particular

```text
p_n(j)<=3/n!.                                         (2.3)
```

For `n=2`, even return is exactly one, so (2.2)--(2.3) remain valid.

### 2.2 New disconnected-support bound at B_* rather than C_*

Let `delta_n(j)` be the probability, under the length-`j` identity bridge,
that the factorization graph on `[n]` is disconnected.  We prove

```text
delta_n(j)<1/4                                        (2.4)
```

for every `n>=3` and even `j>=B_*n log(n+1)`.

Fix a vertex cut with smaller side of size `1<=s<=n/2`, put `b=n-s`, and
write

```text
M_n=binom(n,2),
L=binom(s,2)+binom(b,2)=M_n-sb,
alpha=binom(b,2)/L>=1/2.                              (2.5)
```

The probability that an unconditioned word uses no crossing edge is
`(L/M_n)^j`.  Conditional on this event, its two subgroup walks receive
`J` and `j-J` steps, where

```text
J~Bin(j,alpha).
```

Use the constant-coordinate convention when `s=1`.  Since

```text
A b log(b+1)<=A n log(n+1)<=(A/B_*)j<=j/32
```

and `E[J]>=j/2`, this threshold is at most `E[J]/2`.  Chernoff's inequality
therefore gives

```text
Pr[J<A b log(b+1)]<=exp(-E[J]/8)<=exp(-j/16).         (2.6)
```

If `J` is odd, the large subgroup cannot return to the identity.  If `J` is
even and above the threshold, (2.3) bounds its return by `3/b!`.  Bound the
small subgroup return by one.  The exact probability that this fixed cut
has no crossing edge and the full product returns is consequently at most

```text
(L/M_n)^j[3/b!+exp(-j/16)].                           (2.7)
```

Divide (2.7) by the full bridge return, using (2.2), and union-bound all
cuts.  Since

```text
n!/b!<=n^s,
binom(n,s)<=(en/s)^s,
(L/M_n)^j<=(exp(-s/n))^j,                             (2.8)
```

where the last inequality uses `sb/M_n>=s/n`, the contribution of the
`3/b!` terms is at most

```text
(3/2)sum_(s=1)^[floor(n/2)]
       [e n^2 exp(-j/n)]^s.                           (2.9)
```

For the Chernoff terms, discard `(L/M_n)^j` and use
`sum_s binom(n,s)<=2^n`; their total is at most

```text
2^(n-1)n!exp(-j/16).                                  (2.10)
```

Put `R=e n^2(n+1)^(-B_*)`.  Because `B_*>=64`, `e<3`, and
`n^2<=(n+1)^2`,

```text
R<=3(n+1)^(-(B_*-2))<1/2,
(2.9)<=3R<=9*4^-62<1/8.                              (2.11)
```

Also `2n<=(n+1)^2` and `B_*/16-2=2A>=2`, so

```text
(2.10)
 <=(2n)^n(n+1)^(-B_*n/16)
 <=(n+1)^[-(B_*/16-2)n]
 <=4^-6<1/8.                                          (2.12)
```

Equations (2.9)--(2.12) prove (2.4).  In particular, the small subgroup was
not charged a factorial return penalty; its return stayed inside (2.7) and
was bounded only by one.

### 2.3 Exact support masses, overlaps, and boundary-layer mass

Write `Z_(d,k)=|Omega(d,k)|`, and let `E_(d,k)` count words on `[d]` whose
exact support is `[d]`.  For positive `k`, set `Z_(0,k)=Z_(1,k)=0`.
Inclusion-exclusion and support-set choice give

```text
E_(d,k)=sum_(a=0)^d (-1)^(d-a)binom(d,a)Z_(a,k),      (2.13)

pi(X=s)=binom(N,s)E_(N-s,m)/Z_(N,m),                 (2.14)

pi(T_q)=
 [sum_(s=q)^(N-2)binom(N,s)E_(N-s,m)]/Z_(N,m).       (2.15)
```

Thus all overlaps among missing-label events are exact.  Define

```text
mu_q=E_pi[binom(X,q)].
```

Counting a bridge together with a chosen missing `q`-set yields

```text
mu_q=binom(N,q)Z_(N-q,m)/Z_(N,m).                    (2.16)
```

Put `d=N-q` and `M_d=binom(d,2)`.  Since
`Z_(d,m)=M_d^m p_d(m)`, (2.2)--(2.3) give, for `d>=3`,

```text
mu_(q+1)/mu_q
 =[d/(q+1)]Z_(d-1,m)/Z_(d,m)
 <=[3d^2/(2(q+1))][(d-2)/d]^m
 <=[3d^2/(2(q+1))]exp(-2m/d).                        (2.17)
```

The pointwise upper bound is used at degree `d-1`; (1.4) implies its
hypothesis.  For `d=2`, the ratio is zero because `Z_(1,m)=0`.  Since
`d<=N`, condition (1.4) also gives

```text
exp(-2m/d)<=(N+1)^(-2B_*)<=1/(3d^2).                 (2.18)
```

For `s>=q+1`,

```text
binom(s,q)<=(q+1)binom(s,q+1).
```

Equations (2.17)--(2.18) therefore imply

```text
mu_q-pi(X=q)<=(q+1)mu_(q+1)<=mu_q/2,
pi(X=q)>=mu_q/2>=pi(T_q)/2.                           (2.19)
```

Every omitted label disconnects the graph on `[N]`.  Applying (2.4) at
length `m` gives

```text
pi(T_q)<=pi(U)<=delta_N(m)<1/4<1/2.                  (2.20)
```

Thus `T_q`, whose exact mass is (2.15), is the correctly oriented smaller
side.  It is nonempty by a doubled-tree identity word on a fixed
`N-q`-set plus padding squares, and its complement is nonempty by the same
construction on all `N` labels; (1.4) is well above both required lengths.

### 2.4 Exact safe squares and original-K boundary flow

Conditional on `X=q` and its missing set, the state is uniform among the
`E_(d,m)` exact-support words on the other `d=N-q` labels.  Let `Y(w)` count
adjacent equal pairs whose deletion leaves exact support.  Deletion of a
marked safe pair is a bijection with:

1. an exact-support core counted by `E_(d,m-2)`;
2. one of the `M_d` inserted transpositions; and
3. one of the `m-1` marked insertion gaps.

Hence

```text
E[Y]=(m-1)M_d E_(d,m-2)/E_(d,m).                     (2.21)
```

Connected support is exact support.  Combining (2.4) at degree `d` and
length `m-2` with `E_(d,m)<=Z_(d,m)` gives

```text
E_(d,m-2)>=Z_(d,m-2)[1-delta_d(m-2)]
             >=(3/4)Z_(d,m-2).                       (2.22)
```

For even exponents, (2.1) and `|r_lambda|<=1` imply

```text
p_d(m-2)>=p_d(m).                                    (2.23)
```

Since `Y<=m-1`, equations (2.21)--(2.23) yield

```text
Pr(Y>=1)
 >=M_d E_(d,m-2)/E_(d,m)
 >=3/(4M_d).                                         (2.24)
```

For `d=2`, the unique edge fills every factor and (2.24) holds directly.

Choose the first safe square `e,e`.  Pad it on the right unless it is the
final pair, in which case pad on the left.  For the padding transposition
`a`, use

```text
(e,e,a)->(f,f,a),       (a,e,e)->(a,f,f),             (2.25)
```

where `f` crosses between the `q` missing and `d` used labels.  There are
exactly `qd` distinct choices.  The safe core preserves every old label and
`f` introduces one missing label, so each output has exactly `q-1` missing
labels and leaves `T_q`.

The exact length-three fiber of a transposition product has size

```text
D_N=M+3[2(N-2)]+2binom(N-2,2)
   =(3N^2+N-12)/2.                                   (2.26)
```

This follows by choosing the third factor: the first two multiply to the
identity, a 3-cycle, or a double transposition, which have `M`, three, and
two ordered transposition factorizations respectively.

Under (1.4), `R_m={3,4,5}`.  Including laziness, block-size choice, window
choice, and the conditional heat bath, every certified state has summed
exit probability at least

```text
qd/[2*3*(m-2)D_N].                                   (2.27)
```

For exact full-chain accounting, define

```text
Q_r(T_q,T_q^c)
 =pi(T_q)/[2|R_m|(m-r+1)]
   E_(w|T_q)[sum_(i=1)^(m-r+1)H_(i,r)(w,T_q^c)].     (2.28)
```

Laziness contributes zero, and

```text
Q_K(T_q,T_q^c)=Q_3+Q_4+Q_5.                          (2.29)
```

The last two terms remain present and nonnegative.  Applying (2.19),
(2.24), and (2.27) to `Q_3` gives

```text
Q_K(T_q,T_q^c)
 >=pi(T_q)[1/2][3/(4M_d)]
       [qd/(6(m-2)D_N)]
 =pi(T_q)q/[8(d-1)(m-2)D_N].                        (2.30)
```

Divide by the exact smaller mass from (2.20), substitute `d=N-q`, and get
the first inequality in (1.5).  Finally `q>=1`, `d-1<=N`, `m-2<=m`, and
`D_N<=2N^2` give the second.

## 3. Worst probability, runtime, path, and congestion accounting

- The boundary layer `X=q` has conditional mass at least `1/2` inside
  `T_q`.
- A safe square has conditional probability at least
  `3/[4binom(N-q,2)]` on that layer.
- From a certified state, the summed specified exit probability is at least
  `q(N-q)/[6(m-2)D_N]`.
- Each witness is one transition of the original chain.  There is no
  comparison path or congestion factor.
- Missing-label and occurrence tables take `O(N+m)` time; scanning safe
  squares takes `O(m)` and listing at most `q(N-q)<=M` exits takes `O(N^2)`.
  The exact block heat bath has polynomial per-step cost.
- The support-disconnection audit retains the fixed-cut probability,
  binomial allocation tail, factorial return normalizations, and all
  `2^n` cut multiplicity in (2.7)--(2.12).

## 4. Dependencies with status

- **PROVED HERE:** the new disconnected-support estimate at `B_*`, exact
  overlap/factorial moments, boundary-layer domination, exact orientation,
  safe-square incidence, original-`K` boundary flow, and every constant in
  (1.5).
- **INHERITED PROVED:** exact heat-bath reversibility/stationarity and the
  parity-aware pointwise consequence (2.3).
- **CITED WITH HYPOTHESES AND NORMALIZATION CHECKED IN CYCLE-04 M07:**
  P. Diaconis and M. Shahshahani, *Generating a random permutation with
  random transpositions*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 57
  (1981), Lemma 14 equation (3.1), zone estimates (3.2), (3.3), (3.5),
  (3.7), and (3.13), collected in the proof of Theorem 1.  M07 checks the
  translation from their lazy transform to parity-aware nonlazy ratios.
- **NOT USED:** support-layer or component-count unimodality, independence
  of missing labels, DYZ fixed-genus formulas, pendant ratios, finite
  convergence, Hurwitz-only mixing, or a canonical hub.
- **EMPIRICAL/COMPUTATIONAL DEPENDENCIES:** none.

## 5. First unproved standalone proposition

> **SUB-B_* COVERAGE CONDUCTANCE.**  There are universal `c>0,C<infinity`
> such that for every `N>=3`, every even `m` with
>
> ```text
> 2(N-1)<m<2+B_*N log(N+1),
> ```
>
> and every `1<=q<=N-2` for which both sides of `T_q` are nonempty,
>
> ```text
> Phi_pm^K(T_q)>=c(Nm)^(-C).
> ```
>
> Alternatively, construct an explicit infinite family in this interval
> with superpolynomially small full-`K` conductance, including exact
> stationary mass and complete `Q_3+Q_4+Q_5` flow.

The remaining interval still contains growing surplus.  No monotonicity of
support layers is assumed in this proposition.

## 6. Strongest self-attack and Terminal-B audit

The factor-eight gain is a quantitative improvement of the parity-mixing
route, not a new mechanism for the near-minimal regime.  The proof needs the
large-side subgroup return estimate and a Chernoff allocation; below
`B_*N log(N+1)`, loss of (2.4) only blocks this argument and does not prove a
bottleneck.  The constant `A` is universal but not numerically optimized.

Coverage thresholds are only one family of cuts.  This theorem says nothing
about non-threshold support-set unions, partitions without isolated labels,
or internal full-support geometry.  No superpolynomial full-`K` family was
found, so Terminal B is not claimed.

## 7. Calibration

- Odd `m` gives an empty bridge; `m=0` and `N=2` are singleton regimes; the
  disconnected `m=2,N>=3` chain is excluded.  The theorem begins far above
  all of these.
- At `S_3,m=4`, `pi(U)=3/27=1/9`.
- At `S_4,m=4`, exact support inclusion-exclusion gives

  ```text
  pi(U)=102/120=17/20,
  pi(X=1)=96/120,  pi(X=2)=6/120.
  ```

  Here `R_m={3,4}` and the whole-word `H_4` has kernel coefficient `1/4`.
  Its boundary contribution alone gives every proper cut conductance at
  least `1/8`; it is not omitted from any normalization.
- At `S_4,m=6`,

  ```text
  pi(U)=966/3936=161/656,
  pi(X=1)=960/3936,  pi(X=2)=6/3936.
  ```

  The exact overlap is visible: the four fixed-label events sum to 972
  states, while their union has 966.
- The `27/120/3936` totals and `4/13/17` pure-Hurwitz components are
  consistent, but no Hurwitz-orbit law is used.
- Near-minimal doubled trees fall in the remaining sub-`B_*` interval and
  are not inferred to mix rapidly from this theorem.  Ordered color
  interleavings of disconnected components remain in every exact count.
- No edge/degree parity characterization, failed length-two simulation,
  graph-only model, or canonical hub is used.

## 8. Artifacts and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M23-low-density-coverage-redteam/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M23-low-density-coverage-redteam/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M23-low-density-coverage-redteam/report.md
```

No computation was used.  Reproduction consists of checking the fixed-cut
bridge calculation (2.5)--(2.12), exact factorial moments, safe-square
insertion/deletion, and full kernel factors (2.26)--(2.30).  Repository base
commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

This verdict applies to the new lower-density coverage theorem (1.5), not
to either global terminal outcome.
