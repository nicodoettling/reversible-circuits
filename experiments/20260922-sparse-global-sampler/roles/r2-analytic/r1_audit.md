# Nonauthor audit of R1 proof v1 — R2 referee

Audit completed 2026-09-22 05:57 UTC. Exact input snapshot: r1_proof_v1_review_input.md. SHA256: 43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0. Capture and independent-work hashes: review_manifest.json. This audit began after R2's independent proof and report were frozen. The parent disclosed preliminary agreement and requested particular checks; therefore this is a nonauthor review, not a blind review. Shared model/context lineage makes agreement correlated internal evidence, not human certification.

**Verdict: ACCEPT the analytic claims R1-C1.v1 through R1-C4.v1, and the T0/T1 analytic error corollary, as written in the frozen input.** No mathematical flaw or unresolved inequality was found. This verdict does not certify sampler implementation or its complexity, and does not replace the coordinator's full dependency/blurred-input/referee gate.

## Claim-by-claim review

1. **Law and marking.** The target is correctly U_(N,2k), with labels and factor positions distinguished. Normalization S=Z/(2k)! yields exact macro weight product A_g. Equation (1)'s label binomial and position binomial are correct; no equal-size component factorial is missing because one literal component is marked. R2's independent raw-word enumeration verifies every marked (v,ell) count in all required small cases.

2. **Imported recurrence.** Reopened the primary DYZ PDF. Proposition 1 Eq(13) and Eq(17), and the labeled-monodromy paragraph after Eq(20), support exactly C=v!ell!h. The minimal value is given immediately after Eq(28), PDF page 7. Eq(2)'s ordered degree splits, binomial(v,a), factor 2, cosh(at)-1 and a*b^2 powers are correct. Connected transposition support is equivalent to transitive generated monodromy. Rightmost-first versus reverse multiplication is transported by word reversal, which preserves identity and support data. No large-genus or large-degree asymptotic theorem is being applied outside its range.

3. **Factorial majorant.** Eq(5)'s normalized split coefficient simplifies to binomial(v,a)a^a b^(b-1)/[(v-1)v^(v-1)], as claimed. Its sum is one by the exact constant coefficient of Eq(2). The coefficient inequality (6) holds for every j>=0. B_v=(v^3-v)/36 satisfies B_v-B_a-B_b=abv/12>=a^2/12 for every positive ordered split. Formal nonnegative power-series multiplication justifies the inductive bound and does not assert stochastic independence. There is no need for an analytic convergence hypothesis.

4. **Conditioning ratio and reverse multiplicity.** A cost-(k-q) base on the complement of the fixed V embeds by isolating V. It has at least N-2k+2q isolated labels. An unordered matching contributes exactly (I)_(2q)/(2^q q!) choices; multiplying by pair weights 2^(-q) yields denominator 4^q q!. The reverse object is the subset of q minimal size-two components removed from beta, so its multiplicity is <=binomial(k,q). The extra V condition removes preimages and cannot increase this count. Incidence weight equals w(beta), not w(alpha), and the proof uses exactly that weight. The ratio remains valid at q=0, and all denominators are positive because 2k<=N. This is an endpoint-conditioned exact count comparison, with no guessed return-probability factor.

5. **Tail estimate.** Feasible v satisfy v<=k+1. The bound B_v x<=v a follows from v^2-1<=k(k+2), with a=k^2(k+2)/(9D^2). The finite genus sum can be extended to an exponential since all terms are nonnegative. The factorial estimate and geometric tail in Eq(9) retain the helpful (J+1)^(-3) factor correctly. H0's excluded intersection is a subset of the event bounded here, so the stronger tail applies directly.

6. **Effective threshold and negligible quantifiers.** At N>=2^160, L=log N>100. Under m^3<=N^2, the displayed a<=5/18, c<8, rho<=64N^(-1/3)<=N^(-1/6)<=1/2 are valid. The cutoff witness floor(2L/log L) is admissible and at least L/log L. Finally 1/6-1/10=1/15 and log L<=L/20 for L>=100 give L^2/(15log L)>=(4/3)L>=L+log16. Thus eta=exp(-L^2/[10log L]) is valid uniformly through T1, implies T0, and is negligible with one fixed function. Small N use eta=1; no exponent-dependent algorithm is introduced.

7. **Boundaries.** m=0, m=2, N=1, N=2 and odd m are classified correctly. K>=2 for N>=2 makes repeated-edge words allowed at every even length. Positivity of the restricted count is therefore sound. No approximation of invalid words is permitted or used.

## New targeted falsification after review began

Command:

    python3 -B experiments/20260922-sparse-global-sampler/roles/r2-analytic/audit_r1.py

Environment: Python 3.12.3, standard library, deterministic exact integer/rational arithmetic, no seed and no old experiment import. Results: r1_audit_results.json. Runtime under two seconds; this was a bounded small check, not a heavy grid.

- Enumerated weighted component macros directly for N=2..7, k=0..floor(N/2), q=0..k, and every removed-set size (fixed first labels, with all other fixed sets equivalent by relabeling).
- Checked every forward matching extension against the explicitly reconstructed reverse deletion count, retaining the V-isolate requirement. All 237 parameter cells and 8,107 extension incidences passed exact equality and the binomial(k,q) upper bound. Largest observed reverse degree was 3.
- Independently assembled exact total and size-restricted counts through N=1024,m=14, using only component sizes <=8 (complete at that length). At N in {16,32,64,128,256,1024}, tested R1 Eq(9) against exact large-component mass for each applicable m and J<=6. Exponentials were replaced by the rigorous rational upper bound exp(1+a)<=[100/(99-a)]^100 when 1+a<100. There were 45 cases with bound below one, all passed. The source/output record includes every tested nonzero tail as an exact rational.

The finite checks target reverse multiplicity and the stronger size-only event, rather than rerunning just the inherited zero-tail smoke cases. They provide falsification evidence; the universal result rests on the reviewed proof.

## Objections and limitations retained

No blocking mathematical objection was found. Two nonblocking presentation/provenance points:

- The frozen input's stated 05:55 freeze minute was guessed; parent supplied the actual creation time 05:52:41 and preserved the discrepancy in R1 freeze_manifest.md. The audit preserves the original bytes/hash rather than silently repairing the input.
- “A doubled spanning tree” should be understood as adjacent repeated tree edges (or a word followed by its reverse), which supplies the stated identity word. This is a wording clarification, not a failure of the existence claim.

The sequential cached-prefix regression is not applicable: no step multiplies conditional or marginal random-event probabilities. The proof instead uses deterministic weighted incidences and coefficientwise positivity. Future rewrites must preserve that distinction.

## Accepted scope

The analytic graph is closed at this version, conditional only on the checked imported DYZ exact count theorem. Global sampling certification still requires the exact connected primitive/assembly and polynomial bit-cost arguments, plus remaining full-run review gates. Failure of a larger-length bound would not imply sampling hardness.
