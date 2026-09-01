# M111 plan: fresh referee of M108

Date: 2026-08-12.

## Objective

Independently referee the frozen M108 direct comparison from the lazy raw
adjacent-pair bridge chain to the complete micro-pair chain.  The audit target
is the uniform fixed-endpoint bridge

```text
Omega_(2l)(h)={t in T_N^(2l):t_1...t_(2l)=h},
```

with `(pq)(x)=p(q(x))`, `N>=3`, `l>=2`, and feasible `h in A_N`.

## Checks

1. Verify every frozen M108 hash before using the report or proof note.
2. Reconstruct the raw `J`, aligned `B`, and complete-pair `C` kernels,
   including laziness and scan coefficients.
3. Audit arbitrary-endpoint connectivity and the spanning-tree constants for
   the three-scan two-letter heat bath on every four-letter fiber.
4. Recompute the conditional Poincare, aligned-window overlap, M16
   normalization, and final comparison coefficients.
5. Check edge cases, M67 supersession, and redundancy versus the accepted
   direct `K -> B -> C` route.
6. Run a new deterministic, no-predecessor-import matrix checker only on all
   four-letter endpoint fibers in `S_3,S_4` and on the decisive global cases
   `S_3,l=3,h=id` and `S_4,l=2,h=id`.

## Decision rule

Return `ACCEPT` only if the proof is valid with its exact scope and no
material objection.  Finite matrices are falsification checks, not a
universal proof.  Neither Terminal is in scope.

