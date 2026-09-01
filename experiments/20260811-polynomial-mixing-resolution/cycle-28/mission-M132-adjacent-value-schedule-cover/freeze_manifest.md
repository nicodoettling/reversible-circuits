# M132 freeze manifest

Frozen: 2026-08-13 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen payload hashes

```text
6b1c2ea2f224b9c50e513915e54ec7e5224ee1677bf2984def90f73cf4042372  plan.md
87b881e404c83be797595cd35d602439d61fc9858aeb28c9bed7158c597e610d  checkpoint.md
8b7a2c222fc5cb55b95e7473378d9321c9145d1fa13025a71da8290205ea6eee  contour_metadata_obstruction.md
8b1f8abba35872b00e7921dcff7222b9f305894e5d396b2af9817028ef7c1b99  schedule_cover_audit.py
cebc4b8b07d007b31e1f52785c7fb63079f132205020bb1d650bfde6611cee53  results.json
3c253fd7530e5ece08a2533ac031c21d4fb04fb82a66ea60e6104a110bbb1cc3  results_d3.json
fee699657624366d8a88dce6557d40a310c556a754394418e2f38fb10a00f8d4  results_d4_metadata.json
ca8cef32a17cfe62c38eaaa92eeb994affcf6706a9018c8fcc5a1c8fe0951a7d  report.md
```

`results.json` is the final combined raw output. The two smaller JSON files
are deterministic development snapshots retained for provenance; no final
claim relies on them in place of `results.json`.

## Reproduction

```text
python3 -B schedule_cover_audit.py --d 3 4 --paths-through-d 3 \
  --max-metadata-pairs 1200 --output results.json
```

Python `3.12.3`, dependencies `{}`, seed `null`. The run is deterministic.

## Frozen scope

```text
PROVED: fixed-schedule agreement sets are independent in the conflict graph.
REFUTED: one schedule per tested O(d^40)-range two-label contour key.
EXACT d=3: conflict chi=3 while the true schedule-cover minimum is 5.
UNRESOLVED: general adjacent-value polynomial schedule cover.
```

No UST route, all-edge congestion, physical gap, `Gamma_0`, original
heat-bath gap, Terminal A, or Terminal B claim is included.

