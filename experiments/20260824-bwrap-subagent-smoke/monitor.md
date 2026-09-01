# Monitoring

The tmux session is `codex-bwrap-smoke`.

While it is running:

```bash
tmux has-session -t codex-bwrap-smoke
tmux capture-pane -pt codex-bwrap-smoke -S -120
tail -n 120 experiments/20260824-bwrap-subagent-smoke/run.log
tail -F experiments/20260824-bwrap-subagent-smoke/run.log
```

Milestones, when present:

```bash
cat experiments/20260824-bwrap-subagent-smoke/progress.log
```

After termination:

```bash
cat experiments/20260824-bwrap-subagent-smoke/runner-status.txt
cat experiments/20260824-bwrap-subagent-smoke/result.json
sed -n '1,200p' experiments/20260824-bwrap-subagent-smoke/summary.md
```
