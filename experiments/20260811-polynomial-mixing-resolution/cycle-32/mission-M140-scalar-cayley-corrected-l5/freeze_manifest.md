# M140 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: standalone scalar Cayley Lemma C and corrected auxiliary right-heavy
suffix-excess-five contraction.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **PROMOTE TWO PROVED AUXILIARY RESULTS FOR FRESH REFEREE AUDIT**.

```text
C_s<74969/100000<3/4 for every s>=100.

H(s,K,K-1,s-5)<q(1-q) for every s>=6,K>=1,
q=w_6 w_(s-5)/w_(s+1),
```

where the second statement is relative only to the accepted all-rank
recurrence and lower-excess envelopes.  It uses the corrected one-power
exceptional subtraction `a_E lambda_E`; the rejected two-power M131 display
is never used.  No gap, ROOT-MEAN LIFT, mixing, or project terminal follows.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `9e57b5f5bbd157936e8bc7976ae2237ad4eb60fc4e19752fcf8f5d31715b6923` |
| `checkpoint.md` | `9be0cd67bd02ee643babc625830f41021fe21c9192fffb8ae2c7607e4a94ca46` |
| `scalar_cayley_corrected_l5.md` | `d8e49d7e06eb82f45621febb3107e75d0ab35eea440402db083797675e994bb6` |
| `scalar_cayley_exact.py` | `11ca05a80cb29bcf795ad49658aa4d0f7a814acf82a347ba11c44902b97a3e12` |
| `scalar_cayley_exact.json` | `d20660381064b65ce1ca632282fac188241e34cf4af4f0a5d8d5c6f2d36e6650` |
| `corrected_l5_certificates.py` | `b9330081dbe86a7a5c3cd36e1ada63b21b44275f76d5dfb8ad17210305434bac` |
| `corrected_l5_certificates.json` | `16a816cdeb59a6431e2c33e8965d5f30554184d5babe08fc62b3eedcd3e08937` |
| `report.md` | `4b724f49eb6c47b7697ccb39f16b1a17fed693d17e259569898593898c0946f3` |

## Immutable dependency boundary

| artifact | observed SHA-256 |
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
| M138 `report.md` | `bb6501ae5a7386e70e00ce520449af27aef4a0e32b944aff9a734f082d87cd5e` |
| M138 `proof_audit.md` | `a08a6d99d843c21f9f822b139f625ffe56e456c90e22ea2c4b899fb57c6573d6` |
| M138 `independent_m131_referee.py` | `4e07c4e4202c764a56400945316604ddb2352d4de128aa8e45ec614f3a2ce94e` |
| M138 `independent_m131_referee.json` | `f631c9134b02c29a90e87d564e8a2dd8f020d714b9652679ef14b712fab9fc00` |
| M138 `freeze_manifest.md` | `40bd1d07000e4517e8d1a1f5ac1b40ab3ca7530d8835a55b0f32a1e5ffdc328e` |
| M138 `SHA256SUMS` | `5eb1b857b567b4f3256917cd6648c67aef4fd8cedced3edb59c8ab607ac4a50b` |

All dependency hashes above were independently observed immediately before
freeze.  M131 is retained as a negative provenance artifact, not a positive
theorem dependency.

## Reproduction and exact outcomes

From this mission directory:

```text
python3 -B scalar_cayley_exact.py --output scalar_cayley_exact.json

python3 -B corrected_l5_certificates.py \
  --output corrected_l5_certificates.json \
  --reference-json \
  ../../cycle-31/mission-M138-m131-fresh-referee/independent_m131_referee.json
```

Environment: Python 3.12.3, standard library only, exact
`fractions.Fraction` arithmetic for theorem-critical computations,
deterministic `seed=null`.

Final exact outcomes:

- zero scalar-checker failures;
- 435 exact first-moment rows, zero mismatches;
- zero binomial-to-Poisson direction failures in 7,140 diagnostic tails;
- exact final scalar upper bound `74969/100000<3/4`;
- zero corrected-subtraction failures over all 31 occurrences at `s=6,7`;
- all 1,222 finite Bernstein coefficients positive, with canonical digest
  `733243ff50622263540085ff0d6d4b01246164cc8119003cacb5dbeda11684f7`;
- all 4,212 tail coefficients positive, with canonical digest
  `2c1aa8475dba3ae3d3c09f587662facb78b1c11e14aec2d04ae8d87bb5adf22f`;
- exact post-hoc equality of both coefficient lists with frozen M138;
- strict `s=6` minimum coefficient
  `13461835439971/11861248695609600>0`;
- both JSON files parsed, all owned prose/source had no trailing whitespace,
  and no owned Python cache directory remained at freeze.

No package was installed and no file outside this owned directory was edited.
`SHA256SUMS` hashes every payload above and this manifest; it intentionally
does not hash itself.
