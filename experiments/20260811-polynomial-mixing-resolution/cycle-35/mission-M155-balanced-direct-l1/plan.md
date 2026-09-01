# M155 plan: balanced direct two-step L1

Date: 2026-08-13.  Role owner: M155.

## Objective and exact target

Work only in the accepted minimal-long-cycle coordinate model.  Permutations
compose as `(pq)(x)=p(q(x))`, tuple factors multiply left-to-right, `n=3k`
with odd `k>=3`, and

```text
A_k=(0,k,2k),             B_k=(0,1)(k,2k).
```

Here these displays denote the accepted cyclic-gap representatives from
M91--M105: `A_k` is the balanced oriented-triangle source and `B_k` is the
strict-edge balanced double source.  The target is the exact nonlazy
rank-two cyclic quotient kernel `bar K` under the uniform minimal
factorization law of the long cycle.  Decide the family-specific statement

```text
TV(bar K^2(A_k,.),bar K^2(B_k,.)) = O(k^-2).          (L1)
```

This is not the global identity-word target and not the lazy `{3,4,5}`
heat-bath chain.

## Route

1. Reconstruct the exact signed posterior/Borel--Abel formula, including
   orbit/lift multiplicities and the shell decomposition accepted by fresh
   referees M80, M88, M100, and M105.
2. Express direct L1 as one absolute value *after* summing the two source
   channels and all target/intermediate topology colors.
3. Seek either:
   - a discrete sign/variation decomposition with telescoping cancellation;
   - a matched finite-part bound that pairs every small-Borel/collision
     stratum with its literal lower-support contribution; or
   - a rigorous event lower bound refuting `(L1)`.
4. Use exact diagnostics only for odd `k<=11`; label them finite evidence.
5. Freeze the strongest proved theorem or strict reduction.  Do not infer a
   general H0 gap, a bridge gap, an identity-chain gap, or a Terminal.

## Prohibited shortcuts and falsifiers

- no one-step `O(1/n)` estimate (already refuted);
- no BA2/L2 implication as a substitute for direct L1;
- no generic bulk continuum limit without matched boundary layers;
- no assertion that collision/triangle strata are complete without an
  exhaustive discrete topology argument;
- no termwise triangle inequality before signed channel/color aggregation.

## Deliverables

`checkpoint.md`, a proof/reduction note, a standard-library exact diagnostic
and machine-readable output if useful, `report.md`, `SHA256SUMS`, and a freeze
manifest.  A final verdict will be one of proved, refuted, or unresolved with
a strictly narrower named lemma.

