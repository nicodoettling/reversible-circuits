# Substantive checkpoint / finalization

2026-09-05 15:29 UTC. Status: proved, final report frozen for independent audit.

The requested dense scale is achieved: q=floor(m/[2N(N-1)]) >=4ceil(log_2 N) gives TV <=min(1,3N^2 exp(-q/144)), uniformly over feasible arbitrary endpoints, in expected polynomial Turing time and with exact endpoint and length. Thus m>=2N(N-1)ceil(144 log(3N^2/epsilon)) suffices.

The decisive new lemma replaces the historical factorial bridge-conditioning loss by O(r), using the fact that discarded branches are old-long and their old endpoint completion counts are already pointwise smoothed. Exact token projection then gives a rank factor. Simple summable rational floor increments give the binomial tail exp(-q/144), without exceptional large-N conditions.

Completed deterministic checks: 11,202 rational floor cases; 48,252 all-word probability checks, including all three required small instances; 8,028 projection identities; 533,416 orientation equivalences; new numerator/denominator survival inequalities at all 360 feasible endpoints of S6,L380. Zero failures. Script and compact machine-readable results retained in this directory.

Remaining work for the run: fresh nonauthor audit and coordinator synthesis. The present theorem does not solve arbitrary smaller accuracy at fixed length or infer hardness of the uncovered intermediate regime.
