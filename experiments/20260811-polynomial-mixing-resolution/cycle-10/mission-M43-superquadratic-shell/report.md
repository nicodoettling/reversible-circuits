# M43 final report: canonical renewal closes a linear shell range

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))` and evaluate a word as `t_1...t_m`.  Let

```text
N>=10^12,                         M=binom(N,2),
d=N-1,                            E=binom(d,2),
m=4N^3+4,                         a_*=floor(m/10^8),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

The target is the global uniform identity bridge.  The literal chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1}H_{i,r},                       (1.2)
```

where `H_{i,r}` is the exact uniform length-`r` same-ordered-product heat
bath.

**Theorem (proved).**  Simultaneously for every integer `0<=a<=a_*`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,                       (1.3)
Phi_pm^K(V^(a))>=N^(-25).                              (1.4)
```

Here `Phi_pm(A)=Q_K(A,A^c)/min(pi(A),pi(A^c))`.  This is a literal
small-constant linear-radius anti-bottleneck theorem.  In particular it
contains `a=N^(2+delta)` for every fixed `delta<1` and all sufficiently large
`N`.  It is not a global spectral-gap theorem.

## 2. Full argument

### 2.1 Canonical primitive excursions

Fix an isolate `z` and put `H=Stab(z)=S_d`.  Track

```text
X_j=(t_1...t_j)^(-1)(z).                               (2.1)
```

When `X_j=z`, an internal transposition keeps the state at `z` and a crossing
transposition leaves it.  From a state in `[d]`, exactly one transposition
returns it to `z`.  Since a word in `Omega(N,m)` ends at `X_m=z`, its
crossing factors have a unique decomposition into primitive excursions.

Write their lengths `l_1,...,l_c>=2`; write the counts of internal factors
before, between, and after them as `g_0,...,g_c`.  Define

```text
q_j=ceil((l_j-1)/4),          Q=sum_j q_j,
h=#{j in [c-1]:g_j<=2},       k=c-h,
p=Q-h.                                                 (2.2)
```

Thus `k` is the number of maximal groups separated by internal gaps of length
at least three.

### 2.2 The segmentation inequality

**Lemma 2.1.**  If a word `w` is reached from an `H`-internal word in at most
`a` original updates, then

```text
p=Q-h<=a.                                               (2.3)
```

*Proof.*  Decompose the union of all update windows in the path into
overlap-connected hulls.  A component containing `u` windows has span at
most `5+4(u-1)=4u+1`.  Its target product equals its starting product and
therefore belongs to `H`.  Every crossing target factor lies in one of these
hulls.

Shrink each hull to its first and last crossing; removed factors are
internal, so the shrunken product remains in `H`.  The globally first hull
starts at the first departure from `z`.  Subgroup product forces its endpoint
to occur at a return to `z`.  Inducting from left to right shows that the
shrunken hulls partition the canonical primitive excursions into consecutive
groups.  This ordered-first-uncovered argument is essential: an arbitrary
interval starting while `X_j!=z` need not have this property.

For `q(L)=ceil((L-1)/4)`, direct use of `L>=4q(L)-2` gives

```text
q(L_1+g+L_2)>=q(L_1)+q(L_2)-1_{g<=2}.                 (2.4)
```

Indeed a gap of at least three loses nothing, while a shorter gap loses at
most one.  Iterating within every hull says that its required number of
windows is at least the sum of its primitive `q_j` minus its short gaps.
Summing the hulls proves (2.3). `square`

For the clean source used below all inter-excursion gaps are at least three,
so (2.3) is sharp.  The inherited three/four/five-factor zipper makes each
primitive excursion internal in exactly `q_j` genuine local updates, using
the following gap for the length-two residue.  Hence a clean source with
`Q=a` lies in the literal `V^(a)`.

### 2.3 Exact primitive and internal counts

For a primitive excursion of length `l`, choose the first crossing in `d`
ways.  At every one of the `l-2` middle steps exactly `M-1` choices avoid an
early return, and the final return crossing is unique.  Therefore its exact
count is

```text
d(M-1)^(l-2).                                           (2.5)
```

Put

```text
A=(M-1)/E=(N+1)/(N-1),
D_A=1+A+A^2+A^3,
y=d/E^2.                                                (2.6)
```

Fix the primitive blocks and all gap lengths.  If their total length is `L`,
the remaining `G=m-L` factors are internal.  The internal transposition sum
is central in the group algebra of `H`, so all interspersed internal powers
combine into one arbitrary-endpoint coefficient of length `G`.  Every word
charged by an `a`-update path has `L<=5a`, and therefore
`G>=m-5a`.  The inherited dense trace estimate gives at most

```text
4E^G/d!                                                  (2.7)
```

completions.  This pays the fixed endpoint once, not once per excursion.

### 2.4 Close returns cancel exactly

Fix `p,k,h`.  Then `c=k+h` and `Q=p+h`.  Summing the four possible lengths
for every positive budget composition gives

```text
binom(p+h-1,k+h-1) A^(4(p-k))D_A^(k+h).                (2.8)
```

Choose the `h` short gaps among the `c-1` inter-excursion gaps and choose each
length in `{0,1,2}`.  The factor is

```text
binom(k+h-1,h)3^h.                                     (2.9)
```

The two binomial coefficients satisfy the exact identity

```text
binom(k+h-1,h)binom(p+h-1,k+h-1)
 =binom(p-1,k-1)(p)^(over h)/h!.                       (2.10)
```

After the normalization (2.6), every extra close excursion contributes
`yD_A`.  Consequently all `h` sum to

```text
sum_{h>=0}(3yD_A)^h(p)^(over h)/h!
 =(1-3yD_A)^(-p).                                      (2.11)
```

For `N>=10^12`, `D_A<5`, `y<5/N^3`, and `p<=m/10^8`, so

```text
(1-3yD_A)^(-p)<=exp(2(3yD_A)p)<2.                     (2.12)
```

This is the decisive repair.  The old arbitrary-middle upper encoding paid
`(M/(M-1))^(4a)`.  In canonical return coordinates, intermediate returns
create additional primitive excursions, and their composition and gap
entropies cancel to the negative-binomial factor (2.11), whose logarithm is
only `O(a/N^3)`.

### 2.5 Exact hard-rod layout comparison

There are `k-1` long gaps.  After fixing the short gaps and subtracting three
from each long gap, the leading gap, trailing gap, and long-gap excesses give
at most

```text
binom(m-L-2k+3,k)<=binom(m-4p+3,k)                    (2.13)
```

layouts.  The last inequality follows from
`L>=4Q-2c=4p-2k+2h`.

For a clean boundary source with `k` primitive excursions, total budget `a`,
all inter-excursion gaps at least three, and at least four internal factors
after the last excursion, the exact layout count for prescribed `L` is

```text
binom(m-L-2k-1,k).                                     (2.14)
```

Since `L<=4a+k`, it is at least

```text
binom(m-4a-3k-1,k).                                    (2.15)
```

This termwise hard-rod comparison removes the former
`(m/(m-8a))^k` loss.

Set `C=ceil(20sqrt(a))` and

```text
W_(a,k)=binom(a-1,k-1)y^k A^(4(a-k))D_A^k
          binom(m-4a-3k-1,k),
B_a=(1/2)(E^m/d!)sum_{k=1}^C W_(a,k).                 (2.16)
```

The source count is injective because prefix return times uniquely recover
every primitive interval and every gap.  M42's kicked-prefix estimate is
uniform in fixed blocks, layouts, kicks, and compatible endpoints.  Here the
core has length at least `m-5a-4`, and its allowed away fraction is at most

```text
10a/(m-5a-4)<2x10^(-7).                               (2.17)
```

Thus more than one half of every endpoint-compatible internal completion is
simultaneously robust against every alternative cut.  This proves the lower
bound `B_a` in (2.16), with no endpoint-dependent exceptional class.

### 2.6 Boundary layer versus the cumulative isolate shell

Define the clean outer coefficient

```text
U_(p,k)=binom(p-1,k-1)y^k A^(4(p-k))D_A^k
          binom(m-4p+3,k).                             (2.18)
```

Equations (2.3), (2.7), and (2.11)--(2.13) give, for one isolate,

```text
O_z(a)<=4(E^m/d!)[1+2 sum_{p=1}^a sum_{k=1}^p U_(p,k)]. (2.19)
```

For `p=a-r`, `k<=C`, and
`n=m-4a-3k-1`,

```text
binom(m-4p+3,k)/binom(m-4a-3k-1,k)
 <=exp[k(4r+3k+4)/(n-k)].                              (2.20)
```

The exact `A=1+2/(N-1)` has `log A>=1/N`.  In the stated range,

```text
4k/(n-k)<=1/N,
k(3k+4)/(n-k)<=1.
```

The composition coefficient at `p` is no larger than the one at `a`.
Therefore

```text
U_(p,k)/W_(a,k)<=e exp(-3r/N),
sum_{p=k}^a U_(p,k)<=2N W_(a,k).                       (2.21)
```

For `k>C`, the successive ratio is at most

```text
U_(p,k+1)/U_(p,k)
 <=[m yD_A/A^4]p/[k(k+1)]
 <=80a/[k(k+1)]<=1/5.                                 (2.22)
```

Thus the large-`k` tail costs at most another factor `5/4` and is absorbed by
the `k=C` term.  The no-crossing term in (2.19) is absorbed by `k=1` for the
new range.  Including the factor four in (2.7), the factor two in (2.12), and
the one-half in (2.16) gives the conservative bound

```text
O_z(a)<=41N B_a.                                       (2.23)
```

Union over the `N` isolates costs at most `41N^2B_a`.

### 2.7 Non-isolate cuts and orientation

For a cut with smaller side `2<=s<=N/2`, let

```text
e=M-s(N-s),
D=E-e=(s-1)(N-s-1).
```

The inherited exact shrunken-cluster encoding remains valid.  If
`s<=N/4`, then

```text
log(M/e)<=5s/N,
D>=0.7(s-1)N.                                          (2.24)
```

Relative to the isolate internal baseline, its logarithm is at most

```text
2s log N-5.6(s-1)N^2+20as/N
 +2sqrt(800sa)+O(log a).                               (2.25)
```

Now `20as/N<=9x10^(-7)sN^2`, so (2.25) is below `-2N^2`.
For `s>=N/4`, the internal trace suppression is at least `0.8N^3`, while
all active, cut-entropy, and Bessel terms together are below `10^(-5)N^3`
for the stated threshold.  Summing all non-isolate cuts contributes less than
`B_a`.  Combining with (2.23),

```text
|V^(a)|<=N^3B_a.                                       (2.26)
```

The same direct counts orient the cut globally.  For isolates,

```text
m log(E/M)<=-8N^2,
4a log A<=4x10^(-7)N^2,
log(sum_k weights)=O(sqrt(a))=o(N^2).                 (2.27)
```

Using `|Omega(N,m)|>=2M^m/N!`, the endpoint factorial contributes only
`N!/d!=N` for an isolate.  Non-isolates are smaller by (2.25).  Hence

```text
pi(V^(a))<=exp(-4N^2)<1/2.                             (2.28)
```

### 2.8 A genuine original-chain boundary move

Every source counted by `B_a` consists of clean primitive blocks with budgets
summing to `a`, three-position interblock gaps, and four reserved factors
after the final block.  The inherited zipper gives an exact length-`a` path
to an `H`-internal word.

If the final return crossing is `t` and the four reserved internal factors
are `b_1,...,b_4`, let `h=b_1...b_4`.  The actual length-five same-product
replacement

```text
(t,b_1,b_2,b_3,b_4)
 ->(b_1,b_2,b_3,b_4,h^(-1)th)                          (2.29)
```

extends the final primitive excursion by four.  Every partition of the clean
primitive list now costs at least `a+1`.  The prefix-occupation certificate
in (2.17) excludes a path of length `a` from every other disconnection cut.
Thus (2.29) lands outside the full literal `V^(a)`.

A fixed-product length-five fiber has at most `M^4` elements.  Including
laziness, block-size choice, scan normalization, and heat-bath probability,
each source has specified exit probability at least

```text
p_exit=1/[6(m-4)M^4].                                  (2.30)
```

For `r=3,4,5`, all unretained terms in

```text
Q_r(B,B^c)=1/[6(m-r+1)|Omega|]
 sum_{w in B}sum_i H_{i,r}(w,B^c)                      (2.31)
```

are nonnegative.  Equations (2.26), (2.28), and (2.30) yield

```text
Phi_pm^K(V^(a))
 >=N^(-3)/[6(m-4)M^4]>=N^(-25).                       (2.32)
```

This proves (1.3)--(1.4) in the new range.  The frozen M42 theorem supplies
all smaller positive radii, and the inherited M25 theorem supplies `a=0`.

## 3. Probability, runtime, path length, and congestion accounting

- The endpoint-conditioned robust-core loss is below
  `exp(-0.75N^2)` uniformly in every fixed source skeleton and endpoint.
- The entire close-return renewal correction is less than two.
- The cumulative-depth sum costs at most `2N`; the large-cluster tail costs
  at most `5/4`.
- The source/whole-shell ratio is at least `N^-3`.
- Every source has an exact path of `a` genuine `H_5` zipper updates to `U`.
- Every specified exit is one actual `H_5` heat-bath outcome with probability
  at least `1/[6(m-4)M^4]`.
- There is no comparison-path or canonical-hub congestion.  Canonical return
  decomposition is computed in `O(m)` state updates; the zipper is
  constructive in polynomial time (the inherited maintained-product bound is
  `O(aN)`).  Exact local heat-bath sampling is polynomial in `N,m`.

## 4. Dependencies and status labels

1. **Proved here:** canonical excursion decomposition; segmentation lower
   witness; exact close-return negative-binomial resummation; exact hard-rod
   source/outer comparison; linear-range coefficient bounds.
2. **Proved in M37/M40:** primitive count, three/four/five-factor zipper,
   clean primitive rigidity, exact final `H_5` surgery, and the shrunken
   cluster encoding.
3. **Proved in M42:** kicked Johnson-walk prefix occupation uniformly in all
   deterministic kicks and compatible endpoints.  Its constants are
   explicitly rechecked in (2.17).
4. **Proved in M12/M31:** dense endpoint trace bounds and the global parity
   return lower bound.
5. **Inherited proved:** reversibility, stationarity, irreducibility, exact
   local samplers, and M25 radius-zero leakage.
6. **Cited but not used as proof dependencies:** Hong--Zhou passage-time
   transforms; Goulden--Jackson cluster inversion; Spitzer Markov renewal;
   Friedrich--Göbel--Krejca--Pappik polymer clique dynamics.  Exact
   hypothesis mismatches are in `resource_audit.md`.
7. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **LARGE-FRACTION SHELL ACTION.**  Determine universal constants
> `0<c_0<c_1<1` and an inverse polynomial `q(N,m)` such that every literal
> shell `V^(a)` with `c_0m<=a<=c_1m` is either globally larger-side oriented
> with its complement treated exactly, or satisfies
> `Phi_pm^K(V^(a))>=q(N,m)`; alternatively prove a superpolynomial full-`K`
> bottleneck in this remaining range.

The renewal correction itself stays bounded at `a=Theta(m)`.  The new issue
is the simultaneous balance of internal-core density, prefix occupation,
non-isolate active entropy, and global mass orientation as the constant
fraction grows.

## 6. Strongest self-attack

The theorem controls one geometrically natural family of cuts, not arbitrary
cuts or the spectral gap.  Conductance is not monotone, so polynomial leakage
through `m/10^8` says nothing by itself about later shells.

The most delicate proof point is Lemma 2.1: subgroup product forces a return
only for the globally first uncovered crossing, whose incoming state is `z`.
The proof explicitly orders the disjoint update hulls before induction; it
would be false if applied independently to a hull beginning inside an
excursion.  The second delicate point is fixed-endpoint counting: centrality
permits one coefficient bound after all gaps are fixed, but does not create
independent per-gap bridge laws.  The proof uses only the former.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty; no claim.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 words and four pure-Hurwitz classes; the whole-word `H_4`
  update is retained by the literal kernel.
- `S_4,m=4`: 120 words and 13 pure-Hurwitz classes; again `H_4` is global.
- `S_4,m=6`: 3936 words and 17 pure-Hurwitz classes.  No finite extrapolation
  is used.
- Near-minimal doubled-tree words need not have a dense core; the theorem is
  explicitly for `m=4N^3+4`.
- The argument uses ordered prefix returns and ordered windows, not graph-only
  support, degree parity, edge-multiplicity parity, or color counts.
- A short post-return gap is handled by the exact resummation, so no false
  parity characterization of an identity block is used.
- Every surgery is a genuine `H_5` update; there is no asserted length-two
  local simulation.
- The global smaller-side orientation and every `Q_3,Q_4,Q_5` normalization
  are explicit.

## 8. Artifacts, reproduction, and exact citations

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `resource_audit.md`
- `report.md`

No computation or stochastic experiment was used.  Reproduce the proof by
checking, in order, (2.1)--(2.4), the exact primitive normalization
(2.5)--(2.7), the binomial cancellation (2.8)--(2.12), the hard-rod
coefficients (2.13)--(2.22), cut orientation (2.23)--(2.28), and the full
kernel flow (2.29)--(2.32).

Local audit commands:

```text
ls Literature
grep -R -n -i -E 'renewal|polymer|hard rod|first.return|cluster decomposition' \
  Literature experiments/INDEX.md \
  papers/transposition_identity_samplers/sections/internal_sources.tex
/usr/bin/mutool draw -F text -o - Literature/2603.19110v1.pdf 1-2
```

Primary sources audited:

- Wenming Hong and Ke Zhou, *A note on the passage time of finite state
  Markov chains*, arXiv:1302.5987, Theorem 2.1:
  <https://arxiv.org/abs/1302.5987>.
- I. P. Goulden and D. M. Jackson, *An Inversion Theorem for Cluster
  Decompositions of Sequences with Distinguished Subsequences*, JLMS (2) 20
  (1979), 567--576, DOI 10.1112/jlms/s2-20.3.567:
  <https://doi.org/10.1112/jlms/s2-20.3.567>.
- Frank Spitzer, *Renewal theorems for Markov chains*, Proc. Fifth Berkeley
  Symposium II.2 (1967), 311--320:
  <https://projecteuclid.org/ebooks/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fifth-Berkeley-Symposium-on-Mathematical-Statistics-and/chapter/Renewal-theorems-for-Markov-chains/bsmsp/1200513474>.
- Tobias Friedrich, Andreas Göbel, Martin S. Krejca, and Marcus Pappik,
  *Polymer Dynamics via Cliques: New Conditions for Approximations*,
  arXiv:2007.08293, Theorems 1.1 and 3.4:
  <https://arxiv.org/abs/2007.08293>.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns the assigned literal-shell anti-bottleneck/resource
claim.  It is not Terminal A or Terminal B.
