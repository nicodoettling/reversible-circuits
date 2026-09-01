# M220 checkpoint

## Initialization

- Owned directory initialized before substantive work.
- The reversible-circuit-sampler workflow and current project source of truth
  are active.
- M203/M205, M208/M212, and M214/M218 are declared immutable.
- Analytic target and chronological signed-Hurwitz convention are fixed in
  `plan.md`.
- Next: verify every predecessor inventory, then derive the boundary-closure
  transport algebra before any `d=6 -> 7` computation.
- Current verdict: **inconclusive**.

## Immutable gate

- Every `SHA256SUMS` entry in M203/M205, M208/M212, and M214/M218 returned
  `OK`.
- Their top inventory digests exactly match the frozen values recorded in
  `immutable_gate.md`.
- No predecessor was edited.
- Next: analytic boundary-closure transport derivation. No finite next-rank
  checker has yet been run.

## Final checkpoint

- Analytic-first note proves three formal Hurwitz transport identities and
  declares the finite-key recurrence before the next-rank check.
- The closed recurrence reproduces all 112 M214 rows.
- Complete exact `d=6 -> 7` replay over 125 trees and nine edits gives 1,098
  passes and 27 failures, split edit 1: 11 and edit 7: 16.
- The first same-key pair has identical path `(2,1)`, `late=false`, `run=0`,
  and `exception=false`; its common 17-move word passes the star but fails the
  tree with nonconsecutive child edge `{2,5}` at positions 7 and 8.
- The two newly included edits 8 and 9 pass all 125 finite rows.
- Deterministic output hash is stable across consecutive runs.
- Final verdict: **reject the explicit finite-key recurrence; keep the exact
  obstruction, formal carrier identities, and finite survivors**.
- Next: freeze and request a fresh immutable referee. No general-rank,
  every-color, length, gap, mixing, or Terminal claim is made.
