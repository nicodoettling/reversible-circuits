# M151 plan: fresh referee audit of M147

## Objective

Independently audit the frozen M147 all-suffix scalar-envelope artifacts without modifying them. The declared target is the auxiliary unweighted right-heavy reset recurrence used in the scalar proof route, not the original `{3,4,5}` heat-bath chain.

## Frozen inputs

Verify the six coordinator-supplied SHA-256 values for M147's report, proof note, checker, JSON output, freeze manifest, and `SHA256SUMS` before relying on their contents.

## Checks

1. Reconstruct the exact finite `(kappa,D)` recurrence, including every attachment count `j`, invalid-child killing, and reset terms.
2. Check the root mass and first-moment identities and the scope of the corrected one-power majorant.
3. Derive the `L=1` formula independently and certify the exact `K=31/32` threshold and fractions.
4. Verify reachability of the bad states as `j=1` children and equality of all scalar data named in the obstruction.
5. Audit the fixed-moment parity theorem, including its limitation to unrestricted measures.
6. Implement a clean-room exact rational checker and give a numbered `ACCEPT` or `REJECT` verdict.

## Boundaries

No edits outside this M151 directory. No claim about the original Markov chain, `ROOT-MEAN`, a spectral gap, polynomial mixing, or a terminal resolution.

