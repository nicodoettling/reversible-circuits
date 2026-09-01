# M69 halfway checkpoint

Date: 2026-08-12.

- The frozen `report.md` hash is exactly
  `f817b7dbd9f13101b805fb3a5134633bb5f7df9e252f9ab85f3b9ea7472e4b99`,
  and `sha256sum -c SHA256SUMS` accepts every listed M65 artifact.
- Independent rational recomputation accepts the two-chain terminal count,
  the negative-hypergeometric `J` law, the integrated closed-mean identity,
  the fixed-cut Dirichlet energy, the rank-two Green norm, and the telescoping
  extreme-context weight.
- The exact rank-two absorption ratio is
  `(K-2)^2/[9(K+1)]`: it is `121/126` at ambient `r=15` and first exceeds one
  at `K=14`, ambient `r=16`, where it is `16/15`.
- A finite sparse solve of all 2,275 feasible tuples below ambient `16` found
  no earlier failure; its maximum ratio is the exact rank-two value `121/126`
  and its maximum reported CG residual is below `1e-12`.
- Fresh exact-context reruns through ambient `r=5` found zero failures in 120
  closed-mean composition checks and zero failures in 44 nonvacuous marked
  inheritance checks.
- The proof of the uniform constant excess retains the correct Green and
  Dirichlet normalizations.  The literal outer fibre has inverse-polynomial
  pointwise escape, so the scalar failure still does not furnish a `Pbar` or
  `K` slow mode.

Preliminary verdict: **ACCEPT**, subject to final wording that distinguishes
the exact first failure in the exhibited rank-two family from the numerical
finite exclusion of all other smaller contexts.
