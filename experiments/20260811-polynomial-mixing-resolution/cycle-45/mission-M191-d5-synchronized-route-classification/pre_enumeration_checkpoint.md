# M191 pre-enumeration checkpoint

Date: 2026-08-13 UTC.

Status: immutable gate and exact membership formulation complete.

- M181, M183, and M188 manifests pass completely, with top digests
  `d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0`,
  `ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46`,
  and `5fc669b87d3b7ae44977d08f53e18397ec064e920c322a93644057b0561d4cd8`.
- All stale geometric all-`d` statements in M187 are excluded.
- The ten rooted DPS descriptors independently reconstruct exactly 54 named
  target quotient tuples.
- Exact criterion: choose a Schreier-tree word `alpha(v')` from the first
  source `v` to a target first coordinate `v'`. Then `(v',u')` is in the
  diagonal component of `(v,u)` iff applying `alpha(v')^{-1}` to `u'` lies
  in the orbit of `u` under the action stabilizer of `v`.
- Proof: if a diagonal word `b` sends `(v,u)` to `(v',u')`, then
  `b alpha(v')^{-1}` stabilizes `v` and sends `u` to
  `u' alpha(v')^{-1}`. Conversely, prepend any stabilizer word realizing that
  adjusted second coordinate to `alpha(v')`. Chronological right-action order
  is used throughout.
- This is an exact group-action equivalence, not a generated-subgroup/class
  heuristic.

Next action is capped at one exact `Q_5` enumeration, its source Schreier tree,
and the stabilizer orbit on the second coordinate. No Cartesian quotient,
radius-limited negative search, or broad all-`d` computation will be run.
