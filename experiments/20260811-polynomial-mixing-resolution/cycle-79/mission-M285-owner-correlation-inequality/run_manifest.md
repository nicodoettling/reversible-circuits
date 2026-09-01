# M285 run manifest

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

Target: the signed channel expectation of the diagonal-repaired residual
owner autocorrelation for the first separated fixed cell.  Convention:
`(pq)(x)=p(q(x))`; displayed factors left-to-right.

The sole predeclared command, run once from the repository root, was:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-79/mission-M285-owner-correlation-inequality/psd_obstruction_k3.py --output experiments/20260811-polynomial-mixing-resolution/cycle-79/mission-M285-owner-correlation-inequality/psd_obstruction_k3.json
```

The checker uses only the Python standard library and exact `Fraction`
arithmetic.  It rebuilds both source laws directly, checks the conditional
channel masses, triangle transfer, literal/repaired equality, reflection,
and all admissible OCI values, then searches only the prescribed `k=3`
signed circular kernel for an exact rational PSD witness.  It does not read
or import predecessor code or data.  No other rank or falsifier was run.

All immutable inventory checks preceded the symbolic derivation.  No
predecessor, coordinator, manuscript, skill, or shared project file was
edited.
