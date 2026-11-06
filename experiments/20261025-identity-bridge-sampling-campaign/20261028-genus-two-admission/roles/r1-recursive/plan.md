# R1 plan v1 — frozen before derivation

Target law: uniform connected ordered transposition words on canonical labels [v], fixed endpoint sigma, rightmost-first composition, length r=v+c(sigma)-2+2g, 0<=g<=2. Singleton g=0 is the empty word; singleton positive genus has zero mass. The identity g=2 target is length2v+2. Fair-bit exact arithmetic; degree v is the complexity variable.

1. Read S1.v2 count normalization, final-letter decomposition, allocation DP and exact-version audits. Preserve all old failures named in I1 brief.
2. Freeze and derive L11: a nonnegative tensor-moment DP computing every partially forced (gA,gB)=(1,1) cycle-allocation mass in polynomial time. It is a new auxiliary claim, not a complete genus-two sampler.
3. Freeze and investigate L2: fixed-genus generating/count formulas admit polynomial partial-assignment aggregation for (2,0)/(0,2), including exact fixed-permutation normalization and singleton zeros. Primary-source lookup is limited to this obligation.
4. If L2 closes, specify recursive sampler and exact per-word/fair-bit law, then request a bounded exact rational regression job. If not, preserve L11 and isolate first unproved oracle.
5. Freeze report/proof/code by13:00 UTC for independent coordinator review. All claims provisional before review; no global sampler conclusion.

No computational experiment runs without coordinator reservation. Proposed first check: literal S3 length8 endpoint/support counts plus allocation sums on small labeled cycle lists, exact arithmetic, deterministic seed null; final parameters depend on formula obtained. State estimate <=6561 words for S3 and polynomial moment tables. Detailed output belongs in owned unique JSON files.

Frozen auxiliary lemma L11.v1: for any list of K>=2 individually labeled positive cycle lengths summing to v, with two cycles forced to opposite sides and arbitrary further A/B forcing, the sum over remaining assignments of binom(L,rA) C1(alphaA) C1(alphaB), L=v+K, rA=s+h, is computable by a nonnegative polynomial-size integer-moment DP and exact rational postprocessing in poly(v) bit time. Completed branch totals are nonnegative integers. The corresponding sequential forced-choice oracle samples assignments exactly by their weights.

Candidate lemma L2.v1, currently unresolved: a polynomial bit algorithm evaluates C2(alpha) and every partial-assignment sum for C2(alphaA) C0(alphaB) after factorial cancellation, for all cycle lists of total size v, with distinct labeled cycles and arbitrary forcing. Exact signed formulas may compute masses but must prove their final nonnegativity via genuine count identities; they are not individual probability weights.
