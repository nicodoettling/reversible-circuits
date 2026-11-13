# Planted-subsequence diagnostic integration

Date: 2026-11-10, Europe/Berlin.
Starting commit: `c4331bada5575f58ad463e62479ff20015305759`.

The user explicitly requested one experiment on the new planted assumption.
This selects Q4 over the historical mixing-only GOAL_SPEC for this foreground
investigation; no archived campaign was resumed. Historical AGENTS/GOAL_SPEC
and the current map disagree on irreducibility status, as already documented
by the map. This work uses neither disputed irreducibility nor any gap bound.

## Scope and status

The complete Q4 formulation, earlier projection and noise reports, new
self-contained arguments, checker code and exact outputs were inspected.
The compressed feature histograms were parsed and used to reconstruct the
reported acceptance probabilities. The separately written audit imports no
main-check code. All work is same-agent; there is no independent proof review.

Retain exact planting and likelihood reductions, a complement attack, exact
finite diagnostics and a fixed-length statistical limit. A concrete recursive
computational sampler is conditional on short exact bridges and an explicitly
stronger nonuniform planting assumption at every internal scale. The original
uniform single-sample reduction and any secure schedule remain unresolved.
Minority evidence (a weaker repetition signal at N3,m12,k6) and recursive bias
accumulation are retained. No hardness assumption or new theorem is accepted.

## Map and workflow changes

Extend the research-questions coverage family to the bounded experiment and
link its report from the front page. Q1-Q3 remain proposed directions.
Preserve all 60 mathematical records, 165 pinned sources, dependencies,
priorities and other route descriptions. No source fingerprint is refreshed;
no mathematical descendant is upgraded or invalidated by this diagnostic.
No manuscript or historical HANDOFF changes are needed for this scope.

The project skill's experiment reference gains narrowly scoped checks for
hidden conditioned mixtures and recursive-law composition. The skill-creator
validator passes. Its mathematical detail remains in the experiment, not the
skill entrypoint. Before integration the map validator passed and discovery
reported only the new experiment and this known skill-reference modification.

## Reproduction and evidence

```sh
python3 -B experiments/20261110-planted-subsequence/check.py
python3 -B experiments/20261110-planted-subsequence/audit.py
python3 -B experiments/20261110-planted-subsequence/recursive_check.py
python3 -B /home/hadi98/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/reversible-circuit-sampler
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-10-planted-subsequence.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
```

The first two mathematical runs pass: 34 exact planting cases plus boundaries,
and independent S4,m8,k4 literal counting. The recursive run passes all 12
complete laws and one-level consistency checks. Parameter lists, Python
version, seeds (sampler smoke only), timings and script hashes are in the JSON
outputs. The final map checks are recorded below after baseline acceptance.

Artifact fingerprints at integration:

| Artifact | SHA-256 |
| --- | --- |
| `audit-results.json` | `ad4893062d66f5a1d3d59526b7d3fcee53a687eaee636c5304c56414c2ffe686` |
| `audit.py` | `f359d9bbd29c66fa94427f44b8eb42333a4a05d50c495f77585a8e3ac9eae1ff` |
| `check.py` | `a37175a62714c57aa334f2df81432a50f9310a2892962738021d6b8f11070724` |
| `claim-ledger.md` | `54d8a2767a8e1db1773c9ac14070a80c33d9f34b63e3ad629ef01dccc6b38f3d` |
| `feature-histograms.json.gz` | `d84a40dd0b8cbd7f3720fb0ac84c5fa43daa27f2e4b5af5824f11f857a6cda2e` |
| `plan.md` | `d06c61cec358a898b67437c8ad6435f90a44ea4e1f3dc60b4f5e9ae282b9e6ae` |
| `proof.md` | `5d943d762663d0b42a75d74f59a24abfac1c1a3896989581d1ebd957742fae28` |
| `recursive-results.json` | `dce3105f3b6f13e8f1809400242d36b05f7fc6734de808ee5b3a23ae949134aa` |
| `recursive_check.py` | `08f3ee81f5ff39f699261251a67b28af237622c62d36efe24ad465579d5d13c8` |
| `report.md` | `c490d7f5424ae8daf2c3d4f83d171694cb84c90e01e7ff6cfcd7c913502888e2` |
| `results.json` | `faae74930f6b701ab75d93b94c6d527cbb1520738b273bf7516059c380c831c1` |

## Complete changed-file list

- `.codex/skills/reversible-circuit-sampler/references/experiments.md`
- `PROJECT_MAP.md`
- `notes/project-map/COVERAGE.md`
- `notes/project-map/catalogue.json`
- `notes/project-map/inventory.json`
- `notes/project-map/integration-2026-11-10-planted-subsequence.md`
- `experiments/20261110-planted-subsequence/audit-results.json`
- `experiments/20261110-planted-subsequence/audit.py`
- `experiments/20261110-planted-subsequence/check.py`
- `experiments/20261110-planted-subsequence/claim-ledger.md`
- `experiments/20261110-planted-subsequence/feature-histograms.json.gz`
- `experiments/20261110-planted-subsequence/plan.md`
- `experiments/20261110-planted-subsequence/proof.md`
- `experiments/20261110-planted-subsequence/recursive-results.json`
- `experiments/20261110-planted-subsequence/recursive_check.py`
- `experiments/20261110-planted-subsequence/report.md`
- `experiments/20261110-planted-subsequence/results.json`

## Final verification

All four map checks pass: 60 records and 165 pinned sources validate;
freshness is clean; rendered views match; all 25 maintenance tests pass.
The skill validator and `git diff --check` pass. A structural comparison
confirms all prior mathematical records, sources and non-navigation project
fields are unchanged. Script hashes match the executed JSON results.
