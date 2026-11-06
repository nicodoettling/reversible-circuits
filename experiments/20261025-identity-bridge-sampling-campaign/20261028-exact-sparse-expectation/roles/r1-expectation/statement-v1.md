# ES.v1 and ES-LOG.v1 — frozen author statement

Status PROVISIONAL / INTEGRATION PENDING, frozen for attention handoff on2026-10-28. No theorem acceptance.

One unrestricted exact algorithm, the current R2 PreparedExact sampler, is defined for every N>=2 and even m>=0 and outputs a uniform explicit ordered transposition identity word on canonical[N]={1,...,N}, with rightmost-first composition and independent fair bits. Odd lengths reject.

There is one absolute constant A such that the algorithm has expected bit time at most A(N+m+2)^14 on each of these separately preserved regimes:

1. ES.v1: m^3<=N^2.
2. ES-LOG.v1: m<=N^(2/3)ln(N)/4.

The runtime theorem uses the exact current R2 law/cost argument and the full expectation proof-v1.md. It does not test either analytic inequality in the algorithm. Exactness yields TV0 for every b>=1 without accuracy-dependent choices. No polynomial worst-case running-time or worst-case memory claim is made, and no all-length expected-polynomial bound is asserted.

A standalone analytic consequence of the inherited marked-component tail is: whenever E X_v<=N c rho^(v-1)/v^3 for feasiblev>=2 and fixed integera>=2 has a*rho<1,

E sum_nontrivial_components a^v <=N c a^2 rho/[8(1-a*rho)].

The explicit common proof-only constant K=1+9^(2^2048) bounds E sum9^v by K N^2 throughout the union of the two regimes; it is never computed by the algorithm. R2's conditional P^12*9^v cost therefore gives the exponent14. Production full-law validation and fresh blind/exact-version review remain unfinished. The main all-length campaign mission is OPEN.
