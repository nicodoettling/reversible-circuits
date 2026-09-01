# M142 freeze manifest

Freeze date: 2026-08-13 UTC.

## Mission and verdict

Fresh independent referee for the immutable M139 two-edge-core curvature
package.

Verdict:

```text
ACCEPT:
  marked-pair iff two-edge-core theorem and exact recurrence;
  q_a species weight and unordered-core factor 1/2;
  coupled Phi cavity, Lagrange/Psi and I_2 reductions;
  beta cut transform and exact c=2,3 boundaries;
  shifted-ULC, inverse-linear-surplus, and raw-TP obstructions.

UNRESOLVED:
  universal H2 log-concavity and quantitative surplus;
  higher-core budget and full H log-concavity;
  every downstream projection, sampler-gap, and terminal claim.
```

Numbered blocking objections: none.

## Immutable M142 artifacts

| artifact | SHA-256 |
|---|---|
| `plan.md` | `f6bd44b96c75bc5b84bb4f70caf49e8744b7f2155615492a5fc0d0dd3f9de079` |
| `checkpoint.md` | `6f35ef29de26449b947951a73fa1055f8826b8d4c0c75ec2cbc4d909dc26388c` |
| `clean_room_audit.py` | `56c5abaf347bc72df91f6141824f8db16eee0366643ce59c180b423069e9f04c` |
| `results.json` | `6876c7b6c186c4920c816f507df9344558e9f0f8cdfab992959334d6d7f299ca` |
| `report.md` | `062a998480ad5a969d8a29faa114e6e9fe3e67a0a441725829ecef0093572ccd` |

The final `SHA256SUMS` inventory additionally hashes this manifest.  It does
not hash itself.

## Frozen M139 anchors

| artifact | SHA-256 |
|---|---|
| report | `3a9998104df900cc8385793acc74b6151784e7920486553a4b4382fbe3b73103` |
| proof | `cb067b68ac404f60314f4d85bcb3894c15f55abae1b0276ac8a6e5a3238c6461` |
| checker | `605e01db0ca51f2f5b7fd3a3dea4e6449fb546d9acb6a9c7f5bbfb41aaa9e085` |
| results | `f2bdb9a2a43f88e943e59c303182914beede626fbd8a73cbb771e51ae2fd5873` |
| analytic certificate | `ce9d5b037f5a4214473f45b805719e323db611ad3a044ab894ee6e78a5946db6` |
| curvature budget | `82845e78055032c6c9f7099058eff8699d190ca94a51cf0e312b4e391b8a4bb6` |
| manifest | `ddbcdc572626bfd72a210082866a967703310f1e6548cb49aff58e99fadbb12f` |
| SHA256SUMS | `aaf23ad3ad94e96d592c5e0234a7432c22dc4790ad229a34880f7e2072db99dd` |

The complete M139 eleven-file inventory was also checked successfully.

## Reproduction

From repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-33/mission-M142-m139-fresh-referee/clean_room_audit.py --max-d 16 --output experiments/20260811-polynomial-mixing-resolution/cycle-33/mission-M142-m139-fresh-referee/results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`; Python `3.12.3`; standard
library only; deterministic exact arithmetic; `seed=null`.

## Audit invariants and hygiene

- Literal incidence topology is capped at six atoms.
- Literal weighted enumeration is capped at `d=5`.
- The separate marked recurrence is capped at `d=16`, exactly the first
  claimed inverse-linear counterexample; it was not extended.
- Every independently computed row through `d=16` matches the frozen M139
  row, while all positive LC signs remain explicitly finite-only.
- The initial aborted local run produced no retained output; the final output
  is from the corrected exact-rational checker.
- The compile-only `__pycache__` was removed before freeze.
- No dependency, commit, push, manuscript, skill, coordinator file, M139
  file, predecessor file, or other worker directory was changed.
