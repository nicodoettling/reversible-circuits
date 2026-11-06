# Uniform genus dependence: internally reviewed result

**The campaign produced a source-scoped internally accepted proof of the requested single-exponential genus bound.** It gives one exact fair-bit sampler for connected identity words, with expected bit cost

\[
A C^{g+1}(N+g+2)^{15},
\]

for absolute constants A and C>1, every N>=2 and every integer g>=0. The completion packet requests operator review; it does not declare external certification or operator acceptance. The [full reconciliation](reconciliation-v1.md), [claim ledger](claim_ledger.md), complete proofs and frozen referee reports carry the evidence.

The distribution is uniform on ordered transposition words on exactly [N], with rightmost-first product identity, connected support on every label, and length 2N-2+2g. The auxiliary theorem treats an explicitly specified endpoint with k cycles and length N+k-2+2g. It includes the empty singleton genus-zero base and rejects empty fibers. It does not obtain endpoint samples by conditioning an unavailable sampler.

## What is new beyond the reviewed genus-two work

The inherited I1 work supplied connected arbitrary-endpoint sampling through genus two and a separate marked-cut identity construction. This run supplies a uniform way to generate the higher-genus coefficients and a table whose exponent in N stays fixed as genus grows. Genus three is a diagnostic of that construction, not its justification.

The published ELSV and GJV formulas identify the needed genus-h coefficients with coefficients of a polynomial in at most 3h-3 cycle lengths. Its degree is at most 6h-6. Evaluating it on a positive integer simplex needs only permutation degrees at most 9h-9. Fixed-endpoint quotient counts and exact support-component subtraction compute those values. Finite differences recover the full coefficient list in C^h bit time; the proof pays for signed arithmetic and denominator sizes. Thus published existence of the coefficients is made effective without assuming an oracle or per-genus advice. See the [complete coefficient proof](coordinator/coefficient-theorem-v1.md).

The [complete decoding proof](roles/r1-recursion/proof-v1.md) uses a table with four integer coordinates and at most 3g+2 special-marker bits to compute exact partially forced cycle allocations. Equal cycles remain distinct; repeated special slots retain their multiplicities. Signed terms are added to the full positive integer mass before any random choice. Deleting the final letter gives a unique decomposition into smaller connected endpoint words and a shuffle. The resulting probabilities cancel exactly to the uniform word law.

With n=N+g+2, the proof bounds arithmetic work by C^g n^10 and intermediate bit lengths by C^g plus O(n log n). Elementary exact arithmetic gives the conservative n^15 bound. These are absolute exponents; N^O(g) is not being called fixed-parameter tractable. The potentially large exponential constant is not optimized. This is a mathematical complexity result and a checked research reference implementation, not a practical large-genus benchmark.

The bound is in expectation, because exact uniform integers use fair-bit rejection. Conditional expected retries are below two at every history. No finite worst-case random-bit bound is claimed. The output law has total variation distance zero, so it also meets the separately frozen accuracy target TV<=2^(-b) without accuracy-dependent sampling work. For every fixed K, genus g<=K log(N+2) gives polynomial expected time in N; that polynomial's exponent may depend on K.

## What survived, and what remains open

| Construction or target | Reconciled status | Reason and scope |
|---|---|---|
| Uniform coefficient recovery | Proved; internally ACCEPTED | Complete simplex extraction and bit argument, checked against primary formulas |
| Arbitrary-endpoint allocation and literal decoder | Proved; internally ACCEPTED | Joint forced masses, unique reconstruction, exact fair bits and uniform cost |
| T0 connected identity sampler | Proved; internally ACCEPTED | Exact composition, no internal algorithmic lemma left open under checked published inputs |
| Penultimate-genus marked cuts | Proved structural identities; conditional rejection implication | Tree/unicycle topology, full incidence factors and at most 2N-2 proposals |
| Separate efficient structural grammar | Unresolved | PORT-CONTRACT remains an explicit allocation obligation; the main sampler does not use it |
| Vertex-only parallel-core encoding | Refuted | N2 has two actual-edge directions; collapsing them and dividing by two undercounts |
| Generic balanced-core port enumeration | Insufficient as an FPT proof | The displayed implementation can require N^O(g) assignments |
| Global all-length sampler, heat-bath mixing, wire-polynomial efficiency | Unresolved | No such consequence follows from a C^g prescribed-component sampler |

The prior M-GROW obstruction remains valid: low-genus/small-support eligibility policies fail on its stated m=N^(3/4) subsequence, even with the stated genus growth through N^(1/8). Exponential genus cost does not make that global obstruction disappear. The uncommitted old I2 sparse candidates were neither imported nor promoted. Historical heat-bath and classification disagreements in central documents were recorded, and no protected project source was rewritten.

## Evidence and review limits

The [fresh blind report](roles/r3-adversarial/blind-report-v1.md) froze before author proofs were disclosed. It reconstructed the target through a different coefficient algorithm, with loose exponent 40. The main exponent 15 and actual implementation then received [R2's full nonauthor review](roles/r2-structure/review-t0-v1/report-v1.md) and [R3's explicitly nonblind review](roles/r3-adversarial/review-t0-v1/report-v1.md). The [R1 coefficient review](roles/r1-recursion/review-coefficient-v1/report-v1.md) added a separate exact coefficient audit. Same-model lineage, shared sources and author discussion are disclosed. No vote count substitutes for the full proofs. The imported geometric enumeration theorems are source-checked dependencies, not reproved here.

| Job | Decisive finite evidence | Outcome |
|---|---|---|
| J0 | Current-helper inert actual-sandbox smoke | Passed |
| J1 | Generated genus-two/three coefficients; 262 count comparisons | Passed |
| J2 | 12 N2/N3/N4, genus-zero through three structural cases and cut laws | Passed |
| J3 | Blind reference: 396 count comparisons, 90 forcing cases, genus-two numerator reconstruction | Passed |
| J4 | 132 counts, 128 branch sums, 1,120 forcing cases, 32 reconstructed laws covering 49,184 words; 180 seeded validity samples | Passed |
| J5 | Generated coefficients through genus four: 6/26/85 terms; 223 count/branch checks and 12 validity samples | Passed |
| J6 | 656 independent literal counts and 18 polynomial extrapolation checks | Passed |
| J7 | 5,670 joint suffix cylinders across 30 genus-four endpoints; 27 forced allocations | Passed |
| J8 | Actual production execution laws: 9 full laws over 52,180 outputs; 225 new forced allocations | Passed |
| J9 | Fresh interpreter, 26 frozen payloads, regenerated coefficients and all 19,680 N3 identity genus-three outputs exactly uniform | Passed |

All jobs ran sequentially with the sealed attempt and current v0.4.2 bounded helper; mathematical jobs had a 1 GiB address-space ceiling and 180-second timeout. Python 3.12.3 and the standard library sufficed. Exact argv, execution commits, seeds and raw output paths are in [execution-record-v2.json](coordinator/execution-record-v2.json) and the job plans/receipts. Actual RSS was not measured. No full N4 genus-three word enumeration was performed. Finite success does not prove an asymptotic theorem; its role is falsification and implementation binding.

The [regression registry](failed-approaches.md) retains ordinary 81 versus connected 80 fibers, support-graph bias, the (ab)^3 insertion obstruction, child/parallel multiplicities, adaptive marginal-product failure and M-GROW. Boundary analysis covers singleton genus zero, positive-genus singleton emptiness, N2, odd identity lengths, m0/m2 and zero-count branches. No rejected approach was erased.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| Generated-coefficient marker decoder | Uniform connected identity F(N,g); auxiliary fixed endpoints separately stated | Universal reconstruction proof; actual J8/J9 laws passed | Direct sampler covering the full declared connected fiber; no within-orbit walk premise | J1–J9 counts, arbitrary forcing, joint cylinders and actual literal laws | Promote for source-scoped internal use; operator/external completion review pending |

## Delivery and next investigation

The full algorithmic proofs, claim dependencies, referee inputs/reports, raw results and source hashes are durable. The final Git inventory lists every changed path. Author reports remain immutable even when their original banners say PROVISIONAL; [reconciliation-v1.md](reconciliation-v1.md) gives their later effective status. Central maps/manuscript remain unchanged; [proposed-map-delta-v1.md](proposed-map-delta-v1.md) is a proposal only.

The highest-value next investigation is an external mathematical audit of the uniform coefficient-to-decoder composition. Its first test should independently rederive the repeated-cycle/source normalization and the complete forced-allocation identity at a two-positive-genus split, then inspect the all-genus bit-denominator proof. That directly targets the shared-source and same-model risks left by this internal review. It is a proposed next step, not an authorized successor run. No further mathematical experiment or worker is active, and no automatic continuation is authorized.
