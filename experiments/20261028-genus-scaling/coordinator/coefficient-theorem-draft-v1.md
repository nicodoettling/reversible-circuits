# COEFF-EXP.v1 — coefficient recovery in single-exponential genus time

Author: coordinator, 2026-10-28. PROVISIONAL complete argument, pending exact nonauthor audit and finite checks. This draft is explicitly not certification of T0. Primary sources were opened directly; PDF screenshot retrieval was unsuccessful, so text/formula verification is claimed, not visual page verification.

## Statement and imported identities

For every integer h>=2 there is a uniform deterministic algorithm returning the full rational coefficient list of the GJV genus-h rational Hurwitz series in at most A0 C0^(h+1)(h+2)^a0 bit operations, for absolute constants. It uses only finite integer/rational arithmetic; no Hodge-integral software, advice depending on h, or oracle is required.

Let alpha=(a1,...,ak) list individual cycles of a fixed permutation on n=sum ai labels, r=n+k-2+2h. C_h(alpha) counts ordered connected transposition words of length r with that fixed endpoint, rightmost-first product. Put q(a)=a^a/(a-1)! and B_h(alpha)=C_h(alpha)/(r! product_i q(ai)).

Imported source P1: Goulden, Jackson, Vakil, *The Gromov-Witten potential of a point, Hurwitz numbers, and Hodge integrals*, revised22Dec2000, https://math.stanford.edu/~vakil/files/gjvfinal.pdf, Section2.3 equation(13), Section3.2 Theorem3.2 and equation(16). P1 is used as a published mathematical theorem, not reproved here. Its weighted-cover/fixed-permutation normalization is pinned by P2: Goulden–Jackson, *A proof of a conjecture for the number of ramified coverings of the sphere by the torus*, https://arxiv.org/pdf/math/9902009, Section2, namely cover count = C_h(alpha)/z_alpha, z_alpha=product ai times product multiplicity factorials. This translation was reviewed in prior I1 R1-T2; a new exact audit must check it again at all h. Transitive edge generators are equivalent to connected support, because each support component generates its full symmetric group. Opposite word conventions are exchanged by word reversal and endpoint inversion; cycle lengths are unchanged.

The resulting ELSV specialization says that, for each k>=1, B_h(a1,...,ak) agrees on all positive integer tuples with a rational polynomial P_h,k of total degree at most D=3h-3+k. Its coefficient of a1^theta1...ak^thetak is the signed intersection number (-1)^lambda <tau_theta1...tau_thetak lambda_lambda>_h, where lambda=3h-3+k-sum theta_i and terms outside0<=lambda<=h vanish. This is a polynomial identity, not a count estimate.

Write phi_j(s,p)=sum_{a>=1} a^(a+j)/a! p_a s^a, s=x exp(phi_0(s,p)). Theorem3.2 gives

 H_h(x,p)=sum_theta K_h(theta)/Aut(theta) * product_{i=1}^d phi_theta_i(s,p)/(1-phi_1(s,p))^(2h-2+d),

where theta is a nondecreasing list of d>=1 integers>=2 satisfying 2h-3<=sum_i(theta_i-1)<=3h-3. In particular d<=3h-3 and theta_i<=3h-2. K_h(theta) is exactly the coefficient of the monomial a1^theta1...ad^thetad in P_h,d. Aut(theta)=product_j multiplicity_j!. Repeated powers in theta do not alter this labeled monomial coefficient; the Aut divisor belongs only to the generating-series term.

It suffices to compute these finitely many polynomial coefficients. The proof below is an original algorithmic extraction, distinct from the imported identities.

## Lemma1: ordinary fixed-endpoint counts in finite quotient tables

For every n<=M and 0<=l<=L, compute A_n(lambda,l), the number of length-l transposition words with product a fixed permutation of cycle type lambda. Initialize A_n(lambda,0)=1 if lambda=(1^n), else0. For each lambda choose a canonical permutation sigma_lambda. Enumerate all binom(n,2) transpositions t, compute the type mu of sigma_lambda t, and set

 A_n(lambda,l)=sum_t A_n(type(sigma_lambda t),l-1).

Right multiplication corresponds to deleting the final letter. Conjugation gives the same number at every endpoint in a type; no class-size weight is inserted. This recurrence counts every word once by its last letter. Use n=0 with A_empty(0)=1 and zero at positive length; n=1 has the same length behavior.

There are at most2^(n-1) partitions of n (inject partitions into compositions), so the total number of tables at n<=M is <=2^M times a polynomial in M,L. Each representative type transition takes polynomial time in n. Each count is at most binom(n,2)^l, so has O(L log(M+2)) bits. Exact arithmetic and enumerating partitions/transitions therefore cost2^M poly(M,L) bit time and space. This coarse bound suffices here; no partition asymptotic is imported.

## Lemma2: connected counts on a specified cycle list

For a list of k individually indexed cycles with lengths ai, and subset S of indices, define A(S,l)=A_sum(ai,i in S)(sorted(ai:i in S),l). Define C(S,l) similarly with support connected on the exact union of those cycle-label sets. An endpoint cycle lies entirely within one support component. For nonempty S let i0=min S. Decomposition according to the support component U containing that cycle gives

 C(S,l)=A(S,l)-sum_{proper U subset S, i0 in U} sum_{s=0}^l binom(l,s) C(U,s) A(S\U,l-s).

Process subsets by increasing size. The connected component on U and unrestricted word on its complement have unique subsequences and unique order-preserving interleaving positions in every original word. Conversely these data reconstruct the word uniquely; hence this is a disjoint exact count decomposition, including isolated labels and empty subsequences. The U=S term has complementary empty word, so equals C(S,l) with no further terms. All output counts are nonnegative integers, though subtraction is used computationally.

There are at most3^k pairs (S,U) and at most(L+1)^2 pairs(l,s), so this extraction costs3^k poly(M,L,k) bit time for a single input tuple. Intermediate positive sums count disjoint subsets of A(S,l), hence retain O(L log(M+2)) bits up to harmless polynomial overhead. The resulting C([k],r) is exactly C_h(alpha). This extraction is not an endpoint-conditioned sampler and is used only as finite coefficient-generation arithmetic.

## Lemma3: finite simplex interpolation

For d=1,...,3h-3 set D=3h-3+d. Evaluate P_h,d on every point a=1+b with b in nonnegative integers^d and |b|<=D. These values are obtained by Lemmas1–2, followed by the exact rational normalization for B_h. Every evaluated degree satisfies

 n=sum ai=d+|b|<=d+D<=9h-9, and r=n+d-2+2h<=14h-14.

Take M=9h and L=14h for safe uniform bounds. There are S_d=binom(D+d,d)<=2^(D+d)<=2^(9h) evaluation points. Let Q(b)=P_h,d(1+b). For every |beta|<=D form the exact mixed finite difference

 d_beta=sum_{0<=gamma<=beta} (-1)^(|beta|-|gamma|) product_i binom(beta_i,gamma_i) Q(gamma).

All gamma used are in the simplex. Newton's polynomial identity is

 Q(b)=sum_{|beta|<=D} d_beta product_i binom(b_i,beta_i).

To prove completeness, use the univariate falling-factorial basis in each coordinate: every total-degree<=D polynomial lies in this tensor basis with total degree<=D; the mixed differences at0 recover its coefficients by the univariate difference identity. This proves uniqueness and correctness from the finite evaluations. Return the desired coefficients after replacing b_i by a_i-1 and expanding these explicit univariate polynomials, retaining only total degree<=D. No infinite search for an invertible system is needed.

Even dense expansion and all-pairs finite differences use at most S_d^3 poly(h) rational operations: each univariate-product expansion has at most S_d monomials, and there are S_d basis elements and S_d values. Since d<=3h and S_d<=2^(9h), this is single-exponential in h. Returning only theta>=2 is a further reduction, not needed for the bound. Sum over d and then h<=g preserves single-exponential dependence.

## Bit cost and effectiveness

A normalized value is C_h(alpha) product_i(ai-1)! / (r! product_i ai^ai). Its denominator divides (L!)^(M+1): every ai<=M<=L divides L!, sum ai<=M, and r! divides L!. Its numerator after scaling to this denominator has polynomially many h bits; counts and all original factorial/power operands have O(h log(h+2)) bits and log2((L!)^(M+1))=O(h^2 log(h+2)).

Each finite-difference multiplier has O(h) bits, and there are at most2^(O(h)) summands. For monomial conversion, product_i beta_i! divides D!, since sum beta_i<=D, so a common denominator (L!)^(M+2) covers the interpolation. Expanding binomial(a_i-1,beta_i) adds only coefficients bounded by products of O(h) small integers; O(h^2 log(h+2)) bits is a safe bound for every coefficient and arithmetic intermediate under this common-denominator implementation. Dividing by Aut(theta) contributes a divisor of(3h)!, already absorbable by one additional L! factor. Thus coefficients can be represented with poly(h) bits, and cubic schoolbook rational arithmetic still gives A0 C0^(h+1)(h+2)^a0 for absolute constants.

All loops have explicit bounds and use the input h alone. No unspecified per-genus precomputation or real-number oracle occurs. The ordinary quotient table across n<=9h and l<=14h is reused across evaluations; even recomputing it for every evaluation multiplies only two single-exponential factors. The signed coefficient list is not sampled as probabilities. A downstream decoder must first evaluate full restricted nonnegative integer word masses and account separately for its own rational intermediates.

## Boundaries, dependencies, first remaining checks

This coefficient theorem is for h>=2. Genus0/1 use the exact prior formulas; singleton positive genus evaluates to0, and the empty singleton genus0 is handled separately. Ordinary quotient tables explicitly include sign-zero/length-zero/degree-one cases. C extraction uses distinct endpoint-cycle identities even at repeated lengths. The small connected/ordinary S3 transposition example81/80 must be reproduced before accepting implementation.

Dependencies: P1 polynomiality and rational-series basis; P2 fixed-endpoint normalization; elementary exact quotient recurrence; support-component decomposition; finite multivariate Newton interpolation; exact integer arithmetic. All algorithmic lemmas are provided above. No Hurwitz transitivity, MCMC theorem, random-graph model or marginal-probability product enters.

First unclosed gates: independent source normalization/formula audit, g2 coefficient recovery against the prior formula, g3 diagnostic coefficients/counts, and exact-version nonauthor proof/bit-cost review. T0 further depends on the worker's arbitrary forced-allocation and literal-decoding theorem and blind/nonauthor gates. Neither this provisional proof nor a successful finite check alone upgrades T0.
