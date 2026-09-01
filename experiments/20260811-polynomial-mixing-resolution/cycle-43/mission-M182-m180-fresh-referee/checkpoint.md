# M182 Checkpoint

## Start checkpoint

- Assignment directory initialized before substantive auditing.
- Required project sources read: `HANDOFF.md`, `GOAL_SPEC.md`, the complete
  reversible-circuit-sampler skill, `sampling-problem.md`, and
  `experiments.md`.
- Scope fixed to a fresh immutable audit of M180.  M180 has not been edited.
- Next mandatory gate: verify M180's supplied hashes and complete manifest
  before relying on or drawing conclusions from its contents.

No mathematical verdict has yet been reached.

## Halfway checkpoint

- **Immutable gate passed.** `sha256sum -c` accepted every M180 artifact.
  Recomputed hashes match the supplied report, proof, manifest, and checksum
  hashes exactly.
- **Series rederived.** With `x=1/d`, the first two coefficients of
  `log(e^2 tau(d-2)/tau(d))` are `3` and `17/6`; exponentiation gives
  `17/6+3^2/2=22/3`.
- **Decomposition rederived.** The exact affine expansion gives
  `B=2nQ-7/2-2I_D+R`. The sharper centers imply `u_r=O(1/d)` and the
  recentered `w_r=O(1/d)`, which bounds every displayed term of `R`
  uniformly, including positive two-run boundaries.
- **Signed projection rederived.** The raw identity
  `eta(s)=a(s)delta_k(s)/R_n` makes `M_r(d)` the literal signed component
  pushforward. Its two count moments, size moment, total variation at most
  six, and the `d>n/2` tail follow without channelwise absolute values.
- **Incidence identity rederived.** Ordered lift averaging and centrality of
  the full transposition class give `bar K W=2H/(n-3)`; hence the exact
  `eta(Q)` and `eta(H)` identities imply the stated BIR equivalence.
- **Clean-room computation passed.** A new standard-library script using
  literal permutations, exact fractions, and formal `E` polynomials checked
  only `k=3,5`. It imports no M180 code or data. It checked all source-row
  normalizations, raw coefficient normalization, moments, response
  decomposition, and `KW` on 64 and 810 source-accessible states.

Provisional verdict: `ACCEPT`, subject to writing the numbered nonmaterial
exposition qualifications and completing freeze/hygiene checks. `(SCBR)`,
`(BIR)`, `(BR)`, PCS-bound, and every downstream claim remain open.
