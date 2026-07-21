#!/usr/bin/env bash
#SBATCH --job-name=edge-shift-cycles
#SBATCH --cpus-per-task=16
#SBATCH --mem=8G
#SBATCH --time=24:00:00
#SBATCH --output=edge-shift-cycles-%j.out

set -euo pipefail

experiment_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export WORKERS="${SLURM_CPUS_PER_TASK:-16}"

bash "${experiment_dir}/run_server.sh"
