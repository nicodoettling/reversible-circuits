# M161 plan: fixed boundary cell score

Date: 2026-08-13. Role owner: M161.

## Objective and scope

Work only in the accepted minimal-long-cycle coordinate model. Permutations
compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right. For odd
`k>=3`, put `n=3k`,

```text
A_k=(0,k,2k),              B_k=(0,1)(k,2k).
```

The target is M73's exact nonlazy rank-two cyclic quotient kernel under the
uniform law on minimal length-`n-1` transposition factorizations of the long
cycle. The assigned cell is the separated double-target family

```text
t_y=(0,1,1+y,2+y),       1<=y<=n-3,
```

whose colored gaps are `(1,y,1,n-2-y)`. Derive the complete channel-combined
posterior score `z_k(t_y)` and

```text
A_k(1,1)=1/(n-3) sum_(y=1)^(n-3) k^2 |z_k(t_y)|.
```

All intermediate triangle, double, collision, and lower-support terms remain
inside the signed score before absolute value. This mission makes no direct
all-edge, H0, bridge-gap, identity-heat-bath, or Terminal inference.

## Route

1. Start from M94's accepted orbit-aware raw convolution and specialize the
   target to `t_y`.
2. Classify intermediate products by triangle and the separated/nested
   double colored-composition schemas, retaining collision degenerations.
3. Reduce the phase-averaged target response to exact finite convolutions in
   `y` and critical-Borel/completion-count variables.
4. Prove an asymptotic result if possible: a finite limit/bound, divergence,
   or an exact scalar recurrence with a sharply isolated remaining estimate.
5. Only after the reduction, run compact deterministic checks at `k=3,5,7`;
   use `k=9` only if cheap.

## Deliverables

`checkpoint.md`, a proof note, a compact standard-library checker and JSON
when useful, a nine-field `report.md`, `SHA256SUMS`, and a freeze manifest.
Every computational statement will be labeled exact finite or floating finite;
a fresh independent audit is required before promotion.
