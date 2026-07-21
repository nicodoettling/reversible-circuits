# Experiments Index

## 20260617-214335 Two-Worker Sampler Test

- Coordinator synthesis: `20260617-214335-coordinator-synthesis/report.md`
- Worker A exact harness: `20260617-214335-worker-a-exact-harness/report.md`
- Worker B Hurwitz baseline: `20260617-214335-worker-b-hurwitz-baseline/report.md`

Result: exact small-case harness and pure Hurwitz negative-control baseline both succeeded. Pure Hurwitz is confirmed as an orbit sampler, not a global fixed-length identity-word sampler. Next step is testing orbit-breaking candidates.

## 20260710 Hurwitz Hitting-Time Tests

- Experiment specification: `20260710-hurwitz-hitting-times/plan.md`
- Agent prompt: `20260710-hurwitz-hitting-times/agent_prompt.md`
- Shared Hurwitz utilities: `20260710-hurwitz-hitting-times/common_hurwitz.py`
- Cycle-start test: `20260710-hurwitz-hitting-times/cycle_adjacent_repeat_hitting.py`
- Identity-start test: `20260710-hurwitz-hitting-times/identity_star_hitting.py`
- Report: `20260710-hurwitz-hitting-times/report.md`

Objective: run two separate Hurwitz-only hitting-time experiments.  Test A
starts from the cycle word `C_k` and measures the first adjacent equal pair.
Test B starts from random and worst-case identity words and measures hitting a
canonical star identity node, together with the relaxed star-support target.

Status: specified but not yet implemented or run.  The Python files are
placeholders, `results.jsonl` is empty, and both report verdicts are currently
inconclusive.  No mixing-time conclusion has been established.

## 20260721 Edge-Shift Hitting Time versus Cycle Structure

- Plan and process definition: `20260721-edge-shift-cycle-hitting/plan.md`
- Implementation: `20260721-edge-shift-cycle-hitting/edge_shift_hitting.py`
- Server configuration: `20260721-edge-shift-cycle-hitting/configs/server.json`
- Run instructions: `20260721-edge-shift-cycle-hitting/report.md`

Objective: measure the first proposed parallel edge under uniform ordered-wedge
edge shifting, starting from graphs whose vertices all lie on cycles.  Compare
hitting time against cycle rank, exact simple-cycle counts and lengths when
feasible, and several overlap topologies.