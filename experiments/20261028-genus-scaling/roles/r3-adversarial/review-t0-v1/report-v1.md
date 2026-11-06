# R3 NONBLIND exact-version review v1

**Verdict: ACCEPT for internal exact-version reconciliation** of COEFF-EXP.v1, AUX-ENDPOINT-MARKER.v1 and their composition T0.v1, including the stated expected bit bound A C^(g+1)(N+g+2)^15. No correction to the frozen authors' proofs or code was needed. The acceptance is source-scoped: the published ELSV/GJV enumeration theorems are imported, not reproved. It is not external mathematical certification, a production performance claim, or an all-length global sampling theorem.

This report reviews the authors' actual simplex-coefficient construction and actual decoder. Agreement with my earlier blind existence argument is not its justification. The independent fresh finite check intercepted the integrated production sampler's categorical execution and passed nine whole laws over52,180 distinct outputs, plus225 additional forced allocations. Universal correctness and complexity rely on the proofs audited below, not extrapolation from these checks.

## 1. Exact versions, exposure and ownership

The coordinator acknowledged the immutable blind freeze before supplying this explicitly NONBLIND task. Original blind-report-v1.md remains SHA25697e4d2d4772667e7dbd67bbbff9c44c451947eb4933274277ccf5bebb6dd4e51. Every file covered by the original blind manifest was checked unchanged after this review's computation.

Reviewed versions:

| artifact | SHA256 |
|---|---|
| theorem-v1.md | fecfe4a443be67d8e1a31af9ea2491610e5d9708848f9adab5a333b28d5cfb7c |
| coordinator/coefficient-theorem-v1.md | b152819ed84e460fe1d9248e2d178b7575104232b32551ef7466d518ec5ec610 |
| roles/r1-recursion/proof-v1.md | f87fc0387e4f936ce82ebe0800851cb88a340eacc1188e5b8e0816fa8123d173 |
| roles/r1-recursion/statement-v1.md | e161d83dce0fc5dee0fa6ad40d93142e93eea18cb755bcdc4ab867c02a74f0cf |
| coordinator/coefficient_oracle_v1.py |886bcb74ed39b18ff72b8b9ec4ad6f9e79b0fe6f09e406bdc2001a470e86cedc |
| roles/r1-recursion/sampler-v1.py |26ca9e0d61f62d29f3f99b1d77e4bc925129abd025d07ca412d7dffd097a371d |
| coordinator/integrated_sampler_v1.py |2a0352ebf6750dcf7453b5b2cd8b96569a905d40a7da3fcfce37b5211ce7dcc8 |

All entries of the coefficient author freeze and R1 author manifest were checked, not only these selected entries. `bindings-v1.json` records those checks and the integrated audit/result bindings. The review input and complete script/result/report are retained in this owned directory. No author or blind file was edited.

Read material included the full named proofs, statements, source-verification notes, integrated wrapper/audit/results, coefficient implementation and decoder implementation. Before this phase I had seen only the inputs disclosed in the frozen blind report. In this phase author constructions and verdicts were visible. The same model, project context and primary sources create correlated review; this is not statistical independence. No descendants, research CLI sessions, package installs, Git actions or machine/configuration changes occurred in this phase.

## 2. Source import and normalization: ACCEPT

The relevant primary source is [Goulden–Jackson–Vakil, revised22Dec2000](https://math.stanford.edu/~vakil/files/gjvfinal.pdf), Section2.3 equation(13), equations(14)–(16), and Theorem3.2. Its finite rational form is a proved theorem. The1999 double-torus higher-genus conjecture is not substituted for it. The fixed-permutation normalization was checked against [Goulden–Jackson, arXiv:math/9902009v1](https://arxiv.org/pdf/math/9902009), Section2 and equation(2), with its genus0/1 statements for those bases. PDF text was inspected; screenshots were unsuccessful, and no visual-page check is claimed.

Here is my convention calculation. If alpha=(a1,...,ak), the fixed endpoint count equals the cover normalization times z_alpha=product ai*Aut(alpha). ELSV's prefactor is r!/Aut(alpha) times product ai^ai/ai!. Multiplying these factors gives exactly

    r! product_i ai^(ai+1)/ai! = r! Q(alpha).

Therefore B_h=C_h/(r!Q) is the individual-variable ELSV polynomial, with no extra factorial or class-size multiplier. This calculation remains valid when cycle lengths repeat. Stable genus h>=2 permits every k>=1 used by the preprocessor, including the degree-one positive-genus value zero. Genus0's unstable one/two-cycle cases are supplied by the separately stated genus-zero formula; they are not obtained by applying stable ELSV outside its scope.

The coefficient of one labeled monomial a1^theta1...ad^thetad is the signed primitive integral. The rational-series coefficient is that value divided by Aut(theta), once. It is not divided once per slot or again during marker extraction. The degree condition lambda=3h-3+d-sum theta_i with0<=lambda<=h gives

    2h-3<=sum(theta_i-1)<=3h-3.

It implies d<=3h-3, every theta_i<=3h-2, sum theta_i<=6h-6, and denominator exponent2h-2+d. These are the exact bounds used downstream.

Support connectivity and transitivity of edge generators agree. Reversing factor order inverts the endpoint, preserving cycle type. The implementation directly multiplies rightmost-first via swapping the images at the two transposition positions. No classification, transitivity of a Hurwitz action, or mixing theorem is imported.

## 3. COEFF-EXP.v1 mathematical and code audit: ACCEPT

I independently rederived each of the three algorithmic lemmas.

**Ordinary quotient counts.** A final transposition gives the predecessor sigma*t. Summing counts of fixed predecessors over the literal transpositions is correct; no conjugacy-class factor belongs in this recurrence. Representatives permit the finite table to be indexed by cycle type. The elementary partition-to-composition bound used here is enough because the largest degree is onlyO(h).

**Connected extraction.** The support component containing one distinguished endpoint cycle determines a unique proper cycle subset in every disconnected word. Its connected subsequence and the unrestricted complement subsequence have binom(l,s) possible interleavings. This proves the subtraction identity, including isolates and empty words. The proof's3^k subset-pair bound is valid. The implementation groups equal-length choices into subprofiles and inserts product binom(m_a,b_a); this is a valid compression of distinct indexed subsets. The omission of infeasible length/parity entries is justified by the elementary length bound. No ordinary count is silently substituted for a connected count.

**Positive-simplex interpolation.** For d cycles, P_h,d has total degree at most D=3h-3+d. At a=1+b, |b|<=D,

    n=d+|b|<=d+D<=9h-9,
    r=n+d-2+2h<=14h-14.

The mixed differences at the integer simplex determine every total-degree<=D polynomial in the product falling-factorial basis. All points used by a mixed difference lie in the same simplex. Translation back from b to a and coefficient extraction are finite exact operations. This establishes uniqueness and completeness without an unbounded search or per-genus advice.

The implementation calculates only the needed coefficients, rather than expanding every polynomial. A Newton basis term can contribute to a^theta only when beta_i>=theta_i. Its `simplex(d,slack)` enumerates all nonnegative slack vectors with total at most the slack, exactly the required range. Sorting beta for the cached mixed difference is valid because P_h,d is symmetric in its individual variables; it does not sort or identify the labeled monomial slots during conversion. The final Aut(theta) divisor is inserted exactly once in `recover`.

**Uniform bit cost.** Each ai<=M<=L divides L!, so product ai^ai divides(L!)^(sum ai). With r! dividing L!, the normalized-value denominators divide(L!)^(M+1). The total factorial degree in Newton monomial conversion is at mostD, so product beta_i! dividesD!, which divides L! under the chosen bounds. Aut(theta) divides d!, hence another L! clears it. The source's proposed common-denominator implementation is therefore valid. All these denominators have O(h²log(h+2)) bits. Finite-difference weights, polynomial expansion coefficients and exponential-size summations add only a polynomial number of bits. A fixed polynomial of a single-exponential-size inventory is still single-exponential. Polynomial factors in h can be absorbed into a larger absolute exponential constant.

This proves the coefficient contract required by R1, including uniform effectiveness, list size, bit size and preprocessing time. No algorithm for Hodge integrals is assumed. The coordinator's degreeO(h) simplex route is different from my blind degreeO(h²) numerator/Vandermonde recovery; this review checks the simplex route on its own merits.

## 4. R1 polarization, allocation and literal law: ACCEPT

The polarization p_a=(a/q(a))sum y_i cancels Aut(alpha) and the cycle-length factor in z_alpha correctly. The formal residue contributes exactly one factor(1-psi_1), reducing the denominator exponent from2g-2+d to2g-3+d. Since every selected squarefree cycle monomial already has weighted z-degree N, setting z=1 after its extraction is justified.

Special factors are labeled slots even when their powers coincide. The denominator's ordinary marks contribute the rising factorial(e)_j, and the exponential supplies N for each unmarked cycle. Thus repeated special powers neither lose a factorial nor receive a second Aut divisor. The genus-one positive specifications reproduce the inherited formula: its second specification begins at j=1 and has the possible exponent-1 at the last term. The singleton bases are correct by the source identities or explicit overrides.

For a two-child allocation, table indices retain side degree, side cycle count, both ordinary-marker counts and both masks. The item-by-item multiplication proves that it preserves the full joint allocation/moment weight. Actual equal-length cycles are distinct items. Any prior forcing simply removes disallowed side transitions; it does not alter the identity or require an independence assumption. Final factorial cancellation gives the exact shuffle-weighted count. Signed specification contributions are summed completely before probabilities are formed; the complete answer is a nonnegative integer because of this literal interpretation.

The conditional sampling law is exact at every surviving history: the two extended forced counts add to the current count. Their successive ratios telescope to the completed allocation's weight divided by the initial total. This is stronger and more precise than a marginal probability estimate; it survives zero branches and arbitrary previous assignments.

Final-edge classification is exhaustive. Joining two endpoint cycles leaves a connected predecessor at unchanged genus. Cutting an endpoint cycle leaves either a connected predecessor at genus g-1 or exactly two predecessor components with genera summing to g. The child containing the smaller final-edge endpoint is distinguished, even when numerical child data agree. Removing one graph edge cannot create more than two components, and every endpoint cycle lies wholly in a support component. These facts give the unique inverse reconstruction required by the proof.

For a literal parent in a split branch, the factors

    Z/C_parent, W/Z, 1/C_A, 1/C_B, 1/binom(L,r_A)

multiply to1/C_parent. Unique final-edge reconstruction proves uniformity, rather than only stationarity or a count identity. Induction terminates because child lengths sum to parent length minus one; the number of positive calls is exactly the output length. The explicit continuation stack in production code realizes this recursion. Its merge ordering, child relabeling and subset unranking were included in the new execution-law check below.

## 5. Absolute exponent15 and fair-bit model: ACCEPT

Let n=N+g+2, t(g) be the installed specification count and b(g) the largest coefficient bit size. The coefficient theorem satisfies the frozen t,b,preprocessing<=A0 C0^(g+1) contract after enlarging constants.

For fixed genus pair, four polynomial coordinates have at most(N+1)^4 values, and the two masks together contain at most3g+2 bits. There are at mostN item layers and O(g+1) outgoing transitions per entry. Iterating the specification pairs gives a2^O(g)t(g)^2 factor; it does not change the polynomial degree in N. Evaluating final powers/factorials with direct finite loops fits the proof's conservative n^6 per query. At most O(N²(g+1)+N) queries occur at each positive node, and at most2n nodes occur. The stated2^O(g)t(g)^2 n^10 arithmetic envelope is valid.

The denominator audit does not assume cancellations make intermediate values small. If D_g is the product of installed coefficient denominators, log D_g=O(t(g)b(g)). Genus0/1 degree powers have negative exponent magnitude at most2 per side, and higher-genus residue terms have no negative degree powers. Across all possible child degrees, (N!)^4 clears those denominators. The q-product denominator dividesN!. Therefore D_g²(N!)^5 clears every summand and partial signed sum. A product of reduced rational intermediates can enlarge this common bound by an absolute factor in bit length, which is harmless.

For numerator size, the number of item choices is at most(6g+8)^N. Ordinary marks contribute degree at mostN; special-slot exponents across two children sum to at most6g+O(1). Rising factorials, scalar powers, q-products and factorials contribute O(n log n) bits. Summing absolute values across the specification inventory retains

    B=O(t(g)b(g)+n log n).

This applies before cancellation and after conditioning. Cubic elementary rational arithmetic gives B³<=C1^(g+1)n³log³n. Combined with n^10 operations and log³n=O(n²), it gives the asserted exponent15. Table indexing/comparison work fits the same bit envelope; no variable-dimension exponent in N is introduced. Coefficient-only polynomial factors in g are absorbed into the exponential constant, not into an input-dependent polynomial exponent.

At a logical integer draw, rejection from the next power of two has conditional expected attempts below2, including after any selected history; a one-point distribution is deterministic. The total number of logical draws has a deterministic bound from the finite recursion/table procedure. Summing conditional expectations proves the expected bit bound. No product of marginal acceptance estimates or unbounded accepted-node count is used.

The theorem is an explicit finite mathematical algorithm. The Python reference has ordinary interpreter/resource limits, notably recursive finite count generation; the proof's bounded tables and decoder stack do not rely on that interpreter being able to run every numerical input. Acceptance of the mathematical bound is not a claim that the reference code is optimized or physically feasible at large genus.

## 6. Fresh production-interception check J8

The coordinator alone reserved and ran J8 through the current v0.4.2 bounded helper and sealed attempt000001 run file, after J7 completed. Limits180s and1GiB address space. Execution commit4b123da3c024adbcf73bfbf41c905f2f1f28d122 is recorded in coordinator/job-J8-plan.json. The raw result separately identifies the earlier blind-intake commit as provenance; that field is not the J8 execution commit. Python3.12.3, stdlib only, deterministic seed0 metadata. The job exited0 with child elapsed5.878384137991816s. No actual RSS measurement is claimed.

Exact child command:

    /usr/bin/python3 -B experiments/20261028-genus-scaling/roles/r3-adversarial/review-t0-v1/production_law_check_v1.py --output experiments/20261028-genus-scaling/roles/r3-adversarial/review-t0-v1/production-results-v1.json

The test imported the actual integrated wrapper, which first deletes all built-in genus>=2 specifications. It generated coefficients through genus3, then repeatedly called the actual `sample_endpoint` procedure. Only `weighted_choice` and the interleaving `randbelow` primitive were intercepted. Each unresolved categorical branch generated replay continuations with its exact rational mass. Thus the test used the production branch enumeration, forced-assignment updates, continuation stack, child label maps, subset unranking and word assembly; it did not implement another recursive decoder.

Fair-bit retry loops were analytically contracted to their exact uniform integer law. This tests the categorical execution law, not an enumeration of infinite random-bit tapes. Singleton choices were collapsed, and zero-weight choices were never followed. Replay checked that every previously encountered category's kind and weight list remained identical on its fixed history.

For each output word, an independent evaluator checked length, rightmost-first endpoint and connected support. The number of distinct outputs was compared with an independent state DP over literal endpoint permutation and support partition, imported from my frozen pre-exposure reference implementation. Every output's total rational mass was then checked equal to the reciprocal of that independent count. Validity, exact cardinality and equal mass together establish each tested whole finite law.

| endpoint cycle type | N | genus | complete distinct outputs | mass of each output |
|---|---:|---:|---:|---|
|(1,1)|2|3|1|1|
|(1,1,1)|3|0|24|1/24|
|(1,1,1)|3|1|240|1/240|
|(1,1,1)|3|2|2184|1/2184|
|(1,1,1)|3|3|19680|1/19680|
|(1,2)|3|2|728|1/728|
|(3)|3|3|2187|1/2187|
|(2,2)|4|1|3840|1/3840|
|(4)|4|2|23296|1/23296|

All nine laws passed, totaling52,180 outputs. No full N4,g3 word space was enumerated.

The same job made225 new arbitrary-forcing comparisons. Cycle-size lists were(1,1,2,2), (1,2,1,3), and(2,2,1,1,1). Child-genus pairs were(1,2),(2,1),(1,3),(3,1),(2,2). Every extra cycle independently had state free, forced A or forced B, while the two anchors remained opposite. The reference enumerated actual assignments and used connected counts from the independent frozen implementation's ordinary/anchored-component tables. Production `allocation_mass` agreed in every case. This includes both children at genus2, zero-mass singleton histories, repeated sizes, unequal sizes and asymmetric forcing.

These checks are fresh finite falsification evidence. They do not prove the published source theorem, arbitrary-genus bounds or universal sampling law. The script and raw result include their exact source hashes. The prior J1/J4/J5 results remain prior evidence and are not relabeled as this review's independent computation.

## 7. Retained failures and boundary decisions

| regression | review outcome |
|---|---|
| Ordinary versus connected endpoint81/80 | Retained. Both mathematical extraction and the decoder use connected counts; ordinary counts only feed exact inversion. |
| Unweighted support graph bias | Retained. This algorithm selects literal branches with their complete counts. |
| Adjacent-square insertion misses(ab)^3 | Retained. Actual-final-edge reconstruction covers such words; it assumes no removable adjacent square. |
| Equal-child multiplicities | Retained through anchored child labels; no1/2 quotient is inserted. |
| Parallel-cut/graph code multiplicities | Prior counterexample remains valid; this decoder uses no such encoding. |
| Repeated special exponents | Distinct slot labels plus exactly one source Aut divisor; checked by proof and forcing tests. |
| CP1 cached-prefix failure |21/2000>1/100 remains the rejection of the marginal-product claim. Actual restricted masses and fresh fair-bit integer choices avoid that invalid inference. |
| M-GROW low-genus/small-support policy | Remains valid. Exponential genus time does not turn that policy into a polynomial global sampler. |
| N2, any feasible genus | Unique edge repetition; whole production law checked at genus3 and analytically valid generally. |
| Singleton g0 / positive genus | Empty word / empty fiber; no division by a zero parent mass. |
| Odd identity length | Empty by sign. |
| Identity m0 on N>=2 | Not connected. |
| Identity m2 | Connected only on N2. |
| Near-minimal endpoints | Genus0 formula and connected-length proof apply; empty singleton descendants retained. |
| Negative/signed intermediate terms | Exact arithmetic only; no signed categorical probability or truncation. |
| Fixed-genus inference | Not used: every coefficient-generation loop and table dimension is uniform in g. |

No newly rejected lemma or repair was found. These negative findings are retained as active exclusions, not erased by acceptance of a different construction.

## 8. Claim-addressed verdict and scope

| claim | verdict | decisive reason | remaining dependency |
|---|---|---|---|
| ELSV/GJV source normalization and rational basis | ACCEPT source-scoped | Explicit multiplication by z_alpha and stable degree condition | Published enumeration theorem imported |
| COEFF-EXP.v1 quotient and connected counts | ACCEPT | Literal final-letter recurrence and unique anchored component extraction | Elementary permutation/support facts |
| COEFF-EXP.v1 simplex reconstruction and bit cost | ACCEPT | Complete finite Newton basis; positive-simplex bounds; factorial common denominator | Checked source polynomiality |
| R1-POL.v1 | ACCEPT | Exact polarization and residue Jacobian, multiplicities retained | Source basis and genus0/1 formulas |
| R1-ALLOC.v1 | ACCEPT | Joint marker DP and complete forced counts;225 fresh cases | R1-POL |
| R1-DEL.v1 / R1-WORD.v1 | ACCEPT | Unique reconstruction and per-word cancellation;9 actual production laws | Allocation/count exactness |
| R1-COST.v1 exponent15 | ACCEPT | n10 arithmetic envelope, signed B-bit bound, conditional fair-bit expectation | Coefficient contract, now supplied |
| T0.v1 and AUX-ENDPOINT-MARKER.v1 composition | ACCEPT for internal reconciliation | All stated dependencies close in their exact versions | Coordinator reconciliation/clean delivery; imported published inputs |
| Unrestricted global polynomial sampler, mixing, wire-polynomial efficiency | Not claimed; unresolved | No implication from exponential-in-genus time | Separate research targets |

There is no first unproved internal mathematical step identified in the reviewed composition. The remaining project-level actions are to reconcile the complete reports, retain these exact source bindings, perform the coordinator's clean decisive check, and state the final scope honestly. The theorem should not be advertised as external certification or as a practical large-genus implementation benchmark.

All new files are within `roles/r3-adversarial/review-t0-v1/`: supplied input-v1.md; checkpoint-1517.md; production_law_check_v1.py; production-results-v1.json; bindings-v1.json; this report; and manifest-v1.json. The review followed the explicit no-Git worker instruction; the coordinator owns repository-wide status reporting. Original blind artifacts were verified unchanged.
