# M286 plan: fresh referee audit of M282

## Objective

Independently audit M282's claimed proof of the channel-two seam bounded-variation obligation `CSBV`.  The target is only that analytic lemma in the fixed-length uniform transposition identity-bridge program; `CEBV`, `DOR`, `PBV`, `FD`, `FCL1`, the spectral gap, polynomial mixing, and Terminal A/B remain unresolved.

## Immutable-referee protocol

1. Record this plan and an initial checkpoint before opening any substantive M282 artifact.
2. Verify the frozen M282 `SHA256SUMS` top digest
   `cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7`, its exact inventory, and every declared predecessor ledger before relying on it.
3. Independently reconstruct the exact Abel collapse, the `U_r` support-pair disintegration, the two-seam phase embedding, and the resulting `CSBV` vector.
4. Audit the analytic proof, especially the claimed uniform bound `TV[Z_r-B_r] <= C/R` for `r=1,2`, active/inactive cutoff, midpoint, reflected support, and zero endpoints; the cancellation `sum W = -sum q delta = O(k^-2)`; and low/bulk/junction variation of `A_s`, including `k=3`.
5. Verify that the abstract coefficient bounded-variation lemma implies exactly `CSBV`, without importing any downstream inference.
6. Build one compact clean-room exact checker, importing no M282 code, solely to falsify convention and boundary errors.
7. Issue `ACCEPT` or `REJECT` with numbered material objections, freeze all referee payloads, omit caches and temporary files, and hash the exact inventory.

## Expected failure modes

- a hidden endpoint term in the Abel transform;
- a normalization or reflection error in the support-pair kernel;
- loss of uniformity at `r=1,2`, the active/inactive cutoff, or the midpoint;
- a false cancellation or insufficient rate for `sum W`;
- an untreated low-rank or seam-junction exception;
- promotion of `CSBV` into a downstream lemma not proved here.

## Scope boundary

This mission does not modify M282, any predecessor, coordinator files, the manuscript, `HANDOFF.md`, `GOAL_SPEC.md`, or the project skill.  Its maximum positive conclusion is `CSBV` alone.
