# M330 run manifest

Date: 2026-08-14 UTC

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: 3.12.3.
- Random seeds: none; deterministic exact rational enumeration.
- Nonstandard dependencies: none.
- Finite scope: only `k=7,H_2`, cell `(1,1)`, A split-one raw residual
  fiber, and M323's fixed B atom `(6,14),(3,5)`.
- Command:

```text
python3 -B na_k7_h2_a_fiber.py \
  --repo /home/nico/projects/research_projects/reversible_circuits \
  --output na_k7_h2_a_fiber_results.json
```

The script uses `fractions.Fraction`, SHA-gates all imported frozen objects,
retains every A raw marked slot, and emits machine-readable exact results. It
does not use randomness, floating point, another cell/rank, or an alternative
surgery.

