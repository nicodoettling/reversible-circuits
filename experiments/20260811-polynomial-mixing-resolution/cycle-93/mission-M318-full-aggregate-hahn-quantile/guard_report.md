# M318 sole exact `k=13` guard

Date: 2026-08-14 UTC.

Verdict: **finite survival of the frozen `GQAC_1`; no all-rank inference.**

## Reproduction

The standard-library script SHA-gates frozen M311 checker `qbp_k11.py` at

```text
703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94
```

and makes exactly the declared mechanical changes `K=11 -> 13` and the
corresponding lag-count assertion `30 -> 36`.  It changes no quantile
transport, owner response, rung, sign block, or grouping.

```text
python3 -B gqac_k13.py \
  --source ../../cycle-90/mission-M311-hahn-quantile-block-divergence/qbp_k11.py \
  --output gqac_k13.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python 3.12.3, standard
library only, deterministic exact rational arithmetic, no seed.

## Exact finite result

The guard has `k=13`, `n=39`, six middle-cut classes, thirteen middle phases
per class, 36 admissible lags, and 216 full rows.  Its canonical Abel signs
give exactly three maximal blocks, with signs `(-,+,0)`.

- QTI exact: `true`.
- QBD exact: `true`.
- reflection exact: `true`.
- canonical GQAC prefixes tested: `648`.
- negative prefixes: `0`; rows with a negative prefix: `0`.
- complete aggregates tested: `216`; positive: `216`; zero/negative: `0/0`.
- the minimum prefix is the terminal prefix at `(u,ell,block)=(2,12,2)`,
  approximately `0.09995960785422768`.
- the same minimum complete aggregate occurs at `(u,ell)=(2,12)` and its
  reflected mate `(2,27)`.

The canonical numerator and denominator of the minimum are preserved without
rounding at `gqac.minimum_prefix.exact` in `gqac_k13.json`; that field equals
the corresponding `mclp.minimum.exact`.  The full exact rows and all 648
prefixes are retained in that raw artifact.

This single finite rank neither proves `GQAC_1` nor supplies a finite trend.
No alternate grouping, replacement candidate, or other rank was tested.
