# M281 run manifest

Date: 2026-08-14 UTC.

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Nonstandard dependencies: none.
- Random seed: none; the census is deterministic and exhaustive.
- Audited target: frozen M278 inventory
  `352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad`.
- Locked DPS source: `/tmp/DuPoSc13.pdf`, SHA-256
  `98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
- Clean-room command:
  `python3 -B cleanroom_fixed_edit_check.py`.
- Prescribed scope: all root-leaf templates at `d=5,6`; no route search.
- Frozen-M278 replay: imported the frozen guard read-only, redirected its
  `OUTPUT` to `/tmp/m281_m278_guard_replay.json`, and called `main()`.
- No predecessor, coordinator, manuscript, goal, skill, or M278 file was
  edited.

