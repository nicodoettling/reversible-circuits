# M133 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: positive defect-coefficient no-valley frontier.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **PROMOTE FOR FRESH AUDIT** the exact subtraction-free unique-cycle
expansion; **REFUTE** pairwise fixed-core polarization at `d=4,c=3`; **KEEP
OPEN** ordinary log-concavity and DEFECT NO-VALLEY.  Targeted exact margins
remain positive only through the declared cap `d=26`.  No spectral-gap,
original-chain, or terminal result follows.

Target: `rho(kappa)=|C_kappa|/Z_inc` on M113/M118's realizable connected-
unicyclic incidence keys, under `(pq)(x)=p(q(x))` with tuple factors multiplied
left-to-right.  The unnormalized coefficient is
`H[d,c]=M[d,d-c]=sum_{c(p)=c}|C_kappa|`, not a mass under the original uniform
identity-word law.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `3a616fee2eef82e6fe76226a6710699b2a0616d478e27f3f0a255b57952d65ea` |
| `checkpoint.md` | `986d9abb2d886fb4ab56f26aa9a3cc133c82878c71e49fc6d4e3e4643cbaf089` |
| `positive_unicycle_reduction.md` | `c80606c1d821c82df8c2d2ab9e4d4be01baa4032046d896cba2604f60c299fb9` |
| `positive_unicycle_audit.py` | `5eefdff04b13de058ddafcc9767aae84f5b2b96b7bc9c75896cfeb3cc2a34e82` |
| `positive_unicycle_results.json` | `1a83ddc483f0b8bad2d6c917e4a726e20406066cac9139dfacdf7b9a9635ff00` |
| `core_profile_scan.py` | `b4cbba5dabace6469695abb852c2f07d54a310fd2cbf884d1cabb95db8509b75` |
| `core_profile_results.json` | `ff55915705acc7ea3377e93ca2a1f7fb206f9f0578b4cea4cad384ac48689e0e` |
| `frontier_scan.py` | `8dc1d63ba93e6cf05a1053fdd89202d167ee3253835c74c4cc59d9473303b488` |
| `frontier_smoke.json` | `1ce1f3176c60eede4964b905f9f7bc97901a827c0ec47aa1ec8a636a7ea94755` |
| `frontier_d23.json` | `45ae3dc98dc51ffd4372495364ae5915c4ce49a51bb415c8fb40976b953581e3` |
| `frontier_d24_d25.json` | `4670d2cfcebe0fc687c992eaac3a86d650b31088c0c6156f39ac5cfc1b0ba0d9` |
| `frontier_d26.json` | `3012e8cf3ccb2b8dccfb4218b055286f1d6e6c5570d203353b013deb1f74a6e4` |
| `report.md` | `afd0fcc3dddc51f20c8eb2d3b2d7eeb2d25aa3c9eaea204d91b958adf537619e` |

## Frozen dependency boundary

| artifact | independently observed SHA-256 |
|---|---|
| M113 `report.md` | `295c6d50b70117915cc99d9ebe6e1e88cbfab258a404db66a0b1543ea01cfe47` |
| M113 `freeze_manifest.md` | `64cf3bb48baca3022690cb72c5afc458e3fbf8e514b56612c099b7f9b1e0b6bf` |
| M118 `report.md` | `e780115979cfb3c281007fe62a507cd2062d1d061cd9bd2faa3f6f54a4387b3b` |
| M118 `freeze_manifest.md` | `2c1552d1df1af619cad35d86b45a369473c0852e7c9c5721c6b6e8dac0cfaf98` |
| M120 `report.md` | `9f1cdd5f137b32b3ded80d951b6067565edac2ade9032d18cb0251e7c92803db` |
| M120 `freeze_manifest.md` | `9e70cb1f3db32ae602f99c7ff78e5800e66069ce893b546e7c3f46212a8f515b` |
| M124 `report.md` | `c775a4cc3a6ec6336b082ababd76c90026185069c2d44457942b313c4ea38404` |
| M124 `freeze_manifest.md` | `b774120500c47f4849fafb76dcaba7ca9d62bd5fd7d98d156a7192ab5d52501a` |
| M125 `report.md` | `dc8f8cb0ab9c6c06f9b49cd56a30b29cc258698dcdfccceb887b265ff67c5879` |
| M125 `defect_recurrence.md` | `068a42ed4c9141cbabd81ffe35d352c833b634a295a9a6a6f44dabbeb09ffde1` |
| M125 `defect_species.py` | `74cd0159ac62404db172ff3830a1ef58f9f7a105eb2f595b438af66c24c3dde9` |
| M125 `freeze_manifest.md` | `a6bb1090f1a6f88c38ddd253ec35069e062f9a00563096ae1d0617370b7befdd` |
| M129 `report.md` | `eb7cdcd179a704deed4a8b7cb03a7a69c912bc0b57677a7fb2d886d17056b2d4` |
| M129 `freeze_manifest.md` | `9128aa1883796f6bf757bbb46a60ef8450ce9b859f94a4eeed40dac771320b45` |

All six dependency `SHA256SUMS` inventories passed independently before
freeze.

## Reproduction and validation

The exact commands are recorded in `report.md`.  Environment: Python
`3.12.3`, standard library only, deterministic `seed=null`.  Validation
completed:

- the positive recurrence equals literal ordered partition pairs for all 37
  integer cycle types through total size seven, with zero failures;
- the core-length aggregation equals every accepted M125 row through `d=8`,
  with zero mismatches;
- the two-parallel-edge core, all available longer cores, colour symmetry, and
  canonical orientation factors are included in those audits;
- the first pairwise core-polarization failure is exactly
  `(d,c,k,l)=(4,3,2,4)`, with cleared margin `-17309376`;
- the targeted exact ordinary ratios at `(23,7)`, `(24,8)`, `(25,8)`, and
  `(26,9)` are all strictly greater than one; no universal inference is made;
- every JSON artifact parsed, all scripts executed under `python3 -B`, and no
  Python cache directory remained at freeze time;
- no package was installed and no file outside this owned directory was
  edited.

`SHA256SUMS` hashes every payload above and this manifest; it intentionally
does not hash itself.
