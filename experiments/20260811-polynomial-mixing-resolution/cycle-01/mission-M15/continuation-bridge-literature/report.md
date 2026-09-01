# M15 continuation report: bridge literature and planar-map transfer

Date: 2026-08-11  
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Executive result

No audited primary theorem supplies an inverse-polynomial gap, with constants
polynomial in `N` and bridge length, for the aligned `Q_N=P_N*P_N` bridge
chain.  This report identifies a literal hypothesis or normalization mismatch
for each closest theorem.  More decisively, an exact feasible boundary pair
violates the natural corrected hypothesis of the closest weighted-path
theorem at `N=5`, and at `N=6` forces the Perron root of every standard
dependency matrix above one on a path with nine interior sites.

The proposed direct transport of Caraceni's planar-map gap through the
Duchi--Poulalhon--Schaeffer bijection is also false: the state spaces and
uniform measures differ, the relevant subset is not closed under Caraceni
flips, and Caraceni's proved intertwining uses Tutte's different bijection.

These are rigorous refutations of the named **transfer claims**, not of the
aligned bridge Poincare proposition and not of TERMINAL A.  Failure of
Dobrushin contraction is not evidence of a bottleneck.

## 1. Exact claims, quantifiers, and conventions

Composition is `(pq)(x)=p(q(x))`.  Let `P_N` be uniform on the
`M=binom(N,2)` transpositions, let `Q_N=P_N*P_N`, and put

```text
a_N(g)=M^2 Q_N(g)
      = #{(u,v): u and v are transpositions, uv=g}.
```

For a uniform length-`2n` transposition identity word, pair adjacent letters,
set `Y_j=t_{2j-1}t_{2j}`, and define prefixes
`X_0=e`, `X_j=Y_1...Y_j`, `X_n=e`.  The prefix marginal is

```text
mu_N,n(x_1,...,x_{n-1}) proportional to
  product_{j=1}^n Q_N(x_{j-1}^{-1}x_j).                       (1)
```

The chain under this audit is the **nonlazy** aligned average

```text
B_{N,n}=(1/(n-1)) sum_{j=1}^{n-1} H_{2j-1,4}.                 (2)
```

It updates one interior prefix `X_j` from its conditional law in (1) and
simultaneously refreshes the two adjacent ordered-transposition
microfactorizations.  Every site has action rate exactly `1/(n-1)`.  Since
each summand is a conditional-expectation projection, `B` is positive
semidefinite despite having no imposed laziness.  The sibling M15 report
proved the exact comparison

```text
gap(K_{N,2n}) >= gap(B_{N,n})/12,        N>=3, n>=3.           (3)
```

The spectral gap throughout is the Poincare constant `1-lambda_2`; for these
positive semidefinite heat-bath averages it also equals the absolute gap.

The claims resolved here are the following.

**C1 (fixed-target path-theorem transfer, refuted).**  Neither Dyer--Goldberg--
Jerrum Theorem 28 nor Pedersen Theorems 4/6 gives a bound polynomial in
`N,n` for (2).  Their target graph is fixed and unweighted, their boundary
and/or update kernels differ, and retaining their displayed target-size
dependence is superpolynomial for `|A_N|=N!/2`.

**C2 (weighted-path contraction transfer, refuted).**  Lyu--Memoli--Sivakoff
Theorem 2.4 cannot be invoked as printed because its displayed definition and
the inequalities used in its proof do not align.  Under the natural
worst-case repair, its positive
contraction hypothesis is false for `Q_5`.  The Dobrushin row/column-sum
conditions and every dependency-matrix norm `<1` condition of
Dyer--Goldberg--Jerrum are false for the actual pinned `Q_6` path once there
are nine interior sites.

**C3 (Caraceni-through-Duchi direct transfer, refuted).**  The Duchi bijection
does not identify the uniform minimal-factorization chain with Caraceni's
uniform quadrangulation flip/rotation chain, either as a stationary-measure-
preserving isomorphism or as the bounded transition intertwining proved in
Caraceni Proposition 4.1.

The phrase “no theorem was located” outside C1--C3 is only a targeted search
finding.  No universal nonexistence claim about the literature is made.

## 2. Full argument and construction

### 2.1 Exact bridge representation

Two transpositions have product only of the following types:

```text
a_N(e)=M;
a_N(g)=3 if g is a 3-cycle;
a_N(g)=2 if g is a product of two disjoint transpositions;
a_N(g)=0 otherwise.                                          (4)
```

Indeed, equal factors give `e`; two distinct factors sharing one endpoint
give a 3-cycle with three possible ordered decompositions; disjoint factors
commute and give two orders.  Since every unconditioned transposition word
has the same mass, pairing and conditioning the endpoint gives (1), and the
microfactorizations over each `Y_j` are conditionally independent and
uniform among their `a_N(Y_j)` choices.  A four-letter heat bath therefore
is precisely the prefix heat bath plus the two microfactor refreshes claimed
in (2).

For fixed neighbors `a,c`, the conditional law of the middle prefix `b` is

```text
mu_{a,c}(b) =
  Q_N(a^{-1}b) Q_N(b^{-1}c)
  / sum_z Q_N(a^{-1}z) Q_N(z^{-1}c).                          (5)
```

This is the convention used both in the proof and in the exact harness.

### 2.2 Fixed-`H` path theorems: explicit target-size dependence

Dyer, Goldberg and Jerrum, “Systematic scan for sampling colorings,”
*Annals of Applied Probability* 16 (2006), Theorem 28, considers a free
`L`-vertex path and a fixed connected, possibly looped, unweighted graph
`H`.  Its state space is all `H`-colourings if `H` is nonbipartite and one
compatible class if it is bipartite.  Its random-update `M_Gl` chooses one
site and proposes one of `h=|V(H)|` colours uniformly; an accepted
elementary transition has probability `1/(Lh)`.  The theorem states

```text
Mix(M_Gl,epsilon)=O_H(L^5 log(epsilon^{-1})).                 (6)
```

The hidden constant cannot be discarded here.  In Section 8, Lemma 27 takes
`t=4h-1` or `4h` in the nonbipartite cases.  The canonical path has length at
most `L(L+t)/2`.  Its encoding records an index (at most `L+t` choices), two
colours, a reverse window state, and `2(t-1)` extra colours.  Hence the
number of source/target pairs using a transition is at most

```text
(L+t) h^(2t) |Omega|.
```

Substitution into equation (28), retaining `P_Gl(alpha,beta)=1/(Lh)`, gives
the fully explicit valid bound

```text
A <= (1/2) L^2 (L+t)^2 h^(2t+1),                             (7)
gap(M_Gl) >= 1/A.
```

The paper writes `A=O(L^4)` only after declaring `H`, hence `h,t`, fixed.
For the support Cayley graph of `Q_N`, `h=|A_N|=N!/2` and `t` is of order
`h`, so (7) is far outside every polynomial in `N,L`.

Even (7) is not literally a bound for `B`: the theorem's law is uniform on
unweighted free-path homomorphisms, its update is a one-colour Metropolis
proposal, and it has no edge microfactor labels.  Equation (1) is weighted,
has both endpoints pinned to `e`, and (2) is an exact heat bath.  A new
weighted/pinned comparison would be needed.

Pedersen, “On systematic scan for sampling H-colourings of the path,”
arXiv:0706.3794, also takes a fixed connected unweighted `H`.  In its notation
`q=|V(H)|` and `s=4q+1`.  Definition 5 sets

```text
gamma=2 q^s+1
```

and the random-update chain of Theorem 6 selects among overlapping
heat-bath blocks of size at most `s gamma`.  Theorem 4 uses another prescribed
fixed-order block construction whose sizes also contain `q^s`.  Thus these
are not single-site dynamics (2), and for `q=N!/2` the block size and
constants are superpolynomial in `N`.  Free endpoints and unweighted uniform
`H`-colourings are additional literal mismatches.

The structural support graph itself is not the difficulty hidden here:
3-cycles generate `A_N`, so it is connected, and `e,g,g^2` form a triangle
for a 3-cycle `g`; moreover `Q_N(e)>0` supplies loops.  It is the quantitative
target dependence, weights, pins, and update kernel that prevent transfer.

### 2.3 Closest weighted graph-homomorphism theorem

Lyu, Memoli and Sivakoff, “Sampling random graph homomorphisms and
applications to network data analysis,” *JMLR* 24(9) (2023), equation (30),
defines the same weighted one-site conditional law as (5) when its target
network has vertex set `A_N`, vertex weights uniform, and edge weight
`A(a,b)=Q_N(a^{-1}b)`.  Its Glauber site selection also has the desired
uniform one-site normalization for the prefix marginal.

Theorem 2.4 nevertheless cannot be used as a checked dependency in its
published form.  Equation (31) defines

```text
c(d,G)=max_{x~x', x(1)=x'(1)}
       (1-2d ||mu_{x,1}-mu_{x',1}||_TV),                     (8)
```

where `x~x'` means “differ by at most one coordinate.”  Equal maps are
admissible, so (8) is exactly `1`: total variation is nonnegative and the
equal pair attains one.  In the proof of Lemma B.2, equation (160) needs the
bracket to be bounded **below**, but the text says it is at most `c` and then
deduces contraction.  Lemma B.2 equations (156) and (162) decay as
`exp(-ct/k)`, requiring a mixing bound proportional to `1/c`, whereas
Theorem 2.4 equation (32) multiplies by `c`.  Equation (161) also prints
`-c/k` where the recurrence needs `1-c/k`.  No corrigendum was listed on the
JMLR paper page in the targeted search.  These may be max/min and reciprocal
typographical errors rather than a failure of the authors' intended result,
but the displayed theorem and proof do not establish the bound needed here.

The most favorable obvious repair replaces the maximum by a worst-case
minimum and replaces the mixing-time factor `c` by `1/c`.  It still fails
for this target.  Fix a 3-cycle `g`.  The two degree-two star configurations
with center `e` and leaf pairs `(e,e)` and `(g,e)` are feasible because
`Q_N(e),Q_N(g),Q_N(g^{-1})` are positive.  From (5), after canceling the
common `M^{-4}` denominator, their center weights are

```text
w_00(b)=a_N(b)^2,
w_g0(b)=a_N(g^{-1}b)a_N(b).                                 (9)
```

At `N=5`, exact enumeration gives

```text
sum_b w_00(b)=340,       sum_b w_g0(b)=207,
||w_00/340-w_g0/207||_TV=4441/11730.                         (10)
```

For auditability, the complete histogram
`(a_N(b),a_N(g^{-1}b),multiplicity)` behind (10) is

```text
(2,0,6), (2,2,3), (2,3,6), (3,0,6),
(3,2,6), (3,3,7), (3,10,1), (10,3,1).
```

Thus the repaired degree-two margin is

```text
1-4(4441/11730)=-3017/5865<0.                               (11)
```

The exact finite calculation legitimately refutes this universal theorem
hypothesis; it does not infer convergence or nonconvergence from finite data.

The same paper's Theorem 2.5 analyzes a pivot chain that updates a pivot/root
and redraws descendants.  It is not (2), and Remark 2.1 gives per-iteration
cost of order `Delta(G)^ell Delta(F)`, potentially exponential in motif depth
`ell`.  Its base-walk mixing statement is therefore neither a local bridge
gap nor a polynomial-cost simulation of `B`.

### 2.4 Exact obstruction to all standard dependency-matrix norms

Dyer, Goldberg and Jerrum, “Dobrushin conditions and systematic scan,”
*Combinatorics, Probability and Computing* 17 (2008), defines

```text
rho_{i,j}=max TV(conditional law at j under configurations
                  differing only at i).
```

Its standard random-update conclusion needs the maximum column or row
influence sum below one.  At `N=6`, the feasible pair above has

```text
v=1627/3060,              2v=1627/1530>1.                   (12)
```

Every interior prefix has two neighbors, and left/right symmetry of the
central symmetric law `Q_N` gives both influence lower bounds, so the usual
sum criterion fails.

There is no rescue by choosing a more favorable matrix norm within the
Dyer--Goldberg--Jerrum framework.  Their “Matrix norms and rapid mixing for
spin systems,” *Annals of Applied Probability* 19 (2009), Lemma 1 says that
if some dependency matrix `R` has a matrix norm at most `mu<1`, then the
random-update chain mixes in

```text
asymptotically L(1-mu)^(-1)
  log((1-mu)^(-1) ||J_L||/epsilon)                           (13)
```

steps.  Lemma 9 gives monotonicity of the Perron root for nonnegative
matrices, and Lemma 10 says `rho(R)<=||R||` for every matrix norm.

Take `L=9` interior bridge sites.  The all-identity prefix path is feasible.
Changing any one prefix from `e` to `g` is also feasible, because the two
new increments are `g` and `g^{-1}`.  Therefore every nearest-neighbor entry
of any valid dependency matrix is at least `v` from (12).  If `A(P_9)` is
the adjacency matrix of the nine-vertex path, then entrywise
`R>=vA(P_9)`.  Perron--Frobenius monotonicity and
`rho(A(P_9))=2cos(pi/10)>19/10` give

```text
rho(R) >= 2v cos(pi/10)
       > (19/10)(1627/3060)
       = 30913/30600 > 1.                                  (14)
```

Consequently `||R||>1` for every matrix norm.  This holds for the pinned
`N=6` bridge whenever `n-1>=9`, since the nine-site construction embeds in
the interior.  It is an exact failure of the sufficient hypothesis, not a
lower bound on mixing time.

### 2.5 Caraceni cannot be transported directly through Duchi

Duchi, Poulalhon and Schaeffer define `I_N` as indexed increasing
quadrangulations with exactly `N` black and `N` white vertices.  Their
quadrangulations are simple: no double edges, and every face has four
distinct edges and vertices.  Faces carry labels `1,...,2N-2`, black
vertices carry labels `x_1,...,x_N`, and “increasing” means the descent
orientation has exactly one descent incident to every vertex.  Proposition
1 is a bijection

```text
I_N  <->  minimal transitive identity factorizations in S_N
           of length 2N-2.                                  (15)
```

Their multiplication is `tau_{2N-2}...tau_1=e`; reversing the word converts
it to the present convention.  Corollary 2 counts both sides as
`N^(N-3)(2N-2)!` and gives uniform linear-time generation.

Caraceni's state spaces are instead `M_f`, all rooted planar connected
multigraph maps with `f` edges, and `Q_f`, all rooted unlabelled
quadrangulations with `f` faces.  Double edges, loops on the map side,
degree-one vertices and degenerate faces are explicitly part of the
definitions and transition rules.  Equation (1) chooses one of `2f-1`
nonroot corners and a symbol in `{=,+,-}`, giving elementary probability
`1/[3(2f-1)]`.  Lemma 3.1 proves the rotation chain reversible, aperiodic and
irreducible.  Theorem 1 proves, for universal positive constants,

```text
C_1 f^(-5/4) >= gap(rotation)=gap(nonroot flip)
             >= C_2 f^(-11/2),                              (16)
```

and the proof uses the uniform measure on all `Q_f`.  Proposition 4.1
intertwines nonroot flips with rotations through **Tutte's bijection**
`M_f<->Q_f`.

This does not yield a Duchi transport:

1. At `f=2N-2`, the Duchi image `I_N` is not `Q_f`: it is simple, labelled,
   indexed, increasing, and has fixed bipartition sizes.  Caraceni's uniform
   law assigns positive mass to states outside that class.  Hence the two
   uniform stationary measures are not pushforwards of one another under
   (15).
2. The Duchi-type subset cannot be closed under Caraceni flips.  Caraceni's
   chain is irreducible on all `Q_f`; both simple states arising from (15)
   and the paper's explicit double-edge/degenerate states exist.  A nonempty
   proper subset of an irreducible finite chain is not closed.  Some positive
   Caraceni flow must leave it.
3. Caraceni Proposition 4.1 proves only the Tutte intertwining.  A Duchi face
   label is a word position, whereas Caraceni's kernel has neither face
   labels nor the increasing orientation.  Neither source states or proves
   that changing four consecutive factors is one or boundedly many flips,
   or conversely.

Rejecting exits from a Duchi subset would turn their probability into
holding; decorating/lifting the chain would change stationary multiplicities;
and comparing to (2) would require explicit simulations and capacity
congestion.  None of the action-rate, stationary-flow, or congestion bounds
needed for that new chain follows from (16).  Thus the **direct** stationary-
measure-preserving bounded transfer is false.  This argument does not prove
that every future engineered comparison is impossible.

## 3. Worst-case probability, runtime, path length, and congestion accounting

- A `B` site is chosen with probability `1/(n-1)` and is then refreshed
  exactly from its conditional fiber.  `B` has no added lazy coin.  Its
  inherited comparison loss to `K` is the constant at most `12` in (3).
- Dyer--Goldberg--Jerrum's accepted elementary path-colouring proposal has
  probability `1/(Lh)`, canonical path length at most `L(L+t)/2`, and the
  unsuppressed congestion bound (7), with `t<=4h`; this is superpolynomial
  at `h=N!/2`.
- Pedersen's random-update theorem uses blocks of length at most
  `(4q+1)(2q^(4q+1)+1)`, not a constant uniformly in `q=N!/2` and not the
  one-site chain.
- The exact influence witnesses have probability-free worst-case force:
  they are feasible deterministic boundary conditions.  At `N=6`, (14)
  holds for every bridge with at least nine interior sites.
- Caraceni's elementary choice has mass `1/[3(2f-1)]`; the theorem's
  lower-gap exponent is `11/2`.  No rate is available after restricting,
  labelling, or simulating word moves because those are new, unanalyzed
  kernels.
- `bridge_influence.py` forms `M^2=O(N^4)` ordered transposition products,
  each using `O(N)` tuple arithmetic.  Its conservative worst-case time and
  memory bounds per `N` are `O(N^5)` and `O(N^5)`, respectively.  It is
  deterministic and uses exact rational arithmetic; no seed or nonstandard
  dependency is involved.

No comparison congestion or path family for `B` is claimed.  In particular,
the source failures are not being converted into a slow-mixing conclusion.

## 4. Dependencies and status

- **Proved directly:** equations (1)--(5); the exact Dyer target-size
  expansion (7); feasible-boundary construction; exact rational margins
  (10)--(14); Perron-root embedding argument; incompatibility of the two
  map state spaces and direct intertwinings.
- **Cited with hypotheses checked:** Dyer--Goldberg--Jerrum (2006), Section
  8, Lemma 27 and Theorem 28; Pedersen Definitions 3/5 and Theorems 4/6;
  Dyer--Goldberg--Jerrum (2008) influence definitions; Dyer--Goldberg--
  Jerrum (2009), Lemmas 1, 9, 10; Lyu--Memoli--Sivakoff equations (30)--(32),
  Theorems 2.4/2.5, Lemma B.2 and Remark 2.1; Duchi--Poulalhon--Schaeffer
  Proposition 1 and Corollary 2; Caraceni equation (1), Lemma 3.1,
  Proposition 4.1 and Theorem 1.
- **Conditional/open:** an inverse-polynomial gap or even a fresh proof of
  irreducibility for every `B_{N,n}`; a weighted bridge inequality exploiting
  the special convolution/representation structure beyond worst-case
  influence; any new decorated/restricted planar-map comparison.
- **Exact finite computation:** values (10) and (12), supported by complete
  machine-readable histograms.  They falsify named universal hypotheses but
  do not prove an asymptotic mixing assertion.
- **Search finding only:** the targeted local and primary-source search found
  no other theorem with checked hypotheses proving the desired bridge gap.

## 5. First unproved standalone proposition

**Aligned bridge Poincare proposition.**  There exist universal constants
`c>0` and `C<infinity` such that, for every `N>=3` and every integer `n>=3`,
the nonlazy chain (2), on the complete uniform length-`2n` transposition
identity bridge including its microfactor labels, is irreducible and

```text
gap(B_{N,n}) >= c (Nn)^(-C).                                 (17)
```

Together with the separately audited qualitative dependency, (3), and the
whole-word `m=4` case, (17) would imply TERMINAL A.  The exact first new
analytic subproblem is to prove a bridge Poincare inequality that tolerates
the worst-case influence in (11)--(14), presumably by multiscale blocks,
typical-boundary smoothing, representation modes, or another non-Dobrushin
mechanism.

## 6. Strongest self-attack

The most important limitation is logical: failure of every audited
worst-case contraction criterion does not imply a small gap.  The offending
prefix configurations may have little stationary weight, and block coupling
or an average-case functional inequality may still prove (17).  Likewise,
the fixed-`H` canonical path has bad displayed target dependence, but a new
proof exploiting the `A_N` Cayley geometry might replace `h=N!/2` by a
polynomial group diameter.

The criticism of Lyu--Memoli--Sivakoff is restricted to the published
formulae and their obvious correction.  The authors may have intended a
different metric or constant, but such a theorem is not in the cited source;
moreover the exact `N=5` witness must still be overcome.

For maps, this report refutes the literal Duchi/Caraceni isomorphism and the
claim that Caraceni's theorem itself supplies a bounded simulation.  It does
not prove that no carefully weighted lift, restriction, or randomized flow
can ever compare the chains.  Such a construction would be a new result and
must control off-subset holding, label multiplicities, path length, and edge
congestion.

Finally, a theorem for the prefix marginal alone would still need a checked
lift to the transposition-pair microfactorizations of `B`.  Those labels are
refreshed locally at rate of order `1/n`, suggesting only polynomial loss,
but that statement was not assumed here.

## 7. Calibration results

- **Odd `m`:** the identity bridge is empty by sign; no path theorem is
  applied to it.
- **`m=0`:** singleton and outside the stated kernel regime.
- **`N=2`, even `m`:** singleton; the target-graph calculations begin at
  `N=3`.
- **`m=2`, `N>=3`:** excluded/disconnected for the original local chain;
  proposition (17) starts at `n=3`, hence `m=6`.
- **`S_3,m=4` and `S_4,m=4`:** 27 and 120 identity words are retained as
  calibration.  The original `r=4` whole-word heat bath gives the separate
  `gap(K)>=1/4`; none of the path-theorem mismatches is used to handle it.
- **`S_4,m=6`:** 3936 identity words and 17 pure-Hurwitz components remain
  consistent with the sibling exact audit.  No finite connectivity result is
  promoted to (17).
- **Near-minimal doubled trees:** the Duchi bijection applies exactly to the
  connected minimal fiber `m=2(N-1)`, which is why the Caraceni state-space
  mismatch is relevant.  A theorem on this one fiber would still be
  nonterminal globally.
- **Colour interleavings:** (1)--(2) retain the full ordered word and its
  microfactor labels.  Forgetting labels/order in the map proposal is not
  declared measure preserving.
- **Parity summaries:** all calculations use exact ordered products and
  multiplicities (4), not edge or vertex-degree parity.
- **Known `L=2` failure:** no two-letter transposition simulation is used.
  “One-site” refers to a prefix vertex and exactly four original letters.
- **Canonical hub:** no route through a fixed doubled-tree or square hub is
  proposed; (7) is audited only to expose why a published fixed-`H` route is
  quantitatively unusable.
- **Stationary mass/boundary flow:** no asymptotic cut is proposed.  The map
  argument tracks the fact of positive exit flow only to reject a closed
  restriction, not to infer conductance.

## 8. Artifacts, reproduction commands, and exact citations

Artifacts in this directory:

- `plan.md`: declared transfer claims and expected failure modes.
- `checkpoint.md`: theorem-by-theorem source audit and exact frontier.
- `bridge_influence.py`: deterministic exact permutation/influence harness.
- `influence_results.json`: exact normalizers, rational total variations,
  conjugacy-count histograms, and matrix-norm flags for `N=3,4,5,6,7,8,9,10,12`.
- `report.md`: this nine-field report.

Reproduction command, run with Python 3.12.3, no nonstandard dependencies,
and no seed because it is deterministic:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M15/continuation-bridge-literature/bridge_influence.py \
  --N 3 --N 4 --N 5 --N 6 --N 7 --N 8 --N 9 --N 10 --N 12 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M15/continuation-bridge-literature/influence_results.json
```

Primary citations:

1. M. Dyer, L. A. Goldberg, M. Jerrum, “Systematic scan for sampling
   colorings,” *Ann. Appl. Probab.* 16 (2006), 185--230,
   [primary PDF](https://arxiv.org/pdf/math/0603323), DOI
   [`10.1214/105051605000000683`](https://doi.org/10.1214/105051605000000683).
2. K. Pedersen, “On systematic scan for sampling H-colourings of the path,”
   arXiv:0706.3794, [primary PDF](https://arxiv.org/pdf/0706.3794).
3. M. Dyer, L. A. Goldberg, M. Jerrum, “Dobrushin conditions and systematic
   scan,” *Combin. Probab. Comput.* 17 (2008),
   [author PDF](https://www.cs.ox.ac.uk/people/leslieann.goldberg/papers/dobrushinJournalRevision.pdf),
   DOI [`10.1017/S0963548308009437`](https://doi.org/10.1017/S0963548308009437).
4. M. Dyer, L. A. Goldberg, M. Jerrum, “Matrix norms and rapid mixing for
   spin systems,” *Ann. Appl. Probab.* 19 (2009), 71--107,
   [primary PDF](https://arxiv.org/pdf/math/0702744), DOI
   [`10.1214/08-AAP532`](https://doi.org/10.1214/08-AAP532).
5. H. Lyu, F. Memoli, D. Sivakoff, “Sampling random graph homomorphisms and
   applications to network data analysis,” *JMLR* 24(9) (2023), 1--79,
   [journal PDF](https://jmlr.org/papers/volume24/20-449/20-449.pdf) and
   [article page](https://jmlr.org/papers/v24/20-449.html).
6. E. Duchi, D. Poulalhon, G. Schaeffer, “Uniform random sampling of simple
   branched coverings of the sphere by itself,” SODA 2014,
   [author PDF](https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf), DOI
   [`10.1137/1.9781611973402.21`](https://doi.org/10.1137/1.9781611973402.21).
7. A. Caraceni, “A polynomial upper bound for the mixing time of edge
   rotations on planar maps,” *Electron. J. Probab.* 25 (2020), paper 99,
   [primary PDF](https://arxiv.org/pdf/2001.04166), DOI
   [`10.1214/20-EJP519`](https://doi.org/10.1214/20-EJP519).

## 9. Verdict

The terminal global question remains open.  The exact verdict below concerns
C1--C3: the audited theorem-transfer and direct map-transfer claims.

REFUTED
