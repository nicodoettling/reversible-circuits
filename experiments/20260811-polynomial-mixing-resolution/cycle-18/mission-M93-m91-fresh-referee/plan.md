# M93 plan: fresh referee of frozen M91

Date: 2026-08-12.

## Objective

Independently audit frozen M91 report SHA-256
`df2983ca83c8fd92dec6406eb6341b4f07655304c491a7c74687649ceaa609ea`
and manifest SHA-256
`0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703`.
Issue `ACCEPT` or `REJECT` with numbered material objections.

## Exact scope

The candidate is only the balanced-family reduction for M73's cyclic
rank-two quotient kernel.  Audit the stationary/orbit-stabilizer factors,
posterior-score identity, `J=0` cancellation and color probabilities,
conditional-law and raw micro-lift normalization, conditioned-Borel sign and
Abel identity, the `BA2` stationary-norm/four-step contrast, exact `k=3,5`
certificates, and the positive `J=1`/`J=2` cross-term counterexample to
orthogonality.  `BA2`, balanced two-step decay, H0, the identity sampler gap,
and both Terminals remain outside any positive verdict.

## Method

1. Verify all frozen hashes and package hygiene.
2. Re-derive the identities algebraically with literal quotient orbit masses.
3. Inspect the frozen implementation for agreement with those formulas.
4. Write an independent exact-rational checker in this directory; it may use
   only elementary permutation/factorization formulas, not import M91 code.
5. Run the independent checker at `k=3,5`, compare its invariants with both
   frozen exact certificates, and record machine-readable output.
6. Freeze a nine-field referee report and manifest after removing caches.

## Failure modes sought

- treating the size-`k` orbit of `A` as a generic size-`3k` orbit;
- losing oriented-triangle versus double ordered-pair multiplicities;
- using an unnormalized conditional split law or missing a color-order lift;
- reversing the conditioned-Borel likelihood-ratio sign;
- applying Abel summation with the wrong endpoint term;
- dropping a stationary-mass denominator in the `K^4` contrast;
- identifying finite bounded values with an asymptotic theorem;
- incorrectly declaring the two channel images orthogonal.

