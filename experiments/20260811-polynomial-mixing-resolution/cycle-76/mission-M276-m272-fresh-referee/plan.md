# Mission M276 plan: fresh referee of M272

Date: 2026-08-14 UTC.

## Objective

Perform a clean-room immutable referee audit of frozen M272 signed endpoint
transport.  Verify the declared M272 inventory digest and every cited
dependency; independently reconstruct the raw laws, channel normalizations,
coupling and telescoping identities, cyclic-phase factor, phase partition,
finite refutations, proved variation bounds, and surviving open obligations.

## Scope and discipline

- M272 is read-only and its advertised `SHA256SUMS` digest must equal
  `af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3`.
- This referee directory is the only writable mission scope.
- The audit is independent of M274 and does not use M272 code or generated
  data in any compact checker.
- Every claim is labeled proved, exact finite, refuted, conditional, or open.
- Raw channel laws and normalizations are checked before derived coupling or
  variation claims.
- Any compact falsifier is independently implemented from mathematical
  definitions, predeclared, exact, and restricted to the smallest decisive
  ranks.
- No FCL1, bridge-gap, mixing, or Terminal conclusion is inferred.

## Audit plan

1. Read the repository source-of-truth files, then locate M272 without opening
   its payload and verify its top-level digest.
2. Verify M272's inventory and all cited immutable dependency inventories.
3. Independently derive the two raw channel laws and their probability
   normalizations.
4. Audit the `q`-to-`p` monotone split coupling, the `-D` crossing identity,
   and endpoint telescoping, retaining every boundary term.
5. Audit the cyclic phase `1/n`, literal phase partition, and the exact scope
   of any seam/pathwise refutations.
6. Audit the channel-one bounded-variation estimate and the channel-two
   triangle/vector Abel endpoint calculation.
7. Isolate the first open statements among CIBV, CSBV, CEBV, and DOR.
8. If needed, run only a predeclared independent compact checker, then freeze
   an accept/reject report, audit request, and checksum inventory.

## Expected failure modes

- treating an expectation transport identity as a pathwise order;
- losing a factor `1/n`, `1/2`, or a normalized conditional mass;
- reversing the sign of `D` in the crossing law;
- dropping singleton, cutoff, or shared-endpoint terms in Abel summation;
- using finite phase data as an asymptotic proof;
- silently promoting a surviving conditional BV statement.

