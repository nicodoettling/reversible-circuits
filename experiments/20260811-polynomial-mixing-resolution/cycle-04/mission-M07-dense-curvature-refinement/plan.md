# Plan: `O(v log v)` dense Hurwitz-rate curvature

## Objective

Improve the frozen cycle-03 dense-curvature threshold from
`O(v^2 log v)` to `O(v log v)`.  The exact target is to control the connected
identity-return count at each of the three adjacent even lengths
`k-2,k,k+2` to relative error `O(1/k)`, since a constant-factor return bound
does not preserve the sign of the rate increment.

## Route

1. Use the parity-aware Diaconis--Shahshahani partition-zone estimate already
   audited in M10 to obtain a pointwise identity-return error at one
   `O(v log v)` time, then use the exact second character ratio to amplify it
   to `O(1/k)`.
2. Bound disconnected support under the *identity bridge*, rather than under
   the unconditioned word measure.  For a missing cut `A`, factor the return
   walk on `S_A x S_(A^c)`, require the larger factor to receive enough of the
   internal transpositions, and apply the same pointwise estimate there.
3. Union-bound cuts with the factorial ratio `v!/(v-|A|)!`; the missing-cut
   exponential then beats both the cut count and factorial ratio at
   `k=O(v log v)`.
4. Propagate the three errors through the two adjacent connected-count ratios
   and state the resulting curvature constant.

## Falsification targets

- A noncommutative or parity mismatch in the subgroup-return factorization.
- A small side of a cut receiving too few steps and restoring a hidden `v!`
  loss.
- An error estimate valid at one length but not uniformly decreasing at the
  next two lengths.
- `v=2,3` or the first positive genus violating a threshold inequality.

No computation can prove the universal statement; exact arithmetic will be
used only if a scalar constant check is not transparent.
