# M231 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`PROMOTE Z_2 AS AN EXACT FINITE WORD/ENDPOINT INVARIANT.` No collision or
obstruction occurs in the complete declared odd-edit table.

## Exact certificates

```text
M225 inventory digest        e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M228 inventory digest        d20259c79d993ef63f8aab8235afeb75792153be6948767a0552d84d70f12237
carrier checks               840 / 840
initial-run sign checks      21 / 21
trees / odd edits / rows     125 / 4 / 500
passes / failures            500 / 0
full D_B classes by edit     101,101,101,101
Z_1 classes by edit/global   12,7,6,2 / 27
Z_2 classes by edit/global   6,4,3,2 / 12
odd formula words            12
full-table formula words     14
odd-row digest               43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3
Z_1 class digest             50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2
Z_2 class digest             fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512
checker-file digest          fa5af500637438893a660ce3e1b663081f52cff2d7d34520f4c9b11b058858b0
results-file digest          e72863b42426a5416772c49150b2d1f4328ccd66dc0e636211df10083ebc4c8a
```

Both quotients are word-homogeneous and endpoint-correct. Their first
different-word and different-behavior collision fields are null. Consecutive
deterministic runs produce the same result-file digest.

## Symbolic reduction

The declared Candidate-B word factors through

```text
D_B -> Z_1=(v,late,ascent,epsilon)
    -> Z_2=("closed",) or ("open",v,epsilon).
```

At fixed rank, `Z_2` is the exact kernel of the literal word map: open vertex
values have distinct word lengths, and sign vectors determine the first
differing signed generator pair. The single closed class contains 193 rows;
11 open classes contain the other 307.

## Method and strict boundary

The no-input checker assigns descriptors and words before endpoints, imports
and reads no predecessor implementation/data, and performs no route search or
quotient-state enumeration. The finite endpoint theorem does not prove that
the compressed invariant controls closure at any other rank.

No all-`d`, every-color, arbitrary-representative, voltage-corrected or total
length, spectral gap, mixing, or Terminal claim follows.

## Payload and audit

The frozen payload is exactly the files listed in `SHA256SUMS`; no cache is
included. Request the fresh immutable audit in `audit_request.md`, then stop.
