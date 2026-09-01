# M223 checkpoint

## Initialization

- Owned directory initialized before substantive work.
- Reversible-circuit-sampler workflow is active.
- Frozen M220 is declared immutable.
- Target, chronological convention, clean-room rule, exact expected counts,
  digest, witness, and strict scope are fixed in `plan.md`.
- Next: verify M220's complete frozen inventory and read only its
  human-readable mathematical statement.
- Current verdict: **inconclusive**.

## Immutable gate

- Every M220 payload hash returned `OK`.
- The filesystem inventory and `SHA256SUMS` inventory agree exactly.
- Top digest is
  `0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316`.
- Read M220's human-readable symbolic statement, obstruction, report, and
  freeze boundary; no checker code or result JSON has been read.
- Next: implement the decisive reconstruction from scratch. M220 remains
  immutable and the verdict remains **inconclusive**.

## Halfway checkpoint

- Standalone checker written with no M220 imports, paths, or result reads.
- Formal identities pass exhaustively on `[7]`: 840 distinct carrier labelings,
  210 distinct double-inverse labelings, and all 441 ordered transposition
  pairs for the single-inverse identity.
- Two independent Prüfer constructions agree on both finite tree sets.
- The recurrence passes all 112 rank-five rows and reproduces the rank-six
  pass counts `114,125,125,125,125,125,109,125,125`.
- The independently normalized rank-six digest equals the commissioned value.
- Current verdict: **provisional ACCEPT**, pending witness and hygiene checks.

## Final checkpoint

- Independently reconstructed first witness is exactly the star and
  `{{1,2},{1,3},{1,4},{1,6},{2,5}}`, with equal full descriptors and the same
  17-move word.
- It passes on the star and fails on the second tree exactly at positions 7
  and 8, retaining `(45)^2` instead of the required `(46)^2`.
- A post-hoc read-only comparison after the decision found exact equality of
  witness, counts, and digest with frozen M220.
- Two deterministic runs produced identical result hashes; no cache exists.
- Material objections: none. Nonmaterial objections: none.
- Final verdict: **ACCEPT M220 AS FROZEN, WITH ITS STRICT NO-GO SCOPE**.
