# Run Manifest

Status: complete

```text
repository=/home/nico/projects/research_projects/reversible_circuits
prompt=notes/rank-recursive-identity-bridge-goal-run.md
tmux_session=rank-recursive-bridge-goal
log=notes/rank-recursive-identity-bridge-run.log
codex_path=/home/nico/.local/bin/codex
prepared_codex_version=codex-cli 0.151.0-alpha.7.2
model=gpt-5.6-sol
reasoning_effort=ultra
sandbox=workspace-write
approval_policy=never
target_seconds=21600
synthesis_reserve_seconds=2700
start_utc=2026-09-01T19:28:34Z
start_epoch=1788290914
deadline_utc=2026-09-02T01:28:34Z
deadline_epoch=1788312514
synthesis_start_no_later_than_utc=2026-09-02T00:43:34Z
synthesis_start_no_later_than_epoch=1788309814
end_utc=2026-09-01T20:19:53Z
end_epoch=1788293993
elapsed_seconds=3079
classification=strict-reduction
repository_commit=502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python_version=3.12.3
active_context_capacity=4
worker_capacity_beside_coordinator=3
goal_thread=01a05e71-b4de-7a63-b592-0e688e4bfde9
```

The model and reasoning effort above are the exact prepared and active launch
arguments in the runbook.  The runtime does not expose duplicate
`CODEX_MODEL` or `CODEX_REASONING_EFFORT` environment variables.

## Exact launch command

```sh
tmux new-session -d -s rank-recursive-bridge-goal \
  -c /home/nico/projects/research_projects/reversible_circuits \
  "bash -lc 'set -o pipefail; \
  /home/nico/.local/bin/codex exec \
  --model gpt-5.6-sol \
  -c model_reasoning_effort=ultra \
  --sandbox workspace-write \
  -c approval_policy=never \
  -C /home/nico/projects/research_projects/reversible_circuits \
  - < notes/rank-recursive-identity-bridge-goal-run.md \
  2>&1 | tee notes/rank-recursive-identity-bridge-run.log'"
```

## Repository status at start

The following was recorded before any run-owned edit.  Every path was already
modified or untracked and is treated as user/pre-existing state:

```text
 M HANDOFF.md
?? dev/
?? experiments/20260811-polynomial-mixing-resolution/
?? experiments/20260824-bwrap-subagent-smoke/
?? experiments/20260901-rank-recursive-identity-bridge-goal/
?? notes/
```

The target experiment directory already contained prepared `plan.md`,
`run_manifest.md`, `claim_ledger.md`, and `coordinator_report.md` skeletons.
They are being filled in place; no pre-existing file is reverted.

## Environment and dependencies

```text
numpy=1.26.4
scipy=1.11.4
sympy=1.12
mpmath=1.2.1
networkx=missing
pytest=missing
ripgrep=missing (GNU grep fallback used)
sage=missing
gap=missing
magma=/usr/local/bin/magma, executable present but startup blocked in the
  sandbox by its MAC-address socket initialization
```

No package installation, machine-configuration change, elevation, commit, or
push is authorized.

## Source lock

Completed before worker dispatch, in the order required by the goal prompt:

1. `AGENTS.md`
2. `notes/rank-recursive-identity-bridge-sampling.md`
3. `HANDOFF.md`, `Rank-Recursive Transposition Sampler Direction`
4. `.codex/skills/reversible-circuit-sampler/SKILL.md`
5. `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
6. `.codex/skills/reversible-circuit-sampler/references/experiments.md`
7. the target/calibration/coordination portions of `GOAL_SPEC.md`
8. only the named prior-report sections M12/6, M19/2.1 and 2.4,
   M97/9, and M15's exact-sampling literature audit

The historical local-mixing run log was not read and that proof search is not
being resumed.

## Scheduling

All six required roles are retained.  With four active contexts, the
coordinator will dispatch three workers in wave 1 and the remaining three in
wave 2, reusing completed contexts.  A later fresh audit wave will be assigned
to a worker that did not author the strongest proposed result.

| Wave | Agent context | Role directory | Dispatch UTC | Status |
|---|---|---|---|---|
| 1 | `/root/r0_coverage` | `roles/r0-coverage` | 2026-09-01T19:33Z | final report complete |
| 1 | `/root/r1_bijection` | `roles/r1-bijection` | 2026-09-01T19:33Z | final report complete |
| 1 | `/root/r3_star` | `roles/r3-star` | 2026-09-01T19:33Z | final report complete |
| 2 | `/root/r1_bijection` reused | `roles/r2-branch` | 2026-09-01T19:46Z | final report complete |
| 2 | `/root/r0_coverage` reused | `roles/r4-r5-closure` | 2026-09-01T19:48Z | final report complete |
| 2 | `/root/r3_star` reused | `roles/r6-redteam` | 2026-09-01T19:50Z | final report complete |
| audit | `/root/r1_bijection` reused | fresh nonauthor R3 source/formula/implementation audit | 2026-09-01T20:00Z | accepted |
| audit | `/root/r3_star` reused | fresh R4/R5 cutoff/conditioning/telescope audit | 2026-09-01T20:04Z | accepted |
| audit | `/root/r1_bijection` reused | final outcome-classification calibration | 2026-09-01T20:14Z | recommended conservative literal reading adopted |

Coordinator fresh checks completed:

```text
R1: python3 roles/r1-bijection/check_disintegration.py
      --min-n 2 --max-n 3 --max-length 4 --output-dir /tmp/...
R0: python3 roles/r0-coverage/exact_coverage_check.py
R3: python3 roles/r3-star/run_checks.py
      --max-n 4 --max-k 5 --seed 20260901 --draws 200 --output /tmp/....json
R3 independent: python3 roles/r2-branch/audit_r3_independent.py
      --output /tmp/r3-coordinator-final-audit.json
R2: python3 roles/r2-branch/branch_audit.py
      --output /tmp/r2-coordinator-audit.json
      --max-small-n 4 --max-small-length 6 --dense-n 4 5
R4/R5: python3 roles/r4-r5-closure/check_flat_projection.py
R6: python3 roles/r6-redteam/exact_redteam.py
      --output-dir /tmp/r6-coordinator-audit.YumNHy
```

The abbreviated paths above are relative to the experiment directory.

All commands exited zero. The final artifact/schema audit found all six
required role triplets, exactly one permitted coordinator classification,
and 43 files in the experiment directory (including the pre-existing
top-level `plan.md`). Bulk rerun output remained under `/tmp`.

## Completion

All R0--R6 reports, both mandated fresh audits, the final claim ledger, and
the coordinator report were completed before the synthesis reserve and the
six-hour deadline. The run stopped because every bounded obligation and
audit was complete, not because an individual route failed. No package was
installed, no privileged or network shell was requested, and no commit or
push was performed.
