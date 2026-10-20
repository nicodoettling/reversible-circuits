# Support-marginal audit integration, 2026-10-15

Prior commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`. The user
explicitly narrowed the objective to the support-graph marginal of the
actual walk. This audit preserves vertex labels, gate multiplicities and
the existing mixed all-pair kernel. No extra fiber-resampling algorithm,
agents, packages, commits or pushes.

## Scope and review

Add HB-SUPPORT-MARGINAL version 1, provisional. The new record distinguishes
correct weighted stationary marginal, exact lumpability, averaged projection
mixing, and actual observed-marginal mixing. Finite counterexamples refute
the automatic closed-graph transfer, not the user's rapid-mixing conjecture.
An observable-space sufficient inequality is conditional and not recorded
as a proved growing-N bound. Earlier positive S3 cases are preserved.

All six author artifacts were inspected. The exact script passed on 4766
words in the declared six fibers. Minimal N4 channels were also checked
by hand; all-N projection identities and the four-state counterexample
are proved directly. This is same-author work, not independent review.
Blumberg arXiv:1109.3915v1, Definitions 2 and 5, was inspected only to
identify the standard split-merge state space. Its theorem is not applied
to the circuit-support problem. No prior source hash, accepted status,
research artifact or target ranking changes.

## Discovery

Baseline validation of 46 records and 93 sources, freshness, rendered
views and all 19 map tests passed before the new research files. Candidate
inventory `/tmp/reversible-support-marginal-candidate.json` is reviewed
for the six-file delta. The family is covered explicitly, with no
exclusion changes. All current changes and preserved dirty files are
listed in the new report.md.

## New source fingerprints

- `experiments/20261015-122824-support-marginal-audit/proof.md`: `b5fa342412699d47dc3e56dd0d26f24f8a4b51f1541014f01598a58b2a48cc2a`.
- `experiments/20261015-122824-support-marginal-audit/check.py`: `53276eaacdf4a49ee684e90fc1c0e01fa43c8a325c5f6dcc772a0a8e24f169bc`.
- `experiments/20261015-122824-support-marginal-audit/results.jsonl`: `2dd0db68b72b2f118f62141073ad8a9479d6952f608275e045488c5072925b2e`.
- `experiments/20261015-122824-support-marginal-audit/plan.md`: `3a0272984ead141a65790344128fdfc021a6daa558507a1e2bb14fffb3d3e22e`.
- `experiments/20261015-122824-support-marginal-audit/report.md`: `64f56da12cdac2f196afa2e116a3bc165c6f6c8719eab21bdc584f1a49f91ea7`.
- `experiments/20261015-122824-support-marginal-audit/claim_ledger.md`: `c8b0286dd4ec29d046d45a835df5d5be46ba316e6f84a1a6a114934ca738b5af`.

## Final checks

Completed: validation passed for 47 records and 99 pinned sources;
freshness reported no new, missing or changed entries; deterministic
views and all 19 map tests passed. Retrieval of HB-SUPPORT-MARGINAL
preserved the distinction between failure of lumpability and the open
marginal mixing rate. `git diff --check` passed; `git status --short`
matched the complete changed-file inventory in the report. The reviewed
discovery delta contained only the six new research files and no edits
or deletions of prior research artifacts.
