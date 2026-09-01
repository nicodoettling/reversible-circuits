# M198 plan: fresh immutable referee of M196

## Objective

Audit the frozen M196 claim that all 54 named `d=5`, width-two target pairs
have exact positive words in the diagonal 8,400-point `Q_5` action. Issue an
independent `ACCEPT` or `REJECT` verdict with numbered objections.

## Immutable and exact gates

1. Verify every entry of M196's `SHA256SUMS` and record its top digest before
   using any M196 conclusion. Never edit M196.
2. Load M191's frozen `q5_action.json` independently, recompute the packed
   action digest, check the fourteen permutation rows and signed inverses, and
   independently BFS the one-coordinate action from source 16.
3. Reconstruct the 54 named target inventory and chronological BFS transversal;
   recompute all adjusted second IDs and their deduplication count.
4. Parse but do not import M196 scripts. Independently audit the radius-eight
   forward ball, each stored meeting, chronological concatenation
   `f b^(-1)`, all 41 stabilizer endpoints, and all 54 complete endpoint words.
5. Check every stated count, digest, and maximum segment/word length.

## Falsification and verdict rule

Reject on a manifest mismatch, target-inventory mismatch, action/convention
error, bad meeting decomposition, failed endpoint replay, missing certificate,
or false count/length statement. Accept only if all exact checks pass. The
checker may build the 8,400-state one-coordinate action and the radius-eight
forward product ball, but it will not enumerate `Q_5^2` or a full stabilizer
orbit.

## Scope boundary

This referee concerns only the exact finite `d=5`, width-two named target list.
It makes no every-color, all-`d`, polynomial-length, spectral-gap, mixing, or
Terminal inference.

## Deliverables

Produce this plan, an initialized and halfway checkpoint, independent checker
and machine-readable results, proof audit, nine-field report with numbered
objections, freeze manifest, and complete hashes.
