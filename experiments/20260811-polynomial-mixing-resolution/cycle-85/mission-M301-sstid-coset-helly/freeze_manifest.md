# M301 freeze manifest

Date: 2026-08-14 UTC.

## Frozen verdict

```text
PROMOTE: exact common-class/action-cover identity and residual-agreement-
         density equivalence.
REFUTED at d=3: hereditary 2-Helly on actual subfamilies contained in one
                M135 perfect matching.
OPEN: complete-matching MT2H, MRAD at d>=6, short literal representatives,
      and SSTID.
```

## Frozen exact content

- The generic coset property alone has no 2-Helly theorem.
- The actual `d=3,i=1` matching subfamily `[0,2,9]` has three singleton
  pair intersections with distinct actions and empty triple intersection.
- All complete rank-three perfect matchings have an incompatible pair, so
  the registered complete-matching MT2H candidate is not refuted there.
- Higher-arity common classes are exactly covers by finite-action agreement
  hyperedges.
- Polynomial action-cover number is polynomially equivalent, up to
  `O(d log d)`, to inverse-polynomial residual agreement density on every
  matching subfamily.
- Under finite-action transitivity, a uniformly averaged action agrees with
  exactly `1/d!` matching edges on average.  This is not a maximum bound.

## Frozen boundary

The exact witness is finite rank three and does not lift to `d>=6`.  MRAD,
polynomial literal stabilizer representatives, SSTID, every-color routing,
voltage, congestion, every spectral gap, mixing, and Terminal remain open.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `mt2h_d3_diagnostic.py`
- `results.json`
- `coset_helly_obstruction.md`
- `report.md`
- `audit_request.md`
- this `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest, inventories every payload
above, and excludes itself.
