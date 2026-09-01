# M310 run manifest

- Date: `2026-08-14` UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Seed: null; deterministic checks
- Parent:
  `cycle-88/mission-M305-socl-combined-borel-divergence`
- Required parent top digest:
  `4e81c82223820cde35a8eecb7e8eb837733c5cd97ccb0375ae44d2a012392b46`
- Gate commands: `sha256sum -c SHA256SUMS` and
  `sha256sum SHA256SUMS` in the parent and every cited predecessor.
- Sole finite replay, from the frozen M305 directory:

  ```text
  python3 -B cbpv_k11_guard.py --output /tmp/m310_cbpv_k11_replay.json
  ```

- Replay elapsed: `52.69790212716907` seconds
- Frozen elapsed: `53.307632458163425` seconds
- Comparison: exact JSON equality after deleting only `elapsed_seconds`
- The replay imported the frozen M297 dependency exactly as M305 declares;
  the independent proof reconstruction imported no checker or data.

