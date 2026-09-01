# M332 plan — fresh immutable audit of M325

Date: 2026-08-14 UTC

## Mandate

Audit frozen M325 only, without editing M325, its dependencies, coordinator files, or any other mission. The verdict will be `ACCEPT` or `REJECT` with numbered material and nonmaterial objections.

## Immutable gate

1. Initialize this plan and `checkpoint.md` before opening M325.
2. Read the required project guidance and relevant proof conventions.
3. Verify M325's top `SHA256SUMS` digest is exactly `8fe1b7f9cf1ab650422eecee67c97ff6afa0f0608659a6bd0decce592358b882`.
4. Verify its exact 12-payload inventory and every cited source-ledger payload.

## Independent proof audit

- reconstruct the full-signature, owner-truncated AOTI/TOEC setup, retaining all middle and boundary phases and common mass;
- independently derive the analytic `k=5,u=2,ell=2,T=mu_5` negative seam signature `{{(1,0),(2,0),(12,2)}}` and its mass lower bound `8/125`;
- check that every positive nested state has owner size at least two, so the negative signature has no same-signature positive mass;
- check that this refutes TOEC exactly, and nothing stronger;
- check the active-owner identity AOTI and the conditional implication `AOEC => GQAC`, including quantifiers and scope.

No `k=15` guard, new rank, new transport, replacement grouping, or search is authorized.

## Deliverables

Dependency audit, proof audit, report, run/freeze manifests, `SHA256SUMS`, and a request for fresh integration review. Run `git diff --check` and report every owned change.
