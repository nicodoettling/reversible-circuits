# Runbook: Rank-Recursive Identity-Bridge Goal

This runbook prepares the bounded goal run. It does not launch it.

## Configuration

- Repository: `/home/nico/projects/research_projects/reversible_circuits`
- Prompt: `notes/rank-recursive-identity-bridge-goal-run.md`
- Experiment: `experiments/20260901-rank-recursive-identity-bridge-goal/`
- Log: `notes/rank-recursive-identity-bridge-run.log`
- Tmux session: `rank-recursive-bridge-goal`
- Codex executable: `/home/nico/.local/bin/codex`
- Prepared against Codex: `codex-cli 0.151.0-alpha.7.2`
- Model: `gpt-5.6-sol`
- Reasoning effort: `ultra`
- Sandbox: `workspace-write`
- Approval policy: `never`
- Requested roles: six workers plus coordinator, scheduled in waves if needed
- Target wall time: six hours
- Final synthesis reserve: 45 minutes
- Persistence: enabled; `--ephemeral` is absent

This uses the existing group-gated Bubblewrap/AppArmor configuration.  It does
not use Bubblewrap directly, dangerous full access, or interactive approvals.

## Preflight

Run from a fresh SSH login or tmux server in which the new supplementary group
membership is visible:

```sh
cd /home/nico/projects/research_projects/reversible_circuits
id -nG
command -v bwrap
bwrap --version
codex sandbox /bin/true
echo $?
command -v codex
codex --version
tmux has-session -t rank-recursive-bridge-goal
git status --short --branch
head -n 3 notes/rank-recursive-identity-bridge-goal-run.md
```

Require:

- `id -nG` contains `codex-bwrap`;
- `codex sandbox /bin/true` returns `0`;
- the tmux session does not already exist;
- the prompt starts with `/goal`.

If the group is absent, reconnect through a fresh SSH login and start a fresh
tmux server.  Do not weaken the sandbox to compensate.

## Launch

Run this from any shell. It creates a detached tmux session and returns
immediately:

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

Do not add `--ephemeral`, `--dangerously-bypass-approvals-and-sandbox`, or
`danger-full-access`.

## Monitor

```sh
tmux has-session -t rank-recursive-bridge-goal
tmux list-panes -t rank-recursive-bridge-goal \
  -F '#{pane_pid} #{pane_dead} #{pane_current_command}'
tmux capture-pane -pt rank-recursive-bridge-goal -S -200
tail -n 120 notes/rank-recursive-identity-bridge-run.log
tail -F notes/rank-recursive-identity-bridge-run.log
```

Attach with:

```sh
tmux attach-session -t rank-recursive-bridge-goal
```

Detach without stopping the run with `Ctrl-b`, then `d`.

Durable progress is in:

```sh
sed -n '1,220p' experiments/20260901-rank-recursive-identity-bridge-goal/claim_ledger.md
sed -n '1,260p' experiments/20260901-rank-recursive-identity-bridge-goal/coordinator_report.md
```

A quiet pane is not evidence of termination. Check the tmux session, pane
state, log tail, ledger, and coordinator report together.

## Interruption and resume

For a graceful interruption, attach and send `Ctrl-C` once. Preserve the log
and experiment directory. Do not delete the tmux session while Codex is still
checkpointing.

After the original session has ended, the latest persisted Codex session for
this repository can normally be resumed with:

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
  resume --last \
  \"Resume the bounded rank-recursive identity-bridge goal. Read the run manifest, claim ledger, every completed role report, and the coordinator report. Reconcile interrupted roles and continue from the exact first open obligation without restarting completed work.\" \
  2>&1 | tee -a notes/rank-recursive-identity-bridge-run.log'"
```

If several persisted sessions exist for this repository, identify the new
run's session UUID from its launch output or Codex session metadata and replace
`--last` with that UUID. Do not guess when the paused local-mixing session could
be selected instead.
