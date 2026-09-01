# M279 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
deterministic: true
seed: null
nonstandard_dependencies: none
network: unused
target: M276 append-only salvage, auxiliary balanced cell, odd k>=3
```

The analytic proof and source-gate audit preceded the clean-room checker.
The retained finite command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M279-m276-fresh-referee/cleanroom_salvage_check.py
```

The checker imports no project/predecessor module and reads no M276/M272
artifact.  Its predeclared exact channel ranks are `k=3,5,9`; its predeclared
tail-calibration ranks are `k=3,5,9,31,101`.

After the M279 proof and checker were complete, M276's checker was inspected
and replayed read-only to `/tmp`.  The replay was byte-identical to M276's
frozen `independent_results.json`; the temporary output was removed.

