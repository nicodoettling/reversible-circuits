# M212 substantive checkpoint

Date: 2026-08-13 UTC.

## Immutable gate

- All twelve M208 payloads returned `OK`.
- M208 inventory digest:
  `cda9c3aba4aa058d39576f1656f3ba4158be736684dad4dd64d3c61738a657b8`.
- M196/M198 and M200/M202 accepted dependency inventories also returned
  `OK`. No predecessor was edited.

## Clean-room result

The independent checker imports no M208 code. It reconstructs the DPS closure,
the two named trees, `pi_5`, their one-leaf extensions and `pi_6`, then
replays the seven correction words on both patterns.

- Exact route lengths: `13,0,9,0,5,2,1`.
- All fourteen literal endpoint replays pass.
- Independent certificate digest:
  `0bcfdab81369a4fca73367bee84169dd313c698b42685b8053dae2e764ef4223`,
  equal to frozen M208.
- All 16 root-5-leaf-at-1 Cayley trees give 112 deterministic checks.
- Reproduced known-word failures: 21, split `1:11, 3:9, 5:1`.
- The first failure is exactly frozen tree index 2,
  `{{1,2},{1,3},{1,5},{3,4}}`, edit 3, with identical naive, route-output,
  and actual words.

## Composition audit

All seven stored M196 words reach the required d5 quotient classes. On the
distinguished physical representatives they literally reach the fixed target
pair for edits `1,2,4,6`, so the stored word followed by M208's correction
replays directly. For edits `3,5,7`, the stored quotient word reaches only a
globally relabeled target pair; the accepted M200/M202 application of M175's
full-voltage affine theorem is required to obtain an exact physical d5 braid.
Once such a braid exists, embedding it on positions 1 through 8 leaves the
new square fixed, and appending `C_i` is formally valid.

M208 already preserves this distinction by claiming no voltage-corrected or
total route length. Provisional verdict: **ACCEPT**, no objections.

