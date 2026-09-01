# M191 halfway/final computation checkpoint

Date: 2026-08-13 UTC.

## Immutable gate and exclusions

M181, M183, and M188 pass their complete frozen manifests. M188's accepted
append-only result supplies fourteen explicit positive routes among the 54
named targets. Every stale geometric all-`d` statement in M187 is excluded.

## Exact work completed

The independent target construction gives ten rooted DPS descriptors and
exactly 54 named quotient target tuples. The exact one-coordinate quotient
action was constructed without enumerating `Q_5^2`:

```text
|Z_5| = 5^(5-3) 8! = 1,008,000,
|Q_5| = |Z_5|/5! = 8,400.
```

Starting from the first source, signed Hurwitz orbit traversal found exactly
8,400 quotient states, certifying completeness against the rooted-DPS count.
All fourteen signed generator permutations are bijections and the seven
positive/negative pairs are mutual inverses. Their packed action digest is

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae
```

The source IDs are `(16,0)` in lexicographic quotient order. The exact 54
target IDs/occurrences, full generator action, rooted descriptors, and a Magma
classification script are archived.

## Exact criterion

Fix a chronological tree word `alpha(v')` sending first source `v` to a
target first coordinate `v'`. Then

```text
(v',u') in Orb_diag(v,u)
iff
u' alpha(v')^(-1) in Orb_Stab(v)(u).
```

Both directions follow by factoring a diagonal transporter through
`alpha(v')`. This is an exact group-action theorem, not a heuristic or a
bounded search.

## Cap outcome

Magma V2.29-4 was asked to construct the point stabilizer of ID 16 in the
8,400-point action, its orbit of ID 0, and transporters/certificates for all 54
targets. It stayed in exact stabilizer/orbit construction for approximately
6 minutes 44 seconds, used about 591 MiB RSS at the last observation, and
created no certificate output. It was terminated under the coordinator's
six-minute cap.

Therefore the requested 54-target classification is **INCONCLUSIVE**. No
unclassified radius-five miss is interpreted negatively, and no broader
enumeration will be attempted.
