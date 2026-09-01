# M171 plan: fresh immutable referee of M168

Date: 2026-08-13.

## Objective and frozen target

Audit the frozen M168 fixed-cell phase-collapse reduction at
`cycle-38/mission-M168-fixed-cell-fcl1/` without modifying or importing its
implementation.  The target is only M73's nonlazy cyclic rank-two quotient
kernel under the uniform minimal long-cycle factorization law, for `n=3k`,
odd `k>=3`, at the balanced sources and the first separated physical cell.

## Hash gate

Before accepting any claim, independently check the supplied SHA-256 digests
for M168's `report.md`, `phase_collapse_reduction.md`, `freeze_manifest.md`,
and `SHA256SUMS`, and verify the manifest payload inventory.  Repeat the gate
immediately before freezing M171.

## Proof audit

Check the generic-edge iff; the ordered-pair counts
`g_i(g_i-1)-2a_i` and `2g_i g_j`; the completion sizes and retention of all
`IS/IN/X` topology; the normalization in `(PCS)`; the physical-cell factor
`1/2`; `(TV-close)` including its length factor; and the identities and
quantifiers in `(NEG-id)` and `(SC)`.

## Independent finite audit

Write a clean-room standard-library checker using raw supported rank-two
pairs and direct permutation/completion arithmetic.  It must import no M168
code and must reconstruct only `k=3,5`.  Compare its exact signed phase sums
against the frozen M168 output only after construction.

## Scope and verdict rule

Report exactly `ACCEPT` or `REJECT`, with numbered objections.  Treat all
finite positivity as finite only.  Both `(PCS-bound)` and `(FD-bound)` remain
open unless independently proved.  Make no direct-L1, gap, identity-chain,
mixing, or Terminal inference.

