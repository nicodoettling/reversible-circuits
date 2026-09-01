# M172 Halfway Checkpoint

Date: 2026-08-13 UTC.

## Immutable provenance

The frozen M169 payload passed its complete checksum list. Frozen M141/M143,
M154/M158, and M163/M164 checksum lists also passed. No predecessor file was
executed, imported, or modified.

## Proof findings

- **PROVED on direct audit:** the diagonal quotient
  `R_d=(Z_d x [d])/S_d` is naturally `Z_d/Stab(d)` and has `d` points over
  every absolute class.
- **PROVED on direct audit:** if `h.w=rho.w`, then the induced root-fiber
  permutation is `rho^(-1)`. Taking inverses does not change sign.
- **PROVED on direct audit:** `Z_d^s/P_(d,s)` is the regular
  `F_2^s/Delta` relative-orientation cover of `Q_d^s`, and the stabilizer
  deck-monodromy image is exactly `V_stab`.
- **PROVED on direct audit:** for fixed physical endpoints, zero route voltage
  is equivalent to orbit equality of their relative-orientation lifts.
  Independent endpoint changes translate the displayed class by the endpoint
  coboundary; simultaneous paired relabeling preserves it.
- **PROVED from accepted M141/M154 inputs:** for an accepted nonempty `d>=5`
  matching subfamily, every `p in P_(d,s)` is the root monodromy of an inner
  quotient loop. Hence `P_(d,s)<=K_mon`. Relative sign maps `K_mon` onto
  `V_stab`, with kernel `K_mon intersect P_(d,s)=P_(d,s)`, proving the exact
  sequence and the full-preimage identity.

## Bounded independent falsification

The clean-room `S_3` checker found `|Z_3|=24`, `|Q_3|=4`, twelve rooted
cover points, and zero failures in 72 inverse-monodromy root checks. For one
ordered distinct quotient pair it found `K_mon=P_(3,2)` of order 18,
`V_stab=0`, and the two relative-orientation lifted orbits predicted by
`W_2/V_stab`. All 3,456 sampled exhaustive-in-alpha endpoint-relabel checks
obeyed the exact coboundary formula.

## Interim verdict

Accept M169 at its exact qualitative, nonterminal scope. Full `d>=5` voltage,
specified quotient routing, word length, every gap, and every terminal claim
remain unresolved.
