#!/usr/bin/env bash
set -euo pipefail

experiment_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
workers="${WORKERS:-${SLURM_CPUS_PER_TASK:-1}}"
output="${OUTPUT:-${experiment_dir}/results-server.jsonl}"
analysis_dir="${ANALYSIS_DIR:-${experiment_dir}/analysis-server}"

resume_args=()
if [[ "${RESUME:-0}" == "1" ]]; then
  resume_args+=(--resume)
fi

python3 "${experiment_dir}/edge_shift_hitting.py" \
  --config "${experiment_dir}/configs/server.json" \
  --output "${output}" \
  --workers "${workers}" \
  "${resume_args[@]}"

python3 "${experiment_dir}/analyze_results.py" \
  "${output}" \
  --out-dir "${analysis_dir}"
