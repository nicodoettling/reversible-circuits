# M237 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

```text
ACCEPT M236 AS FROZEN.
```

Accepted scope is only the complete finite `d=7 -> 8` one-leaf endpoint
theorem.  No all-rank or mixing consequence is accepted.

## M236 immutability certificate

All ten M236 payloads pass their frozen checksum inventory; the inventory is
complete and has top digest

```text
0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a.
```

M237 did not modify, import, or execute M236.  Static inspection was deferred
until the independent substantive table and native hashes had been fixed.

## Exact clean-room certificates

```text
root-leaf trees / dual constructions equal       1296 / yes
source-extension identities                       1296 / 1296
formal carrier substitutions                      1680 / 1680
initial-run sign cases                              28 / 28
primary rows / passes / failures                  6480 / 6480 / 0
Z2 classes by edit                                9,6,4,3,2
global Z2 classes                                 20
closed / open primary rows                        2974 / 3506
primary formula words / maximum length            20 / 21
secondary rows / passes / failures                7776 / 7776 / 0
full rows / passes / failures                    14256 / 14256 / 0
full distinct words                               22
first formula failure                             null
first same-Z2 behavior collision                  null
first fixed-family failure                        null
```

The primary histogram is
`{0:2974,5:1029,9:833,13:672,17:540,21:432}`; the complete histogram is
`{0:8158,1:1296,2:1296,5:1029,9:833,13:672,17:540,21:432}`.

## Published-normalization replay

All seven M236 normalized digests are independently reproduced:

```text
tree universe   4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary rows    f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2 classes      30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
primary words   3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608
secondary rows  f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full rows       114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
full words      d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c
```

Two consecutive final runs produced identical result bytes.

## Frozen payload hashes before manifest

```text
plan.md                  d9a204a07eb671993837be56b8dadd31410dc48a6fba580e24fee68e2f12dd60
checkpoint.md            ed253303fbb5c72b9533bb02ce14c22255d9954031c643782da90422b7840f8b
independent_referee.py   b0d27a9011ad3de32b3ecb4264981b6d1ea810b1152db87b6c16f2beb67c756a
referee_results.json     f2f36b7ba75d9bdf978dd07d0b132183f914551df832a3fd528bd5d7342da037
source_audit.md          f5a90a44ed994c22d88295f6320fc060e10f2ed5df90f51689217daf8fa78d9a
report.md                37d598587865c94628e2475a8026adf51897bc4e3d74d56b7da6a488c6133b43
```

## Logical boundary

The only nonmaterial qualification is that source predeclaration is supported
by assertion, checksums, and filesystem chronology rather than an external
cryptographic timestamp.  There are no material objections.

The freeze proves no all-rank DPS closure, every-color route,
arbitrary-representative route, polynomial length, comparison congestion,
spectral gap, polynomial mixing, or Terminal.

