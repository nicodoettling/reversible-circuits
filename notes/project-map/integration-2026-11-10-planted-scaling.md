# Growing planted-identity follow-up integration

Date: 2026-11-10, Europe/Berlin.
Starting commit: `c4331bada5575f58ad463e62479ff20015305759`.

The user requested growing polylogarithmic and N-gate plants in an N^2-gate
host, and explicitly confirmed considering a polylogarithmic plant in an
N-gate host as well. The prior planted-subsequence experiment and integration
were already uncommitted and are preserved. This is a bounded foreground
follow-up, not a campaign launch, commit or push.

## Scope and verdict binding

All six new artifacts were read, the exact checker was executed, and the
primary Diaconis--Shahshahani Fourier estimate was checked for its precise
walk, L2 strength and translation to the parity-periodic pure-transposition
walk. An author-hosted survey supplied a matching explicit theorem statement.
The source passages and URLs are in the experiment's source-audit.md.

The author proof derives low-order inverse-polynomial distinguishing gaps
for both requested quadratic-host schedules under negligible-in-N security.
Finite certificates separately check the formulas without an unspecified
mixing constant. The linear-host version remains unresolved; an unavailable
smoothing bound is not evidence of hardness. Security indexed by log N is a
different guarantee and is not refuted by these gaps. No result is asserted
for other gate libraries or planting mechanisms. All work is same-agent;
there is no independent proof review.

The proof labels elementary inputs, the checked external dependency,
boundary cases and the first unresolved linear-host obligation. The report
contains a claim ledger, exact numerical bounds, candidate assumption,
representation caveats and the remaining host-generation obligation.

## Map and workflow delta

Extend only the research-questions coverage family and its front-page
navigation paragraph. Preserve all 60 mathematical records, 165 pinned
sources, logical dependencies, priorities, other routes and pending branches.
There are no changed source versions or refreshed evidence fingerprints,
and no accepted mathematical descendant is upgraded or invalidated.
The earlier proof, raw data and integration receipt remain unchanged.
No manuscript or HANDOFF update is made at this review depth.

The project skill's experiment reference adds a short reusable instruction
to test random-pair equality/label overlap, retain multiplicative accuracy
under conditioning, and name the security parameter. This is procedural
knowledge; the mathematical argument stays in the experiment directory.

Before accepting the new inventory, validation passed and freshness reported
exactly the six new experiment files and the known skill-reference edit.
No other research delta or missing branch was found. Existing historical
irreducibility disagreements are unaffected; no such theorem is used.

## Reproduction and verification

```sh
python3 -B experiments/20261110-planted-scaling/check.py
python3 -B /home/hadi98/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/reversible-circuit-sampler
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-10-planted-scaling.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
```

The deterministic Python 3.12.3 checker uses only the standard library.
Its 42 scheduled rows contain 21 positive quadratic-host certificates
(19 distinct triples), 8 feasible but inconclusive linear-host rows,
9 trivial rows and 4 infeasible rows. Independent cycle-type return counts
agree for N2..8 through length 2N, including 27/120/3936 in mandatory cases.
All r1..500 radial row checks and eleven earlier literal-word-law comparisons
pass. Finite logarithmic schedules round ceil(log2 N) before raising its
power, as explicitly recorded in plan.md and report.md. Raw results retain
exact rational values, actual parameters and executed script/input hashes.

## Reviewed artifact fingerprints

| Artifact | SHA-256 |
| --- | --- |
| `check.py` | `851e0ac8dfcaf9821d45eedf6f09be110c4abc652444faf41986b29b03e4f9b6` |
| `plan.md` | `be61cf8b39f316217cc004118745ac65c1f215b60bed7d45881578c03b058bc8` |
| `proof.md` | `5d603c9aa696531e8bb828de02af41aee6897b9cd4b9b82b7b801e8ddae2551a` |
| `report.md` | `c9c9849587e27647ac4d0459a25907d5431d8b2a5cd3be3b9932385d5a4bee11` |
| `results.json` | `1bbfce82e10ee74574eed9c03db4d2f1d12157a24268d424d77c29074351bb40` |
| `source-audit.md` | `04a2991414baf6211dffef943123b965ec337fddd98cb99877c5fdb694696e3e` |

## Complete workspace changed-file list

Includes the prior uncommitted experiment and integration, preserved above.

- `.codex/skills/reversible-circuit-sampler/references/experiments.md`
- `PROJECT_MAP.md`
- `experiments/20261110-planted-scaling/check.py`
- `experiments/20261110-planted-scaling/plan.md`
- `experiments/20261110-planted-scaling/proof.md`
- `experiments/20261110-planted-scaling/report.md`
- `experiments/20261110-planted-scaling/results.json`
- `experiments/20261110-planted-scaling/source-audit.md`
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
- `notes/project-map/COVERAGE.md`
- `notes/project-map/catalogue.json`
- `notes/project-map/integration-2026-11-10-planted-scaling.md`
- `notes/project-map/integration-2026-11-10-planted-subsequence.md`
- `notes/project-map/inventory.json`

## Final verification

All four map checks pass: 60 records and 165 pinned sources validate,
freshness is clean, generated views match and all 25 maintenance tests pass.
The skill validator and `git diff --check` pass. Structural comparison with
HEAD confirms every mathematical record, pinned source and unrelated route
is unchanged. Executed script/input hashes match; every earlier experiment
artifact still matches its previous integration fingerprint.
