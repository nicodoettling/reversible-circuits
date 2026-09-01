# M330 minimal immutable source lock

Date: 2026-08-14 UTC

Only the packages and primitive required for the fixed-cell `N_A` check were
locked:

| object | reproduced SHA-256 |
|---|---|
| M323 `SHA256SUMS` | `0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c` |
| M326 `SHA256SUMS` | `a1ea699e4086cb967875c9408f586afc0854c85096a278e32eed9697b5ba2a2a` |
| M329 `SHA256SUMS` | `6f3c67dadba4475b70f3372f4b61be575f917f463dd3c62db1afc14813aa11df` |
| M323 `slpf_k7_h2_guard.py` | `4a00e3d5e74c7d92ba5f95bdbde447a33f1ef327d9625a40445be101f4f81bc1` |
| M323 `slpf_k7_h2_results.json` | `134de6bd6972654bf3b264ef6dac94744007b735f18bc1955b03061e83cf7821` |
| M297 `SHA256SUMS` | `a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792` |
| M297 `bodt_k9_probe.py` | `9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73` |

M323's 15/15 rows and M329's 7/7 rows pass their manifests. M326's ten
payloads were independently rehashed using M329's corrected full
`run_manifest.md` digest. No broader predecessor chain was opened or imported.

The computation SHA-gates every object in this table before loading the
permutation/completion primitive.

