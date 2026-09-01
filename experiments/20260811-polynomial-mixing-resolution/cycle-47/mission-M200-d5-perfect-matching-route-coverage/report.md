# M200 final report: d=5 perfect-matching route coverage

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: PROMOTE THE EXACT FINITE d=5 THEOREM.
```

For every adjacent DPS edit and every M135 perfect-matching color at `d=5`,
M181's selected width-two full-voltage source pair has a synchronized quotient
route to its matched DPS target pair. There are no uncovered color/root-pair
classes.

## Field 2 — immutable provenance

Every payload entry in M135/M137, M181/M183, and M196/M198 passed its frozen
manifest. Top digests are

```text
M135  8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358
M137  47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5
M181  d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0
M183  ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46
M196  7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913
M198  1142912065699b883268b16aee8707b1c1e0d7c4b006eb1ca9bb02282ef9bd84.
```

No predecessor was edited.

## Field 3 — target, convention, and source

The exact finite target is diagonal signed-Hurwitz component membership in
the 8,400-state `Q_5^2` action. Symbols act chronologically on the right. The
source IDs are `(16,0)`, corresponding in order to M181 patterns `[[0],[1]]`.
M181's voltage representative is `[0,1]`, a basis of one-dimensional `W_2`;
thus every color's selected two-edge source subfamily has `V_stab=W_2`.

There is no probability distribution or Markov kernel in this theorem.

## Field 4 — exact incidence table

The checker builds the complete invariant incidence inventory:

```text
7 edits * 2 left source orbits * 5 H-orbit roots = 70 root-edge rows,
7 edits * 5 roots * 5 roots                 = 175 root-pair rows.
```

Every root pair occurs exactly once in the occurrence metadata of M196's 54
deduplicated target classes. Coordinate targets are independent of the other
coordinate's root, and all target pairs have distinct two coordinates. The
full numeric root-edge table is in `incidence_summary.md`; all 175 target IDs,
route references, and certificate digests are in `incidence_table.json`.

## Field 5 — exhaustive color quantifier

M135 freezes no particular numerical `d=5` coloring. Its theorem permits any
perfect-matching decomposition, so numeric color-to-root assignments are
noncanonical. For any actual color `M`, perfectness selects exactly one of the
five `H`-orbit edges over each of the two M181 left source vertices, hence a
unique pair `(r_0(M),r_1(M))` among the 25 rows for that edit.

This is a simultaneous pair incidence. All 25 possibilities per edit—not
merely the 70 individual coordinate edges—have M196 diagonal route
certificates. Therefore every actual color is covered independently of which
edge coloring was chosen.

## Field 6 — exact route certificates

All 54 M196 full words were reloaded and directly replayed on both coordinates
of the frozen action. They cover all 175 root-pair occurrences:

```text
covered incidences:      175 / 175
distinct target classes: 54
uncovered classes:        0.
```

The packed action digest is
`160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae`;
the M196 result digest is
`e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2`.

## Field 7 — endpoint consequence and length boundary

M196's simultaneous quotient route discharges M181's conditional component
hypothesis for every `d=5` color. Since the source has
`V_stab=W_2`, M175's affine theorem qualitatively supplies a
zero-relative-voltage route to each fixed pair of physical DPS endpoints.

The stored M196 word of length at most 22 certifies only the quotient route.
It is not asserted to have zero voltage. No length is assigned to the added
source-stabilizer correction or the total corrected route, so no polynomial
route-length statement is made.

## Field 8 — reproduction and hygiene

Python is 3.12.3, dependencies `{}`, seed `null`. The exact command was

```text
python3 -B coverage_audit.py \
  --m181-results ../../cycle-42/mission-M181-matching-schreier-chord-rank/results.json \
  --m196-adjusted ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/adjusted_targets.json \
  --m196-results ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/targeted_results.json \
  --m198-results ../mission-M198-m196-fresh-referee/referee_results.json \
  --q5-action ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json \
  --output incidence_table.json
```

The script uses only the standard library, directly replays every route word,
and performs no broad quotient or matching enumeration. All writes are
confined to M200.

## Field 9 — accepted boundary and audit request

```text
PROVED: EVERY d=5 M135 COLOR HAS M181'S FULL-VOLTAGE WIDTH-TWO SOURCE PAIR.
PROVED: ITS MATCHED DPS QUOTIENT TARGET PAIR IS SYNCHRONOUSLY REACHABLE.
PROVED QUALITATIVELY: ZERO-VOLTAGE FIXED-ENDPOINT ROUTING EXISTS.
```

No arbitrary-subfamily, all-`d`, quantitative corrected-route, polynomial
length, gap, mixing, or Terminal conclusion follows. Freeze this package and
request a fresh immutable referee to audit the noncanonical-color quantifier,
the 70/175 incidence completeness, simultaneous pair lookup, and the
quotient-word versus voltage-corrected-route distinction.
