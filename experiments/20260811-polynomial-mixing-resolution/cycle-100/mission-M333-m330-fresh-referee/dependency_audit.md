# M333 immutable dependency audit

Date: 2026-08-14 UTC

## M330 payload gate

The SHA-256 of frozen M330's `SHA256SUMS` is exactly
`623ec4026179c81cc2a1ec49ce3318af470562924d7a34ac5bc6a6ba76547f93`.
Its inventory has exactly 12 rows, all passing `sha256sum -c`:

```text
ac516bee56965077f68142f493faa607cf68933083050690691da70e211adf92  plan.md
d3f4a8168b8c8e41b9aae4b22824d0aa7787665b589cf4bab35fa30ed0572d7a  checkpoint.md
647133a42d9d450b30c82a24b10e2f2506da7cd9957877fb0a7bf14b1d41e56c  source_lock.md
c7cc69703fbca5d6c14fe7b28c156319bfa84b8259013d0fbfcd65a74e8dc441  halfway_checkpoint.md
a0170048420490a033e6c449020354e98048cb4e5f44ff1ce08a1bfe7c062cbd  na_k7_h2_a_fiber.py
9d8eecc3b06df3364c6659643cf939012393678bd39c51b2214da911dbc5105e  na_k7_h2_a_fiber_results.json
c8b8edac86c5871a5d68a326253e9c2f89afe6b500617c487c676069cfdecb9d  proof.md
7731071afa881287c8f8ecb4ee7288dc4bc488a956496135502d5295ddbb441d  report.md
df12e67c6d0902a366a8586f6b3c6a01467e1e127ed54a862ae756a2a73f9e0b  run_manifest.md
b923400bf997f0b89542e7df751f7414e179a6b2bdc4ac8db895931824cf24b6  audit_request.md
a3eadc3066df19ed586dc89b8aeceb0efdabf771254037dcba0f2bc789f37432  final_checkpoint.md
eb36d468626690684814a60905b71156ae15c3a850cb5790bedda41bec40c84a  freeze_manifest.md
```

M330 was not modified.

## Predecessor and raw-law locks

| package/input | observed SHA-256 | result |
|---|---|---|
| M323 top | `0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c` | 15/15 payloads pass |
| M323 guard | `4a00e3d5e74c7d92ba5f95bdbde447a33f1ef327d9625a40445be101f4f81bc1` | direct lock |
| M323 result | `134de6bd6972654bf3b264ef6dac94744007b735f18bc1955b03061e83cf7821` | direct lock |
| M326 top | `a1ea699e4086cb967875c9408f586afc0854c85096a278e32eed9697b5ba2a2a` | 9 rows pass; one row malformed |
| M329 top | `6f3c67dadba4475b70f3372f4b61be575f917f463dd3c62db1afc14813aa11df` | 7/7 payloads pass |
| M297 top | `a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792` | 12/12 payloads pass |
| M297 primitive | `9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73` | direct lock |

M323's 198-row source ledger is frozen under its verified top. The minimal
direct raw-law inputs used here were its guard/result and locked M297
primitive.

M326 row 8 has only 63 hex characters:
`a27542054b7af7edbff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4`.
Independent hashing of `run_manifest.md` gives the full value recorded by
M329:
`a27542054b7af7ed7bff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4`.
M329 therefore repairs provenance only; M326's mathematical REJECT is
unchanged.

## Replay

The one authorized `k=7,H_2,(1,1)` replay exited zero in `/tmp`. Its
JSON and M330's frozen result both hash to
`9d8eecc3b06df3364c6659643cf939012393678bd39c51b2214da911dbc5105e`;
`diff -u` is empty. No other cell, rank, row, or surgery was run.
