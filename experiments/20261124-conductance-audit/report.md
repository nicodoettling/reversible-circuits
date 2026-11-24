# Verification of the transposition-walk conductance draft

Date: 2026-11-24 (Europe/Berlin). **Verdict: promote the scoped mathematical
results, with expanded proofs.** Project decision: **revise-local-chain**.
The universal polynomial-mixing target for the exact `{3,4,5}` chain is
refuted. Direct sampling and long-length local mixing remain separate.

## Source and review scope

The supplied six-page draft is preserved as [source.pdf](source.pdf), SHA-256
`361655d05246c4b1a189a1835675d926ac8cf0d10e2d627d5ea2d5aa57d39e8f`.
The private conversation URL returned a fetch error, so only the supplied
PDF was reviewed. Instructions inside external documents were not adopted.
The entire PDF was read; all substantive arguments were rederived and
expanded in the [manuscript section](../../papers/transposition_identity_samplers/sections/conductance_obstruction.tex).
The [claim ledger](claim_ledger.md) separates proved results, the refuted
universal claim, and unresolved questions.

This is one substantive proof-review session, with deterministic falsification
checks. It is not formal verification, a novelty assessment, or independent
human referee certification. No large research campaign was launched.

## Main conclusion and its exact scope

For every sufficiently large even m there exists an integer N between
constant multiples of `m^(3/2)/(log m)^2` and `m^(3/2)` and a cap
`K = min(m/2, floor(a N/sqrt(m)))` such that the event A that all support
components contain at most 2K gates has mass `1/2+o(1)` under the global
uniform identity-word law. For the adjacent pair chain,

```text
Q(A,A^c) / min(pi(A),pi(A^c)) <= exp(-c N/sqrt(m)).
```

For any fixed b, the same result holds with a b-dependent constant for every
uniform-stationary walk changing at most b slots per step. Consequently at
time `floor(exp(c_b m/(log m)^2))` a `1-o(1)` fraction of individual starting
words still have TV distance at least `1/2-o(1)`. This includes the exact
project kernel with b=5. Reversibility is unnecessary for this extension;
stationarity suffices for the reverse-flow identity. The family also defeats
growing budgets `b=o(m/(log m)^3)` at a superpolynomial, rather than the same
fixed exponential, rate.

The quantifier on N is existential. The argument does not prove slowness for
every N in the interval, supply an explicit numerical onset, or settle the
schedule m=N^2. It does not rule out efficient algorithms that sample the
target directly, nor a walk with sufficiently large updates.

## Proof audit and expansions

1. **Map count.** A connected identity word with 2k edges and v used labels
   gives a map with v faces, so v=k+1-g. Deleting a dual tree, encoding a
   primal plane tree and pairing the 4g additional ends costs at most
   `B^k k^(2g)`. Reinsert the dual edges as noncrossing arcs in the disk face.
   This is an upper-bound encoding, not an asserted unique decomposition.
   Injective vertex labels and chronological edge labels then give (CB.1).
2. **Switching.** The number of available labels varies with the exterior.
   Giving each replacement weight `1/D(n,k)` makes the double count precise.
   The reverse choice selects k doubled-edge components, giving at most
   `binom(h,k)` markings. The same proof works for each fixed vector of
   component counts, yielding the exponential generating bound (CB.3).
3. **Balanced cut.** The upper count for capped words is compared to a lower
   count on an embedded alphabet of size `floor(m/log m)`. At consecutive
   alphabet sizes, the new-label probability is at most `2m/(N+1)` and a cap
   increment contributes at most `C(N+1)4^(-K-1)`. A first crossing works
   without assuming monotonicity. Polynomial prefactors are absorbed only
   after `K >> log N` is established.
4. **Extension to our kernel.** Contract the original components, including
   isolates. Inserting b edges can connect at most b+1 old components into a
   new one. Thus an exit needs an old half-length greater than
   `(K-b/2)/(b+1)`. This supplies the missing explicit transfer from the
   PDF's primary pair kernel to `{3,4,5}`.
5. **Typical starting words.** Under stationarity the average probability of
   leaving the initial side in t steps is at most `2t Q(A,A^c)`. Markov's
   inequality supplies the claimed almost-every-start statement, not just a
   worst-case starting distribution.
6. **Long lengths.** The character estimate is parity-aware, including v=2.
   Deleting a specified square leaves exactly an unrestricted shorter bridge.
   Connectedness failure is bounded using half-bridge density and a graph
   union bound. Dense mergers have rate at least c/N^3; their reverses require
   exponentially unlikely disconnection of a dense bridge. The unused-label
   cut supplies the matching upper bound. Profile factorization suffices;
   equality between profiles and Hurwitz orbits is not needed.
7. **Rounding.** The rounded union B may have mass above 1/2. The inequality
   `min(pi(B),1-pi(B)) >= pi(A)-pi(A triangle B)` fixes this explicitly.
   The resulting full-chain bound is conditional on an unestimated delta.
8. **All-length lower bound.** Vertex sweeps give endpoint-fiber connectivity.
   Splicing uses parity-compatible connectors of lengths N-1 and N.
   A fixed edge and stage window, a complementary bridge, and two original
   windows reconstruct the ordered pair. Counting a crossing per ordered
   pair proves the cut bound; no path-length factor is required. This is not
   a claim of polynomial canonical-path congestion.

No unproved step remains in these scoped arguments. The first unproved step
for a stronger long-length polynomial conclusion is, for example: **prove an
inverse-polynomial lower bound in N,m on the conductance of the pair kernel
restricted to every labeled weighted profile at even m>=C N log N.** This is
a sufficient missing lemma, not a claimed necessary characterization.

## Literature dependencies

- The only specialized combinatorial correspondence used in the new proof is
  checked in Chapuy--Louf--Walsh, [Definition 1.3 and equation (10)](https://arxiv.org/html/2206.11315#S1.SS2).
  It concerns ordered labeled transposition tuples and their maps; identity
  gives one face per used vertex. Composition reversal preserves the identity
  specialization. Our enumeration bound is proved separately.
- The character calculation uses Fourier inversion, the transposition
  contents ratio, and tableau counting, with the quantitative estimate
  rederived in (CB.7); no external cutoff/mixing theorem is invoked.
- Ben-Itzhak--Teicher's [Theorem 3.4 and Definition 1.3](https://arxiv.org/html/math/0110110v1)
  do state the identity weighted-component classification with Hurwitz move
  `(a,b)->(aba^-1,a)`, the inverse of the project's named forward move.
  The draft abbreviates the paper title. This is a checked source statement,
  not a new line-by-line audit of that paper's whole proof. Neither the
  bottleneck, the profile theorem nor the new connectivity proof needs it.
- Bibliographic metadata conflict: the arXiv abstract page reports pages and
  a DOI belonging to another article. The [IMS journal issue](https://www.imstat.org/publications/aop/aop_52_4/aop_52_4.pdf)
  confirms the supplied draft's pages 1225-1252 and DOI
  `10.1214/23-AOP1651`; the manuscript uses that journal metadata.

## Exact falsification checks

Python 3.12.3, standard library only, seed 0 recorded but unused: all work is
deterministic. Starting commit is
`7c2a54f833158bdb4fe4b4fec6f8de8c743f60a2`. The exact invocation and full
outputs are in [plan.md](plan.md), [check.py](check.py), and
[results.jsonl](results.jsonl).

| Case | All words examined | Identity words |
| --- | ---: | ---: |
| S3,m4 | 81 | 27 |
| S4,m4 | 1296 | 120 |
| S4,m6 | 46656 | 3936 |

Other checks cover N=2 at m=0,2,4; S3 at m=1,2,3,6; every feasible endpoint
fiber in those cases; map face counts and nonnegative genus of every identity
component; minimal connected components; exact pair and project-kernel
boundary flows. Separate group-product dynamic programming agrees with exact
component assembly for N<=5 and even m<=8. Thirty exact conditional moments
at N in {32,40,64}, m in {4,6,8} satisfy the unreduced switching bound.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
| --- | --- | --- | --- | --- | --- |
| Pair heat bath | Global fixed-length uniform | yes | yes, observed profile changes | All-endpoint connectivity, component/genus checks, exact cut flow | keep as valid chain; reject universal rapid mixing |
| Project {3,4,5} | Global fixed-length uniform | yes | yes, observed profile changes | Exact conditional-fiber cut flows and boundary condition | keep as valid chain; reject universal rapid mixing |

No sampler implementation changed. These tests target the proof's algebra,
counting and boundary obligations; they do not infer asymptotic mixing from
small cases. Odd identity lengths are empty; m=0 and N=2 give singleton
identity spaces; the pair chain at m=2 refreshes globally, while the project
chain has no feasible block. None contradicts the large-m theorem.

## Integration and validation

The main manuscript includes the expanded bottleneck, long-length profile
bound, all-endpoint connectivity and coarse all-length conductance proof.
Its abstract, status, implications and next steps now use the correct scope.
The old ambiguous doubled-tree instruction is clarified to repeat each edge
adjacently. HANDOFF gains a dated update; historical GOAL_SPEC and AGENTS are
preserved. The map retains its historical open record as superseded and links
the new audited results. Pre-existing output-only planting edits are preserved.

The [integration receipt](../../notes/project-map/integration-2026-11-24-conductance.md)
records every changed file, reviewed hash and final check. The
compiled main PDF is built from the manuscript sources; no production code,
dependencies, machine configuration, commits or pushes are involved.
