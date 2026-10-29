# LC1-v2 fresh exact-version review

Reviewer /root/r2_construction, author-distinct and nonblind. Exact input hashes: LC1-v2-review-inputs-v1.json. I read the entire v2 statement/proof, not only the repair note. Same-model reviews are correlated. This is a new assigned review after my construction report froze; it does not alter either candidate or T0.

**Verdict:** KEEP the exact channel identity, normalization, domains, evaluation-count bound, and repaired operand-size bound. No mathematical defect was found in those claims. The efficient M0 corollary needs one explicit input-cost qualifier before unqualified uniform-polynomial-time acceptance: f must be efficiently evaluable (or its finite table must be provided), and b must be polynomial in the security parameter. The proof already states polynomial q,L,b for its efficiency discussion; the statement's short M0 paragraph does not expressly include b or f-evaluation cost. This is an efficiency-quantifier clarification, not a probability counterexample and not a defect in the repaired q^s denominator accounting. A targeted distinct-denominator regression and coordinator reconciliation remain separate gates.

## Exact algebra and noise law

The commuting coordinate averages E_j form projections for the product uniform alphabet measure. Expanding Id=E_j+(Id-E_j) gives f=sum_S f_S pointwise. This decomposition is a deterministic function identity regardless of the source distribution. If j lies in S then E_j f_S=0; otherwise it is unchanged. Thus a realized replacement set erases exactly the components whose S intersects it. The probability a uniform k-subset avoids j fixed local positions is binom(L-j,k)/binom(L,k)=(L-k)_j/(L)_j. This is exact M0 hypergeometric counting; the independent-coordinate Bernoulli noise shortcut is not used.

For k<=L-s, every alpha_j>0 and alpha_j>=alpha_s. The operator inverse g=sum_S f_S/alpha_|S| satisfies Tg=f. Each (Id-E_j) has supremum norm at most two and each E_j at most one, giving ||f_S||<=2^|S| and ||g||<=3^s/alpha_s=C. Therefore h=(g+C)/(2C) is a valid [0,1]-valued randomized test. T preserves constants, so for either source law V its expectation is (E_V f+C)/(2C). Subtracting yields the exact coefficient alpha_s/(2*3^s) and preserves the signed bias. No reconstruction of the underlying sample is asserted.

No conditional source-coordinate independence is needed. The restricted channel conditional on the entire source tuple is source independent because the subset and replacement tapes are independent of the original word. The proof has no selected posterior stages, latent cache branch, or multiplication of marginal survival bounds; CP-1's 21/2000>1/100 counterexample does not challenge this operator calculation.

## Evaluation and arithmetic bounds

For each of 2^s subsets S, expanding the centered product creates at most 2^s coordinate-average terms. Each average can enumerate at most q^s tuples. Thus O(4^s q^s) evaluations is a valid loose upper bound. Only q^s distinct full-table values can occur.

If each f-value denominator has at most b bits, the product D of all distinct denominators has at most q^s b bits. This is the factor v1 had omitted, and v2 includes it. A coordinate average over a coordinates has denominator dividing D q^a, hence all such averages have common denominator D q^s. Inclusion-exclusion adds no new prime denominator factors. Dividing by alpha_j introduces denominator (L-k)_j; a common multiple obtained by multiplying these over j=1,...,s has at most sum_j j log(L+1)=O(s^2 log(L+1)) bits. Numerators (L)_j have only O(s log(L+1)) bits. Finally h=1/2+alpha_s g/(2*3^s) adds O(s log(L+1)+s) denominator bits, absorbed by the displayed bound. Sup-norm bounds and a common-denominator computation bound all intermediate numerator sizes by the same scale plus O(s log(L+1)+s).

Thus a deliberate common-denominator implementation achieves O(q^s b+s^2 log(L+1)+s log(q+1)+s) bits per operand up to constants. The statement says arithmetic CAN use this bound; it need not cover a careless implementation that repeatedly multiplies unreduced denominators. The q^s b term correctly accommodates pairwise unrelated denominators. Exact rational Bernoulli sampling by uniform integer rejection uses finite expected polynomial work in denominator bit length; a fixed worst-case fair-bit tape cannot generate every rational exactly, and the statement correctly excludes that claim.

## Efficiency qualifier and boundaries

The operator/evaluation theorem is an oracle reduction in f unless an evaluation algorithm or table is supplied. For fixed s and polynomial N,L, q^s is polynomial, but a very long rational output b or an expensive/uncomputable family f_lambda is not made efficient merely by having a small local domain. With an efficient f and polynomial b (or a polynomial-size explicit table), the repaired operand bound gives the intended uniform polynomial implementation and inverse-polynomial advantage whenever alpha_s and the original bias are inverse polynomial. The corollary should say these premises explicitly. This is not a request to change any alpha, advantage factor, source assumption or candidate law.

At k=0, T=Id and h rescales the original test correctly. At k=L-s, alpha_s=1/binom(L,s)>0, potentially too small for a useful efficient attack but algebraically invertible. For k>L-s the top component is annihilated, so excluding it is essential. For q=1 or s=0 all source biases vanish; N=2 and L=0 in M0 agree with these degenerate cases. The public-setup use is conditional on publicly fixed I,f; it does not grant an adversary a hidden-key-dependent observable. No generic reused-key amplification is asserted.

## Recheck disposition

Probability identity and arithmetic repair pass this exact-version review. The final computational corollary should remain scoped/conditional until the f-input and b assumptions are explicit. If a clarified version is frozen, a short author-distinct recheck of its actual full statement/proof against these input hashes can close this remaining wording obligation. No new experiment was launched by this reviewer.
