# R2-S.v1 — penultimate-genus cuts have uniformly small topology

Author proof, 2026-10-28. **PROVISIONAL structural partial, pending exact-version and blind reconciliation.** This is not a proof of T0, T1-FPT or T1-QUASI. It supplies a genus-uniform marked-cut identity, a literal-word weighted representation, a uniformly polynomial mark-removal cost, and a precise remaining coefficient primitive. A conditional algorithmic reduction additionally requires actual arbitrary-endpoint local decoders; scalar counts alone do not supply them.

## 1. Frozen statement and conventions

For integers N>=2 and g>=2 put m=2N−2+2g and let F(N,g) be the ordered transposition words on exact labels [N], with rightmost-first product identity and support connected on all N labels. For any word u on this ambient set let c(u) be its endpoint cycle count and q(u) its support-component count, both including isolated labels/fixed points. Define

G(u)=(|u|−N−c(u)+2q(u))/2.

For w in F(N,g), define J(w)={1<=j<m : G(w_1...w_j)=g−1}. Then:

**S1.** J(w) is a nonempty interval and 1<=|J(w)|<=2N−2, independently of g.

**S2.** At any j in J(w), form the bipartite incidence multigraph whose left/right vertices are prefix/suffix support components and whose edges are the individual cycles of the prefix endpoint. This graph is connected and is either a tree, with right total genus1, or a unicycle, with right total genus0. The left total genus is g−1. Loops do not occur in this bipartite graph; parallel edges do occur and remain distinct individual cycles.

**S3.** The converse local-word gluing construction below covers every pair (w,j) with j in J(w), with exactly the weights and code divisors given in Sections3–4. A tree can be rooted without selecting a unique genus-positive component: root a left vertex of genus h with weight h/(g−1). The unicycle divisor remains its core length, including a parallel two-edge core.

**S4.** A uniform sampler of these marked pairs, followed by acceptance probability1/|J(w)|, produces the exact uniform law on F(N,g), with expected at most2N−2 independently refreshed proposals.

No Markov chain or mixing claim is involved. Resource variables are N,g and explicit output length; no wire-polynomial claim follows. All universal statements above are elementary candidate proofs, separate from the finite checks.

## 2. Genus increments, coverage and the stronger rejection bound

Appending a transposition on the right has exactly three cases. It joins two support components, so (length,c,q) changes by(+1,−1,−1); it splits one endpoint cycle, giving(+1,+1,0); or it joins two endpoint cycles within one support component, giving(+1,−1,0). Consequently G starts at0 and increases only by0 or1, the latter exactly in the third case. This also proves that G is the sum of nonnegative component genera, rather than assuming the connected-length criterion.

The final value of G for w in F(N,g) is g. Let i_1<...<i_g be the increment indices. Since the endpoint just before the last letter is that same transposition, the last letter splits its two-cycle; it is not a genus increment. Hence i_g<=m−1 and

J(w)={i_(g−1),...,i_g−1}

is a nonempty interval of internal cuts.

The improved bound uses P(u)=N+c(u)−2q(u). In a support component on v labels with endpoint cycle count k, its contribution is v+k−2>=0. If the word is nonempty, at least one component has v>=2, so P>=1. Universally P<=2N−2 because c<=N and q>=1. At every cut in J, the word is nonempty since G=g−1>=1, and

j=2(g−1)+P(w_1...w_j), with 1<=P<=2N−2.

Different cut positions give different P values. Thus |J(w)|<=2N−2. This is a pointwise bound, not an average extrapolated from genus2. It is sharp at N=2 for every g>=2.

Let the prefix endpoint be p, so the suffix endpoint is p^(-1). Each individual p-cycle is contained in one support block on either side, giving one edge. If the incidence graph were disconnected, the unions of labels in its components would be disjoint nonempty sets preserved by every letter of the whole word, contrary to connected support. Write E=c(p), L=q_left, R=q_right and beta=E−L−R+1. Summing the two genus formulas gives

G_left+G_right=g−beta.                                      (1)

For a cut in J, G_left=g−1, so G_right+beta=1. Both are nonnegative integers because the incidence graph is connected. The two possibilities are (G_right,beta)=(1,0) and(0,1), proving S2.

Conversely, take any connected bipartite tree with left vertex genera summing g−1 and right genera summing1, or any connected bipartite unicycle with those sums g−1 and0. Assign disjoint directed cycles partitioning [N] to its edges. At a left vertex select a connected word whose endpoint is its incident cycles, and at a right vertex select a connected word with the inverse endpoint. Give each vertex the prescribed genus. Interleave the local words in each color and concatenate. The endpoint is identity. The union of the two side support partitions is connected, so the total support is connected. Equation(1) gives genus g, hence length m; the selected cut has prefix genus g−1. Zero-count local fibers are excluded. Thus this construction produces exactly the required marked pairs, after its explicitly counted codes are identified.

Put delta=R−L. The left length is

j=N+E−2L+2(g−1)=N+delta+beta+2g−3.                         (2)

All isolated labels on a side remain degree-one vertices with a size-one incident cycle and an empty genus-zero local word. They cannot be discarded.

## 3. Exact labeled-word weights, without an assumed high-genus formula

For a fixed endpoint on a nonempty exact label set, let a=(a_1,...,a_d) be its individual cycle lengths, S=sum a_i, and r=S+d−2+2h. Define C_h(a) to be its connected ordered word count. This count is invariant under relabeling. Define the normalized number H_h by the identity

C_h(a)=r! product_i q(a_i) H_h(a),  q(a)=a^(a+1)/a!.        (3)

For h>=2 this is a definition, not a claimed efficient formula or decoder. The inherited S-G01 interface gives both evaluable H_0,H_1 and actual fixed-endpoint samplers at those genera. Singleton h0 has the empty word and count1; singleton h>0 has count0. H_h is nonnegative but its evaluation may require difficult signed coefficient computations upstream; no signed quantity is sampled here.

Let an edge e carry cycle size a_e>=1 and sum_e a_e=N. For a numerical incidence code with individually specified edge slots, assigning disjoint directed cycles to [N] has N!/product_e a_e possibilities. A uniform label shuffle cut into blocks of lengths a_e represents each such assignment product_e a_e times, from independent rotations, and therefore samples it uniformly.

At vertex v use the complete list a(v) of incident cycle sizes, retaining equal sizes and parallel incidences as distinct slots. Its local word length is r_v. The side interleavings have j!/product_left r_v! and (m−j)!/product_right r_v! possibilities. Multiplying these with (3) cancels every local factorial. The uncorrected numerical-code mass is

N! j!(m−j)! product_e A(a_e) product_v H_(h_v)(a(v)),
A(a)=q(a)^2/a=a^(2a+1)/(a!)^2.                            (4)

This counts literal labeled ordered words. It is not a uniform support-graph law, and it uses connected endpoint counts rather than ordinary endpoint counts.

## 4. Root, child-order and parallel-core multiplicities

For a tree choose any left root vertex v with h_v>0, orient all other vertices away from it, and order the k_u children at every vertex u. Give each code, beyond (4), the factor

h_v / ((g−1) product_u k_u!).                             (5)

To check this, fix a literal decorated graph, including all cycle labels and local words. For a particular root v there are exactly product_u k_u! child orders. Distinct children contain disjoint nonempty edge-cycle label sets, so these orders remain distinct even when numerical child shapes agree. The total weight of all codes with that root is h_v/(g−1). Summing over left roots gives1 since sum_left h_v=g−1. Equivalently, mark one of h_v abstract genus tokens at the chosen root and divide by g−1; no claim that a unique genus-positive root exists is made. The degree-dependent child factorials are computed for the selected root and are not replaced by one constant over all roots.

For a unicycle, its unique core has2s>=2 edges. Choose a left core vertex as start, one of its two outgoing core incidences as direction, and order every hanging child list. This gives exactly2s product_u k_u! descriptions of any fixed literal decorated graph. Give each code the reciprocal of that number. If s=1 the two core edges are parallel, but their directed cycles have disjoint label sets, so the two orientations remain distinct. No genus-based root is used in this case; positive left genus can occur on or off the core. These arguments prove S3, including all equal-child and parallel-edge cases.

## 5. A uniform-topology symbolic grammar and its precise missing primitive

The following is an exact finite weighted grammar. It does not assert that its contractions have been computed efficiently at every genus.

Use truncated polynomial indices I=(n,delta,l,r), with paid edge-size mass n<=N, imbalance |delta|<=N+1, left genus l<=g−1 and right genus r<=1. There are O(N^2 g) scalar entries. A color-left vertex shifts imbalance by−1 and left genus by its h; color-right shifts by+1 and right genus by h. Planted trees T_c[a] have one unpaid parent port of size a. A child edge and its planted tree contribute A(a)x^a T_(-c)[a]. An ordered forest consists of k such child branches, with immediate child sizes totaling s.

For fixed port sizes P, define the fixed-port forest contraction

V_h(P;k,s;I)= sum H_h(P,a_1,...,a_k) product_(i=1)^k W(a_i,I_i),       (6)

where the sum is over a_i>=1, sum a_i=s and sum I_i=I, and W is the given child-branch table, including its edge weight and paid mass. Every W entry has paid mass at least its a. The sum is over ordered children. Fixed ports include parent/core ports and all child-edge sizes already selected by a parser. Their individual values must remain present; replacing them by only their total generally loses information.

**Primitive PORT-CONTRACT.v1 (OPEN):** Given N,g, a nonnegative rational branch table W with the stated indices and polynomial-bit entries, h<=g−1, a fixed port list P of length at most N+2 and total size at most3N, and k,s,I in the stated bounds, evaluate (6) exactly in f(g)(N+g+L)^c bit operations, for absolute c, where L is the bit size of the explicit input table. Return the full nonnegative rational sum. For T0 one needs f(g)<=A C^(g+1); for T1-QUASI one needs f(g)=2^(O(g log(g+2))). An algorithm polynomial in N for each fixed h with an exponent depending on h does not meet this contract. Direct evaluation of one H_h list is insufficient.

For each vertex, sum (6)/k! over its allowed h,k,s and shift its color/genus indices. This constructs planted trees for one fixed port, and core vertex matrices for two fixed ports. Rebuild the trees for N depth rounds: every child edge pays positive mass, so no retained tree has depth exceeding N. The root tree uses no external ports and has extra factor h/(g−1), h>=1; retain total genera(l,r)=(g−1,1). For the unicycle, let C_c[a,b] be the two-port vertex table and M_c[a,b]=A(b)x^b C_c[a,b]. Sum

sum_(s=1)^floor(N/2) (1/(2s)) tr((M_left M_right)^s),        (7)

retaining genera(g−1,0). Multiply each final mass-N, imbalance-delta coefficient by j!(m−j)!, using (2), and then by N!. Equations(4)–(5) prove that the result is exactly the number of marked pairs. Matrix dimensions, genus indices, depth rounds and core lengths are polynomial in N+g, with an absolute exponent. There is no growing graph-core enumeration in this representation.

The primitive also supplies actual conditional structural decoding. After h,k,s,I are selected at a vertex, and P_fixed contains the original ports and all earlier chosen child sizes, select the next branch (a,I_child) with weight

W(a,I_child) V_h(P_fixed joined with[a]; k−1,s−a; I−I_child).          (8)

The first-child decomposition of (6) proves that these weights sum to the current normalizer. The original1/k! and any root factor are constant after the initial vertex choice and are not inserted again at each child. This is an exact posterior computation, not a product of marginal laws. Core paths use positive suffix matrix products in the same manner. After numeric-code selection, uniform cycle labeling, actual local endpoint-word sampling, and uniform side interleavings complete the literal word law.

There is an additional necessary algorithmic interface: an exact fair-bit connected fixed-endpoint word decoder for all local h<=g−1. S-G01 gives only h0/1, and the reviewed prior genus-two interface gives h2. This report does not pretend that (6), or any scalar C_h, automatically supplies the missing higher-genus decoder. Consequently the structural result alone is not a complete reduction of T0 to only PORT-CONTRACT. It isolates the sole remaining *structural coefficient* obligation, relative to the separately declared local decoder interface. A companion allocation/decoder theorem can close that interface; no such theorem is imported here.

Conditionally, if PORT-CONTRACT has f(g) times an absolute polynomial bit cost and local decoders have e(g) times an absolute polynomial bit cost, this grammar plus Section6 has (f(g)+e(g)) times an absolute polynomial expected bit cost, after replacing f,e by computable nondecreasing majorants. There are O(N) local word calls per proposal and only polynomially many coefficient queries/table entries. Actual local genera sum to at most g and their lengths sum to m. This is a uniform reduction under its two explicit algorithmic hypotheses. It is not an induction deriving arbitrary-endpoint decoders from identity decoders.

Bit size is not an additional hidden exponential-in-N obstacle in the finite structural grammar. Put K=10(N+g+2). Every local tuple has total size<=3N, degree<=3N and h<=g, so its length is<K. The integer C_h is at most binom(K,2)^K. In (3), denominators of H_h divide r! product_i a_i^(a_i+1), which divide a power of K! with exponent O(N). Every retained code has O(N) vertices/edges; child factorials, the root factor and core divisor also divide powers of K!. A common denominator (K!)^(100(N+1)^2) is therefore a deliberately loose bound for all complete or residual structural monomials. Their counts and numerators have exp(poly(N+g)) magnitude, so reduced coefficients have polynomial bit length. Previously fixed ports share the same mass budget; a new full denominator is not multiplied for every successive conditional draw. This bit-size bound does not prove the operation count requested by PORT-CONTRACT.

## 6. Mark removal and exact fair-bit law

Let A be the set of pairs(w,j), w in F(N,g), j in J(w). Assume the marked sampler is exact. A proposal(w,j) has probability1/|A|. Accept it with probability1/|J(w)| and forget j. Every fixed w then has accepted mass

sum_(j in J(w)) (1/|A|)(1/|J(w)|)=1/|A|.

Thus the normalized accepted law is exactly uniform on F(N,g). The overall success probability is |F(N,g)|/|A|>=1/(2N−2). Every proposal uses independent fresh fair bits. Conditional on any failed history its acceptance probability remains this same constant, proving the expected proposal bound2N−2 without a marginal product argument. Exact rational categorical draws and the acceptance coin can be realized with uniform integers from fair-bit power-of-two rejection, with fewer than two trials in expectation. Explicit output costs at least Omega(m log N) bits and is included in the conditional polynomial.

## 7. Why the balanced-core alternative was not used

The initially considered cut with left genus a in[1,g−1] gives beta=g−a−G_right<=g−a. This is valid coverage but needlessly allows increasing excess. For beta>=2, prune leaves and suppress degree-two vertices of the incidence graph. The reduced connected multigraph (loops now allowed) has minimum degree3, at most2beta−2 vertices and at most3beta−3 edges, by 2E>=3V and E−V+1=beta. It has at most2^(O(beta log(beta+2))) combinatorial kernels, including color/parity data. This f(g) abstract-kernel count alone does not establish FPT: directly assigning sizes in[1,N] to its O(beta) endpoint ports costs N^(O(beta)), and tensor contraction on the kernel can have the same issue. This is a limitation of that implementation, not a lower bound or a refutation of T0. The penultimate cut removes this topology issue entirely while leaving higher local genus.

Nor does repeatedly invoking a fixed-genus polynomial bound establish an absolute degree exponent. If local decoder exponents depend on h, the present structural reduction inherits that dependence. No recursive exponent has been silently renamed f(g).

## 8. Boundaries, regressions and dependencies

For N=2 the only word is(12)^(2g+2). Its two admissible cuts are j=2g−1 (tree, right genus1) and j=2g (two parallel edges, right genus0). Thus the2N−2 bound is attained, including all g>=2. g0 and g1 are outside the new theorem and use their separate inherited interfaces; the root divisor g−1 is never used at g1. Odd identity length is empty by sign. Connected N>=2,m0 is empty; connected m2 forces N2. Singleton local genus0 is empty-word count1; positive-genus singleton counts vanish and must be rejected. Local factors near minimum length retain their true connected endpoint counts.

Mandatory negative findings remain: ordinary endpoint81 is not connected count80; uniformly weighted support graphs have the wrong triangle mass1/4 instead of3/4; (ab)^3 has no adjacent square and is not covered by square insertion; equal numerical children remain distinguishable after labels; parallel core edges yield two orientations; forgetting nonconstant cut counts is biased; CP1 has joint21/2000>1/100 and survives the smaller later residual21/221, invalidating the old marginal-product rule; M-GROW's low-genus/small-support policy obstruction remains unchanged. This report makes no global bridge-policy claim.

Dependencies: S1–S4 and weight/code identities are elementary and need no Hurwitz transitivity or literature formula. The symbolic grammar uses H_h defined by actual connected counts, not an accepted all-genus evaluator. Efficient h0/1/h2 counts/decoders retain their exact prior scoped provenance. The conditional algorithm depends explicitly on PORT-CONTRACT and the arbitrary-endpoint decoder interface. All new structural claims are author-proved/provisional, not independently certified. Changing a weight, root convention or primitive reopens its downstream algorithmic claims.

First unproved structural algorithmic step: PORT-CONTRACT.v1 for unbounded h, with the declared absolute polynomial exponent and fair-bit-compatible bit costs. Separately, literal local endpoint decoders beyond the accepted range are required. No T0, T1 or complete single-primitive T2 acceptance is claimed by this role.
