# M87 checkpoint: frozen M82 audit

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen gate

The assigned hashes match exactly:

```text
0df7639c4460ebb428ab44d8e039dffa48f56fcc7c4706adf716254dc2a1ba53  report.md
20ed2e03ebf964f78a7e1e13c7c86c48009ff8b44c9836ed05a0c34a6be327cc  SHA256SUMS
```

`sha256sum -c SHA256SUMS` returned `OK` for all ten entries. No M82 or
shared file was edited.

## Independent exact reconstruction

The owned harness imports no predecessor experiment code. It reconstructs
`rho`, the contextual mean, negative-hypergeometric inheritance, the
canonical basin current/capacity, `D`, `J_can`, and finite-DAG elimination.

- Root masses normalize and contextual means equal `q_x` exactly.
- Every retained deep/reset edge strictly lowers `P=s+K-R`.
- Every reset target is right-heavy.
- The reachable contextual closure is exactly `(1,0)` or `K>R>=1`: for a
  desired `(s,K,R,B)` with `K>R>=1`, start from
  `(s+K-1,1,0,B)`, use composition `(1^(K-2),s+1)`, part count `K-1`,
  and inherited rank `R`.
- Grouped Cayley sums equal direct composition sums in 1,620 exact checks
  over 810 contexts (`s<=7,K<=4`, all `R,B`, and `d=0,1,2`).

## Decisive results so far

The analytic split-mass proof is valid. For `a+b>=3`, `q(a,b)<=2/3`; the
excluded `(1,1)` pair has `q=1` but produces only discarded local rank one.

The independent full rank-eight scan reproduces all 1,015 contexts, all
four maxima, and all failure counts. In particular the first eliminated
unweighted failure is exactly

```text
x=(6,8,1,2),
K_reset 1=1205648301042298686456011/
          1135274399078805562500000>1.
```

It is not right-heavy. There are zero right-heavy, multitype-bound, or
weighted-eliminated failures in that finite scan, which remains finite
evidence only.

The raw constant and `d=0,d=1` counterexamples reproduce exactly. The
independent rank-120 `d=2` floor audit also matches M82 exactly:

```text
deep terms/floor:  1123 / 9035810685106442828848365141114545
reset terms/floor: 8214806 / 5572770673503574703458209485091641
lower bound:       14608.581358610018...
parent:            14550.287347995294...
positive margin:   58.29401061472363...
```

Every summand is nonnegative, so individual `10^-30` floors give a rigorous
lower bound. The full exact rational margin in `independent_audit.json` is
positive.

## Provisional decision

No material objection has emerged. The implication from the still-open
`K_reset W<=W` to reset-epoch mass at most `3` and occupation at most
`3eP^3(1+log P)` is algebraically valid. M82 consistently labels the
antecedent and every `Pbar`/ROOT-MEAN/original-chain conclusion unresolved.
The provisional referee decision is `ACCEPT`, pending final artifact and
hygiene checks.
