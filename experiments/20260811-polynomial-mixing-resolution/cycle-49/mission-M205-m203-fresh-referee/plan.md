# M205 plan: fresh immutable referee of M203

## Objective

Independently audit frozen M203's bounded d=5,6 structural obstruction.  The
audit is restricted to the targeted rooted DPS rows, literal six-factor
locality, d=6 active-block/filler cross-coupling, and the fourteen d5-to-d6
leaf-stabilization comparisons.

## Immutable input

`../mission-M203-all-d-matching-route-structural/` is read-only.  Before any
substantive conclusion, verify every entry in its `SHA256SUMS` and record the
digest of that inventory.

## Independent checks

1. Reconstruct the explicit M181 width-two words at d=5 and d=6.
2. Reconstruct rooted DPS inverse witnesses and all adjacent edits for every
   pattern and root: 70 d=5 rows and 108 d=6 rows.
3. Recompute changed-factor positions, literal adjacent locality, literal
   six-factor-region locality, and the two directed d=6 cross-coupling counts.
4. Recompute the fourteen distinguished-root d5/d6 leaf-stabilization class
   comparisons and the first unequal canonical digests.
5. Compare the independently produced data with frozen M203 artifacts only
   after reconstruction.

## Bounds and exclusions

- Exact finite d=5,6 symbolic work only; no Q6 quotient enumeration.
- No inference about d=6 reachability, all-d routing, corrected route length,
  spectral gap, mixing, or Terminal.
- The strongest possible accepted conclusion is only that the naive proof by
  independent d5 blocks with fixed filler is invalid.

## Deliverables

`checkpoint.md`, `immutable_gate.md`, a compact clean-room checker and JSON
result, a nine-field `report.md` with numbered objections and an exact verdict,
then a manifest and `SHA256SUMS` freeze.

