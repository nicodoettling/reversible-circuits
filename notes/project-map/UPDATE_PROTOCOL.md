# Research Map Maintenance

The map is navigation over existing evidence, not a theorem authority or a
research-run launcher. Start at [PROJECT_MAP.md](../../PROJECT_MAP.md).

## Canonical Files

- `catalogue.json`: versioned claims, sources, statuses, dependencies, targets,
  coverage rules and historical brief dispositions. Edit this file for content.
- `inventory.json`: reviewed filesystem discovery baseline, including untracked
  files. Its receipt acknowledges discovery, not mathematical acceptance.
- `branch-coverage.json`: generated mission/ledger index with explicit pending
  dispositions. Family membership does not certify each branch.
- `PROJECT_MAP.md`, `RESULTS.md`, `OBSTRUCTIONS.md`, `TARGETS.md`, `COVERAGE.md`:
  deterministic views. Do not manually edit their repeated claim fields.
- `integration-2026-10-01.md`: initial integration receipt and verification scope.
- `retrieval_checks.json`: documentary navigation questions and checked sources.
- `PROGRAMME.md` and `PROGRAMME_DECISIONS.md`: versioned planning cards and
  append-only outcome receipts. Planning progress is separate from theorem status.
- `campaign-identity-bridge-sampling-20261025/`: frozen mission and operator
  commands; preparation does not start inference.

Exact source statements and scoped verdicts remain authoritative. The map's
coarse logical graph omits microlemmas, which remain in linked proofs/ledgers.

## Status and Review Depth

`source_claimed_status` records the author's claim. `effective_status` records
what the traced evidence supports. `check_depth` records what this integration
actually inspected. None can substitute for the other.

- `accepted-inherited`: a prior scoped internal verdict was traced. This is not
  fresh proof review, external certification, or independent statistical evidence.
- `accepted-reviewed`: reserved for a new substantive review with named inputs.
- `conditional`: an implication is supported; its application still needs named
  premises. It is not an unconditional theorem.
- `provisional`: an author proposal or repair lacks required scoped review.
- `open`: no positive or negative resolution of the exact target is established.
- `rejected`: a specific claim or proof step failed at the stated scope.
- `superseded`: a later version replaces it; keep the old statement and reason.
- `unresolved`: incomplete reconciliation prevents a reliable verdict.

The depth labels range from `inventory-only` and `summary-only` through
`statement-traced` and `statement-and-verdict-traced` to substantive
`proof-reviewed`, `experiment-reproduced`, and `formalization-checked`.
The initial map claims none of the last three. A failed method is not a refuted
main conjecture; a positive conditional result is not a completed application.

## Routine Check

Run from the repository root with Python 3.9 or newer, standard library only:

~~~sh
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
~~~

All four checks matter. Validation pins mapped evidence and checks structure;
freshness detects new/changed/deleted discovery material. A new inventory cannot
repair a changed proof fingerprint or justify keeping an accepted descendant.

## Integrate a Delta

1. Inspect dirty/untracked files and run the checks before changing baselines.
   Write a candidate inventory outside the map, for example:

   ~~~sh
   python3 -B notes/project-map/manage.py inventory --output /tmp/reversible-map-candidate.json
   ~~~

2. Read changed exact statements, relevant proof inputs and scoped verdicts.
   For unread material, record `pending`; do not inherit acceptance from a title.
   Preserve frozen reports. An unrelated source edit still needs an explicit
   judgment before changing its whole-file fingerprint.
3. Add or version records in `catalogue.json`; preserve stable IDs and aliases.
   If a statement changes materially, retain its old source/version and add the
   new version/record with a supported typed relation. Never edit away a failed
   claim to make its old verdict appear to apply to the replacement.
4. Trace logical descendants of changed premises. Validation reports the affected
   cone, but a human/agent must decide whether each claim is pending recheck,
   invalidated, or survives by a supported replacement. Nonlogical history,
   analogy and refutation edges do not supply proof premises.
5. Reconcile stronger old claims before proposing a supposedly new target. Update
   ranks, stop conditions and historical launch-brief dispositions. New runs need
   separate user authorization; this protocol does not launch or resume them.
   After an operator starts an explicitly authorized resilient campaign, its
   coordinator may choose successive bounded investigations inside that frozen
   mission using programme admission/receipt rules. The selected recovery and
   quota authorization governs attempt continuation. This does not authorize
   a different scientific mission or an unrelated launch.
6. Write a dated integration receipt: prior commit, changed record versions,
   reviewed source hashes and verdict bindings, affected descendants, exact read
   depth, disagreements, coverage exclusions, priority changes and tests run.
7. Only after reviewing discovery, accept the new baseline explicitly. Replace
   the example receipt path with the actual new receipt:

   ~~~sh
   python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-YYYY-MM-DD.md
   python3 -B notes/project-map/manage.py render
   ~~~

8. Run all checks and realistic retrieval questions. Review the diff and report
   any remaining pending branches. Do not update source hashes merely to turn a
   failing check green. There is deliberately no bulk evidence-refresh command.

## Retrieval

~~~sh
python3 -B notes/project-map/manage.py find --query S-DENSE
python3 -B notes/project-map/manage.py find --query genus
python3 -B notes/project-map/manage.py branches --query M340
python3 -B notes/project-map/manage.py branches --query L-0336
~~~

`find` searches records and includes resolved evidence paths. To assess a proposed
target, read its nearest records and their primary statement/verdict links, not
just the search output. The recorded retrieval questions exercise this route;
they are same-session documentary checks, not an independent referee process.

## Limits and Exclusions

The inventory walks the filesystem, not just Git. Unknown new research families
fail discovery/coverage checks. New files inside known families are also flagged
by freshness. Every mission directory and every L-/CP- heading in the declared
heat-bath ledgers receives a disposition; unselected ones remain pending.

The catalogue's explicit policy excludes Git metadata, environment/build caches,
TeX intermediates and the self-referential map tree. Runtime logs/status files
are inventoried as telemetry: appending them does not invalidate research.
Research JSON/JSONL, PDFs, scripts and notes remain hashed. Do not leave the only
evidence for a new claim in a log or excluded directory. Symlinks and special
files are listed without following/reading them. Changing exclusions requires
review; excluded content is an acknowledged coverage limit.

Checks verify IDs, model fields, source bytes/locators, available historical
reviewed hashes, logical cycles, transitive prerequisite status, generated views,
branch coverage, and local links/anchors in the generated Markdown format.
They do not verify mathematical formulas, audit every proof, rerun experiments,
check external URL availability or build formalizations. A hash identifies bytes,
not truth. A baseline acceptance flag requires a receipt but cannot judge whether
its author actually performed an adequate review.

## Campaign Map Integration

The campaign catalogue sets `frontier_path` to
`notes/project-map/FRONTIER.md`. The same render/check commands then keep the
front page inside an authorized artifact directory. The primary checkout uses
the default `PROJECT_MAP.md`. This is a rendering location, not a different
mathematical catalogue. Review campaign results before merging; restore the
primary front-page setting when integrating them into main.

Discovery explicitly excludes `.campaigns/` and linked-worktree `.git` metadata.
Scientific artifacts under the declared `research-campaigns/` and campaign
experiment directories remain hashed, including new/untracked outputs. Runtime
manifests, STOP markers and quota logs must never become research evidence or
Git checkpoint artifacts. No campaign setup changes a source proof fingerprint.
