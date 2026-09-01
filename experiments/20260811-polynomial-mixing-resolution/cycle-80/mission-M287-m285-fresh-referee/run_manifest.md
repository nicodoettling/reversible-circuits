# M287 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
nonstandard_dependencies: null
deterministic: true
seed: null
network: unused
Magma/SAT/ILP: unused
new_exact_rank: k=3 only
imports_predecessor_code_or_data: false
```

Target: fresh immutable audit of M285's strict owner-correlation coefficient
reduction and its canonical signed-PSD obstruction.  Convention:
`(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.

The sole clean-room exact command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-80/mission-M287-m285-fresh-referee/independent_k3_audit.py
```

The checker uses only the Python standard library and exact `Fraction`
arithmetic.  It does not read or import M285 or predecessor code/data.  Its
finite calculation checks conventions and the prescribed falsifier only;
it makes no all-rank positivity inference.

