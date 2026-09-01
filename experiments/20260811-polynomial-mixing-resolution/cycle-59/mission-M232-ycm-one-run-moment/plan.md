# M232 plan: YCM one-run coefficient moment

## Objective

Prove or refute the exact one-run coefficient moment

    |sum_(y=2)^ell c^Y_(k,y)| <= C sqrt(ell)/k

uniformly for odd `k>=3` and `2<=ell<=(3k-1)/2`, using the audited M226/M229 coefficients and the corrected domain `1<=x<=(3k-3)/2` for `G_k(x)`.

## Immutable gate

Verify all M226 and M229 frozen artifacts and checksum-file digests before use. Never edit either mission.

## Proof route

1. Derive a generating-function, convolution, Abel, or telescoping identity from the closed coefficients before computation.
2. Separate `y<k`, the seam `y=k`, and `y>k` exactly.
3. Treat fixed/small `ell` and bulk/comparable `ell` analytically.
4. Seek either an explicit universal constant or an infinite/asymptotic counterexample.
5. Use compact exact odd `k<=21` diagnostics only to falsify identities and calibrate, never to infer a sign or universal bound.
6. If YCM remains open, freeze the first strict scalar convolution lemma with its exact sufficiency or obstruction.

## Exclusions

No TCM, WBE, DE, J2, PCR, spectral gap, mixing, or Terminal inference.

## Deliverables

`checkpoint.md`, proof or strict convolution reduction, compact checker/results, `report.md`, `freeze_manifest.md`, `SHA256SUMS`, and a request for a fresh immutable audit.

