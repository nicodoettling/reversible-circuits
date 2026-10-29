# Construction role final report v1

Role /root/r2_construction, 2026-10-29. **Verdict: reject both frozen candidates on their stated schedules.** Exactly two candidates were authored, sequentially; C1 rejection preceded C2 design. Both are exact identity samplers before M0 noise, and each has a polynomial-time one-sample statistical attack with near-unit advantage. Full proofs and exact quantifiers are retained. These are scoped candidate rejections, not a refutation of general sparse-noise hiding, not a positive cryptographic construction, and not general bridge-sampling hardness.

The authored mathematical claims are proved in the linked elementary derivations and have passed named internal review/checks; final campaign acceptance remains coordinator-owned. Same-model author-distinct reviews are correlated and are not human certification. No claim was upgraded because of a restart. Sources, cap and task scope were read before work; the historical mixing assignment was not pursued.

## Frozen algorithms and outcomes

candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict
---|---|---|---|---|---
C1-v1: six-distinct-edge relator blocks, s adjacent Hurwitz steps | compare full Q_k(D) to matched Q_k(global U), no uniformity claim | proved for every tape; checked all ordered quadruples at N=4,5 | fresh support choices can vary; its scrambling alone cannot | no equal edges within a fresh six-block; exact identity/injectivity/uniform single-position marginals; deterministic surviving-window checks | reject on frozen dense schedule
C2-v1: path factorization glued to inverse star, s=L^3 steps | same exact M0 comparison | proved for every tape; checked all injections in small cases | random planted support varies across replies; each scramble stays in its original support/orbit | mandatory S3L4/S4L4/S4L6 bridge counts, all signed moves, support invariants and explicit counting bound | reject on frozen sparse schedule

C1 algorithm: candidate-1-v1.md plus candidate-1-runtime-erratum-v1.md. It exposes only (N,B,s,k), has no key, and uses fresh label/scrambling tapes on every reply. Its base six-gate word is (ac)(cd)(ab)(ad)(bc)(bd), with six distinct edges. Entropy is at least B log_2((N)_4). Runtime is expected O(L+s) label operations; exact random-bit cost is O(L log N+s log L+s), correcting the originally overgeneral finite-family log N claim.

C2 algorithm: candidate-2-v1.md. It exposes only (N,m,s,k), has no key, samples a uniform ordered injection of m+1 labels, emits a path factorization and an inverse star factorization of the same cycle, then applies s=L^3 Hurwitz moves. Its entropy is at least log_2((N)_(m+1)); pre-noise support is exactly m+1 for every tape and every number of Hurwitz moves. The second candidate removes C1's many short relators and bounded-scrambling premise; it fails by a different global support statistic.

The supplied candidates_v1.py is for small executable validation. implementation-scope-v1.md records the Py_ssize limitation of rng.sample(range(N),v), the noncryptographic test RNG, and complete sparse Fisher--Yates pseudocode implementing the same ideal injection law using O(v) storage and expected polynomial bit work for arbitrary-precision N. No huge N label array was created. This clarification changes neither candidate law nor security quantifier.

## Noisy-word attacks

attack | frozen parameters | one-sample effect | reused setup | time/sample complexity
---|---|---|---|---
C1 aligned null-six count | N=lambda^2, B=lambda^6, L=6B, s=floor(B/10), k=lambda | advantage >=1-min(1,N! binom(B,ceil(B/2)) q^(-ceil(B/2))); deficit exp(-Omega(lambda^6 log lambda)) | already broken with one reply; no key | one reply, O(L) label operations
C2 distinct-label count | m=lambda, N=lambda^6, L=2lambda, s=L^3, k=floor sqrt(lambda) | advantage >=1-R, R=min(1,binom(N,h)binom(h,2)^(2m)/D); R<=lambda^(-lambda) for lambda>=1024 | already broken with one reply; no key | one reply, O(L) expected dictionary operations, or deterministic sorting polynomial time
T0 six-window scan, reviewed in this role | N=lambda^2,L=6N,k=lambda, moves<=floor(N/8), lambda>=32 | advantage >=7/10 for the broader relator class | t independent reference replies give false accept <=(3/10)^t | one reply sufficient; O(L) label operations

Here q=binom(N,2), h=m+1+2k and D=(N)_(2m)(2m)!/(4^m m!). For C1 the candidate has at least B-2s-k intact aligned null windows. For the reference, iid product law is preserved by exact uniform-k-subset replacement; conditioning on its identity endpoint costs at most N!, while independent disjoint iid windows have return probability <=1/q. This is a one-time change of measure, not a product of conditioned marginal probabilities.

For C2, the candidate's observed support is at most h. The GLOBAL bridge count is at least D by counting disjoint transpositions each appearing twice in any order. The reference event support<=h has at most binom(N,h)binom(h,2)^(2m) literal words under the iid/noise law; the q factors cancel in the same conditioning inequality. The finite count requires N>=2m and h<=N; the proof uses no connected bridge substitution. Its explicit asymptotic derivation is in candidate-2-rejection-v1.md.

All schedules are polynomial in lambda,N,L; none claims efficiency merely in log_2 N wires. The common semantic error upper bounds are 4/lambda for C1 and 4 floor(sqrt(lambda))/lambda^6 for C2. These are inverse polynomial, not negligible-error guarantees. Full replacement k=L makes both worlds exactly iid and the attack threshold conditions correctly become vacuous.

## Executed checks and exact provenance

Coordinator reservation J002-candidates, current v0.4.4 bounded helper, sealed attempt 000001 run.json, timeout 120s, address-space ceiling 1GiB. Estimated <=50625 unconditioned words, <=3936 retained bridges and <128MiB. Observed exit 0 and elapsed 0.57283616065979s, Python 3.12.3, stdlib only, commit 24649e0a2b4fa0d0ede444234bfedfc428453571. Exact helper invocation is in ../coordinator/job-registry.json; raw compact machine-readable output is results-candidates-v2.json, including source hashes.

Inner command:

    python3 -B experiments/20261029-noisy-bridge-viability/r2-construction/check_candidates_v2.py --output experiments/20261029-noisy-bridge-viability/r2-construction/results-candidates-v2.json

Exact enumeration found global bridge counts 27,120,3936 for S3L4,S4L4,S4L6, and 765 for S6L4. All 44832 signed adjacent moves on these enumerated identity spaces preserved identity and support and inverted correctly. (Counts 162+720+39360+4590.) C2 base injections were injective with uniform per-position gate marginals; C1 had six distinct edges and identity for every tested ordered quadruple. Seeds 17,29,43 supplied 1740 implementation/noise/surviving-window regressions, not empirical security estimates. N=2 singleton even words, L=0/k=0, odd-length impossibility, k=0,1,L and the common support error bound were checked.

Small support-test behavior was retained even when uninformative: C2 k=0 reference acceptance is 1 at S3L4 and S4L6, 17/20 at S4L4, and 11/17 at S6L4. These finite facts neither prove nor refute the asymptotic schedule. Full support on four labels in S4L6 is NOT the same as connected support: the histogram counts 2970 full-support words, whereas connected count 2880 is a separate inherited/exact fact. No silent connected baseline was used.

Exact integer comparisons at lambda=64,128,256,512,1024 all verified R<=lambda^(-lambda) at those particular points; the theorem's uniform guarantee uses the proved conservative onset lambda>=1024. Compact log bounds are in the raw output; no giant rational outputs were printed. Finite verification alone does not prove the uniform asymptotic estimate.

## Reviews and preserved failures

* C1: coordinator exact-version review at ../reviews/coordinator-C1-review-v1.md; its broader family is independently analyzed by r1 T0 and blind r3 work, as reconciled by coordinator.
* C2: full nonblind author-distinct review at ../r1-theory/review-C2-v1.md with exact input hashes. No mathematical defect found; a source-code materialization wording issue is clarified in implementation-scope-v1.md.
* T0: my complete nonblind exact-version review is review-T0-v1.md, with T0-review-inputs-v1.json. It checks return moments, density domination under Q_k, c6/c12 counts, the N>=1000 constant, adaptive witness budget and repeated-request quantifiers. No mathematical defect found. I later inspected ../r1-theory/results-T0-v1.json from passed J003 (0.6665690129157156s): N=2..7 return DPs, exact mask/channel checks, CP-1 rejection, invalid L=r counterexample and boundary regressions pass. I did not claim to execute that source-author checker independently.
* check_candidates_v1.py is preserved but MUST NOT RUN: source review caught its factorial(N)/factorial(N-2m) implementation at huge N before any execution. checker-v1-rejection.md records this resource-plan failure; v2 uses the exact 2m-factor falling product. No bounded job failed and no truncation was accepted.
* C1-v1's finite-family random-bit bound needed log L for choosing positions; the immutable erratum preserves that correction. No theorem-law or schedule change followed.
* All earlier controls, non-iid conjugated old noise tuple, exact global-vs-connected distinction, parity, pair attenuation and same-noise requirement remain mandatory. The role did not claim fresh certification of the snapshotted source report. An unsolicited r1 outline arrived only after C1 was frozen; its presence is disclosed, and this role makes no blind-review claim. No information was forwarded from r1 to blind r3 by this worker.

## Recommendation and remaining uncertainty

Deprioritize both frozen candidates. Further Hurwitz runtime tuning cannot fix C2's planted support; sparse replacement with k=o(m) leaves its support threshold far below the global reference. A future construction must first reconcile global support/orbit statistics and must avoid a positive density of short identity witnesses after its declared scrambling. Whether a different efficiently generated structured law can meet both obligations and survive M0 remains unresolved. No third candidate or new campaign is proposed here.

Claim-level status, assumptions, evidence, review scope and action are in claim-ledger-v1.json. Full candidate algorithms and proofs remain separate immutable artifacts. Coordinator must reconcile full reports before final campaign acceptance, and may finish the bounded viability study as a scoped negative outcome without declaring the general research problem solved.
