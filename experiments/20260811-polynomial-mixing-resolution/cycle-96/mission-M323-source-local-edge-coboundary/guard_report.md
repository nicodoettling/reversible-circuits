# M323 sole exact `k=7,H_2` guard report

Date: 2026-08-14 UTC.

Verdict: **refute frozen `S_pf` on an actual nonexceptional residual token.**

## Reproduction

```text
python3 -B slpf_k7_h2_guard.py \
  --repo /home/nico/projects/research_projects/reversible_circuits \
  --output slpf_k7_h2_results.json
```

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: 3.12.3.  Dependencies: standard library only.  Seed: none.

The script SHA-gates frozen M297 at top digest
`a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792`
and primitive-script digest
`9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`.

## Exact result

The guard uses only `k=7,n=21,H_2`, with exact rational arithmetic.  It
reconstructs the eight quantile cells and the raw source prefixes solely to
answer the predeclared support question.  The corrected normalization is

```text
c_H=46/17.
```

It finds 420 nonexceptional positive-residual raw-slot/cell incidences for
which the product-fixed opposite-source prefix is invalid.  The first exact
witness is recorded in `analytic_obstruction.md` and in full machine-readable
form in `slpf_k7_h2_results.json`.

The decisive facts are

```text
cell                         (1,1)
first/second edge            (6,14), (3,5)
marked-owner/seam contact    empty
support-head/seam contact    empty
source-A ranks               18 -> 19 -> 18
positive token mass          22000000000/91400180095887.
```

Thus `S_pf` is undefined off `Exc_pf`; no weight comparison is needed.
The count 420 and all displayed values are exact finite facts only.  The
guard ran no other rank, row, surgery, edge norm, or MPCF test.
