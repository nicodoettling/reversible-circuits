# M172 Fresh Referee Plan

## Objective

Independently audit the frozen M169 root-monodromy and relative-orientation claims without editing its payload.

## Frozen target

`cycle-38/mission-M169-d5-stabilizer-voltage/`

## Scope

1. Verify `SHA256SUMS` and `freeze_manifest.md` before drawing conclusions.
2. Audit the quotient identification
   `R_d=(Z_d x [d])/S_d ~= Z_d/Stab(d)`.
3. Audit root-fiber monodromy under a transporter `rho`, including the inverse and parity convention.
4. Audit the tuple claim that the relative sign image is exactly `V_stab`.
5. Audit the relative-orientation quotient `O_(d,s)=Z_d^s/P_(d,s)` and the fixed-physical-endpoint/coboundary caveat.
6. Audit the claimed exact sequence
   `1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1`, checking definitions, kernel, and surjectivity.
7. Use only bounded symbolic/minimal independent checks. Do not attempt `d=5` closure, routing, spectral gaps, or any terminal claim.

## Deliverables

- `checkpoint.md` and `halfway_checkpoint.md`
- compact independent checker/results if useful
- nine-field `report.md` with numbered objections
- `freeze_manifest.md` and `SHA256SUMS`

## Claim labels

Every audited statement will be labeled proved, conditional, empirical, refuted, or unresolved. M169 remains immutable.
