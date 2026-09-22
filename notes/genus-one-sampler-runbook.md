# Four-Hour Genus-One Sampler Run

Authorized on 2026-09-07. Model: gpt-6-astra, effort ultra. Four active
contexts total: coordinator, recursive constructor, structural constructor,
and blind referee/tester. External whole-run cap: four hours; final 30
minutes reserved for synthesis. Sandbox-only, no interactive approvals,
no commits, no pushes. All prior runs are read-only inputs.

Initial repository commit: 20e86f665f69053031fe7eec0c3388458affb1fc.
Worktree was clean before these three instruction/runbook files were added.
The runner records the exact prelaunch worktree and helper hashes separately.

Prompt: notes/genus-one-sampler-goal-run.md
Blind brief: notes/genus-one-sampler-blind-brief.md
Research output: experiments/20260907-genus-one-sampler/
Tmux session: genus-one-sampler-20260907

## Verified Launch

- Started: 2026-09-07 21:07:10 UTC.
- Synthesis begins: 2026-09-08 00:37:10 UTC.
- Graceful shutdown: 2026-09-08 01:06:05 UTC.
- Hard envelope deadline: 2026-09-08 01:07:10 UTC.
- Codex session: 01a07db2-4703-7312-ae54-75fcdc0bdc13.
- Service: codex-cap-genus-one-sampler-20260907-8213274cf7fa.service.
- Startup and subsequent capped status: HEALTHY, fresh heartbeat, live
  contained coordinator, observed gpt-6-astra / ultra / workspace-write /
  approval never. Systemd confirmed RuntimeMaxSec=14335, TimeoutStopSec=60,
  KillMode=control-group, SendSIGKILL=yes, Restart=no.
- Runner checks: 12 unit tests passed; seven host integration tests were
  not rerun. Host Bubblewrap, inherited-group and systemd launch checks passed.
- All three worker session records confirm gpt-6-astra / ultra. Spawn
  requests used fresh contexts (fork_turns=none):
  r1_recursive = 01a07db3-9d81-7002-8e4f-6dd206bc10e5;
  r2_structural = 01a07db4-30f1-76f2-80b2-1ccfcb49cfac;
  r3_referee = 01a07db4-9141-7e91-96e1-549fcaa8a7be.

## Launch

Do not repeat while this run is active. Add --dry-run for preflight only.

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/capped_codex_tmux.py launch \
  --root /home/nico/projects/research_projects/reversible_circuits \
  --session genus-one-sampler-20260907 \
  --prompt notes/genus-one-sampler-goal-run.md \
  --log notes/genus-one-sampler-run.log \
  --run-file experiments/20260907-genus-one-sampler/tmux-run.json \
  --status-file experiments/20260907-genus-one-sampler/tmux-status.json \
  --codex /home/nico/.local/bin/codex \
  --permission-profile sandbox-only \
  --model gpt-6-astra --reasoning-effort ultra --search \
  --max-runtime 4h --wrapup-before 30m
```

Run the launcher from the host context so its Bubblewrap, inherited-group,
and user-systemd preflights are meaningful. If any preflight fails, do not
weaken the sandbox or launch an uncapped substitute.

## Monitor

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/capped_codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/reversible_circuits/experiments/20260907-genus-one-sampler/tmux-run.json
```

```sh
tmux attach -t genus-one-sampler-20260907
```

```sh
tail -F /home/nico/projects/research_projects/reversible_circuits/notes/genus-one-sampler-run.log
```

The precise service and UTC deadlines are recorded in
notes/genus-one-sampler-run.log.genus-one-sampler-20260907.cap-status.json.
Check the cap service, process containment, fresh heartbeat and startup
model/effort; tmux existence alone is insufficient. The cap verdict overrides
stale worker status. The cap is local elapsed time, not a hard token budget.

## Completion and Resume

Research reports and periodic checkpoints are in the experiment directory.
A capped stop may leave a native goal unfinished; it does not automatically
pause or complete that goal. No automatic restart is authorized. A resume
needs a fresh user-authorized duration, the exact stored Codex session ID,
and a new tmux/log identity, after verifying the previous service is stopped.
Never stop the shared tmux server or unrelated services to manage this run.
