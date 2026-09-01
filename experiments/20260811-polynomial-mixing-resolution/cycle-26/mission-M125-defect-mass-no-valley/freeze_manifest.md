# M125 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: exact defect-mass no-valley reduction.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **PROMOTE** the exact cycle-type/incidence-species recurrence and its
proved multiset aggregation; **REFUTE** ULC at `d=4`; **KEEP OPEN** ordinary
log-concavity and DEFECT NO-VALLEY.  Exact rows are unimodal and ordinarily
log-concave through `d=22`, but this is finite evidence only.  No spectral-gap,
original-chain, or terminal result follows.

Target: `rho(kappa)=|C_kappa|/Z_inc` on M113/M118's realizable connected-
unicyclic keys, under `(pq)(x)=p(q(x))` with tuple factors multiplied left-to-
right.  The unnormalized coefficient is
`M[d,r]=sum_{R(kappa)=r}|C_kappa|`, not a mass under the original word law.

## Frozen payload

| file | SHA-256 |
|---|---|
| `plan.md` | `a2c14376339601ab84eb61d54b8568f1a32d2600209a30854096e4c18b434988` |
| `checkpoint.md` | `eac1b8ade7e966cbb72e44c78371da691d1183eaa86b2c19b3aa6e38a0252c23` |
| `defect_recurrence.md` | `068a42ed4c9141cbabd81ffe35d352c833b634a295a9a6a6f44dabbeb09ffde1` |
| `defect_species.py` | `74cd0159ac62404db172ff3830a1ef58f9f7a105eb2f595b438af66c24c3dde9` |
| `run_exact.py` | `0fd1d2e87db67fa3d1adbdff45b3ec7858ce29b8a3e3374d7495efce588810ce` |
| `audit_recurrence.py` | `0061794c17ae1e2ea3e374adf03dc923fc7d2283f0ba59b80617b9299ec0bb62` |
| `exact_results.json` | `01938aab9d001597991d13efb3dd0583d61b629c776cfcd2f4ccfde023588131` |
| `audit_results.json` | `b33f8c39961d2080ff01c71b882c5df229766f94ae7f1daac78fc7747f63bfb6` |
| `report.md` | `dc8f8cb0ab9c6c06f9b49cd56a30b29cc258698dcdfccceb887b265ff67c5879` |

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

All four dependency `SHA256SUMS` files passed independently before freeze.

## Reproduction and validation

From repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/audit_recurrence.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/audit_results.json

python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/run_exact.py \
  --d 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/exact_results.json
```

Environment: Python `3.12.3`, standard library only, deterministic
`seed=null`.  Validation completed:

- the multiset recurrence equals the original indexed-subset recurrence and
  direct set-partition pairs for every cycle type through `d=5`;
- exact raw rows equal frozen M124 through `d=5`, and primitive rows equal the
  independent `d=6,7` stress values;
- all 21 exact rows `d=2,...,22` are unimodal and ordinarily log-concave;
- the first ULC failure is exactly `(d,r)=(4,1)`, with cleared primitive
  margin `-481004`;
- the weakest tested ordinary ratio is exactly recorded at `(22,7)` and is
  strictly greater than one;
- all Python parsed, both JSON artifacts parsed, and `git diff --check` was
  clean for the owned directory;
- no Python cache directory remained at freeze time;
- no package was installed and no file outside this owned directory was
  edited.

`SHA256SUMS` hashes every payload above and this manifest; it intentionally
does not hash itself.
