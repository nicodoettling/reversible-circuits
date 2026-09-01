# M147 freeze manifest

Date: 2026-08-13 UTC.

## Scope and result

M147 proves an exact all-suffix functional recurrence for the auxiliary
unweighted reset excursion on the attachment state `(kappa,D)`, and an
infinite reachable obstruction to any deficit-blind pointwise scalar Bellman
closure using only suffix data, `q`, `C_s`, Cayley ratios, and even `K/z`.
It proves no auxiliary gap, ROOT-MEAN LIFT, original-chain gap, mixing result,
or project terminal.

The first exact strict witness is

```text
H(3,32,1,2)=175033/743424 > 15/64,
margin=793/743424,
```

paired with the right-heavy state

```text
H(3,32,31,2)=24313/743424 < 15/64.
```

Both have identical recorded scalar data except `D=K-R`.

## Environment and deterministic command

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
dependencies: Python standard library only
seed: null
command: python3 -B all_suffix_exact.py --output all_suffix_exact.json
```

Final result payload SHA-256:

```text
441000e76bc60c12093355bda4272ee9fefc9b621c3e4b30b30d17bcb39cb06b  all_suffix_exact.json
```

The final run reports zero failures, 270 attachment normalization rows,
eight suffix recurrence cases, eleven boundary rows, and nine moment rows.

## Accepted dependency hashes observed before freeze

```text
f68c3211d404d1cf045b101bdea26ccf105f38f708d5bbe0d64f9fb1aa1c6575  M109 report
65d0173dbc27df08c6ff653cdbe9e0619f41798a49ec025f3f92a0f0fbc35106  M109 SHA256SUMS
4eb435db38aa6cf05d63a727399e62612bd7968d81a41b31513ebe52dc25f039  M114 report
3567f10502613ed0335c6270a3fa03defd5518b830dcb8a639f67dc1ae324234  M114 SHA256SUMS
30a72149e1213eee3a8eb287db1f6f7f5d649f2cf9aa46b3c0f99b92d46441d5  M115 report
199499d29ffbe7937bf18d0786380c4623b856603e11c3a99c2032ff114bfb2f  M115 SHA256SUMS
7c5c5c7bdf01308a3f436c0d62e359ed37c67751f7c0a7441280b1ccc8fe2388  M116 report
3d5df6f6f6d23f9f1f6aeba129c053a7c7d105bea495afa6c2234ac6b7a2c8b7  M116 SHA256SUMS
65213fb22e677c0a8fb1c23f41b769390cf42a684d0484d9b352d4e4bb8b8044  M117 report
93b420a9a30829a00ebac02446668a77ea1e8c97c5de86d3488517db546c801a  M117 SHA256SUMS
a262e29c32ce8784f6064a0e181086e95e2cab70bfb5f73ed86ac6763b3bdf18  M121 report
57d2a79c76f0b0915ed05145730d1ffd286e35cec95d680840bd909df8efa8df  M121 SHA256SUMS
4b724f49eb6c47b7697ccb39f16b1a17fed693d17e259569898593898c0946f3  M140 report
fa0e32780ad9c9338e49751b02817ed947a6175699cc16a7b2f05d913598a68e  M140 SHA256SUMS
7670f7f4717a81d427df68c24b4bd90a5e38e57ea7d8ae21caa437e79c86b6d2  M144 report
f5830181410af7b8114f474b0091eb963b7c9de4c4a83e93b7c425ba8c9873d6  M144 SHA256SUMS
```

M131 is negative provenance and was not used.  No predecessor artifact was
edited.

## Owned inventory

```text
plan.md
checkpoint.md
all_suffix_functional_obstruction.md
all_suffix_exact.py
all_suffix_exact.json
report.md
freeze_manifest.md
SHA256SUMS
```

The default sandbox intermittently failed during `bwrap` loopback setup with
`RTM_NEWADDR: Operation not permitted`; only scoped approved repository reads,
writes, and exact runs were used.  No package, network access, or machine
configuration change was requested.  The initial checker run exposed an
implementation-only negative-exponent `Fraction` construction in the Cayley
coefficient.  It was replaced by the algebraically identical rational form
before any result was retained; all final audits pass.

