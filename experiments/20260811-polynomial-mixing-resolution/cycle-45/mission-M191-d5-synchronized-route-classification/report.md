# M191 final report: exact d=5 classification attempt

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: INCONCLUSIVE.
```

The exact finite 54-target classification did not finish within the imposed
six-minute stabilizer-computation cap. A complete one-coordinate `Q_5` action
and an exact stabilizer-orbit criterion are preserved. M188's fourteen
explicit positive routes remain accepted; no additional positive or negative
target is claimed.

```text
candidate                  | exact stabilizer-orbit classification
claimed target             | 54 named d=5 width-two quotient tuples
identity ok                | target reconstruction checks pass
crosses Hurwitz components | 14 accepted positives only
exact diagnostics          | complete 8400-point Q5 action; capped stabilizer
verdict                    | inconclusive classification
```

## Field 2 — target and immutable inputs

The exact target is diagonal signed-Hurwitz component membership in `Q_5^2`
for the fixed source pair and 54 named targets. Permutations compose as
`(p q)(x)=p(q(x))`; braid symbols act chronologically on the right.

M181, M183, and M188 pass their complete manifests, with top digests

```text
d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0
ddd2bf1d2ce8d22e2228624d8802b38a527fee27819b92f9f06c3393b567fa46
5fc669b87d3b7ae44977d08f53e18397ec064e920c322a93644057b0561d4cd8
```

respectively. Every superseded geometric all-`d` claim in M187 is excluded.
This mission is a clean replacement, not an amendment.

## Field 3 — exact membership theorem

Fix a word `alpha(v')` sending first source `v` to target first coordinate
`v'`. Proposition 2.1 proves

```text
(v',u') reachable diagonally from (v,u)
iff
u'^(alpha(v')^-1) lies in Orb_Stab(v)(u).
```

The forward direction factors any diagonal transporter through `alpha^-1`;
the converse appends `alpha` to a stabilizer transporter. This is exact in
both directions and independent of the chosen first-coordinate tree word.
It uses no generated-subgroup/class heuristic.

## Field 4 — complete `Q_5` action

The rooted DPS count gives

```text
|Z_5|=5^(5-3)8!=1,008,000,     |Q_5|=|Z_5|/5!=8,400.
```

Independent signed-Hurwitz traversal from the first source finds exactly
8,400 quotient states, proving complete coverage against that count. All
fourteen signed generator actions are bijections and all seven signed pairs
are mutual inverses. The packed action digest is

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

Source IDs are `(16,0)` in lexicographic order. This enumerates only the one
coordinate quotient, not `Q_5^2`.

## Field 5 — target reconstruction

The checker independently reconstructs the two named source words under all
five distinguished roots and all seven adjacent DPS value edits. The ten
rooted descriptors yield exactly 54 distinct eligible ordered quotient
targets, and their IDs/occurrences are archived in `q5_action.json`.

This agrees with immutable M188's independently audited 54-target set. M188's
fourteen explicit positive paths remain valid input. The other forty bounded
radius-five misses remain undecided.

## Field 6 — capped exact stabilizer computation

`classify_q5.m` constructs the exact permutation group on 8,400 points, then
requests `Stabilizer(G,v)`, its orbit on `u`, and action-word transporters for
all targets. Magma V2.29-4 remained in exact stabilizer/orbit construction for
approximately 6 minutes 44 seconds and used about 591 MiB RSS at the last
observation. It created no classification output and was terminated under the
coordinator's six-minute cap.

Therefore no stabilizer orbit size, new route, or negative orbit obstruction
is reported. The aborted run is a resource outcome, not mathematical evidence.

## Field 7 — exact retained artifacts and first unfinished step

The retained exact artifacts are:

- the full fourteen-generator `Q_5` action;
- its 8,400-state completeness certificate and action digest;
- all 54 target IDs and root/edit occurrences;
- the exact reduction theorem;
- a ready Magma script designed to output stabilizer generators, the complete
  orbit set, and explicit positive action words.

The first unfinished step is exactly: compute the point stabilizer orbit
`Orb_Stab(v)(u)` with independently checkable words or an equivalent complete
finite invariant. No broader search is needed.

## Field 8 — reproduction and hygiene

Python is `3.12.3`, Magma is `V2.29-4`, dependencies are otherwise `{}`, and
the deterministic seed is `191` for the Magma script. Commands:

```text
python3 -B exact_classifier.py --gate-only
python3 -B export_q5_action.py --json q5_action.json --magma classify_q5.m
magma -n classify_q5.m
```

The third command was capped and did not complete. Owned artifacts are
`plan.md`, `checkpoint.md`, `pre_enumeration_checkpoint.md`,
`halfway_checkpoint.md`, `proof.md`, `exact_classifier.py`,
`export_q5_action.py`, `q5_action.json`, `classify_q5.m`, `cap_results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No predecessor or file
outside M191 is edited.

## Field 9 — final decision

```text
INCONCLUSIVE ON THE REQUESTED 54-TARGET CLASSIFICATION.
KEEP THE EXACT Q5 ACTION AND STABILIZER-ORBIT REDUCTION.
KEEP ONLY M188'S FOURTEEN POSITIVE ROUTES.
MAKE NO NEGATIVE MEMBERSHIP CLAIM.
```

No all-`d` theorem, every-color inference, asymptotic route length, spectral
gap, mixing, or Terminal conclusion is made.
