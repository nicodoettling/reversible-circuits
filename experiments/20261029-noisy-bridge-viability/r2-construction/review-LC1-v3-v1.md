# LC1-v3 final fresh exact-version review

Reviewer /root/r2_construction. Complete frozen v3 statement and proof were read afresh, with exact hashes in LC1-v3-review-inputs-v1.json. This report does not inherit acceptance from v2. The previous review's remaining efficiency qualification and the original v1 denominator flaw remain preserved. Author-distinct, nonblind, same-model correlated review; no independent human certification.

**Verdict: PASS for the exact LC1-v3 mathematical statement, arithmetic bound, and explicitly scoped efficient corollary.** No remaining mathematical defect or missing computational-input premise was found. The targeted distinct-denominator regression passed in coordinator J005 and is inspected below. Coordinator owns final campaign reconciliation and acceptance; no construction security claim follows from this lemma.

## Fresh mathematical verification

For every coordinate, E_j is an idempotent product-uniform averaging operator; distinct E_j commute. Multiplying Id=E_j+(Id-E_j) gives the full decomposition f=sum_S f_S. The conditional source distribution plays no role in this deterministic identity. A replacement in a coordinate of S kills f_S, and replacement outside S preserves it. Since M0's global k-subset is independent of the word, the exact eigenvalue is alpha_|S|=binom(L-|S|,k)/binom(L,k), not a Bernoulli-noise power.

The condition k<=L-s ensures alpha_s>0 and alpha_j>=alpha_s, so the declared inverse g=sum_S f_S/alpha_|S| is well defined and satisfies Tg=f for every tuple. Sup-norm contraction of E_j and norm bound two for Id-E_j give ||g||<=sum_S 2^|S|/alpha_s=3^s/alpha_s. Therefore the declared h is pointwise in [0,1], T preserves its constant shift, and source expectations differ by exactly alpha_s/(2*3^s) times the original signed bias. All steps are valid for arbitrary dependent source words. The proof neither selects a hidden noise pattern nor multiplies posterior marginal bounds; CP-1 is not a counterexample.

I rechecked the finite domains: q=1 and s=0 have no source bias; k=0 gives the identity channel; k=L-s gives a positive eigenvalue possibly too small for efficiency; k>L-s can erase the full s-coordinate component and is rightly excluded. General alphabet odd L is meaningful while M0 odd identity length is empty. The public-setup application fixes f and I from A before the source/noise draw and does not grant access to a secret-dependent test. Reused-setup amplification is expressly not claimed without additional key-wise premises.

## Fresh arithmetic and computational-interface verification

Expanding 2^s projections into at most 2^s averaging sums and evaluating at most q^s tuples in each gives the stated O(4^s q^s) oracle-evaluation count. Across the entire local domain there are only q^s distinct rational values. The product D of their denominators has at most q^s b bits; each coordinate average has denominator dividing D q^s. A common denominator for reciprocal eigenvalues is obtained by multiplying (L-k)_j for j=1,...,s, costing O(s^2 log(L+1)) bits. Forming h adds only O(s log(L+1)+s) bits. Supremum bounds control intermediate numerators in a deliberate common-denominator implementation. Hence the displayed operand bound is sufficient; it explicitly permits exponential growth in variable s.

The exact v3 statement now places all necessary assumptions next to its M0 efficient corollary: fixed s; polynomial N,L; publicly computable positions; a uniform polynomial-time f evaluator with polynomial-bit rational outputs, or a charged explicit polynomial-size table. This closes my v2 qualification. It no longer treats an arbitrary rational f as free oracle access or free nonuniform advice. The proof's example f=1/2^(2^lambda) correctly illustrates why the b premise matters: its explicit denominator needs 2^lambda+1 bits. Such an f is excluded from the efficient corollary but remains covered by the finite algebraic identity.

With those assumptions, both q^s b and every other operand/evaluation bound are polynomial in lambda, so exact rational acceptance can be sampled in expected polynomial time by unbiased-bit rejection. The statement correctly distinguishes this from a worst-case finite exact bit tape. If k/L<=1-c with fixed c>0, fixed s, and L>=2(s-1)/c, then each factor (L-k-i)/(L-i)>=c/2 for 0<=i<s; thus alpha_s>=(c/2)^s, verifying the stated constant-noise-fraction example. No extra cryptographic assumption is imported.

## Targeted finite evidence inspected

The coordinator's immutable final-decisive-v1.json reports status passed, Python 3.12.3 stdlib, deterministic exact arithmetic, commit 24649e0a2b4fa0d0ede444234bfedfc428453571, elapsed 0.12285355105996132s under bounded J005. For q=2 and s=1,...,6, its distinct-prime denominator fixtures retain every distinct prime in the mean denominator. The mean denominator bit lengths are 4,13,37,90,216,497 while maximum individual denominator bit lengths are only 3,4,6,7,8,9. This directly exercises the repaired accounting rather than assuming a per-value bit bound survives summation unchanged.

For s=1,...,4, the same fixture checks the exact inverse identity and common denominator for h; all pass. This is finite falsification evidence for the implementation and repair, not a proof for all s. The universal bound is justified by the explicit common-denominator argument above. The file also retains independent decisive global-bridge count reruns relevant to other campaign claims; they are not dependencies of LC1.

## Closed and residual scope

The v1 arithmetic omission and v2 efficient-interface omission are both repaired and explicitly rechecked in v3. No additional edit or experiment is requested. The proof retains a historical sentence naming outstanding v2 gates; current acceptance is governed by this exact v3 review and coordinator synthesis, not that historical process label. Any later edit of a load-bearing statement or proof invalidates automatic use of this report.

LC1 is a finite local-observable transfer lemma. It does not establish that any particular sampler has an accessible local bias, choose an advantageous hidden-key test, prove full-word pseudorandomness, or decide the general sparse-noise hiding problem. Those limitations remain explicit in v3.
