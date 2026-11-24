# Output-only planting follow-up integration

Date: 2026-11-17, Europe/Berlin.
Starting commit: `7c2a54f833158bdb4fe4b4fec6f8de8c743f60a2`.
The initial workspace was clean.

## Authorization and scope

The user requested a mathematical investigation of planting pseudorandom
circuits or functionality, with no heavy experiments, then explicitly chose
only input/output access to the final circuit. This is a foreground follow-up
to the earlier planting question, not a launch of the historical GOAL_SPEC
mixing campaign. No agents, experiments, sampler changes, commit or push were
used. Map maintenance checks are the only executed tests.

## Evidence and review depth

Read the earlier scaling proof/report in full, the earlier subsequence
proof's model, bijection and likelihood sections, current project navigation,
and relevant source-of-truth/manuscript passages. The new note was authored
and checked directly for its stated coupling, reduction and group-counting
arguments. The external PRF definition was checked in Barak's author-hosted
lecture; no unverified literature theorem is a premise of the new lemmas.
There is no independent proof review or novelty claim.

The principal distinction is the adversary interface. The earlier explicit
gate attacks remain valid at their original scope. If both final circuits
compute identity, their oracle behavior is equal. A hidden input region has
an elementary q rho transcript bound, giving an efficient secret-prefix
construction conditional on PRF security. Independent uniform group masks
give a separate exact invariance statement, with an efficient PRP version
conditional on the declared PRP security. The note explicitly separates
these constructions from arbitrary small edits to random local circuits.

Boundary falsification is analytical: public/short triggers, q=0, empty and
full modified regions, a constant-output gate change, noninjective
preprocessing, and the old identity-length exceptions. No finite enumeration
or numerical result is used as proof.

## Map delta and descendants

Extend only the existing research-questions coverage family and add a dated
front-page navigation paragraph. Qualify the old navigation's absence of a
secure construction as referring to the full-description game. Preserve all
60 mathematical records, 165 pinned sources, dependencies, priorities and
other families. No source fingerprint was refreshed and no accepted
mathematical descendant was upgraded or invalidated. The old reports and
integration receipts remain unchanged. HANDOFF, manuscript, skill and
GOAL_SPEC are unchanged.

Before editing, all four routine map checks passed, with 25 unit tests and
no freshness differences. After adding the note, freshness reported exactly
that one new research file and no other delta. Structural JSON comparison
confirmed that only the research-questions family and project navigation
changed. The new note's ledger distinguishes proved elementary claims,
conditional instantiations, a refuted universal shortcut and unresolved
literal random-circuit surgery. These are author claims, not map acceptance.

## Artifact fingerprints

| Artifact | SHA-256 | Review |
| --- | --- | --- |
| `notes/planting-output-only-2026-11-17.md` | `3f6666a790a956c6d1ef89ea34e7cb9216700eebe5990ed4b877e0366cfb8b22` | Full author proof and boundary review; no independent review |
| `experiments/20261110-planted-scaling/proof.md` | `5d603c9aa696531e8bb828de02af41aee6897b9cd4b9b82b7b801e8ddae2551a` | Full read for prior scope; unchanged |
| `experiments/20261110-planted-scaling/report.md` | `c9c9849587e27647ac4d0459a25907d5431d8b2a5cd3be3b9932385d5a4bee11` | Full read; unchanged |
| `experiments/20261110-planted-subsequence/proof.md` | `5d943d762663d0b42a75d74f59a24abfac1c1a3896989581d1ebd957742fae28` | Selected sections 1-3 and model; unchanged |

## Verification commands

```sh
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-17-output-only-planting.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
git status --short
```

## Complete changed-file list

- `notes/planting-output-only-2026-11-17.md`
- `notes/project-map/integration-2026-11-17-output-only-planting.md`
- `notes/project-map/catalogue.json`
- `notes/project-map/inventory.json`
- `notes/project-map/COVERAGE.md`
- `PROJECT_MAP.md`

## Final verification

All four map checks passed: 60 records and 165 pinned sources validate,
freshness has no differences, deterministic views match, and all 25
maintenance tests pass. `git diff --check` passed. Final diff inspection
confirmed the inventory gained exactly the new note and the receipt pointer;
generated changes are confined to PROJECT_MAP and COVERAGE. These checks
verify documentary consistency, not the mathematical proofs.
