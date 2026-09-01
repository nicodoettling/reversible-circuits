# M161 freeze manifest

Date: 2026-08-13.

The immutable reviewed package is the six files listed in `SHA256SUMS`.
`SHA256SUMS` and this manifest are excluded from their own recursive hash.

```text
plan.md                       edaff6ad22304dc8c3af96c52eb301f441f9bf68186e33cfb6cf2a8868f28a1b
checkpoint.md                 5474dd25cee84c7ddd94cc3f6de89d07d72ab3013f3328919f74337d16b8849b
fixed_cell_convolution.md     f7d5369f58cf1e0f2aa34caf237fdc907a4012f15b49d5cff1ea9d3465517d09
fixed_cell_exact.py           76dc00d59326f0a1aecad0f3aff16d4b421a95acd88553a5b92b02a620c5331d
fixed_cell_results.json       7295dcbf6cec4a6b1a0a8d67f09add532bbcf66f13e717f441899110df271e19
report.md                      d7a4270525b307f86940cc07c0707a56c1086d489d45edfd96f1474a55dfe71e
```

Verdict frozen: **exact fixed-cell convolution reduction; asymptotic
boundedness unresolved; fresh audit required.**
