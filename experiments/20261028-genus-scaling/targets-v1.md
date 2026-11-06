# Frozen targets — v1, 2026-10-28

T0: For integers N>=2,g>=0, F(N,g) consists of ordered transposition words on the exact labels [N], rightmost-first product identity, support connected on all N labels, length m=2N-2+2g. Seek one uniform exact fair-bit algorithm and absolute constants A,c,C>0, C>1, with expected bit time <=A C^(g+1)(N+g+2)^c. Explicit output; count bit operations. Constants do not depend on N or g. T0 is OPEN.

T1-FPT (separate acceptable partial target): same distribution with expected f(g)(N+g+2)^c time for absolute c and uniformly computable f. T1-QUASI: f(g)=2^(O(g log(g+2))). Neither N^(O(g)) nor g3 alone establishes these. T2-REDUCTION: an exact reduction isolating one concrete genus-dependent coefficient/allocation primitive, with complete literal-word law and remaining complexity obligation. T3-APPROX: TV<=2^(-b) with the same explicit N,g dependence times poly(b), with absolute N exponent.

AUX-ENDPOINT.v1: fixed endpoint sigma on a nonempty exact label set of size N, k individual cycles; connected ordered words of length N+k-2+2g, product sigma. It is a separate auxiliary target, not an assumed conditioning oracle. Singleton has only the empty genus0 word. Identity odd lengths are empty; connected N>=2,m0 empty; N2 has one word at each feasible even identity length; m2 connected only N2. No mixing, wire-polynomial, global all-length or uniform graph claim follows.

Prior reviewed genus0/1/2 inputs are source-scoped internal acceptances; same-model reviews are correlated. The growing-genus policy obstruction M-GROW remains valid. Any claim upgrade requires full proof, checked imports, blind statement report, exact-version nonauthor audit and finite falsification checks. A failed sufficient method does not refute T0.
