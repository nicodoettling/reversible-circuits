# M323 run manifest

Date: 2026-08-14 UTC.

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: 3.12.3.
- Nonstandard dependencies: none.
- Randomness/seeds: none; all arithmetic is deterministic and exact.
- Computation boundary: sole predeclared `k=7,H_2` residual-support guard;
  no other row, rank, or surgery.
- Command:
  ```text
  python3 -B slpf_k7_h2_guard.py \
    --repo /home/nico/projects/research_projects/reversible_circuits \
    --output slpf_k7_h2_results.json
  ```
- Frozen dependency gates:
  ```text
  M297 SHA256SUMS  a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792
  primitive script 9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73
  ```
- Result: exact nonexceptional positive-residual prefix obstruction; `S_pf`
  refuted, no MPCF inference.
