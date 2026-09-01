# M40 plan: full quadratic shell action

## Objective

Work with `(pq)(x)=p(q(x))`, the global uniform identity bridge on
`Omega(N,m)`, `m=4N^3+4`, and the literal original lazy `{3,4,5}` heat-bath
kernel.  For one universal `kappa>0`, decide every graph-neighborhood shell
`V^(a)` of the disconnected set through `a<=kappa N^2` by either proving
inverse-polynomial leakage with the correct stationary orientation or finding
a literal superpolynomial-conductance family.

## Proposed theorem and falsifiable claim

Take `kappa=1/100` and initially retain the conservative threshold
`N>=10^6`.  The claim under test is

```text
pi(V^(a))<=exp(-4N^2)<1/2,
Phi_pm^K(V^(a))>=N^(-25)
```

simultaneously for every integer `0<=a<=floor(N^2/100)`, with `a=0`
handled by the inherited maximal-disconnected-macro leakage theorem.

The only M37 step that fails formally at this scale is its union bound over
all choices of deleted windows.  Replace it by the stronger cut-multiplicity
condition: the internal outside word has more than `5a` occurrences crossing
every nontrivial vertex cut.  Deleting `a` windows removes at most `5a`
factors, so this implies the required connectivity deterministically.

## Proof work

1. Prove an arbitrary-endpoint robust-core lemma by a binomial Chernoff bound
   for each vertex cut and a union bound over only `2^(N-1)` cuts.  Include the
   `d!` loss from endpoint conditioning.
2. Recheck every M37 source/outer coefficient at `a=N^2/100`: primitive
   entropy, block-count tail, layout factors, non-isolate cuts, orientation,
   and the exact `H_5` exit probability.
3. Retain all `Q_3+Q_4+Q_5` terms in the flow identity, using only a positive
   subset of `Q_5` for the lower bound.
4. Audit primary polymer/clique-dynamics literature for a literal theorem on
   graph-neighborhood shells or boundary injection.  Record exact hypotheses
   and any mismatch; do not use a theorem without a bridge-word polymer
   factorization.

## Failure modes and self-attack

- A graph may remain cut-connected only if multiplicity counts every deleted
  core coordinate correctly; global windows can meet erased source blocks.
- Endpoint conditioning costs `d!`, so an unconditioned high-probability
  event is insufficient unless its failure exponent dominates `log(d!)`.
- M37's coefficient comparison might hide an `exp(O(a/N))` or placement term
  that becomes nonconstant at quadratic radius.
- Conductance is not monotone; the theorem says nothing about radii beyond
  `N^2/100` or unrelated full-support cuts.

## Artifacts

- `plan.md`
- `checkpoint.md`
- `resource_audit.md`
- `report.md`

No computation is planned.  Any arithmetic check would only test a stated
constant inequality and would not prove its universal form.
