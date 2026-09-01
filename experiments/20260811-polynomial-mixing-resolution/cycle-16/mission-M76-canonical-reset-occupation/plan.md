# M76 plan: canonical right-heavy reset occupation

Date: 2026-08-12.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and scope

This mission concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal factorization sector of
`(0 1 ... r)`.  It does not concern the identity bridge chain `K`.
Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.

Starting from M71's proved canonical-flow reduction, attack the exact
rank-acyclic operator

```text
(I-D)^(-1) J_can,
```

where `D` is M65's marked deep kernel and `J_can` is the M50
first-boundary canonical quotient-residual kernel.  Every row of `J_can`
lands in `K-R=1`, while `D` contracts suffix excess plus one by `3/4`.

The target is a universal polynomial bound on total normalized reset/base
energy for every ambient-feasible mark, followed by M71's one-shot
`O(r^9)` actual-edge unmarking.  If false, exhibit an exact infinite
counterfamily and determine whether it survives aggregation on unmarked
actual edges.

## Frozen route

1. Resolve a canonical edge along a source composition's first-merge path.
   Its residual child has rank `A+c_2-1` and suffix excess plus one exactly
   `A`, where `A` is the already merged prefix mass.
2. Use M50's exact basin identity and Cauchy bound, retaining this prefix
   mass rather than replacing it by `s`.
3. Sum over the exact stationary deep-descendant law from M71 and formulate
   a reset-to-reset renewal potential.  Try polynomial features in rank,
   suffix excess, and unpassed-attachment count only as falsifiable
   discovery aids.
4. Prove a universal renewal/occupation inequality or an exact infinite
   obstruction.  Finite ranks are falsifiers only.
5. If occupation is proved, aggregate histories with identical
   `(active embedding,s,K,R,B,nearest reset)` before routing and apply the
   one-shot polynomial Cauchy loss.  Audit every `alpha`, stationary-flow
   capacity, and path occurrence factor.

## Expected failure modes

- A reset may create suffix excess `A=Theta(s)` with enough squared current
  to defeat a simple linear potential.
- Polynomial rank weights alone are already refuted by M71; any successful
  potential must use suffix/reset phase information.
- A finite bounded potential need not have a universal closed form.
- Polynomially many current labels do not bound amplitudes coalescing
  inside one label unless aggregation is performed before routing.

## Deliverables

Freeze a halfway checkpoint and a nine-field final report in this directory.
Record exact scripts and machine-readable outputs for any nontrivial finite
falsifier.  State explicitly whether the result is separated marked flow,
actual unmarked `Pbar`, or only a reduction.
