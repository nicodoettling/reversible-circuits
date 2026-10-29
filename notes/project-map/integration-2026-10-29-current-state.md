# Current-State Commit and Remote Reconciliation

Date:2026-10-29, Europe/Berlin. This is a documentary merge/maintenance receipt,
not a new mathematical review, research run or acceptance.

## Preserved Histories

- Local snapshot0251cd7 commits all22 previously modified/untracked research
  and maintenance paths from main1650532. It includes the campaign programme,
  compatibility notes, map-tooling changes, foreground projection experiment,
  and run mission/runbook documents. No runtime directory or credential file
  was staged. The pre-merge validator and all23 maintenance tests passed.
- Remote main8b61d5a preserves the colleague's five additional research commits
  through7640534 and the complete noisy-bridge campaign history through35ad3c2.
  Its proofs, scripts, raw results and full reviews remain byte-for-byte intact.
- Four overlapping paths needed reconciliation: PROJECT_MAP.md, COVERAGE.md,
  catalogue.json and inventory.json. Both sides' catalogue families and records
  were retained. Generated views were regenerated, not manually combined.
  The primary entry remains PROJECT_MAP.md, not the campaign-local FRONTIER.md.

## Check Depth and Pending Work

The existing source/version hashes, claims, statuses, dependency edges and
referee bindings from both histories were not refreshed or upgraded. The
new catalogue families acknowledge the foreground bridge-projection experiment
and completed sparse-noise viability study as pending full mathematical map
integration. Run documents are grouped as operations; research artifacts remain
hashed evidence, not excluded telemetry. The generic research-campaigns family
retains its explicit pending disposition for saved scientific outputs.

The October25 preparation and October28 compatibility documents remain frozen
historical records. Their old unlaunched/READY statements are not current
permission to start or resume anything. This merge itself launches no research.
Isolated campaign worktrees remain excluded from this primary inventory. In
particular, the genus-scaling findings still live in their separate committed
branch; a local runbook does not import that whole result or certify its proof.

New discovery since the remote inventory consists of the foreground experiment,
the previously published noisy-bridge artifacts and frozen inputs, four run
documents, and an ignored machine-local settings file recorded only as an
operations fingerprint. No local settings contents are added to Git. There
were no missing files, changed inventoried research bytes or new ledger/mission
branches in the pre-refresh drift. Classification changes are limited to the
new pending families and the four operation-document paths.

Full proofs were not re-audited for this current-state commit. Prior run reports
and exact-version adjudications retain their own scoped claims and limits.
No blanket all-length sampler, local mixing theorem, sparse-noise security,
or general impossibility is introduced by the merge. Coverage limits and the
need to reconcile newer branch results before reusing historical targets remain
explicit. A discovery baseline acknowledges files, not their truth.

## Verification

The reviewed discovery baseline is regenerated with this receipt, followed by
deterministic rendering. Required checks:

```sh
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-10-29-current-state.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
git diff --cached --check
```

These checks validate evidence fingerprints, catalogue structure, links,
discovery, rendering and maintenance behavior. They are not proof certification.
The user explicitly authorized committing and pushing the full current state;
that permission does not authorize a background restart or successor run.

## Concurrent Remote Update

The first push of the reconciled state13d1e43 was safely rejected because the
remote advanced to37141a8 while checks were running. That history includes
a43bdc9, the relaxed heat-bath comparison and logarithmic correction-budget
investigations. The second merge retains their exact records, proofs, raw
results, source hashes and historical integration receipts. This consolidation
does not upgrade their provisional review scope or claim a general mixing bound.

Only generated COVERAGE.md and inventory.json needed conflict resolution in
that second merge; both were regenerated from the merged catalogue/filesystem.
The new discovery consists of the twelve experiment files, while the shared
experiment-workflow reference has the colleague's committed additions. The
discovery receipt acknowledges those bytes, not a fresh mathematical audit.
The existing local programme and campaign-runtime exclusions remain in place.
All validation, freshness, rendering and23-test checks are rerun before push.
