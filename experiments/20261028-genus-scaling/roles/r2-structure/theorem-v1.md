# R2-S.v1 — statement-only structural partial

For every N>=2,g>=2, let F(N,g) be the ordered transposition words on exact labels[N], length m=2N−2+2g, rightmost-first product identity, connected support. For a prefix u let c(u) be its endpoint cycle count and q(u) its support-component count, including fixed points/isolated labels, and set G(u)=(|u|−N−c(u)+2q(u))/2. Define J(w)={1<=j<m:G(w_1...w_j)=g−1}.

Claim S1: J(w) is a nonempty interval and1<=|J(w)|<=2N−2 for every w in F(N,g).

Claim S2: At any such cut, make a bipartite incidence multigraph from the prefix/suffix support blocks, with one edge for each individual cycle of the prefix endpoint p (the suffix endpoint is p^(-1)). This graph is connected. It is either a tree with right total genus1 or a unicycle with right total genus0; the left total genus is g−1. All individual cycles, parallel incidences and empty singleton local fibers are retained.

Claim S3: Gluing actual connected fixed-endpoint local words along these decorated trees/unicycles and uniformly interleaving each side gives a complete marked-pair representation with the following exact code weights. Define C_h(a)=r! product_i(a_i^(a_i+1)/a_i!) H_h(a), where C_h is the actual connected endpoint count, r=sum a_i+#a_i−2+2h; H_h is a definition here, not an efficient formula. If edge sizes sumN, local genera have the sums above, delta=#right−#left, beta0/1 and j=N+delta+beta+2g−3, the numerical weight before code corrections is N!j!(m−j)! product_e[a_e^(2a_e+1)/(a_e!)²] product_v H_(h_v)(a(v)). A tree rooted at a left vertex of genus h has correction h/((g−1)product_v k_v!), with k_v its children count. A unicycle code choosing a left core start, a direction and child orders has correction1/(2s product_v k_v!), where2s is the core edge count;2s=2 parallel cores are included.

Claim S4: An exact uniform sampler of all pairs(w,j), j in J(w), followed by acceptance1/|J(w)| gives the exact uniform law on F(N,g), with expected at most2N−2 fresh proposals. This assertion is conditional on the marked sampler, not an existence or complexity claim for a high-genus local decoder.

The claims imply no T0/T1 or all-length sampling theorem. They do not assert that scalar connected counts decode literal words. N2 has one word and two admissible cuts for all g>=2. g0/g1, singleton local fibers, odd identity length,m0,m2 must be treated separately. No literature dependency is assumed for these structural statements.

Review request: prove, refute or isolate a gap in the exact statements and multiplicities. The proof, evidence and coordinator opinion are intentionally omitted from this statement-only file.
