# M309 run manifest

Date: 2026-08-14 UTC.

## Role and ownership

- Role: fresh immutable referee for frozen M306.
- Owned path: `cycle-90/mission-M309-m306-fresh-referee/` only.
- Predecessor and coordinator artifacts edited: none.

## Checks

- Verified M306 `SHA256SUMS` top digest and all nine payload rows.
- Verified the top digests and every payload row of M296, M299, M301, and
  M304.
- Re-derived RCOM, the fractional-cover dual, both harmonic implications,
  and the `Sym/Alt` obstruction from definitions.
- Replayed exactly one no-import finite checker for the `d=3` boundary.

## Exact finite command

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-87/mission-M304-m301-fresh-referee/independent_d3_check.py
```

The replay is exhaustive and deterministic; it uses no randomness and no
nonstandard dependency.

