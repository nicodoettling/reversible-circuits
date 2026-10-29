# Genus Scaling: Four-Hour Run

Authorized2026-10-28: fresh gpt-6-astra/ultra session; four total agents;
one external four-hour cap, final20minutes for delivery. Primary target:
genus-uniform parameter dependence for connected identity-bridge sampling,
with genus3 as a diagnostic rather than the main success criterion.

Prompt: [genus-scaling-4h-run.md](genus-scaling-4h-run.md).

## Isolation and Limits

The tested v0.4.2 harness is used only as a one-attempt time/memory/quota backend.
Automatic restart, quota resume and separate campaign manager are disabled.
The old identity-bridge-sampling campaign remains STOPPED; never rearm it as
part of this allocation. A stopped attempt requires a later user decision.

Source baseline: reviewed I1 commit1fe07986764490ebeabb9bccf77e3d713e2a8f95.
New isolated branch: campaign/genus-scaling-20261028. The initializer made
bootstrap commitb178daf320833e859dcdee0ce56eb16c6d2130b7 from that baseline.
All old uncommitted I2 work and primary-worktree edits remain untouched.

Operational root:

    .campaigns/genus-scaling-20261028/

Research worktree:

    .campaigns/genus-scaling-20261028/worktree/

Research outputs relative to that worktree:

    experiments/20261028-genus-scaling/
    research-campaigns/genus-scaling-20261028/

Profile: workspace-write/auto-review; default tier for every context. Aggregate
MemoryMax128GiB, MemoryHigh96GiB, swap0. Bounded experimental jobs have a
16GiB address-space ceiling, explicit timeout and one-job-at-a-time reservation;
smaller limits are preferred for small checks. Local MCP servers are disabled
by the sealed backend. Quota notices3%, stop1%; no automatic refill resume.
The research service has Restart=no and a14400-second total shutdown envelope.
Local coordinator checkpoint commits on the isolated branch are permitted;
workers never commit and no push is authorized. No native goal was requested.

## Monitor

```bash
codex-campaign status --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/genus-scaling-20261028/campaign.json
```

```bash
tail -F /home/nico/projects/research_projects/reversible_circuits/.campaigns/genus-scaling-20261028/attempts/000001/attempt.log
```

The run.json/status.json/cap.json/runtime.json under that attempt identify the
exact tmux session, model controls, process containment and absolute deadlines.
Do not confuse a live metadata supervisor with active model progress. Confirm
fresh native runtime and actual worker starts, not only requested agent slots.

## Verified Startup

- Activated2026-10-28T14:39:21Z; wrap-up18:19:21UTC; total cap18:39:21UTC.
- Fresh coordinator session01a182f3-8cc8-7651-9871-cb522efcd707.
- Current runtime verifies gpt-6-astra, effortultra, collaboration effortultra,
  workspace-write and auto_review at the new run's exact hash.
- Service codex-harness-4680a408e8e14ce600819242f40cc197.service is active,
  populated and contained; kernel memory controls are verified.
- RuntimeMaxSec14335, TimeoutStopSec60, KillModecontrol-group, SendSIGKILLyes,
  Restartno. Aggregate MemoryMax128GiB, MemoryHigh96GiB, swap0.
- Four total agents are requested/configured; coordinator activity is observed.
  Actual worker startup must be checked separately, not inferred from the cap.
- Explicit default tier is configured; independent server-returned tier is
  unavailable. Startup quota reading63%; no reset/refill action is authorized.
- Original identity-bridge-sampling campaign remains STOPPED without an attempt.

```bash
tmux attach -t rh-4680a408e8e14ce600819242f40cc197
```

## Stop

```bash
codex-campaign stop --manifest /home/nico/projects/research_projects/reversible_circuits/.campaigns/genus-scaling-20261028/campaign.json
```

Never reset/rewrite old caps, remove a STOP automatically or kill the shared
tmux server. At timeout, retain unresolved claims and the exact handoff; no
automatic successor research or manager selection is enabled.
