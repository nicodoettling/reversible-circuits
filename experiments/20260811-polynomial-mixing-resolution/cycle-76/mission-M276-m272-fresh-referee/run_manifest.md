# M276 run manifest

Date: 2026-08-14 UTC.

```text
repository_commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
deterministic: true
seed: null
nonstandard_dependencies: none
network: unused
target: auxiliary balanced first fixed cell, odd k>=3
```

The independent checker imports no project module and reads no M272 or
predecessor code/data.  Its sole run is the predeclared exact `k=3,5` run
printed verbatim in `report.md` and `independent_results.json`.

After that independent result was frozen, the two M272 checkers were rerun
read-only at `k=3,5,7` with outputs under `/tmp`; their result arrays match
the frozen JSON exactly.  Temporary rerun files are not payload artifacts.

