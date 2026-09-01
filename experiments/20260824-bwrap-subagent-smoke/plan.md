# Two-Subagent Bubblewrap Smoke Test

## Objective

Verify an ordinary non-interactive Codex run launched from tmux can:

1. start exactly two subagents;
2. execute local commands through the `workspace-write` sandbox;
3. write inside this experiment directory while denying a write outside the
   repository;
4. collect independent finite computations from both subagents; and
5. synthesize the results and terminate without an approval prompt.

This is an infrastructure smoke test, not a goal run and not evidence about
asymptotic mixing.

## Limited Task

Independently count identity transposition words in:

- `S_3` at length `4`, expected count `27`;
- `S_4` at length `4`, expected count `120`.

Worker A uses direct word enumeration. Worker B uses dynamic programming over
permutation states. The independent methods make the task useful as a small
coordination check without opening a research branch.

## Configuration

- Repository commit at preparation: `502a6f0`
- Codex version: `0.149.0-alpha.4.3`
- Model: `gpt-5.6-sol`
- Reasoning effort: `medium`
- Subagents: exactly `2`
- Sandbox: `workspace-write`
- Approval policy: `never`
- Session metadata: persisted so subagents can resolve the parent transcript;
  this is still a bounded non-goal run
- Network: not needed
- Outer timeout: `20 minutes`, then `SIGINT`, then `SIGKILL` after 60 seconds
- Tmux session: `codex-bwrap-smoke`

## Pass Conditions

- Both subagents return and leave distinct artifacts in their assigned
  directories.
- Both can execute Python and write inside the repository.
- Both receive a nonzero result when attempting their named write outside the
  repository, and neither outside file exists afterward.
- Both methods report `27` and `120`.
- The coordinator writes `result.json` with `status: "PASS"` and exits with no
  `bwrap`, `RTM_NEWADDR`, approval, or timeout failure.

## Expected Failure Modes

- Bubblewrap initialization failure.
- A subagent is not spawned or never returns.
- Parent transcript metadata is unavailable during subagent dispatch.
- A command requests unavailable escalation despite `approval_policy=never`.
- The outer timeout terminates the run.
- One independent implementation reports incorrect counts.

## Artifacts

- `run.log`: complete coordinator output
- `runner-status.txt`: outer process timing and exit code
- `progress.log`: explicit coordinator milestones
- `workers/worker-a/`, `workers/worker-b/`: independent artifacts
- `result.json`: machine-readable verdict
- `summary.md`: concise interpretation
- `coordinator-final.md`: final Codex message
