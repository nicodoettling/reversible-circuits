# R2 cut sampler, version C1 (PROVISIONAL; worker proof complete)

Frozen target T0: for every N>=2, exact uniform sampling of ordered length 2N transposition words with product id and support connected on all N labeled vertices. Permutations compose rightmost first. N=2 is the singleton repeated edge. There is no Markov chain. Polynomial time means expected bit time in N, hence suffices for every accuracy input b.

## C1.1 Imported genus-zero count, audited normalization

For a fixed permutation p on a fixed v-set, with k cycles of sizes a_1,...,a_k, write r=v+k-2. The number F0(p) of connected transposition factorizations of length r is

F0(p)=r! v^(k-3) product_i a_i^(a_i+1)/a_i!.

At v=1 this is the empty word and the expression is 1. Source: Vakil, *Genus 0 and 1 Hurwitz numbers*, Section 1.2 defines c^g_alpha for a fixed permutation, G^g_alpha=c^g_alpha/product alpha_i; Corollary 1.5 gives the displayed g=0 expression after multiplication. https://math.stanford.edu/~vakil/files/g01hurwitz.pdf. Word reversal switches multiplication convention and preserves connectedness; the count is unchanged. This input counts words, with no completion-oracle assumption.

## C1.2 Genus-zero word sampling by final deletion

For v=1 return empty. For every transposition t=(a b), let q=pt. Delete the last factor from a connected minimal factorization of p.

If a,b lie in different cycles of p, q merges them. The prefix is connected and genus zero, so its count is F0(q).

If a,b lie in the same p-cycle, q cuts it into two distinguished daughter cycles A0,B0 containing a,b. A prefix has exactly two support components, both genus zero, with these daughter cycles on opposite sides. Assign each other (distinguished) cycle to A or B. If their total A size is u and their count is h, the complete A component has size vA=|A0|+u and cycle count kA=1+h; vB=v-vA and kB=k+1-kA. The number of interleaved prefixes for this specific assignment is

(r-1)! vA^(kA-3) vB^(kB-3) product_(cycles C of q) |C|^(|C|+1)/|C|!.

An integer knapsack counts assignments by (u,h), and backward sampling is uniform among the assignments in the selected cell. Choose t and cell with the displayed count times the cell's assignment count. Independently recurse on the two restrictions of q, interleave their words uniformly, and append t. In the merged case recurse on q and append t. The last factor and the actual two prefix support components recover the branch uniquely. Telescoping gives probability 1/F0(p) for every word.

To justify the exhaustive deletion cases: the prefix support has at most two components because adding one edge makes it connected. The genus formula is g=(length-v-cycles+2components)/2. For merged q it equals components-1, and monotonicity under appending bounds it by final genus zero, forcing one component. For split q it equals components-2, so nonnegativity forces two components. Their genera add to zero. The endpoints a,b must be in opposite components, since t connects them. Conversely every branch listed reconstructs a connected genus-zero factorization of p.

## C1.3 Everywhere-defined cuts

For any word u on the fixed N-set, including isolates, put g(u)=(|u|-N-c(eval u)+2q(u))/2. Under appending a transposition this increases by one exactly when it joins distinct permutation cycles inside an already connected support component, and otherwise stays fixed. Every target word has one forward and one backward genus-creation event. Let h be the forward index and b the backward index in original coordinates. Then b<h, and the cuts J(w)={b,...,h-1} are exactly the cuts with both side genera zero.

At cut j, let p be the prefix endpoint and let QL,QR be the support partitions of prefix and suffix. Every p-cycle belongs to one block on each side. It yields an edge of the bipartite incidence multigraph B joining those blocks. The graph is connected because QL join QR is the full partition. Summing the two genus formulas gives gL+gR=V(B)-E(B). Thus inside J the graph is connected unicyclic. Outside J it is a tree. Equality b=h is impossible: the same factor would have to join cycles in both opposite directions. This rederives M97 Sections 3--4; no transitivity theorem is used.

Conversely choose any connected bipartite unicyclic multigraph whose edges are disjoint labeled cycles partitioning [N]. At each vertex take a connected genus-zero factorization of the permutation formed by its incident cycles, using inverse cycles on the right. Interleave left words and right words separately and concatenate. Its product is id and its support is connected. If VL,VR are the vertex counts, the lengths are j=N+VR-VL and 2N-j. Every such cut pair is obtained uniquely up to the chosen coding of its incidence graph.

## C1.4 Positive local macro weight

For edge e let its cycle size be a_e>=1, with sum a_e=N. For vertex v put S_v=sum_(e incident v)a_e and d_v=degree(v), with parallel edges counted separately. Let

A(a)=a^(2a+1)/(a!)^2,   f(S,d)=S^(d-3).

For a graph with ordered edge slots the number of assignments of disjoint labeled cycles to those slots is N! product_e1/a_e. Uniformly permuting [N], cutting blocks of lengths a_e, and interpreting each as a cycle samples those assignments uniformly, since each has product_e a_e list representations. Genus-zero counts and the two uniform interleavings then give the weighted incidence object mass

N! j!(2N-j)! product_v f(S_v,d_v) product_e A(a_e).

The N! is common to all objects. This formula includes size-one cycles and isolated side blocks (a degree-one vertex with incident size one, whose internal word is empty).

## C1.5 Encoding and correction

Every connected bipartite unicyclic multigraph has an alternating core cycle of length 2s>=2; a parallel-edge pair is the length-two core. Choose a left core vertex as start and one of its two core edges as outgoing. This gives exactly 2s encodings. At every vertex order the children off the core, or away from the core at noncore vertices. The child branches have disjoint nonempty cycle label sets, so there are exactly product_v k_v! child orderings, with k_v the number of children. These facts remain true in the parallel-edge case because the two core edges have disjoint labeled cycles.

Give each ordered code the local weight above times product_v1/k_v! and 1/(2s). Forgetting the code is therefore exactly uniform counting on cut pairs (w,j). Reject a proposed cut pair with probability 1-1/|J(w)| and then forget j. Each word receives mass |J(w)|/|A_N| times 1/|J(w)|=1/|A_N| before normalization. Acceptance is |X_N|/|A_N|>=1/(2N-1), since J is nonempty and contained among the 2N-1 internal cuts. Thus the rejection overhead is polynomial and output is exactly uniform, provided the weighted codes are sampled exactly as specified below.

## C1.6 Polynomial weighted-code DP

Use formal variables x for total edge-size mass and z for color imbalance (#R-#L), truncating x degree at N and z exponents to [-N-1,N+1]. Put color signs epsilon_L=-1, epsilon_R=1. For a planted subtree whose parent edge has size a, let T_c[a] include the root vertex and its descendants, but exclude the parent edge's weight and size. Let B_c=sum_(a=1)^N A(a)x^a u^a T_other[c][a]. Let F_c[k,S]=[u^S]B_c^k, the ordered list of k child branches of total immediate edge-size S. Then

T_c[a]=z^epsilon_c sum_(k,S) (a+S)^(k-2) F_c[k,S]/k!.

The k=0 term is a^-2. Since every child branch contains a positive-size edge, coefficients at mass d depend only on T coefficients of mass <d. Compute them in ascending d. For a core vertex with incoming/outgoing edge sizes a,b,

C_c[a,b]=z^epsilon_c sum_(k,S) (a+b+S)^(k-1) F_c[k,S]/k!.

Define M_c[a,b]=A(b)x^b C_c[a,b]. The total weighted code polynomial for a core with 2s edges is trace((M_L M_R)^s)/(2s). Sum over 1<=s<=floor(N/2). Multiply the coefficient at (x^N,z^delta) by (N+delta)!(N-delta)!. This gives |A_N|/N!.

All operations are additions, products, and explicit positive rational weights on polynomially many indices, each bounded by O(N). Every child edge carries at least one unit of x-degree and core length is <=N. Weighted backward parsing samples a top coefficient, matrix-product path, core vertex child list, and recursively planted trees with their exact local weights. This is an explicit finite arithmetic grammar, not a bijection-only assertion.

Here is a conservative explicit resource audit. A planted object with retained descendant mass <=N has at most N edges and N+1 vertices; a forest has at most N edges and 2N vertices (each planted root is incident to its parent edge). Partial core matrix paths of positive mass <=N have at most N core edges/vertices and at most N attached edges, hence at most 2N vertices even before closing. The argument a+S in a planted weight is <=2N, and a+b+S in a core weight is <=3N. Every local negative exponent is at least -2. Every denominator in a single partial-object monomial therefore divides

D_N=((3N)!)^(12N+4).

Indeed, at most N edge weights contribute two factorial denominators each; at most 2N vertex weights contribute two linear-size denominators each and one child factorial each; and a core quotient contributes a factor 2s<=N. This bound has slack. No sum creates a new prime denominator: a sum of rationals whose denominators divide D_N still has denominator dividing D_N. The number of unlabeled ordered positive-edge-size trees, forests, and core paths at mass <=N is at most exp(O(N log N)); their positive numerators are at most exp(O(N log N)), since the sums of edge sizes and degrees are O(N). Consequently all retained fractions, including side factorials and positive branch sums, have O(N^2 log(N+1)) bits. Transient unreduced fractions have at most twice this bound. In the genus-zero sampler the branch weights are integers counting actual prefixes, bounded by binom(N,2)^(2N), and the subset tables have entries <=2^N. Their rational evaluation has the same conservative polynomial-bit bound.

A Laurent polynomial uses O(N^2) coefficients. Forest tables have O(N^2) pairs (k,S); their direct construction uses O(N^3) polynomial multiplications, or O(N^7) rational operations. Start planted trees with their mass-zero root terms. Recompute forests and trees N times: each iteration extends the permitted tree depth by one, and every tree of descendant mass <=N has depth <=N. Thus the literal implementation uses O(N^8) rational operations to obtain all tree/forest tables. Core matrices take polynomial work within that bound. A matrix product has O(N^3) polynomial multiplications, hence O(N^7) rational operations; O(N) products compute every retained core length and every suffix table used in a draw. This is O(N^8) rational operations per proposed cut. Powers can be precomputed for all bases <=3N and exponents -2,...,N, and factorials can be precomputed; an unoptimized exponentiation adds only O(log(N+1)) factors.

Backward sampling chooses one of polynomially many branches at each of O(N) graph vertices. The genus-zero sampler has exactly one nonempty recursive call per output factor (every call appends its final transposition), thus O(N) nonempty calls in total over both sides. Each call enumerates O(N^2) transpositions and builds O(N^3)-work subset tables, hence O(N^6) elementary exact work in total. All recursive descriptions can be executed with explicit stacks using polynomial space. Side interleaving chooses uniformly among color strings; shuffling the repeated-color list gives each such string the same product-of-factorials multiplicity.

For every categorical draw, take the least common multiple of the polynomially many weight denominators, producing polynomial-bit nonnegative integer weights. Draw an exact uniform integer below their sum using independent fair bits; power-of-two rejection takes fewer than two attempts in expectation. Every proposal uses fresh bits, so reciprocal-cut rejection has the constant conditional acceptance |X_N|/|A_N| at every trial; no multiplication of marginal success bounds is used. Its mean number of trials is at most 2N-1. A conservative total bound is O(N^9 log(N+1)) rational operations on O(N^2 log(N+1))-bit operands. With schoolbook arithmetic and Euclidean reduction this is bounded, for example, by O(N^15 log^4(N+1)) expected bit operations. The exponent is deliberately loose; only polynomiality is claimed. Output size is O(N log(N+1)) bits.

Combining C1.1--C1.6 proves the mathematical existence of an exact uniform expected-polynomial-bit sampler for T0, conditional only on the displayed classical Hurwitz count. Every imported normalization and every new construction is still subject to fresh nonauthor review before coordinator acceptance.

## Status and regressions

C1 remains provisional pending fresh nonauthor review. Direct finite word multiplicities, macro totals, and boundary cases passed in results.json: N=2,3,4 target counts 1,240,131040 and cut counts 1,336,234720; every macro count matched (1,9,101 macros), and every terminal branch matched direct genus-zero enumeration (2,54,6792 full words). Literal adjacent-square insertion remains rejected: (a b)^3 for intersecting transpositions a,b on three labels has no adjacent square, and adding doubled edges of a tree preserves zero connected-deletion fibers. M97 cuts cover these words. Code prototypes accept an RNG object; the theorem interprets its random draws as independent fair-bit draws, while the seeded smoke tests use Python's deterministic PRNG solely for reproducible validity checks.
