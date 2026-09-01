# M103 checkpoint: exact target reconstructed

Date: 2026-08-12. Scope is the auxiliary nonlazy minimal-long-cycle parking
projection only.

The exact paired block is

```text
(I+Q)r_U=U-A-QA-Q^2U.
```

For a right-heavy context `(s,K,K-1,B)`, the frozen attachment law
concentrates at `j=k` as `K->infinity`.  Therefore, writing `r_infty(s,B)`
for M98's exact one-layer limit and `m_(s,t)` for the stationary last-part
mass, the independently derived limiting block is

```text
b_infty(s,B)
 = r_infty(s,B)
   + sum_(t>B, t-1>=2) m_(s,t) r_infty(t-1,B).
```

The accepted M98 family `(s,B)=(16,4)` is compensated and is not a two-layer
counterfamily. The universal condition is nevertheless **refuted exactly**
at the fresh reachable context

```text
(s,K,R,B)=(30,1,0,10),
(I+Q)r_U=-.00015148647363284748...<0,
(I+Q)r_U/U=-.006914605163495121... .
```

Every attachment rank `j=1,...,k` is retained in the standalone exact
certificate. The complete weighted and unweighted resolvents still have
positive exact margins at the witness, so both universal full-excursion
frontiers remain unresolved.
