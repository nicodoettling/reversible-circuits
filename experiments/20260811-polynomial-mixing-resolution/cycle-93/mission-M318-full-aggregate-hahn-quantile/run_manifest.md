# M318 run manifest

Date: 2026-08-14 UTC.

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: 3.12.3.
- Nonstandard dependencies: none.
- Randomness/seeds: none; all arithmetic is deterministic and exact.
- Experiment boundary: sole `k=13` guard after the analytic candidate was
  frozen; no other rank or grouping.
- Command:
  ```text
  python3 -B gqac_k13.py \
    --source ../../cycle-90/mission-M311-hahn-quantile-block-divergence/qbp_k11.py \
    --output gqac_k13.json
  ```
- Frozen source SHA-256:
  `703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94`.
- Result: exact finite GQAC survival at `k=13`; 648/648 prefixes and 216/216
  complete aggregates are positive.  No all-rank inference.
