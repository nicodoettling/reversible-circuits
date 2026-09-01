# M27 final report: base-scale exceptional modes and minimal factorizations

Date: 2026-08-11. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This report is a nonterminal scoped result.  It does not prove the universal
base-scale bridge gap, Terminal A, or Terminal B.

## 1. Exact claims, quantifiers, and convention

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are multiplied
left-to-right.  Let `E=T_N^2`, `p(a,b)=ab`, and let
`Omega_l(h)` be the uniform `E`-word bridge with ordered product
`h in A_N`.  Put

```text
d(h)=N-#cycles(h),             g=l-d(h)/2,
M=binom(N,2).
```

The following claims are proved.

1. **Square-indicator compression and microfiber modes.**  For every
   `N>=3`, every feasible `h`, and every `l>=1`, put
   `I_i=1{p(X_i)=e}`.  Pointwise,

   ```text
   S=sum_i I_i <= g.                                    (1.1)
   ```

   If `0<Var(I_1)`, the normalized additive Gram matrix compressed to
   `span{I_i-EI_i:1<=i<=l}` has operator norm at most

   ```text
   max{g/l,1/(l-1)}.                                    (1.2)
   ```

   The expression `1/(l-1)` is omitted at `l=1`.  If an indicator has
   zero variance, that direction is absent.  Separately, the full subspace
   of one-coordinate functions centered inside each product fiber,
   `E[f(X_i)|p(X_i)]=0`, is Gram-orthogonal to the product-level subspace
   and has additive eigenvalue exactly `1/l`.  Thus the still-open
   correlation problem reduces exactly to functions of the increments
   `G_i=p(X_i)`.  Claim (1.2) is only a compression bound: the square
   span need not itself be invariant inside that product-level problem.

2. **Minimal long-cycle fixed-multiset restrictions.**  Let `n=2l+1`
   be odd, `r=n-1=2l`, and let the endpoint be
   `c=(0 1 ... r)`.  Let

   ```text
   L_n=(r-1)^(-1) sum_(i=1)^(r-1) G_i
   ```

   be the nonlazy adjacent raw-pair same-product heat bath on reduced
   transposition factorizations of `c`.  For every feasible sorted
   Stanley parking multiset `beta`, let `L_n^beta` denote the
   rejected-exit restriction.  Then

   ```text
   gap(L_n^beta)
     >= (2/3)[1-cos(pi/r)]/(r-1).                       (1.3)
   ```

   Let `B_l` be the nonlazy uniform scan of aligned two-increment
   (four-raw-factor) heat baths, and restrict it to the same multiset.
   Then

   ```text
   gap(B_l^beta)
     >= [2/(3M^4)] [1-cos(pi/r)]/(r-1)
     >= 4/[3M^4 r^2(r-1)].                             (1.4)
   ```

   Singleton restrictions use the usual gap-one convention.  Repeated
   labels, rare labels, endpoint windows, and the one-multiset case are
   included.  The projected stationary mass is exactly

   ```text
   bar_pi(beta)=r!/[n^(n-2) product_a m_a!],            (1.5)
   ```

   where `m_a` are the label multiplicities.

3. **An ideal minimal-sector chain.**  Pollak's diagonal quotient
   `Z_n^r/<(1,...,1)>` is the parking-function set.  The chain `D`
   which chooses one raw quotient coordinate uniformly and replaces it by
   an independent uniform element of `Z_n` is reversible for the uniform
   law and satisfies

   ```text
   gap(D)>=1/r.                                         (1.6)
   ```

4. **Exact binary macro rate and bypass.**  For arbitrary `a,b>=1`,
   `r=a+b`, `n=r+1`, and the projected nonlazy chain
   `bar L_n`, set

   ```text
   alpha=0^a 1^b,             beta=0^(a+1)1^(b-1).
   ```

   Then

   ```text
   bar L_n(alpha,beta)
     =2/[3(r-1)binom(r,a)].                             (1.7)
   ```

   Hence a balanced direct Dyck edge is exponentially rare.  If `b>=2`
   and `gamma=sort(0^a 1^(b-1) b)`, nevertheless

   ```text
   bar L_n(alpha,gamma)=2b/[3r(r-1)],
   bar L_n(gamma,beta)
     =2/[3r(r-1)] [1-1/binom(r-1,a)]
     >=1/[3r(r-1)].                                    (1.8)
   ```

   Thus this explicit rare edge has a polynomial two-hop bypass.  For the
   paired bridge, use the even-`r` subfamily.

5. **Two direct tree transfers are refuted.**  The raw factorization-tree
   measure for the 5-cycle is not negatively associated: for
   `e={0,1}` and `f={2,4}`,

   ```text
   P(e,f)=24/125,
   P(e)P(f)=(64/125)(36/125),
   24*125-64*36=696>0.                                 (1.9)
   ```

   Therefore it is not strongly Rayleigh.  This persists along the
   model-compatible infinite family obtained by adjoining any number of
   disjoint 3-cycles at minimal length.  Conversely, Stanley's genuine
   uniform-Cayley-tree bijection is asymptotically nonlocal: the one-rank
   pair

   ```text
   w_n=((0,1),(1,2),(2,n-1),(2,n-2),...,(2,3)),
   v_n=((0,2),(0,1),(2,n-1),(2,n-2),...,(2,3))
   ```

   maps to trees with edge symmetric difference `2(n-2)` and Prüfer
   codes at Hamming distance `n-2`.  These facts refute direct one-edge
   UST-basis domination and direct one-coordinate Prüfer domination, not a
   randomized reverse comparison.

## 2. Full argument

### 2.1 Square count and the exact product/microfiber split

If `p(X_i)=e`, the two raw transpositions in `X_i` are equal.  Delete
all such adjacent squares.  The remaining `2(l-S)` transpositions still
multiply to `h`, while the reflection length of `h` is `d(h)`.
Therefore `2(l-S)>=d(h)`, proving (1.1).

The identity markers are exchangeable even though an arbitrary
noncommutative bridge is not coordinate-exchangeable.  On adjacent
increments use the Hurwitz bijection

```text
(x,y) -> (y,y^(-1)xy).
```

It preserves the ordered product, swaps their conjugacy classes, and
preserves the central two-transposition increment weights.  It lifts
bijectively to microstates by conjugating both raw transpositions in the
second output coordinate by `y^(-1)`.  Adjacent bijections generate all
permutations of the identity markers.

Write `p=E I_1` and let `rho=Corr(I_1,I_2)` when the variance is
positive.  From `0<=S<=g` one has `S^2<=gS`, hence

```text
Var(S)<=E[S](g-E[S]),
rho <=[(g-1)-(l-1)p]/[(l-1)(1-p)] <=(g-1)/(l-1).       (2.1)
```

The normalized Gram compression is the equicorrelation matrix divided by
`l`.  Its constant-vector eigenvalue is at most `g/l`.  Positive
semidefiniteness gives `rho>=-1/(l-1)`, so every contrast eigenvalue is
at most `1/(l-1)`.  This proves (1.2).

Now condition on the whole increment sequence `G_i=p(X_i)`.  The
microfactor choices are independent and uniform in the fibers
`p^{-1}(G_i)`.  Consequently a fiber-centered function at coordinate
`i` is orthogonal both to every product-measurable function and to every
fiber-centered function at `j!=i`.  Its direct-sum Gram block is the
identity, so the corresponding additive eigenvalue is exactly `1/l`.
This proves the exact reduction to product-increment correlations.

### 2.2 Pollak quotient

Stanley's label bijection sends reduced long-cycle factorizations to parking
functions of length `r=n-1`.  Pollak identifies these with the diagonal
translation orbits of `Z_n^r`.  Gauge the last coordinate to zero.  An
update among the first `r-1` coordinates is then an ordinary product
coordinate heat bath on `Z_n^(r-1)`; updating the last coordinate becomes
a common uniform translation of all the first coordinates.  The latter
Dirichlet form is nonnegative.  The former `r-1` coordinate forms have
total coefficient `1/r` each, so discarding the translation term leaves
the product-chain gap `1/r`, proving (1.6).

### 2.3 Fixed parking-multiset restrictions and aligned H4

A rank-two interval in `NC_n` has two or three middle elements.  Under
Stanley's adjacent-coordinate action, a two-state interval swaps the two
labels.  In a three-state interval, the special state is fixed by the
adjacent transposition and the two nonspecial states are swapped.  Thus,
inside a fixed label multiset, the exact heat bath assigns at least `1/3`
to the adjacent swap, whereas the standard half-lazy adjacent-transposition
chain assigns `1/2` conditional on choosing that position.  Therefore

```text
E_(L_n^beta) >=(2/3)E_(S_adj^beta).
```

The path-interchange gap is
`[1-cos(pi/r)]/(r-1)`; taking a multiset quotient cannot decrease it.
This proves (1.3), uniformly in all multiplicities.

For an off-diagonal `L_n` edge, the two changed adjacent raw positions
are unique.  Choose deterministically an aligned four-position window
containing them: start at the pair for an interior odd start, one position
earlier for an even start, and use the first or last available aligned
window at an endpoint.  Keep the two padding factors fixed.  The target has
the same four-factor product and occurs in the H4 fiber.  The aligned scan
probability is `1/(l-1)` and the fiber contains at most `M^4` words, so

```text
B_l(x,y)>=1/[(l-1)M^4].
```

In a reduced word the raw pair fiber is of size two or three, and
`L_n(x,y)<=1/[2(r-1)]`.  Since `r=2l`, this gives the deliberately
loose edgewise domination

```text
E_(B_l^beta)>=M^(-4)E_(L_n^beta).
```

Rejected exits affect neither retained directed edge.  Combining with
(1.3), then using `1-cos(pi/r)>=2/r^2`, proves (1.4).  Finally, all
permutations of a feasible parking multiset are parking functions, and
Stanley's map is bijective.  Dividing the orbit size
`r!/product_a m_a!` by the total `n^(n-2)` proves (1.5).

### 2.4 Binary macro family

Every factor edge with parking label in `{0,1}` has lower endpoint zero
or one.  Its noncrossing tree is therefore exactly one of two threshold
double-stars: `T_E` contains edge `(0,1)`; `T_V` has the unique
common neighbor `b+1`.  The edge poset of `T_E` is a total chain.  The
term edge poset here is exactly the local order in Goulden--Yong,
Theorem 2.2(f3), with the sufficiency direction supplied by Proposition 2.4
and Lemma 2.5: after factors are numbered in word order, incident edge
numbers decrease clockwise across the interior, and those local
inequalities characterize valid numbered noncrossing chord diagrams.
We cyclically relabel their one-based vertices to zero-based vertices; their
right-to-left action agrees with our declared composition convention, so no
word reversal is introduced.
edge poset of `T_V` consists of chains

```text
z_1<...<z_a,       o_1<...<o_b,
```

with the sole cross relation `o_1<z_a`.  Hence the two trees together
have `1+[binom(r,a)-1]=binom(r,a)` linear extensions.

The triangle on `{0,1,b+1}` can lower one label `1` to `0` in
exactly two source words: the unique `T_E` word and the unique `T_V`
word `0^(a-1)101^(b-1)`.  Each has one scan position and one favorable
outcome in a three-state fiber, proving (1.7).

For the first bypass, contract the first two `o`-edges.  There are
`binom(r-1,a)-1` favorable `T_V` extensions and one `T_E`
extension.  Both nonspecial outcomes in the three-state fiber have macro
`gamma`.  Dividing by `binom(r,a)` gives the first formula in (1.8).
For the reverse second bypass, contract the last two `z`-edges in the
`T_V` representation of `beta`; there are
`binom(r-1,a)-1` favorable words.  Detailed balance, together with

```text
|gamma|=(a+1)|beta|,
(a+1)binom(r,a+1)=r binom(r-1,a),
```

gives the second formula in (1.8).  The complete poset count is frozen in
`binary_macro_formula.md`.

### 2.5 Tree-transfer obstructions

The exact count (1.9) violates pairwise negative association, which is
necessary for a strongly Rayleigh measure.  For the infinite extension,
take the endpoint which is the disjoint union of the 5-cycle and `k`
3-cycles, at its minimal length.  Every minimal factorization stays inside
the endpoint-cycle supports; the number of interleavings is independent of
the component words.  The 5-cycle marginal is therefore unchanged.

The first two factors of `w_n` and `v_n` have the same product, so this
is one rank heat-bath/Hurwitz edge, and both full words multiply to the long
cycle.  Direct application of Stanley's tree construction gives

```text
T(w_n)={(0,1),(1,2)} union {(2,j):3<=j<n},
T(v_n)={(0,1),(0,2)} union {(1,j):3<=j<n}.
```

Their symmetric difference is `2(n-2)`.  Smallest-leaf deletion gives
Prüfer codes `(1,2,2,...,2)` and `(0,1,1,...,1)`, differing in
`n-2` positions.  This proves the claimed asymptotic nonlocality.

## 3. Probability, runtime, path, and congestion accounting

- `L_n` scans exactly `r-1` raw boundaries.  Nontrivial reduced pair
  fibers have size two or three.  The fixed-multiset comparison retains the
  factors `2/3`, `1/(r-1)`, and the half-lazy adjacent-shuffle gap.
- `B_l` scans exactly `l-1` aligned windows.  The crude H4 fiber bound is
  `M^4`, so (1.4) is polynomial in `N,l`.  A direct exact H4 sampler can
  enumerate at most `M^4` candidates, hence has polynomial per-step cost.
- A `D` step samples one coordinate in `O(1)`; maintaining a sorted
  macro costs `O(r log r)` if requested.
- The binary bypass has path length two and both edge probabilities are at
  least inverse quadratic in `r`.  No all-macro flow or congestion bound
  is claimed.
- The UST/Prüfer witnesses have one source-chain edge but tree symmetric
  difference `2(n-2)` and Prüfer distance `n-2`.  This is a locality
  obstruction, not a lower bound on every possible simulation length.
- The exact scripts are exponential finite falsifiers: raw enumeration costs
  `M^r` candidate words.  They are not proposed samplers and are not used
  as universal proof.

## 4. Dependencies

- **Proved here:** (1.1)--(1.9), including all normalization and parity
  qualifications above.
- **Cited:** Richard P. Stanley, *Parking Functions and Noncrossing
  Partitions*, EJC 4(2) (1997), Theorem 3.1, Proposition 4.1, and the
  paragraph after Proposition 3.2, for the parking-label, Pollak-quotient,
  and labelled-tree bijections.
- **Cited and convention-checked:** I. P. Goulden and A. Yong,
  *Tree-like Properties of Cycle Factorizations*, JCTA 98 (2002),
  Theorem 2.2(f1)--(f3), Proposition 2.4, and Lemma 2.5,
  doi:10.1006/jcta.2001.3230.  Their clockwise-decreasing incident-edge
  numbering and right-to-left permutation action give exactly the edge-poset
  linear extensions used in Section 2.4 after the stated zero-based cyclic
  relabeling.
- **Cited:** the path-interchange spectral gap, equivalently Aldous'
  spectral-gap theorem (Caputo--Liggett--Richthammer, JAMS 23 (2010)),
  followed by Markov quotient monotonicity, for the multiset shuffle gap.
- **Cited:** strongly Rayleigh measures are negatively associated; only this
  necessary implication is used to reject the raw-tree route.
- **Inherited, proved/accepted:** the exact M16 Gram representation and CGL
  deletion recursion; the dense-tail bound
  `mu_l(h)<5/(4l)` for `l>=C_mix N log(N+1)`; fixed-`l` bridge gaps;
  and `gap(B_l)>=gap(C_l)/(2l^2)`, `K>=B/12`.  The scoped claims above
  use the Gram representation, but do not assume the unresolved base gap.
- **Empirical only:** the finite JSON files.  They falsify named direct
  transfers or calibrate exact formulas; no finite convergence inference is
  used.

## 5. First unproved standalone proposition

> **PRODUCT-INCREMENT BASE CORRELATION.**  There are universal constants
> `A<infinity` and `l_0<infinity` such that, for every `N>=3`, every
> feasible `h in A_N`, and every
> `l_0<=l<C_mix N log(N+1)`, the top mean-zero eigenvalue of the exact
> additive Gram operator restricted to one-coordinate functions of
> `G_i=p(X_i)` is at most `A/l`.

This is strictly smaller than the former raw-microstate claim: every
fiber-centered direction is now proved to have eigenvalue `1/l` and is
Gram-orthogonal to the displayed product-level problem.  The bounded-surplus
square compression (1.2) is one check on this proposition, but does not
control its mixed product-level directions.  Together with the accepted
fixed-length base cases, CGL recursion, and dense tail, the proposition
would give a polynomial complete-pair and aligned-bridge gap.

Inside the minimal long-cycle stratum, an even smaller remaining proposition
is:

> **PARKING-MULTISET PROJECTION.**  The stationary-flow projection of the
> half-lazy rank-two heat bath onto sorted parking multisets has gap at least
> `n^{-C}` for a universal `C`.

Equivalently, it suffices to route Pollak quotient-coordinate refreshes
through macro heat-bath flow with polynomial congestion.  Restrictions are
already closed by (1.3).  Equations (1.7)--(1.8) show why direct edge
domination fails and why that failure alone is not a bottleneck.

## 6. Strongest self-attack

The square-indicator span is generally not invariant: conditioning one
coordinate to be a square can change arbitrary conjugacy-class statistics
of another coordinate.  Therefore (1.2) is not a bound on a standalone
eigenblock, and positive-semidefinite cross-term estimates alone can lose a
square root.  The product-increment proposition remains substantial.

Likewise, polynomial fixed-multiset restrictions do not imply a polynomial
full minimal-sector gap without the projection theorem.  The binary bypass
handles one infinite family only.  The raw-tree positive correlation and
Stanley-tree nonlocality reject two direct comparisons but do not rule out
randomized polynomial-congestion flows.

An earlier version of `stanley_inverse_basis_falsifier.py` used the wrong
rank inequality in the recursive insertion and produced invalid chains.
Those outputs were discarded.  The repaired version keeps the new singleton
for `new_rank<=s`, merges it only for `new_rank>s`, checks every cover,
and verifies the exact counts `n^(n-2)` through `n=7`.  Its remaining
basis-exchange sequence is treated only as a finite falsifier; no asymptotic
claim relies on it.

## 7. Calibration

- Odd original raw length `m` is empty; the paired bridge endpoint is even.
  The long-cycle bridge application consequently uses odd `n` and
  `r=n-1=2l`.  Even `n` computations are only raw-factorization
  falsifiers.
- `m=0` and `N=2` singleton regimes are outside the M27 target and
  cause no division by a nontrivial variance.  The excluded `m=2` global
  chain is not used.
- At `m=4`, the aligned H4 update is whole-word heat bath; this inherited
  base case is retained, not dropped by (1.4).
- The `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` counts and their pure-Hurwitz
  component counts concern the global identity chain.  No scoped
  fixed-endpoint claim here identifies a Hurwitz orbit with that global law.
- The minimal long-cycle analysis is exactly a near-minimal tree sector.
  It tracks ordered factor words through parking labels; it never replaces
  them by an unweighted raw-tree law.
- Rare and repeated colors are covered in (1.3) by the multiset quotient.
- The known failure of isolated length-two local simulation is not
  contradicted: (1.4) embeds a particular adjacent-pair edge with two fixed
  padding factors inside an aligned H4 fiber.
- Direct-rate calibrations for `(a,b)=(2,2),(2,3),(3,2)` are
  `1/27,1/60,1/60`; bypass pairs are
  `(1/9,1/27),(1/10,1/36),(1/15,1/40)`.

## 8. Artifacts and reproduction commands

Owned directory:
`experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/`.
All scripts are deterministic with seed `None`, use Python 3.12.3, and
record the named universal claim they can falsify.

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/raw_tree_measure_falsifier.py --n 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/raw_tree_measure_n4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/raw_tree_measure_falsifier.py --n 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/raw_tree_measure_n5.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_tree_locality_falsifier.py --n 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_tree_locality_n4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_tree_locality_falsifier.py --n 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_tree_locality_n5.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/parking_projection_falsifier.py --n 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/parking_projection_n4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/parking_projection_falsifier.py --n 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/parking_projection_n5.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_inverse_basis_falsifier.py --n-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes/stanley_inverse_basis_n7.json
python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M27-base-exceptional-modes
```

The independent finite distance-two macro calibration is in
`experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M32-parking-projection/`;
it is cited only as a finite calibration.  The universal binary formulas are
proved symbolically in `binary_macro_formula.md`.

## 9. Verdict

OPEN AT A NAMED STEP: PRODUCT-INCREMENT BASE CORRELATION
