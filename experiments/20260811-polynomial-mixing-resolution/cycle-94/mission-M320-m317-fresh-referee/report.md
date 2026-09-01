# M320 final referee report

Date: 2026-08-14 UTC

## Frozen verdict

```text
ACCEPT M317 AT ITS STATED ANALYTIC SCOPE.
MATERIAL OBJECTIONS: 0.
ACTUAL d>=6 HPRN/APOH/SPBE/PHTC/WRAD: UNRESOLVED.
```

M317's assigned top digest and exact ten-payload inventory authenticate.  All
79 payloads in every cited predecessor ledger independently authenticate
against the actual frozen inventories.

## Material objections

None.

## Nonmaterial objections and clarifications

1. **M296 top-digest transcription typo.**  M317 displays
   `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeebe3fe86968514990d1f7f`.
   The independently verified M296 top is
   `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`.
   All seven M296 payloads pass.  No gate or theorem input depends on the
   mistyped string, so this is provenance wording only.  Frozen M317 remains
   unchanged.
2. **HPRN shorthand is contextual.**  Its phrase “inverse-polynomial weight”
   should be read with the same universal `B,C`, all-weighted-instance
   quantifiers, positive anchor, and exact bound
   `lambda(G_I(U))>=||lambda||_1/d^C` stated immediately above in SPBE.  With
   that inherited reading, `HPRN+APOH=>SPBE` is complete.  A future standalone
   quotation should restate those quantifiers.

## Accepted mathematical content

The residual common intersection is exactly a full tagged tuple-orbit, hence
exactly extension of the partial prescription in `H_I`.  Equality preservation
is well-defined injectivity; single signatures, pair intersections, and the
common intersection form the exact point-/pair-/full-orbit ladder.  Witness
and frame changes preserve the predicates by uniform translation/conjugation.

SPBE retains the positive-weight anchor, universal polynomial exponents, the
whole `G_I(supp(lambda))`, and the anchored score maximum, so its implication
to PHTC and then WRAD is valid.  The Sym completion and the Alt two-unused-point
parity correction are exact, and are correctly firewalled from the actual
action.

The two `d=3` facts are reproduced exactly: conflict independence does not
force complete pair compatibility, and `[0,2,9]` is pairwise intersecting with
empty triple intersection.  M317 correctly says neither boundary fact refutes
actual `d>=6` SPBE/PHTC.

HPRN supplies heaviness and pair compatibility; APOH supplies the full
orbital-preserving extension.  Neither is proved for actual `d>=6`.

## Stopping line

No `d=6` guard, alternate grouping, new rank, or theorem search was run.  No
actual `d>=6` WRAD/MRAD/SSTID, literal route, congestion, spectral gap,
mixing, or downstream theorem is inferred.
