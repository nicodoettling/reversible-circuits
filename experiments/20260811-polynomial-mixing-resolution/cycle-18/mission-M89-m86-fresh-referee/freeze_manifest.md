# M89 freeze manifest

Frozen: 2026-08-12 UTC.

Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Decision

```text
ACCEPT M86 WITH ZERO MATERIAL OBJECTIONS.
```

## Immutable source boundary

The audit used the following frozen M86 sources, whose requested hashes were
independently verified before review:

```text
5c09b466fc404ee7145f87125456f23e539fffb1e8c0aeff0264ded32a78a6ff  ../mission-M86-voltage-signed-bypass/report.md
c147163c711ba06b82b8248d0d86fe4ef6ecd7d8b8ae9c2014944e1bc7e25682  ../mission-M86-voltage-signed-bypass/signed_cover_theorem.md
34e1d07d5cda1188dc757d3eb9b6bd32ff5c6daddef5471bdb9f2a124e7d5cbd  ../mission-M86-voltage-signed-bypass/SHA256SUMS
```

`sha256sum -c` also passed for every entry in M86's ten-file manifest.  M89
made no edit to M86 or to any other predecessor artifact.

## Frozen M89 payload

```text
a52957985bef24139c9f90c89e5917b22ef6e4a234883cd19147d618f27fd9c8  checkpoint.md
0d7a606e018d6b1ddc7d4efff8deae67e864365e912dacf69e96532aeaf88332  family-rerun.json
0c7af15155c8e451d1f3f451dbe79c5cd764bdbd29622fadc23dcaf334ed15f2  general_pullback_probe.py
0b580ad0503003e69cd98d797f420ea6c394f88b50abba61b5565315aeb95c09  local-rectangle-rerun.json
e27b4a7c97d2738165e951222dab6e7cd0a6ca21bc694e8ea6fef1b907fadcbc  plan.md
9496bdbb6a56814229cb07f9846896f92af8368ee0dd20f4499c7b7486311e24  pullback-probe.json
b1de5bff15be9e9fe682ebaa0afe51d1cc5e35b9c35da3b33ce363219e5ac421  report.md
```

The separately generated `SHA256SUMS` includes this manifest itself and is
the authoritative final payload check.  It intentionally does not hash
itself.

## Reproduction metadata

Python: `3.12.3`.  Nonstandard dependencies: none.  Fixed seeds and exact
commands are recorded in `report.md` and in the JSON `argv` fields.  The
family and local-rectangle reruns are exact finite falsification checks.  The
four fixed-seed signed walks in `pullback-probe.json` are exact on every
visited state but empirical in state-space coverage.

All `__pycache__` directories and `.pyc` files created during this review
were removed before freeze.
