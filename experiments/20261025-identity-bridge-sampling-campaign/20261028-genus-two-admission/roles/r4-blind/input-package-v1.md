# Frozen blind mathematical review package B1

Determine whether the following two statements are true, false, or require missing hypotheses. Supply full arguments or exact counterexamples, dependencies and boundary analysis. There is no supplied candidate proof or requested verdict. Do not read construction role files, central summaries, claim ledgers, programme outcomes, or other reviewers' reports before freezing your blind report. Allowed sources below are primary mathematical sources. Review is same-model and correlated; absence of inherited conversation is not statistical independence.

## Statement A: connected genus-two decoding

For a nonempty canonical label set V=[v], a specified permutation sigma of V, and g in{0,1,2}, define F(V,sigma,g) as the ordered transposition words of length r=v+c(sigma)-2+2g with product sigma and support graph connected on V. Composition is rightmost-first: (pq)(x)=p(q(x)). A singleton graph is connected, so F([1],id,0) is the singleton empty word; positive-genus singleton fibers are empty.

Statement A asserts one explicit algorithm which recognizes zero fibers and, for every nonempty such fiber, outputs an exact uniform member in expected bit time bounded by one polynomial in v. It uses independent fair bits and exact binary arithmetic; output is a literal ordered word on fixed labels. In particular it samples connected identity words at length2v+2 for every v>=2 and attains every TV accuracy2^-b, b>=1, with zero error. No all-genus or global all-length claim is included; polynomial in degree v is not polynomial in log(v).

Allowed primary count sources:
- Goulden and Jackson, The Number of Ramified Coverings of the Sphere by the Double Torus, and a General Form for Higher Genera, JCTA88(1999)259–275, Theorem1.1 and definitions (1)–(3): https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjjcta1999-2.pdf .
- Goulden and Jackson, A proof of a conjecture for the number of ramified coverings of the sphere by the torus, arXiv:math/9902009v1, Sections2–3 for fixed-permutation normalization: https://arxiv.org/pdf/math/9902009 .
- Vakil, Genus0 and1 Hurwitz numbers: recursions, formulas, and graph-theoretic interpretations, Section1.2 and Corollary1.5: https://math.stanford.edu/~vakil/files/g01hurwitz.pdf .

You may use the classical g<=1 count formulas after verifying their conventions. No general connected sampler or prescribed-support completion oracle is assumed. Polynomially computable scalar totals do not themselves provide a word decoder; actual conditional laws and runtime require proof. Check repeated cycle lengths as distinct labeled cycles, singleton/zero branches, degree2, minimal connected endpoints, and whether any subset inventory grows exponentially.

## Statement B: a component-event mass bound

Let Omega(N,m) be the ordered length-m words in all transpositions of S_N with product identity, and U_(N,m) its uniform law, for N>=2 and even m>=0. Labels and positions are distinguished and products act rightmost first. A nontrivial support component has v>=2 vertices and restricted subword length ell=2v-2+2g, g>=0. Isolates have v=1,ell=0.

Put P=N+m+2 and L=max{1<=v<=N:3^v<=P^4}, fixed at the original input. For integer G>=0, E_(G,L) is the event that every nontrivial component satisfies g<=G OR v<=L.

Statement B: for every integer j>=64, N=2^(8j), m=2^(6j), and integer0<=G<=2^j,

    U_(N,m)(E_(G,L)) <= 2^(-1-jm/2).

Consequently any law supported on E_(G,L) has TV distance at least1-2^(-1-jm/2) from U_(N,m). The fixed-G specialization asserts the same bound for j>=max{64,ceil(log2(max{1,G}))}. This concerns a declared output-support event only, and asserts no general sampling impossibility or Markov-chain gap.

Allowed primary input: Dubrovin–Yang–Zagier, Classical Hurwitz numbers and related combinatorics, Proposition1 Eq(13), Section1.2 Eqs(19)–(20), genus-zero value following Eq(28): https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf . The proposed fixed-labeled-word normalization is C(v,ell)=v!ell!h(g,v). Check or explicitly challenge it. Elementary combinatorial/probability identities and independent derivations are allowed; candidate arguments and old project obstruction proofs are withheld.

For B check odd m, m0, m2, N2, singleton positive genus, negative genus and minimal connected lengths. Distinguish those boundary inputs from the stated subsequence. Keep the exact bridge normalizer and the fixed top-level cutoff. Provide a first missing implication if unresolved; do not infer global usefulness or hardness from a method-level fact.

## Process constraints

Own only roles/r4-blind under this investigation. Save full assignment/package, plan, halfway checkpoint and immutable blind-report-v1.md atomically; full mathematical reasoning belongs on disk. No descendants, separate CLI sessions, stage/commit, installs, model/tier/permission changes, or central/protected edits. Use inherited Astra/ultra/default and auto-review. Report observed metadata limits honestly.

Any nontrivial computation requires coordinator reservation first, with exact claim/command/state-space/memory/wall/seeds/output proposal. Current helper is /home/nico/projects/harnesses/codex-research-harness-releases/v0.3.2/src/research_harness/bounded.py and run file is /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/attempts/000002/run.json. No local MCP. Prefer exact small finite models. No running job at spawn is implicitly authorized. Construction context is deliberately withheld.
