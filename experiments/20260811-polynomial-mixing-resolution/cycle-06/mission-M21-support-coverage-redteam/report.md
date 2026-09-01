# Cycle 06 M21 report: dense support-coverage thresholds rejected

## 1. Exact claim, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  Put `M=binom(N,2)`.  The target `pi` is uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and the chain is exactly

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
   (1/(m-r+1)) sum_(i=1)^(m-r+1) H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

For a word `w`, let

```text
X(w)=#{v in [N]:no factor of w contains v},
T_q={w:X(w)>=q},
U_(N,m)=T_1.                                           (1.2)
```

Let `A>=1` be the universal constant in the parity-aware pointwise random-
transposition estimate audited in cycle-04 M07, and put

```text
C_*=256(A+1).                                         (1.3)
```

The proved theorem is:

> **Dense support-coverage anti-bottleneck.**  For every `N>=3`, every even
> `m` satisfying
>
> ```text
> m-2>=C_*N log(N+1),                                 (1.4)
> ```
>
> and every `1<=q<=N-2`, the cut `T_q` is nonempty and proper, is the
> smaller stationary side, and
>
> ```text
> Phi_pm^K(T_q)
> :=Q_K(T_q,T_q^c)/min{pi(T_q),pi(T_q^c)}
> >=q/[12(N-q-1)(m-2)D_N]
> >=1/(24mN^3),
> D_N=(3N^2+N-12)/2.                                  (1.5)
> ```

In particular, (1.5) rejects the missing-support union `U=T_1` and every
missing-label-count threshold in this regime.  Because `C_*` is universal,
for all sufficiently large `N` there are even lengths satisfying both (1.4)
and

```text
m<2+4 binom(N,2)log(2N),                              (1.6)
```

so this is a genuinely growing-surplus theorem inside the formerly open
intermediate window.  It is not Terminal A or Terminal B and does not
control a non-threshold refinement or a cut internal to full support.

## 2. Full proof

### 2.1 Exact global masses and all overlaps

Write

```text
Z_(d,k)=|Omega(d,k)|
```

and let `E_(d,k)` count identity words on `[d]` whose exact support is all
`[d]`.  For positive `k`, set `Z_(0,k)=Z_(1,k)=0`.  Ordinary
inclusion-exclusion gives

```text
E_(d,k)=sum_(j=0)^d (-1)^(d-j) binom(d,j)Z_(j,k).      (2.1)
```

Choosing the missing set therefore gives the exact support-layer law

```text
pi(X=s)=binom(N,s)E_(N-s,m)/Z_(N,m),                  (2.2)

pi(T_q)=
 [sum_(s=q)^(N-2) binom(N,s)E_(N-s,m)]/Z_(N,m).       (2.3)
```

In particular,

```text
pi(U)=1-E_(N,m)/Z_(N,m)
 =sum_(s=1)^N (-1)^(s+1)binom(N,s)
    Z_(N-s,m)/Z_(N,m).                                (2.4)
```

Equations (2.1)--(2.4) handle all intersections among the events `A_v`
exactly.  No union bound of their individual conductances is used.

Define the binomial factorial moments

```text
mu_q=E_pi[binom(X,q)].
```

Counting a word together with a chosen `q`-subset of its missing labels
gives the exact identity

```text
mu_q=binom(N,q)Z_(N-q,m)/Z_(N,m).                     (2.5)
```

### 2.2 The boundary layer carries at least half the threshold mass

Let `P_d` be the nonlazy uniform-transposition walk on `S_d`, put
`M_d=binom(d,2)`, and write

```text
p_d(k)=P_d^k(id,id),
Z_(d,k)=M_d^k p_d(k).                                 (2.6)
```

For even `k`, Fourier inversion gives

```text
p_d(k)=(1/d!)sum_(lambda partition d)
              (f^lambda)^2 r_lambda^k.                (2.7)
```

All summands are nonnegative.  The trivial and sign representations alone
give

```text
p_d(k)>=2/d!.                                         (2.8)
```

The parity-aware pointwise estimate underlying (1.3) gives, for
`k>=A d log(d+1)`,

```text
p_d(k)<=3/d!                                          (2.9)
```

(the audited estimate is actually `2(1+1/16)/d!`).  The cases `d=2` are
exact with `p_2(k)=1` at even `k`.

Fix `q` and put `d=N-q`.  If `d>=3`, (2.5)--(2.9) imply

```text
mu_(q+1)/mu_q
 =[d/(q+1)] Z_(d-1,m)/Z_(d,m)
 <=[3d^2/(2(q+1))][(d-2)/d]^m
 <=[3d^2/(2(q+1))]exp(-2m/d).                         (2.10)
```

Indeed, (1.4), `d<=N`, and `C_*>=512` give

```text
exp(-2m/d)<=(N+1)^(-2C_*)<=1/[3d^2],                 (2.10a)
```

so the last expression in (2.10) is at most `1/[2(q+1)]`.  The upper
return estimate is being applied at degree `d-1`, whose threshold is also
implied by (1.4); the denominator only uses (2.8).  If `d=2`, then
`Z_(1,m)=0`, so the same conclusion holds with a zero left side.

For every `s>=q+1`,

```text
binom(s,q)=[(q+1)/(s-q)]binom(s,q+1)
           <=(q+1)binom(s,q+1).                       (2.11)
```

Consequently,

```text
mu_q-pi(X=q)
 <=(q+1)mu_(q+1)
 <=mu_q/2,

pi(X=q)>=mu_q/2>=pi(T_q)/2.                           (2.12)
```

Thus the exact threshold mass cannot hide many missing-label layers away
from its one-step boundary.

### 2.3 Exact smaller-side orientation

Let `delta_d(k)` be the probability, conditional on identity return, that
the factorization graph on `[d]` is disconnected.  The audited M07
Diaconis--Shahshahani/cut calculation states that, for even
`k>=C_*d log(d+1)`,

```text
delta_d(k)<=1/[512(k+2)].                              (2.13)
```

Every word omitting a label has disconnected factorization graph on `[N]`.
Using (1.4) at length `m` gives

```text
pi(U)<=delta_N(m)<=1/[512(m+2)]<1/2.                  (2.14)
```

Since `T_q subset U`, every `T_q` is the smaller side.  This proves the
orientation rather than guessing it from an asymptotic coupon-collector
analogy.  Nonemptiness follows from an identity word supported on a fixed
`N-q` set; properness follows from a full-support identity word.  Both can
be made from doubled spanning-tree edges and extra adjacent squares because
(1.4) is even and far above their minimal required lengths.

### 2.4 Exact safe-square incidence inside the boundary layer

Condition on `X=q` and on its missing set.  The word is uniform among the
`E_(d,m)` exact-support words on the other `d=N-q` labels.

Call an adjacent equal pair **safe** if deleting it leaves exact support on
all `d` used labels.  Let `Y(w)` be the number of safe marked positions.
Deletion is a bijection between a safe marked incidence and:

1. an exact-support identity core counted by `E_(d,m-2)`;
2. one of the `M_d` transpositions on the used set; and
3. one of the `m-1` insertion gaps.

The marked gap makes the map injective even if the inserted square overlaps
another square.  Hence

```text
E[Y]=(m-1)M_d E_(d,m-2)/E_(d,m).                      (2.15)
```

Let `C_d(k)` count connected-support identity words.  Connected support is
exact support, so

```text
E_(d,m-2)>=C_d(m-2)
          =Z_(d,m-2)[1-delta_d(m-2)],
E_(d,m)<=Z_(d,m).                                     (2.16)
```

The assumption (1.4) implies the hypothesis of (2.13) for `d` at length
`m-2`.  Also (2.7) shows

```text
p_d(m-2)>=p_d(m)                                      (2.17)
```

because both exponents are even and `|r_lambda|<=1`.  Since `Y<=m-1`,
(2.6) and (2.13)--(2.17) give

```text
Pr(Y>=1)
 >=M_d E_(d,m-2)/E_(d,m)
 >=[1-delta_d(m-2)]/M_d
 >=1/(2M_d).                                          (2.18)
```

For `d=2`, the support is exactly one edge and (2.18) holds directly.

### 2.5 Exact H3 crossing probability and complete K flow

On a state certified by `Y>=1`, select the first safe square `e,e`.  If it
is not the final pair, use the `H_3` window beginning at it; if it is final,
use the window ending at position `m`.  For the padding transposition `a`,
use respectively

```text
(e,e,a)->(f,f,a),       (a,e,e)->(a,f,f).              (2.19)
```

Choose `f` with one endpoint in the missing set and one in the used set.
There are exactly `qd` such transpositions.  The deleted-square core still
uses every old label, and `f` introduces one missing label, so every outcome
has exactly `q-1` missing labels and lies in `T_q^c`.

For completeness, the length-three transposition fiber of a transposition
product has exact size

```text
D_N=M+3[2(N-2)]+2binom(N-2,2)
   =(3N^2+N-12)/2.                                    (2.20)
```

Indeed, after choosing the third transposition, the first two multiply to
the identity, a 3-cycle, or a double transposition, with respectively
`M`, three, or two ordered factorizations.  All `qd` outcomes in (2.19) are
therefore distinct members of the same conditional fiber.

Under (1.4), `R_m={3,4,5}`.  Including the outer laziness, block-size scan,
window scan, and uniform conditional fiber, every certified word satisfies

```text
K(w,T_q^c)>=qd/[2*3*(m-2)D_N].                        (2.21)
```

For each `r`, write its exact boundary contribution as

```text
Q_r(T_q,T_q^c)
 =pi(T_q)/[2|R_m|(m-r+1)]
   E_(w|T_q)[sum_(i=1)^(m-r+1)H_(i,r)(w,T_q^c)].      (2.22)
```

Laziness contributes zero and

```text
Q_K(T_q,T_q^c)=Q_3+Q_4+Q_5.                           (2.23)
```

The last two terms are nonnegative and remain part of the full boundary
flow.  Applying (2.12), (2.18), and (2.21) to the `r=3` term yields

```text
Q_K(T_q,T_q^c)
 >=pi(T_q)[1/2][1/(2M_d)]
       [qd/(6(m-2)D_N)]
 =pi(T_q)q/[12(d-1)(m-2)D_N].                        (2.24)
```

By (2.14), `pi(T_q)` is the exact smaller-side mass.  Divide (2.24) by it,
put `d=N-q`, and obtain the first inequality of (1.5).  Finally,

```text
q>=1,  d-1<=N,  m-2<=m,  D_N<=2N^2
```

give the second inequality.

## 3. Worst probability, runtime, path, and congestion accounting

- The exact boundary layer has conditional mass at least `1/2` inside every
  `T_q`.
- Conditional on that layer, a safe adjacent square occurs with probability
  at least `1/[2binom(N-q,2)]`.
- Conditional on certification, the summed specified original-`K` exit
  probability is exactly lower-bounded by
  `q(N-q)/[6(m-2)D_N]`.
- Every witness is a single original-`K` transition.  There is no comparison
  path and no congestion factor.
- Missing labels and occurrence counts can be found in `O(N+m)` time; a safe
  square can be selected in `O(m)`, and its at most `q(N-q)<=M` displayed
  exits can be listed in `O(N^2)`.  The exact local sampler remains
  polynomial in `N,m`.
- The theorem is a conductance statement for named cuts, not a global mixing
  theorem or an arbitrary-cut gap bound.

## 4. Dependencies with status

- **PROVED HERE:** exact inclusion-exclusion and factorial moments, the
  boundary-layer estimate, exact smaller-side use, safe-square incidence,
  return monotonicity, the boundary-safe transition, exact `D_N`, all kernel
  factors, and full stationary-flow accounting.
- **INHERITED PROVED:** heat-bath reversibility/stationarity and the cycle-04
  M07 deductions (2.9) and (2.13).
- **CITED WITH HYPOTHESES AND NORMALIZATION CHECKED IN M07:** P. Diaconis and
  M. Shahshahani, *Generating a random permutation with random
  transpositions*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981),
  Lemma 14 equation (3.1), the zone estimates (3.2), (3.3), (3.5), (3.7),
  and (3.13), and their collection in the proof of Theorem 1.  M07
  translates their with-replacement lazy transform to the parity-aware
  nonlazy transposition ratios used here.
- **NOT USED:** component-layer unimodality, independence of missing-label
  events, fixed-genus pendant asymptotics, a canonical hub, finite spectra,
  or an auxiliary-chain slowdown.
- **EMPIRICAL/COMPUTATIONAL DEPENDENCIES:** none.

## 5. First unproved standalone proposition

> **LOW-DENSITY COVERAGE-THRESHOLD CONDUCTANCE.**  There are universal
> constants `c>0,C<infinity` such that for every `N>=3`, every even `m>=4`
> with
>
> ```text
> m-2<C_*N log(N+1),
> ```
>
> and every `1<=q<=N-2` for which `T_q` and `T_q^c` are nonempty,
>
> ```text
> Phi_pm^K(T_q)>=c(Nm)^(-C).
> ```
>
> Alternatively, exhibit an explicit infinite sequence of such parameters
> and thresholds with superpolynomially small full-`K` conductance, including
> exact masses and all `r=3,4,5` boundary flow.

This is narrower than the previous missing-label-union proposition: the
entire parity-mixed tail is now proved, uniformly in the threshold `q`.

## 6. Strongest self-attack and Terminal-B audit

The proof uses pointwise parity mixing both to orient the cut and to show
that safe squares have adequate mass.  The universal constant `C_*` is very
conservative.  Below that threshold, failure of either displayed estimate
would only invalidate this proof; it would not show small conductance.

Even the full low-density proposition in Section 5 would reject only nested
support-coverage cuts.  It would not control arbitrary unions of support
sets, support partitions with no isolated labels, or cuts internal to a
full-support macro-fiber.  No infinite family with superpolynomial full-`K`
conductance survived this mission, so Terminal B is not claimed.

## 7. Calibration

- Odd `m` gives an empty bridge.  At `m=0`, the state is singleton and all
  labels are missing.  For `N=2` and even `m`, the state is singleton with
  full support.  The excluded `m=2,N>=3` regime does not have the required
  local chain and some coverage cuts are improper.
- At `S_3,m=4`, `Z_(3,4)=27`, `E_(2,4)=1`, and
  `pi(U)=3/27=1/9`.  The three fixed-label events are disjoint.
- At `S_4,m=4`, inclusion-exclusion gives

  ```text
  E_(4,4)=120-4*27+6=18,
  pi(U)=102/120=17/20,
  pi(X=1)=96/120,  pi(X=2)=6/120.
  ```

  Here `R_m={3,4}` and `H_(1,4)` is a whole-word heat bath of kernel weight
  `1/4`; its boundary contribution alone gives every proper cut two-sided
  conductance at least `1/8`.  It is not silently omitted.
- At `S_4,m=6`,

  ```text
  E_(4,6)=3936-4*243+6=2970,
  pi(U)=966/3936=161/656,
  pi(X=1)=960/3936,  pi(X=2)=6/3936.
  ```

  Thus the overlap correction is visible exactly: the sum of the four
  fixed-label event sizes is `4*243=972`, whereas their union has size 966.
- The counts `27/120/3936` and their `4/13/17` pure-Hurwitz components are
  consistent but no Hurwitz-orbit uniformity is used.
- Near-minimal doubled-tree words lie below (1.4); they are calibration for
  the remaining low-density proposition, not counterexamples to the dense
  theorem.  Disjoint support components retain their ordered color
  interleavings throughout the exact word counts.
- No degree-parity or edge-multiplicity-parity characterization, no failed
  length-two simulation, and no fixed canonical hub enters the proof.

## 8. Artifacts and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M21-support-coverage-redteam/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M21-support-coverage-redteam/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M21-support-coverage-redteam/report.md
```

No computation was used.  Reproduction consists of checking the exact
inclusion-exclusion/factorial-moment identities, the cited parity-aware
return bounds, the marked insertion/deletion bijection, and equations
(2.20)--(2.24).  The repository base commit is
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

This verdict applies to the dense support-coverage threshold theorem (1.5),
not to either global terminal outcome.
