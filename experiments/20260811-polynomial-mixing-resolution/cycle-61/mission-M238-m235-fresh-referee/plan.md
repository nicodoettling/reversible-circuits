# Mission M238 plan: fresh referee of M235 TCM

Date: 2026-08-13 UTC

## Objective

Perform a fresh immutable audit of frozen M235 and return an explicit
`ACCEPT` or `REJECT` verdict, with numbered objections.  The only theorem in
scope is the universal signed two-run coefficient moment

```text
|sum_(y=2)^ell c^T_(k,y)| <= 160 sqrt(ell)/k,
k>=3 odd, 2<=ell<=(3k-1)/2.
```

No conclusion about YCM, WBE, DE, conditional J2, downstream responses, a
spectral gap, mixing, or either Terminal is in scope.

## Source lock and immutability

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Frozen M235 `SHA256SUMS` digest:
  `7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527`.
- M235's seven-file inventory and all cited M192/M195, M199/M207,
  M211/M215, M217/M222, and M226/M229 inventories passed
  `sha256sum -c` before referee work.
- Frozen missions will remain byte-for-byte immutable.  M238 imports no M235
  code or data in its clean-room checker.

## Audit protocol

1. Reconstruct the literal ordered-disjoint-pair laws directly from accepted
   dependencies, with the convention `(pq)(x)=p(q(x))`.
2. Re-derive the B normalization, both parent orientations, placement
   multiplicity, both seam increments, simultaneous seam identity, and the
   cyclic-start placement bound.
3. Re-derive the A marked and untouched formulas, especially M235 (5.3), with
   repeated-size collisions counted with multiplicity.
4. Audit every convolution index/range and all constants in the B and A
   estimates, including the restricted identity `D-t=s+d` for the long
   parent and the complete `k=3` boundary case.
5. Write a clean-room standard-library checker that independently enumerates
   literal permutations and independently evaluates the formula laws at
   `k=3,5,7`, coefficientwise for every size; also test the B placement bound
   for every tuple and allowed cutoff.
6. Freeze proof audit, checker, machine-readable output, report, manifest, and
   `SHA256SUMS`.  Any material gap forces `REJECT`; nonmaterial corrections
   are recorded separately.

## Expected failure modes

- accepting a finite match as a universal proof;
- importing M235 implementation or generated data;
- losing the second parent orientation, a seam, an A channel, or collision
  multiplicity;
- using `D-t=s+d` outside the long-parent parametrization;
- extending a convolution past an empty or negative endpoint;
- accepting constants without checking the smallest odd `k`.
