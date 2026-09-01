# Cycle 04 M14 report: fixed-endpoint base falsification and a complete l=3 theorem

## 1. Exact claim, quantifiers, and conventions

Permutations are maps on `[N]`, composition is `(pq)(x)=p(q(x))`, and a
word is evaluated from left to right as the displayed product.  Put

```text
M=binom(N,2),     P_N=uniform(T_N),     Q_N=P_N^2.
```

The support `Sigma_N=supp(Q_N)` consists of the identity, the 3-cycles, and the
products of two disjoint transpositions.  The numbers of ordered
transposition-pair microfactorizations are respectively

```text
a_N(e)=M,     a_N(q)=3 for a 3-cycle,
a_N(q)=2 for a double transposition.                    (1.1)
```

A pair-length-`l` microfactorized bridge from `u` to `v` is a length-`2l`
transposition word whose `l` ordered-pair products multiply to
`h=u^{-1}v`.  Thus it is enough to work from `e` to `h`.  On a nonempty
fiber define the nonlazy aligned chain

```text
B_l=(1/(l-1)) sum_{j=1}^{l-1} H_{2j-1,4},              (1.2)
```

where an update is exactly uniform over the four-transposition words with
the current block product.  If that product is `g` and

```text
F_{4,N}(g)=#{(s_1,...,s_4) in T_N^4:s_1...s_4=g},
```

a specified outcome of the specified window has probability
`1/[(l-1)F_{4,N}(g)]`.  In particular it is at least
`1/[(l-1)M^4]`.  The bridge law on microfactor words is uniform.

The assigned universal statement under falsification was:

> For every `N>=3`, `l>=2`, and `h in A_N` with `Q_N^l(e,h)>0`, the
> microfactorized fixed-endpoint fiber is irreducible under `B_l`.

No counterexample was found, and that all-`l` statement remains open.  This
mission proves the following strict subtheorem, including a quantitative
bound.

> **Theorem M14.1 (universal pair length three).**  For every `N>=3` and
> every `u,v in A_N` with `Q_N^3(u,v)>0`, the pair-length-three
> microfactorized bridge is irreducible.  If `M=binom(N,2)`, then
>
> ```text
> gap(B_3;u,v) >= M^{-16},
> Lambda_N(3;u,v)=2 gap(B_3;u,v) >= 2M^{-16}.           (1.3)
> ```
>
> Here `Lambda` is the Poincare constant of
> `(I-H_1)+(I-H_2)=2(I-B_3)`.  A singleton fiber has gap one by convention.

The proof is computer-assisted only in a finite, explicitly complete
`3<=N<=12` incidence check.  The reduction from that finite check to all
`N`, and the Poincare bound, are mathematical arguments below.

## 2. Full argument and bounded construction

### 2.1 Microfactor labels can be quotiented exactly

Write a state as ordered transposition pairs `A_1,...,A_l` and let
`q_i=prod(A_i) in Sigma_N`.  Projection to `(q_1,...,q_l)` preserves connected
components:

1. Every aligned `H_4` move replaces two adjacent increments by two elements
   of `Sigma_N` with the same ordered product, so every microfactor edge projects
   to an adjacent product-path edge.
2. Conversely, every such product-path edge lifts: choose any ordered
   two-transposition realization of each new increment and concatenate them
   as the requested four-factor heat-bath outcome.
3. All microfactor states above one product path communicate.  To change the
   ordered realization of one increment, update either adjacent four-factor
   window, retain both increment products and the neighboring realization,
   and select the desired realization.  Every site lies in such a window
   when `l>=2`.

Thus no invariant is lost by the product-path quotient.  The scripts retain
the multiplicity (1.1) when counting stationary mass.

### 2.2 Exact incidence graph at l=3

For `l=3`, write the pair products as `(a,b,c)` with `abc=h`.  Form a
bipartite graph with a left and right copy of `Sigma_N`, deleting isolated
vertices, and put

```text
a -- c    iff    b=a^{-1}hc^{-1} belongs to Sigma_N.    (2.1)
```

This is exact, not only a necessary condition.  With `c` fixed, the left
`H_4` heat bath makes all admissible `(a,b)` one clique; with `a` fixed, the
right heat bath makes all admissible `(b,c)` one clique.  Multiple ordered
middle-pair realizations on one incidence lie in those same cliques.
Consequently the components of the six-factor state graph are exactly the
components of (2.1).

The deterministic harness constructs `Sigma_N` from all ordered transposition
pairs, tests (2.1), and uses union-find.  Through `N=6` it independently
constructs the larger graph whose vertices are ordered first/last
microfactor pairs and asserts equal component counts and incidence counts.
For each endpoint type it also:

- sums component sizes using `a_N(a)a_N(b)a_N(c)`;
- emits an exact representative six-transposition word per component and
  asserts that its product is the requested endpoint;
- multiplies each fiber size by its exact symmetric-group conjugacy-class
  size and asserts that the sum over endpoint types is exactly `M^6`.

An endpoint is feasible at six transpositions exactly when its transposition
defect `N-#cycles` is even and at most six: take a minimal factorization and
pad with adjacent squares.  Hence the endpoint list is complete.  Simultaneous
conjugation by every element of `S_N` intertwines the chain, so one ordinary
`S_N` cycle-type representative suffices even when its `A_N` class splits.

The exact results are:

```text
N                         3  4  5  6  7   8   9  10  11  12
feasible endpoint types   2  3  4  6  8  12  15  17  18  19
components for every type 1  1  1  1  1   1   1   1   1   1
```

Every `N` passes the exact class-mass identity `sum_h |[h]| |fiber(h)|=M^6`.
At the priority case `N=6,l=3`, the six endpoint fiber sizes in JSON order
are

```text
31,250; 24,640; 24,300; 46,413; 39,382; 72,315,
```

and their class-weighted sum is `15^6=11,390,625`.  The product quotient and
the explicit ordered-micro graph both give one component for all six types.
At `N=12` the calculation includes the first defect-six endpoints moving
twelve labels and accounts for `66^6=82,653,950,016` words without listing
those words.

### 2.3 Why N<=12 is a complete universal certificate for l=3

Here is the support reduction, which is stronger than the valid but weaker
union-of-two-states bound of 24 labels.

Take any ambient-`N` six-transposition state `w` with endpoint `h`, and let
`U` be the union of labels occurring in `w`.  Then `|U|<=12`, and every label
moved by `h` belongs to `U`.  Regard `w` and `h` as a bridge in `S_U`.

If `h!=e`, its defect is `d in {2,4,6}`.  Fix a minimal length-`d`
transposition factorization of `h` using only `supp(h)`, and pad it to length
six by `(6-d)/2` adjacent squares using a transposition in `supp(h)`.  This
gives one canonical word `c_h` depending only on `h`, not on `w` or `U`.
The exact connectedness result for `|U|<=12` connects `w` to `c_h` using
only labels in `U`.  The case `|U|=2` cannot occur for nonidentity even `h`.
Therefore every ambient state reaches the same `c_h`.

If `h=e`, the same certificate connects `w` inside `U` to `(s,s)^3` for any
chosen transposition `s` of `U`; `|U|=2` is a direct singleton check.  For
arbitrary transpositions `s,r` in the ambient group, two allowed moves give

```text
(s,s,s,s,s,s) -> (r,r,r,r,s,s) -> (r,r,r,r,r,r).      (2.2)
```

Both refreshed four-factor products are the identity.  Thus all square
canonicals communicate.  This proves universal irreducibility at `l=3`,
including the identity endpoint, without assuming a large-`N` stabilization
heuristic.

More generally, the same argument gives a useful exact finite-basis lemma:
for a fixed pair length `l`, verifying every feasible endpoint through
`N=4l` proves qualitative irreducibility for all `N`.  One state has `2l`
transpositions and hence uses at most `4l` labels; the same endpoint-canonical
argument applies.

### 2.4 Uniform polynomial l=3 Poincare bound

Let `V` be the number of microfactor states in a nonempty `l=3` endpoint
fiber.  Then `V<=M^6`.  Every positive off-diagonal transition used by a
spanning tree has probability at least

```text
p_* = 1/(2M^4),                                        (2.3)
```

because the scan chooses one of two windows and any four-factor conditional
fiber has size at most `M^4`.

Choose a spanning tree of the now-proved connected transition graph and the
unique tree path for every ordered pair `x,y`.  Each path has length at most
`V-1`, and any tree edge is used by at most `V^2` ordered pairs.  For the
uniform bridge law,

```text
Var(f)
 = (1/(2V^2)) sum_{x,y}(f(x)-f(y))^2
 <= ((V-1)/2) sum_{e in tree} (nabla_e f)^2.            (2.4)
```

Uniform reversibility and (2.3) give

```text
E_{B_3}(f,f) >= (p_*/V) sum_{e in tree}(nabla_e f)^2.  (2.5)
```

Combining (2.4)--(2.5),

```text
gap(B_3) >= 2p_*/[V(V-1)]
          >= 1/(M^4 V^2)
          >= M^{-16}.                                  (2.6)
```

This is deliberately crude but universal.  It uses no fixed-hub load:
the canonical words establish connectivity, while the quantitative argument
may use any spanning tree.  Even the worst possible tree has only polynomial
load because a length-six fiber itself has at most `M^6` states.

### 2.5 The next exact case l=4

At `l=4`, the product quotient consists of paths `(a,b,c,d) in Sigma_N^4` with
`abcd=h`.  The three heat-bath clique keys are respectively `(c,d)`, `(a,d)`,
and `(a,b)`.  Enumerating `a,b,c` determines

```text
d=c^{-1}b^{-1}a^{-1}h,
```

so the harness costs a `|Sigma_N|^3` scan rather than `M^8` microfactor words.
It retains the exact microfactor weight `a_N(a)a_N(b)a_N(c)a_N(d)`.

Every feasible endpoint cycle type is connected for every `3<=N<=7`:

```text
N                         3  4  5  6  7
feasible endpoint types   2  3  4  6  8
components for every type 1  1  1  1  1
```

The exact class-mass checks are `M^8`; at `N=7` this accounts for
`21^8=37,822,859,361` microfactor words using at most 783,266 product paths
in one endpoint fiber.  This finite survival does not prove the `l=4`
statement.  The finite-basis lemma shows that an exact all-endpoint check
through `N=16` would be complete, but this mission did not perform or replace
those remaining checks by a structural proof.

## 3. Probability, runtime, path length, and congestion accounting

- The exact nonlazy scan probabilities are `1/2` at `l=3` and `1/3` at
  `l=4`; a selected outcome has the additional factor `1/F_{4,N}(g)`.
  At `N=6`, all occurring four-factor fiber sizes lie between 54 and 765;
  at `N=7` they lie between 36 and 1491.  These finite ranges are diagnostics;
  the proof uses only `F_{4,N}(g)<=M^4`.
- `|Sigma_N|=1+2 binom(N,3)+3 binom(N,4)=O(N^4)`.  The `l=3` product test costs
  `O(c_6(N)|Sigma_N|^2 N)` elementary permutation work, where `c_6(N)` is the
  number of feasible endpoint cycle types (at most 19 once all patterns are
  present).  The explicit micrograph cross-check through `N=6` has
  `M^2` possible vertices per side.
- The `l=4` test costs `O(c_8(N)|Sigma_N|^3N)` plus union-find storage linear in
  the number of feasible product paths.  It avoids enumerating `M^8` words.
- Recorded internal runtimes on this machine were 0.298 seconds for the
  combined `N=6,l=3` case, 50.416 seconds for `N=12,l=3`, 3.085 seconds for
  `N=6,l=4`, and 27.616 seconds for `N=7,l=4`.
- The proof paths in (2.4) have worst length `V-1<=M^6-1`; the deliberately
  coarse ordered-pair load on any tree edge is at most `V^2<=M^12`.
  Equations (2.3)--(2.6) include all scan, fiber-size, stationary-mass, path,
  and load factors.  No claim about the diameter or congestion at growing
  `l` is made.
- An exact `H_4` step can be sampled by enumerating at most `M^4` candidates,
  polynomial in `N`.  The harness is deterministic and uses no random seed.

## 4. Dependencies with status

- **PROVED HERE:** the microfactor-to-product-path component equivalence;
  the exact `l=3` incidence characterization; endpoint feasibility and
  conjugacy reduction; the supportwise finite-basis lemma; the universal
  completion from `N<=12`; and the spanning-tree Poincare estimate.
- **EXACT FINITE / COMPUTER-VERIFIED:** every incidence graph for every
  feasible endpoint cycle type at `3<=N<=12`; ordered-micro versus product
  quotient equality through `N=6`; every `l=4` product graph at `3<=N<=7`;
  representative-product assertions and exact `M^6`/`M^8` class-mass
  identities.  These use integer tuple arithmetic and no floating point.
- **INHERITED, NOT NEEDED FOR THEOREM M14.1:** L-0032's universal identity
  aligned-chain irreducibility and L-0054's constant-loss large-scale bridge
  recursion.  M14.1 independently handles the identity endpoint at `l=3`.
- **CONDITIONAL / OPEN:** a uniform base-scale gap for every
  `2<=l<=O(N log N)`; M10's Terminal-A consequence still depends on it.
- **CITED LITERATURE:** none.  No asymptotic conclusion is imported from a
  finite spectrum or simulation.

## 5. First unproved step

> **UNIVERSAL l=4 PRODUCT-PATH CONNECTIVITY.**  For every `N>=3` and every
> `h in A_N` of even transposition defect at most eight, the graph on
> `(q_1,q_2,q_3,q_4) in Sigma_N^4` satisfying `q_1q_2q_3q_4=h`, with an edge
> whenever one adjacent pair is replaced by another pair in `Sigma_N^2` with
> the same ordered product, is connected.

By Section 2.1 this is equivalent to microfactorized `l=4` irreducibility.
By the finite-basis lemma, it is enough to prove every endpoint case through
`N=16`.  Even its resolution would be only another fixed-length theorem;
the first quantitative implication needed by M10 remains a gap exponent
uniform in `l<=O(N log N)`.

## 6. Strongest self-attack and failure mode

The universal `l=3` conclusion is a computer-assisted theorem and therefore
inherits the risk of a coding or quotient mistake.  The strongest checks are
the independently constructed ordered-micro graph through `N=6`, exact word
witness evaluation, complete cycle-type enumeration including split
`A_N` classes via `S_N` conjugation, and the global class-mass identities.
The quotient proof is also explicit and independent of those assertions.

The `M^{-16}` exponent is intentionally poor.  More importantly, the same
state-count argument at growing `l` gives an exponent proportional to `l`
and is superpolynomial in the M10 base regime.  It does not advance the
uniform-in-`l` quantitative step by itself.  The common canonical state is
safe here only because fixed `l=3` has polynomial total mass; routing long
bridges through one canonical hub would revive the known exponential-load
failure.

The `l=4` runs stop at `N=7`, well short of the complete finite basis
`N<=16`; a disconnect may first occur later or at larger `l`.  Finally, even
a disconnected or slow auxiliary `B_l` fiber would not refute `K`, because
the known comparison `K>=B/12` transfers lower bounds only.  This mission
therefore establishes neither Terminal A nor Terminal B.

## 7. Calibration results

- Odd identity-word length is empty; this paired bridge always has even
  microfactor length.  The `m=0` identity fiber is a singleton.
- For `N=2`, `Q` is supported only at the identity and every paired bridge is
  a singleton.  The support-reduction proof handles the only `|U|=2` case
  directly.
- Original `m=2,N>=3` is excluded.  It corresponds to pair length one, with
  no aligned `H_4`; it must not be inferred from this `l>=2` result.
- At `l=2`, the sole aligned `H_4` is the whole-word heat bath, so every
  nonempty fixed-endpoint fiber is connected with nonlazy gap one.  Likewise,
  the whole-word `r=4` move in the original `m=4` kernel is not discarded.
- The harness reproduces `|Omega(3,4)|=27`,
  `|Omega(4,4)|=120`, and `|Omega(4,6)|=3936` exactly.
- Every feasible endpoint is tested, not only identity.  Minimal-defect
  endpoint factorizations and padded/square examples are included.  Ordered
  increment positions and microfactor multiplicities are retained, so
  disjoint-support color interleavings are not collapsed.
- No edge-multiplicity parity or vertex-degree parity criterion is used.
  The known failure of length-two local simulation is distinct from the
  pair-length-two whole `H_4` heat bath here.
- Finite connectivity and the `l=3` fixed-length gap do not imply a growing-
  length result; no finite spectral grid or slow trace is presented.

## 8. Artifacts and reproduction commands

All artifacts are under
`experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/`:

- `plan.md`, `checkpoint.md`, and this `report.md`;
- `l3_endpoint_quotient.py` and `l4_product_path.py`;
- `results_N3_to_N6_l3.json`, `results_N7_to_N10_l3.json`,
  `results_N11_l3.json`, and `results_N12_l3.json`;
- `results_N3_N4_l4.json`, `results_N5_l4.json`, `results_N6_l4.json`, and
  `results_N7_l4.json`.

Run from the repository root:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 3 --N 4 --N 5 --N 6 --verify-micro-through 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N3_to_N6_l3.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 7 --N 8 --N 9 --N 10 --verify-micro-through 0 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N7_to_N10_l3.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 11 --verify-micro-through 0 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N11_l3.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l3_endpoint_quotient.py --N 12 --verify-micro-through 0 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N12_l3.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l4_product_path.py --N 3 --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N3_N4_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l4_product_path.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N5_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l4_product_path.py --N 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N6_l4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/l4_product_path.py --N 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-04/mission-M14-base-falsification/results_N7_l4.json
```

The JSON records each exact command, the tested universal claim, kernel
normalization, Python `3.12.3`, seed `null`, and repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

OPEN AT A NAMED STEP: UNIVERSAL l=4 PRODUCT-PATH CONNECTIVITY
