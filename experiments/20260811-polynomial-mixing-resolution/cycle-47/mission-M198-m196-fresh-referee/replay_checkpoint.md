# M198 substantive replay checkpoint

Date: 2026-08-13 UTC.

The clean-room checker completed in 3.80 seconds and returned `ACCEPT` with an
empty objection list.

Exact independent results:

```text
Q5 canonical states rebuilt:            8,400
all 14 action rows exact-match frozen:  yes
signed inverse pairs:                   7 / 7
source IDs:                             (16,0)
transversal size / max depth:           8,400 / 13
rooted DPS descriptors rebuilt:         10
named target rows / occurrences:        54 / 175
distinct adjusted targets:              41
radius-8 forward product-ball states:   154,393
direct / nonempty-backward hits:        15 / 26
stabilizer replays:                     41 / 41
adjustment/full endpoint replays:       54 / 54
max forward/back/stabilizer/tree/full:  8 / 7 / 15 / 9 / 22
```

The independent forward level sizes are
`1,6,40,190,795,2976,10416,34256,105713`. The packed action digest and frozen
result digest reproduce exactly as

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae
e40c220ea10798b82d7225cbde54daec751f25e581028c926e2a11ba3e33a4b2.
```

No full stabilizer orbit or `Q_5^2` enumeration was run. No broader inference
is under review. The remaining work is report/proof-audit packaging and freeze
hashes only; no further search is warranted.
