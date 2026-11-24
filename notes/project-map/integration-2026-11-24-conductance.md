# Conductance draft proof audit and manuscript integration

Date: 2026-11-24 (Europe/Berlin).
Starting commit: `7c2a54f833158bdb4fe4b4fec6f8de8c743f60a2`.

## Authorization and initial state

The user requested verification of the supplied conductance draft and, if
valid, integration into the main write-up. This authorizes the bounded proof
audit and its decisive exact checks, not a restart of the historical campaign.
No agents, commit, push, package installation or machine changes were used.

The workspace initially contained edits to PROJECT_MAP, catalogue, inventory
and COVERAGE, plus untracked `notes/planting-output-only-2026-11-17.md` and
`notes/project-map/integration-2026-11-17-output-only-planting.md`. Those
pre-existing changes are preserved. Initial map validation, freshness and
deterministic rendering passed with 60 records and 165 pinned sources.

## Proof scope, verdict and source conflicts

The full supplied PDF, all expanded proofs, the exact script and raw outputs
were inspected. The [report](../../experiments/20261124-conductance-audit/report.md)
and [ledger](../../experiments/20261124-conductance-audit/claim_ledger.md)
give the precise parameters, conventions, checks, dependencies and limitations.
The verdict is promote at the stated scope: a universal polynomial bound for
the project chain is refuted, long-length profile expansion and a coarse
all-length pair-chain bound hold, and full long-length mixing remains open.
This is substantive single-session proof review, not independent human or
formal certification. The new claims do not establish general sampling
hardness or affect accepted direct-sampler results.

The CLW Hurwitz-map correspondence was checked at Definition 1.3/equation
(10); the map-count estimate is derived here. ArXiv abstract bibliography
metadata conflict with the journal issue; the manuscript uses the IMS issue's
correct pages and DOI, as documented in the report. Ben-Itzhak--Teicher
Theorem 3.4 and the move convention were checked, but no new proof depends
on that classification. All-endpoint connectivity has a self-contained proof.

## Record versions, descendants and priorities

- Add `O-LOCAL-BOTTLENECK` and `HB-CONDUCTANCE-BOUNDS`, version 1,
  `accepted-reviewed` with `proof-reviewed` depth and explicit ledger/report
  adjudications. They do not inherit an older audit's acceptance.
- Retain `G-HEATBATH`'s original historical statement and sources, mark it
  superseded at version 2, and preserve its exact version 1 record in
  [history](history/2026-11-24-conductance/G-HEATBATH-v1.json). The new
  obstruction has a typed supersession relation to that old open question.
- Every other pre-existing mathematical record is unchanged. There are no
  logical descendants of G-HEATBATH. The changed source cone is O-HUB,
  ALT-EXPANDER, ALT-CRYPTO and EXP-EARLY; their supporting original passages
  and scoped claims survive unchanged. No unrelated record is upgraded.
- Add one narrowly scoped experiment coverage family and six pinned sources.
  Update the four reviewed source fingerprints for HANDOFF, manuscript status,
  expander discussion and bibliography. These are explicitly inspected deltas,
  not a bulk evidence refresh.
- Reconcile the historical open/conditional wording, update front-page
  navigation, and replace T-HEATBATH's universal target with long-length fiber
  conductance or larger updates. Its rank remains 6. Preserve the old campaign
  files and all unrelated archive branches as pending where they were pending.
  GOAL_SPEC, AGENTS and the skill are unchanged.
- Update the two retrieval contracts that expected the historical question
  to remain open, and add a scope check distinguishing the new obstruction
  from direct-sampling hardness and full mixing at m=N^2.

## Validation

The exact harness passed all cases, including 46,656 words in S4 at m=6,
with 3,936 identity words, plus 30 switching comparisons. These finite checks
do not prove the asymptotic result; the expanded mathematical proof does.
The manuscript built to 28 pages with no final LaTeX warnings or overfull
boxes. The theorem page was visually inspected. Temporary font generation
initially attempted the read-only home cache; the final build uses
`TEXMFVAR=/tmp/conductance-tex-cache` and an output directory under /tmp.
Only the canonical tracked `main.pdf` was refreshed; the historical compiled
compatibility PDF was left unchanged.

Before accepting the inventory, freshness showed exactly seven new research
artifacts and ten reviewed modified research files, no missing files and no
branch changes. The map's self-referential integration/history files and
generated views follow the existing inventory exclusions.

Commands (repository root unless noted):

```sh
python3 -B experiments/20261124-conductance-audit/check.py > experiments/20261124-conductance-audit/results.jsonl
# From papers/transposition_identity_samplers:
TEXMFVAR=/tmp/conductance-tex-cache latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/conductance-paper-build main.tex
# Back at repository root:
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-24-conductance.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
git status --short
```

## Complete changed-file inventory

Files changed or added in this task:

- `HANDOFF.md`
- `PROJECT_MAP.md` (extends pre-existing changes)
- `notes/project-map/catalogue.json` (extends pre-existing changes)
- `notes/project-map/inventory.json` (extends pre-existing changes)
- `notes/project-map/COVERAGE.md` (extends pre-existing changes)
- `notes/project-map/RESULTS.md`
- `notes/project-map/OBSTRUCTIONS.md`
- `notes/project-map/TARGETS.md`
- `notes/project-map/retrieval_checks.json`
- `notes/project-map/history/2026-11-24-conductance/G-HEATBATH-v1.json`
- `notes/project-map/integration-2026-11-24-conductance.md`
- `experiments/20261124-conductance-audit/source.pdf`
- `experiments/20261124-conductance-audit/plan.md`
- `experiments/20261124-conductance-audit/check.py`
- `experiments/20261124-conductance-audit/results.jsonl`
- `experiments/20261124-conductance-audit/claim_ledger.md`
- `experiments/20261124-conductance-audit/report.md`
- `papers/transposition_identity_samplers/README.md`
- `papers/transposition_identity_samplers/main.tex`
- `papers/transposition_identity_samplers/main.pdf`
- `papers/transposition_identity_samplers/sections/conductance_obstruction.tex`
- `papers/transposition_identity_samplers/sections/theoretical_status.tex`
- `papers/transposition_identity_samplers/sections/expander_gate_sets.tex`
- `papers/transposition_identity_samplers/sections/implications.tex`
- `papers/transposition_identity_samplers/sections/internal_sources.tex`
- `papers/transposition_identity_samplers/sections/next_steps.tex`
- `papers/transposition_identity_samplers/sections/references.tex`

Pre-existing untracked files preserved without edits:

- `notes/planting-output-only-2026-11-17.md`
- `notes/project-map/integration-2026-11-17-output-only-planting.md`

## Reviewed artifact hashes

The following hashes bind this integration to the exact reviewed versions.

| Artifact | SHA-256 |
| --- | --- |
| `experiments/20261124-conductance-audit/source.pdf` | `361655d05246c4b1a189a1835675d926ac8cf0d10e2d627d5ea2d5aa57d39e8f` |
| `papers/transposition_identity_samplers/sections/conductance_obstruction.tex` | `5d6ab6684ede6fb0d5011d6eee7eff3f2182268aeabeee4c89f5cba973eaffce` |
| `experiments/20261124-conductance-audit/report.md` | `e29225cae37bbaa1d6e824cd306615ebc70a20d228f6214133c34d63ccbf8c5d` |
| `experiments/20261124-conductance-audit/claim_ledger.md` | `cb7360c49c5826574a4e2b6ae182b6e35c872de3a3f1953d0ea27d081802712a` |
| `experiments/20261124-conductance-audit/check.py` | `dfa779c9c21272563cbebd22699e87e693bbb1073ecc5794d0b1edad5fc586ea` |
| `experiments/20261124-conductance-audit/results.jsonl` | `5c299e6db5549ec24a67501f8e5bf36291e6acedb165b54911b1810231cc11b7` |
| `HANDOFF.md` | `850568ad0ba85e7184f57c63d0a6c05b976c0c19eafbcdfd1424a1fe6ba5e465` |
| `papers/transposition_identity_samplers/sections/theoretical_status.tex` | `e746c3ec7da0bc343c2520d3009f610b670606c93687ba7f0b13f88d99425dc3` |
| `papers/transposition_identity_samplers/sections/expander_gate_sets.tex` | `f940f1bc487f6ef6cb82ad6854f54eb4d624810adff4066d298c958cc9bc5ca5` |
| `papers/transposition_identity_samplers/sections/references.tex` | `bca7f30c9eeadedda79f127232434e2fb8ed3673b11c769c04b91de2e8c65696` |
| `papers/transposition_identity_samplers/main.pdf` | `4d320fcb30fc5813767506df5c13b9a2aa349de03b1cd7729c308175e14d8c0b` |

## Final verification result

All 25 map maintenance tests pass, 62 records and 171 pinned sources validate,
freshness has no changes, and deterministic views match. The two pre-existing
retrieval assertions requiring G-HEATBATH to stay open were updated to the new
superseded status and its supporting theorem; the new scope contract also
passes. `git diff --check` passes. The final changed-file inventory above
includes all task files and both preserved untracked planting files.
