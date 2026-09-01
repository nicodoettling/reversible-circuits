# M168 freeze manifest

Frozen: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

```text
FINAL VERDICT: STRICT EXACT PHASE-COLLAPSE REDUCTION.
FCL1: UNRESOLVED.
```

The frozen proved result is limited to the balanced fixed cell `(a,b)=(1,1)`
for M73's nonlazy cyclic rank-two quotient kernel at `n=3k`, odd `k>=3`.
It includes the complete all-lag component-moment formula `(PC)`, the signed
cell-sum identity `(PCS)`, the physical cell-event identity `(CE)`, and the
deterministic scalar closure `(TV-close)--(SC)`. Both `(PCS-bound)` and
`(FD-bound)` remain unresolved. Finite positivity through the targeted exact
`k=9` check is not promoted.

Pre-manifest SHA-256 inventory:

| artifact | SHA-256 |
|---|---|
| `plan.md` | `f5023496392ae549ab040a77d524a81cfcce440d052065ffd155075094ad95f4` |
| `checkpoint.md` | `936e33611a25b8ca80534a36c9ece7a9c8bcf56070c860ee0787f93486205c2f` |
| `halfway_checkpoint.md` | `be96c412a91da959495e895bad10cf1702f8a3cf85b6e455e64d01f90043340a` |
| `phase_collapse_reduction.md` | `ea6667b8c679ce6fa342c43abbd6dc633cc586b4d972ff5333c28f212c489714` |
| `signed_cell_sum_probe.py` | `4e9f2bc1b2ea88c46433389e5763b37ea3db29d8498e873e09b10ee433e1d195` |
| `signed_cell_sum_results.json` | `ca68df60300bcb13cfbc5b088d42daac1b7e6620923bf31fc107da1c6b83d963` |
| `report.md` | `97357d9a31d5ebb13e41a790c0ff3cf8a82720a7f6e7e57b5a2ec44d3dedf83a` |

`SHA256SUMS` is the final machine-readable inventory and includes this
manifest. The checksum file is excluded from its own recursive hash.

Validation: `signed_cell_sum_probe.py` passed `ast.parse` and
`signed_cell_sum_results.json` parsed as JSON. The checker uses only the
Python standard library, is deterministic with `seed=null`, and imports no
predecessor code. Generated Python cache was removed.

No direct-L1, all-edge, H0, spectral-gap, bridge, identity-chain, mixing, or
Terminal conclusion is frozen. Fresh independent audit is required before
promotion.

