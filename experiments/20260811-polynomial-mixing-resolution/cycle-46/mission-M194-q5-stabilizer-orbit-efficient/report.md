# M194 final report: efficient Q5 stabilizer-orbit attempt

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: INCONCLUSIVE.
```

The exact streamed Schreier-orbit calculation reached its five-minute cap
before completing. It yields no new classification, route, or negative
obstruction.

## Field 2 — target and immutable input

The target is exact finite diagonal component membership for M191's 54 named
`d=5`, width-two targets in `Q_5^2`. M191's complete manifest passed with top
digest

```text
a2aeba9feb5a4bbc3f2161864cfa42ecbc0ef3a578f6a3222c1a9e07c73ab42e.
```

No probability distribution or Markov kernel is involved. No generic Magma
stabilizer was rerun.

## Field 3 — action integrity

The frozen 8,400-point action was loaded and its packed digest independently
recomputed as

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

All fourteen rows are permutations and all seven positive/negative action
pairs are mutual inverses. Source IDs are `(16,0)`.

## Field 4 — exact right-action Schreier convention

For the BFS word `t_x` from first source 16 to `x`, the implementation uses

```text
t_x g t_(xg)^(-1).
```

Chronological application sends 16 along `t_x` to `x`, along `g` to `xg`,
and back along the inverse tree word to 16. These loops generate the point
stabilizer by the standard edgewise Schreier telescoping argument. Applying
them to second source 0 therefore gives precisely the orbit needed by M191's
exact membership criterion.

## Field 5 — completed computation

A BFS transversal reached all 8,400 first-coordinate states. Every stored tree
word was replayed from source 16 to its indexed endpoint. The checker then
streamed the `8400*14` literal Schreier loops on the second coordinate,
retaining orbit-enlarging generators and repeatedly closing under retained
generators and their inverses.

## Field 6 — cap outcome

The internal deadline raised `TimeoutError` at 300 seconds during streamed
Schreier-orbit closure. The process had approximately 26 MiB RSS at the
observed status check and produced no `exact_results.json`. Time, not memory,
was the limiting resource.

No partial orbit is archived or interpreted. In particular, absence from an
unfinished orbit is not nonmembership evidence.

## Field 7 — classification status

The source stabilizer orbit remains incomplete. Consequently all memberships
beyond M188's immutable fourteen explicit positives remain unresolved. There
are no new positives and no negative orbit-ID certificates.

The first unfinished step remains exact completion of
`Orb_Stab(16)(0)` or an equivalent complete finite invariant.

## Field 8 — reproduction and hygiene

Python is `3.12.3`, dependencies `{}`, seed `null`. The capped command was

```text
python3 -B schreier_orbit_fast.py \
  --input ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json \
  --output exact_results.json --cap-seconds 300
```

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`proof.md`, `schreier_orbit.py`, `schreier_orbit_fast.py`, `cap_results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No file outside M194 was
edited.

## Field 9 — final decision

```text
FREEZE INCONCLUSIVE.
RETAIN ONLY THE EXACT METHOD, ACTION/TRANSVERSAL CHECKS, AND TIMEOUT RECORD.
DO NOT INFER ANY NEW ROUTE OR NONMEMBERSHIP.
```

No every-color, all-`d`, asymptotic route-length, gap, mixing, or Terminal
claim is made.
