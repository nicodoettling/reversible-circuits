# M84 final report: an exact zero row for the canonical positive braid

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, and scoped outcome

Permutations compose as `(pq)(x)=p(q(x))`, tuple factors are evaluated
left-to-right, and the right Hurwitz generator is

```text
R(a,b)=(b,bab).
```

The project target remains uniform on `Omega(N,m)` for the literal lazy exact
same-product `{3,4,5}` heat-bath chain. This mission resolves only M78/M81's
safe-duplicate occupation problem for M75's canonical uniform positive-
permutation braid.

The main result is:

> **ZERO-ROW THEOREM.** For every `L>=11`, the accepted voltage word `W_L`
> has no safe duplicate at any reachable preliminary elimination state.
> Therefore its total safe-prefix probability is exactly `eta_L=0`.

Appending a disjoint doubled edge gives a source with two nontrivial support
components at

```text
N_L=8L^2+2,  m_L=16L^2+2=2N_L-2.
```

Its M75 simple-positive-braid marked row is zero. Thus the proposed universal
row lower bound `(Nm)^(-C)` is **REFUTED** on an explicit infinite sequence.

This is not Terminal B: it is an obstruction to one comparison law, not a
stationary bottleneck or a superpolynomial heat-bath gap upper bound. The
original polynomial-mixing decision remains unresolved.

The complete proof, with definitions, is in `zero_row_theorem.md`.

## 2. Full argument and the five proof-critical points

### 2.1 Exact subset-state reduction

For a selected original-label set `S`, stable increasing extraction emits the
original factors of `S`. For unselected `j`, the current residual is

```text
r_j(S)=H_j(S)^(-1)t_jH_j(S),
H_j(S)=product_(s in S,s>j) t_s
```

in chronological order. Swapping two adjacent selection requests applies one
Hurwitz move inside the emitted prefix and leaves the residual unchanged.
Hence the residual depends only on `S`, while every order reaching `S` gives
the original selected-edge support-component partition in its prefix.

For unselected `i<j`, put

```text
B=product_(s in S,i<s<j)t_s.
```

Then

```text
r_i(S)=r_j(S) iff t_i=B t_j B^(-1).                (2.1)
```

The killed elimination process is therefore a uniformly ordered subset chain,
not a history-dependent state tree.

Selections before `i` or after `j` do not affect deletion connectivity. The
literal null-pair identities

```text
(p,p,c) --R_2,R_1--> (c,cpc,cpc),
(c,p,p) --R_1,R_2--> (p,p,c)                      (2.2)
```

show that erasing an adjacent equal pair commutes with moving an outside
strand across both pair strands. After deleting the pair, the remaining
diagrams differ only by Hurwitz moves and therefore have the same support
components. Safety depends only on the selected between-set `B`.

### 2.2 Point 1: cellular genus-one factorization surfaces

For an ordered factorization, cyclically order the edge-occurrence darts at
each symbol vertex by chronological factor index. This oriented ribbon graph
has face permutation `sigma alpha`. Dart tracing is token tracing, so its
boundary components are the cycles of the word product. Capping them gives
the chronological factorization surface

```text
chi(Sigma(w))=v-k+c(eval(w)).                      (2.3)
```

For the base word, exact and symbolic counts are

```text
V=8, E=16, F=8, chi=0.
```

Thus its connected cellular surface is a torus. Every one of the eight facial
4-cycles has integer voltage `(0,0)`. The lifted rotations inherit the base
rotations, all faces lift, and

```text
V_L=8L^2, E_L=16L^2, F_L=8L^2.
```

Consequently `W_L` is the 1-skeleton of a connected unbranched `L^2`-sheeted
torus cover, not merely an abstract connected graph cover.

### 2.3 Points 2 and 3: embedded curve and deletion connectivity

A right Hurwitz move is a ribbon homeomorphism. Disjoint adjacent factors
only exchange timestamps. For `(xy),(yz)`, the move to `(yz),(xz)` is the
local ribbon edge slide of the first band endpoint along the second band.

At a collision endpoint, the two consecutive `p` occurrences have consecutive
darts at both endpoints. Their dual edges join the same two distinct token
faces and form an embedded two-edge simple closed curve `gamma`. Equivalently,
the pair bands and intervening vertex sectors form an annulus, and `gamma` is
its core. Pulling this annulus back through inverse Hurwitz edge slides keeps
the curve embedded. The graph walk below is only a skeleton representative
of that embedded regular-neighborhood core; no claim about a generic
self-intersecting null-homologous walk is used.

Cellular primal/dual duality gives the exact criterion

```text
deleting p,p leaves connected support
  iff gamma is nonseparating.                      (2.4)
```

Indeed, over `F_2`, a separating dual cycle is the boundary of a nonempty
proper union of dual 2-cells. Those cells correspond to primal vertices, and
their boundary is exactly the crossed primal edge pair, a cut. Conversely,
if deleting the parallel pair disconnects, that pair is `delta(U)` for a
primal component and its dual cycle is the displayed cellular boundary.

For the between-set `B`, if `t_j=(c d)`, a local band-slide induction retracts
the pulled-back annular core to

```text
c --B--> B(c) --t_i--> B(d) --B^(-1)--> d --t_j--> c.   (2.5)
```

To see the local induction without hiding selections outside `[i,j]`, first
extract `B`, then bubble the right `p` left across the unselected factors in
the interval until it meets the left `p`. In the inverse ribbon diagram, an
unselected factor is pushed to the exterior side of the annulus. An extracted
factor of `B` gives the complementary local rectangle: if its transposition
meets a tracked endpoint, the annular core slides once along that band and
moves that endpoint; if disjoint, it is an isotopy. Reversing the factors of
`B` gives the two token tracks in (2.5). Formula (2.1) closes the contour.
The outside strands are then erased by (2.2).

### 2.4 Point 4: integral voltage basis and the cover subgroup

The base voltage cochains vanish on every facial boundary. The two oriented
base cycles

```text
0-7-2-6-0 -> (-1,0),
0-7-1-6-0 -> ( 0,1)                               (2.6)
```

have determinant `-1`. Since the base is a torus, `(x,y)` is an integral
`H^1` basis, not only a pair of nonzero mod-`L` labels. The surface cover is
therefore the subgroup `L Z^2` of `pi_1(T^2)=Z^2`. Its map on integral first
homology is injective with image `L Z^2`.

Thus a closed curve upstairs projects to voltage `V in L Z^2`, and projected
voltage zero implies zero integral homology upstairs.

### 2.5 Point 5: the audited coordinate bound

Each of the sixteen base blocks in `W_L` is a perfect matching. Along either
token track in (2.5), a token traverses at most one selected factor from a
fixed block. After traversing that matching edge, no other factor in the same
block is incident to it. There are two tracks.

Exactly four blocks have nonzero `x` voltage and four have nonzero `y`
voltage; every nonzero coordinate is `+1` or `-1`. The closing factors
`t_i,t_j` contribute at most one each. Counting with multiplicity, including
the possibility that both tracks traverse the same factor and counting the
closing blocks again, gives

```text
|V_x|<=2*4+2=10,  |V_y|<=2*4+2=10.                (2.7)
```

There is no repeated pass through a matching block: every endpoint track sees
each chronological block once and its edges are disjoint.

### 2.6 Zero row

For `L>=11`, (2.7) and `V in L Z^2` force `V=(0,0)`. Injectivity of torus-cover
homology makes the embedded collision curve null-homologous. An embedded
circle on an oriented torus is null-homologous exactly when it separates, so
(2.4) says every collision is unsafe. Hence every reachable state has `a=0`
safe duplicate pairs, every next-pair hazard `2a/[s(s-1)]` is zero, and
`eta_L=0`.

Append a disjoint doubled edge on two new vertices. Cross-component Hurwitz
moves are only commutations, so the induced relative order/action on the
genus-one factors is unchanged. A globally marked square in that component
would in particular be a safe consecutive collision in the relative order;
none exists. This gives the advertised two-nontrivial-component zero row.

## 3. Probability, runtime, path, and congestion accounting

| item | exact value or bound | status |
|---|---:|---|
| voltage component vertices/factors | `d_L=8L^2`, `k_L=16L^2` | proved/accepted |
| nontrivial two-component ambient parameters | `N_L=8L^2+2`, `m_L=16L^2+2=2N_L-2` | proved |
| safe unordered pairs in every reachable `W_L` state, `L>=11` | `a=0` | proved |
| conditional next-two hazard | `2a/[s(s-1)]=0` | proved |
| total safe-prefix/marked-row probability | `eta_L=0` | proved |
| canonical braid sampling time | `O(m^2)` elementary operations | inherited; irrelevant to zero row |
| expected canonical braid length | `m(m-1)/4` | inherited M75/M77 |
| M75 coarea lower bound through this row | unavailable because `eta=0` | exact obstruction |
| heat-bath conductance or spectral-gap upper bound | none | unresolved |

The exact scripts use only the Python standard library. The longest owned
exact run reported here, all `635376` `W_2` four-label tail complements, took
about 58 seconds. No proof conclusion depends on Monte Carlo.

## 4. Dependencies and claim status

| input or claim | status | evidence/dependence |
|---|---|---|
| `W_L` identity, simple connected support, genus-one count | inherited accepted M78/M81; independently spot-checked here | exact construction |
| canonical braid = uniform elimination; safe prefix iff marked endpoint | inherited accepted M78/M81 | exact Hurwitz algebra |
| subset residual and duplicate formula | proved here | Section 2.1 |
| safety independent of outside selections | proved here | null-pair diagram (2.2) |
| factorization surfaces and Hurwitz edge slides | proved here | Sections 2.2--2.3 |
| safety iff embedded contour nonseparating | proved here | cellular cut/dual-cycle argument |
| integral voltage basis and torus cover | proved here | face sums and determinant-one cycles |
| coordinate bound `<=10` | proved here | perfect-matching block count |
| `eta_L=0` for every `L>=11` | proved here | Sections 2.1--2.6 |
| M75 simple-positive-braid row lower bound | refuted | explicit infinite zero-row sequence |
| another braid law has a row bound | unresolved | not tested by theorem |
| heat-bath Terminal B | unresolved | no stationary cut follows |

No literature theorem is invoked.

## 5. First unproved standalone step

The zero row removes the canonical uniform simple-positive-braid law from the
M75 coarea theorem. The first surviving alternative is:

> **NONCANONICAL BIJECTIVE MARKED-COVER LEMMA.** Construct a state-independent
> probability law on bijective Hurwitz words, with polynomial expected word
> length, whose worst-source probability of reaching the connected-deletable-
> square set is inverse-polynomial for every two-component minimal exterior
> macro; or prove that every such polynomial-length state-independent law has
> a zero/superpolynomially small row on an explicit family.

This is strictly different from tuning the now-refuted canonical elimination
law. A direct arbitrary-partial-macro flow theorem not mediated by a row cover
would also bypass the obstruction.

## 6. Strongest self-attack

1. The most delicate claim is the local identification of the pulled-back
   pair annulus with contour (2.5). The proof uses literal ribbon edge-slide
   rectangles and distinguishes selected from unselected between-factors; a
   fresh referee should redraw this local move rather than accept the voltage
   diagnostic alone.
2. A null-homologous self-intersecting graph walk need not separate. The proof
   avoids that false step: embeddedness belongs to the annular core preserved
   by homeomorphisms, and (2.5) only computes its homology.
3. Graph-cover connectedness alone would not identify the integral subgroup.
   The proof uses zero voltage on every face and the determinant-one integral
   basis (2.6), so it is a surface-cover statement.
4. The bound `10` deliberately overcounts shared traversals and closing
   blocks. If a path could revisit a block it would fail, but the consecutive
   perfect-matching structure rules this out separately for each endpoint.
5. The theorem starts at `L=11`; the absence of observed hits at `L=2,3` is
   not promoted to an all-state statement for those moduli.
6. Refuting one state-independent braid family does not refute the heat-bath
   chain, another randomized routing law, or polynomial mixing.

## 7. Boundary cases and falsification checks

- Odd `m`, `m=0`, `m=2`, and `N=2` are outside this minimal two-component
  construction.
- `L=1` is a positive calibration: exact full-order hit probability is
  `1280342186496/16!`, about `0.06119366458`.
- The proof asserts no exact total hit probability for `2<=L<=10`.
- Exhausting all `2^16` base subsets gives 23040 duplicate subset-pairs and
  14592 safe pairs. Safety agrees with nonzero contour homology in all 23040,
  and changing selections outside the pair interval changes safety in zero
  cases.
- Independently, all 240 connected genus-one `S_3` identity words, all
  selected subsets, and all 18720 duplicate subset-pairs give zero failures
  of `safe iff contour has nonzero mod-2 homology`; every contour is a cellular
  cycle. This is an exhaustive falsification check of the general local lemma.
- For `W_2`, exact tail enumeration at unselected counts `2,3,4` covers
  `2016`, `41664`, and `635376` subsets and finds zero safe pairs.
- Fixed-seed per-state probes at `L=1,2,3` find 508, 97, and 27 collisions,
  respectively, with zero homology/safety mismatches. Those sampled counts are
  empirical only.

## 8. Artifacts and reproduction

Owned artifacts are:

```text
plan.md
checkpoint.md
zero_row_theorem.md
subset_tail_audit.py
subset-tail-results.json
subset-tail-L2-c4.json
collision_contour_audit.py
collision-contour-results.json
homology_equivalence_probe.py
homology-equivalence-results.json
exact_subset_contour_audit.py
exact-subset-contour-results.json
generic_contour_falsification.py
generic-contour-results.json
topology_voltage_audit.py
topology-voltage-results.json
report.md
SHA256SUMS
```

Commands from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/topology_voltage_audit.py --L 1 2 3 11 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/topology-voltage-results.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/exact_subset_contour_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/exact-subset-contour-results.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/generic_contour_falsification.py --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/generic-contour-results.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/subset_tail_audit.py --case 1 2 3 4 --case 2 2 3 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/subset-tail-results.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/subset_tail_audit.py --case 2 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/subset-tail-L2-c4.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/collision_contour_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/collision-contour-results.json

PYTHONDONTWRITEBYTECODE=1 python3 experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/homology_equivalence_probe.py --case 1 5000 --case 2 3000 --case 3 1000 --output experiments/20260811-polynomial-mixing-resolution/cycle-17/mission-M84-safe-duplicate-occupation/homology-equivalence-results.json
```

Python `3.12.3`; exact seeds are `null`; the empirical probe seed is `840084`
with deterministic case offsets; nonstandard dependencies `{}`. Every JSON
records its arguments, commit, Python version, seed status, method, and scope
warning.

## 9. Verdict

```text
PROVED: eta_L=0 FOR EVERY L>=11.
REFUTED: M75 SIMPLE-POSITIVE-BRAID ROW LOWER BOUND.
NO TERMINAL HEAT-BATH CLAIM.
```

The assigned safe-duplicate reachability/occupation problem is closed for an
explicit infinite family by an exact zero probability, rather than merely a
superpolynomial upper bound. The project should not continue trying to prove a
worst-row cover for this canonical braid law.
