# Exact-version nonauthor review of R1-T2.v1

Frozen2026-10-28. **Verdict: ACCEPT the frozen R1-T2.v1 proof and implementation for coordinator reconciliation, under its stated published count input and fair-bit model.** No material numbered objection or required repair was found. This is a nonblind, same-model nonauthor review with inherited I1 context; agreement is correlated, not statistically independent evidence. No blind-review report was read and no blind reviewer was contacted. The global all-length mission remains OPEN.

The assigned input is preserved verbatim in input.md. All8 frozen hashes matched before review, and the production sampler hash was checked again after the new computation. The exact source, statement, proof, sampler, author test code, raw results, report and manifest were inspected. The reviewer’s structural candidate remains frozen and was not used to supply an absent recursive lemma. No author file was changed.

## Scope and imported theorem

The accepted scope is every specified canonical fixed endpoint sigma on v>=1 labels, with genus g in{0,1,2} and length v+c(sigma)-2+2g, whenever the connected fiber is nonempty. Output is an explicit ordered transposition word with rightmost-first product sigma. The law is exactly uniform under independent fair bits; singleton g0 returns the empty word and singleton positive genus rejects. The proposed O(v^11 log^3(v+1)) expected bit bound is valid under binary exact arithmetic. This result says nothing about arbitrary genus, a global fixed-length sampler, local-chain mixing, or polynomial time in log v.

I opened the two primary sources directly. The published [Goulden–Jackson double-torus paper](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjjcta1999-2.pdf), printed260, Theorem1.1 and equations(1)–(3),(6), gives the claimed genus-two rational series and its six numerator coefficients. The displayed general higher-genus form is conjectural there and is not used. The [predecessor paper](https://arxiv.org/pdf/math/9902009), Section2 and Section3 equation(2), identifies its coefficients with ordered transitive factorizations of a fixed permutation after the explicit conjugacy-class normalization. Thus the source input is the claimed fixed-endpoint count, not a naive count of unweighted cover-isomorphism classes. PDF text was read directly; screenshot calls returned references without visible images, so this review does not claim visual screenshot inspection. The source theorem is imported, not reproved here.

## R1-C2 — ACCEPT: polarization, inversion and positive count formula

I checked the algebra independently rather than accepting the positive formula from the finite counts. Let z_alpha=product_i a_i times product_a m_a!. Under p_a=(a/q(a)) sum_(i:a_i=a)y_i, the coefficient of the product of all distinct cycle variables in p_alpha is product_a m_a! times product_i a_i/q(a_i). Multiplying by the generating-series coefficient C2/(r!z_alpha) leaves exactly C2/(r!product_i q(a_i)). No equal-cycle factorial, branch factorial or label quotient remains. All individual cycles stay distinguished.

For x=z exp(-psi0), formal residues give dx/x=(1-psi1)dz/z. The x^(-v) factor supplies exp(v psi0). Thus the three source denominator powers3,4,5 become2,3,4. After polarization, each y_i has z-degree a_i, so the selected multilinear monomial has degree exactly v and z may be removed. This proves equation(A) with its stated exponent and no missing1/v.

The first signed numerator satisfies5a^4-12a^3+7a^2=a^2(a-1)(5a-7), nonnegative for positive integer a, including zero at a=1. The second factors as L_B L_D, with B(a)=a^2 and D(a)=29a^3-25a^2. The final term is28 L_B^3. Selecting a multilinear monomial forces distinct cycles into special slots; the slots remain labeled even when their weights agree. In particular three B slots count all six assignments to a fixed triple, exactly as L_B^3 requires.

For j ordinary marked cycles, the denominator contributes binom(e+j-1,j), while ordered choices of those j distinct cycles contribute j!, leaving the rising factorial(e)_j. Unmarked cycle variables each contribute v from the exponential. This is precisely the marker coefficient(C) and proves positive formula(D). Genus-one marker formula(E) likewise follows by choosing the distinguished squared-weight member of its marked subset; its j=0 term is correctly excluded in the S-term and the separate q-term is retained.

The new independent signed-source oracle in check.py does not call the production marker weights, specifications or scalar-coefficient functions. It expands the six signed numerator terms by ordered injections and uses elementary symmetric coefficients on the remaining cycles. All1521 count comparisons, every integer partition of degrees1 through14 and every g=0,1,2, agree. These tests support the implementation; the universal identity rests on the algebra above and the named source theorem.

## R1-D2 — ACCEPT: complete final-letter branches

Deleting the last transposition from connected support leaves at most two components. When the endpoints belonged to different final permutation cycles, the predecessor’s merged cycle contains both endpoints, preventing a disconnected prefix from being repaired by that last edge. The predecessor is connected with the same genus.

When the endpoints belonged to one final cycle, the predecessor has two distinguished daughter cycles. A connected predecessor has genus g-1. A disconnected predecessor has exactly two support components separating those daughters, and the two child genera sum to g. Therefore genus2 has precisely(0,2),(1,1),(2,0). The component anchored at x<y is distinguished, so there is no1/2 factor. Every remaining individual cycle goes entirely to one component. The last edge, actual prefix support components, child subsequences and their positions recover the branch uniquely from a literal word. Conversely each listed branch constructs such a word. No unsupported transitivity or normal-form theorem enters.

The production code computes sigma*tau by swapping the endpoint array’s images, consistent with rightmost-first composition. Its daughter-cycle ordering correctly uses the smaller endpoint’s component first. Zero weights are excluded rather than sampled. Genus-zero and singleton boundaries reduce to the inherited exact classification.

## R1-A20 and R1-A11 — ACCEPT: all forced allocation laws

For every single cycle, its placement either changes the A-size/count coordinates or leaves them unchanged on side B. Its mark choice is unmarked, ordinary, or one unused labeled special slot on that same side. Therefore the production transition is the direct product expansion of the marker generating factors plus the side-assignment indicator. It never permits one cycle to fill two slots, and repeated cycle sizes are processed at distinct indices.

Arbitrary forcing, including non-prefix forcing, removes the other side’s transition and changes nothing else. Retaining full masks and multiplying by the component-size/count scalar coefficients gives exactly the product B_ga(alpha_A)B_gb(alpha_B), summed over the retained assignments. The common factorial and q-product are independent of assignment because the genuine interleaving binomial cancels the two local factorials. The anchors ensure both component sizes are positive. Singleton positive genus has zero mass automatically.

For(1,1), the two marker coordinates are carried jointly through each side choice. Hence the DP retains the cross-moments needed for the product of the two genus-one factors; it does not multiply separately summed marginal masses. For(2,0)/(0,2), at most three special slots occur, all constant in number. The procedure loops over integer size/count/marker indices, not subsets.

The sequential sampler recomputes the two exact extension masses after every revealed cycle assignment. They partition the current fiber and sum to its current normalizer; their conditional ratios telescope to the correct normalized literal assignment weight. This remains valid after adaptive support restriction. The CP1 marginal-product argument remains false and is not used.

New tests exhaust2112 arbitrary partial-forcing queries on four cycle inventories, including all1 profiles and unequal profiles up to7 cycles. Each reference mass explicitly sums full assignments using the separate signed-source count oracle. All queries, including zero masses, agree. The largest unequal inventory is(1,2,1,3,2,1,4), beyond the author’s six-cycle allocation inventory. Full raw per-inventory counts and zero-mass totals are preserved.

## R1-W2 — ACCEPT: actual decoder and literal word law

The continuation stack is faithful to the disjoint induction. A connected branch appends its edge after its child completes. A split branch requests A then B, retrieves the completed words in reverse stack order, restores their sorted original labels, samples a uniform position subset and interleaves without changing each child’s internal order. Every positive call consumes one output letter; zero-length singleton leaves are handled directly. No interpreter recursion-limit setting is needed.

For a split branch, the selected branch mass, fully conditioned allocation probability, two child probabilities and reciprocal interleaving count cancel to1/C_parent. The connected branch cancels similarly. These factors are conditional on the branch and actual allocation; no independence assertion replaces a normalizer. Unique reconstruction makes this the full literal-word probability, with no hidden multiple representations.

The new test enumerates every positive logical categorical execution of the actual production sampler for endpoint(0123) in S4, genus2, length7. It compares the resulting complete rational law with all6^7=279936 literal transposition words. There are23296 accepted words, each with probability1/23296, and exactly23296 logical leaves. This target exercises both arbitrary endpoints and the newly feasible split into two size-two genus-one children. Endpoint, label restoration, child ordering, interleavings and zero branches are tested through the production stack rather than inferred from marginal histograms. This extends the author’s complete S3 laws, rather than rerunning the same finite target.

The accepted fairness model is exactly the stated ideal independent-bit interface. `randbelow` uses(bound-1).bit_length() bits and rejects values beyond the bound; conditional expected trials are below two, with bound1 deterministic. Binomial subset unranking is exact, including empty/full subsets. Seeded PRNGs are not used as evidence for uniformity in this review.

## R1-B2 — ACCEPT: explicit polynomial bit bound

The allocation table has coordinates(size,count,j_A,j_B), each O(v), and constant-size masks. At total genus at most2, at most three special slots occur. Thus O(v^4) scalar storage and O(v^5) arithmetic work per arbitrary forcing query are valid. Scalar coefficients, rising factorials and powers can be evaluated in at most O(v) operations per terminal entry, already covered by that bound. An individual node scans O(v^2) final edges and a constant number of genus pairs; sampling its chosen assignment adds O(v) oracle calls. Therefore O(v^7) arithmetic work per positive node and O(v^8) over the O(v) positive nodes are valid. Concatenations, label maps and subset unranking are lower-order polynomial work. Caches have fixed capacities and do not hide an exponential inventory.

Each cycle has a constant number of mark/side choices and multiplier O(v^4), so every integer table entry has O(v log(v+1)) bits. Positive factorial and power factors have the same bit order. The q-product denominator divides v! because sum_i(a_i-1)<=v. At most four negative size powers occur across the two sides; their denominators divide(v!)^4. The numerical divisors are covered by5760^2. Thus5760^2(v!)^5 is indeed a common denominator for every completed allocation summand. Positive sums retain it; no cancellation obscures a large intermediate. Counts and reduced rational operands have O(v log(v+1)) bits.

Charging cubic elementary bit cost per reduced-rational operation gives O(v^11 log^3(v+1)). The expected fair-bit work is polynomial by conditioning on each current positive branch and summing expectations over polynomially many logical draws. No sequential product of marginal success estimates is required. The statement’s exponent is conservative but supported; the observed small runtime is not its proof.

## Regression disposition and residual scope

New checks directly retain the square-free(ab)^3 witness; reproduce81 ordinary versus80 connected S3 length5 transposition words; reject the CP1 inequality21/2000<=1/100 while preserving later residual21/221<1/10; reject singleton genera1,2 and return its empty genus0 word; and verify the unique degree-two word for both endpoints and all three genera. The author’s hashed results preserve global baselines27/120/3936 and odd-length zero counts. These are references, not a new global application of the connected primitive.

The unweighted support-graph shortcut remains invalid; the reviewed algorithm never chooses such a graph. The marked-cut multiplicity problem remains separate; the recursive law has unique final-letter branches. Scalar counts alone remain insufficient, but the explicit forced-assignment oracle and stack decoder discharge that obligation here. No changed hypothesis repairs an old false lemma, and no historical counterexample was deleted.

| Claim | Review status | Exact dependency | Action |
| --- | --- | --- | --- |
|R1-C2 positive g2 fixed-endpoint count|ACCEPT / proved under published input|GJ1999 theorem, checked normalization, formal coefficient derivation|retain exact source and current formula|
|R1-D2 final-letter classification|ACCEPT / proved|elementary support/genus argument|retain all three g2 split pairs|
|R1-A20 forced(2,0)/(0,2) masses|ACCEPT / proved|R1-C2, inherited g0, marker product|retain exact conditional normalizers|
|R1-A11 tensor(1,1) masses|ACCEPT / proved|inherited g1, joint marker DP|retain joint table, not marginal product|
|R1-W2 word law and implementation|ACCEPT / proved|D2,A20,A11, ideal fair bits|current exact stack version passes new whole law|
|R1-B2 stated complexity|ACCEPT / proved|constant marker slots, positive arithmetic, common denominator|retain degree-v input model|
|R1-T2.v1|ACCEPT for coordinator reconciliation|all above and named external count theorem|scope only g<=2 fixed endpoints|
|Global all-length mission|UNRESOLVED|arbitrary larger-genus decoder or other route missing|no completion claim|

**First missing mathematical lemma in the reviewed scope:** none identified under the declared published input. Acceptance is this nonauthor reviewer’s exact-version verdict; blind review, coordinator reproduction and synthesis are separate gates. A future edited dependency reopens its descendants. Same-model concurrence remains correlated.

## Reproduction, runtime and ownership

Job I1-J7 was explicitly reserved by the coordinator and executed once through the current v0.3.2 bounded helper with attempt000002 run.json, timeout180s and1GiB address cap. It exited0 with child elapsed4.025269396s. Estimated memory was below256MiB; actual RSS was not measured. Python3.12.3, standard library only, deterministic seednull. The exact helper command and parameters are in job-I1-J7-plan.json, outcome in job-I1-J7-outcome.json, and complete raw output in results-v1.json. The observed repository HEAD at reservation was a4e2b9a9b7d68f33165ecc6f18b3f1532f344bec; candidate base commit remains d8893491e04aff74ff3185f7054470ffa24a44a4.

Only roles/r2-structural/review-recursive-v1/ was written during this review: input.md, verified-inputs.json, plan.md, checkpoint-halfway-v1.md, check.py, job-I1-J7-plan.json, job-I1-J7-outcome.json, results-v1.json, report-v1.md and review-manifest-v1.json. No frozen C2 payload, recursive author file, central artifact, Git staging or commit was changed. No descendants, installs, separate sessions or model/tier/permission override occurred. Requested/inherited Astra/ultra/default is unchanged; the worker API supplies no independent server-returned tier attestation.
