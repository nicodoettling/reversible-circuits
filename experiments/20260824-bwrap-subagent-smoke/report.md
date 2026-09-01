# Post-Run Audit

## Verdict

`PASS` for the group-gated Bubblewrap setup and `keep` for the bounded tmux
launcher, with one launcher correction recorded below.

## Observed Run

- Start: `2026-08-24T14:20:05Z`
- End: `2026-08-24T14:24:52Z`
- Wall time: `4 minutes 47 seconds`
- Codex exit code: `0`
- Runner verdict: `COMPLETED`
- Reported token use: `72,484`
- Subagents completed: `2`
- Bubblewrap errors: none
- Approval prompts: none
- Outer timeout: not reached

Both workers executed Python inside the `workspace-write` sandbox and wrote
their assigned artifacts. Both deliberate writes to `/home/nico` failed with
`Read-only file system`, and both forbidden paths remained absent. Direct word
enumeration and permutation-state dynamic programming independently returned
`S_3,m=4 = 27` and `S_4,m=4 = 120`; the coordinator reran both scripts.

## Collaboration Warning

The first inherited-context spawn call failed before creating a worker:

```text
collab spawn failed: no thread with id: ...
```

The coordinator retried with self-contained worker prompts and no inherited
conversation. Exactly two workers were then created and completed. Two later
hook warnings likewise reported that the ephemeral parent rollout could not be
found.

This is separate from Bubblewrap. The run was launched with `--ephemeral`, so
the missing parent rollout is consistent with unavailable persisted parent
metadata, although this single run does not prove causation. The reusable
`run.sh` has therefore been corrected to omit `--ephemeral`. Future
multi-agent and goal runs should retain parent session metadata.

## Scope

This validates local sandbox startup, workspace confinement, two-worker
coordination, logging, synthesis, and clean termination. It makes no claim
about sampler quality or mixing time.
