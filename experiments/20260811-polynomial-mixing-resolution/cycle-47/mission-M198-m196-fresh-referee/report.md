# M198 final report: fresh immutable referee of M196

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT.
NUMBERED OBJECTIONS: NONE.
```

M196 correctly gives exact positive certificates for all 54 named `d=5`,
width-two diagonal `Q_5` targets.

## Field 2 — immutable gate

Before accepting any conclusion, all thirteen entries in M196's
`SHA256SUMS` returned `OK`. Its checksum-file digest is

```text
7fa987c6c776e55990c00fcfaea85e34c1d7b0e6d3f97d57fdefba8bcb5bd913.
```

M196 was never edited.

## Field 3 — exact target and convention

The target is component membership for the 54 named pairs from source
`(16,0)` under the diagonal action of M191's 8,400-state `Q_5`. Symbols
`1,...,7,-1,...,-7` act chronologically on the right. There is no probability
distribution or Markov kernel in this finite structural audit.

## Field 4 — clean-room action/transversal audit

Without importing predecessor code, the referee rebuilt all 8,400 canonical
connected identity states, all fourteen action rows, and the source IDs. Every
row exactly matches the frozen action, every row is bijective, and all seven
signed pairs are mutual inverses. The independently rebuilt chronological
transversal has size 8,400 and maximum depth 13; every tree word replays.

The packed action digest is
`160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae`;
the frozen `q5_action.json` file digest is
`d24bfdf3d7c21c1bc4a4313fa83217e766a3e4186e8b1b2b2340f5dc1d8f043c`.

## Field 5 — named-target and adjustment audit

The referee independently rebuilt ten rooted DPS descriptors, all 175
edit/root occurrences, and their exact partition into 54 sorted target rows.
All IDs and occurrence metadata match the frozen action file. Applying each
inverse first-coordinate tree word produces exactly 41 distinct adjusted
second IDs, with all M196 rows and classes matching.

## Field 6 — MITM and endpoint replay

The independent radius-eight forward product ball has 154,393 states and
levels `1,6,40,190,795,2976,10416,34256,105713`, exactly as reported. For all
41 adjusted certificates, both paths reach the stored meeting, the
chronological word is exactly `f reverse_and_negate(b)`, and it fixes first ID
16 while mapping second ID 0 to the adjusted ID. The split is 15 direct and 26
nonempty-backward certificates.

For all 54 original targets, the referee recomputed the adjustment equation,
checked `full_word=stabilizer_word+tree_word`, and replayed the exact endpoint
on both coordinates. All 54 pass.

## Field 7 — counts, lengths, digests, and objections

The stated maximum lengths reproduce exactly:

```text
forward 8 | backward 7 | stabilizer 15 | named tree 9 | full word 22.
```

The frozen result digest is
`e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2`.

Numbered objections: none.

## Field 8 — reproducibility and hygiene

Python is 3.12.3, dependencies `{}`, seed `null`. The command was

```text
python3 -B fresh_referee.py \
  --q5-action ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json \
  --adjusted ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/adjusted_targets.json \
  --results ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/targeted_results.json \
  --prior-verification ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/verification.json \
  --output referee_results.json
```

It completed in 3.80 seconds. It built only one 8,400-state quotient and one
radius-eight product ball; it did not compute a full stabilizer orbit or
enumerate `Q_5^2`. All writes are confined to M198.

## Field 9 — exact accepted boundary

```text
ACCEPT M196'S EXACT POSITIVE CLASSIFICATION OF THE 54 NAMED d=5 WIDTH-TWO TARGETS.
NO EVERY-COLOR, ALL-d, POLYNOMIAL-LENGTH, GAP, MIXING, OR TERMINAL INFERENCE.
```

The maximum length 22 is only an exact fact about this finite archived witness
set.
