# R1 Checkpoint

Status: substantive checkpoint, 2026-09-05 15:24 UTC

The target is uniform on `Omega(N,m;g)`, with public endpoint `e`. The direct
sampler uses the map convention `(alpha beta)(x)=alpha(beta(x))`.

**Proved candidate, awaiting nonauthor audit:** for identity bridges, a prefix
permutation has defect `d=N-cycles(p)<=min(i,m-i)`. Its conjugacy class is
encoded by a partition of `d`, with each part `a-1` representing an `a`-cycle
and `N-d-number_of_parts` fixed points. Positive cut-and-join multiplicities
therefore give an exact suffix-count DP on

`S <= min(sum_{d<=floor(m/2)} p(d), p(N))`

types. Exact selection of individual labeled transpositions telescopes to
per-word probability `1/|Omega|`; no class-size reweighting is needed, because
the table counts suffixes from one fixed permutation of each type.

The preliminary resulting expected bit-time bound is
`exp(O(sqrt(min(m,N)))) poly(N,m)`. Thus `m=O(log^2 N)` is a proved exact
sparse regime, and fixed `N` permits arbitrary lengths. The arbitrary-endpoint
variant uses the cone `d<=min(h+i,m-i)`, `h=N-cycles(g)`, and the same asymptotic
bound. All required endpoints are exact.

The first-appearance sampler also works, with a necessary weight correction:
a pattern using `k` labels and having `b` simultaneous pair introductions has
`(N)_k/2^b` embeddings. Using `(N)_k` indiscriminately is incorrect.
The active-label bound follows directly because every active label must occur
in at least two transposition factors.

`short_exact.py` now implements both samplers and a worst-time approximate
variant: cap each exact random-integer rejection loop and on failure return
a deterministic valid factorization of the requested endpoint. With accuracy
integer `b`, the latter has TV error at most `2^-b` and polynomial overhead in
`b`. This separates exact expected time from bounded random-bit running time.

All exact checks passed in 5.89 seconds on Python 3.12.3, standard library:
cut-and-join coefficients versus every permutation through `S6`; all 27,
120, and 3936 identity-word probabilities at the required cases; all endpoint
words on selected `S3`/`S4` lengths; minimal factorizations and pair padding;
all canonical-pattern weights; exact diagnostic laws; rank-one and rank-two
boundaries. See `results.json`. No stochastic evidence is used in the proof.

First unproved step toward an all-length polynomial sampler: eliminating the
partition-state factor while retaining positive labeled completion weights.
The present DP bound alone says nothing about computational hardness beyond
its polynomial regime.
