# M100 plan: fresh referee of M94

Date: 2026-08-12.  Scope: frozen M94 package only, with accepted M73/M91
interfaces used solely to identify inherited assumptions.

## Decision target

Issue `ACCEPT` or `REJECT` on M94's claimed strict obstruction reduction for
the balanced family `n=3k`, odd `k>=3`.  The target law is uniform on minimal
length-`n-1` transposition factorizations of the long cycle, and `bar K` is
the nonlazy rank-two quotient correlation kernel.  It is not the identity-word
heat-bath kernel.

## Audit obligations

1. Verify the frozen `SHA256SUMS`, assigned report/proof/compact hashes, and
   absence of unfrozen dependencies in the retained claims.
2. Re-derive the raw Borel kernel and quotient convolution, explicitly
   retaining triangle/double lift factors and all cyclic stabilizers.
3. Check both Abel limits, including the error uniformity needed for
   `u -> infinity`, `u=o(k)`.
4. Recount the four colored encodings of the central-double event, verify its
   exact mass and limiting constant, and recheck the Cauchy implication.
5. Audit the stationary minimum-residual shell envelope and its multiplicity
   factors.
6. Build a fresh exact checker independent of M94 code for `k=3,5`; check the
   retained compact `k=11` payload algebraically and against an independent
   event-mass computation.
7. Treat `(BD)`, `(BA2)`, direct signed L1, H0, all bridge gaps, and both
   Terminals as unresolved unless a complete new proof is found.

## Falsification rules

- Any lost orbit-size or raw-lift factor is material.
- Finite positive `k^2 Delta(E_k)` is not an asymptotic sign theorem.
- The Cauchy lower bound is conditional on `(BD)` and cannot itself refute
  `(BA2)`.
- A stationary shell-mass bound alone is not a direct L1 estimate.
- The final report will state numbered objections, commands, dependencies,
  exact/floating status, hashes, and cache hygiene.
