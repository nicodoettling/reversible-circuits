# M139 freeze manifest

Freeze date: 2026-08-13 UTC.

## Mission

Target: two-parallel-edge-core log-concavity and quantitative curvature for
the accepted M125/M129 defect coefficients after the accepted M133/M136
unique-cycle decomposition.

Verdict:

```text
PROMOTE FOR FRESH AUDIT:
  exact marked-pair recurrence;
  exact coupled cavity / Lagrange / beta-integral reduction;
  exact H2 boundaries c=2,3.

REFUTED:
  shifted ULC at d=4,c=3;
  universal inverse-linear surplus 1+1/d at d=16,c=12;
  direct same-orientation TP2/PF closure at the raw Phi cavity level.

UNRESOLVED:
  ordinary universal H2 log-concavity;
  sufficient quantitative H2 surplus;
  universal higher-core curvature budget;
  full H log-concavity and all downstream gaps.
```

No original heat-bath or terminal claim is made.

## Immutable mission artifacts

| artifact | SHA-256 |
|---|---|
| `plan.md` | `0f6ed54da044975248c10ab26c52e4a81aba54d98e70d2652d561a8e59b450c1` |
| `checkpoint.md` | `63015ca0f5dcfa24f37040548aadca0bfe2e8099999617020643b259ed237c62` |
| `two_edge_core_reduction.md` | `cb067b68ac404f60314f4d85bcb3894c15f55abae1b0276ac8a6e5a3238c6461` |
| `two_edge_core_scan.py` | `605e01db0ca51f2f5b7fd3a3dea4e6449fb546d9acb6a9c7f5bbfb41aaa9e085` |
| `two_edge_core_results.json` | `f2bdb9a2a43f88e943e59c303182914beede626fbd8a73cbb771e51ae2fd5873` |
| `analytic_certificates.py` | `c7a13554a6cd268488505a7f0ff2f447bacafb90982761f86a3a0b1a0a39716b` |
| `analytic_certificates.json` | `ce9d5b037f5a4214473f45b805719e323db611ad3a044ab894ee6e78a5946db6` |
| `curvature_budget.py` | `a0136101c5da3f2126e2cb93bffe0060702d89f9bc46b3d8577486141c0619b1` |
| `curvature_budget_results.json` | `82845e78055032c6c9f7099058eff8699d190ca94a51cf0e312b4e391b8a4bb6` |
| `report.md` | `3a9998104df900cc8385793acc74b6151784e7920486553a4b4382fbe3b73103` |

The `SHA256SUMS` inventory additionally hashes this manifest.  The inventory
does not hash itself.

## Frozen predecessor anchors

| predecessor | report SHA-256 |
|---|---|
| M125 exact defect coefficients | `dc8f8cb0ab9c6c06f9b49cd56a30b29cc258698dcdfccceb887b265ff67c5879` |
| M129 fresh audit of M125 | `eb7cdcd179a704deed4a8b7cb03a7a69c912bc0b57677a7fb2d886d17056b2d4` |
| M133 positive unique-cycle reduction | `afd0fcc3dddc51f20c8eb2d3b2d7eeb2d25aa3c9eaea204d91b958adf537619e` |
| M136 fresh audit of M133 | `23e14408ff585eb57db79a876c77edafc382f61b9562c5d3748948ed79eee710` |

## Reproduction

From repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_scan.py --max-d 18 --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/analytic_certificates.py --h2-results experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/analytic_certificates.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/curvature_budget.py --h2-results experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/two_edge_core_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-32/mission-M139-two-edge-core-curvature/curvature_budget_results.json
```

Environment: repository base commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`; Python `3.12.3`; standard
library only; deterministic exact arithmetic; `seed=null`.

## Audit invariants

- New marked recurrence equals every frozen M133 H2 profile through `d=8`.
- Boundary formulas `c=2,3` equal every retained marked row through `d=18`.
- Lagrange/Phi exponent certificates have zero failures.
- H2 finite scan is capped at `d=18`; no asymptotic claim uses its signs.
- Higher-core budget is retained explicitly and is finite only.
- Four obsolete duplicate analytic-search processes were terminated; their
  output was not retained or used.
- No cache, external dependency, stochastic output, commit, push, or shared
  durable-file edit is part of this package.
