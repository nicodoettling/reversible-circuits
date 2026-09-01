# M183 plan: fresh immutable referee of M181

## Objective

Independently referee frozen M181 at its exact narrow scope: an explicit
accepted-matching source family with full relative-orientation Schreier chord
rank.  Verify immutable provenance first, then audit every material proof
interface without modifying M181.

## Target and conventions

The target is qualitative diagonal signed-Hurwitz orbit lifting for connected
product-one transposition words of minimal length `2d-2`, modulo simultaneous
global relabeling.  The voltage group is
`W_s=F_2^s/<(1,...,1)>`.  Permutations compose as
`(p q)(x)=p(q(x))`; signed braid words are applied chronologically.

No probability distribution, sampler kernel, quotient-connectivity theorem,
word-length theorem, spectral gap, mixing bound, or Terminal claim is in
scope.

## Immutable gate

1. Verify M181's complete `SHA256SUMS` and its top-level digest.
2. Read every frozen M181 payload file only after the hash gate passes.
3. Report the exact payload hashes and never edit M181.

## Independent audit

1. Reconstruct the six-factor core and independently replay the 200-move
   relation, including the reverse elementary-conjugation convention.
2. Check the all-label construction symbolically and at a few boundary ranks:
   identity, connectedness, exact length `2d-2`, and literal filler fixation.
3. Audit pairwise nonconjugacy of the selected binary patterns.
4. Audit the single-coordinate voltage basis modulo `Delta`, including even
   tuple width and the edge-vector parity warning.
5. Audit inclusion in every M135 perfect-matching color: one `H`-orbit edge
   per left `G`-orbit and coordinatewise arbitrary `G`-conjugation.
6. Check that endpoint membership is claimed only conditional on a quotient
   route, and that the M169 exact-sequence conclusion is scoped correctly.

## Computation cap and verdict

Use a clean-room standard-library script with no M181 import and no quotient
enumeration.  Replay only the core relation and a few boundary embeddings.
Write numbered objections, a nine-field report, compact results, freeze
manifest, exact hashes, hygiene, and an explicit `ACCEPT` or `REJECT`.

