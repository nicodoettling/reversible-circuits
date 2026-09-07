# R1 Plan: Short Exact Sampling

Status: active; updated 2026-09-05 15:18 UTC

Prove or refute the active-label bound, construct a positive exact sampler via
canonical first-appearance patterns, give Turing and bit complexity, and seek
a better cycle-type/cut-and-join dynamic program. Identify the largest proved
growing-length regime that remains polynomial in `N`.

Target: the uniform law on the feasible fiber `Omega(N,m;g)`, with the public
special case `g=e`. Permutations are maps and `(alpha beta)(x)=alpha(beta(x))`.
This is direct sampling, with no Markov chain or mixing assertion.

1. Prove the support bound and a canonical first-appearance sampler, checking
   the ordering constraints when an edge introduces two new labels.
2. Build the stronger positive cut-and-join recurrence using defect partitions
   and the bridge cone `d<=min(i,m-i)` for the identity endpoint. Extend to
   arbitrary endpoints only after the product convention is checked.
3. Prove exact conditional sampling by labeled-transposition lifting and give
   state, arithmetic, and bit bounds. Distinguish expected exact time from a
   bounded-time version whose only error is capped random-integer rejection.
4. Test formula multiplicities against labeled permutations; compare all
   identity-word probabilities at `S3,m4`, `S4,m4`, `S4,m6`; exercise all small
   endpoints, parity, empty words, rank two, minimal length, and pair padding.

Expected failure modes: a factor-of-two error in equal split/merge sizes;
incorrect pattern weights at simultaneous first appearances; removing a
valid suffix in a truncated defect table; using left/right multiplication
inconsistently; silently claiming worst-case exact random-bit complexity.

Reproducibility: Python 3.12.3, standard library only; repository commit
`9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc`. Exact diagnostics use no seeds.
Stochastic smoke checks, if used, use seeds 7, 20260905, and 4103.
