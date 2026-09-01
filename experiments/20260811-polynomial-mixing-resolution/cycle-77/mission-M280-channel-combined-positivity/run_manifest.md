# M280 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
nonstandard_dependencies: null
deterministic: true
seed: null
network: unused
Magma/SAT/ILP: unused
```

Target: first separated fixed cell of the auxiliary uniform minimal
long-cycle factorization law under M73's nonlazy cyclic rank-two quotient
kernel.  Convention: `(pq)(x)=p(q(x))`; displayed factors left-to-right.

The sole new finite falsifier was fixed before execution:

```text
k=11, n=33, channels={1,2}, ell=2,...,31.
```

Command from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M280-channel-combined-positivity/exact_cp_k11.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M280-channel-combined-positivity/exact_cp_k11.json
```

Runtime recorded by the script: `101.58994345390238` seconds.  The checker
uses only the Python standard library and exact `Fraction` arithmetic.  No
predecessor code or data is imported.  Frozen M168's float was consulted
only after the exact output existed, for the phase-total calibration in the
report.

Source-lock checksum-file digests and the M277 corrections are recorded in
`checkpoint.md`.  All ten required inventories passed before substantive
derivation.  No predecessor, coordinator, manuscript, skill, or shared
project file was edited.
