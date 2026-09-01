# Mission M243 plan: fresh audit of M241

## Objective

Freshly and immutably referee frozen mission M241's three ratio lemmas `R1`,
`R2`, and `R3`, including only their stated numerical implications
`SG=128` and `GG2=70`.  The only permissible positive verdict is acceptance
of those local estimates.  This mission will not claim `YCM`, `WBE`, `DE`,
any downstream theorem, polynomial mixing, or a terminal resolution.

## Source lock

- Repository operating guide and project skill.
- `HANDOFF.md`, `GOAL_SPEC.md`, the sampling-problem reference, and the
  experiment standard.
- Frozen M241 directory
  `cycle-62/mission-M241-ycm-ratio-lemmas/`, verified against its full
  `SHA256SUMS` inventory and top digest
  `07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936`
  before substantive audit.
- Only frozen predecessor artifacts explicitly cited by M241, with their
  hashes checked before use.

## Audit obligations

1. Verify the complete M241 frozen inventory and provenance.
2. Re-derive the exact domain and proof of `R1`, including monotonicity of
   `rho_n`, product indices, Stirling bounds, and the constant `36`.
3. Re-derive `R2` and `R3`, including normalization of `q_s`, all absolute
   values, empty ranges, the small-`k` boundary, and the product-prefactor
   estimate.
4. Verify that the three lemmas imply exactly the advertised local constants
   `SG=128` and `GG2=70`, without importing any larger `YCM` assembly claim.
5. Write and run a compact clean-room boundary checker importing neither M241
   code nor M241 data.
6. Issue an explicit `ACCEPT` or `REJECT` verdict with numbered objections;
   then freeze audit, checker, results, report, manifest, and hashes.

## Falsification policy

Search first for convention, index, normalization, sign, support, small-case,
and empty-range failures.  Any material gap in a stated lemma or numerical
implication forces `REJECT`.  Numerical agreement alone cannot prove a
uniform estimate.
