# M13 report: Hurwitz-barbell and normal-quotient red team

This mission found no TERMINAL B obstruction. It rigorously eliminates every
normal group-quotient mode of a project Hurwitz orbit, gives independently
checkable polynomial flow accounting for the weaker cyclic candidate, and
proves a crude polynomial Hurwitz diameter. It also refutes three tempting
reductions of the remaining nonnormal Schreier geometry. The uniform
connected Hurwitz-orbit gap remains open.

## 1. Exact claims, quantifiers, and conventions

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`. A word is `t_1...t_m`. On a fixed identity
transposition Hurwitz orbit `F`, define

    P_H = (1/2) I
          + [1/(4(m-1))] sum_{i=1}^{m-1}(R_i+R_i^{-1}),

where, for transpositions,

    R_i(a,b)=(b,bab),       R_i^{-1}(a,b)=(aba,a).

The target law in this report is uniform on `F`.

### Claim A: all homomorphic normal quotient modes are trivial

For every feasible identity-transposition macro-fiber `F` of length
`m>=2`, let `B_m` act transitively by the project Hurwitz generators and
let `H` be the stabilizer of a base state. If a homomorphism
`rho:B_m -> G` satisfies `H subset ker(rho)`, then `rho` is trivial.
Consequently the Schreier action has no nontrivial factor obtained by passing
to a normal group quotient. This includes every ordinary braid-abelian,
finite-group, and pure-braid normal-quotient coordinate.

This does **not** exclude a quotient `B_m/H -> B_m/L` with a nonnormal
intermediate subgroup `H subset L`, or an arbitrary state-dependent
statistic.

### Claim B: exact weaker cyclic accounting

More generally, let `F` be any identity-product Hurwitz orbit of length
`m>=2` in any group. If a surjection `phi:F -> Z/qZ` satisfies

    phi(R_i x)=phi(x)+1 mod q

for every state and generator, then `q` divides `m(m-1)`. Uniform measure
pushes forward to uniform measure, and `P_H` pushes forward exactly to the
lazy nearest-neighbor cycle

    C_q(z,z)=1/2,
    C_q(z,z+1)=C_q(z,z-1)=1/4.

For `q>=2`,

    gap(C_q)=sin^2(pi/q) >= 4/q^2.

For every nonempty proper coordinate set `B subset Z/qZ`,

    Phi_pm(phi^{-1}(B)) >= 1/q >= 1/[m(m-1)].

For an interval of `k<=floor(q/2)` residues, the exact stationary mass,
directed boundary flow, and smaller-side conductance are

    pi(A)=k/q,
    Q(A,A^c)=Q(A^c,A)=1/(2q),
    Phi_pm(A)=1/(2k).

In the project orbits Claim A sharpens this to `q=1`, so the candidate cut
does not exist.

### Claim C: universal minimal-orbit locality

Let

    F_N={w in T_N^{2N-2}: product(w)=id, support(w) connected}.

For every `N>=2` and `w in F_N`, put
`X_j=t_1...t_j` and `h_j=N-cycles(X_j)`. Then:

1. `(h_j)_{j=0}^{2N-2}` is a Dyck path with exactly `N-1` joins
   (`h_j-h_{j-1}=1`) and `N-1` cuts.
2. The transposition edges at join positions are distinct and form a labeled
   spanning tree `T_join(w)`.
3. One `R_i` or `R_i^{-1}` changes no prefix height except `h_i`, and
   changes `h_i` by one of `{-2,0,2}`.
4. The join/cut word is unchanged or undergoes one adjacent
   `JC <-> CJ` flip, and
   `|T_join(w) triangle T_join(w')|<=2`: at most one tree edge is replaced.

Under uniform `F_N`, for every fixed labeled edge `e`,

    Pr(e in T_join)=2/N.

No universal boundary-flow bound for this fixed-edge statistic was proved, so
it is not asserted to be an asymptotic cut or a rejected cut.

### Claim D: polynomial Hurwitz diameter

For every `N>=2,m>=2` and every two length-`m` identity-transposition
words `x,y` with the same labeled weighted support components,

    dist_H(x,y) <= 50 N m^3.

The distance counts one project right or inverse Hurwitz generator as one
edge. This quantitatively audits the constructive proof of Classification H
in Ben-Itzhak--Teicher Lemmas 3.7--3.10. It rules out a superpolynomial
shortest-path-distance obstruction, but a graph of polynomial diameter can
still have exponentially small conductance.

### Exact finite refutations

Exhaustive deterministic enumeration proves the following finite statements.

- At `S_4,m=6`, `T_join` is not uniform over Cayley trees. Each of the
  four labeled stars has 186 preimages, while each of the twelve labeled
  paths has 178. Thus the star mass is `744/2880=31/120`, rather than
  `1/4`.
- The Dyck word is not an exact Markov lumping already at `S_3,m=4`.
  Two words with source path `JJCC` have oriented-generator destination
  counts respectively `{JCJC:1, JJCC:5}` and `{JJCC:6}`.
- The labeled join tree and first Pruefer coordinate are not exact lumpings
  already at `S_3,m=4`. The join-tree degree profile is not an exact
  lumping at `S_4,m=6`.

These are counterexamples to auxiliary reductions, not to polynomial mixing.

## 2. Full arguments and constructions

### 2.1 Stabilizer and conjugacy proof of Claim A

Use a left action, `sigma_i . x=R_i(x)`. For a base state `x_0`, let

    H=Stab_{B_m}(x_0).

The transitive orbit is identified with `B_m/H` by
`beta H -> beta . x_0`.

Every feasible project macro-fiber has a paired representative. For each
nontrivial labeled support component `V` of size `v` and even weight
`k>=2(v-1)`, choose a spanning tree `e_1,...,e_{v-1}`, write each tree
edge twice consecutively, and add
`[k-2(v-1)]/2` further consecutive copies of the pair
`(e_1,e_1)`. Concatenate the component words. The result has product
identity and exactly the prescribed labeled weighted components. Audited
Classification H therefore puts it in the given orbit.

Call this paired state `y=beta.x_0`. At every displayed equal pair,
`sigma_i.y=y`, since `R_i(s,s)=(s,s)`. Hence

    beta^{-1} sigma_i beta in H.

Now let `rho:B_m -> G` be a homomorphism with `H subset ker(rho)`.
Applying `rho` to the last display gives

    rho(beta)^{-1} rho(sigma_i) rho(beta)=1,

so `rho(sigma_i)=1`. All standard braid generators are conjugate in
`B_m`, and they generate `B_m`; therefore `rho` is trivial.

The hypothesis `H subset ker(rho)` is exactly what makes the coordinate
`rho(g)` well-defined on `gH`. A nonnormal intermediate subgroup need not
be contained in a normal kernel, which is why arbitrary Schreier bottlenecks
survive this argument.

### 2.2 Full twist and cyclic boundary proof of Claim B

Apply `R_1,R_2,...,R_{m-1}` in that temporal order to a tuple
`(g_1,...,g_m)`, and write `P=g_1...g_m`. One sweep sends it to

    (g_2,...,g_m,P^{-1}g_1P).

Indeed, if `u=g_2...g_m`, the last factor is
`u^{-1}g_1u=P^{-1}g_1P`. Product preservation lets this be iterated.
After `m` sweeps, every factor is conjugated by `P^{-1}`. For
`P=id`, this full twist fixes every state. The positive braid word used has
exactly `m(m-1)` standard generators. Equivariance of `phi` therefore
gives

    m(m-1)=0 mod q.

The bijection `R_1:phi^{-1}(z)->phi^{-1}(z+1)` shows that all coordinate
fibers have equal cardinality. In one `P_H` step, explicit laziness gives
holding probability `1/2`; the `m-1` positive generators, each with
coefficient `1/[4(m-1)]`, give total `1/4` to `z+1`; the inverse
generators give total `1/4` to `z-1`. This proves exact lumping.

For `q>=3`, any nonempty proper subset of the cycle has at least two
undirected boundary edges. Each contributes
`(1/q)(1/4)=1/(4q)` to directed stationary flow. At `q=2`, the two
generator orientations are parallel and give the same total. Thus
`Q(B,B^c)>=1/(2q)`; division by a smaller-side mass at most `1/2`
gives `Phi_pm>=1/q`. An interval has exactly the two stated boundary
contributions. Fourier modes of the lazy cycle give
`gap=sin^2(pi/q)`; `sin(pi/q)>=2/q` proves the displayed polynomial
bound.

### 2.3 Join-tree proof of Claim C

Every right multiplication by a transposition changes permutation cycle count
by exactly one, so each height increment is `+1` or `-1`. Identity
endpoints give `h_0=h_{2N-2}=0`, hence exactly `N-1` increments of each
sign.

Let `G_j` be the support graph of the first `j` factors. Every cycle of
`X_j` lies in one component of `G_j`, because the prefix permutation
preserves every support component. Any factor joining two distinct components
of `G_{j-1}` therefore joins two distinct cycles of `X_{j-1}`, so it is a
height increment. Connected final support requires exactly `N-1`
component-merging factors. There are only `N-1` height increments total,
so every increment is a component merge. Those edges successively merge
components from `N` to one; they are distinct, acyclic, and spanning.

A Hurwitz update at positions `i,i+1` preserves their ordered product.
Thus prefixes before `i` and after `i+1` are unchanged, and only the
intermediate prefix `X_i` can change. Both old and new intermediate prefixes
are one transposition from each fixed endpoint, proving the
`{-2,0,2}` height difference and the local peak/valley description.

The fixed endpoint heights determine how many of the two positions are joins.
If there are zero, neither tree changes. If there is one, each tree selects
one edge from the updated pair. If there are two, a right move
`(a,b)->(b,bab)` retains `b`, while an inverse move retains `a`.
In all cases at most one old tree edge is replaced.

Finally, relabeling by `S_N` preserves uniform `F_N` and is transitive on
the `M=binom(N,2)` possible edges. Since every join tree contains exactly
`N-1` edges, a fixed edge has inclusion probability

    (N-1)/M=2/N.

### 2.4 Exact finite computation and named flows

For a cut `A` in a finite orbit, let `C(A,A^c)` be the number of triples

    (x,i,epsilon),  x in A, 1<=i<=m-1, epsilon in {+,-},

whose oriented Hurwitz generator lands outside `A`. Uniform stationarity and
the exact kernel give

    Q(A,A^c)=C(A,A^c)/[4(m-1)|F|].

Pairing each generator with its inverse proves
`C(A,A^c)=C(A^c,A)`; the script also checks this equality.

For `S_3,m=4`, `|F|=24` and one oriented generator has probability
`1/12`. The Dyck-area cut `area<=2` has mass `1/4`, crossing count
12, flow `1/24`, and smaller-side conductance `1/6`. The fixed join-edge
cut has mass `2/3`, crossing count 20, flow `5/72`, and smaller-side
conductance `5/24`.

For `S_4,m=6`, `|F|=2880` and one oriented generator has probability
`1/20`.

- `area<=7`: mass `7/15`, crossing count 1440, flow `1/40`,
  conductance `3/56`.
- star join tree: mass `31/120`, crossing count 3312, flow `23/400`,
  conductance `69/310`.
- fixed join edge: mass `1/2`, crossing count 1808, flow `113/3600`,
  conductance `113/1800`.
- first Pruefer symbol in `{1,2}`: the same exact finite mass and flow as
  the fixed-edge cut.

All are finite calibration facts. None is extrapolated in `N`.

### 2.5 Quantitative Classification-H audit

Lemma 3.9 fronts any specified transposition in a connected word. A shortest
support path has at most `N-1` edges. Each path-shortening stage moves one
selected factor across at most `m-2` intervening factors and uses one
triangle rewrite; the final target crosses at most `m-1` factors. Thus one
fronting call costs at most `Nm` Hurwitz moves.

The canonical construction makes at most `m/2` square pairs and uses fewer
than `3m/2` fronting calls. Lemma 3.10 swaps adjacent square pairs in at
most four moves and slides an endpoint across a neighboring supporting pair
in three. Deliberately allowing `11m^2` moves to normalize each new pair
accounts for every pair reordering along a path of at most `m/2` existing
pairs. Component sorting costs fewer than `m^2` moves. Hence one word
reaches the componentwise canonical word within `25Nm^3` moves; two words
reach each other within `50Nm^3`.

The complete counter audit is in `diameter_audit.md`. The bound is not
turned into canonical paths: routing all pairs through the common canonical
word would concentrate flow on an exponentially rare hub. Thus Claim D is a
diameter theorem only, not a Poincare or conductance estimate.

### 2.6 Quadrangulation and authoritative-resource check

Duchi--Poulalhon--Schaeffer Proposition 1 bijects minimal transitive identity
factorizations with indexed increasing quadrangulations, and Proposition 3
gives an `N`-to-one correspondence from a Cayley tree plus a permutation to
their Hurwitz trees. This explains the exact count and perfect sampler, but it
does not make the prefix join tree uniform: the `S_4,m=6` counts above
rigorously distinguish those two trees. The paper contains no stated
Hurwitz-move, Markov-chain, or flip intertwining. Primary source:
[Duchi--Poulalhon--Schaeffer](https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf).

Caraceni--Stauffer prove polynomial gap for their edge-flip chain on uniform
rooted quadrangulations, and Caraceni proves a corresponding planar-map edge
rotation result. These stationary objects and moves are not the indexed
increasing quadrangulations with adjacent Hurwitz rewrites. No bounded local
simulation or measure-preserving projection is available, so those gap
theorems do not apply here:
[quadrangulation flips](https://arxiv.org/abs/1809.05092),
[planar-map rotations](https://arxiv.org/abs/2001.04166).

The earlier M15 primary-source audit likewise found structural and diameter
papers but no quantitative theorem for this exact identity Hurwitz walk. This
is a targeted search result, not an absence theorem.

## 3. Probability, runtime, path-length, and congestion accounting

- **Hurwitz kernel:** holding coefficient `1/2`; every oriented generator
  coefficient `1/[4(m-1)]`; total positive and inverse masses `1/4`
  each.
- **Cyclic cut:** exact masses and both directed flows are in Claim B. The
  full-twist certificate has path length exactly `m(m-1)`.
- **Normal-quotient proof:** uses existence of one paired representative. The
  constructive Classification-H path is bounded by Claim D, but is not used
  as a mixing path or comparison flow.
- **Minimal local move:** path length one; it replaces at most one tree edge.
  No congestion bound is inferred.
- **Hurwitz diameter:** at most `50Nm^3` inside each orbit. No stationary
  edge load, vertex load, or congestion bound follows from this diameter
  calculation.
- **Finite harness:** enumerates respectively `3^4=81`, `6^4=1296`, and
  `6^6=46656` candidate words. It checks 144 oriented generator outcomes on
  the 24-state `S_3,m=4` full orbit and 28,800 on the 2,880-state
  `S_4,m=6` full orbit. The final run took 3.5 seconds; a fresh rerun took
  5.1 seconds and was byte-identical. It is deterministic, with recorded seed
  130113, Python 3.12.3, and no nonstandard dependencies.
- **Connection to the target heat bath:** inherited accepted Cycle-01 M13
  accounting for the standard rejected-exit restriction `K^F` gives, with
  `M=binom(N,2)` and `B=|R_m|`,

      E_{K^F}(f,f)
        >= [(m-1)/(2B(m-2)M^2)] E_{P_H}(f,f).

  Exits from `F` are held on the diagonal. At `m=4`, this coefficient is
  `3/(8M^2)`; the whole-word `r=4` heat bath remains present in `K` but
  is not used in the comparison. This is one-way: slow `P_H` does not imply
  slow `K`.
- **No claimed routing:** no canonical path, diameter-to-gap inference, or
  congestion estimate appears in this report. The new coordinator
  `D_N=(3N^2+N-12)/2` triple-fiber sharpening was not needed because no
  direct `K` square-boundary construction survived.

## 4. Dependencies with status

1. **Proved:** algebra of right/inverse Hurwitz moves, product preservation,
   full-twist action, cyclic quotient kernel and flow, minimal join-tree and
   one-edge locality lemmas, fixed-edge mass `2/N`, and the quantitative
   `50Nm^3` Hurwitz diameter audit.
2. **Proved finite calculation:** all entries in `results.json`, including
   normalization, reversibility of crossing counts, orbit sizes, nonuniform
   join-tree counts, nonlumpability witnesses, and named finite cut flows.
3. **Cited and audited:** Ben-Itzhak--Teicher Theorem 3.4 / Classification H
   and the inverse-convention translation. Its Lemmas 3.7--3.10 are the
   constructive input to Claim D; every nested counter is bounded explicitly
   in `diameter_audit.md`.
4. **Cited:** Duchi--Poulalhon--Schaeffer Propositions 1 and 3 for increasing
   quadrangulations, Hurwitz trees, and enumeration. They supply no local gap.
5. **Cited but inapplicable:** Caraceni--Stauffer and Caraceni polynomial gaps
   for their own uniform quadrangulation/map chains.
6. **Proved inherited:** standard restriction normalization and
   `E_{K^F} >= [(m-1)/(2B(m-2)M^2)]E_{P_H}` from Cycle-01 M13, accepted in
   ledger L-0026.
7. **Conditional/unresolved:** no uniform lower bound for the gap of `P_H`;
   no comparison between Hurwitz moves and Duchi/Caraceni local dynamics.
8. **Empirical:** none. Exhaustive small calculations are exact finite facts,
   but they have no asymptotic force.

## 5. First unproved standalone proposition

**Uniform connected Hurwitz-orbit gap.** There exist universal constants
`c>0` and `C<infinity` such that for every `v>=2` and every even
`k>=2(v-1)`, the lazy symmetric random-scan Hurwitz walk on

    F(v,k) = {
      (t_1,...,t_k) in T_v^k:
      t_1...t_k=id and the support graph is connected
    }

satisfies

    gap(P_H^{v,k}) >= c(vk)^{-C}.

For `v=2` the state space is a singleton; the content begins at nontrivial
connected orbits. The smallest especially exposed regime is
`k=2(v-1)`.

A proof would combine with the accepted inverse-polynomial restriction
comparison, but it would still leave the macro projection required by JSTV.
A disproof of this proposition alone would not establish TERMINAL B for
`K`.

## 6. Strongest self-attack

The normal-quotient theorem removes only regular/homomorphic modes. A Schreier
graph `B_m/H` can have a severe barbell caused by nonnormal coset geometry
even when no nontrivial normal quotient exists. The paired state that kills
all group characters may itself lie in an exponentially small part of the
orbit and gives no conductance lower bound.

Claim D does not repair this: two large expanders joined by one edge have
small diameter but exponentially small conductance relative to their size.

Likewise, one-edge join-tree locality is compatible with slow mixing. The
exact audit makes the simple positive comparison harder: the join tree is not
uniform, and the tree, degree profile, Pruefer coordinate, and Dyck path are
not exact Markov lumpings. Conditional transition rates can therefore hide
additional braid-action bottlenecks inside a statistic fiber. This is the
strongest unresolved failure mode for `P_H`.

Finally, even a superpolynomially slow `P_H` would only refute this
sufficient route. The `r=4,5` heat baths in `K` can cross a Hurwitz
barrier. Literal TERMINAL B would require the full `K` boundary and
stationary mass on an explicit infinite family; this report has no such cut.

## 7. Calibration results

- **Odd `m`:** the identity transposition bridge is empty by sign; no claim
  is made.
- **`m=0`:** singleton, outside the displayed `P_H` definition.
- **`N=2`, even `m`:** the identity word orbit is a singleton; the normal
  quotient and gap proposition are vacuous/trivial.
- **`m=2,N>=3`:** excluded from the target `K` theorem. A connected
  Hurwitz orbit can only use two labels and is a singleton.
- **`S_3,m=4`:** reproduced 27 identity words and the 24-state full-support
  orbit; all 144 oriented-generator outcomes passed identity, inverse, fiber,
  height-locality, and tree-exchange checks.
- **`S_4,m=4`:** reproduced 120 identity words and zero all-label connected
  words, as required by `m<2(N-1)`. The target `K` still has its
  whole-word `r=4` heat bath; this report does not drop it.
- **`S_4,m=6`:** reproduced 3936 identity words and the 2880-state
  full-support orbit; all 28,800 oriented-generator outcomes passed.
- **Near-minimal words:** Claim C applies exactly at `m=2(N-1)`, including
  doubled-tree states. It does not route through a fixed doubled-tree hub.
- **Disjoint factors:** their Hurwitz move is a commutation. The exact local
  proof retains word ordering; it does not collapse to an unordered graph.
- **Parity statistics:** no multiplicity- or degree-parity characterization
  is used.
- **Known `L=2` simulation failure:** no local heat-bath simulation is
  asserted. `P_H` is only a one-way subchain comparison.
- **Asymptotic cuts:** the only infinite candidate family claimed rejected is
  the normal/cyclic quotient family, for which Claim B gives exact mass and
  full two-sided boundary flow. Tree/Dyck flows are explicitly finite only.

## 8. Artifacts and reproduction commands

Owned directory:

    experiments/20260811-polynomial-mixing-resolution/
      cycle-02/mission-M13-hurwitz-barbell/

Files:

- `plan.md`: target, convention, and failure modes.
- `checkpoint.md`: genuine first-half cyclic proof plus the paired-state
  sharpening.
- `diameter_audit.md`: explicit `50Nm^3` Classification-H move count.
- `exact_hurwitz_audit.py`: deterministic exact falsification harness.
- `results.json`: machine-readable exact output.
- `report.md`: this report.

Reproduce from the owned directory:

    python3 exact_hurwitz_audit.py --output results.json --seed 130113

Determinism check:

    python3 exact_hurwitz_audit.py --output /tmp/m13-hurwitz-results-final-rerun.json --seed 130113
    cmp results.json /tmp/m13-hurwitz-results-final-rerun.json

Final hashes of the computational artifacts:

    exact_hurwitz_audit.py
      9a6a41236fcb3e430e36b974077e69e625f8473655e3b4fa86369d91977a7935
    results.json
      7e7b8f58aae2dabbc6a3d13ebaa8eef0ab8f4404f7b5ab8fb0f92cb5c71473ea

## 9. Verdict

OPEN AT A NAMED STEP: Uniform connected Hurwitz-orbit gap.
