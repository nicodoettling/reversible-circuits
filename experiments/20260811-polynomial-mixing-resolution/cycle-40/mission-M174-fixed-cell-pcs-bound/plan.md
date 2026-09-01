# M174 plan: fixed-cell PCS coefficient bound

Date: 2026-08-13 UTC.

## Objective

Continue the accepted M161/M166 and M168/M171 fixed-cell frontier and attack
only the scalar statement

```text
(PCS-bound)     k * |sum_y z_k(y)| = O(1),            k odd.
```

Here `z_k(y)` is the exact signed fixed-cell component moment defined in the
accepted predecessor convention. The proof must start from the exact PC/PCS
component-moment formula, preserve the triangle/double decomposition and both
signed source channels until the final sum, and seek a closed cycle-index,
generating-function, or Borel expression giving a rigorous uniform or
asymptotic coefficient bound.

## Work program

1. Verify frozen predecessor hashes and reconstruct the exact definitions,
   normalizations, and claim ledger from M91, M94/M100, M155/M159,
   M161/M166, and M168/M171.
2. Write `sum_y z_k(y)` as one explicit scalar coefficient/extraction problem
   without taking absolute values channelwise.
3. Preserve separately until the final algebra:
   - triangle versus double PC/PCS components;
   - both source channels and their signs;
   - odd-`k` parity and all normalization factors.
4. Seek a closed exponential generating function, Borel transform, or
   cycle-index identity. Prove a uniform `O(1/k)` coefficient estimate, or
   derive the sharpest rigorously falsifiable scalar coefficient lemma.
5. Use deterministic exact arithmetic only for calibration, capped at odd
   `k<=7`. Finite signs or positivity are not promoted to an asymptotic claim.
6. Freeze a nine-field report, proof, compact exact artifacts, hashes,
   provenance, and repository hygiene; request fresh independent review.

## Falsifiable outcomes

- **Proved:** an explicit constant `C` and threshold (or all odd `k`) with
  `|sum_y z_k(y)| <= C/k`.
- **Refuted:** an exact analytic or coefficient family for which
  `k|sum_y z_k(y)|` is unbounded.
- **Strict reduction:** a closed scalar coefficient formula plus a narrower
  named coefficient bound whose proof would imply PCS-bound.
- **Exact obstruction:** a sign/channel term missing from the predecessor
  proposed cancellation, invalidating the stated PCS reduction.

## Scope exclusions

Do not attack FD-bound. Do not form broad quotient matrices, run shell scans,
or infer asymptotics from finite positivity. No direct `L1`, `H0`, spectral
gap, original heat-bath mixing, or Terminal conclusion is allowed.

## Reproducibility

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Any exact calibration uses Python 3, rational/integer arithmetic,
deterministic ordering, `seed=null`, no nonstandard dependency unless
recorded, and odd `k<=7` only.
