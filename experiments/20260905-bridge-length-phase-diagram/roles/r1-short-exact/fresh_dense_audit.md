# Fresh nonauthor audit of the dense theorem

Auditor: R1 short-exact context, after author-freezing its own research report.
Target: the final/frozen R2 report, inspected beginning 2026-09-05 15:36 UTC.
Status: **final; accept**, 2026-09-05 15:46 UTC.

## Verdict and scope

**Accept Theorem D, including the epsilon corollary, relative to its explicitly imported proved star-completion and spectral inputs.** I found no substantive mathematical objection. The new bridge-conditioned survival lemma correctly improves the historical factorial conditioning loss to a factor at most 3r. Floors, ceiling slack, denominator, parity, nonempty support, rank-four base, telescope, and bit complexity are all accounted for.

This was performed after the R2 report was declared final; I did not author or edit its proof or code. The proof audit independently rederived equations (D3)-(D19). A separately written exact-arithmetic script uses the R1 cut-and-join completion recurrence and a new backward group-walk computation for star coefficients, rather than the author's full labeled completion-table implementation.

The accepted theorem is:

    q=floor(m/[2N(N-1)]) >= 4 ceil(log_2 N), N>=5
    implies TV <= min{1,3N^2 exp(-q/144)}

for every feasible endpoint, with exact requested length and product, and expected polynomial Turing time in N,m. Consequently

    m >= 2N(N-1) ceil(144 log(3N^2/epsilon))

is a proved expected-polynomial epsilon regime. This is not arbitrary-accuracy sampling at fixed N,m, and is not a mixing theorem for a chain on words. The retained theorem's error floor and expected-time qualification must remain explicit.

## Line audit

| item | independent derivation/check | disposition |
|---|---|---|
| Rational floors D3-D4 | The decreasing tail sum is at most 2/sqrt(5)<1. Thus c_N<2; its unrounded floor argument is strictly below the integer 2qN(N-1), so taking a ceiling remains at most that integer, which is at most m. The same global q is held fixed at every recursive rank. | accept |
| Exact disintegration D5 | Stable sorting gives old endpoint h and star endpoint z with g=hz. Hence z=h^-1 g and h=gz^-1. The sum counts actual words, including all binomial interleavings. | accept |
| Token projection D6-D7 | The condition that h fixes r is z(g^-1(r))=r. The two-state recurrence counts words from the specified token to the pivot; reversing applied factors produces displayed rightmost-first words. Every star word has one endpoint, so Z<=b^k. | accept |
| Common scale in D8 | In the old-long half, flatten A to 2d^s/(r-1)!; in the star-long half flatten B to 2b^k/r!. Multiplying both halves by r!/2 gives exactly the displayed integer weights. Missing a factor r would be an error, but the report retains it. | accept |
| Smoothing D9-D10 | q>=4 ceil(log_2 N) implies q>=4 log r. The star exponent is at most r log r-L/[2(r-1)]<=-qr/4. The old exponent is at most r log r-L/(r-2)<=-3qr/4. Both bounds include the ceiling/floor midpoint choices and factorial prefactors. | accept |
| Endpoint denominator D11 | Full-rank nontrivial radius is 1-2/(r-1). The parity-relative error is at most exp(r log r-2L/(r-1))<=exp(-7qr/4)<1/2. Multiplying the parity-uniform mass 2/r! gives the lower count M^L/r!, uniformly over the correct parity class. | accept |
| Ceiling gap D12-D13 | p ceil(x)-ceil(y)>=px-y-1. Here px-y=q(r-1)(r-2)/(r ceil(sqrt r)). The inequalities (r-1)(r-2)>=r^2/2 and ceil(sqrt r)<=3sqrt r/2 hold from r=6. Thus the gap is at least qsqrt(r)/3-1>=qsqrt(r)/4 since qsqrt(r)>=12. | accept |
| Binomial Bernstein D14-D15 | At the least retained parent length, the star mean is at most 4qr. At t0=qsqrt(r)/4, the denominator is at most (97/12)qr<=9qr, giving exponent at least q/144. Larger parent lengths reduce the old-count lower-tail event by Bernoulli coupling. | accept |
| Bridge conditioning D17 | All discarded branches are old-long, so old completion counts are smoothed even though discarded child floors need not hold. Summing B_k(h^-1g) over h exactly gives Z_r(k,x); no independence is assumed after conditioning. The old-side factorial normalization cancels all but r against the endpoint denominator. | accept |
| Retained support | Every generated old-long h has parity (-1)^s and s>=L/2>=r-2. Retained children also satisfy the next floor. Every star-long endpoint has positive exact count because its pointwise relative error is strictly below one. The all-star branch is retained and nonempty even when the final error bound is vacuous. | accept |
| Rank-five and rank-four base | There is no cutoff at rank five, and every rank-four-or-smaller child is solved by a constant 24-state-or-smaller exact backward DP for arbitrary lengths. There is no parameter-dependent finite-rank exceptional table hidden in the proof. | accept |
| Retained comparison D18 | On the retained set, all exact/flat unnormalized likelihood ratios still lie in [1-Delta,1+Delta]. Normalization therefore costs at most Delta/(1-Delta) in TV. Conditioning the exact law on retention costs its exact discarded mass b_r. | accept |
| Telescope D19 | Only old-long branches have a child; their domain is retained at rank r-1. Exact reconstruction contracts TV. Taking a supremum over every retained length and feasible endpoint is legitimate because all bounds are uniform. Star-long branches terminate. | accept |
| Final constants D1-D2 | The cutoff sum is at most 2N^2 exp(-q/144), and the smoothing sum is at most N^2 exp(-q/144). The epsilon threshold makes q large enough for both accuracy and the logarithmic precondition. | accept |
| Arithmetic | Floor denominators have O(N log N) bits. Branch weights have O(L log N) bits. The positive star coefficient formula has polynomial-bit common denominators. A single star-long termination plus polynomial-many token, old-word, and stable-sort operations preserves polynomial Turing time. | accept |

## Decisive lemma, expanded independently

Let E be the set of discarded old-long k, and let s=L-k. The numerator of its exact bridge probability is

    sum_(k in E) binom(L,k) sum_h A_s(h) B_k(h^-1 g).

Whenever B_k(h^-1g)>0, endpoint parity forces sign(h)=(-1)^s, so the old completion upper bound applies. It does not need to hold on wrong-parity h, whose star coefficients are zero. Since s>=ceil(L/2),

    numerator <= [2(1+Delta)/(r-1)!]
                 sum_(k in E) binom(L,k)d^s Z_r(k,g^-1(r)).

Use Z<=b^k and enlarge E to the entire old-count event A<B_(r-1). The resulting sum is M^L Pr[A<B_(r-1)]. Division by M^L/r! leaves

    b_r <= 2r(1+Delta) Pr[A<B_(r-1)]
        <= 3r exp(-q/144).

All signs of inequalities are in the required direction. The endpoint denominator need not be close to its expectation in a conditional probabilistic sense; it is a direct pointwise count bound. This avoids the invalid shortcut of treating factor types as independent after endpoint conditioning.

## Exact falsification attempts

Command:

    python3 experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/audit_dense_independent.py

Environment: Python 3.12.3, standard library, no random seeds. The script writes only this auditor's role directory. Machine-readable output is fresh_dense_audit_results.json.

* **25,228 exact rational floor cases**, including ranks immediately below and above powers of two and square-root ceilings through top rank 513, with the least admissible q and additional q values. The smallest squared ratio of actual floor slack to the claimed slack was about 3.29218, exceeding one.
* **Every feasible labeled endpoint at rank six**, q=12, L=B_6=380 and L=381. This checks both even and odd parent lengths, all 720 combined endpoints, the exact D11 denominator, and the exact D17 numerator. The old child floor was 240 in both cases. Maximum discarded mass was approximately 0.0670209182764 at L=380 and 0.0584809765024 at L=381. Exact conditioning ratios relative to the unconditioned tail were below one in these cases; the proof only claims the looser uniform 2r(1+Delta) bound.
* **Full one-rank exact comparison at rank five**, q=12,L=240, for all 60 feasible labeled endpoints. Across 173,520 joint (k,h) branches, the script checks exact normalization, support equality, the common scaling of both halves, every pointwise likelihood ratio, the token projection, and the exact TV inequality. Maximum actual TV was about 6.23654e-19; the claimed Delta/(1-Delta) bound was about 4.50054e-14.

All checks passed in 3.46 seconds. Decimal summaries are not used to decide inequalities; comparisons are exact integers or Fractions. The type-based all-transposition completion counts are a distinct representation from the author's labeled endpoint tables. These checks are falsification attempts and do not replace the proof for general rank.

The user-required S3,m4; S4,m4; S4,m6 and boundary tests are already independently covered by the frozen R1 implementation, with exact word masses and endpoint conventions. For the dense audit I additionally checked the mathematical exceptional branches: m=0, odd identity lengths, m=2, N=2, N=1 if admitted, minimal arbitrary endpoint length, and pair padding. The dense theorem makes no unsupported claim on inputs below its precondition; padding is used only for feasibility.

## External inputs and translation scope

The audit accepts the following explicit dependencies:

1. The product-preserving stable-sort bijection, locally proved in manuscript (RR.3)-(RR.5). Its old/star orientation matches the report.
2. The exact positive prescribed-endpoint star sampler, manuscript (RR.6)-(RR.8), based on Féray, Partial Jucys-Murphy elements and star factorizations, Proposition 1.1, Theorem 1.2, Lemma 3.1, arXiv:0904.4854v2. The exact-support subset decomposition and pivot treatment must remain in the implementation.
3. Caputo-Liggett-Richthammer, Proof of Aldous' spectral gap conjecture, Theorem 1.1, DOI 10.1090/S0894-0347-10-00659-4. Normalizing the complete-graph and star one-particle gaps by edge count gives the stated discrete-time gaps. Sign conjugation pairs positive and negative eigenvalues, so the same nontrivial absolute-radius bound applies after removing constant and sign vectors.

I inspected the relevant manuscript, the named historical retained-rank report, and the local star-completion implementation. Its positive truncated power series has O(r) factors; the product of O(r) denominators each dividing 2^L(L+1)! has O(rL log(L+1)) bits, plus polynomial-size factorial factors. Positive sums and products therefore do not hide exponential bit growth. The declared arithmetic-operation bound is an upper bound, not a claim that arithmetic is unit-cost.

I did not freshly fetch the primary papers. Their source reconciliation belongs in the coordinator's dependency audit. Accordingly this report certifies the new parameterization and proof chain relative to the explicitly named imported inputs; it does not silently upgrade a source citation into a freshly re-proved external theorem.

## Objections, qualifications, and action

Numbered substantive objections: **none**.

Nonblocking qualifications:

1. Preserve expected polynomial Turing time in the theorem statement. Exact integer-range rejection is not bounded worst-case runtime. If desired, the coordinator can apply the already audited capped-randomness/fixed-valid-word argument with an allocated additional error budget.
2. Preserve the fixed-length error floor: the dense algorithm alone is not shown to attain epsilon smaller than 3N^2 exp(-q/144) at the same N,m.
3. The independent exact checks validate formulas and finite laws, not a complete production implementation of the new dense recursive sampler. The algorithmic existence proof is the reviewed positive pseudocode plus its imported exact primitives.
4. Do not claim a hardness threshold from the uncovered sparse-to-dense interval.

Action: **promote the density-parameterized theorem to the coordinator's audited phase diagram**, retaining the imported dependency list, expected-time qualification, and uncovered accuracy band. The most valuable human-review target remains the short numerator proof above, together with the external star-count formula's convention translation.

role: fresh nonauthor audit by r1-short-exact of r2-dense-threshold
claim: Theorem D and the dense epsilon corollary survive a fresh proof audit and independent exact falsification attempts.
status: proved
parameter_regime: N>=5, q=floor(m/[2N(N-1)])>=4ceil(log_2 N), every feasible endpoint; ranks <=4 exact.
target_distribution: Uniform on Omega(N,m;g); public endpoint e.
runtime: Polynomial expected Turing time in N,m, with polynomial-bit exact arithmetic; no worst-case exact random-bit claim.
error: Endpoint and length error zero; TV<=min(1,3N^2 exp(-q/144)).
assumptions: Explicitly imported stable-sort, Féray star-completion, and CLR spectral inputs; independent fair random bits.
evidence: This line audit, audit_dense_independent.py, fresh_dense_audit_results.json.
independent_checks: 25,228 floor cases; 720 parity-spanning rank-six endpoints for exact D11/D17; 173,520 rank-five joint branches for exact support, likelihood ratios, normalization, and TV.
first_unproved_step: Positive connection sampling beyond the retained dense domain, or another primitive covering the intermediate and smaller-error band.
verdict: promote
