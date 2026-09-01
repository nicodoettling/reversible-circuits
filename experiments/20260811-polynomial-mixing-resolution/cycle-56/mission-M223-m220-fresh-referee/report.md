# M223 final report: fresh immutable referee of M220

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
ACCEPT M220 AS FROZEN.
```

Its formal identities, exact finite counts, digest, first same-key obstruction,
and narrow logical boundary all survive independent reconstruction.

## Field 2 — immutable provenance

All M220 payloads return `OK`. Its `SHA256SUMS` digest is

```text
0b953e9c517cfeb379d32abe04b32ea928dd2a83e67bc1ac40d61f87fccd1316
```

and the inventory is complete. M220 remains immutable.

## Field 3 — target, convention, and clean method

The target is exact physical endpoint correction, not a probability law or
sampler. The independent checker uses chronological signed Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

It imports and reads no M220 code or result data, performs no route search,
and enumerates neither `Q_6` nor `Q_7`.

## Field 4 — formal identities

All 840 distinct carrier label assignments, 210 double-inverse assignments,
and 441 ordered transposition pairs for the single-inverse identity pass.
These formal identities survive independently of the finite-key no-go.

## Field 5 — finite specialization and next-rank replay

Two exact Prüfer constructions agree on 16 rank-five and 125 rank-six trees.
The displayed recurrence passes all 112 `d=5 -> 6` rows. At `d=6 -> 7`, the
per-edit pass counts are

```text
114, 125, 125, 125, 125, 125, 109, 125, 125,
```

hence 1,098/1,125 rows pass and 27 fail. The normalized row digest is

```text
f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
```

## Field 6 — first exact witness

The referee independently obtains the rank-six star and

```text
{{1,2},{1,3},{1,4},{1,6},{2,5}}
```

at edit 1. Their complete proposed descriptors are equal, as are their
17-move assigned words. The word passes the star and fails the second tree
only at positions 7 and 8, retaining `(45)^2` in place of `(46)^2`.

## Field 7 — numbered objections

Material objections:

1. None.

Nonmaterial objections:

1. None.

M220's `REJECT` applies exactly to its displayed descriptor-to-word map.

## Field 8 — reproduction and hygiene

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B fresh_recurrence_referee.py
```

Consecutive runs produce identical result hashes. After the decisive run, a
post-hoc comparison finds the independently generated witness, counts, and
digest exactly equal to frozen M220. All writes are confined to M223 and no
cache is retained.

## Field 9 — strict disposition

```text
ACCEPT: formal identities, complete finite checks, and the same-key
obstruction to the displayed recurrence.

DO NOT INFER: nonexistence of another braid or richer key, all-d routing,
every-color or arbitrary-representative compatibility, voltage/total length,
spectral gap, mixing, or Terminal.
```
