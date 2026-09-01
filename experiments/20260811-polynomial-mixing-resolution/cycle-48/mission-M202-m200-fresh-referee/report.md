# M202 final report: fresh immutable referee of M200

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and objections

```text
FINAL VERDICT: ACCEPT M200.
NUMBERED MATERIAL OBJECTIONS: NONE.
```

M200's exact finite `d=5` perfect-matching coverage theorem is correct at its
stated qualitative endpoint scope.

## Field 2 — immutable gate

Every one of M200's ten frozen payload files passed `sha256sum -c` before any
conclusion was accepted. Its manifest digest is

```text
6561e28aa199fc1d463881f399f116bd3c05222d6d26e9f54992ff1b542f2045.
```

M200 was never edited.

## Field 3 — exact target and convention

The finite target is diagonal signed-Hurwitz component membership for M181's
width-two source under each adjacent DPS edit and arbitrary M135 matching
color at `d=5`. Symbols act chronologically on the right. There is no
probability distribution or Markov kernel in this structural audit.

## Field 4 — clean-room quotient and DPS reconstruction

Without importing M200 code, the checker rebuilt 8,400 `Q_5` states, the
fourteen exact generator rows and source IDs `(16,0)`. It independently
recovered ten rooted DPS descriptors, then all seven edits of five roots in
two coordinates. The result is exactly 70 coordinate root-edge rows and 175
simultaneous root-pair rows, deduplicated into exactly the same 54 target
classes and occurrence lists as the frozen data.

## Field 5 — arbitrary-color quantifier

Each relevant global source orbit has exactly five `H`-orbit edges. Any
perfect-matching color selects one over each of M181's two source vertices,
hence one of the 25 root pairs for that edit. The checker verifies all 25
simultaneous pairs, not merely each coordinate separately.

M135 freezes no numerical `d=5` coloring. After labeling colors by their roots
over the first source, their second-source roots form a permutation; M200's
35 normalized edit/color rows correctly cover every possible value. Thus no
hidden choice of coloring is assumed.

## Field 6 — route certificates and exact coverage

All 54 M196 quotient words directly replay to the independently reconstructed
paired targets. Their 54 occurrence classes cover all 175 incidences:

```text
covered 175 / 175 | uncovered 0 | maximum quotient-word length 22.
```

The packed action digest is
`160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae`;
the M196 result digest is
`e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2`;
the M200 incidence digest is
`48b37502a45be316efe39728cee5cb3125c4cc3196b547cf3e90c923e87187f1`.

## Field 7 — full voltage and endpoint scope

M181's exact source patterns are `[[0],[1]]`, with voltage representative
`[0,1]`, a basis of one-dimensional `W_2`. Hence each selected source pair
has `V_stab=W_2`. M196 supplies the needed synchronized quotient route, so
M175's affine criterion qualitatively supplies a zero-relative-voltage route
to the fixed physical DPS endpoints.

The stored word of length at most 22 is only the quotient certificate; it is
not asserted to have zero voltage. No length is known or claimed for the
stabilizer correction or corrected total route.

## Field 8 — reproduction and hygiene

Python is 3.12.3, dependencies `{}`, seed `null`. The command was

```text
python3 -B fresh_coverage_referee.py \
  --q5-action ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json \
  --m181-results ../../cycle-42/mission-M181-matching-schreier-chord-rank/results.json \
  --m196-results ../../cycle-46/mission-M196-q5-target-pair-direct-orbits/targeted_results.json \
  --m200-table ../../cycle-47/mission-M200-d5-perfect-matching-route-coverage/incidence_table.json \
  --output referee_results.json
```

It completed in 3.53 seconds. All writes are confined to M202; no full
`Q_5^2` or stabilizer-orbit enumeration was performed.

## Field 9 — final accepted boundary

```text
ACCEPT: EVERY d=5 M135 COLOR HAS THE ROUTED M181 FULL-VOLTAGE WIDTH-TWO PAIR.
ACCEPT QUALITATIVELY: ZERO-VOLTAGE FIXED-ENDPOINT ROUTING EXISTS.
```

No all-`d`, arbitrary-subfamily, corrected-route length, polynomial length,
gap, mixing, or Terminal inference follows.
