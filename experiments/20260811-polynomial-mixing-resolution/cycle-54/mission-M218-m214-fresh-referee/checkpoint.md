# M218 checkpoint

## Initial checkpoint

- Mission directory initialized before substantive work.
- The reversible-circuit-sampler skill was read in full.
- Next: read the mandated source lock, verify frozen M214 hashes, and design a
  standalone reconstruction that imports no M214 code or data.
- Current verdict: **inconclusive**.

## Source-lock checkpoint

- Read `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, its sampling and
  experiment references, and the relevant graph/theory manuscript sections.
- Frozen M214 `SHA256SUMS` has digest
  `cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f`.
- Its inventory names exactly eleven payload files besides `SHA256SUMS`; an
  independent filesystem listing has exactly those eleven files, and
  `sha256sum -c SHA256SUMS` returned `OK` for every entry.
- Read only M214's human-readable mathematical specification. The decisive
  checker will neither import nor parse M214 code or result data.
- Next: implement the rooted closure, descriptor, schedule table, and all 112
  endpoint replays from the stated definitions.
- Current verdict: **inconclusive**.

## Halfway checkpoint

- A standalone checker, importing and reading no M214 code or result data,
  independently generated the 16-tree set in two ways and proved the sets
  equal.
- It derived all descriptors before endpoint comparison and replayed all 112
  chronological signed-Hurwitz words literally. Every endpoint and identity
  check passed; the independently recovered class counts are exactly
  `5/2/1/8`, `16`, `7/4/5`, `16`, `1/15`, `16`, `16`.
- The first run used an intentionally independent verbose JSON schema, so its
  digests were not expected to equal M214's schema-specific published
  digests. The mathematical endpoint decision was fixed before inspecting
  frozen serialization fields.
- Current verdict: **provisional ACCEPT**, pending published-digest replay and
  hygiene.

## Final checkpoint

- A serialization-only pass regenerated M214's normalized fields without
  reading them in the checker. Exact digests are
  `96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b`
  and
  `0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0`.
- A separate post-hoc comparison found both normalized rows and normalized
  class summaries exactly equal to frozen M214.
- Two deterministic runs produced the same `referee_results.json` hash.
- Material objections: none. Nonmaterial objections: none.
- Final verdict: **ACCEPT M214 AS FROZEN, ONLY IN ITS DECLARED FINITE SCOPE**.
