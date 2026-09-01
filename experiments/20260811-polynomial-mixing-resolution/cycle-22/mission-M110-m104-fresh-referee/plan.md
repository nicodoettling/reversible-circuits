# M110 plan: fresh referee of M104

Date: 2026-08-12 UTC
Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Objective and target

Independently referee the frozen M104 fixed-seam decomposition.  The ambient
target is the uniform law on length-`2d` connected identity transposition
words (the genus-one Hurwitz fiber used by M97/M101), under the convention
`(pq)(x)=p(q(x))` and tuple product from left to right.  The tested claim is
the conditional fixed-cell comparison, not a claim that the global
`{3,4,5}` heat-bath chain already has a polynomial gap.

## Audit obligations

1. Verify every frozen M104 payload and dependency hash before relying on it.
2. Reconstruct literal prefix/suffix factorization and incidence counts.
3. Audit `r_L`, `r_R`, `ell`, and the integral product-mixture identity.
4. Classify internal and seam signed Hurwitz proposals without importing the
   M104 proof.
5. Derive the Radon--Nikodym, edge-form, variance, and `D^3` gap comparison.
6. Recover the generalized two-side M05 shuttle source, two identity slots,
   scan normalizations, and constants `420 D^10` and `420 D^13`.
7. Audit the `alpha beta/7` projection decomposition, positivity/PSD issue,
   conditional constant `2940 D^13`, and the `kappa_e` circularity claim.
8. Run a compact deterministic no-import checker through decisive cases with
   `d<=4`, then issue a nine-field `ACCEPT` or `REJECT` report.

## Expected failure modes

- a fixed key does not determine an exact Cartesian product;
- `ell` has hidden cross-side dependence or an off-by-one error;
- a seam proposal is incorrectly retained in a cell;
- a conductance/source-recovery bound loses an omitted scan or rejection
  factor;
- a signed or projected form is used as if it were a Markov/PSD kernel;
- the explicit `p=id` cell imports a same-size gap and therefore gives no
  induction.

## Reproducibility

Python 3.12.3, no nonstandard dependencies, deterministic exhaustive checks,
`seed=null`.  Bytecode generation will be disabled.  Exact commands, hashes,
runtime, and raw JSON will be recorded in the final report and manifest.
