# M33 final report: polynomial leakage through radius `N log N/100`

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  Let

```text
N>=10^6,                    M=binom(N,2),
d=N-1,                      E=binom(d,2),
m=4N^3+4,                   A_N=floor(N log(N+1)/100),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

The target is the global uniform identity bridge law.  The original chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1}H_{i,r},                       (1.2)
```

where every heat bath is exactly uniform on its same-ordered-product fiber.

**Theorem (proved).**  Simultaneously for every integer `1<=a<=A_N`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,                       (1.3)
Phi_pm^K(V^(a))>=N^(-25).                              (1.4)
```

In particular, the explicit endpoint sequence `a_N=A_N` obeys

```text
a_N/log N -> infinity,                                 (1.5)
```

and is not a Terminal-B bottleneck.  This advances the anti-bottleneck range
from M31's `O(log N)` to `Theta(N log N)`.  It does not reach the prioritized
`Theta(N^2/log N)` radius and is not a global mixing theorem.

## 2. Full argument

### 2.1 Minimal product-cluster encoding of the full shell

Fix a nontrivial bipartition `P`, let `H_P` be its direct-product subgroup,
and let `e=e(P)` and `x=M-e` be its internal and crossing transposition
counts.  Take a path of at most `a` local updates from a disconnected word
and choose `P` between initial support components.  As in M31, overlap-
connected update windows form active hulls whose products lie in `H_P`.

Shrink each active hull to the interval from its first crossing factor to its
last.  The removed prefix and suffix consist of internal factors, so the
shrunken product remains in `H_P`.  If its length is `l`, assign the minimal
integer budget

```text
q=ceil((l-1)/4).                                       (2.1)
```

The original overlap component using `q_0` windows had hull length at most
`4q_0+1`; hence `q<=q_0`.  Therefore the shrunken intervals are disjoint and
satisfy

```text
l in {4q-2,4q-1,4q,4q+1},             sum_j q_j<=a.   (2.2)
```

For a fixed such interval, the number of possible active blocks is at most

```text
xM^(l-2).                                               (2.3)
```

Indeed, choose the first crossing transposition and all `l-2` middle
factors.  If the last crossing is `t` and the preceding fixed product is
`L`, subgroup membership forces `t(S)=L^(-1)(S)` on either cut side `S`.
There is at most one crossing transposition with that action.

For fixed ordered lengths, the number of disjoint interval layouts is at
most `m^c/c!`.  Let

```text
R_P=M/e,                         beta_P=mx/e^2,

T_a(beta)=1+sum_{Q=1}^a sum_{c=1}^Q
 binom(Q-1,c-1)(4beta)^c/c!.                           (2.4)
```

There are `binom(Q-1,c-1)` ordered positive budget compositions and four
length choices per block.  After the blocks are fixed, all outside internal
segments combine because their transposition sum is central in `H_P`.
Cauchy--Schwarz between the two adjacent even times and the frozen dense
direct-product trace estimate give at most `4e^(m-L)/|H_P|`, uniformly in the
required endpoint.  Its density hypothesis holds because `L<=5a<<m`.
Using `L-2c<=4Q<=4a`, the complete set of words charged to `P` is bounded by

```text
O_P(a)<=4 e^m/|H_P| R_P^(4a)T_a(beta_P).              (2.5)
```

This exact interval-layout factor, including `1/c!`, is the first point at
which the proof improves on M31's `C_0^a` estimate.

### 2.2 Exact two-crossing excursions realize the same layout entropy

Now fix the isolate cut `P_z={z}|[d]`, so `x=d`, `e=E`, and
`H_{P_z}=S_d`.  Choose intervals as in (2.2), with at least two internal
positions between consecutive intervals and at least four internal positions
after the rightmost interval.

At one interval, choose a first crossing `s=(z,i)`.  Fill the `l-2` middle
positions with internal transpositions whose product is `g`, and put

```text
t=g^(-1)sg                                             (2.6)
```

at the last position.  This is another crossing transposition and

```text
s g t=s g(g^(-1)sg)=g.                                (2.7)
```

Thus the excursion block has the same ordered product as its internal middle
word.  Deleting every pair of crossing coordinates from the full source
leaves an *internal skeleton*, and (2.7) says that the full word product is
exactly the skeleton product.

Every block in (2.6) is removable in `q` positive updates.  If its two
crossings are more than four positions apart, a same-product `H_5` outcome
changes

```text
(a_1,a_2,a_3,a_4,t)
 ->((a_1a_2a_3a_4)t(a_1a_2a_3a_4)^(-1),
    a_1,a_2,a_3,a_4),                                  (2.8)
```

moving the last crossing four positions left while retaining internal
factors elsewhere.  After `q-1` such moves, both crossings lie in a window of
length at most five whose product is internal.  Its permutation has internal
transposition length at most the window length and the same parity, so a
minimal internal factorization padded by adjacent squares gives an internal
same-length replacement.  If the crossing span has length two, use one of the
reserved following internal positions in an `H_3`.  This is not a length-two
update.  Reversing these positive heat-bath adjacencies proves that all source
words with total budget at most `a` lie in the actual `V^(a)`.

### 2.3 Distinct excursion states prevent shortening regroupings

The fact that a subgroup-valued interval cannot contain exactly one crossing
is insufficient: three crossings can multiply into the isolate subgroup.
The following product-rigidity condition handles this explicitly.

Fix the internal skeleton and interval layout.  Let `P_j in S_d` be the
prefix product before block `j`.  It is determined by the skeleton and is
independent of the first-crossing choices, because (2.7) makes every complete
block product internal.  While the prefix lies between the two crossings of
block `j`, its image of `z` is

```text
y_j=P_j(i_j) in [d];                                   (2.9)
```

outside every excursion it is `z`.  Choose the `i_j` so that all `y_j` are
distinct.  Since each `P_j` permutes `[d]`, the number of choices is exactly

```text
(d)_c=d(d-1)...(d-c+1).                                (2.10)
```

For a contiguous subword `W` beginning and ending with crossing factors,
`W in S_d` exactly when the prefix image of `z` before `W` equals its image
after `W`.  The possible states are `z` and the distinct `y_j`.  Therefore an
`S_d`-valued crossing interval must begin at the first crossing of one block
and end at the second crossing of a later block.  In particular, it contains
whole consecutive excursion pairs.  The alternative pattern beginning with
a second crossing and ending with a later first crossing would require
`y_j=y_k` and is excluded.

If one active update cluster contains consecutive source blocks whose
budgets sum to `Q`, its hull length is at least

```text
sum_j(4q_j-2)+2(number_of_blocks-1)=4Q-2.              (2.11)
```

Since `r` overlapping windows of lengths at most five span at most `4r+1`,
the cluster needs at least `Q` updates.  Thus no regrouping of distinct source
pairs reduces their total budget.

### 2.4 Robust identity skeletons

Call a length-`k` identity word on `[d]` *`a`-robust* if deleting the union of
any at most `a` intervals of length at most five leaves connected support on
`[d]`.  Here

```text
k=m-2c>=m-2a.                                          (2.12)
```

The even identity-return count is at least `2E^k/d!`.  If a word is not
robust, choose a cut disconnected after deleting the witness windows.
Extending shorter intervals to five positions and discarding the endpoint
condition gives at most

```text
k^a 2^d E^(5a)[E(1-2/d)]^(k-5a)                       (2.13)
```

bad words.  Relative to `E^k/d!`, its logarithm is at most

```text
a log k+d log 2+log(d!)-2(k-5a)/d<=-N^2               (2.14)
```

for `N>=10^6` and `a<=A_N`.  Hence every layout has at least

```text
E^(m-2c)/d!                                            (2.15)
```

robust identity skeletons.

Erasing crossing coordinates maps the intersection of any global
length-five window with the skeleton to one contiguous skeleton interval.
This remains true when the window contains several crossing coordinates:
erasure simply closes those gaps in the ordered sequence.

### 2.5 Exact boundary-source count

Fix total budget exactly `a`.  For ordered positive `q_1+...+q_c=a`, choose
one of the four lengths in (2.2) for every block.  With two-position internal
gaps and four trailing positions, the exact stars-and-bars layout count is

```text
binom(m-L-c-2,c)>=(m-8a)^c/c!.                         (2.16)
```

The lower bound uses `L<=5a` and `c<=a`.

Put

```text
beta=md/E^2,                    beta_-=(m-8a)d/E^2,
eta_c=(d)_c/d^c,                C=ceil(2sqrt(80a)),

S_a=sum_{c=1}^{min(a,C)}
 binom(a-1,c-1)(4beta_-)^c eta_c/c!.                  (2.17)
```

Equations (2.10), (2.15), and (2.16) show that the number `B_a` of these
distinct source words is at least

```text
B_a>=E^m/d! S_a.                                       (2.18)
```

There is no path-history multiplicity in this count.  The word itself reveals
its ordered crossing positions; consecutive crossings determine the source
pairs, their lengths determine the `q_j`, erasing them recovers the skeleton,
and the first crossing choices remain visible.

### 2.6 One genuine `H_5` move leaves the shell

In a source counted by (2.18), push the rightmost last crossing through the
four reserved trailing internal factors using one `H_5` outcome.  The
internal skeleton and excursion state do not change, while that pair's span
increases by four.

Suppose the target belonged to `V^(a)`.  Delete the update windows of a
hypothetical path from a disconnected word and choose a cut between its
initial components.  By (2.14), the remaining skeleton support on `[d]` is
connected.  All its undeleted factors are internal to the hypothetical cut,
so `[d]` lies on one side and the cut must be `{z}|[d]`.

Shrink the hypothetical active clusters to their first and last crossings.
Product rigidity from Section 2.3 makes each cluster a union of whole
consecutive source pairs.  A group not containing the extended rightmost pair
still costs at least the sum of its `q_j` by (2.11).  A group containing that
pair has hull length at least `4Q+2`, so even `Q` windows, whose maximum span
is `4Q+1`, do not suffice.  Summing over the cluster partition gives at least

```text
sum_j q_j+1=a+1                                        (2.19)
```

updates, a contradiction.  Thus every specified target is outside `V^(a)`.

A length-five fixed-product fiber has at most `M^4` words.  Including the
lazy factor, uniform choice among three block sizes, scan normalization, and
the exact heat bath, each source has exit probability at least

```text
p_exit=1/[6(m-4)M^4].                                  (2.20)
```

### 2.7 The exact-`a` coefficient dominates the cumulative shell coefficient

For the isolate cut, direct algebra gives

```text
beta<=20,                         lambda=4beta<=80.     (2.21)
```

Define

```text
w_{a,c}(lambda)=binom(a-1,c-1)lambda^c/c!.             (2.22)
```

For `c<=C<=d/2`, `log(1-u)>=-2u` on `[0,1/2]` gives

```text
eta_c>=exp(-C^2/d)>=N^(-5).                            (2.23)
```

Moreover,

```text
(beta/beta_-)^c<e                                      (2.24)
```

uniformly for `c<=C`, since its logarithm is at most `16aC/m`.
For `c>=C`,

```text
w_{a,c+1}(lambda)/w_{a,c}(lambda)
 =lambda(a-c)/[c(c+1)]<=1/4.                           (2.25)
```

Thus the omitted large-`c` tail is at most one third of its `c=C` term, and

```text
sum_{c=1}^a w_{a,c}(4beta)<=N^6 S_a.                  (2.26)
```

For every `Q<=a`,
`binom(Q-1,c-1)<=binom(a-1,c-1)`.  Summing the at most `a` possible total
budgets and using `a<=N^2` gives

```text
T_a(beta)<=N^9 S_a.                                   (2.27)
```

Finally,

```text
(M/E)^(4a)
 =[N/(N-2)]^(4a)
 <=exp(8a/(N-2))<=N^(1/10).                           (2.28)
```

Equations (2.5), (2.18), and (2.27)--(2.28), summed over the `N` isolate
cuts, show that their total contribution to `V^(a)` is at most `N^11B_a`.

### 2.8 Non-isolate cuts remain negligible

Let the smaller cut side have size `2<=s<=N/2`.  Then

```text
beta_P<=200s,                   M/e<=5/2,              (2.29)
E-e=(s-1)(N-s-1),              m/E>=8N.               (2.30)
```

The elementary Bessel-series estimate

```text
T_a(beta_P)
 <=1+sqrt(800sa) exp(2sqrt(800sa))                    (2.31)
```

follows by using
`binom(Q-1,c-1)<=a^(c-1)/(c-1)!` and
`sum_c c y^c/(c!)^2<=sqrt(y)exp(2sqrt(y))`.

Relative to the isolate base `E^m/d!`, the logarithm of the contribution at
size `s` is at most

```text
2s log N
-8N(s-1)(N-s-1)
+4a log(5/2)
+2sqrt(800sa)+O(log(Na)).                              (2.32)
```

For `N>=10^6` and `a<=A_N`, this is at most `-N^2`; the negative term is at
least `8N(N-3)`, while all displayed positive terms together are
`O(N log N)`.  Summing all sizes leaves less than `E^m/d!`, which is itself
smaller than `B_a` because the `c=1` term in (2.17) exceeds one.  Combining
with the isolate estimate yields the deliberately rounded comparison

```text
|V^(a)|<=N^12 B_a.                                     (2.33)
```

### 2.9 Global orientation and full boundary flow

For orientation, use (2.5) directly.  The same Bessel estimate with
`beta<=20`, together with (2.28), gives

```text
|V^(a)|
 <=[4N N^(1/10)
    {1+sqrt(80a)exp(2sqrt(80a))}+1]E^m/d!.             (2.34)
```

The final `+1` absorbs every non-isolate cut.  Since

```text
|Omega(N,m)|>=2M^m/N!,               E/M=1-2/N,        (2.35)
```

division in (2.34) gives

```text
pi(V^(a))<=exp(-4N^2)<1/2.                             (2.36)
```

Indeed the negative term `m log(1-2/N)<=-2m/N` is at most `-8N^2`, while
all positive logarithms in (2.34) are `o(N^2)` uniformly in the range.

For `r=3,4,5`, write

```text
Q_r(A,A^c)
 =1/[6(m-r+1)|Omega|]
   sum_{w in A}sum_i H_{i,r}(w,A^c).                   (2.37)
```

Then the lazy identity has no boundary flow and

```text
Q_K=Q_3+Q_4+Q_5.                                      (2.38)
```

Retain only the `B_a` sources and their specified `Q_5` exits.  Every other
term in (2.38) is nonnegative.  Equations (2.20), (2.33), and (2.36) give

```text
Phi_pm^K(V^(a))
 >=N^(-12)/[6(m-4)M^4]
 >=N^(-25),                                            (2.39)
```

using `m-4=4N^3`, `M<=N^2`, and `24<=N^2`.  This proves
(1.3)--(1.4).

## 3. Probability, runtime, path length, and congestion accounting

- Actual-shell mass: at most `exp(-4N^2)` for every `a<=A_N`.
- Boundary-source count: the exact lower bound (2.18), including layouts,
  robust skeletons, and distinct excursion states.
- Source path: exactly `sum q_j=a` positive local updates from an all-internal
  identity word.  Length-two spans use a padded `H_3`.
- Exit: one genuine `H_5` outcome, probability at least
  `1/[6(m-4)M^4]` in the original chain.
- Full conductance: at least `N^-25`, uniformly through radius `A_N`.
- No canonical path, hub, flow congestion, or comparison-chain simulation is
  used.  The shifts only identify outcomes inside actual heat-bath fibers.
- Given a source certificate, its product, budget, distinct-state condition,
  and exit are verified in `O(Nm+a)` elementary permutation operations.
  Naively checking robustness is exponential in `a`; no efficient source-set
  recognition algorithm is asserted or required by the enumerative flow
  proof.
- The inherited exact `r<=5` block sampler has polynomial per-step cost in
  `N,m`.

## 4. Dependencies and statuses

1. **Proved here:** minimal cluster encoding, exact excursion elimination,
   product rigidity, source injectivity, robust-skeleton count, coefficient
   comparison, non-isolate suppression, target exclusion, orientation, and
   conductance.
2. **Proved in M31 and rederived here:** overlap-cluster product invariance
   and the forced-last-crossing count.
3. **Proved/frozen in Cycle-02 M12:** dense direct-product trace upper bounds
   and parity-coset identity-return lower bounds, with all density hypotheses
   checked here.
4. **Inherited proved:** exact heat-bath reversibility, stationarity, global
   irreducibility, and polynomial exact block sampling.
5. **Not used:** conductance monotonicity, support-only distance, crossing
   parity, canonical hubs, restriction gaps, finite spectra, or an `L=2`
   simulation.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **QUADRATIC-SCALE SHELL ACTION.**  There are universal `c,C>0` such that,
> for `m=4N^3+4` and every proper shell with
> `1<=a<=cN^2/log(N+1)`, one has
> `Phi_pm^K(V^(a))>=N^-C`.

The present exact-two-crossing source loses
`(M/E)^(4a)=exp(O(a/N))`.  It is polynomial through `a=O(N log N)` but
superpolynomial at the proposed quadratic-over-log scale.  Closing the named
proposition requires sources that retain the entropy of additional crossing
excursions inside active blocks, or an exact shell-layer flow recursion.

## 6. Strongest self-attack

The theorem is a substantial but still nonterminal anti-bottleneck result.
Its source family matches all interval-layout and budget-composition entropy,
but it replaces arbitrary active-block middles by internal middles.  The
resulting `exp(O(a/N))` loss is harmless at `N log N/100` and fatal at
`N^2/log N`.  Nothing here permits extrapolation past the stated range, and
conductance need not be monotone as `a` grows.

The proof also starts at the deliberately large explicit threshold
`N=10^6` to keep every analytic inequality literal.  Finite smaller `N` do
not affect (1.5), and their shell behavior is not being inferred from this
asymptotic argument.

## 7. Calibration

- Odd `m`: the bridge is empty; no theorem is asserted.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 identity words and four pure-Hurwitz components; whole-word
  `H_4` prevents extrapolating the shell statement.
- `S_4,m=4`: 120 words and 13 pure-Hurwitz components; whole-word `H_4`
  remains present.
- `S_4,m=6`: 3936 words and 17 pure-Hurwitz components; finite shell data is
  not used as proof.
- Near-minimal connected doubled trees do not satisfy the dense robust-
  skeleton estimate; `m=4N^3+4` is explicit.
- Ordered intervals and products drive both the cluster certificate and the
  excursion-state rigidity.  Color interleavings are not replaced by an
  unordered graph model.
- Three crossing factors can have internal product, so no crossing-parity or
  degree-parity shortcut is used.
- Length-two spans are handled by an actual padded `H_3`, not the false
  universal length-two simulation.
- Every cut is included in the mass bound, global orientation precedes flow
  division, and all `Q_3+Q_4+Q_5` normalizations are explicit.

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was used.  Reproduce the proof by checking:

1. minimal shrunken-cluster encoding (2.1)--(2.5);
2. excursion elimination and state rigidity (2.6)--(2.11);
3. robust skeletons and the injective source count (2.12)--(2.18);
4. the actual one-step exit (2.19)--(2.20);
5. the coefficient and cut comparisons (2.21)--(2.33); and
6. orientation and exact kernel flow (2.34)--(2.39).

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns the uniform inverse-polynomial leakage theorem through
the genuinely mesoscopic radius `N log(N+1)/100`.  It is not either global
terminal outcome.
