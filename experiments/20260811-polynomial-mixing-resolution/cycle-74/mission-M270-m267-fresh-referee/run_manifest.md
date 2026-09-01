# M270 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit=502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python=3.12.3
deterministic=true
seed=null
nonstandard_dependencies=none
network_used=false
packages_installed=false
```

Working directory:

```text
/home/nico/projects/research_projects/reversible_circuits
```

Retained checker command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-74/mission-M270-m267-fresh-referee/independent_check.py
```

The checker writes no file, imports no module, and reads no predecessor.  Its
captured output is `checker_results.txt`.  Frozen inventories were validated
with `sha256sum -c SHA256SUMS` from each mission directory.  The checker is
finite formula/boundary falsification only; the all-rank acceptance comes
from `proof_audit.md`.

