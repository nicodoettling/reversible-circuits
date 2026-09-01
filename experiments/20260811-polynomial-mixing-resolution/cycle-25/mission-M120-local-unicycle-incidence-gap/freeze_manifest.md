# M120 freeze manifest

Frozen: 2026-08-12 UTC.

Mission: local connected-unicycle incidence gap.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **PROMOTE** the universal singleton-cycle split/reverse rate and the
bidirectional cycle-defect rates; **KEEP OPEN** every spectral gap.  For all
`d>=3`, every `A_d` key has singleton-split-or-reverse probability at least
`1/(64d^2)`.  The exact defect birth-death projection has downward rate at
least `1/(64d)` off its bottom and upward rate at least `1/d^3` off its top.
The DEFECT NO-VALLEY lemma, fixed-defect two-step gap, `gap(A_d)`, `beta(d)`,
and the full heat-bath gap remain unresolved.  This is nonterminal.

Target: `rho(kappa)=|C_kappa|/Z_inc` on M113/M118's exact realizable
connected-unicycle keys, under `(pq)(x)=p(q(x))` with factors multiplied
left-to-right.  `A_d` has off-diagonal stationary flow
`|C_kappa intersect C_lambda|/(2Z_inc)` and holds unused mass.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `d53593b892933b68690fc68b9071561a36bdca54c5f374c1ce571cb70ed75b65` |
| `checkpoint.md` | `a5bff43d77a568255537b4db4f2faf33c6ee6ed538cf65f647398e59671d8580` |
| `incidence_gap_audit.py` | `2649acb303c910f1d526f446572eb6fd674aa17c26c78bc175843fc76b94f368` |
| `results.json` | `9285dc8958a59cd62fccd2cd8cdc95053dd1ecb033c6a3562925962bc1af28f9` |
| `report.md` | `9f1cdd5f137b32b3ded80d951b6067565edac2ade9032d18cb0251e7c92803db` |

## Frozen dependency boundary

| artifact | independently observed SHA-256 |
|---|---|
| M113 `report.md` | `295c6d50b70117915cc99d9ebe6e1e88cbfab258a404db66a0b1543ea01cfe47` |
| M113 `freeze_manifest.md` | `64cf3bb48baca3022690cb72c5afc458e3fbf8e514b56612c099b7f9b1e0b6bf` |
| M118 `report.md` | `e780115979cfb3c281007fe62a507cd2062d1d061cd9bd2faa3f6f54a4387b3b` |
| M118 `freeze_manifest.md` | `2c1552d1df1af619cad35d86b45a369473c0852e7c9c5721c6b6e8dac0cfaf98` |

## Reproduction and validation

From repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M120-local-unicycle-incidence-gap/incidence_gap_audit.py \
  --d 2 3 4 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-25/mission-M120-local-unicycle-incidence-gap/results.json
```

Environment: Python `3.12.3`, NumPy `1.26.4`, SciPy `1.11.4`, deterministic
`seed=null`.  Validation completed:

- the exact combinatorial state spaces have `1,9,101,1420` keys;
- the `d<=4` gaps and normalizations match frozen M113 and fresh M118;
- every exact row is valid and the key graph is connected through `d=5`;
- the canonical singleton and join formulas have zero failures through `d=5`;
- exact defect masses/rates, named threshold cuts, and singleton skeletons are
  recorded in `results.json`;
- all Python parsed and the final JSON parsed;
- `git diff --check` returned clean for the owned directory;
- no Python cache directory remained at freeze time;
- no package was installed and no file outside this owned directory was edited.

`SHA256SUMS` hashes every payload above and this manifest; it intentionally
does not hash itself.
