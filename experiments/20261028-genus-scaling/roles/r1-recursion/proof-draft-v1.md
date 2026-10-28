# All-genus marker allocation and literal decoding — R1 draft v1

Status **PROVISIONAL**. This is an original derivation extending the source-scoped internally accepted I1 recursive construction. The separate frozen statement is `statement-v1.md`. The coefficient-procedure obligation is deliberately explicit; this draft does not promote a scalar count to a sampler. Same-model internal reviews are correlated.

## 1. Source contract and conventions

For a nonempty exact label set of size N, endpoint sigma with k individual cycles of lengths alpha=(a1,...,ak), and genus g>=0, let C_g(alpha) count connected ordered transposition words of length r=N+k−2+2g with rightmost-first product sigma. Cycles with equal lengths remain different objects. Set q(a)=a^a/(a−1)!, Q(alpha)=product q(ai), and B_g(alpha)=C_g(alpha)/(r!Q(alpha)).

The new imported structural input is Goulden–Jackson–Vakil, *The Gromov–Witten potential of a point, Hurwitz numbers, and Hodge integrals*, revision22Dec2000, Theorem3.2, with equations(13)–(16): [primary PDF](https://math.stanford.edu/~vakil/files/gjvfinal.pdf). In the notation frozen in our statement, it gives the finite rational expansion with tuples theta satisfying 2g−3<=sum(theta_i−1)<=3g−3, theta_i>=2. In particular d=len(theta)<=3g−3, max theta_i<=3g−2, sum theta_i<=6g−6, and denominator exponent is 2g−2+d. The 1999 paper's conjecture is not being treated as a theorem; the later theorem proves it.

Normalization is pinned independently by Goulden–Jackson, *A proof of a conjecture for the number of ramified coverings of the sphere by the torus*, Section2 and Section3 equation(2), [primary arXiv PDF](https://arxiv.org/pdf/math/9902009): its cover number is C_g(alpha)/z_alpha, where z_alpha=product_a a^(m_a)m_a!. GJV Section2.3 uses that same Hurwitz convention. Transitivity is equivalent to connected support. Reversing a source word inverts its endpoint and preserves its cycle lengths; the decoder below directly uses rightmost-first products. No classification or mixing theorem enters.

Source-scoped internally accepted genus-zero/one counts from prior I1 are used explicitly:

    B0(alpha)=N^(k−3),
    B1(alpha)=(N^(k−2) sum_i ai(ai−1)
       +sum_(j=1)^(k−1) j! N^(k−2−j) M_j(alpha; a^2))/24.

The marker M is defined next. Negative powers mean exact rationals. Singleton genus0 has one empty word, and singleton positive genus has no word. These boundary overrides can be applied before any count evaluation.

## 2. Polarization and the all-genus marker formula (R1-POL.v1)

Let each actual endpoint cycle have its own indeterminate yi, and substitute p_a=(a/q(a))sum_(i:ai=a) yi. For the monomial indexed by alpha, coefficient extraction y1...yk multiplies by (product_a m_a!)(product_i ai)/Q(alpha). Thus the coefficient of x^N y1...yk in H_g is exactly B_g(alpha), including all equal-cycle factorials.

The substituted psi_j(z,p) is sum_i ai^j yi z^ai. In the formal residue x=z exp(−psi0(z,p)), we have dx/x=(1−psi1)dz/z. Therefore

    [x^N]R(psi(s))=[z^N]R(psi(z))(1−psi1(z,p))exp(N psi0(z,p)).

Every squarefree y1...yk term automatically has z-degree N. Write L_j=sum_i ai^j yi and L0=sum_i yi. Each source term becomes

    c_(g,theta) [y1...yk] exp(N L0)
        product_(ell=1)^d L_(theta_ell)/(1−L1)^(2g−3+d).

For an ordered list of special weight functions w=(w1,...,wd), define

    M_j(alpha;w)=[u^j z1...zd]
        product_(i=1)^k (1+ai u+sum_(ell=1)^d w_ell(ai) z_ell).

Special slots are labeled even if their exponents agree; a cycle fills at most one slot. Expanding the denominator and exponential gives, for e>=1,

    [y1...yk] exp(N L0) product L_w/(1−L1)^e
      =sum_(j=0)^(k−d) (e)_j N^(k−d−j) M_j(alpha;w).

The rising factorial (e)_j includes the j! ways of assigning distinct ordinary marked cycles; the special-slot labels already include their own multiplicities. Consequently, for every g>=2,

    B_g(alpha)=sum_(theta in Theta_g) c_(g,theta)
        sum_(j=0)^(k−d) (2g−3+d)_j N^(k−d−j)
            M_j(alpha; a^theta_1,...,a^theta_d).       (P)

This identity is proved from the imported rational structure, not inferred from finite checks. Coefficients c may be signed. The complete B_g is nonnegative; an individual source term need not be.

The number of possible theta is at most sum_(w=0)^(3g−3)p(w), because theta−1 is a partition of w; the elementary partition<=composition bound makes this at most 2^(3g−2) for g>=2. This bound is used only to count specifications, not as a list of all endpoint profiles.

## 3. Exact deletion branches (R1-DEL.v1)

Fix a positive-length parent word and its last transposition tau=(x y), x<y. Its predecessor has product pi=sigma tau and length L=r−1. Removing one edge from connected support leaves one or two components.

If x and y are in different sigma cycles, pi merges those cycles. Its merged cycle contains both endpoints and must be inside one predecessor support component. A disconnected predecessor would have its two components joined by tau and would put x,y in different components, a contradiction. The predecessor is therefore connected of genus g, with count C_g(type pi).

If x,y are in the same sigma cycle, pi cuts it into cycles P containing x and Q containing y. A connected predecessor has genus g−1; it exists only if g>=1. A disconnected predecessor has exactly two components A containing P and B containing Q. Every other individual pi-cycle is assigned wholly to one side. Child genera ga,gb satisfy ga+gb=g, from their lengths

    rA=|A|+kA−2+2ga, rB=|B|+kB−2+2gb, rA+rB=L.

For a fixed assignment and genus pair the number is

    W=binom(L,rA) C_ga(alphaA) C_gb(alphaB).           (D)

Conversely, two connected child words, an order-preserving interleaving, and tau reconstruct a parent. Each parent uniquely recovers tau, predecessor components, genera, child subsequences and interleaving positions. Ordering A by the endpoint x<y eliminates any division by2, including equal child sizes/types. These are disjoint exhaustive literal branches.

Feasible genus is nonnegative: among the cycle joins of the endpoint product at least N−1 joins are needed to connect support, while joins minus splits equals N−k. Hence r>=N+k−2 with matching parity. The same argument applies to every child, including singleton zero-length children.

## 4. Arbitrarily forced allocation oracle (R1-ALLOC.v1)

Take K distinct cut cycles with lengths a1,...,aK, total degree N. Cycles1 and2 are forced to opposite children A and B; any additional cycle may already be forced to either side. Let H be the resulting partial assignment. A completion has side degree s=|A| and cycle count h=kA, so B has degree N−s and K−h cycles.

Cancellation in (D) yields

    W=L! Q(all cycles) B_ga(alphaA) B_gb(alphaB),
    L=N+K−4+2(ga+gb).                                (A)

For a chosen marker specification on each side, process the actual cycles sequentially using the table

    T[s,h,jA,maskA,jB,maskB].

Initialize T[0,0,0,0,0,0]=1. A forced cycle chooses only its assigned side; a free cycle chooses either. On its side it is unmarked with weight1, ordinarily marked with weight a and increment j, or fills one unused special slot ell with weight w_ell(a) and sets that mask bit. Placement in A additionally increments s by a and h by1. Genus0 allows only unmarked status; the first genus1 specification allows only its single special slot; the second genus1 and every genus>=2 specification allow ordinary marks. A cycle cannot fill two slots.

Induction on processed cycles proves that a table entry sums exactly the products of slot/ordinary weights of all assignments and marker choices giving that key. This uses the full joint table; no factorization of A/B marginals occurs. At completion retain full masks, multiply by the scalar factors from (P) or genus0/1, sum over all keys and all specification pairs, and multiply by L!Q. The answer is

    Z(H)=sum_(assignments extending H) W.

It is therefore a nonnegative integer. Source coefficients and intermediate rational sums may be signed. The algorithm evaluates the complete Z(H) before forming any probability. No signed term is ever used as a probability, and no positive-part replacement is permitted.

Sequential sampling visits free cycles in a fixed order. For a free index i compute Z(H+i→A) and Z(H+i→B); their sum is Z(H). Choose by these two integer masses, and update H. At each positive-mass history this is the exact conditional law. Multiplying the actual conditional ratios telescopes to W/Z(initial). Zero extensions have probability0. No marginal-product bound, cached independence, rejection acceptance estimate or latent support event is used.

## 5. Literal decoder and fair bits (R1-WORD.v1)

At each positive-length input, enumerate all O(N²) possible final transpositions and their connected branches and ga+gb=g disconnected branches. Compute complete integer masses and select one by its mass divided by C_g(alpha). In a connected branch recurse and append tau. In a disconnected branch use R1-ALLOC to choose the complete assignment, recurse independently on the two exact labeled child fibers, choose a uniform rA-subset of the L predecessor positions, interleave in order, and append tau. Canonically rename each child's labels and restore them at merge.

For a particular literal parent in a disconnected branch with aggregate mass Z, the probability is

    (Z/C_parent)(W/Z)(1/C_A)(1/C_B)/binom(L,rA)
       =1/C_parent.

A connected branch gives (C_child/C_parent)/C_child=1/C_parent. Unique reconstruction in R1-DEL and induction on output length prove exact uniformity on the entire declared fiber. The output has the correct endpoint, length and full support. This is a direct sampler, not an orbit walk and not a support-graph sampler.

Every positive call consumes one output letter. In a split call, child lengths sum to the parent length minus1. Hence there are exactly r positive calls and at most N singleton leaves. An explicit continuation stack avoids any recursion-depth assumption.

A uniform integer in [0,Z) uses ceil(log2 Z) fair bits followed by rejection of values>=Z, with Z1 deterministic. Acceptance exceeds1/2; thus expected attempts are less than2 conditional on every history. Integer categories use cumulative weights. Interleavings use binomial unranking. Exact fair bits are the theorem model; seeded random.Random draws are only diagnostics.

## 6. Uniform bit complexity (R1-COST.v1)

Write n=N+g+2 for the original input. All child degrees/cycle counts are <=N, child genera are <=g, and lengths are <=2N+2g−2. Let t(g) be the total number of installed specifications through genus g, and b(g) the largest coefficient numerator/denominator bit length. The frozen coefficient contract gives t,b<=A0 C0^(g+1), and preprocessing itself takes that bound. The structural support in fact gives t(g)<=2^(O(g)).

For any genus pair with ga+gb<=g, the total number dA+dB of special slots is at most3g+2; the extra2 covers genus1 specifications uniformly. Thus the masks have at most2^(3g+2) states. The coordinates s,h,jA,jB each have at mostN+1 values. There are K<=N cycle layers and at most2(3g+4) transitions from an entry. One forced query therefore uses at most

    O(t(g)^2 2^(3g+2)(g+2)(N+1)^5)

arithmetic operations. This also covers evaluating each final scalar with O(N+g+1) elementary multiplications if the harmless factor polynomial in g is absorbed in the genus function; using n in place of N gives an even looser n^6 bound. A direct single-child count is smaller. Iterate specification pairs, reusing the table; no subset-indexed table in N or unbounded profile cache is needed.

Each positive decoder call uses O((N+1)²(g+1)) allocation/count queries to choose a branch and O(N) further queries to sample its assignment. There are at most2N+2g positive calls. With the conservative n^6 per query this gives 2^(O(g))t(g)^2 n^10 arithmetic operations, allowing polynomial-g factors to be absorbed into a larger constant exponential. Output construction and interleaving unranking are smaller polynomial costs.

Here is a common denominator and size bound for all exact arithmetic. Let D_g be the product of the denominators of every installed rational coefficient and include24. Then log2 D_g<=O(t(g)b(g)). At fixed child degree, genus0/1 introduce negative powers of that degree of magnitude at most2 per side; higher genera in (P) have none. Therefore all allocation summands, including L!Q, have denominators dividing

    D_g² (N!)^5.

Indeed the q denominator product divides N!, and summing over side degrees s,N−s is safely cleared by (N!)^4. All reduced intermediate denominators divide this same common denominator, even with signed summation. A single-side count is also covered.

Integer table weights are bounded in absolute value by the number of side/mark choices times N^(N+6g+O(1)): ordinary marks contribute exponent at mostN, and the total special-slot exponents at total genus g are at most6g+O(1). Choice count is at most(6g+8)^N. Rising factorials have j<=N and initial value O(g); powers have exponent at mostN; factorials have argument O(N+g). Multiplying by the coefficients and summing over the exponential-in-g specification list gives an intermediate bit bound

    B=O(t(g)b(g)+(N+g+2)log(N+g+2)).

This holds for partial signed sums as well as their smaller cancelled answer, by bounding sums of absolute values. Standard reduced rational operations on B-bit integers take O(B³) elementary bit operations; the numerator/denominator magnitudes in those operations obey the same bound up to an absolute factor. Since t,b are C0^O(g), B³<=C1^(g+1)n^3 log³n for an absolute C1. With n^10 arithmetic calls and log³n<=n² for a sufficiently enlarged absolute constant (or a slightly sharper per-query bound), a conservative A C^(g+1)n^15 bit bound follows. No exponent of N depends on g.

Fair-bit rejection has conditional expected attempts<2 at every logical selection; summing the conditional expectations over the deterministic polynomial/exponential upper bound on logical calls gives the same expected complexity. No assertion about a random number of accepted recursion nodes is required: the positive node count is exactly r.

## 7. Dependency graph, first open obligation and regressions

R1-POL depends on primary GJV rational form, primary normalization and formal residue algebra. R1-ALLOC depends on R1-POL, inherited g0/g1 formulas and joint marker multiplication. R1-DEL is elementary. R1-WORD depends on R1-DEL/R1-ALLOC and exact fair-bit choices. R1-COST depends on the coefficient contract and the explicit table bounds. The conditional theorem follows from this graph.

The first unresolved external-to-this-role step for unconditional T0 is COEFF-EXP: uniformly generate the correct rational list in C^g bit time. The coordinator is constructing this by positive-simplex interpolation using ordinary cycle-type counts and anchored connected-component extraction. This draft neither assumes a connected conditioning oracle nor treats source existence alone as effective computation.

Retained regressions: N2 has exactly one feasible word at each genus; singleton positive genus vanishes by cancellation (or explicit boundary); m2 connected identity requiresN2; identity odd length is empty. The ordinary S3 transposition length5 count81 differs from connected80, so ordinary bridge counts cannot replace C. The square-free literal word (ab)^3 survives despite failing adjacent-square insertion. Equal-child and repeated-slot multiplicities are kept by x<y anchoring, slot labels and distinct cycle indices. Parallel cut representations do not enter because last-letter/support reconstruction is unique. Unweighted graph bias is absent because the law is on literal words. CP1 still refutes multiplying marginal conditional-lightness bounds; this proof instead uses complete posterior counts at every history. The growing-genus/small-support policy obstruction remains valid; this theorem is about a prescribed component, not the probability of that component under a global bridge.

## 8. Genus-three diagnostic scope

The general formula at g3 has at most six special slots; denominators before the residue range5..10 and after it4..9. The built-in diagnostic table transcribes the26 monomials in GJ1999 AppendixA, confirmed as source values by GJV Remark3.3. It extends the prior production marker and decoder code but does not implement the uniform coefficient preprocessor. Tests will compare all exact endpoint counts on N<=4 and g<=3, arbitrary forced allocation masses, and tiny literal laws without enumerating all N4,g3 words. Finite success cannot prove the all-genus source form, coefficient effectiveness, or asymptotic complexity.
