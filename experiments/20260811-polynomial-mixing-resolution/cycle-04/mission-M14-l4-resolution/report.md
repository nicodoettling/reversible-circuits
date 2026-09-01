# Cycle 04 M14 report: universal l=4 product-path connectivity and gap

## 1. Exact claim, quantifiers, and conventions

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and displayed words
evaluate as `t_1...t_m`.  Let

```text
M=binom(N,2),     P_N=uniform(T_N),     Q_N=P_N^2.
```

Fix `N>=3` and endpoints `u,v in A_N` for which the pair-length-four
`Q_N` bridge is nonempty.  Equivalently, with `h=u^{-1}v`, let

```text
Omega_h^(8)={(t_1,...,t_8) in T_N^8:t_1...t_8=h}.
```

This fiber has the uniform microfactor law.  Define the nonlazy aligned
heat-bath chain

```text
B_4=(1/3)(H_{1,4}+H_{3,4}+H_{5,4}),                   (1.1)
```

where `H_{j,4}` is uniform on all four-transposition blocks with the current
ordered block product.  The exact theorem proved here is:

> **Theorem M14.2.**  For every `N>=3` and every feasible `u,v in A_N`,
> `B_4` is irreducible on `Omega_{u^{-1}v}^(8)`.  Its product-path projection
> onto four increments in `supp(Q_N)` is also irreducible.  Moreover,
>
> ```text
> gap(B_4;u,v) >= 2/[3 M^20] >= (2/3)N^{-40}.          (1.2)
> ```
>
> For the continuous-time local Hamiltonian
> `mathcal H_4=sum_{j=1}^3(I-H_{2j-1,4})`,
>
> ```text
> Lambda_N(4;u,v)=3 gap(B_4;u,v) >= 2M^{-20}.          (1.3)
> ```

A singleton fiber has gap one by convention.  This proves the assigned
fixed-length claim, not the growing-base theorem required by M10 and not a
terminal result for the global goal.

## 2. Full proof

### 2.1 Checked arbitrary-product Hurwitz classification

The cited input is Douvropoulos--Lewis, published Theorem 18 (numbered
Theorem 4.2 in the section-numbered preprint):

> Theo Douvropoulos and Joel Brewster Lewis, “Hurwitz Orbits on Reflection
> Factorizations of Parabolic Quasi-Coxeter Elements,” *Electronic Journal
> of Combinatorics* **31**(1) (2024), #P1.27,
> [doi:10.37236/11787](https://doi.org/10.37236/11787).

The project audit verifies that every permutation in `S_N` is a parabolic
quasi-Coxeter element: factor each disjoint cycle minimally, obtaining a
reduced transposition factorization that generates the corresponding Young
parabolic subgroup.  The theorem therefore implies the following graph form.

For a transposition factorization `w`, make the labeled factorization graph
whose factors are edges.  Two same-length factorizations of the same arbitrary
`h in S_N` are Hurwitz-equivalent exactly when their graphs have the same
labeled connected components and the same number of factors on every
component.  Indeed, the factors generate the product of the full symmetric
groups on the graph components, and all transpositions within one component
form one conjugacy class in that generated subgroup.

Douvropoulos--Lewis use

```text
(a,b) -> (b,b^{-1}ab)=(b,bab)                         (2.1)
```

for transpositions.  Its inverse is the other common project convention;
inverting every braid generator leaves the orbit relation unchanged.

### 2.2 Every Hurwitz generator is an actual aligned-H4 outcome

Every adjacent position pair in a length-eight word lies in an aligned
window:

```text
(1,2),(2,3),(3,4) in [1,4];
(4,5),(5,6)       in [3,6];
(6,7),(7,8)       in [5,8].                           (2.2)
```

The overlap pairs may be put in either containing window.  Since

```text
b(bab)=ab,
```

performing (2.1) on the selected adjacent pair and retaining the other two
window factors preserves the exact ordered four-factor product.  It is
therefore one positive-probability heat-bath outcome.  Thus every fixed
labeled-component/weight macro-fiber is connected by moves of `B_4`.

### 2.3 Square normal form for one macro-fiber

Every component `C` of a factorization graph is a union of cycles of `h`.
Let `v_C` be its number of vertices, `q_C` the number of cycles of `h|_C`
including fixed points, and `k_C` its number of factors.  For a nonsingleton
connected component, Douvropoulos--Lewis published Proposition 8(4)
(Proposition 2.7(4) in the section-numbered preprint), specialized to type A,
gives

```text
k_C=v_C+q_C-2+2g_C,       g_C>=0.                      (2.3)
```

To see both the lower bound and the required target factorization, factor
each endpoint cycle minimally.  Those blocks use `v_C-q_C` transpositions.
Choose a tree on the `q_C` endpoint cycles and, for each tree edge, append an
adjacent square `(f,f)` crossing the two cycle supports.  The `q_C-1` bridge
squares make the factor graph connected and bring the length to
`v_C+q_C-2`.  Append `g_C` further adjacent squares.  This also directly
realizes every value allowed by (2.3).  An isolated fixed point has weight
zero.

This constructed word has the original restricted product `h|_C`, connected
support `C`, and weight `k_C`.  The graph-form Hurwitz theorem therefore
connects any factorization with that macro to a word in which all bridge and
surplus pairs are exposed as adjacent squares.

### 2.4 Square replacement is an actual aligned-H4 outcome

Every adjacent square position `p,p+1`, `1<=p<=7`, is contained in one of
the windows in (2.2).  Retain the other two factors in that window and replace

```text
(f,f) -> (s,s).                                        (2.4)
```

Both pairs have product the identity, so the full ordered four-factor block
product is unchanged even when the square occupies the middle two positions.
Hence (2.4) is an actual positive-probability outcome of the exact heat bath,
including at both word boundaries.

### 2.5 All macros reach one common macro

First suppose `h!=id`.  Fix one nontrivial cycle `D` of `h` and a
transposition `s` inside `D`.  In every current graph component, use Section
2.3 and the Hurwitz moves of Section 2.2 to expose:

- a minimal factorization of each endpoint cycle;
- all tree-bridge squares joining distinct endpoint cycles; and
- all surplus squares.

Replace every exposed bridge or surplus square by `(s,s)`.  Removing all
tree bridges separates every endpoint cycle into its own graph component;
fixed points become isolated.  Minimal factorizations keep each nontrivial
cycle connected.  Every excess factor pair is now stored as a square on `D`.
The resulting labeled-component/weight macro depends only on `h` and total
length eight, not on the starting word.  Within that common macro the
Hurwitz theorem supplies connectivity.

If `h=id`, every component target from Section 2.3 consists entirely of
adjacent bridge and surplus squares.  Fix a designated transposition `s` and
replace every one of the four square pairs by `(s,s)`.  This reaches `s^8`
from every starting word.  Equivalently, square canonicals on two edges are
connected directly by

```text
r^8 -> s^4 r^4 -> s^8.                                 (2.5)
```

At absolute minimum endpoint length eight there is no square surplus: every
endpoint cycle is already its own component, so the macro is unique and the
Hurwitz theorem alone applies.  These cases prove irreducibility for every
feasible endpoint.

### 2.6 Exact translation to product paths

Group the factors as ordered pairs

```text
A_i=(t_{2i-1},t_{2i}),     q_i=prod(A_i) in supp(Q_N).
```

Projection sends each aligned `H_4` move to replacement of two adjacent
increments by another pair with the same ordered product.  Conversely, every
such product-path replacement lifts by choosing ordered transposition-pair
microfactorizations of the two new increments.

Microfactor labels above a fixed product path also communicate: update a
window containing a chosen increment, retain both increment products and the
neighboring ordered realization, and select the desired ordered realization
of that increment.  Every increment lies in an aligned window.  Thus the
microfactor and product-path graphs have exactly the same component count,
and the named universal product-path proposition follows from Section 2.5.

### 2.7 Quantitative gap without a Hurwitz diameter bound

Let `V=|Omega_h^(8)|`.  Since there are `M` choices for each transposition,

```text
V<=M^8.                                                 (2.6)
```

For a block product `g`, put

```text
F_{4,N}(g)=#{(r_1,...,r_4) in T_N^4:r_1...r_4=g}.
```

The window scan has probability `1/3`, its heat bath is exactly uniform, and
`F_{4,N}(g)<=M^4`.  Therefore every positive off-diagonal transition chosen
for a spanning tree has

```text
B_4(x,y)>=p_*:=1/(3M^4).                               (2.7)
```

Choose any spanning tree of the connected transition graph and the unique
tree path for every ordered pair `x,y`.  Each path has length at most `V-1`,
and a tree edge is used by at most `V^2` ordered pairs.  With the uniform
stationary law,

```text
Var(f)
 = (1/(2V^2)) sum_{x,y}(f(x)-f(y))^2
 <= ((V-1)/2) sum_{e in tree}(nabla_e f)^2.             (2.8)
```

Uniform reversibility and (2.7) give

```text
E_{B_4}(f,f) >= (p_*/V) sum_{e in tree}(nabla_e f)^2.  (2.9)
```

Consequently

```text
gap(B_4)
 >= 2p_*/[V(V-1)]
 >= 2/[3M^4(M^8)^2]
 = 2/(3M^20)
 >= (2/3)N^{-40}.                                      (2.10)
```

Since `mathcal H_4=3(I-B_4)`, equation (1.3) follows.  Each heat bath is an
orthogonal conditional-expectation projection, so `B_4` is positive
semidefinite.  The standard worst-case fixed-fiber total-variation estimate
therefore also gives

```text
tau_{B_4}(epsilon)
 <= (3/2)M^20 (8 log M + log(1/epsilon)).              (2.11)
```

## 3. Probability, runtime, path length, and congestion accounting

- The block scan contributes exactly `1/3`; the selected outcome contributes
  exactly `1/F_{4,N}(g)`.  The proof uses the uniform lower bound
  `1/(3M^4)` and no hidden laziness.
- The comparison paths have length at most `V-1<=M^8-1`.  The coarse ordered
  pair load per tree edge is at most `V^2<=M^16`.  Stationary edge conductance
  is at least `p_*/V`; equations (2.8)--(2.10) retain every factor.
- No quantitative diameter from the cited Hurwitz theorem is assumed.  A
  spanning tree can, if desired, be constructed by enumerating at most `M^8`
  states and at most three exact four-factor fibers per state.  This is
  polynomial in `N` because `l=4` is fixed.
- One real `B_4` step can enumerate at most `M^4` candidate blocks, again
  polynomial in `N`.  Existing direct exact block samplers may be used but
  are not needed for the bound.
- No computation or random seed is used in the proof.  The prior exact
  `3<=N<=7` all-endpoint calculations are calibration only.

## 4. Dependencies with status

- **CITED AND CHECKED:** Douvropoulos--Lewis, published Theorem 18 and
  Proposition 8(4), respectively numbered Theorem 4.2 and Proposition
  2.7(4) in the section-numbered preprint, including the theorem's
  parabolic quasi-Coxeter hypothesis, arbitrary factor length, generated-
  subgroup/conjugacy-class conclusion, and Hurwitz convention.  The complete
  project audit is
  `cycle-03/mission-M05-referee/post_referee_resource_note.md`.
- **PROVED HERE:** containment of every Hurwitz and square move in the exact
  aligned windows; the square-tree macro canonicalization; exact
  microfactor/product-path component equivalence; and the full quantitative
  spanning-tree comparison.
- **EXACT FINITE, NOT A PROOF DEPENDENCY:** the frozen M14 product-path
  quotient finds every endpoint connected for `3<=N<=7`, with exact
  conjugacy-class mass checks.
- **INHERITED, CONDITIONAL USE ONLY:** M10's large-scale recursion and
  `K>=B/12`.  Combining the latter with (1.2) gives a fixed-`m=8` lower bound
  for the identity chain, but this is not the universal theorem.

## 5. First unproved proposition

> **UNIFORM BASE-SCALE FIXED-ENDPOINT GAP.**  There exist universal
> `c>0`, `C<infinity`, and `C_0<infinity` such that for every `N>=3`, every
> integer `2<=l<=C_0N log(N+1)`, and every feasible fixed endpoint pair
> `u,v in A_N`,
>
> ```text
> Lambda_N(l;u,v) >= c(Nl)^{-C}.
> ```

The checked classification gives qualitative connectivity for all these
lengths, but the state-count/spanning-tree exponent above grows linearly with
`l` and does not prove this proposition.

## 6. Strongest self-attack and failure mode

The qualitative theorem depends materially on the cited arbitrary-product
Hurwitz classification.  If its generated-subgroup or parabolic hypothesis
were mistranslated, Section 2.3 would fail; the frozen primary-source audit
checks exactly those points.  The square-tree targets independently exhibit
the required subgroup, product, component labels, and weights.

The polynomial bound is intentionally extremely weak and works only because
length eight gives at most `M^8` states.  Repeating it at pair length `l`
would use `M^{2l}` states and produce an exponent depending on `l`, which is
superpolynomial in the M10 base regime.  The canonical macro is used only for
connectivity; routing all growing-length comparison paths through it would
repeat the known exponentially loaded hub failure.

Finally, this proof rules out an `l=4` disconnected auxiliary bridge but does
not refute or prove rapid mixing of the full chain `K`.  One-way comparison
means a slow `B` mode would not automatically imply a slow `K` mode.

## 7. Calibration results

- Pair length `l=2` has one aligned window and is a whole-word exact heat
  bath, hence gap one on every nonempty endpoint fiber.
- `N=2` is elementary: there is one transposition and every feasible paired
  bridge is a singleton.  The theorem is stated for `N>=3`.
- Odd identity-word length is empty; `m=0` is singleton; original `m=2` has
  no aligned `H_4` and is excluded.  These are not inferred from `l=4`.
- The original `m=4` chain's whole-word `r=4` update is retained; it is
  distinct from the current length-eight auxiliary chain.
- The frozen exact harness reproduces `|Omega(3,4)|=27`,
  `|Omega(4,4)|=120`, and `|Omega(4,6)|=3936`, and tests every feasible
  endpoint cycle type through `N=7` for `l=4`.
- Minimum-length endpoint factorizations are handled explicitly: no square
  exists or is needed, and the endpoint-cycle macro is unique.
- Component labels, weights, ordered factor positions, and microfactor
  multiplicities are retained.  Disjoint supports still have ordered
  interleavings; no degree-parity or edge-multiplicity characterization is
  assumed.
- The failed generic surjective-support zipper for `N>=5` is not used.
  `supp(Q_N)` need not equal `A_N`.

## 8. Artifacts and reproduction commands

Owned artifacts:

- `experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-l4-resolution/plan.md`;
- `experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-l4-resolution/checkpoint.md`;
- this `report.md`.

Checked dependencies:

- `experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M05-referee/post_referee_resource_note.md`;
- `experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/report.md` and its exact JSON artifacts.

No new computation was required.  The exact finite calibration commands,
Python `3.12.3`, null seeds, and commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993` are recorded in the frozen M14
report and JSON.  This proof is reproducible by auditing the displayed
algebra and the cited theorem chain; no disposable `/tmp` artifact is used.

## 9. Verdict

PROVED
