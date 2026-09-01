# M290 run manifest

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
wall_time_seconds: 10.08
imports_predecessor_code_or_data: false
```

Target: convention/falsification check for the already-fixed DSR candidate,
with the two normalized source laws reconstructed from completion counts and
the complete `A e^2+B` coefficient evaluated before signs.

The sole exact command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-81/mission-M290-decorated-owner-ratio-bv/k9_symbolic_falsifier.py
```

The checker uses only the Python standard library and exact `Fraction`
arithmetic.  It imports no predecessor code or data.  The rational enclosure
of `e` uses 50 Taylor terms and the rigorous tail bound
`0<e-sum_(j=0)^50 1/j!<2/51!`.  No other rank was run.
