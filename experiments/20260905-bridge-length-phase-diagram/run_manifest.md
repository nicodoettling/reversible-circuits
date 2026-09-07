# Run Manifest

Status: complete; classification `quantified-phase-diagram`

```text
repository=/home/nico/projects/research_projects/reversible_circuits
prompt=notes/bridge-length-phase-diagram-goal-run.md
tmux_session=bridge-length-phase-diagram
log=notes/bridge-length-phase-diagram-run.log
runner_file=experiments/20260905-bridge-length-phase-diagram/tmux-run.json
runner_status_file=experiments/20260905-bridge-length-phase-diagram/tmux-status.json
codex_path=/home/nico/.local/bin/codex
prepared_codex_version=codex-cli 0.153.0
model=gpt-6-astra
reasoning_effort=ultra
permission_profile=sandbox-only
sandbox=workspace-write
approval_policy=never
web_search=enabled
target_seconds=10800
synthesis_reserve_seconds=1800
active_context_ceiling=4
worker_contexts_beside_coordinator=3
preflight_utc=2026-09-05T15:07:20Z
preflight_status=passed-no-launch
start_utc=2026-09-05T15:09:34Z
deadline_utc=2026-09-05T18:09:34Z
repository_commit_at_start=9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc
repository_status_at_start=untracked run scaffold and three notes listed below
```

Actual startup observations below supersede prepared launch arguments.

## Startup observation and source lock

- Start clock: `2026-09-05 15:09:34 UTC`; hard deadline: `18:09:34 UTC`.
- Mandatory checkpoint deadline: `16:24:34 UTC`; fresh audits start by
  `17:09:34 UTC`; final synthesis starts by `17:39:34 UTC`.
- Available collaboration capacity: coordinator plus exactly three workers.
  Workers may not spawn. Inherited model/configuration is used.
- Runner JSON records actual launch arguments `--model gpt-6-astra` and
  `model_reasoning_effort="ultra"`; platform identifies this agent as GPT-6.
  The actual launch header in the first 15 lines of the current run log
  independently confirms model `gpt-6-astra`, effort `ultra`, permissions,
  and session `01a0721d-f2ff-78e0-af0c-ed987ee15191`.
- Python: `3.12.3`; available distributions: numpy `1.26.4`, scipy `1.11.4`,
  sympy `1.12`, mpmath metadata `0.0.0`. Prefer standard-library exact arithmetic.
- Permissions: workspace-write, approval policy never, restricted network;
  no installations, elevated execution, commits, pushes, or publication.
- Ordered source lock completed: AGENTS; HANDOFF rank-recursive section;
  manuscript rank-recursive section; next_steps; rank-recursive note;
  20260901 coordinator report; project SKILL; sampling reference; experiment
  reference; GOAL_SPEC (discipline only). The present user task overrides
  the local-chain objective and skill instructions to edit durable files.
- No historical resolution ledger or old run log was read.

Pre-existing status, preserved:

```text
?? experiments/20260905-bridge-length-phase-diagram/
?? notes/bridge-length-phase-diagram-goal-run.md
?? notes/bridge-length-phase-diagram-run.log
?? notes/bridge-length-phase-diagram-runbook.md
```

The run directory initially contained prepared coordinator/role Markdown
scaffolds and runner metadata. Role and coordinator scaffolds were filled
within their declared ownership. Runner files, top-level plan, and notes are
preserved (the runner may append its log/status). No tracked edits existed.

## Method and target

Public target: uniform on length-m identity transposition words. Internal
endpoints allowed; every output has exact endpoint and length. Composition is
`(alpha beta)(x)=alpha(beta(x))`. No Markov kernel on words is analyzed.
Exact arithmetic tests are deterministic; stochastic diagnostics must name
fixed seeds. The proof-audit workflow is supplied by the user's run protocol;
no skill outside the authorized repository paths is read.

## Progress log

- Startup: source lock complete, three independent roles being dispatched.

- Worker dispatch completed shortly after source lock: `/root/r1_short_exact`,
  `/root/r2_dense_threshold`, `/root/r3_intermediate_hybrid`; each owns only
  its corresponding hyphenated role directory and may not spawn.
- Named historical dependencies inspected: M02 component count; M12
  all-genus count-ratio report; M112 rooted product and M119 independent
  audit. Local-chain passages are excluded from synthesis.
- Focused primary-source reads opened: Féray 0904.4854 (star coefficient),
  Caputo–Liggett–Richthammer 0906.1238 (Theorem 1.1), DPS DuPoSc13.pdf
  (minimal connected sampler), DYZ HurwitzRevised.pdf (Prop.1 eq.13).
  DYZ is followed because M12 identifies a positive recurrence that may
  discharge component counting; no broad literature review is underway.
- Decisive early findings (awaiting audits): R1 defect-partition DP suggests
  exact exp(O(sqrt(m))) runtime; R2 and coordinator independently identify
  an O(r) rather than r! bridge-tail conditioning factor.

- 15:22 UTC decisive heartbeat: all three directions have concrete results;
  R3 independently accepts the coordinator's sparse minimal-component
  bound. R2 derives the requested N²(log N+log(1/epsilon)) scale.
- All substantive worker checkpoints arrived within the first 20 minutes,
  well before the 75-minute limit.
- R2 report finalized and frozen before 15:35 UTC. R1 will independently
  audit its full theorem and code after freezing its own report; R2 is
  reserved for the reciprocal short-sampler audit.
- Focused fixed-positive-genus sampler search: primary Féray–Louf–Thévenin
  2105.03284 / DOI 10.1007/s00440-022-01170-9 has long-cycle endpoint,
  fixed genus, and asymptotic TV approximation, so it does not discharge
  the connected identity primitive. Failure to locate another result is
  not evidence of novelty or hardness.


## Final completion and audit record

- Outcome: `quantified-phase-diagram`; early completion is authorized because
  all three research reports, fresh nonauthor audits, the phase diagram,
  claim ledger, and final classification are complete.
- Strongest theorem: R2's length-dependent dense error bound and its
  sufficient `O(N²(log N+log(1/epsilon)))` length regime. R1's fresh audit
  accepted the full theorem at 15:46 UTC. R2's reciprocal fresh short audit
  accepted the exact sampler. Reports and audits are in their role directories.
- R3 research artifacts froze at 15:47:36 UTC. Its reused context audited
  the final cross-document synthesis from 15:49 to 15:56 UTC and accepted
  with all three observations resolved. Only final provenance was appended
  after the reviewed synthesis snapshots; its recorded hashes remain an
  accurate record of those snapshots.
- All three worker contexts are completed. Maximum simultaneous active
  contexts was four; workers spawned no descendants. A transient R2
  context-capacity interruption was handled by resuming the same context.
- Substantive checkpoints were received within 20 minutes. Fresh audits
  and synthesis began well before the two-hour and final-30-minute limits.
  Progress was emitted after decisive findings and at synthesis/completion.
- All finite checks passed, including independent coordinator reruns of
  each role's complete deterministic harness. No failed decisive test or
  unresolved substantive audit objection remains. Proofs, not finite tests,
  support the asymptotic claims.
- The dense deliverable is a constructive proof/pseudocode and exact finite
  harnesses, not a production implementation of the whole large-input sampler.
- No local-chain mixing program was resumed. No packages were installed;
  no configuration, tracked source/manuscript/skill file, or pre-existing
  note was edited. No commit, push, publication, or elevated execution occurred.

```text
finish_utc=2026-09-05T16:04:17Z
elapsed_seconds=3283
deadline_utc=2026-09-05T18:09:34Z
remaining_required_work=none
```

## Reproduction commands and retained evidence

All commands run from the repository root unless a role-directory working
path is stated. All code uses Python 3.12.3 and the standard library only.
No nonstandard dependency is required. Exact tests have no seed. Recorded
seeded smoke/validity checks use R1 seeds 7, 20260905, 4103 and R3 seeds
1729, 2718, 31415; no asymptotic conclusion relies on stochastic diagnostics.

Author/auditor commands (rerunning an author command may replace its result
JSON with the same checks and a new elapsed-time field):

```bash
python3 -B experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/short_exact.py --output experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/results.json
python3 experiments/20260905-bridge-length-phase-diagram/roles/r2-dense-threshold/check_dense_threshold.py
python3 -B experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/audit_dense_independent.py
python3 -B experiments/20260905-bridge-length-phase-diagram/roles/r2-dense-threshold/fresh_short_audit.py
```

In `roles/r3-intermediate-hybrid/`:

```bash
python3 -B component_audit.py --n-max 48 --m-max 96 --output results.json
```

Coordinator independent original-recurrence check and separate reruns:

```bash
python3 -B experiments/20260905-bridge-length-phase-diagram/coordinator_checks.py --output experiments/20260905-bridge-length-phase-diagram/coordinator_check_results.json
python3 -B experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/short_exact.py --output /tmp/bridge-phase-r1-coordinator-rerun.json
python3 -B experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py --n-max 48 --m-max 96 --output /tmp/bridge-phase-r3-coordinator-rerun.json
```

R2's coordinator rerun imported its file with `importlib.util` and invoked
`scalar_checks()`, `small_word_checks()`, `projection_checks()`, and
`dense_survival_check()` with defaults (including N=6,q=12), storing their
returned objects under `floor`, `small_words`, `projection`, `survival` in
`/tmp/bridge-phase-r2-coordinator-rerun.json`. This ran the complete harness
without invoking its `main()` writer or modifying the frozen role output.
The durable `coordinator_check_results.json` has the independent 78-cell
results and a compact passed record for all three reruns. A direct rerun of
`coordinator_checks.py` regenerates the independent section; the extra
`role_reruns` provenance was appended after the separate harness calls.
The three named `/tmp` files contain duplicate raw rerun output only;
reproduction and future research do not depend on their survival.

Retained exact cases include S3,m4; S4,m4; S4,m6, with totals
27,120,3936. Original labeled-DP counts were checked through N6,m12.
R3's table extends through N48,m96 (114 feasible certificate rows).
Audit result JSON files record their full finite ranges and exact values.

Fresh primary sources were read only for named obligations: Féray star
coefficients; CLR endpoint spectra; DPS minimal-word/root normalization;
DYZ connected counts. Focused positive-genus literature checks and their
failure to discharge the open primitive are recorded in the coordinator
report. The current-run log header alone was read to verify actual model
configuration; no enormous historical ledger or old log was searched.

## Complete changed-file inventory and final hashes

Every run-written repository file is listed below, relative to this run
folder. These include filled pre-existing scaffolds and newly created
research artifacts. The manifest is excluded from its own content hash.
The R3 research freeze hashes were independently verified unchanged at
completion. All other hashes below are completion snapshots.

| run-written file | SHA-256 |
|---|---|
| `claim_ledger.md` | `b805c04e07e8e815aee66b3955e953978e20c7ebfa9261162094bf538a7b396c` |
| `coordinator_check_results.json` | `4cc6f63db92060a4828330b8eb5363dae5c48bd1a3c49e90fd3771e85bd9788d` |
| `coordinator_checks.py` | `d3abdd4e6fbf6fd7876c850fe7745624c6d3e2063d7007b2388f561d52e8fe8f` |
| `coordinator_report.md` | `b07e93eef675718375588474e878b5a1d9054607cd3cda3edb7897d998253a93` |
| `phase_diagram.md` | `90f391c265d1c8114ece5cdeffcc7a62d47114791314b09d65f9fee4415a6ebf` |
| `roles/r1-short-exact/audit_dense_independent.py` | `4f7ca6738e756dd516992383a27f5618c3d51096d7d91f3e86146948f0f003d4` |
| `roles/r1-short-exact/checkpoint.md` | `f200b441e559bc9c418af4d728fce3eea0b8b813d77f820776e55d0deb5ecc8e` |
| `roles/r1-short-exact/fresh_dense_audit.md` | `d5e584dcb6254cf38c657f8a96a89c81a864d31bbe0310d140880bd2cdc56f7d` |
| `roles/r1-short-exact/fresh_dense_audit_results.json` | `970fc393b2a52f6b75e7b03b133eded808fb59ca9111c60847751d6ce2d56148` |
| `roles/r1-short-exact/plan.md` | `36b08f74737bfb31629c45421e8ce8a10e07ca2b9d4cd258aca4a3513a37972b` |
| `roles/r1-short-exact/report.md` | `2ef9e3bb86b8925c6fe8224ab38cdf7857b4c200af437041d886b95b4512e9d3` |
| `roles/r1-short-exact/results.json` | `1f0e690a3bd4cc4e2d4b095c0011b59712a55fbac3a28bf95e074b549c0e61e1` |
| `roles/r1-short-exact/short_exact.py` | `18266d27da511d824ade378368c98b8adcc5c75cf7e84460bb56658931c18962` |
| `roles/r2-dense-threshold/check_dense_threshold.py` | `48aa36b85440f77f0dc025f0d11a7b79273c26742651d1ac0127f44d4fd06354` |
| `roles/r2-dense-threshold/checkpoint.md` | `b2d8668d12c722bf9b0a44cd911b9c21f02f271fa4ef6dff0b0ead883bb40779` |
| `roles/r2-dense-threshold/fresh_short_audit.md` | `d3dd868bbe148680a1d6f3b2f2e661c0a3565731a891bca8fe79e75a107216f9` |
| `roles/r2-dense-threshold/fresh_short_audit.py` | `c7b9a3b6dca0b3726843a518019338712a12d67874a142c0e44bdeeee7a56db5` |
| `roles/r2-dense-threshold/fresh_short_audit_results.json` | `1868434882d3e9e4331fef9f1ad70385bcb6dbeec3dbcab989791f01bd8f6838` |
| `roles/r2-dense-threshold/plan.md` | `838027763d437ba07d5b627863e1dbe40ca84c83acc760f37fa7c33e5ea91bbd` |
| `roles/r2-dense-threshold/report.md` | `ae1205ffa8f50f61dd3e46564bb98875c4f8d635df29c7a941f80dfe9d4aa0d7` |
| `roles/r2-dense-threshold/results.json` | `9b4809ed4b281bf8e2351dce8aed9a633f2d8d1050447b29312b6216a4f39ee7` |
| `roles/r3-intermediate-hybrid/SHA256SUMS` | `9cfb730f22aad63973d3ff2b93860c8ffe61482da9478199e43ec5d8d3c2ea4a` |
| `roles/r3-intermediate-hybrid/checkpoint.md` | `fcc6548de20ac4f02e178a3862fc58539bb8a21c45f95d92ac2db92359d0ec34` |
| `roles/r3-intermediate-hybrid/component_audit.py` | `a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2` |
| `roles/r3-intermediate-hybrid/freeze_manifest.md` | `cb52768e791821d59d399f81155af8cc63cd7c22de61d0124d9accbaa80d2a1a` |
| `roles/r3-intermediate-hybrid/plan.md` | `0689a4490484efb8459680769a8968f7157060d45a8f09ecfdf8bbf62e69dc93` |
| `roles/r3-intermediate-hybrid/report.md` | `77e7e2060a8f1ec0fc6dda1e2ea73541dbd3628aa4b32967d90ce6c1272c6231` |
| `roles/r3-intermediate-hybrid/results.json` | `a61984171d02b50466711160880194a9a67240e6c643af007efb30c40503d9e5` |
| `roles/r3-intermediate-hybrid/sparse_bound_audit.md` | `426e4b4532c21131c070db0b367e528903e76970be86eeb0874729f03ec126c2` |
| `roles/r3-intermediate-hybrid/synthesis_audit.md` | `a1114637e9c673b26b684d6a2ab53ee68bf7b8e78e2486d4bc45d06e9272b47e` |
| `run_manifest.md` | `self; no recursive hash` |

Preserved pre-existing run files: `plan.md`, `tmux-run.json`, and
`tmux-status.json` (runner-owned status may change after this agent exits).
Preserved pre-existing notes: `notes/bridge-length-phase-diagram-goal-run.md`,
`notes/bridge-length-phase-diagram-runbook.md`, and
`notes/bridge-length-phase-diagram-run.log` (the runner appends the log).
No other repository file was changed by a research context.

Final `git status --short`:

```text
?? experiments/20260905-bridge-length-phase-diagram/
?? notes/bridge-length-phase-diagram-goal-run.md
?? notes/bridge-length-phase-diagram-run.log
?? notes/bridge-length-phase-diagram-runbook.md
```

`git diff --exit-code -- AGENTS.md HANDOFF.md GOAL_SPEC.md
papers/transposition_identity_samplers .codex/skills/reversible-circuit-sampler`
exited zero. There are no tracked modifications.

## Resume instructions

No required run work remains. For a future explicitly authorized research
run, start with `coordinator_report.md`, `phase_diagram.md`, and the claim
ledger. The next human-review target is R2 Lemma S plus the retained-rank
error telescope and Féray normalization. The next constructive open task
is a connected genus-one identity sampler at length 2v, or a correctly
weighted word decoder for the positive connected recurrence. Do not resume
any local-chain mixing program or old historical run from these artifacts.
Protected durable patches are proposed only in the coordinator report.
