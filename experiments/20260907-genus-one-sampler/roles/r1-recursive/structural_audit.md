# Fresh nonauthor audit of structural candidate C1

Reviewer: R1 recursive role. Date: 2026-09-07. Verdict: **ACCEPT C1 as an internally checked exact expected-polynomial sampler**, conditional on its explicitly cited classical genus-zero count. No mathematical repair or missing outer-parser lemma was found. Coordinator acceptance and synthesis remain separate. This is a correlated same-model nonauthor review, not statistically independent confirmation.

The exact review input is preserved in [structural_review_input.md](structural_review_input.md). All seven payload hashes in the author's freeze_manifest.json and all entries in SHA256SUMS were verified before and after the new tests. In particular:

| artifact | SHA256 |
|---|---|
| R2 proof.md | 42cf1bdc767462157d5aa173244d604becf2c1f0a77a0d783b9d3d00b73e5b68 |
| R2 report.md | 798425705773608919b85404223700376571f67c4e47d8f4d840bb0835533b38 |
| R2 cut_sampler.py | 8e289a234124acad571223a7f70dec9c0d912dd2065808369bdcb7ff477f3224 |
| R2 audit.py | e36c587adb36f632ab8fd1959c1efa8a404186fe80236b373319cccaa7801db5 |
| R2 results.json | 6d85e3764afbdcf90d479176c1e68f64d7569f632ac83b9a8e30365789e5cd81 |

The full proof, production code, author audit code, report, and raw results were read. The review does **not** use R1's genus-one formula or sampler to fill any step of C1. The new independent checks use only the proposed grammar, literal small words, and the cited genus-zero local formula.

## Frozen theorem and boundary audit

The target is exactly X_N: ordered length-2N words in all transpositions of S_N, identity product, connected support on every one of the N fixed labels, N>=2. The algorithm always produces an exact target element and, under independent fair random bits, has the exact uniform distribution. Its expected bit time is polynomial in N, which satisfies all requested b>=1 without approximation. This says nothing about polynomial complexity in log N or a local-chain mixing time. N=2 is handled directly; N=1 at length two is infeasible. Singleton genus-zero factors have the empty-word base case, and zero-length internal component words are preserved rather than dropped from the support partitions.

## Claim-addressed proof audit

### C1.1 — ACCEPT: fixed-endpoint genus-zero count

The displayed expression equals Vakil's c^0_alpha after applying Section 1.2's relation c^0_alpha=G^0_alpha product alpha_i to Corollary 1.5. The source was checked directly in this run: [primary PDF](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf). This counts a fixed labeled permutation's ordered words. The a_i^(a_i+1)/a_i! factors equal a_i^a_i/(a_i-1)!, so there is no additional cycle-label, conjugacy, vertex, or word-order quotient. The singleton case is 1. The rightmost-first implementation obtains the predecessor endpoint by swapping the two images of p, namely p t; it matches the stated convention.

### C1.2 — ACCEPT: actual genus-zero sampling, not just counts

Deleting one final graph edge leaves at most two components. If the endpoint cycle is merged by the deletion, the prefix's total genus is q-1, with q its support-component count. Genus is nonnegative and cannot decrease when the final transposition is appended, so a genus-zero parent forces q=1. If the endpoint cycle is split, the prefix genus is q-2 and nonnegativity forces q=2. The two distinguished daughter cycles must occupy opposite components. Thus the branch classification is exhaustive.

The product of connected child counts and the genuine interleaving binomial cancels to the stated cell weight. All remaining cycles are distinct objects even when their lengths agree. subset_table processes their indices one by one, and sample_subset uses the correct two predecessor-cell counts; consequently each assignment in a selected cell is uniform. The final edge and actual prefix support recover the two subsequences and their interleaving uniquely. This establishes the per-word induction. The explicit `tasks` stack in sample_genus_zero evaluates the same induction without interpreter recursion. Its append/join continuations preserve local label maps and child order.

### C1.3 — ACCEPT: nonempty cut interval and unicyclic incidence graph

For any transposition word, g=(length-N-cycle_count+2*support_component_count)/2 starts at zero. A letter increases it by one precisely when it joins permutation cycles within an existing support component; all other letters leave it unchanged. A target word ends at g=1, giving unique forward and backward events h and b.

At any cut the prefix/suffix endpoint cycle counts coincide because their endpoints are inverse. Every endpoint cycle is contained in one support block on either side. The resulting bipartite graph is connected: its connectivity is exactly the join of the two support partitions, which is full because the whole word is connected. Writing V=q_L+q_R and E=c(p), the two genus formulas give g_L+g_R=V-E. A connected graph has E>=V-1, so g_L+g_R<=1. Hence b<=h. Equality cannot occur: if the middle transposition takes p to p t by joining cycles in forward order, the reverse-prefix product is p t and its next multiplication by t splits those cycles. The same letter therefore cannot be both events. Thus b<h, and J={b,...,h-1} is nonempty.

Inside J, g_L+g_R=0 implies E=V, so the incidence graph is connected and unicyclic. The converse construction assigns disjoint endpoint cycles to edges, and each side block receives a connected genus-zero word. The two interleaved side products are inverse, the whole support is connected, and its length is 2N. Summing left vertex lengths gives j=N+#R-#L. Isolates on a side appear as degree-one vertices with an incident singleton edge and zero local word length, so they cause no omission.

### C1.4 — ACCEPT: local and labeling weights

For a fixed ordered edge-slot inventory, a permutation of [N] cut into blocks yields each cycle assignment exactly product_e a_e times, from the independent cyclic rotations of each block. Thus there are N!/product_e a_e distinct assignments, and the uniform shuffled list induces the uniform cycle-assignment law. Within a side, component factorization counts and the exact interleaving multinomial cancel their local word factorials. Each edge contributes the square of its endpoint-cycle factor, divided by its labeling factor a_e. This is precisely A(a)=a^(2a+1)/(a!)^2. The remaining vertex factor is S^(d-3), including leaf S^-2 and core S^-1 cases. Both side factorials are retained. There is no independence assumption between cycle type and exposed connectivity in this argument.

### C1.5 — ACCEPT: code multiplicity and reciprocal-cut rejection

A connected unicyclic bipartite graph has one alternating core. Choosing one of its s left vertices and one of the two outgoing core edges gives exactly 2s rooted directed descriptions. In the two-parallel-edge case, those edges carry different disjoint labeled cycles, so the two directions remain distinct. Every off-core branch has a nonempty cycle-label set disjoint from its siblings; hence all k! orders of a vertex's children are distinct after labels are assigned, even if the numerical subtree shapes and edge sizes coincide. The factor (2s product k!)^-1 exactly removes these descriptions. No unmentioned graph automorphism quotient is needed.

Numerically isomorphic child branches can collapse to one numerical ordered shape before labeling. This does not invalidate the quotient: their distinct label allocations occur in separate edge slots afterward. The new degree-five witness below checks this point explicitly with a parallel core and three identical numerical leaves, where exactly 2*3!=12 label-list descriptions give a fixed macro.

Uniformity on cut incidences gives proposal mass 1/|A_N| for each (w,j). Conditional acceptance 1/|J(w)| yields total accepted mass 1/|A_N| for every w. After normalization the law is uniform on X_N. Since 1<=|J(w)|<=2N-1, acceptance is at least 1/(2N-1). Each new proposal uses fresh fair bits, so the conditional acceptance after any sequence of failed trials is the same constant. The geometric mean-trial bound is valid; there is no illicit product of marginal probabilities. Production code uses exactly `randrange(len(valid_cuts(word,N)))==0`.

### C1.6 — ACCEPT: positive grammar, actual parser, and resource bounds

Every child branch includes a positive-size edge. Accordingly, a coefficient of descendant mass d in a planted tree depends only on planted coefficients of mass <d. Starting with mass-zero roots, N complete forest/tree rounds contain every planted tree of retained mass <=N. Computing final forests from these tables adds no missing deeper object: an extra level would require mass >N. The finite-depth iteration therefore equals the ascending-mass solution claimed in the proof.

The forest recurrence is ordinary ordered concatenation with immediate child-edge sum S and child count k. The local vertex correction 1/k! is applied once by the planted/core vertex rule. An open parent port supplies the a in a+S without paying or double-counting its edge weight. The core matrix M_c[a,b] pays for the outgoing b-edge once; the incoming a-edge is paid at its preceding core vertex. Closing the matrix path makes every core edge appear exactly once, including a parallel core. Positive mass bounds core length by N. Laurent imbalance has magnitude <=N+1 for every retained rooted object; the code omits an explicit imbalance cutoff but cannot generate an out-of-range coefficient.

The actual parser matches the grammar. Its suffix matrices sum the remaining core path; each next choice has weight equal to its local coefficient times the appropriate suffix coefficient and its outgoing edge weight. The final state enforces the same incoming port a_0 and zero residual mass/imbalance. At each core/planted vertex, the (k,S) choice multiplies a forest coefficient by the vertex factor. Forest backward choices split off one edge/planted child and the remaining list with their exact product weights. Child mass decreases. Choosing the last algebraic forest factor before its preceding factors reverses the local child-list presentation, but is a weight-preserving bijection of ordered lists; it does not alter the projected law. Both tree and genus-zero decoding use explicit task stacks.

The polynomial index and arithmetic counts are sound. Laurent polynomials have O(N^2) entries; O(N^3) polynomial products construct forests, and N rounds cost O(N^8) rational operations. Core and suffix matrix powers fit the same bound. A proposed code has O(N) vertices and local words total 2N, so parsing and genus-zero generation are polynomial and dominated by that conservative budget. At most 2N-1 proposal attempts are needed in expectation.

The common-denominator argument includes partial ports. All paid edge-size mass is <=N, with O(N) edges/vertices. A planted parent size is at most N, and open core arguments a+b+S are at most 3N. Negative exponents are at least -2; edge/child factorial denominators and these size powers each divide a bounded power of (3N)!. The exponent 12N+4 is conservative and covers roots, forests, and open paths. Positive sums introduce no denominator primes absent from this common denominator. There are exp(O(N log N)) finite ordered objects, and total edge-size/degree exponents are O(N), bounding numerators by the same exponential order before conversion to the common denominator. The resulting O(N^2 log(N+1))-bit bound is valid. Categorical weights are converted by their denominator lcm into polynomial-bit integers; integer rejection uses fewer than two attempts in expectation. Allowing cubic elementary rational arithmetic yields the stated loose O(N^15 log^4(N+1)) expected bit bound.

## New exact falsification tests

The new script [structural_parser_audit.py](structural_parser_audit.py) imports the frozen production module without changing its file. It intercepts the categorical-choice callback to enumerate all positive-probability execution branches with exact rational weights. Its RNG shuffle replacement enumerates distinct multiset permutations, each with its mathematically correct uniform weight. The grammar, production decoding code, explicit stacks, and local weight expressions are unchanged. This tests the actual parser law, beyond comparing a DP's total with an independent inventory.

Results are in [structural_parser_results.json](structural_parser_results.json):

| check | N=2 | N=3 | N=4 | N=5 |
|---|---:|---:|---:|---:|
| actual parser numeric codes, all exact probabilities | 1 | 4 | 15 | 58 |
| weighted execution nodes for that parser | 1 | 6 | 22 | 85 |
| parallel-core numeric codes | 1 | 4 | 14 | 50 |
| full labeled macros, all exact weights | 1 | 9 | 101 | 1420 |
| ordered code/label-list descriptions | 2 | 24 | 360 | 6960 |
| partial coefficient denominator/support checks | 91 | 357 | 1176 | 2807 |

The maximum checked child count and hanging depth are both three. In the degree-five fixed identity macro with left block [5], right blocks {0,1},{2},{3},{4}, and j=8, exactly 12 ordered code/list representations give the macro, agreeing with 2*3!. Its word-fiber weight is exactly 1,008,000. This specifically attacks both the parallel-core and equal-shape-child multiplicity issues.

The complete production `sample_cut` execution was separately exhausted through N=3. At N=3 there are 1,056 weighted execution leaves and exactly 336 cut-pair outputs, each of probability 1/336. Literal word enumeration finds exactly those 336 pairs over 240 words. Applying the actual reciprocal-cut acceptance yields exact acceptance 5/7 and probability 1/240 for every accepted word. At N=2 the two label-shuffle executions project to the singleton cut pair with probability one. Thus duplicate execution paths, label-cycle rotations, code symmetries, and interleavings are counted explicitly rather than inferred from histograms.

Every retained tree, forest, core, matrix, trace, and open suffix-path coefficient in these tests has nonnegative weight, mass <=N, imbalance magnitude <=N+1, and denominator dividing ((3N)!)^(12N+4). These finite checks corroborate, but do not replace, the universal denominator proof.

The author's full N<=4 exact harness was also rerun under supervision, writing a separate reviewer-owned [structural_author_rerun.json](structural_author_rerun.json). It reproduced all target/cut counts, every labeled macro, all 6,792 genus-zero words at degree four, and the 27/120/3936 global regressions. The square-free (ab)^3 and doubled-tree family retain zero connected-square-removal fibers and valid genus-zero cuts. Three validity samples for each of seeds 1729 and 2718 at each N=2,3,4 passed. Stochastic outputs are used only for validity; the exact laws are proved and checked by rational enumeration.

## Decision and residual scope

| claim | review decision | repair required | evidence |
|---|---|---|---|
| C1.1 genus-zero normalization | ACCEPT | none | primary count convention and formula |
| C1.2 genus-zero recursive word law | ACCEPT | none | full branch proof, code inspection, exact rerun |
| C1.3 nonempty cut interval | ACCEPT | none | monotone genus, incidence identity, strict b<h |
| C1.4 local/labeled weights | ACCEPT | none | factorial and cycle-rotation cancellation; 1420 N5 macros |
| C1.5 coding and rejection | ACCEPT | none | labeled code multiplicity; 2*3! witness; all N3 accepted words |
| C1.6 positive parser and bit time | ACCEPT | none | complete grammar induction and exact actual-parser branches |
| C1.T frozen exact T0 theorem | ACCEPT for coordinator synthesis | none | all dependencies above |

No first missing mathematical lemma remains in this reviewed version. The proof rests only on the stated classical genus-zero count; it does not silently import a genus-one formula, assume a mobile bijection is already samplable, or use a completion count as a word decoder. Higher-genus sampling, unconstrained all-length sampling, and local mixing remain outside this verdict. Finite verification is evidence for the named finite claims; the universal result rests on the audited proof.

## Reproduction and ownership

From this reviewer role directory:

    timeout 180s python3 -B structural_parser_audit.py --numeric-max 5 --cut-max 3 --output structural_parser_results.json

From the repository root:

    timeout 180s python3 -B experiments/20260907-genus-one-sampler/roles/r2-structural/audit.py --max-n 4 --samples 3 --output experiments/20260907-genus-one-sampler/roles/r1-recursive/structural_author_rerun.json

Python 3.12.3, standard library only, repository commit 20e86f665f69053031fe7eec0c3388458affb1fc. New tests are deterministic; rerun validity seeds are explicitly 1729 and 2718. The independent parser test completed in under one second and the author's complete exact rerun in approximately 4.68 seconds. No installs, subagents, services, detached execution, or configuration changes occurred. The R2 snapshot and the original R1 payload remain unchanged. New reviewer files are structural_review_input.md, structural_parser_audit.py, structural_parser_results.json, structural_author_rerun.json, and this structural_audit.md; only R1 checkpoint.md is additionally updated.
