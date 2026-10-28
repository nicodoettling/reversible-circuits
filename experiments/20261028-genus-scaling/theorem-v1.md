# T0.v1 candidate theorem — uniform exponential genus dependence

Coordinator synthesis, 2026-10-28. **PROVISIONAL; exact-version and blind gates pending.** This statement preserves the original frozen T0. A complete proposed proof is the composition of the two full versioned proofs below; it is not accepted merely by this synthesis.

For every integer N>=2 and g>=0, let F(N,g) consist of all ordered words of m=2N-2+2g transpositions on exactly [N], whose rightmost-first product is identity and whose support graph is connected on [N]. There exist absolute constants A,C>1 and one uniform algorithm using independent fair bits that returns an exactly uniform element of F(N,g) in expected at most A C^(g+1)(N+g+2)^15 bit operations. Labels and the ordered word are explicit. This is degree-polynomial, not a claim about log2N wires.

The same algorithm accepts an explicitly specified endpoint sigma on a nonempty label set [N], with k individual cycles, and returns an exactly uniform connected word of length N+k-2+2g when the fiber is nonempty. The singleton empty genus0 word is the only singleton fiber. This stronger auxiliary statement is separately frozen as AUX-ENDPOINT-MARKER.v1; no endpoint conditioning oracle is assumed.

## Proposed proof and dependencies

1. **Uniform coefficient generation.** `coordinator/coefficient-theorem-v1.md` (COEFF-EXP.v1) provides the full deterministic construction. Published ELSV polynomiality and GJV Theorem3.2, with fixed-permutation normalization checked against the primary GJ source, identify the needed genus-h coefficients with coefficients of polynomials in at most3h-3 cycle lengths and total degree at most6h-6. Positive-simplex interpolation uses only degrees<=9h-9 and lengths<=14h-14. Ordinary cycle-type dynamic programming and exact anchored support-component extraction evaluate every required polynomial value in single-exponential h time. Exact Newton interpolation and a common factorial denominator give the rational list with polynomial h bit sizes. Summing h<=g absorbs polynomial factors into a larger absolute C. The source theorem is imported; all effectiveness and extraction arguments are on disk.

2. **Restricted allocation and literal decoding.** `roles/r1-recursion/proof-v1.md` proves AUX-ENDPOINT-MARKER.v1 under precisely that coefficient-list contract. Lagrange residue and polarization turn each rational term into a squarefree marker table. Two-child allocations use four integer coordinates bounded by N and at most3g+2 labeled special-slot bits, so the table dimension in N is constant. Arbitrarily forced cycle assignments retain their joint masses. Signed source expressions are summed to complete nonnegative integer branch counts before probabilities are formed. Final-letter deletion gives disjoint literal branches, with exact child sampling and interleaving. Its per-word cancellation proves uniformity.

3. **Complexity and probability.** The second proof bounds all signed intermediate numerators and denominators and derives A C^(g+1)(N+g+2)^15 bit time after the first proof's preprocessing. Fair-bit integer rejection has conditional expected trials<2 at each logical draw; the number of positive decoder nodes equals the output length. Expectation is summed over these bounded logical decisions, without multiplying marginal probabilities. This yields T0 by specializing sigma to identity.

The exact source/proof/code/result hashes are in `coordinator/coefficient-freeze-v1.json` and `roles/r1-recursion/manifest-v1.json`. The mathematical proof is independent of the Python interpreter's finite recursion/resource limits; reference code implements its finite checks and literal sampler. `coordinator/integrated_sampler_v1.py` explicitly removes built-in genus>=2 constants, generates the lists, and installs them into the decoder. It is a research reference, not an optimized implementation.

## Boundary and scope

N2 has the single feasible even identity word. Odd identity lengths have no words. At m0 only the singleton is connected; at m2 connected identity requiresN2. The auxiliary recursion retains empty singleton children and zero-count branches. Repeated cycle lengths remain individually labeled throughout allocation; equal special powers retain labeled slots and the coefficient's automorphism divisor exactly once.

Exactness gives TV0, hence meets every precision b with no added b work. For each fixed constant K, g<=K log(N+2) gives polynomial expected bit time in N, with exponent allowed to depend on K. This is not a global all-length sampler: its C^g factor can be large on high-genus components, and M-GROW's obstruction to low-genus/small-support eligibility policies remains valid. No local heat-bath mixing claim follows.

## Current evidence and first unclosed gates

J1: independent coefficient recovery g2/3,262 finite count comparisons. J4: conditional decoder132 count cases,1120 forced allocations,32 complete small laws over49184 words,128 branch totals. J5: integrated generated coefficients throughg4 (6,26,85 terms),223 count/branch checks,12 seeded validity samples. Full raw outputs and exact commands remain linked in job records. These checks cannot prove the all-input theorem or complexity.

First unclosed gates: full blind statement-only report, exact-version nonauthor coefficient/decoder/source/bit audit, fresh integration falsification, coordinator reconciliation and clean-state reproduction. All remain explicit. Same-model reviewers are correlated. No COMPLETION request is justified yet.
