# M329 final report

Date: 2026-08-14 UTC

## Integrity verdict

```text
ACCEPT THE APPEND-ONLY CHECKSUM SALVAGE.
M323 MATHEMATICAL VERDICT REMAINS REJECT.
```

The sole M326 freeze defect is a one-character omission in its
`run_manifest.md` checksum row. Independent recomputation gives the corrected
row:

```text
a27542054b7af7ed7bff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4  run_manifest.md
```

All nine other M326 payload rows match independent recomputation. M323's
assigned top digest and all fifteen of its payload checksums also verify.

## Unchanged material objection to M323

1. **The frozen package certifies no non-Touch A endpoint.** The M323 checker
   filters the bad B atom but aggregates and discards the raw A-side slots.
   Because `Exc_pf` is the OR of the A- and B-endpoint Touch predicates, the
   exact positive bad-B-prefix mass does not by itself exhibit a token outside
   `Exc_pf`. Therefore M323's claimed off-exception `S_pf` failure remains
   rejected.

The exact B-side rank obstruction and its positive mass survive only
conditional on a positive-weight A raw partner outside `TouchSigma`.

## Exact append-only mathematical salvage obligation

With M326's fixed cell and bad B atom, define

```text
N_A=sum_P a_(1,1)(P)
    sum_(xi_A over the raw fiber (s=1,P))
       Pr[xi_A|s=1,P] 1[not Touch_Sigma(xi_A)].
```

The missing assertion is exactly `N_A > 0`, equivalently an explicit A raw
marked atom with positive residual and conditional weights whose marked owner
and support-head sets both avoid `Sigma`. M329 neither searches for nor proves
such an atom.

No downstream theorem or additional M323 claim is promoted.

