# M228 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`ACCEPT M225 AS FROZEN AT ITS STRICT FINITE SCOPE`.

Material objections: none.

Nonmaterial objections: the textual/mtime source-order evidence is consistent
but not independently cryptographically timestamped.

## Exact certificates

```text
M225 SHA256SUMS digest       e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M225 payloads verified       12 / 12
carrier substitutions        840 / 840
initial-run sign cases       21 / 21
unedited leaf extensions     125 / 125
trees / edits / rows         125 / 9 / 1125
Candidate A passes/failures  1109 / 16
Candidate A pass counts      125,125,125,125,125,125,109,125,125
Candidate A row digest       85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
Candidate B passes/failures  1125 / 0
Candidate B classes/words    407 / 14
Candidate B maximum length   17
Candidate B row digest       80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
checker-file digest          e37b930bbd96dbb630fde4d80f03ca0c19e40897396bde8b468817040e63634f
results-file digest          635cfb590175360929311d0c6a2863959fc304fa851d478a65b8fb0c657ed852
```

Candidate B's row-length histogram is
`{0:568,1:125,2:125,5:108,9:84,13:65,17:50}`. Consecutive deterministic runs
produce the same result-file digest.

## First exact collision

At edit 7, the star and `{{1,3},{1,4},{1,6},{2,3},{2,5}}` share Candidate-A
descriptor `("odd_A",5,false,[],false)` and its five-move word. The word
passes the star and fails the second tree at positions 8 and 11; Candidate B
records its ascending path `(5,2,3,1)` and assigns identity.

## Method and anti-lookup certificate

The no-input clean-room checker imports and reads no M225 code/data. A
formula route is assigned from tree/edit/candidate before endpoint construction.
Expected claims appear only as terminal assertions. There is no route search,
quotient enumeration, or route-output lookup.

Candidate B nearly records the full contour: for each odd edit it forms 101
classes on 125 trees, with 83 singleton classes. Its finite success and
17-move maximum do not imply all-rank descriptor sufficiency or length.

## Strict boundary and payload

No all-`d`, every-color, arbitrary-representative, voltage-corrected or total
length, spectral gap, mixing, or Terminal claim follows. The frozen M228
payload is exactly the files listed in `SHA256SUMS`; no cache is included.
