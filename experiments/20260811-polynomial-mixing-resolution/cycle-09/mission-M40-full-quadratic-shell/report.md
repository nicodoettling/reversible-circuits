# M40 final report: all shells through `N^2/100` have polynomial leakage

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; an ordered transposition word evaluates as
`t_1...t_m`.  Let

```text
N>=10^6,                      M=binom(N,2),
d=N-1,                        E=binom(d,2),
m=4N^3+4,                     a_* =floor(N^2/100),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

Here `c(w)` counts support components including isolates.  The target is the
global uniform identity-bridge law.  The literal original chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1} H_{i,r},                     (1.2)
```

where `H_{i,r}` is the exact uniform same-ordered-product heat bath.

**Theorem (proved).**  Simultaneously for every integer `0<=a<=a_*`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,                      (1.3)
Phi_pm^K(V^(a))>=N^(-25).                             (1.4)
```

Thus no shell in this full quadratic range is a Terminal-B bottleneck.  The
result is a theorem about this explicit family of cuts, not a global gap
bound.

## 2. Full proof

### 2.1 Outer encoding of every literal shell state

Take `w in V^(a)`, choose a path of at most `a` local updates from a
disconnected word, and choose a nontrivial bipartition `P` between components
of that initial word.  Let `H_P` be the direct-product subgroup, let `e=e(P)`
be its number of internal transpositions, and set `x=M-e`.

The overlap-connected update clusters have hull product in `H_P`.  Shrink
each hull to its first and last crossing factor; removed prefixes and suffixes
are internal, so the product remains in `H_P`.  If a shrunken block has
length `l`, put

```text
q=ceil((l-1)/4).
```

For its parent cluster `q` is no larger than the number of update windows,
and

```text
l in {4q-2,4q-1,4q,4q+1},           sum_j q_j<=a.     (2.1)
```

On a fixed interval there are at most `xM^(l-2)` such blocks: choose the
first crossing and all middle factors; subgroup membership forces the action
of the last crossing on a cut side, hence forces that crossing transposition
uniquely if it exists.  For `b` prescribed blocks, the interval layouts are
at most `m^b/b!`.

Put

```text
R_P=M/e,                 D_P=1+R_P+R_P^2+R_P^3,
beta_P=mx/e^2,           theta_P=beta_P D_P/R_P^4.
```

The internal transposition sum is central in `H_P`.  The frozen dense
direct-product trace bound therefore gives the following exact upper
encoding, after summing the four possible lengths in (2.1):

```text
O_P(a)<=4e^m/|H_P| [1+
 sum_{Q=1}^a sum_{b=1}^Q
 binom(Q-1,b-1) R_P^(4Q) theta_P^b/b!].               (2.2)
```

Every member of `V^(a)` is charged to at least one `P`; multiple charging is
harmless in this upper bound.  All outside lengths are at least
`m-5a>=3.99N^3`, so the inherited trace hypotheses hold uniformly.

### 2.2 Five-factor zipper and primitive sources

Fix `z=N` and `H=Stab(z)=S_d`.  Two M37 lemmas are recalled with proofs
because their constants are used below.

**Five-factor zipper.**  If `g` is a product of five transpositions, then

```text
g=tau a_1a_2a_3a_4,                                  (2.3)
```

where `tau` is a transposition and every `a_i` is internal to `H`.  If `g`
moves `z`, take `tau=(z,g(z))`; then `tau g` fixes `z`, and left
multiplication splits a cycle, lowering Cayley transposition length by one.
If `g` fixes `z`, split a nontrivial internal cycle instead.  In either case
`tau g` is an even internal permutation of length at most four and can be
factored into exactly four internal transpositions by square padding.

Consequently every `H`-valued block of length `l`, with up to three following
internal padding positions, can be made wholly internal in exactly

```text
q=ceil((l-1)/4)                                        (2.4)
```

positive `H_5` moves.  Pad to `4q+1` positions and sweep from right to left
in strides of four using (2.3).  The last carrier is internal because the
full block and peeled suffix products are in `H`.

For the source count, track the inverse prefix state

```text
X_j=(prefix product)^(-1)(z).                          (2.5)
```

Call a crossing block *primitive* if it leaves `z` at its first factor,
does not return in the middle, and returns at its last factor.  From any
state in `[d]`, exactly one of the `M` transpositions sends it to `z`; the
other `M-1` keep it in `[d]`.  Hence the exact number of primitive blocks of
length `l` is

```text
d(M-1)^(l-2).                                          (2.6)
```

Use primitive blocks with budgets summing exactly to `a`, at least three
internal positions between blocks, and four internal positions after the
rightmost block.  Any subgroup-valued active cluster covering their crossings
must group consecutive whole primitive blocks: its endpoint must be a return
of (2.5) to `z`.  A group of `b_0` blocks with total budget `Q` has span at
least

```text
sum(4q_j-2)+3(b_0-1)=4Q+b_0-3>=4Q-2,                 (2.7)
```

so it needs at least `Q` update windows.

### 2.3 New quadratic-scale cut-repair lemma

For an internal transposition word `u` and a nontrivial cut
`S|([d]\S)`, let `X_S(u)` count factor occurrences crossing that cut.  Say
that `u` is *`a`-cut-robust* if

```text
X_S(u)>5a for every nontrivial S subset [d].           (2.8)
```

This is a deterministic deletion code: deleting any set of at most `5a`
coordinates leaves a crossing factor across every cut, hence leaves connected
support on `[d]`.  In particular it survives the intersection with the union
of any `a` update windows.  No interval enumeration is needed.

**Lemma 2.1 (uniform arbitrary-endpoint abundance).**  Let

```text
t>=4N^3-5a,                    1<=a<=N^2/100.          (2.9)
```

For every parity-compatible endpoint `h in S_d`, at least

```text
(1/2)E^t/d!                                             (2.10)
```

length-`t` transposition factorizations of `h` are `a`-cut-robust.

*Proof.*  The inherited arbitrary-endpoint Fourier/content estimate gives at
least `E^t/d!` total factorizations of every compatible endpoint at these
lengths.  For a fixed cut with smaller side `s`, under the unconditioned
uniform word law,

```text
X_S ~ Bin(t,p_S),               p_S=s(d-s)/E>=2/d,
mu_S=t p_S>=2t/d.                                     (2.11)
```

Since `5a<=N^2/20<mu_S/2`, Chernoff's lower-tail inequality gives

```text
Pr[X_S<=5a]<=exp(-mu_S/8)<=exp[-t/(4d)].               (2.12)
```

Union-bound only the fewer than `2^d` vertex cuts.  Across all endpoints, the
number of bad words is at most

```text
2^d E^t exp[-t/(4d)].                                  (2.13)
```

Subtracting this from one fixed endpoint class costs the full factor `d!`.
But `t>=4N^3-N^2/20>=3.99N^3`, and therefore

```text
d!2^d exp[-t/(4d)]
 <=exp{N log N+N-0.9975N^2}
 <=exp(-0.98N^2)<1/2                                  (2.14)
```

for `N>=10^6`.  Equations (2.10) and the claimed uniformity in `h` follow.
This explicitly rules out any hidden endpoint-dependent core loss. `□`

### 2.4 Source count and membership in the actual shell

For fixed primitive blocks and layout, reserve the first four internal
positions after the final block for the boundary surgery.  The concatenated
remaining core has length

```text
t_0=m-L-4>=4N^3-5a.                                   (2.15)
```

After the blocks and reserved factors are fixed, centrality turns the global
identity condition into one arbitrary-endpoint coefficient of the internal
transposition walk.  Its parity is compatible because `m` is even and all
fixed letters are transpositions.  Lemma 2.1, summed over the `E^4` reserved
choices, supplies at least

```text
(1/2)E^(m-L)/d!                                        (2.16)
```

endpoint-compatible robust outside choices for every fixed block/layout
selection.

For `b` blocks the layouts number at least `(m-8a)^b/b!`.  Define

```text
A=(M-1)/E,                   D_A=1+A+A^2+A^3,
beta_-=(m-8a)d/E^2,          theta_-=beta_-D_A/A^4,
C=ceil(20sqrt(a)),

S_a=sum_{b=1}^{min(a,C)}
 binom(a-1,b-1)theta_-^b/b!.
```

Using (2.6), summing the four lengths for each budget, and using (2.16), the
injective boundary-source count is

```text
B_a>=(1/2)E^m/d! A^(4a)S_a.                            (2.17)
```

Injectivity is literal: scanning the prefix state recovers every departure
from and first return to `z`, hence all primitive blocks, layouts, factors,
and the core.  There is no update-history multiplicity.

The zipper removes the blocks in exactly `sum q_j=a` genuine `H_5` moves,
yielding an all-internal identity word.  Symmetry of positive same-fiber
adjacency therefore puts every source in the literal `V^(a)`.

### 2.5 One actual boundary move leaves the shell

Let the last return crossing of the rightmost primitive block be `t`, and let
the reserved factors be `b_1,...,b_4` with `h=b_1...b_4`.  Use the genuine
same-product output

```text
(t,b_1,b_2,b_3,b_4)
 ->(b_1,b_2,b_3,b_4,h^(-1)th).                         (2.18)
```

The delayed block stays primitive and its span grows by four.

Suppose the target lay in `V^(a)`.  Delete the windows of a hypothetical
path from a disconnected word.  Their intersection with the robust core has
at most `5a` coordinates, so (2.8) leaves `[d]` connected.  Every surviving
factor is internal to a cut between components of the hypothetical starting
word.  Therefore the cut must be `{z}|[d]`.

Primitive rigidity now applies.  Every group not containing the extended
block costs at least its total source budget `Q`; the group containing it has
span at least `4Q+2`, while `Q` windows span at most `4Q+1`, so it costs at
least `Q+1`.  The total is at least `a+1`, a contradiction.  Thus the target
is outside `V^(a)`.

A length-five fixed-product fiber has at most `M^4` words.  Including
laziness, block-size choice, scan normalization, and exact heat-bath
probability, this particular exit has probability at least

```text
p_exit=1/[6(m-4)M^4].                                  (2.19)
```

### 2.6 Quadratic entropy comparison

For the isolate outer encoding in (2.2), put

```text
R=M/E,                    D_R=1+R+R^2+R^3,
beta=md/E^2,              theta=beta D_R/R^4.
```

Here `theta<=80` and `theta_->60`.  Since
`f(u)=(1+u+u^2+u^3)/u^4` decreases and `R>A`,

```text
theta/theta_-<=beta/beta_-=m/(m-8a).                  (2.20)
```

For completeness, these numerical bounds follow from
`m-8a>3.99N^3`, `d>=0.999999N`, `E<N^2/2`, and
`1<A<R=N/(N-2)<1.000003`; also `beta<20` and `f(R)<4`.

All quadratic-scale constants are explicit:

```text
[M/(M-1)]^(4a)<exp(0.081)<2,
C<=2N+1,
16aC/m<0.081,
4a log(5/2)<0.037N^2.                                 (2.21)
```

For `b<=C`, (2.20) raised to `b` is below two.  For

```text
w_{a,b}(theta)=binom(a-1,b-1)theta^b/b!,
```

the ratio `w_{a,b+1}/w_{a,b}` is at most `1/4` after `b>=C`, so the omitted
tail is geometric.  Moreover, for `Q<=a`,

```text
R^(4Q)<2A^(4a),
binom(Q-1,b-1)<=binom(a-1,b-1).                       (2.22)
```

The whole cumulative isolate coefficient in (2.2), including `Q=0`, is at
most `7aA^(4a)S_a`.  The trace factor four, robust factor one-half, and all
`N` isolate choices then give

```text
|V^(a) charged to isolate cuts|<=56NaB_a<=N^4B_a.     (2.23)
```

For a non-isolate cut with smaller side `2<=s<=N/2`,

```text
E-e=(s-1)(N-s-1),             M/e<=5/2,
beta_P<=200s,                 m/E>=8N.                (2.24)
```

The same Bessel bound as M37 makes the logarithm of the total size-`s` cut
contribution relative to `E^m/d!` at most

```text
2s log N-8N(s-1)(N-s-1)+4a log(5/2)
 +2sqrt(800sa)+log 8+(1/2)log(800sa).                 (2.25)
```

This is below `-2N^2` uniformly for `N>=10^6`; summing the fewer than `N`
possible values of `s` remains below `exp(-N^2)E^m/d!<B_a`.  Consequently

```text
|V^(a)|<=N^5B_a.                                       (2.26)
```

For orientation, divide the direct outer count by the parity-coset lower
bound `|Omega(N,m)|>=2M^m/N!`.  The isolate logarithm is at most

```text
log(2N^2)+m log(E/M)+4a log(M/E)
 +log(1+sqrt(80a)exp(2sqrt(80a)))
 <=-7N^2,                                             (2.27)
```

using `E/M=1-2/N`.  The non-isolate contribution is smaller.  Therefore

```text
pi(V^(a))<=exp(-4N^2)<1/2.                             (2.28)
```

### 2.7 Full-kernel flow

For `r=3,4,5`,

```text
Q_r(B,B^c)=1/[6(m-r+1)|Omega|]
 sum_{w in B}sum_i H_{i,r}(w,B^c),
Q_K=Q_3+Q_4+Q_5.                                     (2.29)
```

Retain only the `B_a` sources and their specified positive `Q_5` exits.
Every omitted `Q_3,Q_4,Q_5` term is nonnegative.  From (2.19), (2.26), and
(2.28),

```text
Phi_pm^K(V^(a))
 >=N^(-5)/[6(m-4)M^4]
 >=N^(-25).                                           (2.30)
```

This proves (1.3)--(1.4) for every `1<=a<=a_*`.  For `a=0`, use
`U subset V^(1)` for the mass bound and the frozen M25 theorem
`Phi_pm^K(U)>=1/(32N^3)>=N^-25`.  Thus the theorem includes every radius in
the claimed range, with no silent omission at zero.

## 3. Probability, runtime, path length, and congestion

- Robust-core failure before endpoint conditioning is at most
  `2^d exp[-t/(4d)]`; after paying `d!`, it is at most `exp(-0.98N^2)`.
- Every compatible endpoint retains at least `(1/2)E^t/d!` robust cores;
  there is no endpoint-dependent exceptional class.
- Each source has a path of exactly `a` genuine `H_5` updates to `U`.
- Its explicit exit is one `H_5` outcome of probability at least
  `1/[6(m-4)M^4]` in the original lazy chain.
- No canonical path, hub, randomized routing, history congestion, or modified
  chain is used.
- The zipper is constructive in `O(aN)` time with maintained local products.
  Recognizing cut robustness is not needed by the Markov chain or the
  enumerative conductance proof.
- The inherited exact `r<=5` heat-bath samplers have polynomial per-step cost
  in `N,m`.

## 4. Dependencies and statuses

1. **Proved here:** the cut-multiplicity repair lemma, its arbitrary-endpoint
   abundance with every constant, the quadratic-scale substitution, and the
   endpoint-uniform source retention.
2. **Proved in M37 and restated here:** minimal cluster encoding, five-factor
   zipper, primitive count and rigidity, injective source coefficient,
   entropy comparison, and genuine boundary surgery.
3. **Proved/frozen in M12/M31:** dense direct-product trace upper bound,
   parity-coset global return lower bound, and compatible arbitrary-endpoint
   Fourier/content lower bound.
4. **Inherited proved:** reversibility, stationarity, irreducibility,
   polynomial exact local block sampling, and M25's
   `Phi_pm^K(U)>=1/(32N^3)` bound for radius zero.
5. **Cited but not used:** Friedrich--Goebel--Krejca--Pappik, arXiv:2007.08293v4,
   Theorem 3.4 on clique polymer dynamics.  Its hypotheses do not match this
   endpoint-conditioned word chain; see `resource_audit.md`.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **SHELL ACTION BEYOND THE QUADRATIC REPAIR SCALE.**  Determine universal
> constants `kappa'>1/100,C<infinity` and the largest explicit range of
> proper radii `a` for which
> `Phi_pm^K(V^(a))>=(Nm)^(-C)`, ultimately testing radii linear in `m`.

The cut-multiplicity core is intrinsically quadratic for an isolate: its
least-populated cut has only about `8N^2` occurrences in a length-`4N^3`
internal word, so arbitrary deletion of `5a` positions cannot be certified by
this condition once `a` exceeds a constant multiple of `N^2`.  A linear-in-
`m` result needs a different distributed repair mechanism, an exact shell-
layer recursion, or a literal bottleneck construction when the entropy balance
reverses.

## 6. Strongest self-attack

The theorem controls every radius through `N^2/100`, but conductance is not
monotone.  At larger radii an adversary can delete all occurrences across a
singleton cut, defeating this particular robust-core certificate.  Nothing
here rules out a superpolynomial bottleneck at `a=Theta(N^2)` with a larger
constant, at `a` between `N^2` and `m`, or inside another full-support phase.

The isolate primitive construction also incurs
`[M/(M-1)]^(4a)=exp(Theta(a/N^2))`; this is constant here but becomes
exponential at radii linear in `m`.  Thus neither the repair code nor the
entropy comparison may be extrapolated.  The result is not Terminal A or B.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty; no claim is made.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 words and four Hurwitz classes; whole-word `H_4` makes the
  analogous shell global.
- `S_4,m=4`: 120 words and 13 Hurwitz classes; whole-word `H_4` is retained.
- `S_4,m=6`: 3936 words and 17 Hurwitz classes; finite behavior is not used.
- Near-minimal doubled-tree words need not contain this dense repair core;
  the theorem explicitly fixes `m=4N^3+4`.
- Ordered prefix states and windows are essential.  No parity, degree, edge-
  multiplicity, color-interleaving, or unordered-graph shortcut is used.
- Three crossing factors may have subgroup product; primitive return times,
  not crossing parity, force cluster grouping.
- The zipper uses actual `H_5` moves and does not assert the false general
  length-two simulation.
- The global smaller-side orientation and every `Q_3+Q_4+Q_5` normalization
  are explicit.

## 8. Artifacts, reproduction, and literature citation

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `resource_audit.md`
- `report.md`

No computation was used.  Reproduce by checking, in order, the outer encoding
(2.1)--(2.2), the zipper/primitive lemmas (2.3)--(2.7), the new cut-repair
count (2.8)--(2.14), source and target arguments (2.15)--(2.19), coefficient
and orientation estimates (2.20)--(2.28), and full-kernel flow
(2.29)--(2.30).

Primary resource audited:

- Friedrich, Goebel, Krejca, and Pappik, *Polymer Dynamics via Cliques: New
  Conditions for Approximations*, arXiv:2007.08293v4, Definition 3.1,
  clique-dynamics condition, and Theorem 3.4:
  <https://arxiv.org/abs/2007.08293v4>.

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict is the assigned uniform quadratic-radius shell-leakage theorem.
It is not either global terminal outcome.
