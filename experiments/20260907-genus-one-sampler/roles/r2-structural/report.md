# R2 structural route: complete exact sampler candidate C1

Worker-final, 2026-09-07 21:28 UTC. Verdict: **promote for fresh audit**. The mathematical construction and implementation are complete; coordinator certification is **PROVISIONAL** until nonauthor review. No open mathematical construction step is being hidden behind a counting oracle.

The frozen target T0 is uniform on X_N, the ordered length-2N transposition words in S_N whose product is id and whose support is connected on all N labeled vertices. Products satisfy (pq)(x)=p(q(x)). For every N>=2, candidate C1 produces an exact target word and, under independent fair random bits, has exact uniform law in expected polynomial bit time in N. It therefore meets every requested b>=1 with TV error zero. It is polynomial in the permutation degree, not in log_2 N wires. N=2 is the repeated-edge singleton; X_1 at length two is empty. No Markov kernel or mixing result is asserted.

## Construction and proved probability law

The complete proof is [proof.md](proof.md), version C1; the implementation is [cut_sampler.py](cut_sampler.py).

1. **Arbitrary-endpoint genus-zero factors.** For a fixed permutation p on v labels with cycle sizes a_i and k cycles, the classical count is F0(p)=(v+k-2)! v^(k-3) product_i a_i^(a_i+1)/a_i!. Deleting the final transposition either merges two endpoint cycles and leaves a connected genus-zero prefix, or splits one endpoint cycle and leaves exactly two genus-zero support components. In the latter case the other distinguished cycles are assigned between the daughter components. Once total assigned size and cycle count are fixed, their weight is constant: a knapsack DP samples the assignment, recursive factorization samplers supply the two words, and uniform interleaving reconstructs the prefix. Every word's final transposition and support components recover its branch, proving exact per-word uniformity.
2. **Everywhere-defined M97 cut.** Each genus-one identity word has a nonempty interval J(w) of cuts whose two sides are componentwise genus zero. Its cycle-incidence multigraph is bipartite, connected, and unicyclic. The elementary genus proof was rederived; neither Hurwitz transitivity nor any gap bound is imported.
3. **Positive weighted incidence grammar.** An edge carries a cycle of size a>=1; a vertex has support size S equal to the sum of incident cycle sizes and degree d. With j=N+#R-#L, the cut weight after summing cycle labels and both side interleavings is N! j!(2N-j)! product_v S_v^(d_v-3) product_e a_e^(2a_e+1)/(a_e!)^2. An alternating core of length 2s with hanging ordered trees represents each labeled incidence graph exactly 2s product_v k_v! times. The reciprocal factors 1/(2s) and 1/k_v! cancel these multiplicities, including the two-parallel-edge core.
4. **Exact DP and decoding.** The positive grammar tracks total edge-size mass, color imbalance, number of children, and sum of immediate incident edge sizes. Planted-tree coefficients feed core-vertex transfer matrices; trace((M_L M_R)^s)/(2s) enumerates the core. Truncation at mass N is complete because every edge has positive size. Polynomially many exact coefficients support backward weighted parsing. A uniform label permutation supplies endpoint cycles; the genus-zero sampler supplies both sides and uniform interleavings.
5. **Correct forgetting.** The proposal is exactly uniform on cut incidences A_N={(w,j):j in J(w)}. Accept with probability 1/|J(w)| and forget j. Each word has exactly 1/|A_N| accepted mass before normalization, so the output is uniform on X_N. Acceptance is |X_N|/|A_N|>=1/(2N-1); fresh independent proposals give expected at most 2N-1 attempts.

The only load-bearing literature input is the displayed genus-zero count. Its fixed-permutation normalization was checked directly in Vakil, Section 1.2 and Corollary 1.5: c^g_alpha counts the fixed-permutation transitive factorizations and equals G^g_alpha product alpha_i. [Primary source](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf). This count is used inside an explicit decomposition, never treated as an arbitrary prefix-completion oracle. DPS's identity sampler and its genus-one mobile bijection are not dependencies of C1.

## Runtime and random bits

The conservative proof bound is O(N^9 log(N+1)) rational operations on O(N^2 log(N+1))-bit operands, and for example O(N^15 log^4(N+1)) expected bit operations with elementary arithmetic. This exponent is loose. A common denominator ((3N)!)^(12N+4) covers all partial-object monomials, including open core paths and planted parent ports, so positive coefficient sums retain polynomial bit length. Positive edge size bounds all grammar depths and makes the N-round truncated planted-tree iteration exact. Every genus-zero recursion appends one output factor; all execution stacks are explicit in the implementation.

Categorical rational weights are converted to polynomial-bit integer weights. Exact uniform integer draws use unbiased-bit rejection, taking fewer than two attempts in expectation. The implementation accepts an RNG; the convenience function sample_connected_genus_one(N) uses SystemRandom. Seeded random.Random streams in the tests check reproducibility and validity only. No PRNG output is used as a proof of uniformity.

## Exact finite and regression results

The final implementation passed the full exact rerun recorded in [results.json](results.json), using [audit.py](audit.py). The audit imports the new sampler for comparison but independently enumerates all literal words and all ordered numeric code structures. It is author-run finite verification, not a nonauthor or statistically independent audit.

| N | target words | cut incidences | distinct labeled macros | numeric codes | exact acceptance |
|---|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 240 | 336 | 9 | 4 | 5/7 |
| 4 | 131040 | 234720 | 101 | 15 | 91/163 |

Every labeled macro multiplicity from explicit code generation equals direct word enumeration. Thus this tests the full endpoint/support-partition disintegration, not a marginal histogram. Separately, every final-factor/support-component branch of every genus-zero factorization was checked on all endpoints in S_2,S_3,S_4: respectively 2,54,6792 complete words across 2,6,24 endpoint permutations, with 2,21,192 terminal branches. All counts and branches match exactly.

The required global boundaries reproduce 27 identity words for S_3,m=4; 120 for S_4,m=4; 3936 for S_4,m=6. The m=0, odd m, m=2, N=1 and N=2 cases were also checked. In the target sectors N=3 and N=4, there are respectively 24 and 41472 words with no connected-deletable adjacent square. The alternating (a b)^3 example and doubled-tree extensions through N=12 retain zero square-insertion fibers and have the valid M97 cut j=3. This regression is preserved, not repaired by claiming literal square coverage.

Each of seeds 1729 and 2718 produced 30 accepted samples for each N=2,3,4, all of the exact required length, product, and support. Those smoke tests are not evidence for asymptotic uniformity or runtime. The deterministic multiplicity tests and the proof carry those claims.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| C1 genus-one cut grammar + reciprocal-cut rejection | exact uniform X_N | proved; every tested output passes | not a walk; covers all target words by the cut theorem | full labeled macro multiplicities and all genus-zero terminal branches through N=4 | promote for fresh audit |
| literal adjacent-square insertion | exact uniform X_N | identity valid but incomplete support in word space | not a coverage repair | 24/41472 zero fibers at N=3/4; explicit family every N>=3 | reject |

## Claim ledger and dependency closure

| claim/version | mathematical status | assumptions | evidence | nonauthor check | action |
|---|---|---|---|---|---|
| C1.1 F0 fixed-permutation count | proved from literature | Vakil normalization | proof.md C1.1; primary Cor.1.5 | pending this run | retain explicit source |
| C1.2 exact arbitrary-endpoint genus-zero sampler | proved by worker | C1.1 | final-deletion classification, size/count knapsack, all small full branches | pending | promote for audit |
| C1.3 everywhere-defined cuts | proved by worker rederivation | elementary genus monotonicity | proof.md C1.3; M97 Sec.3--4 | pending this run | retain old zero-square regression |
| C1.4 local macro weight | proved by worker | C1.1, C1.3 | factorial/cycle normalization; every finite macro | pending | promote for audit |
| C1.5 coding multiplicity and 1/|J| rejection | proved by worker | C1.3--C1.4 | root/direction and child orders; exact accepted mass | pending | promote for audit |
| C1.6 polynomial grammar, parsing and bits | proved by worker | C1.4--C1.5; ideal fair bits | explicit positive DP and denominator bound | pending | promote for audit |
| C1.T exact expected-polynomial T0 sampler | PROVISIONAL complete candidate | C1.1--C1.6 | proof.md; cut_sampler.py; results.json | pending | coordinator must reconcile before acceptance |

The first unproved mathematical step within C1 is **none claimed**: the full argument is supplied. The outstanding certification gate is fresh nonauthor review of the current proof, particularly the 2s product k! quotient, backward parsing law, and denominator/operation bounds. A disagreement there must reopen the dependent claims. Correlated same-model review will be reported as repeated review, not independent statistical evidence.

## Reproduction, provenance, and scope

Repository commit: 20e86f665f69053031fe7eec0c3388458affb1fc. Python 3.12.3, standard library only. The initial and recorded dirty state contains the new run directory and the preexisting run-note inputs/live log outputs; no unrelated path was edited. Exact tests use seed null; smoke seeds are 1729 and 2718. The authoritative rerun command from the repository root is:

```text
timeout 180s python3 -B experiments/20260907-genus-one-sampler/roles/r2-structural/audit.py --max-n 4 --samples 30 --output experiments/20260907-genus-one-sampler/roles/r2-structural/results.json
```

The command was supervised, completed in roughly five seconds, and required no package, configuration, or permission change. The final payload is frozen by SHA256SUMS and freeze_manifest.json. Only this role directory was edited. Owned files are assignment.md, plan.md, checkpoint.md, proof.md, cut_sampler.py, audit.py, results.json, report.md, freeze_manifest.json, and SHA256SUMS. No manuscript or project-level claim was changed. Broader enumeration was stopped once the decisive exact checks passed, at coordinator request.

Awaiting coordinator's audit assignment after this report.
