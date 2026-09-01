# M335 final report

Date: 2026-08-14 UTC

## Verdict

```text
OBSTRUCTION PROGRESS.
REJECT THE FROZEN S_pf^* TOKENWISE COBBOUNDARY.
KEEP THE EXACT J SPLIT AND EXCEPTIONAL BOREL SCALAR REDUCTION.
```

The enlarged literal exception

```text
Exc_pf^*=Touch_A or Touch_B or BadPref_A or BadPref_B
```

removes M323's prefix-existence failure. Off this set, the product-fixed raw
source switch is a literal involution and preserves the unordered profile
pair. It nevertheless need not land in the reverse residual-product token
law.

The obstruction is structural. Within one cell the positive residual profile
supports `a_st` and `b_st` are disjoint. Thus a positive token `P->Q` cannot
be reversed as `Q->P` in the same cell. The sole exact `k=9,H_2` guard finds
an actual off-`Exc_pf^*` token for which both switched splits stay 1. Its
original weight is the positive rational `(3.1)` in
`analytic_obstruction.md`, while the required reverse masses are exactly

```text
a_11(Q)=b_11(P)=0.
```

The failure precedes weight equality and is not repaired by the enlarged
exception.

## Surviving exact reduction

- `J=J_compatible+J_exceptional` remains an exact tokenwise identity.
- The raw-label switch remains involutive and source-local off `Exc_pf^*`.
- `mass(Exc_pf^*)` is bounded exactly by the combined Borel scalar expression
  `(4.2)` of `analytic_obstruction.md`.
- Proving its target scales
  `C d b_d/k`, `C d b_d/k`, and
  `C max(d,e)b_d b_e/k` remains open.

Those scalar bounds alone would not control the surviving compatible flux.
No alternative surgery or pairing is proposed.

## Strict scope

No other rank, row, cell scan, grouping, or surgery was used. MPCF, CMPAD,
CBPV, SOCL, gap, mixing, Terminal, and all downstream statements remain open.

