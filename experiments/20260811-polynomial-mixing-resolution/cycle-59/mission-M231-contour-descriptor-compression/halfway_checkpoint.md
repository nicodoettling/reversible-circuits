# M231 halfway checkpoint: route-normal quotient is exact on the finite table

Date: 2026-08-13 UTC.

## Source order and symbolic stage

M225 and M228 pass their complete frozen inventories. Before any M231
endpoint construction, `quotient_descriptors.md` fixed exactly two nested
quotients:

```text
Z_1=(v,late,ascent,epsilon),
Z_2=("closed",) if late OR ascent,
    ("open",v,epsilon) otherwise.
```

`symbolic_invariance.md` proves that the declared Candidate-B literal word
factors through both quotients. Thus word homogeneity is analytic: path and
off-path details cannot alter the displayed word once `Z_2` is fixed.

## Exact finite outcome

The no-input checker independently reconstructs 125 rank-six root-leaf trees
and all 500 ordinary odd-edit endpoints. It assigns the formula word before
endpoint construction, performs no route search or quotient-state enumeration,
and obtains 500/500 exact replays for both quotients.

```text
descriptor             edit 1   edit 3   edit 5   edit 7   global
full D_B classes          101      101      101      101      404
Z_1 classes                12        7        6        2       27
Z_2 classes                 6        4        3        2       12
```

`Z_2` has exactly one closed class plus eleven occurring open `(v,epsilon)`
classes. These are in bijection with the 12 distinct odd formula words:
identity plus 11 carrier conjugates. Adding the two fixed nonidentity boundary
words gives the frozen 14-word full-table count; internal even edits reuse
identity.

## Class sizes and certificates

The closed `Z_2` class contains 193 rows. Open class sizes are

```text
v=2: 1,3,11,11,24       (50 open; 75 closed at edit 1)
v=3: 5,14,46            (65 open; 60 closed at edit 3)
v=4: 24,60              (84 open; 41 closed at edit 5)
v=5: 108                (108 open; 17 closed at edit 7)
```

No same-quotient different-word or pass/failure collision exists. Digests:

```text
500 normalized rows 43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3
Z_1 classes         50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2
Z_2 classes         fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512
```

## Current verdict and boundary

**PROMOTE `Z_2` AS AN EXACT FINITE WORD/ENDPOINT INVARIANT.** It is
proof-scale in size and is the literal kernel of the declared formula at this
rank. This does not prove that `late OR ascent` and `epsilon` control DPS
closure at any other rank, nor any all-`d`, every-color, total-length, gap,
mixing, or Terminal statement.

Next: write the exact finite theorem/report, freeze, and request a fresh audit.
