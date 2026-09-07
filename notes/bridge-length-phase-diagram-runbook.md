# Runbook: Bridge-Length Phase-Diagram Run

This runbook prepares the requested background run. It does not launch it.

## Configuration

- Repository: `/home/nico/projects/research_projects/reversible_circuits`
- Prompt: `notes/bridge-length-phase-diagram-goal-run.md`
- Experiment: `experiments/20260905-bridge-length-phase-diagram/`
- Log: `notes/bridge-length-phase-diagram-run.log`
- Tmux session: `bridge-length-phase-diagram`
- Codex executable: `/home/nico/.local/bin/codex`
- Model: `gpt-6-astra`
- Reasoning effort: `ultra`
- Permission profile: `sandbox-only`
- Sandbox: `workspace-write`
- Approval policy: `never`
- Live web search: enabled for targeted primary-source checks
- Active context ceiling: four total, comprising the coordinator and three
  concurrent workers
- Target wall time: three hours
- Final synthesis reserve: 30 minutes
- Persistence: enabled; `--ephemeral` is absent

The installed Codex 0.153.0 model catalog exposes `ultra` for GPT-6 Astra as
"Maximum reasoning with automatic task delegation." This run therefore uses
the requested Codex-native `gpt-6-astra` plus `ultra` configuration directly.

## Preflight-only command

This checks the CLI, Bubblewrap setup, prompt, repository, tmux name, and
launcher arguments without creating a tmux session:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/codex_tmux.py launch \
  --dry-run \
  --root /home/nico/projects/research_projects/reversible_circuits \
  --session bridge-length-phase-diagram \
  --prompt notes/bridge-length-phase-diagram-goal-run.md \
  --log notes/bridge-length-phase-diagram-run.log \
  --run-file experiments/20260905-bridge-length-phase-diagram/tmux-run.json \
  --status-file experiments/20260905-bridge-length-phase-diagram/tmux-status.json \
  --codex /home/nico/.local/bin/codex \
  --model gpt-6-astra \
  --reasoning-effort ultra \
  --search
```

Run the preflight from a host shell with current `codex-bwrap` group
membership. A nested Codex sandbox may be unable to perform the sandbox
probe even when the host setup is healthy.

## Launch command

Run only after the user approves:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/codex_tmux.py launch \
  --root /home/nico/projects/research_projects/reversible_circuits \
  --session bridge-length-phase-diagram \
  --prompt notes/bridge-length-phase-diagram-goal-run.md \
  --log notes/bridge-length-phase-diagram-run.log \
  --run-file experiments/20260905-bridge-length-phase-diagram/tmux-run.json \
  --status-file experiments/20260905-bridge-length-phase-diagram/tmux-status.json \
  --codex /home/nico/.local/bin/codex \
  --model gpt-6-astra \
  --reasoning-effort ultra \
  --search
```

The helper will print the exact status command. The expected command is:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/reversible_circuits/experiments/20260905-bridge-length-phase-diagram/tmux-run.json
```

Report the run as healthy only if this command returns `HEALTHY`, `STARTING`,
or a successful early `COMPLETED` state with matching process and heartbeat
evidence.

## Monitoring

```sh
tmux capture-pane -p -t bridge-length-phase-diagram:0.0 -S -100
tail -n 100 notes/bridge-length-phase-diagram-run.log
tail -F notes/bridge-length-phase-diagram-run.log
```

Durable mathematical progress is recorded in:

```sh
sed -n '1,220p' experiments/20260905-bridge-length-phase-diagram/claim_ledger.md
sed -n '1,260p' experiments/20260905-bridge-length-phase-diagram/phase_diagram.md
sed -n '1,300p' experiments/20260905-bridge-length-phase-diagram/coordinator_report.md
```

## Interruption and resume

For a graceful pause, attach to tmux and send `Ctrl-C` once. Allow the
supervisor to record final status. Preserve the tmux sidecars, log, role
checkpoints, and coordinator files.

Resume by using the exact Codex session ID recorded in `tmux-run.json` with
the runner's `resume` command. Do not use `--last` when more than one project
session is plausible.
