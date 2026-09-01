# M102 plan: central-double bulk defect

Date: 2026-08-12. Scope: frozen M94/M100 balanced family only.

## Objective and status discipline

Use permutation convention `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right.  For `n=3k`, odd `k>=3`, the target is the uniform law on
minimal length-`n-1` transposition factorizations of the long cycle and the
kernel is M73's nonlazy rank-two pair-product quotient kernel.  Decide the
M94 scalar obligation

```text
|Delta_k(E_k)| >= c/k^2                              (BD)
```

eventually, where `E_k` is the invariant double-target event with all four
cyclic support gaps at least `(k+1)/2`.

## Method

1. Reconstruct M94's exact channel-combined gradient/embedding formula and
   express the event response by residual support-gap compositions.
2. Seek a uniform Riemann-sum limit for `k^2 Delta_k(E_k)`, including boundary
   layers and the jump in the conditioned-Borel split law.
3. Prove the limiting constant is nonzero by an analytic sign/dominance
   argument or certified interval bounds.  If it vanishes or changes sign,
   identify an exact countersequence/asymptotic.
4. Use deterministic finite calculations only to check formulas and guide
   decomposition; no conclusion will be based on `k<=11`.
5. If `(BD)` is proved, record only the consequence that `(BA2)` is refuted;
   direct signed `L1`, H0, the identity heat-bath gap, and both Terminals stay
   open.  Attack a direct shell envelope only after the scalar decision.

## Falsifiable deliverables

- a proved nonzero limiting integral or eventual lower bound for `(BD)`;
- a proved zero/countersequence refuting `(BD)`; or
- a strictly sharper exact asymptotic reduction with the first missing
  uniform/sign estimate isolated.

The mission will retain a halfway checkpoint, analytic proof/obstruction,
compact reproducible diagnostics if used, a nine-field report, hashes, and a
clean cache/status record.  No files outside this owned directory will be
edited.
