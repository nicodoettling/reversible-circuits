# R3 blind statement-only report v1

**Verdict:** a candidate proof of T0, and of the stronger fixed-endpoint AUX-ENDPOINT.v1 target, is supplied below. The new uniform ingredient is an exact genus-coefficient recovery algorithm with single-exponential genus cost. It uses neither an oracle for Hodge integrals nor an assumed higher-genus sampler. This is **PROVISIONAL / author-proved pending exact-version nonauthor audit**, not an accepted project theorem. The coordinator must retain T0 as OPEN until the required certification gates close.

The original target is unchanged: for N>=2 and integer g>=0, sample uniformly from ordered transposition words on the exact labels [N], rightmost-first product identity, connected support on all N labels, and length2N-2+2g. The proposed algorithm is uniform in N,g, outputs the literal word, and uses fair random bits. Its expected bit cost is2^O(g)(N+g+2)^c for one absolute exponent c. The proof also handles a specified permutation sigma with k individual cycles and lengthN+k-2+2g. Neither a mixing theorem nor an unrestricted all-length polynomial sampler follows.

## 1. Isolation, sources and certification scope

This worker received only `input-v1.md` as its new mathematical brief. Before freezing this report it inspected no new other-worker proof, coordinator mathematical summary, claim ledger or status artifact. The visible user AGENTS instructions, project navigation and historical status were not withheld. Required project reading comprised AGENTS.md, PROJECT_MAP.md, notes/project-map/FRONTIER.md, HANDOFF.md, GOAL_SPEC.md, the project sampler skill and its sampling/experiment references, and the mathematical-proof-audit skill with audit-protocol/probability-regressions. The project maps disagree chronologically about whether the decoder stops at genus1 or2; the permitted prior I1 report/reconciliation gives the exact later scope. Historical heat-bath targets and classification disputes are not used in this argument.

Permitted prior mathematical artifacts inspected were I1's report/reconciliation, recursive proof/source-verification, structural proof and old blind report under `experiments/20261025-identity-bridge-sampling-campaign/20261028-genus-two-admission/`. Those supplied context and regressions, not a new growing-genus proof. No I2 sparse work was read. The construction below was derived during this statement-only phase. Same-model review and shared project context remain correlated; blindness is not statistical independence. Inherited model/effort/tier were described as Astra/ultra/default, with no override or independent runtime verification. No descendants, research CLI sessions, installs, commits or permissions were requested.

Two primary source inputs were checked through extracted PDF text:

* Goulden–Jackson–Vakil, *The Gromov–Witten potential of a point, Hurwitz numbers, and Hodge integrals*, author-hosted version revised22Dec2000, [Theorem3.2 and equation(16)](https://math.stanford.edu/~vakil/files/gjvfinal.pdf). For g>=2 the connected Hurwitz series is a finite sum of terms c_l product(phi_j^l_j)/(1-phi_1)^(2g-2+sum l_j), with j>=2 and sum(j-1)l_j<=3g-3. Its phi_j=sum_a a^(a+j)p_a z^a/a!, evaluated at s=x exp(phi_0(s,p)).
* Goulden–Jackson, *A proof of a conjecture for the number of ramified coverings of the sphere by the torus*, [Section2, equation(2), equation(1), Theorem4.2](https://arxiv.org/pdf/math/9902009), explicitly gives the fixed-permutation normalization, genus-zero count and genus-one series used below.

These published inputs are imported, not reproved. Attempts to obtain source screenshots did not expose visible page images, so no visual verification is claimed. The all-genus input is the proved GJV theorem, not the earlier conjecture in the1999 double-torus paper. The finite change of variables below is not an assertion that the infinite map Xi in GJV is invertible.

## 2. Definitions and exact finite counting without a sampler

Let alpha=(a_1,...,a_k) be the cycle lengths of a fixed permutation sigma on n labels. Actual equal-length cycles are distinct objects. Write C_r(alpha) for the number of connected ordered length-r transposition words with endpoint sigma, and A_r(alpha) for the ordinary count without connectivity. Conjugation proves that these counts depend on cycle type. Put

    r_g(alpha)=n+k-2+2g,
    C_g(alpha)=C_(r_g(alpha))(alpha),
    q(a)=a^a/(a-1)!=a^(a+1)/a!,
    Q(alpha)=product_i q(a_i),
    z_alpha=product_i a_i * product_a m_a!,
    B_g(alpha)=C_g(alpha)/(r_g(alpha)! Q(alpha)).

Here m_a is the multiplicity of part a. The fixed-permutation normalized Hurwitz series is

    H_g(x,p)=sum_(n>=1,alpha partition n) C_g(alpha)/(r_g(alpha)! z_alpha) p_alpha x^n.

The source's inverse or opposite product convention, if used, is translated by reversing the word and inverting its endpoint; cycle type is unchanged. Our decoder itself always uses sigma*t for the predecessor endpoint when t is the final letter.

A connected word has r=n+k-2+2g with g>=0. Indeed, if J letters join current permutation cycles and K letters split them, k=n-J+K and r=J+K. At least n-1 letters join previously distinct support components, each a permutation-cycle join. Hence g=J-n+1>=0. Support connectivity is equivalent to transitivity of the edge-generated subgroup, since graph paths generate all transpositions inside each connected component.

For later preprocessing, all A_r,C_r at n<=S,r<=R can be computed exactly in exp(O(sqrt(S)))poly(S,R) bit operations when R is polynomial in S. The following deliberately simple algorithm suffices.

First list integer partitions of all n<=S. For every partition alpha construct a representative permutation, inspect each of its at most S² transpositions t, and record the cycle type of sigma*t and its multiplicity. Then

    A_0(alpha)=1 if alpha=(1^n), otherwise0,
    A_r(alpha)=sum_t A_(r-1)(type(sigma*t)).                 (2.1)

This loops over cycle types, not group elements or words.

Recover connected counts by degree induction. Anchor one particular endpoint cycle of length a0. A proper support component containing that cycle consists of the anchor plus a submultiset of the other endpoint cycles. For its type beta, the number of actual cycle choices is

    M(alpha,beta)=product_a binom(m_a-delta_(a,a0), b_a-delta_(a,a0)).

The component and its complement have disjoint label sets, their words commute across sets, and the two subsequences have a unique order-preserving interleaving. Therefore

    C_r(alpha)=A_r(alpha)
      -sum_(proper beta containing anchor) M(alpha,beta)
         sum_(s=0)^r binom(r,s) C_s(beta) A_(r-s)(alpha-beta).       (2.2)

Every disconnected word occurs once, through its unique support component containing the anchor. All children beta have smaller degree. Singleton C_0((1))=1 and C_r((1))=0 for r>0 follow either directly or from(2.1). This proves(2.2), including isolates and repeated equal-length cycles.

For completeness, let P(S) count partitions of all integers through S. With t=1/sqrt(S),

    p(n) <= exp(tn) product_(j>=1)(1-exp(-tj))^-1
         <= exp(tn + (1/t)sum_(h>=1)1/h²)
         <= exp(3sqrt(S)),

where 1/(exp(th)-1)<=1/(th) and sum h^-2<=2. Thus P(S)<=(S+1)exp(3sqrt(S)). Each possible beta in(2.2) is itself a partition in this inventory. Even scanning the entire inventory for each alpha costs at most P(S)^2 times a polynomial. Standard nondecreasing-part recursion lists partitions with polynomial overhead per emitted item. Transitions may be stored in sorted dictionaries; no unit-cost random-access assumption on gigantic integers is needed.

All counts are at most binom(S,2)^R, with O(R log(S+2)) bits. Binomial coefficients and partial disconnected sums have polynomial bit length. Formula(2.2) is an exact integer subtraction of disjoint positive contributions, not signed sampling. This establishes the asserted finite counting complexity independently of any higher-genus formula.

## 3. Uniform recovery of the higher-genus numerator

Fix h>=2 and define

    D=3h-2,  K=3h-3,  E=5h-5,  S=DK,  R=2S+2h.

The GJV structure theorem implies

    H_h(x,p)=P_h(phi_1(s,p),...,phi_D(s,p))/(1-phi_1(s,p))^E,       (3.1)

where P_h is a rational polynomial of ordinary total degree at most K. To verify the degree bound, a source term with d=sum l_j numerator factors has denominator exponent2h-2+d. Multiplication by(1-phi_1)^E contributes the polynomial powerK-d. Its combined numerator degree is at mostK, and j<=D. No positivity of the coefficients is assumed.

There are at most

    M_h=binom(D+K,K)<=2^(D+K)<=2^(6h)

possible monomials. Their coefficients are not treated as advice, an oracle, or genus-specific hard coding. The following uniform algorithm computes all of them.

Set p_a=0 for a>D, put phi_j(p)=sum_(a=1)^D a^(a+j)p_a/a!, and work modulo terms of total p-degree>K. Invert the tree substitution by x=z exp(-phi_0(z,p)). Setting z=1 after this substitution gives the finite identity

    F_h(p)=[degree<=K] sum_(parts(alpha)<=D, length(alpha)<=K)
          C_h(alpha)/(r_h(alpha)! z_alpha)
          p_alpha exp(-|alpha| phi_0(p)),
    P_h(phi_1(p),...,phi_D(p))
          =[degree<=K] (1-phi_1(p))^E F_h(p).                    (3.2)

This substitution is legitimate in the p-adic finite truncation. A term with more than K cycles cannot lower its p-degree; a term containing p_a for a>D vanishes; every remaining original partition has degree at mostDK. Thus setting z=1 does not hide an infinite sum. All required connected counts in(3.2) are available from Section2 at degree<=S and length<=R.

The linear map p -> (phi_1,...,phi_D) has matrix

    V_(j,a)=a^(a+j)/a!,  1<=j,a<=D.

Factoring a^(a+1)/a! from column a leaves the Vandermonde matrix a^(j-1). Its determinant is nonzero. Invert V exactly and substitute p=V^-1 Y in the polynomial obtained in(3.2). The result is exactly P_h(Y), because its known degree bound prevents any omitted higher-degree term from contributing. This finite square matrix is invertible even though a different infinite-variable map discussed in GJV is not.

The coefficient recovery costs2^O(h)poly(h) bit operations. Indeed S=O(h²), so Section2 costs exp(O(sqrt(S)))poly(h)=2^O(h)poly(h). All multivariate polynomials have D=O(h) variables and total degree<=K=O(h), hence at most2^O(h) monomials. Naive convolution, repeated multiplication by linear forms, and termwise linear substitution use only a fixed power of this inventory times a polynomial in h. Gaussian elimination on the D-by-D rational matrix is polynomial work.

Here is a common-denominator and magnitude audit. Let W=D!V be an integer matrix. Its entries have O(h log(h+2)) bits and det(W), all cofactors, and V^-1 entries have O(h² log(h+2)) bits by elementary determinant bounds. Reduced Gaussian elimination can equivalently be implemented by fraction-free elimination, so intermediate bit lengths are polynomial. The initial normalized counts have denominators dividing R!S!: r! dividesR!, and z_alpha divides|alpha|! which dividesS!. A safe common denominator for all coefficients after(3.2) and inverse substitution is

    Delta_h=R! S! (D!)^(2K) K! |det(W)|^K.                      (3.3)

The exponential truncation uses at mostK linear factors and a factorial dividingK!; the multiplier contributes at mostK retained linear factors; inverse substitution contributes at mostK entries of V^-1. Thus(3.3) covers every term. Its logarithm is O(h³ log(h+2)). Each unsummed numerator is a product of at most polynomially many polynomial-bit factors; the exponential-size term inventory adds only O(h) bits to an absolute-value sum. Consequently every recovered coefficient has O(h³ log(h+2)) bits, with a common denominator of that order. Cancellation does not defeat this estimate.

Precompute P_2,...,P_g if g>=2. The sum of their single-exponential bounds is still2^O(g)poly(g). The source theorem supplies a finite structural identity; the new recovery algorithm supplies its uniform effectiveness and its bit bound.

## 4. From recovered coefficients to finite marker expressions

For an endpoint alpha, substitute

    p_a=(a/q(a)) sum_(i:a_i=a) y_i.

Squarefree extraction in the actual cycle variables y_1,...,y_k cancels the equal-cycle factorial in z_alpha and yields B_h(alpha). Under this substitution,

    phi_j(z,p)=sum_i a_i^j y_i z^(a_i),
    L_j=sum_i a_i^j y_i,  L_0=sum_i y_i.

The formal residue change x=z exp(-phi_0(z,p)) has

    dx/x=(1-phi_1(z,p)) dz/z.

Extracting x^n and the squarefree cycle monomial, whose z-degree is automatically n, gives for h>=2

    B_h(alpha)=[y_1...y_k] exp(nL_0)
                    P_h(L_1,...,L_D)/(1-L_1)^(5h-6).           (4.1)

For h=0 the known count is B_0(alpha)=n^(k-3). For h=1, differentiate the source series with respect to its tree argument before Lagrange inversion. The result is

    B_1(alpha)=(1/(24n))[y_1...y_k] exp(nL_0)
                      (L_2/(1-L_1)-L_1).                     (4.2)

Thus every B_h is an explicitly computable finite sum of descriptors

    c n^(-b) [y_1...y_k] exp(nL_0)
                   product_(j in ordered slots) L_j /(1-L_1)^e.      (4.3)

Genus0 has one descriptor: c=1,b=3,e=0,no slots. Genus1 has two: (c,b,e,slots)=(1/24,1,1,[2]) and(-1/24,1,0,[1]). Genus h>=2 uses each monomial of P_h as ordered slots, its rational coefficient c, b=0 and e=5h-6. Repeated slot exponents remain separate slots. The total slot count is at most3h-3; across two children with genera adding to g it is at most3g. There are2^O(g) term pairs, their exponents are O(g), and their coefficient bit lengths are polynomial in g.

Expanding a descriptor gives the following concrete interpretation. Assign distinct cycles to its labeled special slots, weight a_i^j for slot j; assign an additional q-subset of cycles as ordinary denominator marks, weight product a_i; leave every remaining cycle exponential/unmarked, weight n each. Multiply by

    R_e(q)=q! binom(e+q-1,q) for e>=1,
    R_0(q)=1 if q=0, otherwise0.                              (4.4)

Then multiply by c n^(-b) and sum. Equation(4.4) accounts for the ordering of the q factors in L_1^q. Special-slot ordering already accounts for repeated special factors, so no extra factorial is inserted or removed. Individual descriptors may be negative; they are evaluated and summed, never sampled.

## 5. Arbitrarily forced two-child allocation in single-exponential genus time

Suppose an endpoint's cycles have been split by a proposed final transposition into two anchor cycles. For fixed child genera h_A,h_B with h_A+h_B=g, the necessary allocation mass is a sum over assignments of the remaining actual cycles to A or B. Either anchor and any additional cycles may already have forced sides. Let all lengths sum to n and let the total number of cycles be k'.

For one descriptor of B_(h_A) and one of B_(h_B), loop over the target degree s=1,...,n-1 of A; write t=n-s. If s=1,h_A>0 or t=1,h_B>0, skip this entire degree, since that child fiber is empty. Let d_A,d_B be the numbers of special slots. Process cycles in their fixed actual order with the integer table

    T[v,q_A,q_B,M],

where v is allocated A degree, q_A,q_B ordinary-marker counts, and M is a subset of the d_A+d_B labeled special slots. Initially T[0,0,0,empty]=1. Place a cycle of size a on any allowed side. On A its degree increment is a, and on B it is0. On that side choose precisely one of:

* exponential/unmarked, multiplier s on A or t on B;
* ordinary mark, multiplier a and increment the corresponding q;
* one unfilled special slot j belonging to that side, multiplier a^j and set its bit.

Discard v>s. After all cycles, retain v=s and the full mask. Multiply each entry by R_(e_A)(q_A)R_(e_B)(q_B), the two descriptor coefficients, and s^(-b_A)t^(-b_B). Sum over table entries, descriptors and s. Induction on processed cycles proves that this is exactly

    Z_B(H)=sum_(assignments extending forcing H)
                B_(h_A)(alpha_A) B_(h_B)(alpha_B).             (5.1)

Actual cycles are DP items, even if their lengths match. This table retains all cross-moments; it never multiplies independent marginal subset sums. It also avoids enumerating N^d special-slot injections: the exponential factor is2^(d_A+d_B), depending only on genus.

The table has at most(n+1)^3 2^(d_A+d_B) entries. There are at most n item layers, n choices of s, and O(g+1) transitions per entry. Evaluating one term pair therefore costs2^O(g)poly(n,g), with a fixed polynomial exponent. The2^O(g) term-pair inventory preserves that bound. Every arbitrary forcing query has the same bound.

For fixed allocation, the number of pairs of connected child words and shuffles is

    binom(L,r_A) C_(h_A)(alpha_A) C_(h_B)(alpha_B)
       =L! Q(all cycles) B_(h_A)(alpha_A) B_(h_B)(alpha_B),     (5.2)

where r_A=s+|alpha_A|-2+2h_A and L=r_A+r_B=n+k'-4+2g. Thus L!Q(all cycles) times(5.1) is an actual nonnegative integer word count, including after arbitrary forcing. Only these final counts are used as probabilities. Complete signed sums are evaluated exactly before asserting nonnegativity or integrality.

To sample an allocation, visit free actual cycles in a fixed order. Recompute the two masses for H extended by that cycle's side. Their sum is the current mass. Select by the exact ratio and continue. For a completed assignment a, the successive ratios telescope to its full weight divided by the initial mass. This is a pointwise statement about the actual surviving history, including zero-mass branches, not a multiplication of marginal estimates.

## 6. Literal-word decoder and its law

For a nonempty connected fixed-endpoint fiber (V,sigma,g), inspect every final transposition tau=(x y), x<y, and set pi=sigma*tau.

If x,y lie in different cycles of sigma, pi merges them. The predecessor is necessarily connected and has genus g. Its branch count is C_g(type pi).

If x,y lie in the same sigma-cycle, pi splits it. There are two possibilities: a connected predecessor of genus g-1, or exactly two connected predecessor support components. In the latter case let A contain the pi-cycle of x and B contain the pi-cycle of y. All other actual pi-cycles are allocated to one side, and the child genera satisfy h_A+h_B=g. For each genus pair the aggregate branch count is the integer from(5.1)–(5.2).

Deleting one edge occurrence from a connected graph leaves at most two support components. In a disconnected predecessor each pi-cycle lies wholly in a component, and the two anchors lie on opposite sides. Conversely any such allocation, connected child words and order-preserving shuffle, followed by tau, reconstruct a parent. These facts prove that all described branches are disjoint and exhaustive. The child containing x is distinguished, so there is no factor1/2.

The algorithm computes these branch counts and selects a branch proportionally. In a connected branch it recursively samples the predecessor, then appends tau. In a disconnected branch it samples the allocation by Section5, recursively samples each labeled child, chooses a uniform r_A-subset of the L predecessor positions for the A-word, interleaves, and appends tau. Relabeling a child to an ordered canonical label set and back is allowed, but all original labels and positions remain distinguished. A singleton at genus0 returns its empty word; a positive-genus singleton is assigned zero count. A stack implements the recursion without a recursion-depth assumption.

Induction on length proves the literal law. For a fixed parent word in a split class with aggregate count Z, allocation weight W from(5.2), and child counts C_A,C_B, its probability is

    (Z/C_parent) (W/Z) (1/C_A) (1/C_B) /binom(L,r_A)
       =1/C_parent.

Connected-branch factors cancel in the same way. The unique reconstruction proves that every target word is represented once by the selected data. This construction neither samples an unweighted support graph nor assumes that a scalar Hurwitz count is already a word sampler.

Every positive recursive call emits one letter; its child lengths sum to one less than its own length. Hence a root of length r has exactly r positive calls. All child genera are at most g, degrees at most N, and lengths at most r<=2(N+g). The number of zero-length leaves is at most r+1.

For fair bits, sample an integer uniform in[0,Z) using ceil(log2 Z) bits and rejection of values>=Z. For Z>1 the conditional acceptance probability is greater than1/2; Z=1 is deterministic. Cumulative integer weights choose branches and allocations. Uniform binomial unranking chooses interleavings. At every history the same bound applies to a fresh logical draw. Linearity of expectation over the bounded number of logical draws gives the expected bit bound; no adaptive marginal-product assertion is required.

## 7. Full uniform complexity

Set X=N+g+2. The coefficient preprocessing of Section3 takes2^O(g)poly(g) deterministic bit time and space. It is performed once through the input genus and then reused. No count inventory over endpoint types of the full input degree N is precomputed.

A direct B_h count uses the one-side version of the marker table. A forced allocation query uses at most2^O(g)N^5 poly(g) arithmetic operations by Section5. Each positive recursion node considers at most N² transpositions and g+1 genus pairs per split, plus at most N further forcing queries for the selected allocation. There are O(N+g) positive nodes. Therefore the total number of arithmetic operations is2^O(g)X^c0 for an absolute exponent c0 (a loose value c0=12 covers these loops).

Bit lengths also have an absolute polynomial bound. A descriptor's rational coefficient has O(g³log(g+2)) bits. At a fixed allocation degree s, DP entries sum at most(2+3g)^N choices. Each unmarked or ordinary weight is at mostN; the at most3g special slots have exponents at most3g, so their total weight has at most O(g²log(N+2)) bits. Rising factorials R_e(q), with e<=5g and q<=N, add O((N+g)log(N+g+2)) bits. Exact factors Q(alpha), factorials and shuffle counts add the same polynomial bit order.

For the forced oracle, negative degree powers are only s^-3,t^-3 or s^-1,t^-1. Across the degree sum their denominators divide((N-1)!)^6. The q-products have denominator dividingN!. The descriptor coefficients have the common denominators(3.3). If one wants a single denominator for every genus at once, the product of these Delta_h through g has O(g^4log(g+2)) bits. Thus no sum over assignments or term pairs introduces an uncontrolled product of unrelated denominators. Absolute numerator bounds use the same polynomial bit order; cancellation is harmless because arithmetic is exact. A loose uniform bound is O(X^5) bits for all reduced rational intermediates, including temporary products up to a constant factor.

Elementary reduced rational arithmetic can be charged O(B³) bit operations on B-bit quantities; gcd, exact integer comparisons, and fair-bit choices fit this bound. Combining with the operation count gives2^O(g)X^c for one absolute c; taking c=40 is a conservative bound for the displayed algorithms. Every exponential factor above is bounded by a fixed constant to the power g+1: the partition inventory through S<=9g², the polynomial inventory with D+K<=6g, and the marker masks of size<=3g. Consequently there exist absolute A>0,C>1 such that the expected bit time is at most

    A C^(g+1) (N+g+2)^40.                                    (7.1)

This proves the requested uniform form within the imported structure theorem. It does not merely prove a separate polynomial for each fixed g, an N^O(g) bound, an arithmetic-operation bound, or a count-only reduction. The exact law gives TV error0, so T1-FPT, T1-QUASI and the stated T3 accuracy requirement follow as weaker conclusions if T0 passes audit.

## 8. Adversarial findings, boundaries and regressions

The following failed routes remain rejected. Their failure does not refute T0.

| attack or boundary | required outcome and resolution |
|---|---|
| Genus coefficients supplied as a fixed list for each g | Insufficient for uniform T0. Section3 computes the list uniformly, with its own full bit bound. |
| Enumerate special-slot injections into cycles | N^O(g) is insufficient. Section5 replaces injections by a subset mask of at most3g labeled slots and a fixed number of polynomial coordinates. |
| Compute connected counts on all full-degree endpoint types | Partition inventories in N would destroy the target bound. They are used only at degreeO(g²) in coefficient preprocessing. |
| Interpret signed numerator terms as probabilities | Invalid. The complete restricted sums become actual nonnegative integer branch counts before any random selection. |
| Assume the infinite change of variables is invertible | Invalid in general. Only the explicit finite D-by-D Vandermonde map is inverted, after the proven degree cutoff. |
| Ordinary versus connected endpoint | S3 transposition endpoint at length5 has81 ordinary and80 connected words. Section2 inversion and Section6 branch masses use connected counts. |
| Unweighted support graph | Historical triangle weight1/4 versus required3/4 remains a counterexample. The new algorithm uses literal branch counts, not graph-uniform sampling. |
| Adjacent-square insertion | The word((12),(23))^3 has no adjacent equal factors and still evaluates to identity. Insertion-only support failure remains. The decoder deletes the actual last edge and has universal coverage. |
| Equal-shaped children or parallel cut cores | Historical multiplicities remain essential. No cut/core encoding is used here; anchors distinguish children, actual cycles are separate DP items, and shuffles retain positions. Equal slot exponents remain labeled slots. |
| CP1 adaptive product |21/2000>1/100 remains the counterexample. Selection changes support and normalization. Here every posterior choice uses recomputed restricted counts and telescopes pointwise. |
| Fixed/small-genus and small-support policy | M-GROW remains valid on its stated subsequence. This sampler allows every input genus with exponential genus cost; it implies no polynomial all-length global algorithm. |
| Odd identity length | Empty by sign; no uniform target exists. T0's length is always even. |
| Identity m=0,N>=2 | Connected fiber empty. Singleton genus0 alone has the connected empty word. |
| Identity m=2 | Connected only on exactly two labels; the unique repeated edge is returned. |
| N=2 | One edge exists. Every feasible identity fiber is its even repetition; every feasible transposition-endpoint fiber is its odd repetition. The algorithm can return it directly. |
| Positive-genus singleton | Empty and skipped before random choices. |
| Genus0/minimal connected endpoints | Factor each endpoint cycle minimally, then append doubled edges linking cycle supports in a tree. This realizes lengthN+k-2. Additional doubled edges realize every higher genus for N>=2. |
| Zero conditional mass | Has probability0; a zero root fiber is rejected. Every valid N>=2 endpoint/genus input has a positive fiber by the preceding construction. |
| Literal labels and order | Retained throughout the unique final-letter decomposition, child relabeling and uniform interleaving. |

The new proof uses no quantitative Hurwitz transitivity, local heat-bath mixing, unsupported independence, or unproved positivity of Hodge coefficients. The externally imported theorem remains a substantive geometric enumeration input. Exact source normalization and the finite coefficient recovery are load-bearing audit targets.

## 9. Reserved finite falsification and resource record

The coordinator reserved and executed the sole mathematical job as J3 under the current v0.4.2 bounded helper and sealed attempt000001 run file. Exact child argv:

    python3 -B experiments/20261028-genus-scaling/roles/r3-adversarial/check_blind_v1.py --output experiments/20261028-genus-scaling/roles/r3-adversarial/check-results-v1.json

Timeout180s, address-space ceiling1GiB; no actual RSS measurement is claimed. The job exited0. Coordinator tool observation0.159200725s; child report0.138903904s. Python3.12.3; stdlib only; deterministic, seed0 metadata. Intake source commit b178daf320833e859dcdee0ce56eb16c6d2130b7. The script was written but not run until coordinator reservation. It performs no exhaustive N4,g3 word enumeration.

Results:

* Ordinary and anchored-component-inversion tables through degree12,length28 recovered the complete genus2 polynomial P_2 from the new coefficient algorithm. All14 nonzero coefficients agree with the known genus2 numerator after multiplying by(1-phi_1)^5.
* An independent state DP over literal endpoint permutation and support partition gave396 exact comparisons for N2,3,4, including all identity genera0..3 and arbitrary endpoints through the tested lengths.
*90 arbitrary-forcing allocation queries, with repeated sizes and up to six labeled slots, matched direct injection/subset/allocation sums exactly. These are generic descriptor identities, not assertions of a full genus3 production sampler.
* The old baseline counts27,120,3936 and the ordinary/connected81/80 distinction passed. The exact CP1 numerical inequality was retained.

Connected identity counts found were:

| N | g0 | g1 | g2 | g3 |
|---|---:|---:|---:|---:|
|2|1|1|1|1|
|3|24|240|2184|19680|
|4|2880|131040|4959360|180686880|

Finite agreement can refute implementation/normalization mistakes; it does not prove the universal structure theorem, complexity bounds or full all-genus word law. This report is a mathematical algorithm, with a targeted falsification script; it is not a complete production implementation of the sampler. No further computational claim is made.

| candidate | claimed target | identity/endpoint valid | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| R3 uniform coefficient-recovery decoder | connected fixed-endpoint all-genus literal uniform law | candidate proof in Sections2–7 | direct decoder; no walk or mixing claim | genus2 recovery,396 endpoint/support comparisons,90 forced-mask queries | promote for exact-version audit; not accepted |

## 10. Claim graph and first unresolved certification step

| claim | mathematical status in this report | dependencies | evidence/artifact | independent check required | action |
|---|---|---|---|---|---|
| R3-C1 ordinary and connected finite counting | proved | elementary word/component decomposition | Section2; check script | recurrence multiplicities and partition cost | retain |
| R3-C2 bounded numerator form | imported proved theorem, source-scoped | GJV Theorem3.2; normalization | Sections1,3 | exact published statement and normalization | audit import |
| R3-C3 uniform single-exponential coefficient recovery | candidate proved / provisional | C1,C2; finite Vandermonde inversion | Section3; full genus2 recovery | truncation completeness, denominator and operation bounds | audit closely |
| R3-C4 marker and forced-allocation oracle | candidate proved / provisional | C3; Lagrange inversion; genus0/1 formulas | Sections4–5;90 finite queries | every forcing/slot multiplicity; signed sum bound | audit closely |
| R3-C5 literal all-genus word law | candidate proved / provisional | C4; elementary deletion | Section6 | unique reconstruction and conditional cancellation | audit |
| R3-C6 uniform fair-bit cost | candidate proved / provisional | C3–C5 | Section7 | absolute exponents and every large-integer operation | audit |
| R3-T0 and AUX-ENDPOINT | PROVISIONAL; no internal gap identified | C1–C6 and checked source inputs | complete report | frozen exact-version nonauthor audit and coordinator reconciliation | leave project T0 OPEN until gates close |
| General all-length polynomial sampler, mixing, wire-polynomial efficiency | unresolved / not asserted | absent | scope statements and M-GROW regression | separate targets | do not infer |

No first unproved mathematical implication is presently identified inside Sections2–7 under the stated published structure theorem and genus0/1 enumeration inputs. The first unresolved certification obligation is a fresh nonauthor check of the **exact** coefficient-recovery lemma R3-C3, especially that degreeO(g²) counts determine the full numerator and that every coefficient/intermediate retains polynomial-in-g bit size. A counterexample to any dependency reopens every downstream claim. This worker's verdict is not an automatic promotion, and source-scoped internal review remains distinct from human/external certification.

The immutable final report and companion artifacts will be bound by SHA256 in `manifest-v1.json`. Subsequent revisions or nonblind audits must use new files, leaving this statement-only report unchanged.
