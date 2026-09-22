# Run manifest

Repository commit: 20e86f665f69053031fe7eec0c3388458affb1fc. Python 3.12.3; standard library for planned computations. Initial status and environment are saved separately. Old dependency SHA256 values are in source_hashes.json. Launcher artifacts and pre-existing untracked research/notes are excluded from research attribution.

One native goal created without token budget at 09:25:45 UTC (thread 01a0c86f-4026-7bf2-955b-76e171b42774). Only coordinator owns it. No extra service, tmux, coordinator or external run launched.

Requested capacity: six contexts total, five worker slots. Observed startup: all five spawn calls succeeded and list_agents at approximately 09:28 UTC showed coordinator plus all five running. This verifies startup, not an independently observable backend model identity. Each call explicitly requested gpt-6-astra, ultra, fork_turns=none; no substitution.

| Role | Agent ID | Owned directory | Requested model / effort |
|---|---|---|---|
| Upper bounds | /root/r1_upper | roles/r1-upper | gpt-6-astra / ultra |
| Obstruction | /root/r2_obstruction | roles/r2-obstruction | gpt-6-astra / ultra |
| Diagnostics | /root/r3_diagnostics | roles/r3-diagnostics | gpt-6-astra / ultra |
| Construction | /root/r4_construction | roles/r4-construction | gpt-6-astra / ultra |
| Blind referee | /root/r5_referee | roles/r5-referee | gpt-6-astra / ultra |

Assignments require workers to preserve their complete inputs and hashes. R5 received only the blind brief path and operational/safety instructions, with no surrounding fork. Same-model review is correlated internal review, not external human certification.

Timing authority: tmux-run.json plus ../../notes/sparse-boundary-run.log.sparse-boundary-20260922.cap-status.json, activation 2026-09-22T09:25:28.937730Z, wrap-up 10:15:28.937730Z, graceful 10:24:23.937730Z, hard 10:25:28.937730Z. Sandbox-only workspace-write approval never. No installs, escalation, permission/config changes, commits, pushes, detached jobs or cap extensions.
