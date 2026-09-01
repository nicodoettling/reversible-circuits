# M25 plan: rare-macro closure under the full chain

## Objective

Use `(pq)(x)=p(q(x))` and the original lazy exact `r=3,4,5` heat-bath chain.
Start from the M22 macro consisting of a connected size-three weight-four
component and a connected complementary component.  Enlarge it far enough to
absorb every same-macro color move and every merge, split, or repartition move
which does not reach connected full support.  Test the resulting globally
oriented cut with exact stationary mass and complete kernel normalization.

## Strongest explicit macro closure

For `N>=5`, retain `L=N^3` and `m=4(L+1)`.  Let `A_N` be the whole rare macro
(all label choices, internal words, and color interleavings).  Define

```text
U_N={w: the support graph of w has at least two components},
```

counting isolated labels as components.  This contains `A_N` and every
possible disconnected macro, so it is the maximal proper union of complete
macro-fibers before adding the unique connected full-support macro.  It is
strictly stronger than a one-step halo.

## Proof route

1. Check the dense hypothesis `m-2>=4 binom(N,2) log(2N)` exactly.
2. Audit and specialize the frozen M12 exact-partition trace theorem:
   `W_{c+1}/W_c<=4/N^4`, global orientation of `U_N`, and exact mass formula.
3. On the boundary layer `c=2`, count safe adjacent squares whose deletion
   keeps the exact partition, refresh them across the component cut through
   an actual padded `H_3`, and recover the exact lower bound
   `(N-1)/(128M^2)`.
4. Keep `Q_4,Q_5` explicitly as nonnegative boundary flow.  No rejected-exit
   or projection kernel replaces the original chain.
5. Identify the next closure.  Since `c=1` is one unique macro datum, every
   larger proper cut must split the full-support macro internally; this is no
   longer a macro/color closure question.

## Failure modes to audit

- Confusing a missing-label cut with graph disconnection: the rare macro uses
  every label, so M23's `X>=1` cut does not contain it.
- Treating a macro transition as a word-chain probability.
- Omitting exact-partition color interleavings or parity modes in layer mass.
- Applying the dense theorem outside its hypothesis.
- Inferring a global gap lower bound from one cut family.

## Computation

No new computation is needed.  The frozen theorem has exact finite
calibrations; the present work is an audited specialization and closure
interpretation.
