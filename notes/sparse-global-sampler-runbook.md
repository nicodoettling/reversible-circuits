# Sparse Global Sampler: Four-Hour Run

Authorized 2026-09-22. Research target: a global negligible-error sampler
for every even m with m^5<=N^3, using small-support exact sampling and the
existing genus-zero/one primitives. This is a proposed theorem, not an
assumed result. A proved smaller regime or checked candidate obstruction is
useful partial progress, with the original target's status retained.

## Configuration

- Model/effort: gpt-6-astra / ultra, coordinator and workers.
- Six total contexts: coordinator plus five workers. The v2 runner requests
  agents.enabled=true and agents.max_concurrent_threads_per_session=5.
  Actual worker capacity must be verified; no machine config is changed.
- Whole-run cap: 4h, final 30m for synthesis, no automatic continuation.
- Workspace-write, approval_policy=never, focused live web search enabled.
- No installs, commits, pushes or edits to old research/manuscript/skills.
- Root: /home/nico/projects/research_projects/reversible_circuits.
- Tmux: sparse-global-sampler-20260922.
- Prompt: notes/sparse-global-sampler-goal-run.md.
- Blind input: notes/sparse-global-sampler-blind-brief.md.
- Output: experiments/20260922-sparse-global-sampler/.
- Baseline commit: 20e86f665f69053031fe7eec0c3388458affb1fc.

Pre-existing untracked work: experiments/20260907-genus-one-sampler/ and
the genus-one-sampler blind brief, goal prompt, runbook, transcript and cap
status under notes/. Those files are not changes attributable to this run.

## Launch

Do not repeat while the run is active. Add --dry-run for preflight only.
Use the host context for sandbox, inherited-group and user-systemd checks.

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py launch \
  --root /home/nico/projects/research_projects/reversible_circuits \
  --session sparse-global-sampler-20260922 \
  --prompt notes/sparse-global-sampler-goal-run.md \
  --log notes/sparse-global-sampler-run.log \
  --run-file experiments/20260922-sparse-global-sampler/tmux-run.json \
  --status-file experiments/20260922-sparse-global-sampler/tmux-status.json \
  --codex /home/nico/.local/bin/codex \
  --permission-profile sandbox-only \
  --model gpt-6-astra --reasoning-effort ultra --agents 6 --search \
  --max-runtime 4h --wrapup-before 30m
```

## Monitor

Verified launch on 2026-09-22:

- Started at 05:43:44 UTC; wrap-up at 09:13:44 UTC.
- Graceful shutdown at 09:42:39 UTC; hard envelope deadline 09:43:44 UTC.
- Coordinator session ID: 01a0c7a4-3ed2-7372-914a-19f0ed2228c6.
- Service: codex-cap-sparse-global-sampler-20260922-4c2bfb1288c4.service.
- Observed startup: gpt-6-astra / ultra, workspace-write, approval never.
- Capped status HEALTHY, fresh heartbeat, active service, live contained
  coordinator. Systemd independently confirmed RuntimeMaxSec=14335,
  TimeoutStopSec=60, KillMode=control-group, SendSIGKILL=yes, Restart=no.
- CLI: codex-cli 0.154.0-alpha.6.2; Bubblewrap host preflight passed.
- Requested team ceiling: six total, configured as five spawned threads.
- Actual startup verified: all five SubAgentActivity started events are
  present, with no intervening completion; all five worker session records
  confirm gpt-6-astra / ultra. This verifies six simultaneous contexts,
  independently of the helper's conservative unverified-capacity label.
- Worker sessions, all created with fork_turns=none:
  r1_combinatorial = 01a0c7a6-6ede-7ce1-91fa-5b3d6baf2b84;
  r2_analytic = 01a0c7a6-ba09-73a3-8cc8-dd01cee41e59;
  r3_sampler = 01a0c7a6-e72f-7b43-b9c3-df3b631b285b;
  r4_diagnostics = 01a0c7a7-1232-7fb0-b671-013d4c6d15dc;
  r5_referee = 01a0c7a4-ff39-7eb3-b235-8d916fe32845.
- Native goal creation was issued at startup; the coordinator records an
  active goal in its initial checkpoint. No budget was assigned.
- Post-dispatch capped status: HEALTHY, service active/running, live
  containment, heartbeat 0.3 seconds old. No permission, Bubblewrap or
  thread-capacity error appeared in the launch transcript at verification.

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/reversible_circuits/experiments/20260922-sparse-global-sampler/tmux-run.json
```

```sh
tmux attach -t sparse-global-sampler-20260922
```

```sh
tail -F /home/nico/projects/research_projects/reversible_circuits/notes/sparse-global-sampler-run.log
```

Cap state and exact UTC deadlines:
notes/sparse-global-sampler-run.log.sparse-global-sampler-20260922.cap-status.json.
The cap verdict, live service/cgroup and fresh heartbeat determine health;
tmux existence alone does not. Verify actual model/effort and five worker
starts separately from the requested concurrency configuration.

## Resume and Files

Only the uniquely recorded service owns this run's cap. Never kill the
shared tmux server or unrelated services. No expired run may restart itself.
A later resume needs explicit user authorization, a fresh duration, the exact
Codex session ID, and a new tmux/log identity after the old service is stopped.
Native goal completion/unfinished state is separate from process exit.

Setup adds the three sparse-global-sampler Markdown files in notes/. The
launcher adds its transcript, cap status, and the experiment's tmux-run.json
and tmux-status.json. Workers add research outputs only in the new experiment;
its final changed_files.txt must inventory those separately from old work.

## Prelaunch Checks

The updated v2 capped runner passed 18 unit tests; seven optional host
integration tests were not rerun. Host launch checks and actual service
containment must still pass. Initial inspection found no active tmux session
or active capped research service; unrelated failed services are left alone.
