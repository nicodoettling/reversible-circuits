# LC1-v2 efficient-corollary scope repair

Both r3 and the fresh r2 reviewer independently identified the remaining missing hypothesis: an arbitrary rational-valued f need not have a public polynomial-time evaluator or polynomial-bit values. The finite probability identity and v2 operand bound remain sound. A one-coordinate rational 1/2^(2^lambda) already has exponential explicit denominator size; coordinate locality alone does not confer efficiency.

Version 3 explicitly assumes public polynomial-time f evaluation (or charged polynomial-size table), polynomial output bit bound b, and publicly computable positions I. All prior proofs and objections remain immutable. No T0/C1/C2 claim depends on LC1. Status: REPAIRED-PENDING-RECHECK; exact v3 reviews are required, not inherited from v2. Targeted denominator tests passed; the new computational interface is an explicit assumption and will be audited as such.
