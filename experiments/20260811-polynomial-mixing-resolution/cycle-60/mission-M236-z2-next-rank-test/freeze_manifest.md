# M236 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

```text
PROMOTE ONLY AN EXACT FINITE d=7 -> 8 NEXT-RANK THEOREM.
```

The predeclared M231/M234 route-normal formula has no failure or same-Z2
behavior collision in the complete declared primary table. This freeze makes
no all-rank claim.

## Immutable source gate

Every frozen payload in M214/M218, M220/M223, M225/M228, and M231/M234 passed
its checksum inventory before any next-rank endpoint was constructed. The
formula gate changes only the rank from `d=6` to `d=7`; all descriptors,
predicates, signs, and route words remain fixed.

## Exact certificates

```text
formal carrier substitutions                 1680 / 1680
initial-run sign checks                         28 / 28
root-leaf trees                               1296
primary edits                                 1,3,5,7,9
primary rows / passes / failures              6480 / 6480 / 0
Z2 classes by edit                            9,6,4,3,2
Z2 classes / primary words                    20 / 20
closed / open primary rows                    2974 / 3506
maximum finite primary route length           21
secondary edits                               2,4,6,8,10,11
secondary rows / passes / failures            7776 / 7776 / 0
full rows / passes / failures                 14256 / 14256 / 0
full distinct words                           22
first formula failure                         null
first same-Z2 behavior collision              null
first fixed-family failure                    null
tree-universe digest                          4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary-row digest                            f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2-class digest                               30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
primary-word digest                           3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608
secondary-row digest                          f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full-row digest                               114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
full-word digest                              d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c
```

The primary route-length histogram is
`{0:2974,5:1029,9:833,13:672,17:540,21:432}`. The full-table histogram is
`{0:8158,1:1296,2:1296,5:1029,9:833,13:672,17:540,21:432}`.

## Frozen payload hashes before manifest

```text
plan.md                         8662f0091964f231645cbe0239d501f29f5f96681c97a7996d6f359fd4ca8bab
checkpoint.md                   4bb7d791d7825df3800f571ea0485c47d97898c0ee2f3bd42b933beaae1cb440
immutable_gate.md               aea6947e9d328b96393090ad691789ca1717e86c7bcc8096833e8f3838594da5
halfway_checkpoint.md           efea968c6ff52c93b18c535e47f8b0e0b7e6b6bdac328ed245bba3829db6643c
z2_next_rank_check.py           82fddb99feea08eb8604439475065b7d4ba739c4e3b2fa89a858b921c5c57dd1
z2_next_rank_results.json       34e7a7a76b7993595b71a588d43afe85a443d851e722bb60b6e3d5f2bc3e1585
finite_next_rank_theorem.md     57ccf3ccbdcf0f83c73b9ee2fea8332fd1f45d7d8af3af7d5f7bfc1223bbc07d
report.md                       60eefd6511d970eb58727d32a95bb9011739e07285337f30ee83eaca311f0b3e
audit_request.md                01b5e95ef5c39e4e3476c875bfc07182cae37ffa6f001379251d70b031e7f8f0
```

Two consecutive executions produced the identical result-file digest shown
above.

## Method and logical boundary

The checker reads no inputs and imports no predecessor. It computes Z2 and
the formula word before endpoints, independently constructs the DPS words,
checks identity products, and performs literal signed-Hurwitz replay. It uses
no route search, target lookup, quotient-state enumeration, or group-element
enumeration. The remaining fixed families are reconciled separately and are
not Z2 rows.

The first unproved step remains the all-rank DPS closure lemma. This finite
pass proves no every-color route, arbitrary-representative routing,
polynomial or corrected total length, comparison congestion, spectral gap,
mixing bound, or Terminal result.

The frozen payload is exactly the files listed in `SHA256SUMS`; no cache is
included. Request the fresh immutable audit in `audit_request.md`, then stop.

