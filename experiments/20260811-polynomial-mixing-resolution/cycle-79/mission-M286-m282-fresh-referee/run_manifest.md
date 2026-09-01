# M286 run manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Mission: fresh immutable audit of M282's `CSBV` proof
- Convention: `(pq)(x)=p(q(x))`; displayed factors left-to-right
- Parameter regime: odd `k>=3`, `D=2k-1`, `R=2k-3`, `n=3k`
- Computation: deterministic clean-room completion-count reconstruction at
  `k=3,5`; formula-only boundary falsification through `k=65`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Network: unused
- Seed: `null`
- M282/predecessor edits: none
- Shared durable-file edits: none

Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-79/mission-M286-m282-fresh-referee/cleanroom_csbv_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-79/mission-M286-m282-fresh-referee/cleanroom_results.json
```
