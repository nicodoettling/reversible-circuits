# M138 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: fresh referee audit of frozen M131 suffix-excess-five reduction.

Repository commit audited: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

```text
FINAL VERDICT: REJECT AS FROZEN.
MATERIAL OBJECTION M-1: proof equation (5.1) uses supported_mass*lambda^2,
while the source and positive certificates use supported_mass*lambda.
CORRECTED CONDITIONAL THEOREM: independently salvaged, not promoted.
LEMMA C: unresolved and not attempted.
```

## Immutable M131 gate

| artifact | observed SHA-256 |
|---|---|
| M131 `report.md` | `129326b37b8b401e90093012452205ea86db478e57ce6f8c2e24fb9024870eb3` |
| M131 `suffix_excess_five.md` | `b4b22d9f98109709c7bd81b11b1c0408510ec2c7e6a2d9380601a31dda9c1628` |
| M131 `l5_exact.py` | `f8a77e8a02881649fe14fac1d8e71412c72680d600ae56d5fbdcdf314a18f724` |
| M131 `l5_exact.json` | `ad8779c8b465110940b2cae351da4ace9df3c4c2d5fb4af379b882ae5fb6d217` |
| M131 `freeze_manifest.md` | `db81797b3d6b56c36166844dde09da7d5552f265f8a65b72618f33836155069c` |
| M131 `SHA256SUMS` | `20b239f7c3d979a5616ed56e3ecd81c1cf7969d5b604118c192e41f3e6bf96f7` |

All checksum inventories for M109/M114, M115/M116, M117/M121, M123/M128,
and M131 passed before freeze.  No frozen artifact was edited.

## Owned payload

| file | SHA-256 |
|---|---|
| `plan.md` | `38152074216d9d837b4a580c7426e52ef3fe2eb0e367c3c8ce8bf87a31b5bb51` |
| `checkpoint.md` | `ee39dfdc3613e3e37b70341fe4460bf7b8918136285d27754f53fd3830489197` |
| `proof_audit.md` | `a08a6d99d843c21f9f822b139f625ffe56e456c90e22ea2c4b899fb57c6573d6` |
| `independent_m131_referee.py` | `4e07c4e4202c764a56400945316604ddb2352d4de128aa8e45ec614f3a2ce94e` |
| `independent_m131_referee.json` | `f631c9134b02c29a90e87d564e8a2dd8f020d714b9652679ef14b712fab9fc00` |
| `report.md` | `bb6501ae5a7386e70e00ce520449af27aef4a0e32b944aff9a734f082d87cd5e` |

## Reproduction and exact outcomes

Run from this directory:

```text
python3 -B independent_m131_referee.py \
  --output independent_m131_referee.json \
  --reference-json ../../cycle-28/mission-M131-suffix-excess-five/l5_exact.json
```

Environment: Python 3.12.3, standard library only, exact
`fractions.Fraction` arithmetic, deterministic `seed=null`.

The fresh mathematical payload is completed before the optional frozen JSON
is opened.  Exact outcomes:

- corrected-formula failure count: zero;
- frozen-artifact material objection count: one;
- root counts `32/31/8/16/11` and the 17-child `s=6` boundary pass;
- 504 arbitrary-deficit rows pass, with exact accepted `L=1,2` formula
  equality;
- all 1222 corrected finite Bernstein coefficients are positive and equal the
  frozen checker fractions;
- all 4212 corrected conditional-tail coefficients are positive and equal the
  frozen checker fractions;
- all 20 selected `L=5` rows, six selected `C_s` values, and the coarse
  counterexample fractions agree post hoc;
- the written `lambda^2` envelope fails at `(s,K)=(6,64)` and has exact
  negative `s=6` coefficient
  `-19717205656843140443/125254786225637376000` at index two;
- JSON parsing, source compilation, exact off-grid identities, whitespace,
  and owned cache hygiene pass.

`SHA256SUMS` hashes every owned payload listed above and this manifest; it
intentionally does not hash itself.  No package was installed, and no file
outside this owned directory was edited.
