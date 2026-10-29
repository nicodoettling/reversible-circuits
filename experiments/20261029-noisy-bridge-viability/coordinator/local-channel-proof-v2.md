# LC1 proof v2 — REPAIRED-PENDING-RECHECK

Statement: local-channel-statement-v2.md. Version 1 is preserved; the only change is an explicit arithmetic bound including the number of distinct evaluated rational values. Target in this campaign: global fixed-length bridge versus a candidate law under M0; proof itself is alphabet-general. Composition of gate permutations is irrelevant to this lemma.

For j in [s], E_j averages coordinate j against uniform mu while keeping other coordinates fixed. The E_j commute, are idempotent and are contractions in the supremum norm. Define

 f_S = (product_(j in S)(Id-E_j)) (product_(j notin S) E_j) f.

The identity Id=E_j+(Id-E_j), multiplied over all coordinates, gives f=sum_(S subset [s]) f_S, and E_j f_S=0 if j in S and =f_S otherwise. Also ||f_S||_infty<=2^|S| since ||f||_infty<=1. These are pointwise function identities; no source law or conditional independence assumption about word coordinates is made.

The restricted replacement operator T acts on functions: Tf(x)=E[f(Y_I)|W_I=x]. This conditional law depends only on x because the global replacement subset and fresh symbols are independent of the complete original word. For each realized replacement subset J, E_J f_S vanishes if J intersects S, and otherwise is f_S. Thus T f_S=alpha_|S| f_S, since the probability that a uniform k-subset avoids |S| specified positions is alpha_|S|. Uniform-subset sampling is used exactly; no independent-coordinate/Bernoulli substitution occurs.

Because k<=L-s, alpha_s>0, and all alpha_j>=alpha_s. Define g=sum_S f_S/alpha_|S|. Then Tg=f. The uniform bound ||g||_infty <= sum_S 2^|S|/alpha_s=3^s/alpha_s=:C holds pointwise. Set h=(g+C)/(2C), which lies in [0,1]. For either source law V,

 E_(Q_k V) h = (E_V f+C)/(2C).

Subtract the two identities to obtain LC1. This uses linearity and a conditional expectation with a source-independent replacement law. There is no sequential multiplication of marginal probabilities. In particular the cached-prefix counterexample CP-1 does not supply a failure: the operator is computed conditional on the entire fixed source tuple, with exact hypergeometric subset weights.

Computation expands each projection into at most 2^s sums, averaging at most q^s tuples per sum. Across 2^s subsets, O(4^s q^s) evaluations suffice. Binomial coefficients have O(L) bits, or can be evaluated as length-s falling-factorial ratios for alpha_j. There are at most q^s distinct f values. If each numerator/denominator has at most b bits, take D to be the product of their denominators, so log2 D<=q^s b. Every coordinate average has denominator dividing D q^s. Writing alpha_j=(L-k)_j/(L)_j, multiplication of denominators (L-k)_j over j=1,...,s supplies a common denominator for all inverse components with O(s^2 log(L+1)) additional bits. Forming h additionally divides by 2*3^s and multiplies by alpha_s, which adds O(s log(L+1)+s) bits. The sup-norm bounds control numerator sizes by this denominator bit count plus O(s log(L+1)+s). Thus O(q^s b+s^2 log(L+1)+s log(q+1)+s) bits per operand suffice. Total exact bit work is polynomial in the number of arithmetic operations and this bit bound. For variable s, unrelated denominators can have product bit length exponential in s: the original v1 sentence omitting this factor was overbroad. Fixed-s polynomial efficiency when q,L,b are polynomial is unchanged. Generate an exact Bernoulli rational h using uniform integer rejection, expected <2 attempts per rejection level and O(bit length) expected bits per integer draw. No fixed finite fair-bit tape exactly samples every rational denominator; claims of worst-case exact finite-bit generation are intentionally excluded.

Boundaries: k=0 gives alpha=1 and T=Id; k=L-s permits alpha_s=1/binom(L,s), positive but possibly tiny; k>L-s annihilates the top s-coordinate component, so the inversion premise is necessary for a universal version. q=1 forces all nonempty components zero and no source bias. s=0 is constant. Odd L is outside M0 but irrelevant to the general alphabet statement. N=2 gives q=1. In M0 L=0 has only the empty word.

Dependencies: elementary commuting conditional-average operators, exact uniform-subset counting, rational arithmetic. No literature theorem. Version-1 algebra already passed 108 exact finite channel cases; its numerical identities are unchanged. Outstanding gates for v2: targeted distinct-denominator regression, author-distinct exact-version recheck, and final synthesis. A finite check cannot prove the universal identity.
