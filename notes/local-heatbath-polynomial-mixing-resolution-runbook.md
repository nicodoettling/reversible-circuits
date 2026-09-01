# Runbook: Persistent Local Heat-Bath Mixing Goal

This runbook prepares the goal run. It does not launch it.

## Configuration manifest

- Repository root: /home/nico/projects/research_projects/reversible_circuits
- Preparation commit: 502a6f0
- Slug: local-heatbath-polynomial-mixing-resolution
- Tmux session: heatbath-mixing-goal
- Prompt: notes/local-heatbath-polynomial-mixing-resolution-goal-run.md
- Ledger: notes/local-heatbath-polynomial-mixing-resolution-resolution-ledger.md
- Resolution: notes/local-heatbath-polynomial-mixing-resolution-resolution.md
- Log: notes/local-heatbath-polynomial-mixing-resolution-run.log
- Codex path: /home/nico/.local/bin/codex
- Codex version: codex-cli 0.149.0-alpha.4.3
- Tmux version: tmux 3.4
- Permission mode: approval_policy="never"
- Sandbox mode: workspace-write
- Working directory flag: -C with the absolute repository root
- Prompt transport: stdin using a relative prompt path
- Persistence: enabled; --ephemeral is absent
- Requested subagent concurrency: up to 15, excluding the coordinator
- Total subagent-call cap: none
- Token cap: none
- Terminal condition: only the proof or refutation defined in the goal prompt
- Sandbox flag: --sandbox workspace-write
- Approval configuration: -c approval_policy=never
- Dangerous bypass: absent
- Shell wrapper: bash -lc with set -o pipefail
- Logging: tee on launch and tee -a on resume

The installed CLI was checked with:

    codex exec --help
    codex exec resume --help

Official Codex documentation confirms that codex exec accepts - for stdin and
that codex exec resume --last resumes the latest persisted exec session for
the working directory:
https://developers.openai.com/codex/cli/reference

## Sandbox status

The group-gated Bubblewrap/AppArmor setup is operational for `nico`. The
bounded two-subagent smoke test in
`experiments/20260824-bwrap-subagent-smoke/` passed: sandbox startup and
workspace writes succeeded, writes outside the allowed roots were denied, and
no approval prompt or Bubblewrap error appeared.

Launch from a fresh login whose supplementary groups include `codex-bwrap`.
The outer coordinator and its subagents run with `workspace-write` and
`approval_policy="never"`. They must use normal sandboxed commands and must not
request elevated, unsandboxed, full-access, or interactive execution. A task
that needs unavailable access or a missing dependency is recorded as blocked;
the run continues on other supported tasks. Do not add
`--dangerously-bypass-approvals-and-sandbox` or `--ephemeral`.

## Pre-launch audit

Run these from the repository root:

~~~sh
id -nG
command -v bwrap
bwrap --version
codex sandbox /bin/true
git status --short --branch
head -n 1 notes/local-heatbath-polynomial-mixing-resolution-goal-run.md
sed -n '1,12p' notes/local-heatbath-polynomial-mixing-resolution-resolution-ledger.md
tmux has-session -t heatbath-mixing-goal
~~~

Require `id -nG` to include `codex-bwrap`, `/usr/bin/bwrap` to be present, and
`codex sandbox /bin/true` to return zero. If group membership is absent, open a
fresh SSH login and start a new tmux server before retrying. The expected tmux
check before first launch is a nonzero exit status and "can't find session".
If a session already exists, inspect it rather than starting a duplicate.

## Exact launch command

Run exactly this command from any shell. It creates a detached session and
returns immediately.

~~~sh
tmux new-session -d -s heatbath-mixing-goal -c /home/nico/projects/research_projects/reversible_circuits \
  "bash -lc 'set -o pipefail; \
  codex exec --sandbox workspace-write -c approval_policy=never \
  -C /home/nico/projects/research_projects/reversible_circuits \
  - < notes/local-heatbath-polynomial-mixing-resolution-goal-run.md \
  2>&1 | tee notes/local-heatbath-polynomial-mixing-resolution-run.log'"
~~~

Do not add other Codex permission or sandbox flags.

## Attach and detach

Attach:

~~~sh
tmux attach-session -t heatbath-mixing-goal
~~~

Detach without stopping the run by pressing Ctrl-b, then d.

## Health and monitoring

Test whether the session exists:

~~~sh
tmux has-session -t heatbath-mixing-goal
~~~

Inspect pane process state:

~~~sh
tmux list-panes -t heatbath-mixing-goal -F '#{pane_pid} #{pane_dead} #{pane_current_command}'
~~~

Capture the most recent pane output:

~~~sh
tmux capture-pane -pt heatbath-mixing-goal -S -200
~~~

Inspect the latest log records:

~~~sh
tail -n 120 notes/local-heatbath-polynomial-mixing-resolution-run.log
~~~

Follow the log without attaching:

~~~sh
tail -F notes/local-heatbath-polynomial-mixing-resolution-run.log
~~~

Inspect durable research status:

~~~sh
sed -n '1,30p' notes/local-heatbath-polynomial-mixing-resolution-resolution-ledger.md
tail -n 160 notes/local-heatbath-polynomial-mixing-resolution-resolution-ledger.md
sed -n '1,240p' notes/local-heatbath-polynomial-mixing-resolution-resolution.md
~~~

A quiet pane is not evidence of termination. Use tmux has-session, pane state,
the log tail, and the ledger banner together.

## Graceful interruption

Prefer attaching and sending Ctrl-C once so the coordinator can run its
interruption policy. If the process cannot checkpoint itself, preserve the log
and manually set up a later resume; do not label the research resolved.

Do not kill unrelated process IDs or remove session data.

## Resume a persisted exec session

Use resume only after the original tmux session has ended. The command below
keeps the validated sandbox and approval configuration, selects the most recent
persisted exec session for this working directory, and appends to the same log.

~~~sh
tmux new-session -d -s heatbath-mixing-goal -c /home/nico/projects/research_projects/reversible_circuits \
  "bash -lc 'set -o pipefail; \
  codex exec --sandbox workspace-write -c approval_policy=never \
  -C /home/nico/projects/research_projects/reversible_circuits \
  resume --last \
  \"Resume the ACTIVE persistent goal. Read the resolution ledger and resolution document first, reconcile any interrupted assignments, and continue from the exact smallest open implication. Do not mark completion unless a terminal outcome survives refereeing.\" \
  2>&1 | tee -a notes/local-heatbath-polynomial-mixing-resolution-run.log'"
~~~

After resuming, verify that the ledger banner returns to ACTIVE and that a new
ledger entry records the resumed assignment set.

## Session identity fallback

If more than one persisted exec session exists for this repository, do not
guess. Identify the correct UUID from the original run output or persisted
session metadata, then substitute that UUID for --last in the exact tmux
resume command above. Keep the sandbox and approval options before the resume
subcommand.

## Post-run interpretation

RESOLVED is valid only when the frozen universal proof or frozen rigorous
refutation has three accepting fresh referee reports and all objections are
closed. Any process exit with ACTIVE status is an interruption. Any partial
theorem, failed route, or finite experiment leaves the mathematical status
UNRESOLVED.
