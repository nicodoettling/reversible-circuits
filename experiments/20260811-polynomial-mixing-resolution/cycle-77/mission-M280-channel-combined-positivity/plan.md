# M280 plan: exact channel-combined positivity

## Objective

Resolve, or sharply reduce, the all-rank per-channel recombined-positivity
claim isolated by M274/M277.  For every admissible lag `y` and separately for
each literal M91 channel, determine the sign of the complete
gradient-plus-embedding/collision response after retaining the exact `T/D`,
`IS/IN/X`, phase, Borel-normalization, endpoint, and reflection terms.

## Source lock

Before substantive derivation, verify the frozen inventories and reports for
M161/M166, M168/M171, M174/M178, M266/M268, and M274/M277.  Record exact top
hashes and any caveats in the checkpoint.  This mission treats accepted PCS as
an input but does not infer CP from finite positivity.

## Mathematical target

1. Reconstruct a precise literal-channel formula `z_{k,y}^{(c)}` for the full
   response contribution in channel `c`.
2. State the implication chain `CP => OS+ => MS => FCL1`, specifying where
   accepted PCS is used and which quantifiers/constants are uniform.
3. Prove CP analytically, or refute it with the first exact counterexample.
4. If CP remains unresolved, isolate the weakest exact signed/minority lemma
   sufficient for FCL1 and the first standalone analytic inequality.

## Computation budget

At most one predeclared compact exact falsifier beyond the frozen `k=3,5,9`
data.  If used, it will enumerate exact rational responses for one explicitly
declared next rank/rank range solely to seek a sign counterexample.  Positive
finite results remain empirical and are never promoted to an all-rank claim.

## Deliverables

- `checkpoint.md` and `halfway_checkpoint.md`
- exact derivation/reduction document
- at most one compact exact falsifier with machine-readable output
- `report.md`, `run_manifest.md`, `freeze_manifest.md`, and `SHA256SUMS`
- a fresh-audit request for any promoted theorem

## Prohibited conclusions

No spectral-gap, polynomial-mixing, or Terminal claim follows from this
mission alone.
