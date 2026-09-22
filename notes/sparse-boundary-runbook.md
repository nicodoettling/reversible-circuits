# Sparse Boundary: One-Hour Run

Authorized 2026-09-22. Target: extend global negligible-error identity-word
sampling past m<=N^(2/3), using m^4<=N^3 as the benchmark, or prove an
asymptotic obstruction to the current H0 sampler. A weaker new extension
must be labeled separately; a failure of H1 alone does not refute H0.

## Configuration

- Model/effort: gpt-6-astra / ultra for all contexts.
- Six total contexts: coordinator plus five workers, no worker delegation.
- Cap: 1h, final 10m for synthesis, no automatic continuation.
- Profile: sandbox-only, workspace-write, approval never; search enabled.
- No installs, machine changes, old-file edits, commits or pushes.
- Output: experiments/20260922-sparse-boundary/.
- Prompt: notes/sparse-boundary-goal-run.md.
- Referee input: notes/sparse-boundary-blind-brief.md.
- Tmux: sparse-boundary-20260922.
- Prior September 7 and September 22 sparse-global artifacts are read-only.

## Launch

Do not repeat while active. --dry-run checks prerequisites without launching.
The helper needs host context for Bubblewrap/group/systemd checks; it does
not weaken the inner sandbox.

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py launch \
  --root /home/nico/projects/research_projects/reversible_circuits \
  --session sparse-boundary-20260922 \
  --prompt notes/sparse-boundary-goal-run.md \
  --log notes/sparse-boundary-run.log \
  --run-file experiments/20260922-sparse-boundary/tmux-run.json \
  --status-file experiments/20260922-sparse-boundary/tmux-status.json \
  --codex /home/nico/.local/bin/codex \
  --permission-profile sandbox-only \
  --model gpt-6-astra --reasoning-effort ultra --agents 6 --search \
  --max-runtime 1h --wrapup-before 10m
```

## Monitor

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/reversible_circuits/experiments/20260922-sparse-boundary/tmux-run.json
```

```sh
tmux attach -t sparse-boundary-20260922
```

```sh
tail -F /home/nico/projects/research_projects/reversible_circuits/notes/sparse-boundary-run.log
```

Authoritative absolute deadlines and service identity are in
notes/sparse-boundary-run.log.sparse-boundary-20260922.cap-status.json.
Health requires the live contained process and fresh heartbeat, not just
tmux. Requested concurrency must be checked against actual worker starts.
Completion can occur before the cap only after the mathematical goal and
audits close. A timed-out incomplete goal is not completed or paused.

Any later resume needs fresh user authorization, a new duration and exact
session ID, after confirming this service is stopped. Never kill the shared
tmux server or unrelated services, and never reset a live cap.

## Files and Verification

Setup creates these three sparse-boundary Markdown files in notes/. The
launcher creates its transcript/cap sidecar and the experiment's run/status
manifests. Workers write research only into the new experiment, with a final
inventory. Pre-existing untracked work is preserved, not attributed to this
run.

## Verified Startup

- Service activation: 2026-09-22 09:25:28.937730 UTC.
- Wrap-up: 10:15:28.937730 UTC; graceful shutdown: 10:24:23.937730 UTC.
- Hard envelope deadline: 10:25:28.937730 UTC.
- Coordinator session: 01a0c86f-4026-7bf2-955b-76e171b42774.
- Service: codex-cap-sparse-boundary-20260922-f29bda8ea57b.service.
- Observed startup: gpt-6-astra / ultra; workspace-write, approval never.
- Capped status HEALTHY, fresh heartbeat, active/running service and live
  populated cgroup. Systemd independently reports RuntimeMaxSec=3535,
  TimeoutStopSec=60, KillMode=control-group, SendSIGKILL=yes, Restart=no.
- CLI 0.154.0-alpha.6.2; host Bubblewrap/group preflight passed. The capped
  helper passed 18 unit tests; seven optional integration tests were not rerun.
- All five workers actually started between 09:26:17 and 09:27:45 UTC,
  without an intervening worker completion. Their persisted turn contexts
  report gpt-6-astra / ultra; all explicit spawn calls use fork_turns=none.
  This confirms six simultaneous contexts, beyond merely configured slots.
- Workers: r1_upper = 01a0c870-97bd-7623-b61a-65c43c814188;
  r2_obstruction = 01a0c870-da37-7620-9fbe-2fd6017f84d2;
  r3_diagnostics = 01a0c871-1c72-7420-a32a-9ae88e64794b;
  r4_construction = 01a0c871-53a2-7a42-bfb3-244f07e550b1;
  r5_referee = 01a0c86f-fc2d-78c0-a54d-96397be9867e.
- Coordinator reports its native goal active, without a token budget.
- Baseline commit: 20e86f665f69053031fe7eec0c3388458affb1fc. Tracked diff
  was empty at launch; existing untracked September 7 and sparse-global
  artifacts remain preserved. No commit or push was made by the launcher.
