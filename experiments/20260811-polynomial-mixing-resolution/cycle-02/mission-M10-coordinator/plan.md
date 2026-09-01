# Plan: two-type path-coupling audit

## Objective

Test a named repair of the failed scalar Dobrushin argument for the adjacent
pair bridge heat bath `J`.  In prefix-path coordinates, classify a one-site
discrepancy by whether the quotient of its two transposition labels is a
3-cycle (`C`, the labels overlap) or a double transposition (`D`, the labels
are disjoint).  Determine whether any positive weights `w_C,w_D` make the
standard single-discrepancy maximal/optimal-transport path coupling contract.

This finite orbit-type calculation can falsify that two-weight coupling
criterion.  It cannot prove or refute the spectral gap of `J` or `K`.

## Exact criterion tested

Normalize `w_C=1` and put `w_D=x>0`.  For every distinct transposition pair
`t,t'` of type `q` and every preceding transposition `p`, compare the uniform
midpoint laws for the two-step products `pt` and `pt'`.  Their optimal
transport cost uses cost zero for equal midpoint labels, cost one for an
overlapping unequal pair, and cost `x` for a disjoint pair.  Let `A_q(x)` be
the maximum such cost.  The usual random-scan path-coupling drift requires

    2 A_C(x) < 1,       2 A_D(x) < x.

The factor two is for the two neighboring update sites; updating the original
discrepancy coalesces it.

## Parameters and falsification scope

Enumerate `N=3,...,9`.  The computation is deterministic (recorded seed zero
only for schema consistency), uses exact group arithmetic, and solves finite
transportation linear programs.  If incompatible explicit witnesses are
found, extract rational plans or elementary lower bounds for a proof.  Finite
success would remain nonproof of a universal contraction theorem.

## Calibration and failure modes

- Keep `(pq)(x)=p(q(x))` and ordered products.
- The two-step midpoint fiber has size `M`, `3`, or `2` for identity,
  3-cycle, or double-transposition endpoints.
- Do not infer slow mixing from failure of path coupling.
- Check both discrepancy types and all choices of the neighboring factor.
- Record SciPy/Python versions and every exact witness tuple.

