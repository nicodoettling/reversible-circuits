# Cycle 06 M26 report: balanced-separator union remains open at exact shell mass

## 1. Exact claims, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.
The target `pi` is uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and the exact chain is

```text
K=(1/2)I
 +(1/(2|R_m|))sum_(r in R_m)
   (1/(m-r+1))sum_(i=1)^(m-r+1)H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

Put `a=floor(N/2)`.  For a labeled set `S`, let `A_S` be the event that no
factor crosses `(S,S^c)`, and define

```text
B_(N,m)=union_(|S|=a) A_S,
C_(N,m)={w:largest support-component size<=N/2}.      (1.2)
```

No global conductance theorem or Terminal-B family is proved.  The exact
new results are:

1. **Deep support interior.**  For every `N>=24`, even `m>=4`, and

   ```text
   D_(N,m)={w:the number of used labels is at most a-10},
   ```

   every possible original-`K` outcome remains in both `B` and `C`:

   ```text
   K(w,B^c)=K(w,C^c)=0,       w in D_(N,m).            (1.3)
   ```

2. **Full-support deep interior.**  For every `N=4k>=60`, at length `m=N`,
   every word containing each edge of a perfect matching exactly twice has
   the same zero-exit property (1.3).  The family has exact size

   ```text
   W_match(N)=(N!)^2/[2^N(N/2)!].                     (1.4)
   ```

3. **Matching-mass hypothesis refuted.**  For `N=2a`, `a>=3`, `m=N`, the
   boundary profile `(a,2,1^(a-2))` has exact count `W_cap` satisfying

   ```text
   W_cap/W_match
    =4^(a-1)(a-1)a^(a-2)/a!
    >=4^(a-1)(a-1)/a^2,                              (1.5)
   ```

   and conditional original-`K` exit probability from both `B` and `C` at
   least `1/[3(N-2)D_N]`, where

   ```text
   D_N=(3N^2+N-12)/2.                                 (1.6)
   ```

Thus worst-state escape is exactly false even on full support, but the
simplest proposal that these zero-exit matching states carry the relevant
stationary mass is exponentially false.  The full union/profile cut remains
open at an exact stationary boundary-shell implication.

## 2. Full argument and construction

### 2.1 Exact overlap-free stationary masses

Let `mathcal P_N` be the labeled set partitions of `[N]`, with isolated
labels included as singleton blocks.  Let `E_P(m)` be the number of words
whose factorization graph has exact component partition `P`.  Define

```text
b(P)=1{there is a subcollection of blocks with total size a},
c(P)=1{max_(V in P)|V|<=N/2}.                         (2.1)
```

A set is a no-crossing separator exactly when it is a union of connected
components.  Therefore the exponentially overlapping union is counted
exactly once by

```text
|B|=sum_(P in mathcal P_N)b(P)E_P(m),
|C|=sum_(P in mathcal P_N)c(P)E_P(m),                 (2.2)

pi(B)=|B|/Z_(N,m),     pi(C)=|C|/Z_(N,m),             (2.3)
```

where `Z_(N,m)=|Omega(N,m)|`.  The exact smaller-side masses are

```text
min{|B|,Z_(N,m)-|B|}/Z_(N,m),
min{|C|,Z_(N,m)-|C|}/Z_(N,m).                         (2.4)
```

No inclusion multiplicity or unsupported mass orientation is hidden in
(2.2)--(2.4).

For completeness, if `F_(N,r)(g)` is the length-`r` transposition fiber of
`g`, and `w[i<-u]` denotes block replacement, the exact contribution of
each block size to either cut `A in {B,C}` is

```text
Q_r(A,A^c)
 =1/[2|R_m|(m-r+1)Z_(N,m)]
   sum_(w in A)sum_(i=1)^(m-r+1)
    #{u in F_(N,r)(t_i...t_(i+r-1)):w[i<-u] in A^c}
    /|F_(N,r)(t_i...t_(i+r-1))|,                     (2.5)

Q_K(A,A^c)=sum_(r in R_m)Q_r(A,A^c).                 (2.6)
```

Equations (2.5)--(2.6) are the full `r=3,4,5` boundary flow, including
laziness through the factor `1/2`.

### 2.2 A support-size deep interior for all lengths

Let `V(w)` be the union of endpoints of all factors.  In an `r`-block
update, the unchanged factors use labels in `V(w)`, while the new block can
introduce at most `2r` labels outside it.  Thus every output `w'` satisfies

```text
|V(w')|<=|V(w)|+2r.                                  (2.7)
```

If `w in D_(N,m)` and `r<=5`, (2.7) is at most `a`.  Hence at least
`N-a>=a` labels are isolated in `w'`.  Choose any `a` of them.  Their union
is a balanced no-crossing separator, so `w' in B`; also every nontrivial
component has size at most `|V(w')|<=a<=N/2`, so `w' in C`.  Laziness is
immediate.  This proves (1.3) simultaneously for every outcome in every
conditional fiber, not only a specified square refresh.

Let

```text
Sigma_B=B minus D_(N,m),     Sigma_C=C minus D_(N,m).
```

Because the total nonlazy kernel mass is `1/2`, (1.3) and (2.5)--(2.6)
give the exact localization and crude upper bound

```text
Q_K(B,B^c)=Q_K(Sigma_B,B^c)<=pi(Sigma_B)/2,
Q_K(C,C^c)=Q_K(Sigma_C,C^c)<=pi(Sigma_C)/2.           (2.8)
```

If `E_(s,m)` counts exact-support words on a fixed `s`-set, the deep mass is
itself explicit:

```text
pi(D_(N,m))
 =Z_(N,m)^(-1)sum_(s=2)^(a-10)binom(N,s)E_(s,m).     (2.9)
```

Thus (2.8) is an exact stationary-mass route to an upper-conductance proof,
but no asymptotic comparison of its numerator with (2.4) is assumed.

### 2.3 Full-support zero-exit matching words

Let `N=4k>=60`, `m=N`, fix a perfect matching of `[N]`, and let `w` contain
each matching edge exactly twice in arbitrary order.  Disjoint matching
edges commute and each has even multiplicity, so the ordered product is
identity.  The factorization graph is the full-support partition
`2^(N/2)`.

Consider any update with `r<=5`.  Its deleted old factors belong to at most
`r` matching pairs.  The `r` new transpositions have at most `2r` endpoints
and hence meet at most `2r` additional matching pairs.  At most `3r` of the
original pair components are affected.  Therefore at least

```text
N/2-3r>=N/2-15>=N/4                                  (2.10)
```

pair components remain completely untouched: neither their factors are
deleted nor their labels used by a new factor.  Choose `N/4` such pairs;
their union has size `N/2` and remains a no-crossing separator of the output.

All changed components lie on at most `2(3r)=6r<=30<=N/2` labels, while
untouched components have size two.  Hence the output also remains in `C`.
This proves the full-support form of (1.3).

The number of perfect matchings is
`N!/[2^(N/2)(N/2)!]`; for each matching, the number of orderings of two
copies of each edge is `N!/2^(N/2)`.  Their product is (1.4).

The overlap causing the failure of fixed-cut aggregation is already
exponential on a repeated-edge word.  The number of balanced `S` that do
not split its two used endpoints is

```text
Kappa_N=binom(N-2,a-2)+binom(N-2,a).                  (2.11)
```

For even `N=2a`,

```text
Kappa_N/binom(N,a)=(a-1)/(2a-1),                     (2.12)
```

and the analogous odd ratio is `a/(2a+1)`.  Thus one word can belong to an
asymptotic half of exponentially many fixed balanced-separator events.

### 2.4 Exact rejection of matching-state mass dominance

Now let `N=2a`, `a>=3`, and `m=N`.  Consider component profile

```text
(a,2,1^(a-2)).                                       (2.13)
```

Choose the `a` labels of the large component and the two labels of the pair
in

```text
binom(2a,a)binom(a,2)
```

ways.  The exact connected genus-zero count on the large block is

```text
C_0(a)=(2a-2)!a^(a-3),                               (2.14)
```

the pair has the unique word `(e,e)`, and there are `binom(2a,2)` color
interleavings.  Therefore

```text
W_cap(N)
 =binom(2a,a)binom(a,2)N!a^(a-3)/2.                  (2.15)
```

Dividing (2.15) by (1.4) and using `a!<=a^a` proves

```text
W_cap/W_match
 =4^(a-1)(a-1)a^(a-2)/a!
 >=4^(a-1)(a-1)/a^2.                                 (2.16)
```

The profile (2.13) lies in both cuts: the size-`a` block is itself a
balanced separator and is the largest component.  It is also a genuine
boundary profile.  Conditional on this profile, the two occurrences of its
size-two edge occupy a uniform two-subset of the `N` positions.  They are
adjacent with exact probability

```text
(N-1)/binom(N,2)=2/N.                                (2.17)
```

When adjacent, pad the square on its available side to an actual `H_3`
window.  Refresh it to `(f,f)`, where `f` joins one of the two pair labels
to one of the `a` labels in the large component.  There are `2a=N` distinct
choices.  The large connected component is unchanged, one pair vertex joins
it to form a component of size `a+1`, and the other pair vertex becomes
isolated.  The remaining `a-2` labels were already isolated.  The new profile
is

```text
(a+1,1^(a-1)),                                       (2.18)
```

which lies outside both `B` and `C`: the giant is too large and the other
blocks total only `a-1`.

For a transposition product, the exact `H_3` fiber size is (1.6).  Since
`m=N>=6`, `|R_m|=3`.  Including laziness, block-size choice, window choice,
and conditional output gives

```text
Pr(exit | profile (2.13))
 >=(2/N)[N/(2*3*(N-2)D_N)]
 =1/[3(N-2)D_N].                                     (2.19)
```

Every `r=4,5` term in (2.6) is additional nonnegative flow.  Equations
(2.16)--(2.19) prove that the selected full-support zero-exit family is
exponentially dominated by an explicitly escaping family already on the
same side of both proposed cuts.

## 3. Worst probability, runtime, path, and congestion accounting

- Deep-interior statements (1.3) have exact exit probability zero under
  the complete original kernel; no transition type is omitted.
- The boundary profile has certification probability exactly `2/N` and
  certified summed `H_3` exit probability `N/[6(N-2)D_N]`.
- Its witness has path length one and no comparison congestion.
- Component partitions and support size can be computed in `O(N+m)` time.
  Listing the `N` boundary outcomes takes `O(N^2)` arithmetic work, and the
  exact local sampler remains polynomial.
- Formula (2.5) is the exact all-window, all-fiber flow.  Formula (2.8) uses
  only the total nonlazy mass and is valid for `Q_3+Q_4+Q_5` together.
- No claim is made that exact macro sums (2.2) can be evaluated in polynomial
  time for arbitrary `N,m`; they specify stationary mass without replacing
  it by a graph-only sampling law.

## 4. Dependencies with status

- **PROVED HERE:** exact overlap-free macro masses, exact full-flow formula,
  both deep-interior theorems, matching count, overlap multiplicity, cap
  profile count and ratio, and its full-`K` exit probability.
- **INHERITED PROVED:** heat-bath reversibility/stationarity, exact `D_N`,
  minimal connected count (2.14), and polynomial exact local sampling.
- **CITED DEPENDENCIES:** none newly invoked.
- **EMPIRICAL/COMPUTATIONAL DEPENDENCIES:** none.
- **NOT USED:** union-bounding M24, graph-only edge shifts, component-count
  unimodality, dense smoothing, fixed-genus asymptotics beyond the exact
  genus-zero formula, finite spectra, or a canonical hub.

## 5. First unproved standalone proposition

> **BALANCED-PROFILE BOUNDARY-SHELL MASS AND ACTION.**  For
> `A in {B_(N,m),C_(N,m)}`, let
>
> ```text
> partial_K A={w in A:K(w,A^c)>0}.
> ```
>
> Either prove universal `c>0,C<infinity` such that, whenever `A` is a
> proper cut,
>
> ```text
> Q_K(A,A^c)>=c(Nm)^(-C)min{pi(A),pi(A^c)},           (2.20)
> ```
>
> by controlling the exact macro mass and average action on `partial_K A`,
> or exhibit an explicit infinite sequence for which the reverse inequality
> is superpolynomially small.  Every claim must use (2.2)--(2.6), not a sum
> of fixed-separator conductances.

The explicit sequence `N=4k,m=N` is the first unresolved test: (2.10)
proves a full-support zero-exit interior, while (2.16) rules out its simplest
mass-dominance argument.

## 6. Strongest self-attack and Terminal-B audit

Zero pointwise escape does not imply small conductance.  The matching words
in (1.4) are exponentially fewer than just one explicit boundary profile,
by (1.5), so presenting them alone as a bottleneck would fail the required
stationary-mass accounting.  Conversely, the cap profile does not prove a
conductance lower bound because the total mass of all other interior
profiles relative to it is unknown.

The exact shell upper bound (2.8) can prove Terminal B only after a
superpolynomial shell-to-smaller-side mass estimate.  No such estimate, and
no inverse-polynomial lower bound for the complete union/profile flow,
survived this mission.  Therefore neither terminal outcome is claimed.

## 7. Calibration

- Odd `m` gives an empty bridge; `m=0` and `N=2` are singleton regimes;
  `m=2,N>=3` is the excluded disconnected chain.
- At `S_3,m=4`, `B` is the missing-label event and has mass `3/27=1/9`.
  The largest-component cut `C` is empty because every used component has
  size at least two, greater than `3/2`.
- At `S_4,m=4`, exact profiles give 6 words of type `(2,1,1)` and 18 of type
  `(2,2)`.  Hence `B=C` has mass `24/120=1/5`.
- At `S_4,m=6`, there are 6 words of type `(2,1,1)` and 90 of type `(2,2)`;
  hence `B=C` has mass `96/3936=1/41`.  The other 960 exact-support-three
  and 2880 connected-support-four words lie outside.
- These exact counts coexist with the `4/13/17` pure-Hurwitz components; no
  pure-Hurwitz stationary law is substituted.
- At `m=4`, `H_(1,4)` is a whole-word heat bath of coefficient `1/4`, so
  every proper cut gets that complete boundary flow.  Equations (2.5)--(2.6)
  retain it.
- The full-support matching family is a near-minimal disconnected analogue
  of doubled-tree words and explicitly retains all color interleavings.
- No parity-only graph invariant, failed length-two simulation, graph-only
  model, slow finite trace, or canonical hub is used.

## 8. Artifacts and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M26-balanced-separator-union/plan.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M26-balanced-separator-union/checkpoint.md
experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M26-balanced-separator-union/report.md
```

No computation was used.  Reproduction consists of checking the support
bound (2.7), matching-pair accounting (2.10), exact factorial counts
(2.14)--(2.16), adjacency probability (2.17), and kernel factors (2.19).
Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

OPEN AT A NAMED STEP: BALANCED-PROFILE BOUNDARY-SHELL MASS AND ACTION.
