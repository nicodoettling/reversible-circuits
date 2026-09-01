#!/usr/bin/env bash
set -uo pipefail

ROOT=/home/nico/projects/research_projects/reversible_circuits
RUN_DIR="$ROOT/experiments/20260824-bwrap-subagent-smoke"
LOG="$RUN_DIR/run.log"
RUNNER_STATUS="$RUN_DIR/runner-status.txt"
FINAL_MESSAGE="$RUN_DIR/coordinator-final.md"

mkdir -p "$RUN_DIR"
: >"$LOG"
: >"$RUNNER_STATUS"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf 'start_utc=%s\n' "$start_utc" | tee -a "$LOG" "$RUNNER_STATUS"
printf 'runner_pid=%s\n' "$$" | tee -a "$LOG" "$RUNNER_STATUS"
printf 'sandbox=workspace-write approval_policy=never timeout=20m subagents=2\n' \
  | tee -a "$LOG" "$RUNNER_STATUS"

set +e
timeout --foreground --signal=INT --kill-after=60s 20m \
  /home/nico/.local/bin/codex exec \
  --color never \
  --model gpt-5.6-sol \
  --sandbox workspace-write \
  -c 'approval_policy="never"' \
  -c 'model_reasoning_effort="medium"' \
  -C "$ROOT" \
  --output-last-message "$FINAL_MESSAGE" \
  - <"$RUN_DIR/prompt.md" 2>&1 | tee -a "$LOG"
codex_rc=${PIPESTATUS[0]}
set -e

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf 'end_utc=%s\n' "$end_utc" | tee -a "$LOG" "$RUNNER_STATUS"
printf 'codex_rc=%s\n' "$codex_rc" | tee -a "$LOG" "$RUNNER_STATUS"

if [ "$codex_rc" -eq 124 ]; then
  printf 'runner_verdict=TIMEOUT\n' | tee -a "$LOG" "$RUNNER_STATUS"
elif [ "$codex_rc" -eq 0 ]; then
  printf 'runner_verdict=COMPLETED\n' | tee -a "$LOG" "$RUNNER_STATUS"
else
  printf 'runner_verdict=FAILED\n' | tee -a "$LOG" "$RUNNER_STATUS"
fi

exit "$codex_rc"
