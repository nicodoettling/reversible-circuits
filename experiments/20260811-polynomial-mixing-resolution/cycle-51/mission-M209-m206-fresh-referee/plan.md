# M209 plan: fresh immutable referee of M206

Date: 2026-08-13 UTC.

## Objective

Independently audit frozen M206's exact slack-ladder reduction. Return a
binary `ACCEPT` or `REJECT` verdict with numbered objections.

## Ownership and immutable gate

- Own only `cycle-51/mission-M209-m206-fresh-referee/`.
- Never edit M206 or any accepted dependency.
- Before reading M206 conclusions, verify its exact inventory and every
  payload hash, then verify the accepted dependency ledgers it cites.

## Audit targets

1. Derive from definitions, with signs explicit,
   `(1-q)-T_1=S_1+S_2+S_3-X`.
2. Independently prove universal suffix-zero annihilation at `B=2` and hence
   actual fresh-parent `T_h1=0` for every `L`.
3. Reconstruct the complete actual-history rows `(B,L)=(2,4),(3,4)` with a
   compact standard-library `Fraction` checker importing no predecessor.
4. Verify exact terminal payment at `B=2`, exact terminal-only failure at
   `B=3`, and exact finite cumulative `h=1,2` payment there.
5. Audit orthogonal sector additivity and the absence of literal
   cross-sector Gram cancellation, while preserving all within-branch cross
   terms, covariance subtraction, and killed `a=d`.
6. Check logical reach: cumulative slack-ladder lemma only; no universal
   two-rung result or contraction theorem.

## Scope and method

No additional rows, parameter scan, generalization, tail theorem, total AMV,
gap, mixing, or Terminal inference. Use exact rational arithmetic and a
clean-room literal-composition history recursion.

## Deliverables

Durable substantive checkpoint; independent proof audit; no-import checker
and machine-readable results; nine-field report with numbered objections;
freeze manifest and SHA ledger.
