# R4 plan — v1

Target: global Unif(Omega(N,m)); rightmost-first permutation composition. Exact H0 retained mass uses a fixed top-level K. No Markov kernel or mixing claim.

1. Implement connected positive count recurrence independently and cross-check tiny counts against labeled permutation walk DP with proper-component subtraction. The positive recurrence remains an imported mathematical dependency; agreement does not prove it.
2. Build full-active-support coefficients F[s,m] and evaluate Z(N,m)=sum_s binom(N,s)F[s,m]; do the same after the H0 component restriction. This avoids an unnecessarily large N grid.
3. Derive and validate marked component identity E X_(v,ell)=binom(N,v)binom(m,ell)C(v,ell)Z(N-v,m-ell)/Z(N,m). Record exact first/second moments and excluded mass. Separate size> K, genus>=2 and their intersection, and component-length tails.
4. Tiny cases include N=1,2; m=0,2,odd; (3,4),(4,4),(4,6), high-genus small supports and forced small cutoffs. Wider actual-K cases must include at least one nonzero tail.
5. Send counterexamples or stress cases to proof workers. Check any proposed tail inequality exactly before reporting. No finite data extrapolation.

R3 owns full literal-word/law enumeration and its heavy slot. R4 owns count/certificate grids, initially supervised timeout 120 seconds maximum.
