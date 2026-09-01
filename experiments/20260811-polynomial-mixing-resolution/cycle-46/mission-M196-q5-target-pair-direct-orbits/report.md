# M196 final report: exact target-directed Q5 pair classification

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: ACCEPT.
```

All 54 named `d=5`, width-two target pairs are exactly certified positive in
the diagonal `Q_5^2` action. The verdict covers only this finite target list.

## Field 2 — target and convention

The source is `(16,0)` in M191's frozen 8,400-point `Q_5` action. Signed
Hurwitz symbols `1,...,7,-1,...,-7` act chronologically on the right and act
diagonally on the pair. No probability distribution or Markov kernel is
involved.

## Field 3 — immutable gate

M191 and M194 passed their full frozen manifests, with respective top digests

```text
a2aeba9feb5a4bbc3f2161864cfa42ecbc0ef3a578f6a3222c1a9e07c73ab42e
f51442fac7e1ebd5dc9f62dd2803d7ecd3863f10e5205927fd51e50ade4e4830.
```

The packed action digest independently recomputes to
`160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae`.
Neither immutable predecessor was edited.

## Field 4 — exact reduction

The rebuilt first-coordinate BFS transversal reaches all 8,400 states, has
maximum depth 13, and every stored tree word replays. For each target
`(v_j,u_j)`, its tree word `alpha_j` gives the adjusted second ID
`z_j=u_j^(alpha_j^(-1))`. The 54 rows deduplicate to exactly 41 adjusted IDs.

## Field 5 — target-directed result

A complete radius-eight forward product ball contains 154,393 states, with
level sizes `1,6,40,190,795,2976,10416,34256,105713`. Fifteen adjusted targets
are direct hits. Target-directed backward searches give meeting certificates
for the remaining 26. Thus all 41 adjusted targets, and hence all 54 original
targets, are positive. The run took 0.5166 seconds, well below the five-minute
cap. It made zero negative claims.

## Field 6 — explicit certificates and replay

For each adjusted ID, `targeted_results.json` stores the forward word, backward
word, signed inverse composition, meeting state, and stabilizer word. For each
of the 54 original target IDs it explicitly stores the stabilizer word, tree
word, concatenated full word, and endpoint.

An independent checker reloads the frozen action and certificate JSON. It
passes 41 meeting decompositions, 41 stabilizer pair replays, 54 adjustment
relations, the exact 54-ID inventory, and 54 full pair replays. The result-file
digest it records is
`e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2`.

## Field 7 — exact finite theorem and lengths

For every named target `(v_j,u_j)`, the archived chronological word `w_j`
satisfies `(16,0)^w_j=(v_j,u_j)`. Maximum segment lengths are forward 8,
backward 7, stabilizer 15, and named-target tree word 9. The maximum complete
endpoint-word length is 22. These are exact finite `d=5` witness lengths only,
not an asymptotic or polynomial route-length bound.

## Field 8 — reproduction and hygiene

Python is 3.12.3, dependencies `{}`, and seed `null`. Commands were

```text
python3 -B dedup_targets.py --input ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json --output adjusted_targets.json
python3 -B targeted_pair_mitm.py --action ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json --adjusted adjusted_targets.json --output targeted_results.json --forward-depth 8 --backward-depth 8 --seconds 285 --max-backward-visited 300000
python3 -B verify_certificates.py --action ../../cycle-45/mission-M191-d5-synchronized-route-classification/q5_action.json --results targeted_results.json --output verification.json
```

All writes are confined to M196. The checker did not compute the full
stabilizer orbit, call Magma, or enumerate `Q_5^2`.

## Field 9 — final scope and audit request

```text
ACCEPT: ALL 54 NAMED TARGETS HAVE EXACT POSITIVE WORD CERTIFICATES.
NO NEGATIVE, EVERY-COLOR, ALL-d, POLYNOMIAL-LENGTH, GAP, MIXING, OR TERMINAL CLAIM.
```

Freeze this payload and commission a fresh immutable referee to replay the
deduplication, signed meet-in-the-middle convention, target inventory, and all
54 explicit endpoint words.
