# Full nonblind review of T0, version 1

Reviewer: /root/r2_construction, 2026-10-29. Exact input hashes are in T0-review-inputs-v1.json. Inputs were frozen statement-T0.md and proof-T0.md, plus M0 model-v1.md. No source edits were made. This reviewer authored different construction-side proofs and had seen an unsolicited early outline of the surviving-window idea. The review is author-distinct and NONBLIND; agents use the same model and their assessments are correlated. It is not human certification.

**Verdict:** mathematical review PASS for the exact T0 statement and proof, with coordinator acceptance still pending finite-regression and other referee gates. I found no counterexample or missing load-bearing hypothesis. This is a review verdict, not authorization to upgrade unrelated candidate/security claims. The acceptance scope is the stated bounded-scrambling relator family, not general noise-hiding impossibility.

## D1: return moment ratio and pointwise maximum

The symmetric Cayley kernel is diagonalizable with eigenvalues in [-1,1]; passing to even times makes all theta_j^2 nonnegative. The moment sequence a_s=p_(2s)(id) is positive, including a_0=1. Cauchy--Schwarz gives log convexity and monotone adjacent ratios. The exact index translation is correct: r=2d, L=2n, L>=2r means n>=2d, so every ratio index n-d,...,n-1 is at least its corresponding d,...,2d-1 index. Inverting positive ratios yields p_(L-r)/p_L<=p_r/p_(2r), in the stated direction. No false odd-time maximum is used. The off-diagonal even-time maximum follows from the two equal l2 norms and translation bijection.

## D2: local bridge law and matched replacement

Cyclic rotation is a literal-word bijection preserving identity and uniformity, so a fixed consecutive r-window can be counted as the first r gates. Completion count is precisely q^(-r)p_(L-r)(h^{-1})/p_L under GLOBAL U. The proof correctly restricts r and L to even values, making the completion length even. The pointwise density bound nu<=R rho uses the even-time maximum and D1. Every fixed-coordinate replacement channel is positive and preserves iid rho; therefore nu K_J<=R rho is valid after applying it. M0's independent subset I allows conditioning on I without tilting the old word. Averaging over I then gives the claimed noisy-window bound. Conditioning on the event that a window survives is never done. This is the load-bearing bridge-to-noisy-reference step, and it is sound.

## D3/D4: exact endpoint classes and the numerical constant

For three transpositions, the possible odd endpoints have distance 1 or 3, hence only types 2,4,3+2,2+2+2. The enumerated per-endpoint counts q+6(N-2)+2 binom(N-2,2), 16,9,6 are correct by splitting with the last transposition. Class sizes q,6 binom(N,4),20 binom(N,5),15 binom(N,6) are correct. Squaring these counts gives the stated c6 formula. As a hand check, at N=4, q=6 and A=20 give 2400+1536=3936; at N=3 the value is 3*9^2=243; at N=2 it is 1.

The c12 lower count has no overcount: each returned word uniquely identifies its six equal-edge pairs. There are 12!/(2^6*6!)=10395 pair partitions, and assigning ordered vertex-disjoint unordered edges to canonically ordered position pairs gives (N)_12/2^6. The product is exactly (10395/64)(N)_12. Other identity words are omitted, which makes the inequality valid in the required direction.

The displayed c6 polynomial majorant expands correctly: its N^6 coefficient is 9/8+3/4=15/8, N^5 coefficient is 3/4+27/2=57/4, and N^4 coefficient is 1/8+64=513/8. The falling-factorial product bound uses sum_{j=0}^{11}j=66, so at N>=1000 it is >=467/500. Finally 40*(19/10)^2=722/5 is strictly less than 4854465/32000. Thus beta_N<1/40 is correctly established with that finite onset. No asymptotic estimate replaces these exact comparisons.

## D5/D6: witness budget, setup and repeated requests

Rotating a partition into M length-six intervals discards at most one wrapping interval. A move changes only two coordinates, each meeting at most one retained disjoint interval; B arbitrarily chosen, possibly adaptive moves can therefore destroy at most 2B witnesses. A k-subset hits at most k more witnesses. This is deterministic and survives arbitrary setup/source correlations; it does not multiply survival probabilities. The resulting H is a valid lower bound, though deliberately loose.

For the reference, summing L-5 window marginals and applying Markov is valid even though windows overlap. If H>=M/2, the bound is strictly below (6M)/(M/2)/40=3/10. The per-key structured acceptance is pointwise one; the reference global U is independent of setup under M0. The one-sample distinguishing advantage is therefore at least 7/10. For a fixed t, the reference replies are actually independent conditional on the same exposed setup with fresh word/noise tapes; this conditional product law justifies (3/10)^t. No conclusion is drawn from marginal bounds alone.

The cached-prefix CP-1 failure cannot invalidate this proof: its 21/2000>1/100 multiplication is explicitly forbidden by the proof's structure. The sole multi-request product is justified by actual fresh conditional product law, with no adaptive posterior selection or oracle cache. This is a conceptual probability-regression check; the campaign's dedicated executable CP-1 regression remains separate.

## D7: parameter, runtime, candidate membership and boundaries

For lambda>=32, N=lambda^2>=1024; B=floor(N/8) gives H>=3N/4-lambda-1>=N/2. All counts and k<=L are feasible. The semantic error 4/lambda is correctly called inverse polynomial, not negligible. A six-gate window needs only its at most twelve incident labels, so O(L) label operations and O(L log N) bit work are plausible; counting can use amortized binary increments and a final threshold comparison. Runtime is explicitly not logarithmic-wire efficiency.

C1-v1's six-distinct-edge blocks and signed adjacent Hurwitz updates fit T0 after mapping its block-count B to T0's M and its steps s to T0's B. T0's direct schedule differs from C1-v1's principal dense schedule, which is harmless: C1's finite family admits both, and its principal schedule also has H>=M/2 for all sufficiently large lambda. The source's optional conjugation/rotation only broadens the theorem; C1 uses neither. No claim that arbitrary generators in the theorem class run efficiently is smuggled into test complexity.

N=2 correctly gives identical words and a vacuous constant; L=0,2 lie outside construction; odd L is infeasible; L=6 must be excluded from r=6 local domination, because at k=0 its entire window is identity with probability one. The proof explicitly retains this counterexample. At k=L, H<=0 and both sources are iid. The H<=0 and large-scrambling regimes remain unclaimed. These boundaries match M0.

## Remaining acceptance tasks

The coordinator should attach the exact T0 bounded-check output and blind/nonblind referee reports, then reconcile statuses. My role's separate candidates_v2 bounded job verifies C1/C2 identities, all signed local moves on mandatory global small spaces, and sparse-support arithmetic, but is NOT a complete independent execution of T0's moment/count checker. No change to T0 is requested. If T0 or a load-bearing dependency is edited, this review does not automatically cover the revision.
