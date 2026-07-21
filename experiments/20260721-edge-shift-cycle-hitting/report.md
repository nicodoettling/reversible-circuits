# Edge-Shift Cycle Hitting Experiment

## Status

Implementation complete; server-scale results are intentionally not committed.
The local smoke workflow completed 8 unit tests and 120 Monte Carlo trials
across 5 settings with no censored trial.

## Files

- `edge_shift_hitting.py`: generators, validation, exact/scalable cycle
  statistics, edge-shift walk, multiprocessing, JSONL checkpoints, and resume.
- `analyze_results.py`: CSV aggregation, censor-aware restricted means, and
  exploratory log-linear scaling models.
- `configs/smoke.json`: quick correctness run.
- `configs/server.json`: cycle-count, cycle-length, overlap, and theta sweeps.
- `run_server.sh`: server entry point.
- `slurm_job.sh`: editable `sbatch` template.
- `tests/test_edge_shift_hitting.py`: standard-library unit tests.
- `plan.md`: precise process and measurement definitions.

## Commands

From the repository root:

```sh
python3 -m unittest discover \
  -s experiments/20260721-edge-shift-cycle-hitting/tests \
  -p 'test_*.py' -v

python3 experiments/20260721-edge-shift-cycle-hitting/edge_shift_hitting.py \
  --config experiments/20260721-edge-shift-cycle-hitting/configs/smoke.json \
  --workers 1

python3 experiments/20260721-edge-shift-cycle-hitting/analyze_results.py \
  experiments/20260721-edge-shift-cycle-hitting/results-smoke.jsonl \
  --out-dir experiments/20260721-edge-shift-cycle-hitting/analysis-smoke
```

On a server or SLURM allocation:

```sh
WORKERS="${SLURM_CPUS_PER_TASK:-8}" \
  bash experiments/20260721-edge-shift-cycle-hitting/run_server.sh
```

Or submit the included template after adjusting its time, memory, and any
cluster-specific partition/account directives:

```sh
sbatch experiments/20260721-edge-shift-cycle-hitting/slurm_job.sh
```

Resume an interrupted run without repeating completed graph jobs:

```sh
RESUME=1 WORKERS="${SLURM_CPUS_PER_TASK:-8}" \
  bash experiments/20260721-edge-shift-cycle-hitting/run_server.sh
```

On resume, records from a graph without a final `graph_complete` checkpoint are
discarded before that graph is rerun, preventing partial trials from being
counted twice.

## Supplying an Arbitrary Graph

Add an explicit setting to a copied configuration:

```json
{
  "id": "my-graph",
  "generator": "edge_list",
  "n": 6,
  "edges": [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[5,2]],
  "graphs_per_setting": 1,
  "walks_per_graph": 1000,
  "max_steps": 2000000
}
```

The program rejects self-loops, duplicate edges, isolated vertices, and any
initial vertex that does not belong to a simple cycle.

## Known Limitations

- Exact simple-cycle enumeration is exponential in cycle rank and is skipped
  above the configured cap.  Cycle rank and fundamental-basis lengths remain
  available.
- The initial cycle-covered condition is not preserved.  This is part of the
  specified unrestricted edge-shift process, not a validation failure.
- `cycle_with_chords` is one controlled overlapping-cycle ensemble, not a
  uniform distribution over all graphs satisfying the initial condition.
- Hitting-time summaries are empirical and may be cutoff-sensitive; inspect
  censor fractions before fitting or interpreting scaling laws.
