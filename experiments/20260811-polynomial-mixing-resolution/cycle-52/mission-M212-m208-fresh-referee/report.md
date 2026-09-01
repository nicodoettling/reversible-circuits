# M212 final report: fresh immutable referee of M208

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — exact verdict

```text
ACCEPT M208 AS FROZEN.
```

The finite named-pattern correction theorem, its qualitative composition with
accepted fixed-endpoint d5 routing, and the limited universality falsification
all survive an independent reconstruction. General rooted recursion remains
unresolved exactly as M208 states.

## Field 2 — immutable provenance and payload hashes

Before substantive comparison, every M208 entry returned `OK`. Exact payload
hashes are recorded in `immutable_gate.md`; the M208 `SHA256SUMS` digest is

```text
cda9c3aba4aa058d39576f1656f3ba4158be736684dad4dd64d3c61738a657b8.
```

Accepted dependencies M196/M198 and M200/M202 also passed their complete
inventories, with top digests

```text
M196 7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913
M198 1142912065699b883268b16aee8707b1c1e0d7c4b006eb1ca9bb02282ef9bd84
M200 6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045
M202 33f34abf2f6d763b61fd15e6f64c895249792e70dab933894242584886491f70.
```

No predecessor was edited.

## Field 3 — target, convention, and clean method

There is no probability distribution or Markov kernel in this mission. The
audited target is exact synchronized signed-Hurwitz endpoint realization.
Actions are chronological under

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

`fresh_rooted_referee.py` implements the DPS boundary closure and Hurwitz
action independently. It imports no M208 code, completes its reconstruction
before reading frozen M208 JSON, and never enumerates `Q_6` or searches for a
route.

## Field 4 — descriptor-extension reconstruction

The checker reconstructs the named trees

```text
T_0={{1,2},{1,3},{1,5},{2,4}},
T_1={{1,2},{1,3},{1,4},{1,5}}
```

with `pi_5=(7,8|1,2|3,4|5,6)`. Adding `{1,6}` and using
`pi_6=(9,10|1,2|3,4|5,6|7,8)` gives the literal original source followed by
`(05)^2` for both patterns. All source and target products evaluate to
identity.

## Field 5 — seven corrections and digest

All seven displayed correction words replay on both named patterns. The exact
length vector is

```text
13, 0, 9, 0, 5, 2, 1,
```

and all fourteen literal endpoint comparisons pass. The independently encoded
certificate digest is

```text
0bcfdab81369a4fca73367bee84169dd313c698b42685b8053dae2e764ef4223,
```

equal to frozen M208. Descriptor rows, certificate rows, and the maximum
correction length 13 also match field-for-field.

## Field 6 — d5 route composition audit

All seven accepted M196 words for distinguished roots `[4,4]` reach the two
required d5 quotient classes. The stored words themselves reach the fixed
physical target pair for edits `1,2,4,6`, and their literal embedding followed
by `C_i` replays to the d6 endpoint.

For edits `3,5,7`, the stored M196 word reaches only a globally relabeled
target. Here composition relies on the accepted M200/M202 use of M181 full
voltage and M175's affine criterion to supply an exact fixed-endpoint d5 braid.
Embedding any such braid in positions 1 through 8 leaves `(05)^2` fixed, after
which `C_i` applies. M208 correctly claims no length for that voltage-corrected
d5 braid or the composite.

## Field 7 — 16-tree falsifier and numbered objections

The independent Prüfer traversal finds exactly 16 trees with old root 5 a leaf
at vertex 1. Applying the known table to all 112 tree/edit rows gives exactly
21 failures:

```text
edit 1: 11,       edit 3: 9,       edit 5: 1.
```

The first is frozen tree index 2,
`{{1,2},{1,3},{1,5},{3,4}}`, edit 3. Every displayed factor in its naive
target, route output, and actual target matches M208.

Numbered objections:

1. None. M208 explicitly limits this failure to the archived schedule table
   and does not infer that an alternative correction route is impossible.

## Field 8 — reproduction and hygiene

Environment: Python 3.12.3; nonstandard dependencies `{}`; seed `null`.
Command:

```text
timeout 120s python3 -B fresh_rooted_referee.py
```

The checker archives exact descriptors, fourteen replays, the full first
failure, frozen-field comparisons, and the seven d5 composition rows in
`referee_results.json`. All writes are confined to M212. No route search,
Q6 enumeration, cache, or external dependency is used.

## Field 9 — accepted scope and disposition

```text
ACCEPT: finite correction for the two named M181 patterns at d5->d6 and old
edits 1..7; qualitative distinguished fixed-endpoint route composition.

ACCEPT AS A FALSIFIER ONLY: the seven-word table is not universal on the
declared 16-tree template.

DO NOT INFER: general d6 routing, edits 8,9, every color, arbitrary
representatives without the accepted affine dependency, all-d routing,
voltage-corrected length, polynomial length, gap, mixing, or Terminal.
```

Freeze M212 and return its hashes for coordinator synthesis.

