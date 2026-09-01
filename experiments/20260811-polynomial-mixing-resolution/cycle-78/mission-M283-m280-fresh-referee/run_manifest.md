# M283 run manifest

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
```

Target: first separated fixed cell of the auxiliary uniform minimal
long-cycle factorization law under M73's nonlazy cyclic rank-two quotient.
Convention: `(pq)(x)=p(q(x))`; displayed factors left-to-right.

Exact command from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M283-m280-fresh-referee/cleanroom_cp_audit.py \
  --frozen-k11 experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M280-channel-combined-positivity/exact_cp_k11.json \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M283-m280-fresh-referee/cleanroom_results.json
```

The checker uses only the Python standard library and exact `Fraction`
arithmetic.  It imports no M280 or predecessor code.  It completes the new
`k=3` calculation before reading frozen M280 JSON for hash and exact
self-consistency checks.  It does not enumerate a new `k=11` row.

All required immutable inventory checks were run before derivation.  No
predecessor, coordinator, manuscript, skill, or shared project file was
edited.
