# M15 final report: resource and paradigm audit

Date: 2026-08-11  
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Executive result

The literature audit did not locate a quantitative Hurwitz-action or
fixed-endpoint bridge theorem that proves the requested universal gap.  It did
locate one theorem that materially simplifies the dominant decomposition
route: JSTV Theorem 1 already combines a stationary-flow projection and
rejected-exit restrictions, with no separate mean-lift hypothesis.  For the
exact half-lazy kernel it gives

```
gap(K) >= gap(projection) * min_fiber gap(restriction) / 3.
```

I also give a different, exact random-walk-bridge reduction.  Pairing
transpositions turns the target into a bridge of the two-step random
transposition law `Q=P*P` on `A_N`.  The aligned length-four heat baths form a
two-increment bridge Gibbs sampler `B`, and

```
gap(K_{N,2n}) >= gap(B_{N,n})/12.
```

The remaining bridge gap proposition is precise but unproved.  Thus this
mission produces nonterminal reductions, not TERMINAL A or B.

## 1. Exact claims, quantifiers, and conventions

Throughout, `(pq)(x)=p(q(x))`; products are the displayed products
`t_1...t_m`.  For `N>=3` and even `m>=4`, `pi` is uniform on
`Omega(N,m)`, and

```
K = (1/2)I
    + (1/(2|R_m|)) sum_{r in R_m} (1/(m-r+1)) sum_i H_{i,r},
R_m = {r in {3,4,5}: r<=m}.
```

The gap is the Poincare constant.  The following claims are established.

**M15.1 (two-factor decomposition, proved/cited).**  Partition any finite
irreducible instance of `K` into nonempty fibers.  If `bar_K` is the exact
stationary-flow projection and `K_a` is the exact restriction obtained by
rejecting every exit from fiber `a`, then

```
gap(K) >= gap(bar_K) * min_a gap(K_a) / 3.                     (1)
```

In particular, the weighted-component decomposition requires projection and
restriction gap bounds, but no additional mean-lift bound.

**M15.2 (whole-word small case, proved).**  For every `N>=3`,

```
gap(K_{N,4}) >= 1/4.                                          (2)
```

**M15.3 (parity-block bridge comparison, proved).**  For `m=2n>=6`, define

```
B_{N,n} = (1/(n-1)) sum_{j=1}^{n-1} H_{2j-1,4}.
```

Then `B` is exactly the adjacent two-increment heat bath for the `Q=P*P`
return bridge, including its transposition-pair refinements, and

```
gap(K_{N,2n}) >= gap(B_{N,n})/12.                              (3)
```

Claims (1)--(3) are not a universal gap proof because no bound for the right
side of (3), nor the two gaps on the right side of (1), has been proved.

## 2. Full argument and construction

### 2.1 Exact JSTV application

For fibers `Omega_a`, set

```
bar_pi(a) = sum_{x in Omega_a} pi(x),
bar_K(a,b) = bar_pi(a)^(-1)
             sum_{x in Omega_a,y in Omega_b} pi(x) K(x,y).
```

For `x,y in Omega_a`, the restriction is

```
K_a(x,y) = K(x,y)                                     if x!=y,
K_a(x,x) = 1-sum_{y in Omega_a,y!=x}K(x,y)
         = K(x,x)+K(x,Omega\Omega_a).
```

Thus exits are holding probability; they are not removed and the remaining
moves are not normalized upward.  Put

```
bar_lambda = gap(bar_K),
lambda_min = min_a gap(K_a),
gamma = max_a max_{x in Omega_a} K(x,Omega\Omega_a).
```

Jerrum--Son--Tetali--Vigoda (JSTV), Theorem 1, states

```
gap(K) >= min{bar_lambda/3,
              bar_lambda*lambda_min/(3*gamma+bar_lambda)}.     (4)
```

For an arbitrary stochastic kernel, `gamma<=1`; for gaps at most one, (4)
therefore gives the product divided by four.  Here the explicit half-hold
improves `gamma<=1/2`.  The projection and restrictions retain at least a
half-hold, so their eigenvalues are nonnegative and their gaps are at most
one.  The first term of (4) is at least
`bar_lambda*lambda_min/3`; the second denominator is at most `5/2`, so the
second term is at least `2 bar_lambda*lambda_min/5`.  Their minimum proves
(1).

The current manuscript uses the phrase "restricted-fiber Poincare" without
defining its kernel.  Formula (1) applies only to the rejected-exit restriction
above.  A fiber chain that conditions on a macro-preserving proposal or
renormalizes accepted moves needs a separate action-rate Dirichlet comparison.
That comparison may lose badly when macro-preserving moves are rare.

Zero individual projection transitions are harmless: the JSTV proof invokes
edge-conditioned measures only for positive projection edges.  A reducible
projection or restriction, however, has gap zero and makes (4) vacuous.  Global
irreducibility forces projection irreducibility but does not force each
rejected-exit restriction to be irreducible.

### 2.2 Orthogonal-projection formulation and `m=4`

For a fixed `(i,r)`, partition the word space by the unchanged exterior letters
and the ordered product of the block.  `H_{i,r}` is conditional expectation
onto that partition and hence an orthogonal projection in `L^2(pi)`.  Therefore
`I-H_{i,r}` is positive semidefinite and

```
I-K = (1/(2|R_m|)) sum_r (1/(m-r+1)) sum_i (I-H_{i,r}).        (5)
```

When `m=4`, `R_m={3,4}` and `H_{1,4}` is uniform refresh of the whole identity
fiber.  It annihilates every mean-zero function, while its coefficient in (5)
is `1/4`.  All other terms are positive semidefinite, proving (2).  Formally,
the same argument gives `gap(K_{N,5})>=1/6`, but the identity bridge is empty
at odd length.

More generally, on the full word space define the finite-range,
frustration-free operator

```
A_{N,m} = sum_{r in R_m} sum_i (I-H_{i,r}).
```

For `m>=6`, coefficient comparison gives

```
(1/(6m)) A_{N,m} <= I-K <= (1/(6(m-4))) A_{N,m}               (6)
```

as quadratic forms on each total-product sector.  This identifies the problem
with a one-dimensional finite-range conditional-expectation Hamiltonian up to
the displayed polynomial normalization.  No finite-size criterion checked in
this audit automatically bounds its identity-sector gap: the local alphabet
grows with `N`, the sector constraint is global, and a gapless diffusive mode is
not ruled out.

### 2.3 Parity-block bridge construction

Let `M=binom(N,2)` and let `P` be the uniform measure on transpositions.  For
`m=2n`, group letters into

```
Y_j=t_{2j-1}t_{2j}.
```

Let `a(y)` be the number of ordered transposition pairs with product `y` and
`Q(y)=a(y)/M^2`.  Counting the possible intersections of two transposition
supports gives

```
a(id)=M,
a(y)=3  for each 3-cycle y,
a(y)=2  for each product y of two disjoint transpositions,
a(y)=0  otherwise.
```

Every unconditioned transposition word has mass `M^{-2n}`.  Consequently, after
conditioning the total product to be identity, the increment vector has law

```
Pr(Y_1=y_1,...,Y_n=y_n | product=id)
  proportional to 1{y_1...y_n=id} product_j Q(y_j),            (7)
```

and, conditional on `(Y_j)`, each micro-pair is independently uniform among
its `a(Y_j)` factorizations.

An aligned `H_{2j-1,4}` chooses a quadruple uniformly conditional on its
product.  Under pairing, a candidate `(y,y')` has exactly `a(y)a(y')`
quadruples, so the induced law is precisely two independent `Q` increments
conditioned on `yy'` being the fixed two-step product; its micro-pairs are then
uniform.  This proves the claimed identification of `B`.

For `m>=6`, the contribution of every length-four window to (5) has coefficient
`1/[6(m-3)]`.  Retaining only the `n-1` aligned windows gives

```
E_K(f,f) >= (1/[6(m-3)]) sum_{j=1}^{n-1}<f,(I-H_{2j-1,4})f>
          = ((n-1)/[6(m-3)]) E_B(f,f)
          = ((m-2)/[12(m-3)]) E_B(f,f)
          >= (1/12) E_B(f,f).
```

Taking the Poincare infimum proves (3).  This is a bridge-measure/functional-
inequality route, not a normal-form canonical-path or support projection.

## 3. Quantitative primary-source audit

### Hurwitz actions

- **Ben-Itzhak--Teicher, Theorem 3.4.**  For two factorizations of identity
  into the same number of factors, their braid/Hurwitz orbits agree exactly
  when their labeled factorization-graph components and component weights
  agree.  Definition 1.3 uses
  `(t_k,t_{k+1})->(t_k t_{k+1} t_k^{-1},t_k)`, the inverse of the project's
  common right generator; the equivalence relation is the same.  This applies
  literally to qualitative orbit classification, not to diameter,
  conductance, or spectral gap.  Primary source:
  [arXiv:math/0110110](https://arxiv.org/abs/math/0110110), local audited PDF
  `Literature/0110110v1.pdf`.

- **Khachatryan-Raziel, arXiv:1508.02620.**  The paper's Hurwitz graph has
  vertices given by reduced transposition factorizations of the long cycle and
  edges given by local shifts.  It studies radius, center, and diameter-type
  properties, not Poincare constants or mixing.  Its state space and endpoint
  differ from the identity factorizations here.  Source:
  ["On the center of the Hurwitz graph"](https://arxiv.org/abs/1508.02620).

Targeted primary-source searches for "Hurwitz graph/action" together with
"spectral gap," "mixing time," and "random walk" located structural,
diameter, and enumeration papers but no quantitative theorem for the identity
Hurwitz orbit chain.  This is a report of the targeted search, not a theorem
that no such result exists.

### Transposition-factorization enumeration and exact sampling

- **Duchi--Poulalhon--Schaeffer, Proposition 1, Theorem 5, Proposition 6,
  Corollary 2.**  Proposition 1 bijects indexed increasing quadrangulations of
  size `N` with connected/transitive identity factorizations of the minimal
  length `2N-2` (their displayed multiplication order is reversed relative to
  this report, immaterial after reversing a word).  Theorem 5 gives uniform
  generation through Hurwitz trees; Proposition 6 proves the fast construction
  is linear time and space; Corollary 2 gives the exact count
  `N^{N-3}(2N-2)!` and uniform linear-time generation.  This applies only to
  one connected, near-minimal macro-fiber and is a perfect sampler, not a gap
  theorem for a local rewrite chain.  Primary source:
  [SODA paper PDF](https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf), DOI
  [`10.1137/1.9781611973402.21`](https://doi.org/10.1137/1.9781611973402.21).

- Classical simple Hurwitz-number formulas enumerate connected factorizations
  at fixed genus/surplus, but an exact state count alone does not bound local
  boundary flow.  No enumerative formula found in this audit supplies a
  comparison congestion or a bridge Gibbs inequality.

### Random-map surgery chains

- **Caraceni, Theorem 1, equation (1), Lemma 3.1.**  On rooted planar maps with
  `n` edges, choose one of the `2n-1` nonroot corners and one of three symbols
  `{=,+,-}` independently, so an elementary choice has probability
  `1/[3(2n-1)]`.  Lemma 3.1 proves uniform reversibility, aperiodicity, and
  irreducibility.  Theorem 1 identifies the gap with the non-root-flipping
  quadrangulation flip chain and proves constants `C_1,C_2>0` with
  `C_2 n^{-11/2} <= gap <= C_1 n^{-5/4}`, hence mixing `O(n^{13/2})`.
  Primary source:
  [arXiv:2001.04166](https://arxiv.org/abs/2001.04166).

  This does **not** transfer through the Duchi bijection.  Duchi's objects are
  indexed increasing quadrangulations carrying face/order and vertex labels,
  not uniform rooted planar maps, and no intertwining between a word
  `r=3,4,5` heat bath and a bounded number of Caraceni rotations was proved.
  Even the stationary measures therefore do not match after forgetting the
  extra structure.

### Heat baths, decomposition, and mean lift

- **Jerrum--Son--Tetali--Vigoda, Theorem 1.**  Exact statement and application
  are given in Section 2.1.  It literally applies once the project's fiber
  kernels are defined as rejected-exit restrictions and their gaps are proved.
  It removes the separate mean-lift obligation, but proves neither constituent
  gap.  Primary source:
  [arXiv:math/0503537](https://arxiv.org/abs/math/0503537), DOI
  [`10.1214/105051604000000639`](https://doi.org/10.1214/105051604000000639).

- **Dyer--Greenhill--Ullrich, Definition 1.1 and Lemma 1.2.**  A heat-bath
  kernel is an arbitrary convex combination of stationary conditional-fiber
  kernels.  Each component is idempotent and reversible; Lemma 1.2 proves the
  mixture has no negative eigenvalues.  The nonlazy local average
  `P_0=(1/|R_m|)sum_r avg_i H_{i,r}` literally satisfies this definition on
  each product sector.  Thus `P_0` is positive semidefinite and the prescribed
  `K=(I+P_0)/2` satisfies `gap(K)=gap(P_0)/2`.  This checks spectral
  normalization but supplies no positive lower bound.  Primary source:
  [arXiv:1301.4055](https://arxiv.org/abs/1301.4055), DOI
  [`10.1016/j.laa.2014.04.018`](https://doi.org/10.1016/j.laa.2014.04.018).

### Random-transposition walks and bridge block dynamics

- **Diaconis--Shahshahani, Lemma 5 and Corollary 1.**  A central walk on
  `S_N` diagonalizes in irreducible representations by character ratios.
  Their specific random-transposition measure chooses two uniform labels, so
  it has identity mass `1/N` and mass `2/N^2` on each transposition; Corollary
  1 gives its exact scalar Fourier transform.  Removing the identity mass
  yields the familiar uniform-transposition spectrum, and parity blocking
  yields the base law `Q` above.  This is an unconditioned endpoint walk
  theorem.  It gives return-probability formulas but no Poincare inequality
  for the path law conditioned to return.  Primary source: P. Diaconis and
  M. Shahshahani, "Generating a Random Permutation with Random
  Transpositions," *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 57 (1981),
  159--179, DOI
  [`10.1007/BF00535487`](https://doi.org/10.1007/BF00535487).

- General spectral-independence/approximate-tensorization theorems require an
  influence or entropy-factorization estimate uniformly under all feasible
  pinnings.  Endpoint conditioning here is precisely the source of those
  influences, so invoking such a theorem before proving its hypothesis merely
  renames the bridge proposition.  Targeted searches did not locate a general
  finite-group theorem saying that an inverse-polynomial base-walk gap implies
  an inverse-polynomial local Gibbs gap for all fixed-endpoint paths.

### Kassabov generators and reversible-circuit transfer

- **Kassabov, Theorems 2 and 3.**  There are universal `L<infinity` and
  `epsilon>0` and explicit generating sets of size at most `L` making all
  alternating, respectively symmetric, group Cayley graphs an
  `epsilon`-expander.  These are unconditioned Cayley walks with a different
  bounded generator set.  Source:
  [arXiv:math/0505624](https://arxiv.org/abs/math/0505624), published as
  "Symmetric Groups and Expander Graphs," *Invent. Math.* 170 (2007).

- **Chen--Haah--Haferkamp--Liu--Metger--Tan, Theorem 1.1.**  For `n>=4` bits
  and `t>=1`, the `t`th moment operator of an all-to-all random 3-bit
  reversible-gate walk is within operator norm `1-Omega(n^{-3})` of the
  uniform `Alt(2^n)` moment operator.  This is an unconditioned circuit/moment
  statement, not a gap for all-transposition words conditioned on identity.

- **Theorems 5.1 and 5.2 of the same paper.**  Theorem 5.1 restates Kassabov's
  constant Kazhdan bound for a constant-size generating set of
  `Alt((2^{3s}-1)^6)`, `s>6`.  Theorem 5.2 gives, for every bit count `n>=1`,
  a constant-size generating set of `Alt(2^n)` with a uniform Kazhdan constant;
  each generator is a strongly explicit ancilla-free `O(n)`-gate circuit over
  NOT/CNOT/Toffoli and each bit participates in `O(1)` gates.  This is a useful
  separate expander-bridge benchmark, but neither theorem transfers to
  `K_{N,m}` without a new comparison of endpoint-conditioned path measures.
  Source: [arXiv:2406.07478](https://arxiv.org/abs/2406.07478), local audited
  version `Literature/2406.07478v3.pdf`.

## 4. Probability, runtime, path length, and congestion accounting

- A particular full-chain update choice `(r,i)` has outer selection mass
  `1/[2|R_m|(m-r+1)]`; the leading `1/2` is holding.  Conditional outcomes
  have mass equal to that selection mass divided by the exact block-fiber
  size, summed over choices that produce the same next word.
- In a JSTV restriction, every off-fiber outcome contributes holding mass.
  Hence `gamma<=1/2` exactly.  No lower bound on the rate of macro-preserving
  action is assumed or silently canceled.
- The aligned bridge comparison loses the exact factor
  `12(m-3)/(m-2)<12`, independent of `N,m`; see (3).
- An exact length-four update is polynomial-time even by brute-force
  enumeration.  The midpoint implementation enumerates at most `M^2=O(N^4)`
  ordered pairs and their products; using explicit permutation arrays gives a
  conservative `O(N^5)` target-table build and polynomial memory, followed by
  exact weighted and uniform draws.  Fixed block lengths 3 and 5 are also
  polynomial by exhaustive enumeration (`O(M^5 poly(N))` is already
  polynomial), while the durable direct samplers are substantially faster.
- Duchi's perfect generator has proved `O(N)` time and space only in the
  connected minimal case.  Caraceni's gap bound is for its own
  `1/[3(2n-1)]` rotation normalization.
- No canonical paths, comparison paths, or congestion bound are claimed in
  M15.  The missing bridge proposition is a Poincare problem, not a hidden
  zero-congestion assertion.

## 5. Dependencies and status

- **Proved directly:** equations (2), (3), (5)--(7); exact `Q` multiplicities;
  the `1/3` corollary of JSTV for the half-lazy kernel; polynomial fixed-block
  enumeration cost.
- **Cited with checked hypotheses:** JSTV Theorem 1; Dyer--Greenhill--Ullrich
  Definition 1.1/Lemma 1.2; Ben-Itzhak--Teicher Theorem 3.4; Duchi et al.
  Proposition 1/Theorem 5/Proposition 6/Corollary 2; Caraceni equation
  (1)/Lemma 3.1/Theorem 1; Kassabov Theorems 2--3; Chen et al. Theorems 1.1,
  5.1, 5.2; Diaconis--Shahshahani Lemma 5/Corollary 1.
- **Conditional:** a universal polynomial gap for `B_{N,n}`; a universal
  projection gap; uniform gaps for every rejected-exit macro-fiber
  restriction; full qualitative irreducibility until M01's separate audit is
  incorporated.
- **Exact finite computation only:** aligned-`r=4` connectivity in the three
  calibration cases.  It can falsify but cannot prove the conditional bridge
  statement.
- **Search finding, not a mathematical claim:** no directly applicable
  quantitative Hurwitz/bridge theorem was found by the targeted local and
  external searches.

## 6. First unproved standalone proposition

**Parity-block bridge Poincare proposition.**  There exist universal constants
`c>0` and `C<infinity` such that for every `N>=3` and every integer `n>=3`, the
chain

```
B_{N,n}=(1/(n-1))sum_{j=1}^{n-1}H_{2j-1,4}
```

on the uniform length-`2n` transposition identity bridge is irreducible and

```
gap(B_{N,n}) >= c (Nn)^(-C).                                  (8)
```

By (2), (3), and the polynomial sampler accounting, (8), together with the
checked qualitative irreducibility dependency, would imply the literal
TERMINAL A bound for every admissible `m`.

An equivalent path formulation may be more tractable: update one interior
vertex at a time in a length-`n` return path whose increments have law `Q`,
while refreshing the two associated transposition microfactorizations.  The
base character spectrum can be used to estimate convolution/return ratios;
the genuinely new obligation is to turn those ratios into a bridge Poincare
inequality uniformly through sparse and near-minimal regimes.

## 7. Strongest self-attack

The aligned chain `B` is a strict subchain of `K`.  It may possess a hidden
invariant or a superpolynomial bottleneck even if the full `{3,4,5}` chain does
not; the exact small checks cannot exclude this.  More conceptually, a
polynomial base-walk gap for `Q` says nothing by itself about the common-
neighbor geometry after every endpoint pinning.  Fixed-endpoint path measures
can have long-range dependence and disconnected single-site dynamics.

The JSTV correction removes one named obligation but not necessarily the hard
one: a rejected-exit restriction can be far slower than a renormalized
within-fiber chain because most update mass may leave the macro-fiber and become
holding.  Moreover, if an individual restriction is disconnected, the theorem
is vacuous even though excursions through other fibers connect the full chain.

Finally, the map-surgery route has a serious measure-preservation mismatch:
forgetting increasing labels/order is many-to-one with nonconstant fibers, and
there is no proved local intertwining.  Caraceni's polynomial gap cannot be
imported by analogy.

## 8. Calibration results

- **Odd `m`:** `Omega(N,m)` is empty by sign.  The formal `m=5` whole-block
  inequality is therefore vacuous for the identity target.
- **`m=0`:** singleton; outside the stated kernel regime.
- **`N=2`, even `m`:** singleton.  No cited theorem is used to inflate this to
  a nontrivial gap claim.
- **`m=2`, `N>=3`:** excluded and disconnected under the stated block choices.
  The parity-block proposition begins at `n=3` (`m=6`).
- **`S_3,m=4`; `S_4,m=4`; `S_4,m=6`:** exact enumeration reproduced 27, 120,
  and 3936 identity words.  The aligned subchain had respectively one
  component of those full sizes.  The first two are also covered by the exact
  whole-word lower bound `1/4`.
- **`m=4` normalization:** `H_{1,4}` is retained and has coefficient `1/4` in
  `I-K`; it is not ignored as a lower-order update.
- **Near-minimal doubled trees:** Duchi's bijection/count/sampler applies to
  the connected `m=2(N-1)` fiber, but not to other macro-fibers or to the local
  gap.  No normal form is used in (1)--(8).
- **Color interleavings:** the parity bridge retains the complete ordered word
  and hence the interleaving; the planar-map transfer was rejected in part
  because forgetting labels/order changes this law.
- **Parity summaries:** the construction uses the exact ordered product and
  exact multiplicities `a(y)`, not edge-multiplicity or vertex-degree parity.
- **Known `L=2` failure:** no length-two transposition simulation is asserted.
  An aligned move is an actual length-four heat bath; its two-site description
  is after changing the alphabet to `Q` increments.
- **Canonical hub:** no path is routed through a fixed doubled tree or square
  hub, so the known exponential hub-mass obstruction is not invoked.
- **Bottleneck mass/flow:** no asymptotic cut is proposed.  Thus there is no
  stationary-mass or boundary-flow claim masquerading as a refutation.

## 9. Artifacts, reproduction, and citations

Artifacts in this mission directory:

- `plan.md`: declared target and failure modes.
- `checkpoint.md`: exact JSTV theorem application and bridge reduction.
- `aligned_r4_connectivity.py`: deterministic exhaustive connectivity test.
- `results.json`: machine-readable output.
- `report.md`: this report.

Reproduction command (Python 3.12.3, no nonstandard dependencies, no random
seed because the calculation is deterministic):

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M15/aligned_r4_connectivity.py \
  --case 3,4 --case 4,4 --case 4,6
```

The run completed in approximately 2.7 seconds on the current machine.  Every
external source retained above is linked directly to its primary paper or DOI.
The local source audit included every mandated manuscript section and indexed
experiment report, both supplied PDFs, and relevant history through the
current commit.  Temporary PDF copies used only for source inspection were
kept under `/tmp` and are not project artifacts.

OPEN AT A NAMED STEP: Parity-block bridge Poincare proposition.

