# M294 halfway checkpoint

Status: initialized before inspection of M291.

The audit directory and scope are fixed. No M291 payload or predecessor ledger has yet been inspected. The next phase is a clean-room hash/inventory check followed by independent algebraic and counting verification.

## Halfway update

- M291's top digest is exactly `cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0`; its seven listed payloads all pass, and there are exactly seven payload files besides `SHA256SUMS`.
- All 20 cited frozen predecessor inventories reproduce their displayed top digests; all 166 payload rows pass. M13's two observed artifact hashes also match.
- The M13 component hypothesis applies: `w_Q`, `tau_i(w_Q)`, and the doubled-star chart all have the single labeled component `[d]` of weight `2d-2`. Each endpoint frame therefore has length at most `50d(2d-2)^3`.
- The exact chart convention, framed-stabilizer identity, same-rank action-image equality, physical-color normalization, paired-tree count, and injective-preimage lower bound have been independently reconstructed with no material objection.
- The proof remains strictly a common-prefix paired-chart obstruction. Stabilizer cancellation prevents any inference about the number of genuine common-schedule classes.

