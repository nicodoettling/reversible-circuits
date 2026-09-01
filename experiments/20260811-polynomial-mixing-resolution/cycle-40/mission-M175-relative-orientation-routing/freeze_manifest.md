# M175 freeze manifest

Date: 2026-08-13 UTC.

## Ownership and base

- Mission: `M175-relative-orientation-routing`.
- Owned directory only:
  `experiments/20260811-polynomial-mixing-resolution/cycle-40/mission-M175-relative-orientation-routing/`.
- Repository base commit:
  `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- No predecessor, coordinator, manuscript, skill, or file outside the owned
  directory was edited.

## Frozen claim scope

- **PROVED:** the explicit synchronized signed-Hurwitz local gain formula.
- **PROVED:** `V_stab(q)` is exactly the `F_2` span of actual fundamental-
  cycle chord gains in the synchronized quotient Schreier component.
- **PROVED:** fixed-physical-endpoint zero-voltage routing is affine
  membership in that chord span.
- **PROVED using accepted M169/M172:** for accepted nonempty `d>=5` matching
  subfamilies, `K_mon/P_(d,s)` is that chord-column space.
- **EXACT FINITE:** at `d=3`, both ordered-pair components have rank zero;
  at `d=4`, component size/rank rows are `(120,0)`, `(240,0)`, `(4320,1)`,
  `(9720,0)`.
- **EXACT FINITE:** on the displayed `d=4` pair, chronological positive word
  `R_4 R_3 R_5 R_4` fixes both quotient points and has transporter sign bits
  `(1,0)`, hence nonzero relative voltage.
- **REFUTED at `d=3,4`:** the universal synchronized-character ansatz
  `kappa_j(a)=theta(a)+theta(R_j a)+c_j`.
- **UNRESOLVED:** the accepted `d>=5` matching chord rank, fixed physical DPS
  endpoint membership, and all polynomial word-length obligations.
- No `d=5` quotient orbit was enumerated. No common braid, gap, mixing, or
  Terminal claim is made.

## Deterministic validation

Environment: Python `3.12.3`, standard library only, `seed=null`.

Run from this mission directory:

```text
python3 -m compileall -q relative_orientation_cycle_audit.py
python3 -B relative_orientation_cycle_audit.py
python3 -B -c 'import json; q=json.load(open("results.json")); r3,r4=q["rows"]; assert r3["ordered_pair_cycle_space"]["all_pair_stabilizer_voltages_trivial"]; assert all(r["ordered_pair_cycle_space"]["augmented_bfs_cross_check_all"] for r in (r3,r4)); h=r4["ordered_pair_cycle_space"]["component_size_voltage_rank_histogram"]; assert h==[{"base_size":120,"count":1,"rank":0},{"base_size":240,"count":1,"rank":0},{"base_size":4320,"count":1,"rank":1},{"base_size":9720,"count":1,"rank":0}]; c=r4["ordered_pair_cycle_space"]["short_positive_certificate"]; assert c["endpoint_quotient_indices"]==c["source_quotient_indices"] and c["relative_voltage"]==1; assert [x["sign_bit"] for x in c["literal_transporters"]]==[1,0]; print("assertions ok")'
sha256sum -c SHA256SUMS
```

The exact checker completed successfully. It independently reconstructs
`d=3,4`, verifies each chord-rank result against direct augmented-cover BFS,
and directly replays the short `d=4` physical transporter certificate.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `halfway_checkpoint.md`
- `proof.md`
- `relative_orientation_cycle_audit.py`
- `results.json`
- `report.md`
- `freeze_manifest.md`
- `SHA256SUMS`

`git status --short` restricted to the mission directory reports only this
new owned directory. Generated `__pycache__` was removed before hashing.

