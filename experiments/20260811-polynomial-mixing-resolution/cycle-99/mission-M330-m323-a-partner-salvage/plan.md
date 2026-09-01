# M330 plan — fixed-cell A-partner salvage

Date: 2026-08-14 UTC

## Objective

Decide exactly the sole M329 salvage obligation `N_A > 0` for M323's frozen
bad-B-prefix witness. This is an append-only finite certificate; M323, M326,
and M329 are immutable.

## Declared finite measure and universe

This is not a sampler or an asymptotic claim. The target measure is exactly the
frozen A-side raw residual/completion measure in the following single profile
fiber:

```text
k = 7
type = H_2
quantile cell = (s,t) = (1,1)
B witness: e=(6,14), f=(3,5)
Sigma = {0,1,6,14,20}
```

The sole finite universe is the A-side raw residual fiber over this cell,
paired with that fixed B atom. Retain every raw marked slot, its residual and
completion probabilities, marked-owner set, support-head set, and exact
`Touch_Sigma` predicate. Use exact rational arithmetic only.

## Immutable gates

Before opening any raw-profile script:

1. this plan and `checkpoint.md` are initialized;
2. lock M323, M326, and M329 by their top `SHA256SUMS` digests;
3. identify and lock only the minimal raw-profile source required by M323.

No predecessor file may be edited.

## Fixed decision rule

Compute exactly

```text
N_A=sum_P a_(1,1)(P)
    sum_(xi_A over raw fiber (s=1,P))
       Pr[xi_A|s=1,P] 1[not Touch_Sigma(xi_A)].
```

- If `N_A>0`, exhibit the first explicit non-Touch A atom, its exact weights,
  and the exact product token mass with the frozen B atom. Verify both endpoints
  lie outside `Exc_pf` and invoke only the already-frozen B rank obstruction to
  conclude that `S_pf` is undefined there.
- If `N_A=0`, freeze that exact finite refutation.

## Scope firewall

No other rank, cell, type, surgery, pairing, or search is allowed. No MPCF,
Borel-scale, mixing, or downstream theorem follows. The final package must
request a genuinely fresh immutable audit.

## Reproducibility

Any finite reconstruction will be a single deterministic exact-rational
script with machine-readable output, an explicit command, repository commit,
and no random seed.

