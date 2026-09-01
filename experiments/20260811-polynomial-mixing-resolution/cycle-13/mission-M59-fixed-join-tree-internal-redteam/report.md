# M59 final report: fixed join-tree internal red team

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  The chain is exactly

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

where `H_(i,r)` is uniform on the ordered length-`r` transposition words with
the same ordered product.  The target is uniform on the global
`Omega(N,m)`.

For `m=2N-2`, let `F_N` be the minimal connected full-support identity macro,
`T_J(w)` its prefix join tree, and

```text
F_N(T)={w in F_N:T_J(w)=T}
```

for a fixed labeled tree `T`.

This mission proves three scoped results.

**Claim 1 (exact fiber/chain characterization; proved).** For every `N>=2`
and every labeled tree `T`, `F_N(T)` is exactly the set of paths of the
prefix automaton in Section 2.1 below.  For `N>=3`, its literal rejected-exit
`H3/H4/H5` restriction is exactly the union of the conditional bucket cliques
in Section 2.2, with the original global conditional-fiber denominators.

**Claim 2 (uniform full-K rejection of thin edge-chronology cuts; proved).**
Let `N>=3`, `m=2N-2`, fix `T` and `e in E(T)`, and write `rho_e(w)` for the
rank of `e` among the `N-1` join events and `j_e(w)` for its factor position.
For either statistic `s in {rho_e,j_e}`, every nonempty threshold side

```text
A_<={w in F_N(T):s(w)<=q},
A_> ={w in F_N(T):s(w)>q}
```

viewed as a cut in the global `Omega(N,m)`, satisfies

```text
Phi_pm^K(A)
 :=Q_K(A,A^c)/min{pi(A),pi(A^c)}
 >= 1/[2|R_m| binom(m,2)(N-1)^2 (m-2)D_N]
 >= 1/(48N^7),                                      (1.1)

D_N=(3N^2+N-12)/2.
```

For `N>=4`, `|R_m|=3`, so the first denominator is exactly
`6 binom(m,2)(N-1)^2(m-2)D_N`.  At `N=3,m=4`, `|R_m|=2` and the exact bound is
stronger.  All `H4/H5` flow is retained as nonnegative additional flow.

**Claim 3 (bounded exact falsification; proved finite fact only).** Every
fixed labeled tree restriction is connected at `N=4` and `N=5`.  At `N=4`
this is exhaustive over all 16 labeled trees and 3,936 identity words.  At
`N=5`, exact dynamic programming treats one representative of each of the
three unlabeled tree shapes; conjugation equivariance covers all 125 labeled
trees.  This is not a universal connectivity or gap theorem.

Neither Claim 2 nor Claim 3 resolves the assigned universal restriction/
mean-lift target or Terminal B.

## 2. Full argument and construction

### 2.1 Exact fixed-tree automaton

Scan a word from left to right.  A prefix state is `(p,S)`, where `p` is its
permutation product and `S subseteq E(T)` is the set of support-component
join factors already seen.  The support components of the prefix are exactly
the components of the forest `(V,S)`: internal factors do not change them,
and every join factor merges two of them.

For the next transposition `a={x,y}`, there are exactly two allowed cases:

1. `x,y` lie in the same component of `(V,S)`, and `S` stays fixed;
2. `a` is an unused edge of `T` joining two components, and `S` becomes
   `S union {a}`.

Any other cross-component factor would itself become a join edge outside
`T`.  This proves necessity.  Conversely, an automaton path from
`(id,empty)` to `(id,E(T))` has precisely the edges of `T` as its joins, has
connected support, length `2N-2`, and product identity.  It is therefore in
`F_N(T)`.  This proves Claim 1's fiber statement without enumeration.

### 2.2 Exact rejected-exit bucket operator

Fix `r,i`, an outside prefix `u`, outside suffix `v`, and a block product
`g`.  Let `B` be the fixed-tree words of the form `u b v` with
`b in T_N^r` and product `g`.  Every word belongs to exactly one such bucket
for each `(r,i)`.  Write

```text
F_r(g)={b in T_N^r:product(b)=g}.
```

The global chain assigns every ordered replacement in `F_r(g)` the weight

```text
1/[2|R_m|(m-r+1)|F_r(g)|].                         (2.1)
```

Rejecting exits from `F_N(T)` turns the words of `B` into a conditional
clique and sends every other outcome to the holding probability.  In the
principal minimal regime `N>=4`, (2.1) is
`1/[6(m-r+1)|F_r(g)|]`.

If `B` has `b` words and `a` of them lie in a candidate set `A`, its exact
directed contribution, already including laziness, block-size choice, window
choice, and heat-bath multiplicity, is

```text
full K:        [1/(6(m-r+1))] a(|F_r(g)|-a)/|F_r(g)|,
restriction:   [1/(6(m-r+1))] a(b-a)/|F_r(g)|.       (2.2)
```

The exact harness sums (2.2) over every bucket and every `r=3,4,5`.

### 2.3 Leaf-strand counting input

Fix a tree leaf `v`, with incident edge `f={v,u}`.  Erasing strand `v` from
the prefix permutation path makes every projected increment either a
transposition on `X=[N] minus {v}` or the identity.  For a minimal word there
are exactly two identity increments.  Deleting them gives

```text
Del_v(w) in F_(N-1)(T-v).                            (2.3)
```

Every old join edge other than `f` survives as the same transposition and in
the same relative order; the two null positions alone are removed from the
factor-position chronology.  For fixed base word and fixed null positions,
there are at most `(N-1)^2` lifts.  Hence every deletion fiber has size at
most

```text
Lambda_N=binom(m,2)(N-1)^2.                         (2.4)
```

This is the accepted M49 strand-deletion lemma; its proof follows the exact
insertion-coordinate right-multiplication table and does not use an
enumerative asymptotic.

### 2.4 Proof of the chronology anti-bottleneck theorem

Fix the distinguished edge `e`.  A tree on at least three vertices has a leaf
`v` whose incident edge `f` is not `e`: a tree has two leaves, and `e` cannot
join both leaves unless the tree has only two vertices.  Use this `v` in
(2.3).

First take the low rank side `A={rho_e<=q}` and let `Z=Del_v(A)`.  Removing
`f` from the join order changes `rho_e` by either zero or minus one, so every
`z in Z` has `rho_e(z)<=q`.  Embed `z` on `[N]` fixing `v` and define

```text
S_z=z f f.                                           (2.5)
```

The first `f` joins leaf `v`, the second is internal, and `f` is last in the
join order.  Thus `S_z in A`.  Distinct bases give distinct sources.  By
(2.4),

```text
|A|<=Lambda_N |Z|,
```

so at least a `1/Lambda_N` fraction of `A` consists of sources (2.5).

For the high rank side `A={rho_e>q}`, instead use

```text
S_z=f f z.                                           (2.6)
```

If `f` preceded `e` in the original lift, deletion reduces the rank by one
and prepending restores it; otherwise prepending increases it.  In either
case `rho_e(S_z)>=rho_e(w)>q`.  The same source fraction follows.

For a factor-position threshold, deletion changes `j_e` to `j_e-k` for some
`k in {0,1,2}`.  Appending (2.5) preserves `j_e-k<=j_e`, so it stays in every
low side.  Prepending (2.6) adds two positions, giving
`j_e-k+2>=j_e`, so it stays in every high side.  The same count therefore
handles both statistics and both orientations.

It remains to exhibit literal K boundary from every source.  Choose any
transposition `s` supported on `X`.  If `c` is the last factor of `z`, the
last length-three window in (2.5) is

```text
c f f,
```

with product `c`; the block `c s s` has the same product.  The resulting word
is `z s s`, which omits `v` and hence lies outside `F_N`, and outside `A`.
For (2.6), use the first window `f f c` and outcome `s s c`, obtaining
`s s z`, again omitting `v`.

The exact length-three same-product fiber over a transposition has size

```text
|F_3(c)|=D_N=(3N^2+N-12)/2.
```

Thus each source has one specified exit of probability

```text
p_0=1/[2|R_m|(m-2)D_N].                              (2.7)
```

Every subset of one fixed labeled tree fiber has global stationary mass at
most one half.  Indeed, a labeled tree has a distinct conjugate for `N>=3`,
and simultaneous relabeling bijects their disjoint, equally sized fibers.
Uniformity of `pi` and (2.4)--(2.7) now give

```text
Q_K(A,A^c)/pi(A)>=p_0/Lambda_N.
```

This is the first inequality in (1.1).  Finally,
`binom(m,2)<=2N^2`, `(N-1)^2<=N^2`, `m-2<=2N`, and
`D_N<=2N^2`, proving the coarser `1/(48N^7)` bound.  No path routing or
canonical hub is used.

### 2.5 Exact bounded results and the failed counterexample family

At `N=4,m=6`, exhaustive enumeration gives 3,936 identity words, 2,880
minimal full-support words, and 16 labeled tree fibers.  Four star fibers have
size 186 and twelve path fibers size 178.  Every rejected-exit support graph
is connected, with exact diameter at most 2.  Among the named cuts, the
minimum full-K escape is

```text
1041421447/2486764800 = 0.4187856636...,
```

and the minimum restriction escape is

```text
600121/107069040 = 0.0056049909....
```

At `N=5,m=8`, automaton dynamic programming and exact buckets give:

| tree shape | labeled copies | fixed-fiber size | components |
|---|---:|---:|---:|
| star | 5 | 8,856 | 1 |
| path | 60 | 7,808 | 1 |
| T | 60 | 8,254 | 1 |

The weighted sum is
`5(8856)+60(7808)+60(8254)=1,008,000`, the exact size of `F_5`; the global
bridge has 1,770,940 words.  The thinnest tested restriction cut is the star
event `rho_e<=2`, with 4,428 of 8,856 states and

```text
restriction escape =
110972985703459/131702333737927680
=0.0008426045503816381...,

full-K escape =
2267545133196643259/5487597239080320000
=0.413212747657236....
```

The full flow is the sum of the exact `H3/H4/H5` terms in the JSON artifact.
Thus this explicit half-rank family looks much thinner after rejecting tree
exits, but those exits destroy it as a full-K bottleneck.  Leaf-null
separation, join time, midpoint join count, and midpoint largest-component
thresholds likewise have positive exact full flow.  These finite results only
falsify disconnects or zero-flow instances at the tested sizes.

## 3. Probability, runtime, path length, and congestion accounting

- The universal certificate uses a `1/Lambda_N` source fraction and one exact
  H3 outcome of probability `p_0` in (2.7).  The worst proved full-K escape is
  `1/[2|R_m|Lambda_N(m-2)D_N]>=1/(48N^7)`.
- The block formula (2.2) accounts for every block length, window, and target
  multiplicity.  `H4/H5` are not discarded in the exact computation and are
  nonnegative in the analytic lower bound.
- There are no comparison paths and no congestion claim in Claim 2.
  Recognizing the tree/statistic and constructing a source/certificate takes
  polynomial time, `O(mN)` with direct prefix/strand tables.
- For one fixed tree, the bounded DP has at most
  `O(m 2^(N-1) N!)` prefix states and `M=binom(N,2)` transitions per state;
  positive-completion enumeration costs an additional output-linear term.
  Product-fiber tabulation costs `O(M^5)`.  These are exact bounded
  falsification costs, not a polynomial sampler.
- The recorded all-shape N=5 run used Python 3.12.3, no nonstandard package,
  no randomness, and 3.828243811847642 seconds before JSON writing.

## 4. Dependencies with status

1. **PROVED HERE:** the fixed-tree automaton and conditional bucket
   characterization; equations (2.1)--(2.2); the chronology threshold source
   injection; exact mass orientation; and (1.1).
2. **PROVED / INHERITED FROM ACCEPTED M49:** leaf-strand deletion, exactly two
   null increments, preservation of surviving join order, output tree `T-v`,
   and the multiplicity bound (2.4).
3. **PROVED / INHERITED COMMON-CORE LEMMA:**
   `|F_3(c)|=D_N` for every transposition `c`, and the padded adjacent-square
   H3 refresh probability (2.7).
4. **PROVED / INHERITED:** uniform heat-bath reversibility/stationarity and
   irreducibility of global `K`.  Irreducibility is not used to manufacture
   any finite gap claim here.
5. **EMPIRICAL IN THE ASYMPTOTIC SENSE, BUT EXACT FINITE FACT:** the complete
   N=4 and N=5 connectivity/flow calculations.
6. **UNRESOLVED:** a universal fixed-tree restriction Poincare or mean-lift
   inequality.

## 5. First unproved standalone proposition

**FIXED-TREE LEAF-CELL EXPANSION.** For `N>=4` and every labeled tree `T`, let
`K_T` be the literal rejected-exit restriction of `K` to `F_N(T)`.  For every
tree leaf `v` and base `z in F_(N-1)(T-v)`, put

```text
C_(v,z)={w in F_N(T):Del_v(w)=z}.
```

Let `P_T^leaf` choose a tree leaf uniformly and exactly heat-bath resample the
current word within its nonempty cell `C_(v,z)`.  Prove universal
`c>0,C<infinity` such that, simultaneously for all `N,T`,

```text
gap(P_T^leaf)>=cN^(-C)
and
E_(P_T^leaf)(f,f)<=N^C E_(K_T)(f,f) for every f.     (5.1)
```

Equation (5.1) would give a universal fixed-tree restriction gap without
paying a fresh polynomial loss at every recursive leaf deletion.  It is
strictly stronger than the proved cardinality bound `|C_(v,z)|<=Lambda_N`;
the missing point is local communication among insertion histories and
between overlapping leaf cells.

## 6. Strongest self-attack / failure mode

The `1/(48N^7)` theorem rejects only join-rank and join-position thresholds.
Its boundary deliberately exits the fixed tree and even the minimal macro,
so it gives no restriction gap and no mean-lift inequality.  A hidden cut can
vary among insertion histories inside every `(v,z)` cell while avoiding the
endpoint-square sources counted here.  Exact connectivity through `N=5`
cannot preclude such a cut at growing `N`, and the small N=5 restriction flow
already warns that rejected-exit geometry can be much thinner than full K.

The natural strategy of routing every lift to `zff` or `ffz` would turn these
sources into canonical hubs.  Although a single deletion fiber is only
polynomially large, iterating this normalization through `N` leaves can
accumulate an exponential load.  No such routing is claimed.  Finally, even
a superpolynomially slow `K_T` would not by itself prove Terminal B unless a
globally oriented cut also controls all tree-changing and macro-exit flow.

## 7. Calibration suite

- Odd `m`: `Omega` is empty; no claim is made.
- `m=0` and `N=2` even: singleton calibrations; the fixed-tree theorem starts
  at `N=3`.  The disconnected `m=2,N>=3` case is excluded and no length-two
  simulation is used.
- `S_3,m=4`: the global bridge has 27 words and pure Hurwitz has 4 components.
  Here `H4` is whole-word, `|R_m|=2`, and the H3 coefficient in (2.7) is
  stronger than the uniform `1/6` lower bound.  Whole-word H4 is retained.
- `S_4,m=4`: 120 words and 13 Hurwitz components; whole-word H4 again cannot
  be omitted.  This is below the connected full-support minimal length for
  four labels.
- `S_4,m=6`: the exact harness reproduces 3,936 words, 2,880 minimal
  full-support words, and all 16 labeled fixed-tree fibers connected.  The
  inherited pure-Hurwitz count is 17 components.
- Connected near-minimal doubled-tree words `e_1e_1...e_(N-1)e_(N-1)` realize
  arbitrary join-edge orders, so proper rank threshold sides are genuinely
  nonempty.  They are used only as calibration, never as routing hubs.
- The automaton and buckets retain the complete ordered word.  No commuting-
  component/color interleaving is quotiented out.
- No edge-multiplicity or degree-parity characterization is used.  The known
  length-two local-simulation failure is irrelevant to the literal H3 move.
- Every analytic and finite cut is oriented in the global uniform bridge.
  A fixed labeled tree fiber has mass at most one half by its disjoint equal-
  size conjugate; the N=5 artifact also records each exact mass numerator over
  1,770,940.

## 8. Artifacts and reproduction

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-13/mission-M59-fixed-join-tree-internal-redteam/
```

Commands, from repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M59-fixed-join-tree-internal-redteam/fixed_tree_restriction_audit.py \
  --N 4 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M59-fixed-join-tree-internal-redteam/fixed-tree-N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M59-fixed-join-tree-internal-redteam/fixed_tree_dp_bucket_audit.py \
  --shape all \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M59-fixed-join-tree-internal-redteam/fixed-tree-N5-all.json
```

Metadata: commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python
3.12.3, seed `null`, and no nonstandard dependency.

SHA-256:

```text
6a7527145714c9febaded86c398a218fe22c52f0df02c9876d169a8deba72730  fixed_tree_restriction_audit.py
770f26b0544b34cddd11af65de6979aba9eca7abf47f559eedf30ed1fbc2fb1c  fixed-tree-N4.json
07419be4cfb61cd2a1d5b9168e17736fdf80508803fccc2672b42bbdf829c473  fixed_tree_dp_bucket_audit.py
38d6d5d372534356ccfeb412c87e397f4f7cf8268c9a39fd227f8ebfe03e8b0b  fixed-tree-N5-all.json
```

The preliminary `fixed-tree-N5-star.json` is retained as an append-only
single-shape run; `fixed-tree-N5-all.json` supersedes it for conclusions.

## 9. Verdict

**OPEN AT A NAMED STEP: FIXED-TREE LEAF-CELL EXPANSION (5.1).**

Claims 1--3 are proved in their stated scope.  They do not prove Terminal A
or Terminal B.

