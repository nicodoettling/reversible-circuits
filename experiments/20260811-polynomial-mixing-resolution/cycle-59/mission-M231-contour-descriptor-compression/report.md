# M231 final report: full contour compresses to the formula kernel

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
PROMOTE Z_2 AS AN EXACT FINITE WORD/ENDPOINT INVARIANT.
```

No obstruction occurs on the declared 500-row table. The 404 full odd
contour classes compress to 12 route-normal classes, exactly the 12 occurring
odd formula words.

## Field 2 — immutable provenance

Every frozen payload in M225 and M228 returns `OK`. Their inventory digests
are

```text
M225 e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M228 d20259c79d993ef63f8aab8235afeb75792153be6948767a0552d84d70f12237
```

Neither predecessor was edited or imported into the decisive checker.

## Field 3 — exact target and convention

There is no probability distribution, sampler, or Markov kernel in M231. The
target is exact endpoint correction for 125 rank-six root-leaf trees and odd
edits `{1,3,5,7}` under chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

## Field 4 — predeclared quotients

Before constructing any endpoint, `quotient_descriptors.md` fixed exactly
two nested quotients and forbade a third:

```text
Z_1=(v,late,ascent,epsilon),
Z_2=("closed",) if late OR ascent,
    ("open",v,epsilon) otherwise.
```

Their a priori per-edit upper bounds were respectively `4*2^L` and `1+2^L`,
already substantially below 101. No post-result tuning occurred.

## Field 5 — symbolic compression lemma

The declared Candidate-B word uses the full descriptor only through the
closure bit `late OR ascent` and `(v,epsilon)` in `Q B Q^-1`. Hence the word
map factors through both quotients. Moreover, `Z_2` is the literal word-map
kernel at fixed rank: open `v` values have distinct lengths, and different
sign vectors give different first differing signed transport pairs.

This proves word homogeneity symbolically. It does not by itself prove that
the assigned word reaches the endpoint.

## Field 6 — exact compression and endpoint result

The complete independent replay gives

```text
descriptor             edit 1   edit 3   edit 5   edit 7   global
full D_B classes          101      101      101      101      404
Z_1 classes                12        7        6        2       27
Z_2 classes                 6        4        3        2       12
passes                     125      125      125      125      500
failures                     0        0        0        0        0
```

Both quotients are classwise word-homogeneous and endpoint-correct. No first
collision exists. The `Z_2` closed class has 193 rows; its 11 open classes
have sizes `1,3,11,11,24,5,14,46,24,60,108`.

## Field 7 — word counts and exact digests

`Z_2` has exactly 12 classes and exactly 12 odd literal words. Internal even
edits reuse identity; the two fixed boundary words raise the full-table image
to 14, reconciling M225/M228 without endpoint-derived route lookup.

```text
odd-row digest  43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3
Z_1 digest      50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2
Z_2 digest      fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512
```

## Field 8 — reproduction and anti-lookup audit

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B contour_compression_check.py
```

The checker has no input-read calls or predecessor dependency. For every row
it computes descriptor and literal formula route before endpoints. It performs
no route search or quotient-state enumeration. Consecutive runs have identical
result hashes, all writes are confined to M231, and no cache is retained.

## Field 9 — reduction boundary and audit request

```text
PROMOTE: exact symbolic factorization of the declared word map and the
complete finite 404 -> 27 -> 12 descriptor compression with 500/500 endpoint
replays.

DO NOT INFER: all-rank correctness of the closure/sign invariant, every-color
or arbitrary-representative routing, voltage-corrected or total route length,
spectral gap, mixing, or Terminal.
```

The next standalone lemma is the all-rank DPS closure implication for
`late OR ascent` and `epsilon`. Freeze M231 and request a fresh immutable
clean-room audit of source order, both quotients, class census, word-kernel
proof, endpoint replays, digests, and strict scope.
