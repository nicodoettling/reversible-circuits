# M282 run manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Mission: channel-two signed scalar-Abel vector bound (CSBV) only
- Convention: `(pq)(x)=p(q(x))`; displayed factors left-to-right
- Parameter regime: odd `k>=3`, `D=2k-1`, `R=2k-3`, `n=3k`
- Computation: one deterministic exact formula-only falsifier, no randomness
- Python: `3.12.3`
- Nonstandard dependencies: none
- Network: unused
- Seed: `null`
- Predecessor edits: none
- Shared durable-file edits: none

Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M282-channel-two-csbv/coefficient_probe.py --k 3 5 7 9 15 31 --output experiments/20260811-polynomial-mixing-resolution/cycle-78/mission-M282-channel-two-csbv/coefficient_results.json
```

