# M313 run manifest

- Date: `2026-08-14` UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Seed: null; deterministic exact arithmetic
- Scope: auxiliary M91/M297 first-pair law, odd `k>=3`, `n=3k`
- Source gates: `source_lock.md`
- Sole finite command:

  ```text
  python3 -B mpcf_k13_h2_guard.py --output mpcf_k13_h2_results.json
  ```

- Elapsed guard time: `10.530196919105947` seconds
- Guard imports only SHA-gated M297 permutation/completion primitives; it
  reads no M305 checker or result data.
- Output: `mpcf_k13_h2_results.json`

