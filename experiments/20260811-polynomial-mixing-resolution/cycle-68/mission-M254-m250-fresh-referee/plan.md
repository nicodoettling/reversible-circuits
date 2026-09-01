# M254 plan: fresh referee of M250

## Objective

Independently audit the frozen M250 metric-pruning/root-seam reduction without
editing M250 or importing its conclusions.  The audit checks the exact DPS
source, accepted M244 Theorem 3.1, and the M247 repair obligations.

## Target and claim labels

- Ultimate sampler target: the global fixed-length uniform law on
  `Omega(N,m)` for the lazy exact same-product block heat-bath chain with block
  lengths `{3,4,5}`.
- Immediate proof target: a deterministic combinatorial implication from the
  stated root-seam path transducer (RSPT) to the repaired root-slot matching
  invariant (RSMI+) and the initial-defect lemma (IDL).
- No mixing, irreducibility, spectral-gap, routing-length, or Terminal claim is
  under test.
- Every conclusion will be labeled `proved`, `conditional`, `empirical`,
  `refuted`, or `unresolved`.

## Frozen input

M250 is immutable.  Its claimed top inventory digest is
`243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7`.
The audit first verifies every inventory entry and this top digest.

## Checks

1. Reconstruct the DPS definitions and conventions from the original source.
2. Recheck accepted M244 Theorem 3.1 and M247's counterexample/correction.
3. Derive, without assuming M250's conclusion:
   - canonical metric pruning `E_a -> S W^(R_a) S S`;
   - child distance-three and ordinary child rows;
   - open common-nonchild `h_r^2` and disjoint endpoint;
   - boundary conditions and exclusion of edited `x_v`;
   - the exact logical status of `RSPT => RSMI+ => IDL`.
4. Replay only M250's four predeclared `d=7` rows and symbolic token identities.
   This is a finite falsification check, not proof and not a census.

## Expected failure modes

- A digest mismatch or undeclared post-freeze edit.
- Reuse of the rejected M244 Proposition 5.1/RSMI.
- A hidden seam, endpoint, or edited-vertex case in the token reduction.
- A conditional RSPT statement presented as an unconditional IDL proof.
- Finite rows used to infer a universal statement.

## Deliverables

`checkpoint.md`, `proof_audit.md`, `report.md`, `freeze_manifest.md`, and
`SHA256SUMS`, with an `ACCEPT` or `REJECT` verdict and numbered objections.

