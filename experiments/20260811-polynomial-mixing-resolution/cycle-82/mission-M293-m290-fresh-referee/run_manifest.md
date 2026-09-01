# M293 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
nonstandard_dependencies: null
deterministic: true
seed: null
network: unused
Magma/SAT/ILP: unused
new_exact_rank: k=9 only
guard_wall_time_seconds_observed: approximately 109
guard_imports_predecessor_code_or_data: false
```

The sole exact reconstruction command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-82/mission-M293-m290-fresh-referee/independent_k9_guard.py
```

The program uses only the Python standard library and exact `Fraction`
arithmetic. The retained `guard_results.json` was added without running
another rank. The exponential enclosure uses 60 Taylor terms and the rigorous
tail bound `0<e-sum_(j=0)^60 1/j!<2/61!`.

Read-only provenance commands independently computed each top checksum,
ran `sha256sum -c SHA256SUMS`, counted inventory lines, and compared actual
top-level file counts for M290 and all twelve cited predecessors.
