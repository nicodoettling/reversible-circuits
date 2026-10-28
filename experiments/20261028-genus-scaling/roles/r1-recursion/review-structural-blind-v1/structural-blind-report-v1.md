# Independent statement-only structural review — R2-S.v1

Reviewer: r1-recursion. Scope is exactly claims S1–S4 in `roles/r2-structure/theorem-v1.md`. **Verdict: the four assertions are proved below under the statement's literal-incidence convention.** No mathematical counterexample or missing hypothesis was found within that convention. The meaning of direction on a two-edge parallel core is made explicit: its two actual incidence edges are distinguished. Forgetting that information would make the stated divisor wrong, as the N2 boundary demonstrates.

This is a limited statement-only review. Before freezing this report, the reviewer read only the supplied `input-v1.md` and the R2 theorem statement for this structural task. No R2 proof, report, finite results or coordinator structural discussion was read. The reviewer previously authored the recursive marker decoder and reviewed the coordinator's coefficient theorem in the same campaign, and shares model/context lineage. The inherited campaign context also includes the historical I1 report/reconciliation, which summarize the earlier genus-two cut construction and its multiplicity issues. Thus this is not a fresh-session blind T0 review and not statistically independent evidence. No mathematical computation or external source was used.

## 1. Definitions and elementary genus increment

A displayed word multiplies rightmost first. On the exact N labels, every prefix endpoint preserves each support component. Both its cycle count c and support-component count q include isolated fixed labels. Define

    G(u)=(ell−N−c+2q)/2,  ell=|u|.

The empty prefix has G=0. Append tau=(x y), so the new endpoint is p tau. Swapping the two successors in a permutation cuts one cycle into two when x,y belong to the same cycle, and joins their cycles when they belong to different cycles. There are precisely three possibilities:

| Positions of x,y before appending tau | Delta c | Delta q | Delta G |
|---|---:|---:|---:|
| different support components | −1 | −1 | 0 |
| same support component, different endpoint cycles | −1 | 0 | 1 |
| same endpoint cycle | +1 | 0 | 0 |

In the first case they must lie in different endpoint cycles because the endpoint preserves the support components. These cases are exhaustive. Therefore every prefix G is a nonnegative integer and G increases only by0 or1.

For each support component V, its subsequence of letters is a connected local word on V and its endpoint is the restriction of the global endpoint. The displayed formula is additive over these components:

    G(u)=sum_V (ell_V−|V|−c_V+2)/2.

Each local summand is nonnegative by the same increment argument on its exact labels. This includes the isolated singleton component: its empty word contributes(0−1−1+2)/2=0. In particular the term “total genus” in S2 is exactly the sum of the local connected genera, with no topological or classification theorem assumed.

## 2. Proof of S1: admissible cuts form a bounded interval

For a full word w in F(N,g), the endpoint is identity, c=N, support is connected, q=1, and ell=m=2N−2+2g. Thus G(w)=g. Since g>=2, a process starting at0 and moving by0 or1 must attain g−1. It does so at a positive index strictly less than m. Monotonicity implies that all such indices form one nonempty integer interval [a,b].

Throughout the interval G=g−1, so

    j=N+c_j−2q_j+2(g−1).

Subtracting at its endpoints gives

    b−a=(c_b−c_a)+2(q_a−q_b).

Every support component contains at least one endpoint cycle, hence c_a>=q_a. Also c_b<=N and q_b>=1. Because a>=1, at least one transposition has already joined two original isolated vertices, so q_a<=N−1. Consequently

    b−a <= N−q_a+2q_a−2
          =N+q_a−2 <=2N−3.

It follows that1<=|J(w)|=b−a+1<=2N−2. No estimate depending on genus is hidden in this bound.

## 3. Proof of S2: the incidence graph is a tree or a unicycle

At a cut j in J(w), let u be the prefix, v the suffix, and p the prefix endpoint. The suffix endpoint is p^(-1), so the two endpoints have the same individual cycles as label sets. Every such cycle belongs wholly to one prefix support block and one suffix support block. Use these blocks as the two vertex classes and the actual endpoint cycles as edges. Different cycles remain different edges even when their sizes and incidences agree.

There are no isolated incidence vertices, because every nonempty support block contains an endpoint cycle. The incidence graph is connected: a disconnected incidence graph would partition the actual labels into two nonempty classes which no prefix support block and no suffix support block crosses. Then no transposition in the full word could cross that partition, contradicting connected full support.

Write L and R for the numbers of left and right blocks, E=c for the number of incidence edges, and

    beta=E−(L+R)+1.

For a connected finite multigraph, beta is its nonnegative cycle rank. The total genera computed on the prefix and suffix satisfy

    G_left+G_right
      =(m−2N−2E+2(L+R))/2
      =g−1−E+L+R
      =g−beta.

Since G_left=g−1, we obtain G_right=1−beta. The right genus is nonnegative, so beta is0 or1. If beta0, the incidence graph is a tree and right total genus1. If beta1, it is a connected unicycle and right total genus0. A connected bipartite multigraph of cycle rank1 has a unique even core cycle; its length may be2, consisting of two parallel edges. This case is included, not replaced by a simple graph. All local genera are nonnegative, so right total genus0 means each right vertex has genus0.

This proves S2 including repeated/parallel incidences and empty singleton local fibers.

## 4. Inverse construction and the marked-pair correspondence

Start with a bipartite tree or unicycle, with positive edge sizes a_e summing to N. Assign disjoint exact label subsets of those sizes to its individual edge positions, partitioning[N], and on each subset choose a cyclic permutation. Let p be the permutation formed by these disjoint cycles. Each vertex receives the union of the label sets on its incident edges. Choose a connected local word on that union: on the left its endpoint is the restriction of p; on the right its endpoint is the restriction of p^(-1). Let the nonnegative local genera sum to g−1 on the left and1−beta on the right.

Within a side, distinct vertices have disjoint label sets. Their endpoint permutations therefore commute, and any order-preserving interleaving of their local words has endpoint p on the left and p^(-1) on the right. Concatenating the two side words gives identity. Each local support is connected on its assigned vertex labels; together with connected incidence this makes the full support connected on[N]. Empty singleton words cause no failure: the singleton label still lies on its incident edge and joins the union through the other support block.

At a vertex let n_v=sum_(e incident v)a_e, d_v be its incidence degree, h_v its genus and r_v=n_v+d_v−2+2h_v. Summing on the left gives

    j=sum_left r_v=N+E−2L+2(g−1)
      =N+(R−L)+beta+2g−3.

Thus the statement's delta=R−L gives exactly its asserted cut index. The right length is m−j, and total length is m because E−(L+R)=beta−1. Both side lengths are positive. On the left this follows from positive total genus g−1. For a tree the right total genus1 makes the right side positive. For a unicycle a right core vertex has at least two distinct incident endpoint cycles; any connected word on their union has positive length. Hence the produced cut is internal. Its left total genus is g−1, so j belongs to J(w).

Conversely, a literal marked pair(w,j) uniquely recovers the actual left/right support blocks, the actual endpoint cycles and their cyclic permutations, each local subsequence, and the positions defining the side interleavings. Thus before root/order coding, this is an exact bijection between marked pairs and the fully labeled local-word incidence decorations. It is not merely a correspondence of support graphs or scalar counts.

## 5. Proof of the numerical factor in S3

Fix an abstract code whose individual edge positions and child positions are distinguished. Equal numerical edge sizes do not identify positions. Assigning the actual edge label subsets gives

    N! / product_e a_e!

choices. A cyclic permutation on an assigned a_e-element set has(a_e−1)! choices. Therefore selecting all label subsets and actual endpoint cycles gives

    N! product_e 1/a_e.

The right endpoint cycle is the inverse of the chosen left endpoint cycle, so it is determined and contributes no second cycle-order factor.

For each resulting actual endpoint, the independent number of local word choices is product_v C_(h_v)(a(v)). The numbers of order-preserving interleavings on the two sides are

    j!/product_left r_v!,   (m−j)!/product_right r_v!.

Empty local words have r_v0 and0!1, with one empty placement. By definition in the statement,

    C_(h_v)(a(v))/r_v!
      =product_(e incident v) [a_e^(a_e+1)/a_e!] H_(h_v)(a(v)).

Every edge is incident to two vertices. Multiplying all factors yields exactly

    N! j! (m−j)!
      product_e [a_e^(2a_e+1)/(a_e!)²]
      product_v H_(h_v)(a(v)).

This proves the proposed raw numerical weight. The expression is a count of literal code decorations before the root/order corrections; the fact that it is written with rational H values does not authorize sampling signed or unnormalized terms. No efficient evaluation of H is asserted here.

## 6. Proof of the tree and unicycle corrections in S3

Fix one literal decorated incidence graph from a marked pair, retaining the actual cycles, local words and interleavings. Count all its root/order codes pointwise.

For a tree, choose a left root vertex v. Rooting orients every nonroot edge toward a unique parent. If k_x is the number of children of vertex x for this rooting, there are product_x k_x! child orders. The actual children/edges are distinguishable even when their sizes, genera or abstract subtree shapes agree. Each such code has correction

    h_v / ((g−1) product_x k_x!).

Summing over its child orders leaves h_v/(g−1). Summing over all left roots leaves

    sum_left h_v/(g−1)=1.

Genus-zero roots have zero weight; at least one positive-genus left root exists because the left total genus is g−1>0. Child-order factorials are recomputed for each rooting, so their possible variation causes no problem. This proves the tree quotient without dividing by the number of unlabeled graph automorphisms.

For a unicycle, remove the unique core edges. Each remaining component is a tree rooted at its core vertex, and the orientation toward the core fixes every off-core parent. If the core has2s edges, it has exactly s left vertices. There are s choices of left core start and two directions, giving2s directed core listings. Here direction is a listing of the **actual edges**, not just a vertex sequence. When s1, the two parallel edges still give two different listings. For any such choice there are product_x k_x! orders of the off-core children. Thus precisely2s product_x k_x! codes represent the fixed literal decoration, each with correction its reciprocal. Their total weight is1.

At a core vertex k_x counts off-core children; its two core incidences are already placed by the directed core listing. At a noncore vertex it counts children other than the parent. This is the ordinary meaning of the unicycle code's child orders. Counting a core edge again as a freely ordered child would describe a different code and would not satisfy the stated divisor.

The pointwise normalization proves that summing corrected raw code weights counts every literal marked pair once. It does not justify an unweighted distribution on abstract trees, unicycles or support graphs, nor does it remove any unresolved local-word or allocation oracle.

## 7. Proof of S4: reciprocal-cut rejection

The target family F is finite and nonempty. For instance, a word consisting of doubled edges of a spanning tree, followed by g additional doubled copies of one of its edges, has the required length, identity product and connected support.

Let M=sum_(w in F)|J(w)| be the number of marked pairs. Under an exact uniform marked-pair proposal, a particular word w receives accepted probability mass

    sum_(j in J(w)) (1/M)(1/|J(w)|)=1/M.

The total acceptance probability is p=|F|/M, and conditioning on acceptance makes every word's probability1/|F|. Since S1 bounds every |J(w)| between1 and2N−2,

    1/(2N−2) <= p <= 1.

Fresh proposals therefore have expected number1/p=M/|F|<=2N−2 and terminate almost surely. Acceptance1/|J| can be realized exactly with an integer uniform draw on[0,|J|), accepting one designated value. No marginal probability product or untracked posterior conditioning is involved. The assertion is conditional on the exact marked sampler; no bound on the cost of producing one marked proposal follows from this rejection calculation.

## 8. Boundary and falsification audit

For N2 there is one transposition t, and the sole target word is t^(2g+2). For a prefix length2r>=2, endpoint is identity and G=r−1. For a prefix length2r+1, endpoint is t and G=r. Therefore

    J={2g−1,2g},  |J|=2=2N−2.

The first cut has one endpoint cycle of size2 and one support block on each side: its incidence graph is a single-edge tree, with left genusg−1 and right genus1. Its only possible positive root has correction1. The second cut has two distinct singleton endpoint cycles and one block on each side: its incidence graph is exactly the two-parallel-edge unicycle, with right genus0. There are exactly two edge-aware directed core listings, each of weight1/2, totaling1. The raw numerical expression for this latter abstract shape is2 and the unicycle divisor is2, giving one marked pair. This independently tests the smallest parallel-core multiplicity.

A concrete rejected interpretation is to encode that parallel core only by its vertex sequence(L,R,L). The two directions would then collapse to one code; multiplying that single code by1/2 would undercount the unique decoration. The statement avoids this failure because it explicitly retains every individual cycle and parallel incidence. Any implementation must retain this information as well.

Other boundaries:

- For g0 the requested level g−1 is negative, so J as defined here is empty; these assertions are deliberately outside that genus.
- For g1 the increment and topology arguments can still be applied to level0, but the displayed tree root quotient has denominator g−1=0 and is not a valid formula. No g1 extension of S3 is claimed.
- The empty singleton local fiber has genus0, endpoint its fixed point, C0=1 and r0. A positive-genus singleton local fiber is empty. Such zero-count decorations contribute nothing.
- Odd identity length is impossible by sign. At length0 connected support on N>=2 is impossible. At length2 connected identity requires N2 and the doubled single edge, which is genus0 and outside the theorem's g>=2 domain.
- Equal-size child subtrees, equal cycle sizes and parallel edges are still distinguished by their actual label sets and endpoint cycles. There is no unrecorded factor1/2 for equal children.

The graph-weight bias, insertion-only failure on(ab)^3, cached-prefix CP1 and growing-genus/small-support policy obstruction remain valid against their original mechanisms. These structural statements neither invoke those mechanisms nor claim to solve their efficiency obstructions. In particular no PORT-CONTRACT, new high-genus decoder, T0/T1, all-length or mixing conclusion is made here.

## 9. Claim ledger and freeze

| Claim | Independent outcome | Load-bearing reason | Qualification |
|---|---|---|---|
| S1 | proved | exact0/1 genus increments and bounded plateau span | N>=2,g>=2 |
| S2 | proved | connected incidence and G_left+G_right=g−beta | multigraph retains actual cycles |
| S3 raw factor | proved | exact label/cycle/local-word/interleaving counts | H is a definition, not an oracle |
| S3 tree quotient | proved | weighted root sum equals left total genus | g−1>0; actual child positions |
| S3 unicycle quotient | proved | exactly2s edge-aware core listings | parallel-core directions remain distinct |
| S4 | proved conditionally | exact accepted mass1/M per word | exact uniform marked proposals assumed |
| Efficient structural sampler | not reviewed or asserted | outside assigned scope | no PORT-CONTRACT inference |

No unproved step remains in S1–S4 as stated with the literal-edge code convention. The only rejected variant found is the vertex-only encoding of a parallel core; it does not satisfy the statement's retained-incidence requirement. This report supplies an independent full argument before reading the author's evidence. Source statement and report hashes are frozen in the adjacent manifest. No mathematical job was run. The reviewer will stop after freeze pending coordinator instructions.
