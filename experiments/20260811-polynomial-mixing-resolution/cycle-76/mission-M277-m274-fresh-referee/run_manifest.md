# M277 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
deterministic: true
seed: null
network: unused
clean_checker_nonstandard_dependencies: none
frozen_M274_checker_transitive_dependency: numpy 1.26.4
scope: auxiliary first fixed cell, odd k>=3
```

Decisive commands:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/check_monotonicity.py --output /tmp/m277-m274-monotonicity-rerun.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_exact.py --k 9 --output /tmp/m277-exact-sign-k9-rerun.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-76/mission-M277-m274-fresh-referee/cleanroom_sign_audit.py --m274-small experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/monotonicity_results.json --k9 experiments/20260811-polynomial-mixing-resolution/cycle-75/mission-M274-minority-sign-closure/exact_sign_k9.json --output experiments/20260811-polynomial-mixing-resolution/cycle-76/mission-M277-m274-fresh-referee/cleanroom_results.json
```

The clean checker imports no project module and no nonstandard package.  Its
odd-rank raw-atom loop through `k=21` is a sanity test for the separately
proved symbolic counterfamily, not evidence used to infer all ranks.
