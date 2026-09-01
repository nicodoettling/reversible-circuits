# M131 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: first open all-suffix boundary, suffix excess `L=5`.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **PROMOTE A CONDITIONAL STRICT REDUCTION**. The complete unweighted
right-heavy auxiliary contraction is proved for every `6<=s<=99,K>=1` and,
for `s>=100`, is conditional only on the standalone exact scalar lemma
`C_s<=3/4`. The inherited `beta<=degree` envelope is refuted only as a proof
template. No auxiliary gap, original-chain mixing result, or Terminal
inference follows.

Target:

```text
H(s,K,K-1,s-5)=(I-Q)^(-1)A_0 <= q(1-q),
q=w_6 w_(s-5)/w_(s+1),  s>=6,K>=1.
```

All attachments `j=1,...,k` and the initial `q` normalization are retained.
Only `j=0` and auxiliary rank-one targets are killed.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `2deebf7037db0161f3b31bde70c1ef4dcc7cd92297da14aa718e93e9f797f09c` |
| `checkpoint.md` | `a55516f03164dfa45ca62bdf44e6ba802889373602027fd7172855b1871f4391` |
| `suffix_excess_five.md` | `b4b22d9f98109709c7bd81b11b1c0408510ec2c7e6a2d9380601a31dda9c1628` |
| `l5_exact.py` | `f8a77e8a02881649fe14fac1d8e71412c72680d600ae56d5fbdcdf314a18f724` |
| `l5_exact.json` | `ad8779c8b465110940b2cae351da4ace9df3c4c2d5fb4af379b882ae5fb6d217` |
| `report.md` | `129326b37b8b401e90093012452205ea86db478e57ce6f8c2e24fb9024870eb3` |

## Frozen dependency boundary

| artifact | independently observed SHA-256 |
|---|---|
| M109 `report.md` | `f68c3211d404d1cf045b101bdea26ccf105f38f708d5bbe0d64f9fb1aa1c6575` |
| M109 `excursion_reduction.md` | `6abb460e61592761bcb9be28095e578e6660138f67bb1ed110772fdca750062b` |
| M109 `SHA256SUMS` | `65d0173dbc27df08c6ff653cdbe9e0619f41798a49ec025f3f92a0f0fbc35106` |
| M114 `report.md` | `4eb435db38aa6cf05d63a727399e62612bd7968d81a41b31513ebe52dc25f039` |
| M114 `proof_audit.md` | `f042126cb20164b137d0d8f4bc60e90712a280e73e750d73d0cf1391336e33dd` |
| M114 `SHA256SUMS` | `3567f10502613ed0335c6270a3fa03defd5518b830dcb8a639f67dc1ae324234` |
| M115 `report.md` | `30a72149e1213eee3a8eb287db1f6f7f5d649f2cf9aa46b3c0f99b92d46441d5` |
| M115 `suffix_excess_three.md` | `b12ee541ceee4e195d9741fe3956fa668c22d8c8fe0859ea99232b00ba3c1835` |
| M115 `SHA256SUMS` | `199499d29ffbe7937bf18d0786380c4623b856603e11c3a99c2032ff114bfb2f` |
| M116 `report.md` | `7c5c5c7bdf01308a3f436c0d62e359ed37c67751f7c0a7441280b1ccc8fe2388` |
| M116 `proof_audit.md` | `af68cd411b126dd6f05b012a02702978a92172e3d7c29ae4ac59405a4dc7e198` |
| M116 `SHA256SUMS` | `3d5df6f6f6d23f9f1f6aeba129c053a7c7d105bea495afa6c2234ac6b7a2c8b7` |
| M117 `report.md` | `65213fb22e677c0a8fb1c23f41b769390cf42a684d0484d9b352d4e4bb8b8044` |
| M117 `suffix_excess_four.md` | `e9a1d5ca3080b1cb16308f201b83329131a13f8db50b98e863761dc3ed2c5398` |
| M117 `SHA256SUMS` | `93b420a9a30829a00ebac02446668a77ea1e8c97c5de86d3488517db546c801a` |
| M121 `report.md` | `a262e29c32ce8784f6064a0e181086e95e2cab70bfb5f73ed86ac6763b3bdf18` |
| M121 `proof_audit.md` | `b25f2234e762706866e45d623d817283bd83cba747d4dc2211d5ae1c863cd0ef` |
| M121 `SHA256SUMS` | `57d2a79c76f0b0915ed05145730d1ffd286e35cec95d680840bd909df8efa8df` |
| M123 `report.md` | `05a65a8f6111029a93a1c06e1dc014579ae013ff3d0ccaa356050189437afb9c` |
| M123 `freeze_manifest.md` | `72c8c7387fd71d0556ca91ebcc09ed2462aae891b6ad71342b64bbad7c5c51bd` |
| M123 `SHA256SUMS` | `624f97e155e4b142a56520ac149d5a9b7137a3ebf346a24a9b701c4534d837a0` |
| M128 `report.md` | `4a9e29d3bfa13940c06e4bc2d547c79f413e100e7437d97b6b58670ab07f97db` |
| M128 `freeze_manifest.md` | `9287db21dfb3770baa29104ef1685a5a3be6000ac6ccaecf384287e56a2a27cd` |
| M128 `SHA256SUMS` | `5b1252ee9da723c1d02f94400c658884529ca41a406a598103b91f616a0ee292` |

All eight predecessor checksum inventories passed independently before this
freeze.

## Reproduction and validation

From this mission directory:

```text
python3 -B l5_exact.py --s-max 12 --certify --output l5_exact.json
```

Environment: Python `3.12.3`, standard library only, exact
`fractions.Fraction` arithmetic, deterministic `seed=null`.

Validation completed:

- all 32 supported roots, 31 nominal exceptional occurrences, 11 live groups,
  and every attachment `j=1,...,k` were retained in the grouped audit;
- literal full-basin resets match grouped resets at `s=6,7` and `K=1,5`;
- the `s=6` audit retains 17 children and confirms every `t=2` child is
  inactive;
- the arbitrary-deficit `L=1,2` formulas match accepted predecessors exactly,
  and the structural `L=3` envelope has zero finite falsification failures;
- all 1222 finite exact Bernstein coefficients for `s=6,...,99` are positive;
- all 4212 conditional-tail tensor coefficients are positive, and the exact
  off-grid interpolation identity passes;
- the rational ratio-box endpoint inequalities and the corrected
  `2(3-e)<17/30` partial-sum inequality pass exact checks;
- `l5_exact.json` parsed, the script compiled, and no Python cache directory
  remained at freeze time;
- no package was installed and no file outside this owned directory was
  edited.

`SHA256SUMS` hashes every payload above and this manifest; it intentionally
does not hash itself.
