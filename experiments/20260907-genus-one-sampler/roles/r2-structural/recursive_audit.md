# Nonauthor audit of R1-T1.1 and the global integration

Final, 2026-09-07 21:42 UTC. **ACCEPT R1-T1.1, R1-C1--C6, and the reviewed global claims G1-COUNT, G1-SAMPLE, G1-SAT, G1-OMIT. Material numbered objections: zero.** This is a nonauthor same-model review, not external human certification or statistically independent evidence. I did not read the blind referee's audit. Coordinator reconciliation still owns project-level acceptance.

The assigned review input is preserved verbatim in recursive_review_input.md. My independent cut construction C1 was already frozen; no payload named by its SHA256SUMS was modified during this review. Its checkpoint is the only mutable old file.

## Frozen scope and provenance

R1 proves exact uniform sampling of connected ordered transposition factorizations of any specified permutation sigma on a nonempty v-set, at length r=v+c(sigma)-2+2g with g in {0,1}, whenever the fiber is nonempty. The product convention is rightmost first. The genus-zero singleton is the empty word; genus-one singleton is empty. In particular, the genus-one identity endpoint gives the requested X_N at length 2N for every N>=2, with TV zero and expected bit complexity polynomial in N. N means permutation degree, not logarithmic wire count.

All five assigned hashes matched before review:

| R1 artifact | SHA-256 |
|---|---|
| proof.md | c779902224eaab4ebe2837fbb0d4aaaf9850aa4aede5443cd86259a746f6b9ba |
| sampler.py | d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d |
| audit.py | eb2aeffb1e4c4c2efd95245e407257461c8e2f79cb4e541646f6a72d10899930 |
| results.json | 930c2b945168216bbd81b5eaef213140f4b2fc60f470eedd71a1eff336785722 |
| report.md | 8e49c40ea29b2275cc8d4d3937bd8963a5f3c05e5438cbd3c7f79ddabf1d6bbb |

The additionally reviewed coordinator snapshots are sample.py (bf4e11bdde4ad918225cc050aaf4ab070ded63bbdec9e0be4c5938d477b23a8f), global_consequence.md (76c310c1495e29766a3f0daa35bcdb36aa24c2342ceb746f62da2a41ac39bcc6), and global_mass.py (ef0b588811798c861a8af3609ee0215e3a20c7e4a5fcc1c0656cb2c539bd0d80). This verdict is specific to those contents.

## R1-C1: fixed-endpoint normalization and positive formula

I checked Vakil's primary PDF, Section 1.2 and Corollary 1.5. Its c^g_alpha counts transitive ordered factorizations of a fixed permutation, and c^g_alpha=G^g_alpha product_i a_i. Multiplication yields precisely R1's q(a)=a^a/(a-1)! factors. No sheet, branch-order, repeated-cycle, conjugacy-class, or rotational quotient remains. Transitive edge generators are equivalent to connected support. Reversal/inversion gives a bijection between opposite displayed product conventions. [Primary source](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf).

The positive genus-one expansion is also correct by a direct algebraic audit. Let e_j be the elementary symmetric polynomial. Counting pairs consisting of a j-subset and a marked cycle outside it gives S_j=v e_j-(j+1)e_{j+1}; also Q=v^2-v-2e_2. Substituting these identities into the positive formula, the coefficient of e_2 is -v^(k-2). For j>=3 it is [(j-1)!-j(j-2)!]v^(k-j)=-(j-2)!v^(k-j). These are exactly the subtractive Corollary 1.5 coefficients. The unpaired final term vanishes because e_(k+1)=0. This proves the expansion, not just its agreement at a few profiles.

Every term actually used for sampling is nonnegative. Genus-one singleton profiles give Q=0 and no S_j terms, so their zero mass is detected exactly.

## R1-C2--C3: final-letter classification and multiplicity

Deleting a single final edge from a connected support graph leaves at most two components. For a final edge joining different sigma-cycles, the merged predecessor cycle contains both endpoints. It therefore forces them into the same predecessor support component; a second component could not be connected by that final edge. The predecessor stays connected with the same genus.

When the final edge cuts one sigma-cycle, the connected predecessor has genus g-1. A disconnected predecessor has two components, each containing one distinguished daughter cycle; the genera sum to g. Every remaining individual cycle must belong wholly to one component. The elementary genus lower bound excludes negative genera and the zero singleton convention handles leaves.

Conversely each listed branch reconstructs a valid connected parent. The ordered endpoint pair x<y orients A and B, eliminating any factor 1/2. A literal output word recovers its final edge, predecessor support blocks, genera, child subsequences, and positions uniquely. Repeated cycle lengths create distinct assignments when their actual label sets differ. Thus the branch count binom(r-1,r_A) C_A C_B is exact, disjoint, and exhaustive.

## R1-C4: every partially forced law is exact

The moment updates hold assignment by assignment. Including a new cycle a multiplies a marked old subset's product by a and increases its marked sum by a, producing a S_(j-1)+a^2 E_(j-1). Unmarked old subsets supply the unchanged S_j. The elementary-symmetric recurrence and Q increment a(a-1)M are likewise exact. Coalescing states with the same accumulated size and cycle count adds vectors of the same length, as the code assumes.

Forced cycles simply retain one transition instead of two. This preserves every moment identity for arbitrary forced sets, including non-prefix choices and zero-mass assignments. When genus one lies on B, tracked_side=1 correctly swaps the tracked component; the opposite component's size and cycle count are determined by the total. The common cycle q-product and factorial L! are independent of the allocation, so the aggregated formula equals the sum of actual nonnegative integer branch counts.

During sampling, let H_i be the exposed assignment prefix. The two weights are the exact masses of H_i extended by A and B, their sum is the exact current mass, and the chosen conditional probability is their ratio. Telescoping yields the normalized final allocation weight. No marginal-independence claim is needed; a zero extension has conditional probability zero. The original cached-prefix product claim remains false: posterior A masses 21/2000, C masses 1/20, and D mass 879/1000 give selected joint mass 21/2000>1/100, although the later incidence 21/221 is below 1/10. The independent harness reproduces this regression. R1 survives because its denominators are recomputed for the actual surviving assignments.

## R1-C5--C6: implementation, full law, and resources

The production continuation stack implements the proof exactly. Connected branches place an append continuation below the child request. Split branches place the merge continuation below B and A requests, so A finishes first, then B, and the merge pops them in the correct reverse stack order. Restrictions use sorted label sets; the merge restores original labels before interleaving. Exact subset unranking preserves each child's internal order. There is no interpreter recursion-depth dependence.

Every positive call removes exactly one output transposition, and a split conserves total remaining child length. Thus there are exactly r positive-length calls and at most v singleton leaves. Degree never grows, and r<=2N. The O(N^4) allocation oracle, O(N^2) final-edge scan, and at most O(N) extra forced-oracle calls per selected assignment give O(N^6) arithmetic work per positive node and O(N^7) overall. Fixed-capacity caches cannot create an exponential retained inventory.

I checked the claimed denominator carefully. The product of (a_i-1)! divides N! because its arguments sum to at most N. Negative powers are at worst -2 for a genus-zero component and -1 for genus one; both component sizes lie in [1,N]. Hence 24(N!)^5 is a valid common denominator for the allocation expressions. Integer moment entries, factorials, powers, all positive sums, and final branch counts have O(N log(N+1)) bits. Reducing rational intermediates retains this bound. Charging O(B^3) for B-bit exact rational operations gives the stated conservative O(N^10 log^3(N+1)) bit bound.

The fair-bit integer primitive draws enough bits for [0,Z) and rejects the excess; its conditional expected number of trials is below two, with Z=1 deterministic. Only polynomially many logical draws occur, so linearity of expectation gives polynomial expected random-bit work without a product-of-marginals argument. Exact branch selection, allocation, child sampling, and interleaving probabilities cancel to 1/C_parent for each literal word. Endpoint, length, and connectivity hold on every output. The theorem has no accuracy dependence because the error is zero.

## New independent tests

The new test is recursive_independent_check.py, with machine-readable output recursive_independent_results.json. It is not a rerun of the author's harness. Production code is loaded solely as the implementation under test; references use literal subsets, a separately written subtractive count formula, direct word enumeration, and direct support sets.

The first test checks every raw E/S/Q entry, not only the final scalar mass. Across four inventories, including asymmetric total sizes 16 and 19 beyond the author's size cutoff, it exhausts all partially forced assignments: 4,920 table/mass queries, 97,232 exact moment-entry comparisons, and four zero-mass branches. Both tracked sides and all genus allocations (0,0),(1,0),(0,1) pass.

The second test exhausts complete forward executions of the actual production stack. An exact categorical-choice oracle enumerates the finite logical decision tree and supplies each primitive's mathematically exact probability; it does not enumerate infinite rejected-bit tapes. Every output is compared with independently enumerated literal words. All 14 cases pass with one logical tape per word and uniform mass:

- all six endpoints of S_3, each at genus zero and genus one;
- endpoint (01)(23) in S_4 at genus one: 3,840 words, each probability 1/3840;
- endpoint (0123) in S_4 at genus one: 640 words, each probability 1/640.

Together these are 5,068 complete words. This specifically tests the new explicit stack and arbitrary endpoints instead of re-evaluating an inverse reconstruction formula on the author's identity-only output list.

## Coordinator integration and global consequences

The sample.py component loop implements the exact least-label recursion. Its label and position subsets use the appropriate remaining-coordinate indices. The selected-label list remains increasing; positions are filled in increasing order with a correctly relabeled child word. The remaining label/position filters remove exactly those choices. An isolate invokes genus-zero singleton sampling; zero component weights are excluded. Positive branches guarantee the residual restricted partition function is positive and the loop ends with no positions left.

For every literal allowed word, the selector weight, label subset probability, position subset probability, internal word probability, and remaining assembly probability cancel to 1/Z_01. Thus **G1-SAMPLE is accepted**, including the exact global TV certificate 1-Z_01/Z. The approximate-component extension also uses valid history-conditional couplings and a union bound over at most N components.

I separately checked the DYZ fixed-identity normalization and positive recurrence against Proposition 1 equation (13) and Section 1.2 equations (19)--(20). The latter identifies the d! quotient for ordered monodromy tuples, while h divides by the branch factorial. Multiplication gives C(d,k)=d!k!h and precisely the displayed binomial/multinomial recurrence. The imported counting implementation uses two binomial convolutions and the stated positive least-label assembly. **G1-COUNT is accepted.** [Primary source](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf).

For **G1-SAT**, the equality chain 2N=2s-2k+2G<=2s<=2N forces s=N and G=k. Every nontrivial component has genus at most one, so each has genus exactly one. Conversely a partition into such components has total length 2N. Isolates are excluded by s=N. The displayed saturated recurrence follows from distinguishing the component containing the least label and choosing its 2v positions. It is accepted.

I also audited **G1-OMIT**. The upper bound a_v<=v^v/24<=3^v v! follows from the nonnegative subtracted terms and v!>=(v/e)^v. Ordering blocks gives the correct factor 1/k!, and summing positive ordered compositions bounds the restricted normalized count by 6^N N!. The embedded S_r return bound uses inversion symmetry and Cauchy--Schwarz on one parity class, giving 2 binom(r,2)^(2N)/r!. For r=floor(N/log N), the numerator's logarithm is at most 3Nlog N+O(N), while the denominator contributes 4Nlog N-4Nloglog N+O(N). The claimed ratio tends to zero and the restricted law's global TV tends to one. This is a valid named-method obstruction, not hardness or an obstruction to richer samplers.

New complete forward integration tests give all 27,120,340 words uniformly at (N,m)=(3,4),(4,4),(5,4), respectively. Direct finite reference certificates additionally give 80/81 at (3,6), 655/656 at (4,6), and 4375/4672 at (4,8). At (4,8), the allowed count is 131250: 131040 connected genus-one words plus 3*binom(8,4)=210 words on two size-two genus-one components. Boundary tests include N=0,m=0; N=1,m=0; empty, odd, and zero-restricted-mass cases. Two seeded validity draws per boundary use 1729 and 2718. Every allowed saturated word was directly checked to have full support and genus-one nontrivial components only.

## Retained limitations and final decision

No new rejection or minority objection arose. The historical limitations remain: adjacent-square insertion has zero fibers, scalar counts alone are not completion oracles, and fixed genus does not make partition enumeration polynomial. R1 avoids those steps. Exact connected g<=1 sampling does not supply arbitrary higher-genus sampling, an exposed-prefix support-joining oracle, all-length global sampling, any local-chain gap, or polynomial time in log N.

The first unproved mathematical lemma in the reviewed R1 claim is **none identified**. The dependency graph is closed under the named classical count theorem, the elementary final-letter decomposition, the positive conditional allocation DP, and the bit-complexity analysis. Accept the current R1-T1.1 proof and implementation and the specified global snapshots, while preserving the restricted-target and asymptotic-omission statements alongside them.

Reproduction, repository root:

```text
timeout 180s python3 -B experiments/20260907-genus-one-sampler/roles/r2-structural/recursive_independent_check.py --output experiments/20260907-genus-one-sampler/roles/r2-structural/recursive_independent_results.json
```

Python 3.12.3, standard library only; exact tests have seed null; diagnostic seeds are 1729 and 2718. The final run completed in about five seconds under supervision. Commit 20e86f665f69053031fe7eec0c3388458affb1fc and dirty state are in the raw output. No packages, configuration, subprocess services, or shared-file edits were used. New owned review files are recursive_review_input.md, recursive_independent_check.py, recursive_independent_results.json, recursive_audit.md, recursive_review_manifest.json, and RECURSIVE_AUDIT_SHA256SUMS; checkpoint.md records progress. All original C1 payload files remain unchanged.
