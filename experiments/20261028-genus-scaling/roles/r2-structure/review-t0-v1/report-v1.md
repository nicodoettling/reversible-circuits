# Exact nonauthor review v1 — coefficient generation and literal endpoint decoding

**Verdict: ACCEPT the exact composed mathematical argument for coordinator reconciliation**, under its explicitly imported published identities and scoped genus-zero/one formulas. I found no unproved algorithmic step or mathematical objection in COEFF-EXP.v1 plus AUX-ENDPOINT-MARKER.v1, including their claimed expected A C^(g+1)(N+g+2)^15 bit bound. This is one **NONBLIND, same-model, correlated internal review**, not final campaign certification or external human confirmation. Blind review, other exact reviews, integration reconciliation and final delivery remain the coordinator's gates.

This review was commissioned only after my separate R2-S.v1 structural report froze. That structural result is not used in the proof or this verdict. I did not inspect another current review's report before freezing this one. No author bytes were edited.

## Exact reviewed objects and source boundary

The coefficient proof SHA256 is `b152819ed84e460fe1d9248e2d178b7575104232b32551ef7466d518ec5ec610`; its coefficient implementation is `886bcb74ed39b18ff72b8b9ec4ad6f9e79b0fe6f09e406bdc2001a470e86cedc`. R1's proof is `f87fc0387e4f936ce82ebe0800851cb88a340eacc1188e5b8e0816fa8123d173`; its sampler is `26ca9e0d61f62d29f3f99b1d77e4bc925129abd025d07ca412d7dffd097a371d`. All16 payloads in the two author manifests matched at intake. Four integration/synthesis files were additionally hashed. The full records are verified-inputs-v1.json; final-verification-v1.json records the end-of-review recheck.

The target is exact uniformity on ordered connected transposition words with a specified endpoint on [N], length r=N+k−2+2g, where k counts individual endpoint cycles. T0 specializes to identity, N>=2, r=2N−2+2g. Multiplication is rightmost first; fair bits and exact binary arithmetic are the model. The proposed absolute polynomial degree is15. Labels and output words are explicit. There is no all-length global, graph-uniform, Hurwitz-walk or wire-polynomial conclusion.

The primary-source inspection is documented separately in source-verification-v1.md. It directly checked [GJV Theorem3.2 and equations13–16](https://math.stanford.edu/~vakil/files/gjvfinal.pdf) and [GJ Section2 and equation2](https://arxiv.org/pdf/math/9902009). PDF text/formulas were inspected; screenshot retrieval was unsuccessful, so visual-page verification is not claimed. The geometric identities are imported theorems; this review checks their hypotheses and translation, and separately checks the constructive extraction. It does not reprove ELSV or Hodge geometry. The earlier conjectural general form is not substituted for the later theorem.

## COEFF-EXP: source translation and uniform extraction

The two source normalizations compose correctly. Multiplying the covering count by z_alpha converts its factor product a_i^a_i/a_i! into product a_i^(a_i+1)/a_i!, leaving exactly the normalized polynomial B_h used by the authors. The polynomial variables correspond to individually marked cycle lengths. Equal numerical lengths do not divide its labeled monomial coefficient. The repeated-exponent automorphism divisor is applied once, when that coefficient becomes a rational-series term. Transitive transpositions generate one support component, and a connected transposition graph generates the full symmetric group on its vertices, so the connected-support restriction is exact.

The target coefficient K_h(theta) is a coefficient of the ELSV polynomial in d=len(theta) variables. This is important: the proof does not fit a possibly nonunique rational generating expression by guessing values. It recovers the uniquely specified polynomial monomial coefficient and then uses the source's identification. The allowed theta satisfy d<=3h−3 and total polynomial degree D=3h−3+d<=6h−6. All interpolation evaluations use positive a_i=1+b_i, |b|<=D. Thus degree n=sum a_i<=d+D<=9h−9, and transposition length r=n+d−2+2h<=14h−14. These inequalities have the correct constants and include the largest d boundary. h>=2 gives stable moduli for every d>=1; genus-zero exceptions never enter this interpolation.

The ordinary quotient recurrence is a fixed-endpoint recurrence. Each last transposition t contributes the count at sigma*t; conjugation equates counts within a cycle type. It must not receive a conjugacy-class-size multiplier, and the code does not insert one. Partitions of n inject into compositions, yielding at most2^(n−1) types, enough for2^M poly(M,L) work over all n<=M and lengths<=L. Each count has O(L log(M+2)) bits.

The connected extraction is also correct. In an unrestricted word with endpoint cycles indexed by S, take the unique support component containing the anchored cycle. It is a union U of whole endpoint cycles. Its connected subword and the unrestricted complement have unique subsequences and interleaving positions. This gives the stated disjoint anchored decomposition and its binomial factor, including empty singleton components. Processing proper subsets makes the recurrence well founded. The code groups equal lengths only after inserting the binomial multiplicity for actual indexed choices among the remaining equal cycles. This implements the subset recurrence rather than replacing labeled cycles by unweighted profiles. Its length/parity pruning uses only necessary endpoint and connected-support minima.

I independently checked simplex completeness. The products of binomial(b_i,beta_i), with |beta|<=D, form a basis for all polynomials of total degree<=D: expand ordinary monomials coordinate by coordinate in falling factorials. Mixed forward differences at0 recover those basis coefficients. Every gamma<=beta lies inside the sampled simplex, so no uncomputed value or degree assumption is hidden. Shifting b_i=a_i−1 and expanding recovers every desired monomial. In the implementation, only beta_i>=theta_i can contribute to coefficient a^theta, so its restricted sum beta=theta+eta is exactly equivalent. Sorting beta inside the difference cache is valid because the normalized polynomial is symmetric; the unsorted beta is still used for the target coefficient multiplier.

The simplex contains binom(D+d,d)<=2^(9h) points. Dense difference/conversion work bounded by its cube is therefore still single-exponential, even if deliberately inefficient. Anchored subset extraction has3^d rather than n! work, with d<=3h−3. Multiplying these exponential factors, or repeating the finite quotient computation for every point, remains C^h times a fixed polynomial in h. Summing through genus g and absorbing fixed powers of g into a larger absolute C closes the uniform coefficient-generation contract. There is no per-genus advice or assumed Hodge-integral evaluator.

The bit argument survives signed interpolation. All normalized sample denominators divide (L!)^(M+1); products of the Newton basis denominators divide D!, which divides L! at the declared bounds. The final automorphism divisor also divides a further L!. Consequently a single common denominator with O(h² log(h+2)) bits clears the computation. Finite differences and polynomial expansions add at most exponential-in-h many terms whose individual multiplier bits are polynomial in h. Bounding the sum of absolute values controls partial signed sums before cancellation. Thus coefficient numerators, denominators and reduced arithmetic intermediates have polynomial h bit size, and elementary exact arithmetic preserves single-exponential total bit cost. This is stronger than the exponential-bit allowance in R1's interface.

**COEFF-EXP verdict: ACCEPT at the exact frozen version.** No remaining effective-computation gap was found under the two declared published identities.

## R1-POL and R1-ALLOC: exact joint masses rather than marginal products

I rederived the polarization factor. Replacing p_a by(a/q(a))sum y_i contributes product m_a! for equal endpoint cycle lengths. It cancels the multiplicity factorial in z_alpha, while product a_i cancels its remaining cycle-length factor. The squarefree y coefficient is therefore C/(r!Q), with no repeated-cycle factor missing.

For the change of variables x=z exp(−psi0), dx/x=(1−psi1)dz/z. This removes exactly one power from each denominator. After taking the squarefree y coefficient, z-degree is automatically sum a_i=N. An unmarked cycle contributes N from the exponential. A set of j ordinarily marked cycles contributes product a_i times j! from the power of L1, canceling the j! in the denominator-series coefficient and leaving the rising factorial(e)_j. Each special slot remains labeled, even if two exponents agree; its repeated-exponent divisor already sits in the installed source coefficient. These observations reproduce formula(P), including its exponent N^(k−d−j), range j<=k−d, and e=2g−3+d. Genus-zero/one special formulas match the inherited normalized interface; their negative powers occur only at bounded magnitude.

For disconnected deletion branches, the interleaving binomial cancels both child length factorials, leaving L!Q(all cycles) times B_ga(alphaA)B_gb(alphaB). This cancellation is valid for every assignment because the total L=N+K−4+2(ga+gb) is assignment independent. It does not require either child to have a typical size or genus.

The allocation DP keeps the entire joint state(s,h,jA,maskA,jB,maskB). At a cycle layer, the actual individual cycle goes to an allowed side and fills either no marker, one ordinary marker, or exactly one available labeled special slot. Induction on layers gives the stated sum of all assignment/marker products. The four integer coordinates are bounded by N; the masks are bounded by the total number of special slots, not by the number of cycles. Thus no hidden2^N subset table is used in the theorem algorithm. The finite audit may enumerate assignments only on its explicitly small reference instances.

All source signs reside in scalar factors outside the integer marker transitions. The algorithm sums all specification pairs and all compatible terminal states before exposing Z(H) as a sampling mass. The combinatorial expansion proves that this completed quantity is the nonnegative integer sum of genuine branch counts. The code asserts this integrality/nonnegativity. It does not sample a signed term, take an absolute value, clip a negative subtotal, or use a sign-rejection mechanism.

For a free cycle i, the two completed extensions partition the remaining assignment set, so Z(H+i→A)+Z(H+i→B)=Z(H) at every positive history. The selected assignment probability telescopes through these exact conditional ratios to its full W/Z(initial). Earlier forced assignments remain in the table. This establishes the needed filtration-level conditional law; no marginal independence premise is used, so CP1's support restriction and renormalization do not invalidate it.

**R1-POL and R1-ALLOC verdict: ACCEPT at the exact frozen version under the coefficient contract.** The newly accepted coefficient extraction discharges that contract at the required uniform cost.

## R1-DEL and R1-WORD: literal reconstruction and probability

Deleting the last letter from connected support leaves at most two components. If its endpoints lie in different final endpoint cycles, the predecessor merges those cycles, placing both endpoints in one predecessor cycle and hence in one support component. A disconnected predecessor would place the deleted edge's endpoints in different components, a contradiction. This is the connected genus-g branch.

If they lie in the same final cycle, the predecessor splits it into two individually specified cycles containing x and y. A connected predecessor has genus g−1. A disconnected predecessor has exactly two components, with the distinguished split cycles on opposite sides and child genera summing g. Every remaining endpoint cycle lies wholly in one child. The canonical order x<y fixes the side names, so equal child sizes, profiles or genera need no factor1/2. The formulas include singleton empty children and omit zero-count branches.

Every literal parent word uniquely determines its final letter, predecessor support partition, child genera/subsequences and interleaving positions. Conversely those data reconstruct the word with endpoint sigma because predecessor endpoint is sigma*tau and tau²=id. In a split branch, the multiplication of branch, assignment, child and interleaving probabilities cancels to1/C_parent. In a connected branch the cancellation is immediate. Induction on output length therefore proves exact uniformity over the declared full connected fiber. The endpoint convention is implemented by right-swapping permutation entries and appending the chosen transposition.

The continuation stack matches this recursion: it restores child labels, samples the order-preserving interleaving, then appends the last edge. Each positive node consumes exactly one output letter; split child lengths sum to parent length minus1. Thus there are exactly r positive calls and at most N singleton leaves, not an uncontrolled branching recursion. The mathematical procedure can use explicit stacks for all bounded loops; finite Python recursion limits in the coefficient reference are correctly disclosed as implementation limits, not assumptions of the theorem.

Uniform integer rejection uses fresh fair bits and has success probability greater than1/2 conditional on every preceding history. The remaining bit stream is fresh at each logical draw. Summing conditional expectations over the deterministic bound on logical decisions justifies the expected-time claim. The proof never multiplies marginal success estimates or assumes that hidden previously used bits become independent again.

**R1-DEL and R1-WORD verdict: ACCEPT.** A scalar count is not being promoted automatically: the complete forced-assignment decoder and unique literal reconstruction supply the missing law.

## R1-COST and the exponent15

Let n=N+g+2. For total child genus at most g, at most3g+2 special bits occur. Each specification pair needs at most(N+1)^4 integer-state keys per cycle layer, K<=N layers, and O(g+1) transitions per entry. This is2^O(g)t(g)^2 times an absolute polynomial, with n^6 per forced query a safe loose arithmetic bound. A node needs O(N²(g+1)) branch queries and O(N) further assignment queries. With r<=2N+2g positive nodes, the author's2^O(g)t(g)^2 n^10 arithmetic bound has slack. No recursive exponent depending on genus is introduced.

The product D_g of coefficient denominators has bit length at most t(g)b(g), up to constants. The product of q(a) denominators divides N!. At most two inverse powers of each side degree occur in the genus-zero/one formulas; clearing all possible side degrees by(N!)^4 suffices. Thus D_g²(N!)^5 clears every allocation summand. Reduced partial sums and scalar products have denominators dividing this common integer; temporary products increase its bit bound only by an absolute constant factor.

For numerators, ordinary marks contribute total exponent at most N and special marks total exponent at most6g+O(1). The number of assignments/marker choices is at most(6g+8)^N. Rising factorials, powers, output factorials and the absolute sum over coefficient pairs give the bound

B=O(t(g)b(g)+n log n)

for intermediate bit length, even before signed cancellation. A value such as N^g has only O(g log N) bits; it is not an N^g state-space enumeration. Bounding exact reduced rational operations by O(B³) yields C1^(g+1)n³log³n. Multiplying by the n^10 arithmetic bound and using log³n<=constant*n² gives A C^(g+1)n^15. Constructing the common denominator, reading coefficients, explicit endpoint relabeling, uniform integers, interleaving and output copying all fit within this deliberately loose bound. Fixed powers of g and the coefficient-generator polynomial are absorbed into a larger absolute C; its value need not depend on N or g.

The result is an existence/complexity theorem with potentially large constants, not a practical performance guarantee for large genus. No arithmetic-unit-cost assumption or signed-probability oracle is hidden in the estimate.

**R1-COST verdict: ACCEPT the stated exponent15 and single-exponential genus dependence.** I found no asymptotic counterexample to the resource accounting.

## New exact falsification and implementation binding

Coordinator J7 ran `check_joint_v1.py` with exclusive reservation, current v0.4.2 bounded helper, sealed attempt000001 run,180s timeout and1GiB address ceiling. Exit0; child10.700962610077113s, estimated memory<256MiB, actual RSS unmeasured. Python3.12.3, standard library, deterministic seednull. The exact command and coordinator receipt paths are job-J7-record-v1.json. Actual execution commit was4b123da3c024adbcf73bfbf41c905f2f1f28d122. The raw script's base_commit field records original intakeb178daf...; this is an explicit provenance distinction, not a claim that the job ran at the old HEAD.

The test imports the integrated reference with only genus0/1 installed, generates and installs all6,26,85 terms at genera2,3,4, then obtains the production branch weights and every production sequential forced-normalizer law. It independently derives the terminal interleaving factor: if a suffix of length t contains k_A A-symbols, the compatible position sets have factor binom(L−t,r_A−k_A)/binom(L,r_A). Child suffix laws are combined with those factors and actual branch masses.

A separate DP over literal endpoint permutations and support partitions counts all unrestricted prefixes. Appending each fixed terminal word gives the exact connected endpoint cylinder counts. It uses neither the source polynomial nor the marker formula. The complete four-letter suffix law for all6 S3 endpoints and three-letter suffix law for all24 S4 endpoints at genus4 agrees exactly: **30 endpoint cases and5670 positive joint cylinders**. The full reference-law hashes are retained in joint-results-v1.json. Peak independent state count was36; no full N4 word enumeration occurred. These are joint marginals of the production-weight recursion, not a claim to enumerate every full execution of the stack implementation.

The test additionally checks all27 partial force maps on cycle profile(1,1,1,1,2), genus pair(2,2), against separate anchored connected quotient counts. It includes2 zero-mass assignments, exercising signed cancellation and singleton infeasibility with both child genera positive. This extends earlier forcing ranges and uses generated rather than built-in higher-genus constants.

The finite outcome supports the exact versions and can refute implementation errors; it does not prove the source theorem, universal law or asymptotic complexity. The proof audit above supplies those arguments. No failed test, timeout or repaired author version is omitted.

## Regressions, boundaries and final dependency verdict

The retained exact reference package includes S3m4=27,S4m4=120,S4m6=3936; ordinary endpoint81 versus connected80; the connected zero-adjacent-square word(ab)^3; triangle graph bias3/4 versus1/4; and CP1's21/2000>1/100 with later residual21/221. My earlier reserved J2 reproduced these numbers and its immutable artifact remains unchanged. The reviewed proof addresses each mechanism: connected counts rather than ordinary counts; no adjacent-square coverage premise; literal rather than unweighted-graph laws; unique x<y child anchoring; repeated slot labels and one automorphism quotient; actual posterior normalizers rather than marginal products. Parallel-cut multiplicities are irrelevant to this deletion architecture because its literal decomposition is unique; the structural cut theorem is not imported.

Singleton genus0 is the empty word; singleton positive genus is zero. The exact formulas/code retain those zeros. For N2 each feasible endpoint/parity has one repeated-transposition word. Odd identity lengths are impossible. Connected identity m0 exists only on a singleton, and m2 requires N2. The minimum connected length and parity constraints used in pruning hold componentwise. The stated algorithm needs no endpoint oracle; it explicitly builds the endpoint decoder.

M-GROW remains valid for its global eligibility-policy target. A prescribed-component C^g sampler neither makes high genus globally inexpensive nor changes that support-event mass. No all-length, mixing or hardness conclusion is gained from this review.

|claim|exact-version verdict|assumptions/evidence|residual obligation|
|---|---|---|---|
|Primary source translation|accept|direct P1/P2 formula/hypothesis check; source-verification-v1.md|published geometry remains imported|
|COEFF-EXP.v1|accept|complete finite quotient/support extraction, simplex interpolation and bit proof|none within declared source contract|
|R1-POL.v1|accept|independent residue/polarization and multiplicity derivation|none|
|R1-ALLOC.v1|accept|joint marker induction, arbitrary forcing and exact normalization; J7 forcing|none|
|R1-DEL.v1|accept|exhaustive last-edge support/cycle cases and unique reconstruction|none|
|R1-WORD.v1|accept|per-word probability cancellation; J7 integrated joint laws|none|
|R1-COST.v1|accept|constant-dimensional tables, denominator/numerator bounds, n^15 calculation|none|
|T0.v1 composition|accept for coordinator reconciliation|coefficient contract discharged plus endpoint decoder specialization|remaining campaign review/delivery gates, not an identified mathematical gap|

The **first unproved algorithmic step is none** in this exact composition under the explicitly stated published inputs and inherited genus-zero/one formulas. This verdict does not override a contrary blind/referee finding or the coordinator's final ledger. Any repair to an author proof, coefficient normalization, source contract or implementation reopens its dependent review scope.

## Files and containment

This review owns only `roles/r2-structure/review-t0-v1/`: input-v1.md(coordinator supplied, unchanged), plan.md, verified-inputs-v1.json, checkpoint-halfway-v1.md, source-verification-v1.md, check_joint_v1.py, joint-results-v1.json(coordinator executed), job-J7-record-v1.json, report-v1.md, final-verification-v1.json, manifest-v1.json and SHA256SUMS-v1. The preexisting R2 structural freeze was not changed. No protected/shared author files, manuscript, map or skills were edited. No descendants, package installs, research CLI sessions, machine changes, staging or commits occurred. Git status was inspected; other coordinator/worker changes remain theirs and were preserved.
