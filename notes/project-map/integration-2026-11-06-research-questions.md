# Research-Question Formulation Receipt

Date: 2026-11-06, Europe/Berlin.
Starting commit: `0f9f132746b4655f0506187eddc016a35f8689b0`.
Branch: `research/20261106-research-questions`.

## Scope

The user requested a branch and clearer written formulations of four ideas for
future agents, with additional questions where useful. They clarified that the
Toffoli two-component intuition refers to permutation parity. The resulting
[note](../research-questions-2026-11-06.md) preserves that motivation while
distinguishing endpoint parity from connectivity of identity-word descriptions.

This is editorial formulation and navigation work. No experiment, research
campaign, proof audit, or new theorem acceptance is part of this delivery.
The note's explicit elementary formulation checks prevent ambiguity; they do
not promote any of its proposed connectivity or hardness claims. The initial
delivery was uncommitted. The user subsequently requested the connectivity
clarification below and authorized committing and merging this branch into
local `main`.

## Connectivity clarification before merge

The user permits arbitrarily many local moves and prioritizes small working
memory. Q2 and Q3 now state qualitative reachability by finite paths with no
required step-count bound. They distinguish the stored current circuit from
auxiliary workspace, bound the local gate/wire patch, and require explicit
accounting for expansion, recompilation, padding and ancillas. A path need not
be short; an implementation must not silently store its entire history or a
global permutation table. Efficient sampling and rapid mixing remain optional
stronger questions, with their additional premises stated separately.

This clarification changes only the formulation note and its discovery hash;
it does not change the existing mathematical claims or research priorities.

The cited Jain-Jin FOCS 2022 conference paper was consulted at its primary
conference PDF, especially Section II-A, printed pages 1029–1030, to identify
Delta-equivalence and the padding/local-replacement distinction. The abstract
and bibliographic identity were checked against ePrint 2022/1430. No full-paper
audit or transfer to reversible Toffoli circuits was performed. The stable
conference version, rather than an unspecified revision of the ePrint, is the
scope of that terminology check. Source links are in the note.

## Navigation and evidence

- Add one coverage family for the new formulation note and a link in the map's
  opening navigation; update the documentary date.
- Preserve all 53 mathematical records, 140 pinned sources, review bindings,
  dependencies, priorities, and historical campaign dispositions unchanged.
- No claim descendants require re-evaluation: no mathematical premise changes.
- The complete note was read for definitions, scope, links, and incorporation
  of the user's clarification. This is not acceptance of its proposed assumptions.

Before edits, validation and generated-view checks passed. The existing
freshness discrepancy was a missing ignored machine-local file,
`.claude/settings.local.json`, already observed during onboarding. Accept its
absence in this discovery baseline; no settings file was read, changed, or
deleted by this work. The only new research artifact is the question note.
The inventory hash records its exact bytes, not proof certification.

## Verification

Regenerate the discovery baseline with this receipt and regenerate the views:

```sh
python3 -B notes/project-map/manage.py inventory --output notes/project-map/inventory.json --accept-reviewed --review-receipt notes/project-map/integration-2026-11-06-research-questions.md
python3 -B notes/project-map/manage.py render
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
git status --short
```

Affected files: the new question note, this receipt, catalogue and
inventory JSON, and generated `PROJECT_MAP.md` and `COVERAGE.md`. Checks cover
documentary consistency; no mathematical experiment is required for this edit.

Final verification passed: 53 records and 140 pinned sources validate;
freshness has no new, missing, or changed entries; generated views match;
all 23 maintenance tests pass; and `git diff --check` passes. A separate
structural comparison against the starting catalogue confirms that existing
claims, source records, dependencies, priorities, and route summaries are
unchanged. Local links in the question note also resolve.

## Push integration, 2026-11-10

To fulfill the user's push request, replay commit `cdc25b6` onto remote main
`b8dd0f2`, which includes the separately recorded
[campaign consolidation](integration-2026-11-06-campaigns.md). Preserve that
consolidation's catalogue records and pinned sources and the research-question
note's exact original bytes. Resolve the inventory receipt in favor of this
combined receipt and regenerate coverage counts from the merged inventory.
Relative to remote main, inventory changes are only the question note and the
previously documented absence of `.claude/settings.local.json`.

All four map checks pass after reconciliation: 60 records and 165 pinned
sources validate, discovery is fresh, generated views match, and all 25
maintenance tests pass. `git diff --check` also passes. These are documentary
consistency checks; no research claim or proof status is changed by the rebase.
