# M37 final report: quadratic-over-log shells have polynomial leakage

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; an ordered word evaluates as `t_1...t_m`.  Let

```text
N>=10^6,                    M=binom(N,2),
d=N-1,                      E=binom(d,2),
m=4N^3+4,                   A_N=floor(N^2/[100log(N+1)]),
U={w in Omega(N,m):c(w)>=2},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.  (1.1)
```

Here `c` counts support components including isolates.  The target is the
global uniform identity bridge law, and the original chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1}H_{i,r}.                       (1.2)
```

Every `H_{i,r}` is exactly uniform on its same-ordered-product transposition
fiber.

**Theorem (proved).**  Simultaneously for every integer `1<=a<=A_N`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,                       (1.3)
Phi_pm^K(V^(a))>=N^(-25).                              (1.4)
```

In particular, the explicit endpoint sequence

```text
a_N=floor(N^2/[100log(N+1)])                           (1.5)
```

is proper and cannot be a Terminal-B bottleneck.  This reaches the
prioritized quadratic-over-log scale.  It remains a scoped anti-bottleneck
theorem, not a proof of the global spectral-gap lower bound.

## 2. Full argument

### 2.1 Minimal active-cluster upper encoding

For a nontrivial bipartition `P`, let `H_P` be its direct-product subgroup,
let `e=e(P)` count internal transpositions, and put `x=M-e`.  Take a path of
at most `a` local updates from a disconnected word and choose `P` between its
initial support components.  Overlap-connected update windows have hull
length at most `4q_0+1` when they contain `q_0` updates, and every active hull
has ordered product in `H_P`.

Shrink an active hull to its first and last crossing factors.  Removed
prefixes and suffixes are internal, so the shrunken product remains in
`H_P`.  For its length `l`, assign

```text
q=ceil((l-1)/4).                                       (2.1)
```

Then `q<=q_0` and

```text
l in {4q-2,4q-1,4q,4q+1},             sum_j q_j<=a.   (2.2)
```

For a fixed interval, the block count is at most

```text
xM^(l-2).                                               (2.3)
```

Choose the first crossing and every middle factor.  If the last crossing is
`t` and its fixed left product is `L`, subgroup membership forces
`t(S)=L^(-1)(S)` on a cut side `S`; at most one crossing transposition has
that action.

For prescribed ordered lengths, disjoint interval layouts number at most
`m^c/c!`.  Let

```text
R_P=M/e,                         beta_P=mx/e^2,

T_a(beta)=1+sum_{Q=1}^a sum_{c=1}^Q
 binom(Q-1,c-1)(4beta)^c/c!.                           (2.4)
```

The composition factor is exact and the four comes from (2.2).  For fixed
blocks, all outside internal segments combine because the internal
transposition sum is central in `H_P`.  Splitting their total length between
two adjacent even times, Cauchy--Schwarz and the frozen dense direct-product
trace bound give at most `4e^(m-L)/|H_P|` for the required endpoint.  Since
`L<=5a<<m`, all density hypotheses hold.  Thus the words charged to `P` obey

```text
O_P(a)<=4e^m/|H_P| R_P^(4a)T_a(beta_P).               (2.5)
```

The subsequent source count will match both the interval-layout entropy and
the arbitrary-middle-factor entropy in this bound.

### 2.2 Five-factor coset/Cayley zipper

Fix `z=N` and `H=Stab(z)=S_d`.  The following lemma is the new algebraic
input.

**Lemma 2.1.**  If `g in S_N` is a product of five transpositions, then there
are a transposition `tau` and four transpositions `a_1,...,a_4 in H` such that

```text
g=tau a_1a_2a_3a_4.                                   (2.6)
```

If `g` moves `z`, set

```text
tau=(z,g(z)),                         h=tau g.          (2.7)
```

Then `h(z)=z`.  Moreover `z` and `g(z)` lie in the same cycle of `g`, so
left multiplication by their transposition splits that cycle and lowers the
Cayley transposition length by one.  Hence `h in H` has length at most four.
If `g` fixes `z`, it has odd sign and is nonidentity.  Choose `tau` between
two vertices in one nontrivial internal cycle of `g`; again `h=tau g in H`
and its length drops by one to at most four.  In both cases `h` is even, so
its minimal internal transposition length is `0,2`, or `4`; pad by adjacent
internal squares to obtain exactly four factors.  Since `g=tau h`, this
proves (2.6).

**Corollary 2.2 (zipper).**  Every length-`l` word with product in `H` can be
made internal in

```text
q=ceil((l-1)/4)                                        (2.8)
```

positive `H_5` moves, provided up to three following internal padding
positions are available.

Pad on the right to length `4q+1`.  Apply Lemma 2.1 to the rightmost five
factors, replacing them by one transposition carrier followed by four
internal factors.  Repeat in strides of four.  At the last window, the
carrier is internal: the full padded block and every already peeled suffix
are internal-product words, so the last five-factor product belongs to `H`.
Exactly `q` same-product `H_5` outcomes make the entire padded interval
internal.

This is a linear-length constructive theorem for these subgroup-valued
blocks; it is not the false general length-two simulation.

### 2.3 Exact primitive-excursion count

For a block beginning with a crossing factor, track

```text
X_j=(prefix product)^(-1)(z).                          (2.9)
```

After the first crossing, `X_0 in [d]`.  Appending a transposition `t`
changes the state to `t(X_j)`.  From a non-`z` state exactly one of the `M`
transpositions, namely `(z,X_j)`, sends it to `z`; every other choice remains
in `[d]`.

Call a crossing block *primitive* when the state does not return to `z`
between its first and last factors.  For length `l`, choose the first crossing
in `d` ways, choose every one of the `l-2` middle factors among the exact
`M-1` safe choices, and use the unique final return transposition.  Therefore
the primitive count is exactly

```text
d(M-1)^(l-2).                                          (2.10)
```

Every primitive block has product in `H` and is removable in the minimal
budget (2.8) by Corollary 2.2.  Compared with the outer count (2.3), the total
entropy loss over all block middles is only

```text
[M/(M-1)]^(sum_j(l_j-2))
 <=[M/(M-1)]^(4a)
 <=exp(4a/(M-1))<2.                                   (2.11)
```

The last inequality is uniform through `a<=A_N`.

### 2.4 Primitive blocks force whole-block cluster covers

Choose primitive source blocks with budgets summing exactly to `a`, at least
three internal positions between consecutive blocks, and at least four
internal positions after the rightmost block.

Before and after every primitive block the prefix state in (2.9) is `z`; it
is never `z` inside.  Consider any collection of disjoint subgroup-valued
active hulls covering all crossings.  Its leftmost hull begins at the first
crossing of the first primitive block.  Since its product fixes `z`, it can
end only at a later return to `z`, hence after a whole primitive block.  The
same argument inductively shows that every active hull contains consecutive
whole source blocks.

If a hull contains `r` consecutive source blocks whose budgets sum to `Q`,
its length is at least

```text
sum_j(4q_j-2)+3(r-1)=4Q+r-3>=4Q-2.                   (2.12)
```

A connected union of `u` update windows has span at most `4u+1`; (2.12)
therefore requires `u>=Q`.  No alternative regrouping, including a
three-crossing subgroup product, lowers the total budget.

### 2.5 Robust outside core and endpoint-compatible counting

Fix primitive block words and a layout, and reserve the first four internal
positions after the rightmost block for the final boundary move.  Let

```text
t_0=m-L-4                                                 (2.13)
```

be the number of remaining outside positions.  Concatenate their internal
transpositions in word order.  Call the result *`a`-robust* if deleting the
union of any at most `a` intervals of length at most five leaves connected
support on `[d]`.

After the block products and four reserved factors are fixed, centrality of
the internal transposition sum turns the global identity condition into one
arbitrary-endpoint coefficient of `T^(t_0)`.  The parity is compatible, and
the transposition content bound gives at least

```text
E^(t_0)/d!                                              (2.14)
```

solutions at this density.

If a core is not robust, choose a cut disconnected after deleting the
witness windows.  Extending shorter intervals to length five and ignoring
the endpoint condition gives at most

```text
t_0^a 2^d E^(5a)[E(1-2/d)]^(t_0-5a)                  (2.15)
```

bad cores.  Relative to (2.14), its logarithm is at most

```text
a log t_0+d log 2+log(d!)-2(t_0-5a)/d<=-N^2.          (2.16)
```

Indeed `a log t_0<=0.04N^2`, while the last negative term is asymptotic to
`-8N^2`.  Hence, after summing the `E^4` reserved-factor choices, every fixed
block/layout selection admits at least

```text
(1/2)E^(m-L)/d!                                        (2.17)
```

robust endpoint-compatible outside choices.

Erasing all primitive block intervals and the four reserved boundary factors
maps the intersection of any global five-window with the remaining ordered
core to one interval of length at most five.  This is the robustness statement
needed in the target-exclusion proof below.

### 2.6 Exact source coefficient and injectivity

For `c` prescribed block lengths totaling `L`, the number of ordered layouts
with three-position interblock gaps and four trailing positions is

```text
binom(m-L-2c-1,c)>=(m-8a)^c/c!.                        (2.18)
```

Put

```text
A=(M-1)/E,                     D_A=1+A+A^2+A^3,
beta_-=(m-8a)d/E^2,            theta_-=beta_-D_A/A^4,
C=ceil(2sqrt(100a)),

S_a=sum_{c=1}^{min(a,C)}
 binom(a-1,c-1)theta_-^c/c!.                           (2.19)
```

For one budget `q`, summing the four lengths in (2.2) contributes

```text
sum_l A^(l-2)=A^(4(q-1))D_A.                           (2.20)
```

Therefore (2.10), (2.17), (2.18), and the ordered compositions of total
budget `a` show that the boundary-source family has size

```text
B_a>=(1/2)E^m/d! A^(4a)S_a.                            (2.21)
```

This count is injective.  For the fixed isolate `z`, scanning the word's
prefix state uniquely identifies every departure from and first return to
`z`, hence its primitive block intervals.  Their lengths recover the
budgets, and all block and outside factors remain visible.  No update-history
multiplicity appears in (2.21).

Corollary 2.2 eliminates the blocks in exactly `sum q_j=a` positive local
updates, using at most three following gap factors as padding.  The resulting
word uses only internal transpositions and therefore belongs to `U`; by
symmetry of positive same-fiber adjacency, every source lies in the actual
`V^(a)`.

### 2.7 One genuine `H_5` move exits `V^(a)`

Push the final return crossing of the rightmost primitive block through the
four reserved internal factors.  If their product is `h`, the actual
same-product output is

```text
(t,b_1,b_2,b_3,b_4)
 ->(b_1,b_2,b_3,b_4,h^(-1)th).                         (2.22)
```

The delayed block remains primitive: before the old return its state lies in
`[d]`, each added internal factor keeps it in `[d]`, and the conjugated final
crossing returns it to `z`.  Its span has increased by four.

Suppose the target were in `V^(a)`.  Delete the update windows of a
hypothetical path from a disconnected word and choose a cut between its
initial components.  By (2.16), the undeleted robust core remains connected
on `[d]`.  All its factors are internal to the hypothetical cut, so `[d]`
lies on one side and the cut must be `{z}|[d]`.

Shrink the hypothetical active clusters to their first and last crossings.
Section 2.4 makes them groups of consecutive whole primitive blocks.  A group
not containing the extended block costs at least the sum `Q` of its source
budgets.  A group containing it has length at least

```text
4Q+2,                                                   (2.23)
```

whereas `Q` windows span at most `4Q+1`; it costs at least `Q+1`.  Summing
the cluster partition requires at least `a+1` updates, a contradiction.  The
target is outside `V^(a)`.

A length-five fixed-product fiber has at most `M^4` elements.  Including
laziness, the uniform block-size choice, scan normalization, and the exact
heat bath, the specified exit probability is at least

```text
p_exit=1/[6(m-4)M^4].                                  (2.24)
```

### 2.8 Exact entropy comparison with the whole isolate shell

For the isolate outer count define

```text
R=M/E,                         D_R=1+R+R^2+R^3,
beta=md/E^2,                  theta=beta D_R/R^4.      (2.25)
```

Here `beta<=20` and `theta<=80`.  The function

```text
f(u)=(1+u+u^2+u^3)/u^4=u^-4+u^-3+u^-2+u^-1           (2.26)
```

is decreasing.  Since `R>A`,

```text
theta/theta_-<=beta/beta_-.                            (2.27)
```

This comparison uses the unsimplified length sum underlying (2.5).  For
fixed total budget `Q` and `c` blocks that sum is exactly

```text
R^(4Q) binom(Q-1,c-1)theta^c/c!,                       (2.27a)
```

whereas (2.5) replaced it by the looser
`R^(4a)binom(Q-1,c-1)(4beta)^c/c!`.  Thus no comparison between
`theta` and the differently normalized `T_a(beta)` is being assumed.

For `c<=C`, the right side raised to `c` is at most two: its logarithm is at
most `16aC/m<1`.  For

```text
w_{a,c}(theta)=binom(a-1,c-1)theta^c/c!,              (2.28)
```

the ratio after `c>=C` is

```text
w_{a,c+1}/w_{a,c}
 =theta(a-c)/[c(c+1)]<=1/4.                            (2.29)
```

Thus the omitted large-`c` tail is controlled by its first term.  Also,

```text
R^(4Q)<=R^(4a)
 =[M/(M-1)]^(4a)A^(4a)<2A^(4a),                       (2.30)
```

and `binom(Q-1,c-1)<=binom(a-1,c-1)` for every `Q<=a`.
Also `theta_->60` for `N>=10^6`: indeed
`m-8a>3.99N^3`, `d>0.999999N`, `E<N^2/2`, and
`1<A<R<1.000003`.  Thus the `Q=0` term is absorbed by `S_a`.
It follows that the cumulative `Q<=a` isolate coefficient, including that
term, is at most `7aA^(4a)S_a`.

Including the trace factor in (2.5), the robust factor `1/2` in (2.21), and
all `N` choices of isolate gives

```text
|V^(a) charged to isolate cuts|<=56Na B_a<=N^4B_a.    (2.31)
```

This is the entropy match that replaces both M31's `C_0^a` and M33's
`exp(O(a/N))` losses.

### 2.9 Non-isolate cuts and global orientation

For a cut with smaller side `2<=s<=N/2`,

```text
beta_P<=200s,                  M/e<=5/2,
E-e=(s-1)(N-s-1),             m/E>=8N.                (2.32)
```

As in M33, the elementary Bessel-series bound is

```text
T_a(beta_P)
 <=1+sqrt(800sa)exp(2sqrt(800sa)).                    (2.33)
```

Relative to `E^m/d!`, the logarithm at cut size `s` is at most

```text
2s log N
-8N(s-1)(N-s-1)
+4a log(5/2)
+2sqrt(800sa)+log 8+(1/2)log(800sa).                  (2.34)
```

Here the `2s log N` term already pays both the number of cuts of size `s` and
`d!/|H_P|`.  Since

```text
(s-1)(N-s-1)>=(s-1)(N/2-1),
4a log(5/2)<=N^2/[20log(N+1)],
```

the resulting right side is at most `-2N^2` for every
`2<=s<=N/2` and `N>=10^6`.  Summing the fewer than `N` possible values of
`s` leaves at most `exp(-N^2)E^m/d!`.  Finally `theta_->60` in (2.19), so
`B_a>=30E^m/d!`; in particular the non-isolate contribution is below `B_a`.
Consequently

```text
|V^(a)|<=N^5B_a.                                       (2.35)
```

For stationary orientation, use (2.5) directly.  The isolate contribution
divided by the lower bound in (2.37) has logarithm at most

```text
log(2N^2)+m log(E/M)+4a log(M/E)
 +log(1+sqrt(80a)exp(2sqrt(80a)))
 <=-7N^2.                                             (2.36)
```

The preceding `exp(-N^2)E^m/d!` non-isolate estimate is smaller still after
the same division.  Here we used `log(1-u)<=-u`, the definition of `A_N`,
and only elementary monotone bounds at `N=10^6`.  Since

```text
|Omega(N,m)|>=2M^m/N!,                 E/M=1-2/N,      (2.37)
```

the dominant ratio contributes
`m log(E/M)<=-2m/N<=-8N^2`.  Therefore

```text
pi(V^(a))<=exp(-4N^2)<1/2.                             (2.38)
```

This orients the actual global shell before any flow division.

### 2.10 Full `Q_3+Q_4+Q_5` flow

For `r=3,4,5`, write

```text
Q_r(B,B^c)
 =1/[6(m-r+1)|Omega|]
   sum_{w in B}sum_i H_{i,r}(w,B^c).                   (2.39)
```

The lazy identity contributes no boundary flow and

```text
Q_K=Q_3+Q_4+Q_5.                                      (2.40)
```

Retain only the `B_a` sources and their specified `Q_5` targets.  Every
uncharged term is nonnegative.  Equations (2.24), (2.35), and (2.38) give

```text
Phi_pm^K(V^(a))
 >=N^(-5)/[6(m-4)M^4]
 >=N^(-25),                                            (2.41)
```

using `m-4=4N^3`, `M<=N^2`, and `24<=N^9`.  This proves
(1.3)--(1.4).

## 3. Probability, runtime, path length, and congestion accounting

- Actual-shell mass: at most `exp(-4N^2)` uniformly through `A_N`.
- Boundary-source count: the exact primitive/layout/robust-core lower bound
  (2.21).
- Source path: exactly `sum q_j=a` genuine `H_5` zipper updates from an
  all-internal identity word.
- Exit: one genuine `H_5` outcome, probability at least
  `1/[6(m-4)M^4]` in the original chain.
- Conductance: at least `N^-25` for every `a<=A_N`.
- No canonical path, hub, comparison congestion, modified chain, or
  path-history count is used.
- The zipper is constructive and processes a certified source in `O(amN)`
  naive permutation time, reducible to `O(aN)` with maintained local
  products.  Robust-core recognition need not be efficient for this
  enumerative flow theorem.
- The inherited exact `r<=5` block sampler has polynomial per-step cost in
  `N,m`.

## 4. Dependencies and statuses

1. **Proved here:** the five-factor zipper, exact primitive count, primitive
   cluster rigidity, robust endpoint-compatible outside count, injective
   source count, entropy comparison, target exclusion, orientation, and
   conductance.
2. **Proved in M31/M33 and rederived here:** shrunken product-cluster outer
   encoding, forced-last-crossing count, and factorial cut comparison.
3. **Proved/frozen in Cycle-02 M12:** dense direct-product trace upper bounds,
   parity-coset return lower bounds, and the content gap used for arbitrary-
   endpoint smoothing; every density hypothesis is checked here.
4. **Inherited proved:** exact heat-bath reversibility, stationarity, global
   irreducibility, and polynomial exact block sampling.
5. **Not used:** conductance monotonicity, support-only distance, crossing
   parity, canonical hubs, restriction gaps, finite spectra, or an auxiliary
   length-two chain.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **QUADRATIC SHELL ACTION WITHOUT THE LOG LOSS.**  There are universal
> `c,C>0` such that, for `m=4N^3+4` and every proper shell with
> `1<=a<=cN^2`, one has `Phi_pm^K(V^(a))>=N^-C`.

The primitive block entropy remains adequate at this larger scale.  The
present robust-core union bound does not: selecting `a` possible windows costs
`a log m`, which becomes `Theta(N^2 log N)` at `a=Theta(N^2)` and overwhelms
the `Theta(N^2)` support-disconnection exponent.  A sharper deletion-resilient
connectivity theorem, or a boundary argument not requiring adversarial
window robustness, is the named next step.

## 6. Strongest self-attack

The theorem rigorously rejects this shell family only through
`N^2/[100log(N+1)]`.  Conductance is not monotone in the radius, and a larger
shell could behave differently.  In particular, the robust-core proof loses
the logarithm by a crude union bound over window locations; nothing here
justifies extrapolation to `Theta(N^2)`, later shells, or unrelated internal
full-support cuts.

The explicit threshold `N>=10^6` is intentionally conservative.  It keeps
all analytic inequalities literal and has no bearing on the asymptotic
sequence.  This scoped result is neither Terminal A nor Terminal B.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty; no theorem is asserted.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 identity words and four pure-Hurwitz components; the
  whole-word `H_4` makes the analogous first shell global.
- `S_4,m=4`: 120 words and 13 pure-Hurwitz components; whole-word `H_4`
  cannot be dropped.
- `S_4,m=6`: 3936 words and 17 pure-Hurwitz components; finite shell behavior
  is not used asymptotically.
- Near-minimal doubled-tree words need not have a dense robust outside core;
  `m=4N^3+4` is explicit.
- Ordered windows, ordered block products, and prefix-return states are
  essential.  Color interleavings are not replaced by an unordered graph.
- Three crossing factors can multiply into the isolate subgroup; primitivity,
  not parity or degree parity, controls regrouping.
- The zipper uses actual `H_5` updates.  It does not assert a general `L=2`
  simulation.
- Every cut enters the mass bound, global smaller-side orientation is proved,
  and the complete `Q_3+Q_4+Q_5` normalization appears in
  (2.39)--(2.41).

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was used.  Reproduce the theorem by checking:

1. the minimal outer encoding (2.1)--(2.5);
2. the cycle-splitting zipper (2.6)--(2.8);
3. the exact killed-state count and primitive rigidity (2.9)--(2.12);
4. robust endpoint-compatible outside words (2.13)--(2.17);
5. the injective source count and exit (2.18)--(2.24);
6. coefficient/cut comparisons (2.25)--(2.35); and
7. orientation and exact kernel flow (2.36)--(2.41).

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns the uniform inverse-polynomial leakage theorem through
the quadratic-over-log shell radius.  It is not either global terminal
outcome.
