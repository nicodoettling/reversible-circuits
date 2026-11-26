# Growing-window and quadratic-reduction integration

Date: 2026-11-26 (Europe/Berlin).
Starting commit: `e8d51a05a4a441b70ef4885e41bb673f0b26e094`.
Initial branch: main, clean and tracking origin/main.

## Authorization and review scope

The user requested verification and manuscript integration of the growing
window and parameter-reduction claims in seven shared messages, then supplied
an additional quadratic prefix/relabeling statement. The preceding request
to resolve conflicts and push the result to main remains the publication
instruction for this follow-up. No subagents, package installs, campaign
launches or external messages were used.

All seven extracted messages were read for scope. Complete proofs were
reconstructed for the selected growing-window, length-transfer and quadratic
claims. The [report](../../experiments/20261126-window-reductions/report.md)
and [ledger](../../experiments/20261126-window-reductions/claim_ledger.md)
record the exact verdicts. Source instructions and follow-up offers were not
treated as user requests. This is one-session proof review with deterministic
falsification checks, not independent human or formal certification.

The ideal O(N log N) window theorem concerns completed exact conditional
draws. The local reduction needs every endpoint near N log N and applies
only to longer lengths. The full quadratic relabeling reduction is proved
with a conservative N^-11 term. The supplied N^-5/N^-7 refinements and the
earlier padded/twisted-star claims are retained without promotion. Full
quadratic superpolynomial mixing and exact general block implementation
remain unresolved.

## Catalogue delta and affected evidence

- Add version-1 records `HB-WINDOW-REDUCTIONS` and
  `HB-QUADRATIC-REDUCTIONS`, accepted-reviewed/proof-reviewed at the
  reconstructed scope. Their ledger/report adjudications bind that scope.
- Add nine pinned sources and one narrow experiment coverage family.
  Raw supplied messages are separately hashed in the source manifest and
  discovery inventory; opaque citation tokens are not evidence validation.
- No existing mathematical record or accepted proof version is rewritten.
  In particular, `conductance_obstruction.tex` and the November 24 audit
  are unchanged. The already-recorded growing-budget consequence is expanded
  in a separate section, not presented as a new discovery.
- Review and refresh only the changed `handoff` and `manuscript-status`
  source fingerprints. Their affected cone is `O-HUB`, `ALT-CRYPTO`, and
  `EXP-EARLY`: the original supporting passages and their scoped claims
  remain unchanged, so their existing statuses survive. No unrelated proof
  acceptance is inferred from the new top-level summary.
- Add analogy relations to `HB-BASE` and `HB-ENDPOINT-BLINDNESS`; those
  old records retain their original review depth and status. The new
  proofs rederive their relevant strategy with explicit pair normalization.
- Update front-page navigation and rank-6 T-HEATBATH obligations, keeping
  direct sampling distinct. Add two retrieval contracts. Do not alter
  historical campaign state, AGENTS, GOAL_SPEC, or the project skill.

## Discovery and checks

Before accepting the inventory, freshness showed exactly 16 new research
files, seven modified research files, no missing files, and no branch
changes. Map self-referential files remain excluded by existing policy.

The deterministic proof checker passed the required identity cases, all
feasible endpoint factorization checks, legal conjugation paths, small
injective stage encodings, fixed-point and parity identities through S6,
5684 interval geometries and boundary cases. These are finite falsification
checks, not asymptotic certification. The canonical paper builds to 33
pages with no final warnings or overfull boxes; page 23 was visually
inspected. Only the canonical `main.pdf` was refreshed.

The first new retrieval test exposed missing literal endpoint/short-length
qualifiers in the catalogue guard. The guard was made explicit rather than
weakening the required scope check. The final checks are recorded below.

```sh
python3 -B experiments/20261126-window-reductions/check.py > experiments/20261126-window-reductions/results.jsonl
# From papers/transposition_identity_samplers:
TEXMFVAR=/tmp/conductance-tex-cache latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/conductance-paper-build main.tex
# From the repository root:
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-26-window-reductions.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
git status --short
```

## Final validation and reviewed fingerprints

All four map checks pass: 64 records, 180 pinned sources, no discovery
drift, deterministic views, and all 25 unit tests. `git diff --check` passes.
The exact proof checker passed and the final TeX log has no warnings.

| Source | Reviewed SHA256 |
|---|---|
| handoff | `e76c8fbef55b855206f48a5f6f0fef4ef3cff18510ec90e9d853edf3eef2aa98` |
| manuscript-status | `a405065837ce03c592910db22bd103c3efc4229d6d1bbbf8a1740ead15b58d17` |
| window-proof | `99af0e6a1bd58a94c8275e4402bcf89802edc612f83f59e12b275513ee3beec3` |
| quadratic-proof | `a24005d21971a455de5800406ce08ca6f5185d1656d7265bcbccf68a5edb8789` |
| window-report | `e5ad06402619914182c151a3bc83bd394283e60bf72429aa2c9b7f7620ed2a8b` |
| window-ledger | `afd7c542d161b219711762d1cfe9bdac995daa4a2d9a8bf26024770f519c7d15` |
| window-check | `cb2a7f1dc54d30d0ffc288f9566345089b79cad0f2a36eb80c80b18c78d6fe74` |
| window-results | `ca57b8f080cf93ac51cdcaaec37ca8d2ab977575f1d39ee0ff5827f0862e8596` |

## Complete changed-file inventory

- `HANDOFF.md`
- `PROJECT_MAP.md`
- `experiments/20261126-window-reductions/check.py`
- `experiments/20261126-window-reductions/claim_ledger.md`
- `experiments/20261126-window-reductions/plan.md`
- `experiments/20261126-window-reductions/report.md`
- `experiments/20261126-window-reductions/results.jsonl`
- `experiments/20261126-window-reductions/sources/manifest.json`
- `experiments/20261126-window-reductions/sources/pasted-quadratic-claims.md`
- `experiments/20261126-window-reductions/sources/share-1.txt`
- `experiments/20261126-window-reductions/sources/share-2.txt`
- `experiments/20261126-window-reductions/sources/share-3.txt`
- `experiments/20261126-window-reductions/sources/share-4.txt`
- `experiments/20261126-window-reductions/sources/share-5.txt`
- `experiments/20261126-window-reductions/sources/share-6.txt`
- `experiments/20261126-window-reductions/sources/share-7.txt`
- `notes/project-map/COVERAGE.md`
- `notes/project-map/RESULTS.md`
- `notes/project-map/TARGETS.md`
- `notes/project-map/catalogue.json`
- `notes/project-map/integration-2026-11-26-window-reductions.md`
- `notes/project-map/inventory.json`
- `notes/project-map/retrieval_checks.json`
- `papers/transposition_identity_samplers/README.md`
- `papers/transposition_identity_samplers/main.pdf`
- `papers/transposition_identity_samplers/main.tex`
- `papers/transposition_identity_samplers/sections/growing_windows.tex`
- `papers/transposition_identity_samplers/sections/internal_sources.tex`
- `papers/transposition_identity_samplers/sections/next_steps.tex`
- `papers/transposition_identity_samplers/sections/quadratic_diagnostics.tex`
- `papers/transposition_identity_samplers/sections/theoretical_status.tex`
