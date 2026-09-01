# M297 run manifest

Date: 2026-08-14 UTC.

- Mission: `M297-bodt-small-owner-tail`
- Owner: `/root/m297_bodt_small_owner_tail`
- Target: strict proof/reduction for the accepted M290/M293 BODT tail
- Convention: `(pq)(x)=p(q(x))`, displayed factors left-to-right
- Analytic scope: every odd `k>=3`, `n=3k`
- Computational scope: `k=9` only; exact standard-library arithmetic
- Python: `3.12.3`
- Nonstandard dependencies: none
- Seed: null (deterministic exact enumeration)
- Command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-83/mission-M297-bodt-small-owner-tail/bodt_k9_probe.py
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-83/mission-M297-bodt-small-owner-tail/bodt_k9_self_rows.py
```

- Imported project code/data: none in the primary probe; the self-row
  separator imports only the mission-local primary probe and rebuilds the
  source laws.
- Output: `bodt_k9_results.json`, `bodt_k9_self_results.json`
- Downstream inference: none

