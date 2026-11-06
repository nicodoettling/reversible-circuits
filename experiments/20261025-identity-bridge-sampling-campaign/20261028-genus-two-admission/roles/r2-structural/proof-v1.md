# C2.v1 — genus-two identity sampling by a genus-one cut

Author proof frozen for review, 2026-10-28. **PROVISIONAL complete construction; not coordinator acceptance.** The target is the uniform law on

\[
 X^{(2)}_N=\{(t_1,\ldots,t_{2N+2}):t_i\text{ transpositions in }S_N,
             \ t_1\cdots t_{2N+2}=1,\ \operatorname{supp}(t_1,\ldots,t_{2N+2})\text{ connected on }[N]\},
\]

for every integer N>=2. Products act rightmost first. Output is an explicit ordered labeled word; randomness consists of independent fair bits. The proposed theorem is exact uniform sampling, hence TV error zero for every b>=1, in expected time polynomial in N (and therefore in N,b). It does not assert arbitrary-endpoint genus-two sampling, an unrestricted all-length sampler, a Hurwitz-orbit claim, or any Markov-chain mixing statement. Degree N is the resource variable, not log N wires.

## Dependency D0: the accepted genus-zero/one component interface

For a permutation on a fixed nonempty label set with individual cycle lengths a=(a_1,...,a_d), put S=sum a_i and

\[
 q(a)=a^{a+1}/a!,\quad Q(a_1,\ldots,a_d)=\sum_i a_i(a_i-1),
\]

\[
 E_j(a)=\sum_{|J|=j}\prod_{i\in J}a_i,
 \qquad W_j(a)=\sum_{|J|=j}\Big(\prod_{i\in J}a_i\Big)\Big(\sum_{i\in J}a_i\Big).
\]

The number C_h(a) of connected words of length r_h=S+d-2+2h with that **fixed** endpoint, for h=0,1, is

\[
 C_h(a)=r_h!\prod_i q(a_i)\,H_h(a),
\]

\[
 H_0(a)=S^{d-3},\qquad
 H_1(a)=\frac1{24}\left[S^{d-2}Q(a)+\sum_{j=2}^d(j-1)!S^{d-1-j}W_j(a)\right]. \tag{1}
\]

All displayed summands are nonnegative; negative powers are rational numbers. The singleton genus-zero word is empty and has count1; singleton positive genus has count0. The S-G01 result supplies an actual exact expected-polynomial-bit sampler for every nonempty such fiber, including arbitrary endpoints. This interface is more than scalar counts and is used explicitly below.

Exact inherited source: `experiments/20260907-genus-one-sampler/proof.md`, S1.v2/R1-T1.1, with current-version nonauthor audits `roles/r2-structural/recursive_audit.md` and `roles/r3-referee/candidate_audit.md`. Formula(1) ultimately uses Vakil, *Genus 0 and 1 Hurwitz numbers*, Section1.2, Corollary1.5 and the positive expansion in Proposition3.2, with the fixed-permutation normalization recorded there. This construction does not claim a new independent literature verification; its imported dependency is the exact accepted S-G01 interface and its recorded source checks. A change to that interface reopens C2. No connected-support Hurwitz transitivity is needed.

## C2.1: genus increments and universal cut coverage

For a transposition word u on the ambient N-set, let c(u) be its endpoint's cycle count including fixed points, and q(u) its support-component count including isolated vertices. Define total component genus

\[
 G(u)=\frac{|u|-N-c(u)+2q(u)}2.
\]

It is the sum of the nonnegative connected-component genera. Under appending a transposition, it increases by1 precisely when the letter joins two current permutation cycles lying in the same current support component. In the other cases it stays fixed: joining two support components lowers both cycle and component counts by1; splitting a permutation cycle increases the cycle count by1 without changing support components. These three cases prove nonnegativity and unit increments directly from the empty word.

A word w in X_N^(2) ends at G(w)=2. Let h_1<h_2 be the two forward indices where genus increases. Then

\[
 J(w)=\{j:1\le j<2N+2,\ G(w_{1:j})=1\}=\{h_1,\ldots,h_2-1\}. \tag{2}
\]

This is a nonempty interval of internal cuts. In particular h_2<=2N+1: the last letter of an identity word starts from its own transposition endpoint and splits that 2-cycle, so the last letter cannot increase genus. Thus 1<=|J(w)|<=2N+1.

At a cut j, put p=eval(w_{1:j}); the suffix endpoint is p^(-1). Form a bipartite multigraph B: left vertices are prefix support components, right vertices are suffix support components, and **each individual p-cycle**, including every fixed point, gives one edge connecting its containing components. This edge carries the directed p-cycle. Distinct cycles give distinct edges even when their lengths agree. The graph is connected: a disconnection would partition the labels into nonempty unions of support blocks of both sides, contradicting connectedness of the whole word. Its number of edges is c(p), and vertices q_L+q_R.

For a connected identity word of arbitrary genus g, summing the two side genus formulas gives

\[
 G_L+G_R=g-1+(q_L+q_R)-c(p)=g-\beta_1(B),\qquad
 \beta_1(B)=|E(B)|-|V(B)|+1. \tag{3}
\]

Consequently every j in(2) satisfies G_R<=1. There are exactly two possibilities:

* **tree:** G_L=G_R=1 and beta_1=0;
* **unicycle:** G_L=1,G_R=0 and beta_1=1.

Nonnegative component genera imply a unique genus-one left vertex in either case, a unique genus-one right vertex in the tree case, and genus zero at all other vertices. This is universal coverage, not a finite-test extrapolation.

Conversely, take any connected bipartite tree with the specified one genus-one vertex in each color, or any connected bipartite unicycle with one genus-one left vertex and none on the right. Assign disjoint directed cycles partitioning[N] to its edges. At each vertex choose a connected word with endpoint its incident cycles (inverse cycles on the right) and its assigned genus. Interleave local words independently within each side, and concatenate the sides. The endpoint is identity, the union support is connected, and equation(3) gives genus2, hence total length2N+2. Prefix genus is1, so the chosen cut belongs to J. Zero-count local choices contribute no objects.

Write delta=#R-#L and beta=0 or1. The left length is

\[
 j=\sum_{v\in L}(S_v+d_v-2+2h_v)=N+\delta+\beta+1. \tag{4}
\]

The right length is2N+2-j. Isolated labels on one side remain degree-one vertices with incident size1 and zero local genus-zero word; they are not dropped.

## C2.2: exact local and labeling weights

For an edge e let a_e>=1 be its cycle size; sum_e a_e=N. At vertex v, let a(v) be its full list of incident edge sizes, including parallel incidences separately. Then S_v=sum a(v), d_v=|a(v)|. For ordered edge slots, the number of ways to assign disjoint directed cycles on[N] is N!/product_e a_e: a uniform shuffled list of[N], cut into blocks of lengths a_e, gives each cycle assignment exactly product_e a_e rotational representations.

Using D0 and the genuine multinomial for each side's interleaving cancels every local word factorial. Hence the number of labeled cut pairs attached to an incidence shape, before correcting its shape encoding, is

\[
 N!\,j!(2N+2-j)!\prod_e A(a_e)\prod_v H_{h_v}(a(v)),
 \qquad A(a)=q(a)^2/a=a^{2a+1}/(a!)^2. \tag{5}
\]

The genus-one factor depends on all individual incident sizes; it is not replaced by a function only of S_v,d_v. No ordinary endpoint count substitutes for connected support. Uniformly sampling an unweighted graph would not have law(5).

## C2.3: code multiplicities, including trees and parallel cores

In a tree, root at the unique genus-one left vertex, which is intrinsic to the decorated incidence object. Orient each other vertex away from that root and order the k_v children at each vertex. Exactly product_v k_v! ordered codes represent any fixed labeled decorated graph. Every child branch contains a nonempty cycle-label set disjoint from the others, so there is no additional symmetry divisor, even if numeric branch shapes coincide. Give each ordered code the factor product_v1/k_v! in addition to(5). There is **no root-count quotient** in this case.

In a unicycle, the unique alternating core has2s>=2 edges. A two-parallel-edge pair is the length2 core. Choose any left core vertex as start, choose either outgoing core edge as direction, and order all hanging children. Exactly2s product_v k_v! codes represent the fixed labeled graph. The two directions remain distinct in the parallel-core case because the core edges carry disjoint, individually labeled cycles. The genus-one vertex may lie on or off the core; it does not change the2s count because we do not use it to root the core. Give each code the factor1/(2s product_v k_v!).

Equations(5) and these quotients reduce the task to sampling positive weighted numerical codes, followed by uniform cycle labeling, D0 local word sampling, and uniform side interleaving. The resulting proposal will be exactly uniform on

\[
 \mathcal A_N=\{(w,j):w\in X_N^{(2)},\ j\in J(w)\}. \tag{6}
\]

## C2.4: finite positive tables for numerical codes

Use indices (mass,delta,l,r), with mass<=N, l,r in{0,1}. Here l,r are total genera of left/right vertices. Addition adds indices; discard any product exceeding the mass or genus caps. Imbalance magnitude in a retained partial object is at most2N+2, so there are O(N^2) scalar entries per such polynomial (the genus flags contribute only4). Color c is-1 for left,+1 for right; adding a genus-h vertex shifts by(0,c,h,0) on the left or(0,c,0,h) on the right.

Let T_c[a] count planted trees of color c with one external parent edge of size a. It includes its root vertex and descendants, but does not pay the parent edge's mass or weight. At a vertex of color c, an ordered list of children consists of branches A(a)x^a T_{-c}[a]. Let F_c[k,s] denote this ordered forest's polynomial, with k children and total immediate child-edge size s. Alongside its scalar coefficient F store the weighted moments Q,E_j,W_j of the k immediate sizes. Initially k=s=0 has F=E_0=1 and all other moments0. Appending an edge of size a, with its tree coefficient multiplying every record, gives the positive updates

\[
 F'=F,\quad Q'=Q+a(a-1)F,\quad
 E'_j=E_j+aE_{j-1},\quad
 W'_j=W_j+aW_{j-1}+a^2E_{j-1}. \tag{7}
\]

Indices and branch weights are convolved exactly. These are sums over actual ordered forests, not an enumeration of subsets.

For fixed external ports P (one at a planted root, two at a core vertex, none at the whole tree root), insert their sizes into the moments with the same updates(7), without edge weight/mass. Formula(1) applied to the combined moments computes exactly

\[
 \mathcal H_h(P;k,s;I)=
 \sum_{\substack{\text{ordered child forests}\text{index }I,k\text{ children},\sum a_i=s}}
 \operatorname{weight}(\text{forest})\ H_h(P,a_1,\ldots,a_k). \tag{8}
\]

The genus-zero case is just F times(sum P+s)^(|P|+k-3). The genus-one case is the positive linear combination in(1) of the merged Q,W records. Empty size is skipped; it never represents an incidence vertex with nonempty support.

For any vertex, sum(8)/k! over k,s and h=0,1, shift its color/genus index, and retain caps. This gives T_c[a] when P=[a]. Start with no children and iterate the forest/vertex construction N times. Every child branch pays a positive edge-size unit, so a planted tree of retained descendant mass<=N has depth<=N. After N rounds all retained trees are present exactly once. Recompute the final forest tables from these exact planted tables; no missing deeper tree can contribute at retained mass.

For the whole tree case, use color left, no ports, and **force root genus1**. Retain mass N and genus totals(l,r)=(1,1). Multiply its coefficient of imbalance delta by j!(2N+2-j)! with j=N+delta+1. This sums every ordered tree code exactly once.

For the unicycle define C_c[a,b] by the same vertex formula with ports[a,b], and M_c[a,b]=A(b)x^b C_c[a,b]. The outgoing core edge is paid once here; the incoming one is paid at the preceding vertex. For each1<=s<=floor(N/2), take

\[
 \frac1{2s}\operatorname{tr}\big((M_LM_R)^s\big), \tag{9}
\]

retain mass N and genus totals(1,0), then multiply the imbalance-delta coefficient by j!(2N+2-j)! with j=N+delta+2. Positive edge size bounds all core lengths by N. The sum of the tree and unicycle masses, times N!, equals|A_N|.

These tables have polynomially many indices. The missing question is not an arbitrary-endpoint genus-two count formula: only H_0,H_1 from D0 occur.

## C2.5: actual backward parser and its exact conditional law

An explicit implementation is `cut_genus_two.py`. The following specifies the mathematical decoder independently of programming language.

First choose tree/unicycle, core length where relevant, and imbalance by their weighted top coefficients. In the tree case parse its forced genus-one root. In the unicycle case retain suffix matrix products for the chosen alternating core length; choose the closing edge-size a_0 from the appropriate diagonal coefficient, then each outgoing size b and local core coefficient with weight

\[
 A(b)\ C_c[a,b](I_{\rm local})\ 
 \operatorname{suffix}[b,a_0](I_{\rm remaining}-I_{\rm local}-(b,0,0,0)).
\]

This is ordinary positive-product backward sampling; the final suffix is the diagonal identity at zero residual index. It records each core vertex's ports and index, to be parsed below.

At a vertex with ports P and prescribed index, choose its genus h, child count k and immediate sum s by the positive mass(8)/k!, with the vertex's own color/genus shift removed from the index. To parse the actual child list, hold a list P_fixed initially equal to P. With residual index I, k children and sum s remaining, choose the **next** child-edge size a and its planted-tree index I_child with weight

\[
 A(a)\ T_{-c}[a](I_{\rm child})\
 \mathcal H_h(P_{\rm fixed}\cup[a];k-1,s-a;
 I-I_{\rm child}-(a,0,0,0)). \tag{10}
\]

Append a to P_fixed and repeat on the residual forest. Formula(8) recomputes the exact local moment sum after every forced size; selected child trees have their own prescribed indices and are parsed recursively. The original1/k! is constant after the first vertex choice, so it does not appear again in(10). This is essential: adding a new reciprocal factorial at every child would bias the law.

The forest's first-child decomposition proves that the weights(10) sum to its current mass(8). Induction over the number of remaining children proves that the child sequence receives probability proportional to its product of edge/tree weights times the **full** local H_h on all incident sizes. The sum-of-moments oracle therefore supplies a real polynomial decoder; no claim that a count automatically decodes words is used. All partial-assignment normalizers are recomputed, rather than multiplying marginal probabilities. Although algebraic moment records count auxiliary marked subsets, the actual parser samples the unmarked child list through its exact conditional masses; it neither needs to enumerate those subsets nor forgets them with a missing multiplicity correction.

The planted child mass decreases by at least its positive edge size. An explicit task stack parses all vertices; no interpreter recursion-depth setting is required. The code's `flatten_code` also uses a stack and preserves child order.

After a numeric code is sampled, uniformly shuffle[N] into the edge slots and interpret each block as a directed cycle. The rotational multiplicity is constant for that code, so this is uniform cycle labeling. Sample each local word by D0 using its full fixed endpoint and its genus. Uniformly interleave the left local words and separately the right local words. A uniform permutation of a multiset of component-color tokens gives every valid order-preserving interleaving the same multiplicity product_v r_v!, including empty local words. Concatenate. The macro decomposition recovers the local subsequences and their positions uniquely from the resulting marked word. Combining(5), the coding quotients, and the exact parser establishes the constant probability1/|A_N| of every marked pair in(6).

## C2.6: forgetting the cut and fair-bit complexity

Given a uniform marked proposal(w,j), compute J(w) by evaluating all prefixes (or all side genera). Accept with probability1/|J(w)| and discard the mark. Every fixed w has |J(w)| marked preimages, hence total accepted proposal mass

\[
 \sum_{j\in J(w)}\frac1{|A_N|}\frac1{|J(w)|}=\frac1{|A_N|}.
\]

After normalization the law is exactly uniform on X_N^(2). Acceptance is|X_N^(2)|/|A_N|>=1/(2N+1). Every proposal uses fresh independent random bits; its conditional acceptance after any failed history is the same constant, so the expected number of proposals is at most2N+1. This is a direct conditional calculation, not a product of marginal estimates.

For completeness, a conservative explicit polynomial bound follows. A polynomial indexed by(mass,delta,l,r) has O(N^2) coefficients. Forest count/sum tables have O(N^2) cells, and each coefficient carries O(N) moments; O(N^5) scalar storage suffices for these tables. A direct forest construction loops over O(N^3) triples(k,s,a), two polynomial indices O(N^4), and O(N) moment coordinates, hence O(N^8) rational operations. N depth rounds cost O(N^9). Vertex and core tables are polynomial and fit a loose O(N^10) budget. Matrix multiplication has O(N^3) size triples and O(N^4) coefficient pairs, hence O(N^7) work; O(N) core powers/suffix products cost O(N^8).

Each proposal has O(N) vertices and edges because every edge carries positive integer size and total size N. Each sequential choice in(10) considers O(N^3) candidate size/index pairs; merging at most O(N) fixed ports into O(N) moments costs O(N^2). Thus parsing is polynomial and lies below O(N^8) rational work. Allowing power calculations, branch assembly, genus checks and generous slack, **O(N^12) rational operations** bound preprocessing and each structural proposal. The imported component samplers together use polynomial time: there are O(N) components, all degrees<=N and all lengths summing2N+2; a crude sum of their inherited O(N^10 log^3(N+1)) bounds is O(N^11 log^3(N+1)) bit work per proposal.

Rational bit lengths remain polynomial. Every retained partial object has O(N) paid edges and vertices, including forests and open core paths. Parent/core ports are each<=N and local total size is<=3N. Negative size exponents in H_0,H_1 are at least-2. Each edge contributes at most two factorial denominators, each vertex at most two size denominators, one child factorial, and possibly24; the core divisor2s is<=N. All partial monomials, their moment factors, and the conditional products in(10) are covered, with slack, by the common denominator

\[
 D_N=24^{2N+4}\big((3N)!\big)^{20N+20}. \tag{11}
\]

For a conditional product, the chosen child and residual forest share a total paid-mass budget<=N; already fixed port sizes add only O(N) boundary data. Thus(11) does not multiply one full denominator per sequential step. There are exp(O(N log(N+1))) possible ordered partial objects and auxiliary markings; monomial numerators have exp(O(N log(N+1))) magnitude because total edge sizes and total degrees are O(N). The logarithm of D_N is O(N^2 log(N+1)), so every reduced coefficient or conditional mass has O(N^2 log(N+1)) bits. Positive sums cannot introduce a denominator not dividing their common D_N. Temporary products can increase this bound by a constant factor, still polynomial.

A categorical draw converts its polynomially many rational weights using their denominator lcm to nonnegative integer weights. Their common denominator bound makes these integers polynomial-bit. Draw an integer below their sum by fair-bit power-of-two rejection, with expected fewer than two trials. Exact uniform shuffles and interleavings use the same primitive. Together with the outer expected2N+1 proposals, elementary arithmetic yields, for example, the deliberately loose bound **O(N^20 log^4(N+1)) expected bit operations**, with polynomial space. No dependence on b is necessary because the law is exact. This bound is an existence/implementation audit, not a practical benchmark at large N.

## Boundaries, regressions and certification state

N=2 has the single target word(12)^6. Its two admissible cuts are j=3(tree, both genera1) and j=4(unicycle, right genus0); reciprocal-cut rejection returns that singleton exactly. N=1 has no positive-length transposition target and the public interface rejects it. The general bridge m=0, odd m and m=2 boundaries are outside this fixed genus-two interface; D0 retains its empty singleton and zero-count branches, and the coordinator's unchanged-baseline checks retain the exact general classifications. Near-minimal local factors use the full genus-zero interface without assuming nonempty side support words.

Historical counterexamples remain intact. Literal square insertion still omits(12,23)^3 and its tree extensions; C2 coverage uses genus cuts, not removable squares. Ordinary endpoint81 versus connected80 remains a support-conditioning obstruction; C2 uses connected local fibers. Unweighted graph triangle mass1/4 versus required3/4 remains a graph-bias obstruction; C2 uses(5). Parallel cores and equal-shape children have the explicit multiplicities in C2.3. Unequal |J(w)| requires the reciprocal correction. CP1's21/2000>1/100 remains a rejection of the old marginal-product argument; C2 uses exact posterior masses(8),(10) and fresh proposals.

Finite evidence: coordinator literal enumeration at N=2,3 proves finite cut totals2,4656 and checks every labeled macro against independently evaluated component counts. Author `audit_grammar.py` independently enumerates positive-size plane codes with the subtractive classical expression for H_1, intercepts the **actual production numeric parser** to enumerate its exact rational execution law, and compares every code through N=4. It finds2,10,47 codes and2,23,303 labeled macros, respectively. For N=2,3 the complete label projection agrees with the coordinator's literal reference. N=4's cut total11952000 is a grammar/inventory identity in this job, not a full literal-word enumeration. Seeded samples1729,2718 check validity only. Full exact raw results and job receipts are on disk.

**Dependency graph:** D0 -> local factors and local word decoder; elementary genus lemma -> C2.1 coverage; D0+C2.1 -> C2.2 local weights; C2.2 -> C2.3 encoding; C2.3+(7),(8) -> C2.4 grammar; C2.4+(10) -> C2.5 parser; C2.1+C2.5 -> C2.6 exact target and expected cost. A failed lemma reopens every descendant. All new nodes are author-proved/provisional pending fresh blind and exact-version review. Same-model reviews are correlated.

**First unproved mathematical step claimed by the author:** none within the stated C2 theorem under D0; the complete proposed argument and decoder are supplied. Outstanding certification is substantive nonauthor review, especially fixed-port moment conditioning, tree-root and unicycle multiplicities, and uniform polynomial bit bounds. This report does not upgrade T2 or the global mission. The unrestricted global question remains OPEN.
