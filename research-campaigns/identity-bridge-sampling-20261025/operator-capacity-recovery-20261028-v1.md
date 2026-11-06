# Reviewed Capacity Recovery

Operator-side maintenance decision, 2026-10-28 (Europe/Berlin), acting under
the user's authorization for automatic same-mission capacity recovery and
their instruction that routine capacity conditions must not need manual care.

## Exact Prior Incident

Campaign identity-bridge-sampling-20261025, attempt 000001, native session
01a18176-ce37-7e33-92b4-9b74319a5485. The final native events were top-level
error and turn.failed with the exact message:

    Selected model is at capacity. Please try a different model.

Both events were inspected in the original attempt.log and exactly match the
new regression fixture. They carry no structured error code. The old v0.3.1
matcher knew only the shorter message and incorrectly left the outcome unknown.
This is a transient capacity incident, not a refusal or permission exception.
No other terminal error was found in the recorded turn.

Cleanup was verified: exact old service stopped, cgroup empty, adapter lock free,
tmux absent. Latest verified checkpoint is generation 2, coordinator commit
d8893491e04aff74ff3185f7054470ffa24a44a4. The worktree was clean before this
operator note. Existing research and historical attempt evidence are preserved.

## Repair and Recovery Decision

Installed a separate immutable harness v0.3.2, repair commit
bd89de2c1814523043b8a2cd44e4c76630538373. All 346 offline tests pass, including
seven new regressions for recorded events, real backend classification,
same-session resume, ten consecutive capacity failures/cooldown and STOP.
The operator skill was structurally validated and synchronized. Old releases,
attempts and manifest settings were not rewritten.

Resume the same frozen mission and exact native session using the supported
rearm/start commands. Retain four total agents, gpt-6-astra/ultra,
service_tier=default, workspace-write/auto-review, existing quota guards,
memory controls and same-mission recovery authorization. Do not change models
in response to the error message's suggestion.

Future recognized capacity failures use automatic backoff and one-hour cooldowns
after persistent failures, then retry. This note resolves only the old
misclassified capacity incident. It grants no permission to clear a STOP,
refusal, auth/permission failure, cleanup uncertainty or unrelated unknown error.
The optional manager remains disabled and no platform-restart delegation is added.

## Resumed Coordinator Handoff

Preserve the already committed preparation/intake and generation-2 checkpoint.
Confirm the current attempt's fresh runtime and run the tiny bounded-job smoke
through the CURRENT v0.3.2 helper and sealed run file before mathematical work.
Retain this note as operational provenance and reconcile its new discovery entry
at the next normal reviewed map/programme checkpoint. It is not a mathematical
finding. Continue the pending P0 admission and research tasks rather than
restarting completed preparation review.
