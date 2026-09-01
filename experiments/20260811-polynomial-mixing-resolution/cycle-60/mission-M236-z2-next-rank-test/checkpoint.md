# M236 checkpoint

Date: 2026-08-13 UTC

Status: initialized before substantive mission work.

- Read `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, its sampling-problem
  reference, and its experiment reference.
- Fixed the task to the complete `d=7 -> 8` one-leaf template and the exact
  finite decision rule in `plan.md`.
- The M231 formula and `Z2` gate have not yet been transcribed; the eight
  frozen source missions and coordinator-ledger entries will be verified next.
- No checker has been written and no next-rank rows have been evaluated.

## Pre-replay source lock update

- Every payload in M214/M218, M220/M223, M225/M228, and M231/M234 passes its
  frozen `SHA256SUMS` inventory. Their accepted/refuted scopes match ledger
  entries L-0278, L-0281, L-0283, and L-0286.
- `immutable_gate.md` now copies the M231 formula and fixes `Z2` without any
  next-rank endpoint inspection.
- Primary Z2 scope: all 1,296 root-leaf trees times ordinary odd edits
  `{1,3,5,7,9}`, for 6,480 rows.
- Secondary reconciliation only: internal even edits `{2,4,6,8}` and fixed
  boundary edits `{10,11}`, bringing the full endpoint table to 14,256 rows.
  These six families are not Z2 rows.
- No `d=7 -> 8` endpoint has yet been constructed or replayed.

## Final exact outcome

- The predeclared Z2 formula passes all 6,480 primary rows: 1,296 passes and
  zero failures at each edit `1,3,5,7,9`.
- There are 20 global Z2 classes/words, with per-edit class counts
  `9,6,4,3,2`; 2,974 rows are closed and 3,506 are open. Maximum finite route
  length is 21.
- The six fixed non-Z2 edit families pass all 7,776 rows. The full table passes
  14,256/14,256 and uses 22 words.
- Both first-failure fields and the first same-Z2 behavior-collision field are
  null. The result is outcome (a), a finite next-rank theorem only.
- Two consecutive runs give result-file SHA-256
  `34e7a7a76b7993595b71a588d43afe85a443d851e722bb60b6e3d5f2bc3e1585`.
