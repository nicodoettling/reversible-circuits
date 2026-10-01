# Initial Map Integration: 2026-10-01

Baseline repository commit: `3162c87e3b6d1a1c750221d6d6c659e06158dd12`.
Initial worktree was clean. Scope: repository documentary consolidation; no new
theorem, research experiment, literature campaign, tmux run or proof certification.
Only entry-point pointers and the new map/maintenance files are edited.

## Evidence and Version Binding

The canonical catalogue pins every selected whole-file SHA256, exact locator and
read scope. Some scopes are selected passages, not full readings. Record-level
`review_binding` distinguishes scope-matched historical verdicts from byte-matched
review snapshots. Source `reviewed_sha256` is retained where the actual prior
verdict supplies the digest. Current bytes were checked against those digests;
no evidence source was edited to make a digest match.

Important bindings include the September 7 frozen R1 proof, canonical S1.v2 and
G1.v1.2 synthesis, and the C1 structural report; the September 22 first sparse
proof; and the later canonical sparse extension and obstruction. The dense/short
September 5 verdicts identify their frozen report and date but do not supply a
historical report hash. Their map acceptance is a documentary scope match, with
this limitation disclosed. The full microlemma graphs remain in source artifacts.

All records are new map version 1. No inherited mathematical statement was
reproved here. Same-model nonauthor reviews are correlated. There is no new
`accepted-reviewed`, `proof-reviewed`, `experiment-reproduced`, or
`formalization-checked` promotion.

## Reconciliations and Ranking Changes

- Replaced the impression that only the 2N^3 dense schedule is known with the
  already audited September 5 length/error theorem. Negligible error is not
  asserted at fixed-constant N^2 log N based on that bound.
- Retired the old genus-one existence task. Both the recursive endpoint sampler
  and the separate marked-cut sampler were accepted in September 7 reviews.
- Retained both sparse theorems: larger length scope has a weaker explicit
  error envelope and later onset, not an across-the-board replacement.
- Separated the accepted explicit-subsequence obstruction from the stronger
  all-N blind author's claim, which remains provisional in this map.
- Recorded the archived acceptance of qualitative heat-bath irreducibility and
  elimination of the standalone mean-lift obligation. Neither closes mixing.
- Preserved the unaudited M340 claim and initialized M341/M342 branches without
  promoting them into results. Most heat-bath microbranches remain pending.
- Ranked a connected higher-genus decoder, bridge-conditioned component mass,
  and focused independent theorem review above another broad local-mixing run.

## Dependency Impact

There was no prior catalogue to migrate and no mathematical source alteration.
The new coarse prerequisite graph includes star -> dense sampling, connected
counts/genus-one -> sparse sampling, and count/decoder primitives -> the open
global assembly reduction. Classical literature imports are explicit assumptions.
It does not infer full-chain mixing from direct sampling or from rejected support
policies. Future source drift reports all mapped transitive descendants for
recheck; it does not automatically call a theorem false.

## Coverage and Retrieval

The inventory includes actual dirty/untracked research and original raw outputs.
Fourteen named families cover the discovered repository roots. Manuscript and
large heat-bath sources were selectively read; hundreds of unselected missions
and ledger branches are individually indexed as pending, not silently omitted.
The excluded map/cache/telemetry policy is explicit in catalogue.json and
UPDATE_PROTOCOL.md. No formalization branch was discovered.

`retrieval_checks.json` records questions checked against exact statement/audit
artifacts, including stronger predecessor claims and incomplete review gates.
The questions initially exposing stale impressions (dense threshold, genus one,
mean-lift) are retained with their corrections. These checks were performed by
the mapping session, without a separate reviewer.

## Verification

Python 3.12.3, standard library only; all commands run from repository root:

~~~sh
python3 -B notes/project-map/manage.py validate
python3 -B notes/project-map/manage.py check-freshness
python3 -B notes/project-map/manage.py render --check
python3 -B -m unittest discover -s notes/project-map -p 'test_*.py'
git diff --check
~~~

All pass: 37 records, 49 pinned source files, 4,023 discovered entries (3,996
research and 27 telemetry), 920 mission/ledger branches, no unclassified research
entries and no discovery drift. Nineteen tests pass, including nine documentary
retrieval subcases. No research experiment was rerun. Local generated links and
anchors resolve; deterministic views match the catalogue and discovery baseline.

Initial real-data validation caught a duplicated C1 alias, which was corrected.
Live mission retrieval exposed overbroad matches through generic family links;
search now uses branch-specific identifiers/headings/records, and a regression
test prevents unrelated family branches from matching M340. Quantitative
normal-form congestion is retained as a provisional documentary warning because
the selected M01 audit does not supply a separate scope-matched quantitative
verdict. None of these maintenance fixes changes a source theorem.

This receipt authorizes the initial discovery baseline only; it does not
authorize changing proof hashes, promote unread content, or launch a run.

## Changed Files

Navigation-only edits: `AGENTS.md`, `HANDOFF.md`, `README.md`.

New entry point: `PROJECT_MAP.md`.

New files under `notes/project-map/`:

- `catalogue.json`
- `inventory.json`
- `branch-coverage.json`
- `RESULTS.md`
- `OBSTRUCTIONS.md`
- `TARGETS.md`
- `COVERAGE.md`
- `UPDATE_PROTOCOL.md`
- `integration-2026-10-01.md`
- `retrieval_checks.json`
- `manage.py`
- `test_manage.py`

Historical research proofs, code, reports, launch prompts and manuscript sections
are unchanged. Nothing was committed, pushed, launched or resumed.
