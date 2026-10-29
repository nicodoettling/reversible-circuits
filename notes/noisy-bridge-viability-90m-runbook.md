# Noisy Bridge Viability Run

Authorized and launched 2026-10-29. Fresh gpt-6-astra/ultra session, four total
agents, default tier, workspace-write/auto-review. One90-minute capped attempt;
no automatic restart, quota refill resume or separate campaign manager.

Mission: [noisy-bridge-viability-90m-run.md](noisy-bridge-viability-90m-run.md).
Investigate full noisy-word indistinguishability against the same sparse noise
applied to globally uniform identity bridges. Seek a meaningful attack theorem
or an explicit candidate with scoped diagnostics, not an assumed hardness
theorem. The separate continuous-prc project is read-only.

## Completed Outcome

The attempt completed cleanly at09:08:31 CET (08:08:31 UTC), after61minutes
24seconds, before either runtime or quota stop. All three workers finished;
the last quota reading at completion was14% remaining, versus16% initially.
No research remains active and no automatic continuation is authorized.

Both specified constructions were rejected by internally reviewed one-query
attacks. Six-gate relator constructions retain a detectable surplus of short
identity windows after the stated bounded scrambling and sparse noise. The
path/star construction retains detectably small support even after arbitrary
Hurwitz scrambling. These are scoped obstructions, not a general impossibility
or hardness theorem. Same-model reviews are correlated; human review remains
appropriate.

The durable [full report](../experiments/20261029-noisy-bridge-viability/report.md)
links exact statements, full proofs, rejected versions, raw diagnostics and
reviews. Research checkpoint35ad3c24e6bb424c4eb0ef119b1d505b16b33336 preserves
the complete delivery. Its completion request remains an operator-review gate,
not self-certification or authorization to restart.

Publication preparation verified92 manifest hashes, parsed26 JSON and8 Python
artifacts, and reran the independent decisive checker with a60-second timeout
and1GiB address-space cap. Exact counts and denominator regression results
matched the frozen output. Integration used a clean worktree based on the
latest remote main, retaining its five additional commits and leaving the
primary worktree's unrelated map edits untouched.

## Limits and Verified Launch

- Activation:2026-10-29 08:07:06 CET (07:07:06 UTC).
- Time-based delivery begins09:27:06 CET; total deadline09:37:06 CET.
- Quota wrap-up<=8%, external stop<=6%; earlier than the time cap if reached.
- Metadata polling15seconds; maximum allowed reading age30seconds. A stale
  meter cannot authorize continuing. Initial verified remaining allowance16%.
- The6% stop is a best-effort buffer above the requested5% reserve, not an
  exact billing guarantee. Other sessions and accepted requests can overshoot.
- Aggregate128GiB memory maximum,96GiB pressure threshold, swap0. Bounded
  experiment ceiling16GiB address space; no separate per-native-agent RSS cap.
- Verified service RuntimeMax5335s, stop grace60s, scheduling reserve5s,
  KillModecontrol-group, SendSIGKILLyes, Restartno, active populated cgroup.
- Host and service sandbox no-op passed; codex-bwrap groups/metadata passed.
- Coordinator runtime verifies Astra/ultra, collaborationultra, workspace-write
  and auto_review. Explicit default tier is configured; this is not separate
  server-returned billing/tier attestation.
- Actual tool-sandbox bounded smoke passed with exit0 and the current sealed
  run file:1GiB address space,15-second timeout, inert Python output.
- All three workers actually started by08:10:59 CET, not merely configured:
  r1_theory `01a1867e-aa3a-7aa1-aab3-c7c36c891510`, r2_construction
  `01a1867e-e975-7110-a87c-a40f90266be1`, r3_adversarial
  `01a1867f-67eb-7330-b006-8a7499b7df83`. Native child settings verify
  gpt-6-astra/ultra/default and the same scoped sandbox/auto-review profile.
- Startup artifacts include plan.md, model-v1.md and a provisional report;
  they are research state, not completed findings. A fresh post-spawn status
  reports RUNNING/HEALTHY with16% remaining and no failures.

## Identity and Artifacts

Operational root: `.campaigns/noisy-bridge-20261029/`.

Isolated worktree:
`.campaigns/noisy-bridge-20261029/worktree/`.

Branch: `campaign/noisy-bridge-20261029`.
Source HEAD:`1650532de223436eb09abb363e3a09efd6a44aba`.
Preparation checkpoint:`61cba521d833996a3232a5c2516bb6c213e6b6ce`.
Session:`01a1867b-dd58-7152-8af7-fec525bb1371`.
Tmux:`rh-76f2fe0c79787509604ad3ed31c5c0e5`.
Harness release:`/home/nico/projects/harnesses/codex-research-harness-releases/v0.4.4`.

Research outputs relative to the isolated worktree:

- `experiments/20261029-noisy-bridge-viability/`
- `research-campaigns/noisy-bridge-20261029/`

The inputs/ directory contains frozen copies of the current project map,
foreground projection/replacement derivations and checker, plus the continuous
project's overview and M4 model. Its README records provenance and SHA256.
No protected primary documents were integrated or rewritten. Local coordinator
checkpoints are scoped to these two roots; no push is authorized.

## Monitor and Stop

```bash
codex-campaign status --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/noisy-bridge-20261029/campaign.json
```

```bash
tail -F /home/nico/projects/research_projects/reversible_circuits/.campaigns/noisy-bridge-20261029/attempts/000001/attempt.log
```

```bash
tmux attach -t rh-76f2fe0c79787509604ad3ed31c5c0e5
```

```bash
codex-campaign stop --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/noisy-bridge-20261029/campaign.json
```

Do not confuse a live supervisor with active model work. Verify actual worker
starts and artifacts separately; configured slots alone prove no concurrency.
NEEDS_ATTENTION/completion_requested_review_required after clean completion
means operator review is pending, not a failed proof or a crash.
No restart, acknowledgement or quota resume is authorized by this runbook.

## Primary Worktree Inventory

This preparation adds only the mission and this runbook in the primary
worktree. The campaign operational directory is ignored. Existing modified
files were preserved:

```text
PROJECT_MAP.md
notes/project-map/COVERAGE.md
notes/project-map/TARGETS.md
notes/project-map/UPDATE_PROTOCOL.md
notes/project-map/catalogue.json
notes/project-map/inventory.json
notes/project-map/manage.py
notes/project-map/test_manage.py
```

Existing untracked artifacts were preserved:

```text
experiments/20261028-bridge-projections/
notes/genus-scaling-4h-run.md
notes/genus-scaling-4h-runbook.md
notes/project-map/PROGRAMME.md
notes/project-map/PROGRAMME_DECISIONS.md
notes/project-map/campaign-identity-bridge-sampling-20261025/
notes/project-map/integration-2026-10-25.md
```
