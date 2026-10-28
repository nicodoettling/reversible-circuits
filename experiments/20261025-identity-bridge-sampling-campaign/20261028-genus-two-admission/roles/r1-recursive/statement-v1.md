# R1-T2.v1 — frozen candidate statement, 2026-10-28 10:57 UTC

Status PROVISIONAL; frozen before full derivation/code validation. Coordinator review owns acceptance.

For every nonempty canonical finite label set V, every permutation sigma of V, and integer g in {0,1,2}, let F(V,sigma,g) be the connected ordered transposition words of length r=|V|+c(sigma)-2+2g whose rightmost-first product is sigma. The singleton g=0 fiber contains the empty word; singleton positive-genus fibers are empty. There is one explicit exact fair-bit sampler for every nonempty such fiber, rejecting zero fibers, with expected bit time polynomial in v=|V|. A conservative proposed bound is O(v^11 log^3(v+1)). No claim concerns time polynomial in log(v), arbitrary g, global identity bridges, or a Markov kernel.

Named auxiliary obligations:

- R1-D2: the elementary final-edge decomposition remains disjoint and exhaustive at g=2; same-cycle connected predecessors have g-1, disconnected genera are (0,2),(1,1),(2,0).
- R1-C2: normalize Goulden–Jackson 1999 Theorem1.1 to a fixed permutation and derive the positive marker formula in proof-v1.md. It uses marker weights a²(a−1)(5a−7), a², a²(29a−25), plus ordinary weight a, on positive integer cycle sizes a.
- R1-A20: every arbitrary partially forced labeled-cycle allocation mass for (2,0)/(0,2) is polynomially computable by the marker DP.
- R1-A11: every arbitrary partially forced labeled-cycle allocation mass for (1,1) is polynomially computable by the tensor of the genus-one marker transitions. No subset or endpoint inventory enumeration is used.
- R1-W2: exact integer branch selection, sequential allocation, recursive children and uniform order-preserving interleavings cancel to the constant probability1/Cg(alpha) for each literal word.
- R1-B2: table entries, counts and rational denominators have O(v log(v+1)) bits, and the total operation count is polynomial.

Primary inputs: S1.v2 and its exact-version audits for g<=1; Goulden–Jackson, The Number of Ramified Coverings of the Sphere by the Double Torus, and a General Form for Higher Genera, JCTA88(1999)259–275, Theorem1.1 and Lemma3.1/Corollary3.2. Normalization from its Hurwitz encoding and weighted conjugation-orbit formula must be checked explicitly. All proposed extensions remain provisional pending source verification, finite falsification, fresh blind report and exact-version nonauthor review.
