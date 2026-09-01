# M64 final report: exterior closures have polynomial endpoints; intermediate layers remain open

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  The target is the global uniform law `pi` on
`Omega(N,m)`, and the literal chain is

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m}.                              (1.1)
```

Throughout the main theorem `N>=5`, `m=2N-2`, `M=binom(N,2)`, and `F_N`
is the connected full-support minimal macro.  Fix the M63 labeled path tree,
its two original leaves, and any nonempty proper balanced union of the
all-original-leaves core fibers.  Call the resulting set `A subset F_N`.
Define the literal exterior closure

```text
E_0={y in F_N^c:K(x,y)>0 for some x in A},
E_(k+1)=E_k union {y in F_N^c:K(x,y)>0 for some x in E_k},
L_0=E_0,   L_k=E_k minus E_(k-1),
C_k=A union E_k.                                      (1.2)
```

This mission proves four scoped statements.

**Claim A (exact mass and full boundary identity).**  For every `k>=0`,
with `W=|Omega(N,m)|` and `s_k=min{|C_k|,W-|C_k|}`,

```text
pi(C_k)=|C_k|/W,

Q_K(C_k,C_k^c)
 =W^(-1) [
    sum_(x in C_k) K(x,F_N minus A)
   +sum_(x in L_k) K(x,L_(k+1))
  ],                                                   (1.3)

Phi_pm^K(C_k)={the bracket in (1.3)}/s_k.             (1.4)
```

Thus (1.3) accounts for every H3/H4/H5 boundary transition and uses the
exact global smaller-side orientation.

**Claim B (quantitative shell criterion and every fixed radius).**  Put

```text
D_out=sum_(r=3)^5 (m-r+1)M^r,
p_min=1/[2|R_m|(m-2)M^5],
D_N=(3N^2+N-12)/2,
Lambda_N=binom(m,2)(N-1)^2,
alpha_N=(N-2)/[6(m-2)D_N Lambda_N].                  (1.5)
```

Then, exactly,

```text
Phi_pm^K(C_k)
 >=[alpha_N|A|+p_min|L_(k+1)|]/s_k.                  (1.6)
```

Moreover

```text
|E_k|<=|A| sum_(j=1)^(k+1) D_out^j,                  (1.7)
```

so for every fixed integer `k>=0`, uniformly in `N`,

```text
Phi_pm^K(C_k)>=1/[288 N^(11k+17)].                   (1.8)
```

The exponent in (1.8) depends on the fixed radius; this is deliberately not
advertised as a uniform growing-radius theorem.

**Claim C (the exterior induced graph is connected with polynomial
diameter).**  Every state of `F_N^c` reaches one fixed exterior word `q_v`
using only literal positive H3 edges that remain in `F_N^c`, in at most

```text
R_ext=50N^2m^3+N+1                                  (1.9)
```

steps.  Consequently the induced exterior diameter is at most `2R_ext`, and

```text
E_k=F_N^c for every k>=K_ext:=2R_ext.                (1.10)
```

For all those polynomially growing radii, M62 and complement symmetry give

```text
Phi_pm^K(C_k)>=1/(24N^13).                           (1.11)
```

Diameter is used only to prove exact set saturation in (1.10), never to
infer conductance at an intermediate radius.

**Claim D (exact N=5 closure and full flow).**  For the accepted balanced
path-core choice at `N=5,m=8`,

```text
|A|=3,904,
|F_5^c|=762,940,
|L_0|=314,771,
|L_1|=448,169,
L_2=empty.                                            (1.12)
```

Thus the exterior closes exactly at radius one.  The two exact global cuts
have

```text
pi(C_0)=63,735/354,188,
Phi_pm(C_0)
 =113047114123584102629/418163570101368000000
 =0.27034185234304386...,

pi(C_1)=191,711/442,735,
Phi_pm(C_1)
 =1521791645588931368459/8553111823588026240000
 =0.17792257098663075....                             (1.13)
```

The exact H3/H4/H5 and `F_N minus A`/next-exterior-shell splits are in the
machine-readable artifact.  Claim D is a finite falsifier, not evidence for
an asymptotic gap.

No Terminal-B family is proved.

## 2. Full argument and constructions

### 2.1 Proof of the exact breadth-first identity

The positive-transition graph of `K` is undirected: two words have positive
transition probability exactly when they occur in the same exact
same-product conditional fiber, and heat-bath transition probabilities are
symmetric under the uniform law.

Every exterior neighbor of `A` is in `E_0`.  Every exterior neighbor of
`E_(k-1)` is in `E_k`.  Therefore an exterior boundary edge of `C_k` can
only start in its last layer `L_k`, and its target is exactly in
`L_(k+1)`.  Every remaining boundary target is a minimal full-support word
outside `A`, namely a member of `F_N minus A`.  These categories are disjoint
and exhaustive, proving (1.3).  Uniform stationarity cancels the common
factor `W^(-1)` against the smaller-side mass and proves (1.4).  This
argument does not drop H4 or H5; they occur in the sums in (1.3).

### 2.2 Minimum transition, alternate targets, and layer growth

For any positive off-diagonal transition, at least one `(r,i)` conditional
outcome supplies it.  Its exact contribution is

```text
1/[2|R_m|(m-r+1)|F_r(g)|].                            (2.1)
```

Since `|F_r(g)|<=M^r<=M^5` and `m-r+1<=m-2`, (2.1) is at least `p_min`.
Every `y in L_(k+1)` has at least one predecessor in `L_k`; choosing one per
target gives

```text
W^(-1) sum_(x in L_k)K(x,L_(k+1))
 >=W^(-1)p_min|L_(k+1)|.                              (2.2)
```

M63 proves that the path-core cut is saturated by deletion cells, that
`|A|<=Lambda_N|Z|`, and that every cell base supplies `N-2` distinct
full-support alternate leaf attachments outside `A` and outside every
exterior halo.  Their exact padded-H3 probability is
`1/[6(m-2)D_N]`.  Hence

```text
W^(-1) sum_(x in C_k)K(x,F_N minus A)
 >=W^(-1)alpha_N|A|.                                 (2.3)
```

Equations (1.3), (2.2), and (2.3) prove (1.6).

For one word, one window of length `r` has at most `M^r` ordered outcomes,
so its number of distinct positive neighbors is at most `D_out`.  Every
state in `L_(j+1)` has a predecessor in `L_j`; therefore

```text
|L_j|<=D_out^(j+1)|A|,
```

and summing proves (1.7).  Since the smaller-side denominator is at most
`pi(C_k)`, M63's alternate-target bound gives

```text
Phi_pm(C_k)
 >=alpha_N/[1+sum_(j=1)^(k+1)D_out^j].               (2.4)
```

For `N>=5,m=2N-2`, use

```text
D_out<=6NM^5<=N^11,
alpha_N>=1/(96N^6),
1+sum_(j=1)^(k+1)D_out^j<=3D_out^(k+1),
```

which proves (1.8).

### 2.3 Support-component genus accounting

Let a nontrivial support component on `v_i` vertices have word length `k_i`.
The inherited connected-factorization feasibility theorem gives a unique
integer `g_i>=0` such that

```text
k_i=2(v_i-1)+2g_i.                                   (2.5)
```

Count isolated labels as components with `v_i=1,k_i=g_i=0`.  If there are
`c` total labeled components, then

```text
2N-2=sum_i k_i=2(N-c)+2sum_i g_i,
sum_i g_i=c-1.                                       (2.6)
```

Thus every exterior state (`c>=2`) has a surplus component.

### 2.4 Merging down to two components inside the exterior

The accepted quantitative Classification-H construction says that any two
words in one labeled weighted-component macro are at Hurwitz distance at
most

```text
H_N=50Nm^3.                                          (2.7)
```

In particular one can reach a paired representative in which every tree
edge and every surplus pair is adjacent.  A project Hurwitz move on an
adjacent factor pair is one literal H3 transition after padding it on either
available side by an unchanged factor.  It preserves the macro and hence
stays exterior.

Choose a component `U` with `g_U>=1`, expose one surplus square `e,e`, and
choose any other component `V`.  Replace that pair by a square `s,s` whose
edge crosses from `U` to `V`; pad by one unchanged neighbor to make the move
a literal H3 update.  The two components merge.  Their new genus is

```text
g_(U union V)=g_U+g_V-1>=0.                           (2.8)
```

Thus `(c,sum g)` changes to `(c-1,c-2)` as required by (2.6).  While
`c>=3`, the target still has at least two components and remains in
`F_N^c`.  Repeating at most `c-2` times reaches two components, whose genera
sum to one.

### 2.5 Isolating a prescribed label without entering `F_N`

Fix a label `v`.  If it is already an isolated component, nothing is needed.
Otherwise let `W` be its component and `U` the other component after Section
2.4.  Normalize within that macro to the following tailored paired word.

If `|W|>=3`, choose a spanning tree of `W` in which `v` is a leaf, with leaf
edge `f`, and choose every surplus pair away from `v`.  There is an internal
edge `s` on `W minus {v}`.  Refresh

```text
f f -> s s.                                          (2.9)
```

The result has components `{v}`, `W minus {v}`, and `U`; the middle
component's genus has increased by one.  Refresh the displayed surplus
square to a cross-component square joining `W minus {v}` to `U`.  The two
non-`v` components merge with genus one, leaving exactly the macro

```text
{v} isolated,  [N] minus {v} connected of genus one. (2.10)
```

If `|W|=2`, write its only edge as `f`.  Necessarily `|U|=N-2>=3`, so `U`
has an internal edge `s`.  The paired `W` word contains `1+g_W`, hence one
or two, copies of the square `f f`.  Refresh all of them to `s s`.  The two
labels of `W` become separate isolates and `U` receives the corresponding
surplus pairs.  Refresh one added pair to a cross edge attaching the label
other than `v` to `U`.  Again (2.10) results.  This uses two moves when
`g_W=0` and three when `g_W=1`.

Every replacement in this section is an equality `tt=ss=id`, padded on an
available side; all intermediate macro genera satisfy (2.6), so no step
enters `F_N`.  Finally normalize within (2.10) to a fixed paired word `q_v`.

There are at most `c` Hurwitz-normalization stages and at most `c+1` square
refreshes.  Equations (2.7) and `c<=N` give

```text
length(x to q_v)<=cH_N+c+1<=50N^2m^3+N+1=R_ext.
```

This proves Claim C.  Since M63 explicitly constructs an exterior neighbor
of `A`, choose one `e in E_0`.  Route `e` and an arbitrary exterior `y` to
`q_v` and reverse the second route.  Their exterior distance is at most
`2R_ext`, proving (1.10).  At saturation,
`C_k=F_N^c union A`; M62 applies to its complement `F_N minus A` and proves
(1.11).

### 2.6 Exact N=5 signature-clique audit

For fixed `(r,i)`, two identity words lie in the same conditional heat-bath
fiber exactly when their ordered factors outside the window agree.  Indeed,
the outside prefix and suffix force the window product, and every length-`r`
block with that product completes an identity word.  Thus each outside
context is an exact clique.

The verifier enumerates all `1,770,940` identity words by matching two
four-factor blocks with inverse products.  It identifies exterior words by
support connectivity, constructs each breadth-first layer by equality of one
outside context, and obtains (1.12).  For a context clique of size `T`
containing `a` cut states, its exact directed boundary contribution is

```text
a(T-a)/[6(m-r+1)T].                                  (2.11)
```

Summing (2.11) over every window and every context gives (1.13).  Replacing
`a(T-a)` by the product of the `L_k` and `L_(k+1)` context counts gives the
second term in (1.3); subtraction gives the exact `F_N minus A` term.  The
result retains every block size and is independent of any Monte Carlo
approximation.

## 3. Structurally distinct thick bridge-history candidate

The coordinator's pointwise result seals a single exact prefix-product
fiber, so the second lane uses a thick union.  Put `j=N-1`,
`X_j=t_1...t_j`, let `ell(g)=N-#cycles(g)` be transposition length, and set

```text
P_(N,q)={w:ell(X_j)<=q}.                              (3.1)
```

If `a_j(g)` is the exact number of length-`j` transposition words with
product `g`, then bridge decomposition gives the exact global mass

```text
pi(P_(N,q))
 =sum_(ell(g)<=q)a_j(g)^2/a_(2j)(id).                (3.2)
```

This set contains portions of both the minimal macro and positive-surplus
exterior macros.  It absorbs every Section-13-style H3 target, and every H4
or H5 target, whose update window does not cross the midpoint.  If a crossing
window has `a` old/new factors to the left of the cut, then

```text
X_j^(-1)X'_j=U^(-1)U',
|ell(X'_j)-ell(X_j)|<=2a<=8.                          (3.3)
```

The complete nonlazy action probability of all crossing windows is at most

```text
rho_m=sum_(r=3)^5 (r-1)/[6(m-r+1)]
 <=3/[2(m-4)].                                       (3.4)
```

Therefore the full original-chain boundary satisfies the rigorous upper
localization

```text
Q_K(P_(N,q),P_(N,q)^c)
 <=rho_m pi(q-8<=ell(X_j)<=q).                       (3.5)
```

This accounts for all H3/H4/H5 crossings; locality alone gives only the
polynomial factor in (3.4).  A Terminal-B use would still need the exact
shell in (3.5) to be superpolynomially small relative to the globally
oriented side.

Exact endpoint dynamic programming through `N=8` finds no such finite
effect.  At `N=5`, the endpoint-length masses are

```text
ell=0: 5,780/88,547,
ell=2: 64,017/88,547,
ell=4: 18,750/88,547.                                (3.6)
```

The literal quartile-threshold formulation already has no feasible `q` at
`N=4,5,6`, because one layer jumps across the whole interval `[1/4,1/2]`.
At `N=7,8`, the quartile boundary layer is respectively more than `0.96` and
`0.91` of its lower tail.  Finally the exact full-K N=5 conductances are

```text
Phi_pm(P_(5,0))=0.27528756111570407...,
Phi_pm(P_(5,2))=0.20782831271948604....               (3.7)
```

Only midpoint-crossing windows contribute, and every H3/H4/H5 contribution
is recorded exactly in the JSON.  These finite values reject no asymptotic
theorem, but they refute the small-N universal quartile formulation and show
that the first thick endpoint shell is not a hidden finite obstruction.

## 4. Worst probability, runtime, path length, and congestion accounting

- Every specified padded H3 move in the exterior path has exact probability
  `1/[6(m-2)|F_3(g)|]>=1/[6(m-2)M^3]` for `N>=5`.
- Every arbitrary positive edge used in (1.6) has probability at least
  `p_min` in (1.5), including laziness, block-size choice, window choice,
  and conditional-fiber size.
- The path to `q_v` has length at most `R_ext`; the exterior diameter is at
  most `2R_ext`.  No congestion is claimed or inferred from these paths.
- Fixed-radius mass growth uses exact support outdegree at most `D_out`; it
  does not route flow through a common hub.
- The signature-clique verifier has exact state count `1,770,940`, uses no
  random seed, and ran in `16.93` seconds.  The independent construction-only
  E0 check ran in `10.31` seconds and returned the same `314,771` states.
- The midpoint endpoint DP through `N=8` and the N=5 full-boundary verifier
  are deterministic; the latter ran in roughly `16` seconds.  No finite
  runtime is used as a universal proof dependency.

## 5. Dependencies, with status

1. **PROVED HERE:** exact layer identity (1.3), shell criterion (1.6),
   fixed-radius theorem (1.8), exterior macro surgery and connectivity,
   saturation radius (1.10), thick midpoint mass/action formulas, and the
   signature-clique counting formula.
2. **PROVED / INHERITED M63:** deletion-cell saturation, `Lambda_N`, and the
   alternate full-support leaf targets giving `alpha_N`.
3. **PROVED / INHERITED M60--M62:** every nonempty subset of `F_N` and its
   macro-closed complement placement has conductance at least `1/(24N^13)`.
4. **PROVED / INHERITED M13, LEDGER L-0037:** Classification H and the
   quantitative within-macro Hurwitz diameter `50Nm^3`, with the paper/project
   inverse-generator convention already reconciled.
5. **PROVED / INHERITED:** connected identity feasibility
   `k=2(v-1)+2g`, exact H3 fiber size/bounds, reversibility, and stationarity.
6. **EXACT FINITE:** N=5 exterior layers and rational full boundary; midpoint
   endpoint masses through N=8; N=5 midpoint rational full boundary.
7. **UNRESOLVED:** uniform expansion of genuinely growing intermediate
   exterior layers; asymptotic no-cliff/outward-action for the thick midpoint
   length shell.

## 6. First unproved standalone proposition

**INTERMEDIATE EXTERIOR-LAYER EXPANSION.**  There are universal
`c>0,C<infinity` such that, for every `N>=5` and every integer

```text
0<=k<2(50N^2(2N-2)^3+N+1),
```

the exact layers (1.2) satisfy

```text
alpha_N|A|+p_min|L_(k+1)|
 >=cN^(-C) min{|C_k|,|Omega(N,2N-2)|-|C_k|}.         (6.1)
```

Proving (6.1) would reject every multistep exterior-closure cut.  Refuting
the cut route requires an explicit growing radius at which the *complete*
two terms in (1.3), not merely the lower-bound terms in (6.1), are
superpolynomially small relative to the correctly oriented side.

## 7. Strongest self-attack / failure mode

Polynomial exterior diameter does not control the conductance of an
intermediate breadth-first ball.  Two large regions joined by a thin neck can
have polynomial diameter.  The canonical word `q_v` is used only to prove
eventual equality `E_k=F_N^c`; using those paths as comparison flow would
recreate the forbidden hub-congestion error.

Likewise, (1.8) loses a factor `N^11` per layer.  It is useful for every fixed
radius but becomes superpolynomially weak as soon as `k` grows.  The N=5
two-layer saturation is especially nonrepresentative: two windows of length
five can cover an eight-factor word, whereas at general `m=2N-2` a bounded
number of windows cannot rewrite a generic ordered word.

The exterior connectivity construction depends on the accepted quantitative
Classification-H audit.  Its delicate cases are a two-vertex component of
genus zero or one; Section 2.5 explicitly refreshes respectively one or two
copies of its only edge square before the final merge.  A fresh referee
should recheck those macro genera and every padding position.

Finally, the midpoint shell is only a candidate reduction.  Formula (3.5)
is an upper bound useful for a bottleneck, not a lower conductance theorem;
an asymptotic shell cliff could still exist despite the finite data.

## 8. Calibration suite and artifacts

### Calibration

- Odd `m`: `Omega` is empty.  The theorem uses even `m=2N-2`.
- `m=0` and `N=2` even are singleton calibrations; `m=2,N>=3` is excluded.
- `S_3,m=4` has 27 words and four pure-Hurwitz components.  Here `|R_m|=2`
  and H4 is a whole-word heat bath.  The balanced two-leaf core cut starts
  only at `N=5`; no N=3 theorem is silently asserted.
- `S_4,m=4` has 120 words and 13 Hurwitz components; its H4 whole-word move
  cannot be dropped.  `S_4,m=6` has 3,936 words and 17 Hurwitz components;
  the midpoint square-sum computation reproduces 3,936 exactly.
- At `N=5,m=8`, the exact bridge count is 1,770,940 and the minimal macro
  count is 1,008,000.  Equations (1.12)--(1.13) account for all remaining
  762,940 states and every boundary transition.
- Near-minimal doubled-tree representatives are used only as feasible paired
  words.  The proof retains full word order and labeled component data;
  disjoint components are not collapsed to an unordered graph.
- No parity-only invariant, length-two simulation, finite-spectrum
  extrapolation, or random-slot heuristic is used.
- The fixed paired word in Claim C is a connectivity endpoint, not a
  stationary-flow hub.  No polynomial mixing conclusion is drawn from it.

### Artifacts and exact commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/
```

Commands from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -u experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/exact_n5_signature_closure.py \
  --max-radius 20 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/exact-n5-signature-closure.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/midpoint_shell_audit.py \
  --max-n 8 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/midpoint-shell-N3-N8.json

PYTHONDONTWRITEBYTECODE=1 python3 -u experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/exact_n5_midpoint_conductance.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/exact-n5-midpoint-conductance.json
```

Metadata: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python 3.12.3, seed `null`, no
nonstandard dependency.

SHA-256:

```text
27d81e340d1db76e27f621b6c1e04029c96a775ea083fbe3e4fcfd4a4dd4600a  exact_n5_exterior_closure.py
e3d7d2508a9c3d97f6e8681344dc7214fca5e31d548b02c0862081c2caf0cd08  exact_n5_midpoint_conductance.py
e5d6200de117e93392cd95f0dbd3571cb385d0cd76756ab8e4eea497cd88feb1  exact_n5_signature_closure.py
5ad67069a71d95560159a414b74145f17b09fe2af36e66dced428e5c79a92ab3  midpoint_shell_audit.py
6db1999920846c7be40adb8376378747f9b76a018a63a6766bc4d8bba6548d08  exact-n5-E0.json
2ef0698a7342ac84f740c6e51d04eb1030dc3559b09d8e2e1c797e15e432d461  exact-n5-midpoint-conductance.json
7e9d58ff6248d53b07ae20b285076973a2c24327a84c59df60521d8c7f47c124  exact-n5-signature-closure.json
f6811276ed8640f0c6d49e78189559ec9847a9485edf8773967feadb2aa7cf55  midpoint-shell-N3-N8.json
```

The exact closure calculation can falsify the layer identity, signature
clique formula, immediate-saturation claim, or a missing r=3,4,5 category.
The endpoint calculations can falsify the bridge mass formula, claimed
noncrossing invariance, or bounded-N no-cliff statement.  None can establish
asymptotic expansion without the proof requested in Section 6.

## 9. Verdict

**OPEN AT A NAMED STEP: INTERMEDIATE EXTERIOR-LAYER EXPANSION.**

The assigned Terminal-B search did not produce an irreducibility failure or
a superpolynomial full-K conductance family.  Every fixed halo radius and
every radius after the explicit polynomial saturation time is rigorously
polynomially leaky; the exact remaining implication is (6.1).
