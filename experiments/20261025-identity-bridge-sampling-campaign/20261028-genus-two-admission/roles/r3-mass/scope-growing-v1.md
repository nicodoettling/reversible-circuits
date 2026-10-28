# Separately admitted scope M-GROW.v1

Frozen 2026-10-28 10:55 UTC before writing the new corollary proof. Coordinator explicitly admitted this scope after receiving the finite-bound proposal. Original FG.v1 and M2 are unchanged.

For each integer j>=64, N=2^(8j), m=2^(6j), and every integer 0<=G<=2^j, let E_(G,L) retain every nontrivial support component with genus g<=G OR size v<=L, where L=max{1<=v<=N:3^v<=(N+m+2)^4} is fixed at the original input. Proposed conclusion: U_(N,m)(E_(G,L))<=2^(-1-jm/2). Thus every law confined to that event has TV error at least1-2^(-1-jm/2).

Explicit analytic sufficient conditions to prove: k=m/2, x=k/N^2, q=3Nx<=1/2, b_L*x<=1, and6G^3*x<=1/16, with b_v=(v^3-v)/36. The finite component-count estimate must hold for varying G without hidden constants. G=0 is included with an empty positive-genus sum. Negative genus is infeasible, not an included branch.

This corollary does not say those growing-genus components have an efficient decoder. It bounds a larger hypothetical output support and therefore remains a support obstruction. It neither upgrades the older all-N blind report nor proves failure of all global algorithms. New proof status remains provisional pending fresh blind and exact-version nonauthor review.
