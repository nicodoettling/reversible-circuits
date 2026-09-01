# Cycle 05 M17 report: balanced two-lobe midpoint pinch

## 1. Exact quantified claim and convention

Permutations are maps on `[N]`, composition is `(pq)(x)=p(q(x))`, and a
word evaluates as `t_1...t_m`.  Let `M=binom(N,2)`, let `pi` be uniform
on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and use the original lazy kernel

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_{r in R_m}
    (1/(m-r+1)) sum_i H_{i,r},
R_m={3,4,5} intersect [m].
```

No Terminal-B family and no every-subset isoperimetric theorem was obtained.
The following explicit hidden-cut rejection is proved.

Fix `s>=1`, put `N=2s+1` and `m=4s=2N-2`.  Define `A_N` to contain
the words whose first and second length-`2s` halves are minimal connected
identity factorizations on label sets `S,T`, respectively, where

```text
|S|=|T|=s+1,  S union T=[N],  |S intersect T|=1.
```

Then `A_N` is contained in the minimal full-support macro and

```text
|A_N|
 =(2s+1) binom(2s,s)
   [(2s)!(s+1)^(s-2)]^2.                               (1.1)
```

Its exact global stationary mass is the numerator in (1.1) divided by

```text
|Omega(2s+1,4s)|
 =(1/(2s+1)!)
   sum_{lambda partition (2s+1)}
      (f^lambda)^2 c_lambda^(4s),                      (1.2)
```

where `f^lambda` is the irreducible dimension and `c_lambda` is the
Young-diagram content sum.  In particular `pi(A_N)<=1/4`.

For every `x in A_N`,

```text
K(x,A_N^c)
 >=q_s:=1/[2|R_m|(m-2)M^2].
```

Consequently

```text
Q_K(A_N,A_N^c)>=pi(A_N)q_s,
Phi_pm(A_N)>=q_s=Theta(s^-5).                           (1.3)
```

Although this temporal-articulation cut has exponentially small mass, it is
not a superpolynomial bottleneck for the full `r=3,4,5` chain.

## 2. Full proof and construction

### 2.1 Exact enumeration

Let

```text
C_(s+1)=(2s)!(s+1)^(s-2).
```

This is the checked count of minimal connected identity transposition
factorizations of length `2s` on a fixed set of `s+1` labels.  It also
gives `C_2=1` when `s=1`.

For a word in `A_N`, the supports of its displayed halves uniquely recover
the ordered pair `(S,T)`; their unique common label recovers the
articulation.  Conversely:

1. choose the articulation in `2s+1` ways;
2. choose the other `s` labels of `S` from the remaining `2s` labels;
3. choose an arbitrary minimal connected identity word on `S`;
4. independently choose one on the forced complementary support
   `T=([N] minus S) union {the articulation}`.

The two identity halves concatenate to an identity word, and their support
union is connected on all labels.  This construction is inverse to support
recovery, proving (1.1) without overcounting.

Equation (1.2) is the exact content-character formula for the identity
coefficient of the central transposition sum.  It supplies the global, rather
than macro-conditional, stationary mass.

### 2.2 Mass orientation and asymptotics

The full minimal connected macro has size

```text
|F_(2s+1)|=(4s)!(2s+1)^(2s-2).
```

Dividing (1.1) by this count gives

```text
R_s:=|A_N|/|F_(2s+1)|
 = [binom(2s,s)/binom(4s,2s)]
   [(s+1)^(2s-4)/(2s+1)^(2s-3)].                       (2.1)
```

At `s=1`, `R_1=1/4`.  For `s>=2`, the first bracket is at most one and

```text
(s+1)^(2s-4)/(2s+1)^(2s-3)
 = (1/(2s+1))((s+1)/(2s+1))^(2s-4)
 <=1/(2s+1)<=1/5.
```

Since `A_N subset F_(2s+1) subset Omega(N,m)`,

```text
pi(A_N)<=R_s<=1/4,                                     (2.2)
```

so the smaller stationary side is exactly `A_N`.

The central-binomial asymptotics give

```text
binom(2s,s)/binom(4s,2s)
 ~sqrt(2)4^(-s).
```

Also,

```text
(s+1)^(2s-4)/(2s+1)^(2s-3)
 =[(2s+1)^3/(s+1)^4]
  [(s+1)/(2s+1)]^(2s)
 ~(8e/s)4^(-s).
```

Therefore

```text
R_s ~(8 sqrt(2)e/s)16^(-s).                            (2.3)
```

This quantifies the tempting rare-mass signal but does not infer low
conductance from it.

### 2.3 One exact midpoint exit from every state

Take `x in A_N`.  Let `a=t_(2s)` be the last factor of the left half and
`b=t_(2s+1)` the first factor of the right half.  The equality `a=b` is
impossible: both endpoints of that common edge would belong to
`S intersect T`, contradicting `|S intersect T|=1`.

Let `P=t_1...t_(2s-1)`.  The left half has product identity, so

```text
Pa=id,  hence P=a.
```

Apply the right Hurwitz move at the midpoint,

```text
(a,b)->(b,bab).
```

It preserves the ordered pair product because `b(bab)=ab`.  It is a
positive outcome of the legal length-three window beginning at position
`2s`, with position `2s+2` retained.  This window exists even at
`s=1`, where it is positions `2,3,4`.

The new midpoint prefix is

```text
Pb=ab!=id,
```

because distinct transpositions cannot have identity product.  Thus the
output is not in `A_N`, regardless of its new support geometry.

A length-three same-product fiber has at most `M^2` elements: choosing its
first two factors determines the third permutation uniquely.  Hence the
specified transition has probability at least

```text
q_s
 =(1/2)(1/|R_m|)(1/(m-2))(1/M^2),                      (2.4)
```

where the factors are respectively the nontrivial half of `K`, block-size
scan, length-three window scan, and conditional outcome.

Averaging (2.4) over `A_N` proves the boundary-flow inequality in (1.3).
By (2.2), division by the smaller stationary mass gives
`Phi_pm(A_N)>=q_s`.  For `s>=2`, `|R_m|=3`,
`M=s(2s+1)`, and `m-2=4s-2`, so

```text
q_s=1/[6(4s-2)s^2(2s+1)^2] ~1/(96s^5).
```

This is an inverse polynomial.  All `r=4,5` transitions contribute
nonnegative additional flow.  For `s=1`, `R_m={3,4}` and the whole-word
`H_4` term is retained.

## 3. Worst-case probability, runtime, path, and congestion accounting

- Every state of the cut has the single length-three exit (2.4); there is no
  exceptional or merely average subset.
- The exact scan probability is
  `1/[2|R_m|(m-2)]`; the specified conditional outcome is at least
  `M^-2`.
- Duplicate targets and all uncounted block outcomes only increase boundary
  flow.  No cancellation is possible because stationary flows are
  nonnegative.
- Constructing the Hurwitz output costs `O(1)` permutation-edge operations.
  Enumerating an exact length-three fiber uses at most `M^2` candidates,
  polynomial in `N,m`.
- The proof uses one transition, no comparison path and no canonical state.
  Path length is one and there is no congestion claim.
- The deterministic verifier generates the six `N=3` and 17,280 `N=5`
  cut states, checks every certificate, evaluates the full `N=3` kernel,
  and computes exact formula cases through `N=21`.  The recorded internal
  runtime is about 0.34 seconds.  This computation can falsify the formulas
  but is not their universal proof.

## 4. Dependencies with status

1. **CITED AND CHECKED:** the minimal connected identity count
   `(2v-2)!v^(v-3)`, already used and convention-checked in the project.
2. **PROVED HERE:** uniqueness and count of the ordered two-lobe
   decomposition, exact mass orientation, asymptotic (2.3), midpoint
   Hurwitz exit, and every `K` normalization.
3. **PROVED INHERITED:** uniform global stationarity and reversibility,
   arbitrary-endpoint aligned-fiber connectivity, polynomial Hurwitz
   diameter, trivial normal braid quotients, and the earlier macro/star cut
   rejections.  They are context, not dependencies of the exit proof.
4. **EXACT FINITE:** all entries in `results.json`, including full
   forward/reverse `N=3` flows and the 27/120/3936 counts.
5. **CONDITIONAL/OPEN:** inverse-polynomial original-`K` expansion for every
   subset of the minimal full-support macro.
6. **EMPIRICAL:** none; floating values only render exact integers or
   fractions and illustrate the proved asymptotic.

## 5. First standalone unproved proposition

> **Full embedded minimal-macro isoperimetry.**  There exist universal
> `c>0,C<infinity` such that, for `m=2N-2`, every `N>=3`, and every
> nonempty `A subset F_N` with `|A|<=|Omega(N,m)|/2`,
>
> ```text
> (1/|A|) sum_{x in A} K_(N,m)(x,Omega(N,m) minus A)
> >=cN^(-C).                                            (5.1)
> ```

A superpolynomially small family in (5.1) would be a literal Terminal-B
conductance construction for the original chain.  A polynomial Hurwitz
diameter does not prove (5.1): exponentially many source-target routes may
coalesce on a tiny-capacity interface.  Trivial normal quotients do not prove
it either because the orbit stabilizer is nonnormal.  Conversely, a slow
Hurwitz-only cut would not refute `K`, whose `H_4,H_5` outcomes may cross
it.

## 6. Strongest self-attack

The theorem rejects only a rigid renewal geometry: both halves individually
return to identity and have connected supports meeting at one articulation.
An arbitrary nonnormal barbell can avoid a clean midpoint renewal and can
spread its interface across many prefix products or map configurations.
Nothing here bounds the boundary of such a subset.

The very small mass in (2.3) is not evidence for slow mixing.  The proof
correctly divides the boundary flow by that same mass, leaving the
inverse-polynomial rate (2.4).  This is the principal self-attack against
using rare indexed-map shapes as candidate bottlenecks.

The exact calculation is not extrapolated.  No Terminal-A or Terminal-B
claim is made.

## 7. Calibration results

- Odd identity length is empty; `m=0` and `N=2` are singleton cases;
  original `m=2` is excluded.  Here `m=4s` is even and at least four.
- `S_3,m=4`: the verifier finds 27 identity words and six two-lobe states.
  Their exact mass is `2/9`.  The `r=3` and whole-word `r=4` flows are
  each `7/162`, total flow is `7/81`, forward and reverse flows agree,
  and conductance is `7/18`.  The known four Hurwitz components are not
  treated as global components of `K`.
- `S_4,m=4` and `S_4,m=6`: the character calculation reproduces 120 and
  3936 states, with 13 and 17 pure-Hurwitz components respectively.  These
  even-`N` cases are not members of the odd-`N` two-lobe family.
- `S_5,m=8`: the verifier generates exactly 17,280 distinct cut states,
  all with valid midpoint exits; `pi(A)=864/88547` and
  `q_2=1/3600`.
- Formula cases through `N=21` satisfy the exact count, and
  `s16^s|A|/|F|` approaches the proved limit `8sqrt(2)e`.
- Ordered halves, label sets, the articulation, multiplication convention,
  both midpoint orientations, conditional multiplicities, laziness, and
  block-size/window scans are explicit.
- No parity characterization, fixed canonical hub, raw uniform-tree law,
  leaf-square cut, first-edge star, or modified chain is used.

## 8. Artifacts and reproduction command

Owned files:

- `plan.md`;
- `checkpoint.md`;
- `two_lobe_check.py`;
- `results.json`;
- this `report.md`.

Run from the repository root:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M17-embedded-isoperimetry/two_lobe_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M17-embedded-isoperimetry/results.json
```

The run uses Python `3.12.3`, no random seed or nonstandard dependency, and
records commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, the exact command,
runtime, target distribution, kernel, and named universal falsifier.

## 9. Verdict

PROVED

This verdict applies to the exact count, mass asymptotic, and full-`K`
rejection of the balanced two-lobe midpoint-pinch cut.  The terminal
polynomial-mixing question remains open at (5.1).
