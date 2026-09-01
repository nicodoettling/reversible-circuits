# M241 checkpoint

Date: 2026-08-13 UTC.

## Initialization

- Owned directory and plan were created before mathematical derivation.
- The project skill and required source-of-truth documents were read.
- M226/M229 were inspected as immutable accepted inputs. M232/M239 were
  inspected only as interrupted/unaccepted candidate reductions.
- Scope is locked to R1--R3. YCM and every excluded downstream statement
  remain open unless all three lemmas and their exact sufficiency are proved.

## Immediate actions

1. Complete and record predecessor checksum/hash verification.
2. Reconstruct the exact R1--R3 formulas and domains without inheriting
   unquantified `O(.)` statements.
3. Attempt explicit ratio-product bounds, then use compact exact diagnostics
   solely for falsification.

## Immutable-input verification

- M226's complete frozen inventory passes; its `SHA256SUMS` digest is
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`.
- M229's complete frozen inventory passes; its `SHA256SUMS` digest is
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.
- Interrupted M232 snapshot hashes are
  `42530e2f07a16d2a6c0049ab1dab35075efacb3589d748a70a5e321353386b4a`
  (`plan.md`) and
  `f71c2697c53d8d48b8ad71369ef5e4e84341d45106fe8e129725351bf5656450`
  (`checkpoint.md`).
- Active-unaccepted M239 snapshot hashes are
  `4f235d97a70d8b3bed1f77ffdadef92362587ef5e9b82b528fbbdcc25ba06ea8`
  (`plan.md`) and
  `4763a336240b1232e432d9012b85c3aad42f77468d9f8a3e5b7af1646b4a4c75`
  (`checkpoint.md`).
- Source commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.

## Substantive theorem status

All three assigned scalar estimates now have analytic proofs with explicit
constants on their exact candidate domains.

- **R1:** for odd `k>=3`, `j=(k-1)/2`, `D=2k-1`,
  `L=(3k-1)/2`, `j<=x<=L-1`, and
  `1<=s<=min(j,D-x-2)`,

      b_x b_(k-s)/(b_k b_(D-s)) <= 36.

  The recurrence `rho_n=b_(n-1)/b_n` is decreasing for `n>=2`, so the
  bracket is maximized at `x=s=j`. An explicit two-sided Stirling envelope
  independently gives the displayed constant.
- **R2:** on the SG domain `1<=x<=k/4`, the stronger absolute aggregate
  smooth comparison satisfies

      sum_(s<=j) q_s |a_(D-s)(x)-(D-s)/R|
        + sum_(2x<=s<=j) q_s |a_s(x)-s/R|
      <= 34(x+1)/k.

  Here `a_r(x)=((r-x-1)/R)b_(r-x)/b_r`. The product formula for
  `b_(r-x)/b_r` and `0<=log rho_n<=2/n` give a uniform pointwise estimate
  whenever `r>=2x`.
- **R3:** on the same domain, with empty strips interpreted as zero,

      sum_(x<s<2x) q_s s/R <= 42 sqrt(x)/R,
      sum_(x<s<2x) q_s a_s(x) <= 28 sqrt(x)/R.

  The actual-mass proof cancels the `b_s` denominator before applying the
  Borel/Stirling tail bound.

These statements suffice for the named GG2 positive-convolution step and
the smooth/strip portions of SG. The mission will not claim YCM: its exact
assembly also includes survivor and coefficient-region estimates outside
the three assigned lemmas and belongs to M239/fresh audit.
