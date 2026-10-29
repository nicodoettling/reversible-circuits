# LC1 proof v1 — provisional, exact-version review pending

Statement: local-channel-statement-v1.md. Target in this campaign: global fixed-length bridge versus a candidate law under M0; proof itself is alphabet-general. Composition of gate permutations is irrelevant to this lemma.

For j in [s], E_j averages coordinate j against uniform mu while keeping other coordinates fixed. The E_j commute, are idempotent and are contractions in the supremum norm. Define

 f_S = (product_(j in S)(Id-E_j)) (product_(j notin S) E_j) f.

The identity Id=E_j+(Id-E_j), multiplied over all coordinates, gives f=sum_(S subset [s]) f_S, and E_j f_S=0 if j in S and =f_S otherwise. Also ||f_S||_infty<=2^|S| since ||f||_infty<=1. These are pointwise function identities; no source law or conditional independence assumption about word coordinates is made.

The restricted replacement operator T acts on functions: Tf(x)=E[f(Y_I)|W_I=x]. This conditional law depends only on x because the global replacement subset and fresh symbols are independent of the complete original word. For each realized replacement subset J, E_J f_S vanishes if J intersects S, and otherwise is f_S. Thus T f_S=alpha_|S| f_S, since the probability that a uniform k-subset avoids |S| specified positions is alpha_|S|. Uniform-subset sampling is used exactly; no independent-coordinate/Bernoulli substitution occurs.

Because k<=L-s, alpha_s>0, and all alpha_j>=alpha_s. Define g=sum_S f_S/alpha_|S|. Then Tg=f. The uniform bound ||g||_infty <= sum_S 2^|S|/alpha_s=3^s/alpha_s=:C holds pointwise. Set h=(g+C)/(2C), which lies in [0,1]. For either source law V,

 E_(Q_k V) h = (E_V f+C)/(2C).

Subtract the two identities to obtain LC1. This uses linearity and a conditional expectation with a source-independent replacement law. There is no sequential multiplication of marginal probabilities. In particular the cached-prefix counterexample CP-1 does not supply a failure: the operator is computed conditional on the entire fixed source tuple, with exact hypergeometric subset weights.

Computation expands each projection into at most 2^s sums, averaging at most q^s tuples per sum. Across 2^s subsets, O(4^s q^s) evaluations suffice. Binomial coefficients have O(L) bits, or can be evaluated as length-s falling-factorial ratios for alpha_j. Rational arithmetic has polynomial bit growth in L,s,log q and the bounded rational descriptions of f outputs (a polynomially evaluable rational f must have polynomial bit output). Generate an exact Bernoulli rational h using uniform integer rejection, expected <2 attempts per rejection level and O(bit length) expected bits per integer draw. No fixed finite fair-bit tape exactly samples every rational denominator; claims of worst-case exact finite-bit generation are intentionally excluded.

Boundaries: k=0 gives alpha=1 and T=Id; k=L-s permits alpha_s=1/binom(L,s), positive but possibly tiny; k>L-s annihilates the top s-coordinate component, so the inversion premise is necessary for a universal version. q=1 forces all nonempty components zero and no source bias. s=0 is constant. Odd L is outside M0 but irrelevant to the general alphabet statement. N=2 gives q=1. In M0 L=0 has only the empty word.

Dependencies: elementary commuting conditional-average operators, exact uniform-subset counting, rational arithmetic. No literature theorem. Outstanding gates: finite rational verification for small alphabets and all boundary k; author-distinct exact-version review; explicit final use in candidate synthesis. A finite check cannot prove the universal identity.
