# Adjacent-gap attempt claim ledger

All proved statuses are same-author proofs, pending independent review.
Exact certificates are reproducible checks, not independent certification.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| K_A has inverse-polynomial gap for full-cycle m=N+1 | unresolved | none asserted | proof.md Sections 4-6 | no finite extrapolation | do not claim the user's conjecture proved |
| For every endpoint and length, (1/2) E_Q2 <= E_KA <= E_Q2 | proved | declared half-lazy kernels | proof.md Section 1 | 20375 words and 229196 directed channels, exact rational ratios | keep |
| Every nontrivial length-three endpoint fiber has gap(K_A)>=1/24, uniformly in N | proved | complete four-type classification and conditional-projection algebra | proof.md Section 2 | exact LDL certificates for three minimal types; symbolic arrowhead calculation plus N=2,...,12 transposition checks | keep with length-three scope |
| Transposition-endpoint three-gate generator has gap exactly 1/3 for N>=4 | proved | generator (I-E1)+(I-E2), unnormalized | proof.md Section 2.1 | explicit exact eigenfunction and all conditional states through N=12 | keep; distinguish from K_A normalization |
| The problematic conditional case can be excluded from full-cycle m=N+1 | refuted | outside-tail conditioning | proof.md Section 4 | every triple word embeds, checked N=4,...,12 | reject this shortcut only |
| Three-gate local gap closes the elementary local-to-global inequality | refuted for this argument | direct expansion in equation (5) needs delta>1/2 | proof.md Section 4 | delta=1/3 has an explicit eigenfunction | retain negative result; does not refute polynomial mixing |
| E_Q3 <=24 E_KA and E_KA <=2 E_Q3, globally for m>=3 | proved | exact length-three conditional Poincare bound | proof.md Section 3 | normalization/overlap counting checked analytically | keep reduction; Q3 polynomial gap unresolved |
| At full-cycle m=N+1, gap(K_A)>=3/[N^(N+3)(N-1)^2(N+1)^3] | proved | prior vertex-sweep construction; checked full-cycle count | proof.md Section 5 | tightened normalization length tested on N=3,4,5 fibers | keep explicitly exponential bound |
| Normal-form path length proves polynomial congestion | unjustified inference, not used | missing load control | proof.md Section 5 retains the state-count factor | no claimed certificate | reject inference |

Decision: **continue-local-chain**; run classification **proof-progress**
for the short-block theorem and constant-factor reduction, while the main
requested growing-N theorem remains **inconclusive**. No alternate sampler
or spectral experiment is substituted for K_A.
