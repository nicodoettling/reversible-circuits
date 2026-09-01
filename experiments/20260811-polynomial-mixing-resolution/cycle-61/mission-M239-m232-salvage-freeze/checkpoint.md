# M239 checkpoint

Date: 2026-08-13 UTC.

## Initialization

- Owned path initialized before further substantive work:
  `experiments/20260811-polynomial-mixing-resolution/cycle-61/mission-M239-m232-salvage-freeze/`.
- M232 is explicitly classified as **interrupted before freeze**. M239 will
  not modify any M232 file.
- The project skill and required source-of-truth documents have been read.
- M226/M229 and M232's durable plan/checkpoint have been inspected only as
  candidate immutable inputs.
- An initial top-level `sha256sum -c` invocation failed because the checksum
  inventories contain mission-relative paths. It is not counted as a
  verification result. The required verification will be rerun with each
  mission directory as the working directory.

## Scope lock

The sole target is YCM. TCM, WBE, DE, J2, all downstream gap/mixing claims,
and both Terminals remain outside this mission and open.

## Immediate next actions

1. Verify frozen M226/M229 inventories from their respective directories.
2. Hash M232's plan and checkpoint as immutable interrupted inputs.
3. Independently audit the foundational Borel/Stirling assertions before
   relying on SG/GG1/GG2 or the coefficient-region argument.

## Immutable-input verification

- M226's complete inventory passes from its own directory; its checksum-file
  digest is
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`.
- M229's complete inventory passes from its own directory; its checksum-file
  digest is
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.
- Immutable interrupted M232 inputs: `plan.md` has SHA-256
  `42530e2f07a16d2a6c0049ab1dab35075efacb3589d748a70a5e321353386b4a`;
  `checkpoint.md` has SHA-256
  `f71c2697c53d8d48b8ad71369ef5e4e84341d45106fe8e129725351bf5656450`.
- Source commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.

## First substantive audit finding

Current YCM status: **not yet proved by M232's checkpoint**. The displayed
coefficient-envelope shapes survive initial direct evaluation, but its
advertised choices `C_*=2^16` and `C_Y=2^20` do not follow from the text.

SG invokes two unquantified assertions: (i) shifted fragmentation kernels
outside `x<s<2x` differ from the no-shift comparison by
`O((x+1)/k)`, and (ii) both masses on the nonsmooth strip are bounded by an
unspecified multiple of `sqrt(x)/R`. GG2 likewise bounds

    b_x b_(k-s)/(b_k b_(D-s))

by an unnamed uniform constant before applying the weighted Borel
convolution. No numerical constant or complete ratio-range proof is supplied.

The corrected GG2 algebra is structurally sound: with `M=D-x`, its third
source is

    (k/(k-1))/R * sum_(s<=j)
      b_s (M-s-1)b_(M-s)
      [b_x b_(k-s)/(b_k b_(D-s))].

A genuine uniform bound on the bracket permits enlargement to the full
positive weighted convolution. This is the exact constant step to prove.

A preliminary direct-formula spot check at `k=9,21` found no contradiction to
SG or GG2's scales. It is falsification evidence only. Next: establish or
refute the three explicit ratio/strip lemmas; otherwise freeze them as the
first strict constant reduction.

## Post-R1--R3 assembly status

M241 is now frozen and independently verified in its own directory. Its
inventory digest is
`07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936`.
It proves R1 with constant `36`, R2 with constant `34`, and the two R3 strip
bounds with constants `42` and `28`. Its exact assembly proves

    |G_k(x)-2b_x| <= 128(x+1)b_x/k,  1<=x<=k/4,
    G_k(x) <= 70/[k sqrt(D-x)],       j<=x<=L-1.

The corrected GG2 summation domain is
`1<=s<=min(j,D-x-2)`. This discharges the three unnamed M232 ratio/strip
steps, including the survivor calculation for SG and the `x=j` survivor in
GG2.

YCM is **still unresolved in this checkpoint**. The exact first remaining
standalone inequality is the missing quantified GG1 bound:

> For odd `k>=3` and `1<=x<=j`, prove
> `G_k(x)<=C_G b_x` with an explicit absolute constant `C_G`.

This requires the short-parent convolution after `t=s-x` and the long-parent
ratio bound with `D-s>=3k/2`; neither M232 nor M241 supplies a full proof.
Conditional on GG1, the remaining audit must still quantify the small-`y` A
expansion, the B second seam atom, the middle/below/at/above-seam coefficient
regions, all four prefix ranges, and `k=3,5,7`. No claim beyond SG/GG2 is made
here until that assembly is written.

## Final assembly checkpoint

- M243's frozen inventory was verified; digest
  `99e30270a3852d53ecbdf70222f5a6490b6d12d01a4720e18745e3e30351d59b`.
  Its verdict is ACCEPT M241 with no material objection.
- GG1 is proved with `C_G=172`: survivor `<23b_x`, short-parent convolution
  `<14b_x`, and long-parent convolution `<135b_x`.
- Four all-rank coefficient envelopes are proved with constants `3000`,
  `176`, `70`, and `242` below/moving toward/at/above the seam.
- Their four prefix ranges give `6906sqrt(ell)/k`; hence YCM is proved with
  the explicit universal constant `C_Y=7000` for every odd `k>=3` and every
  `2<=ell<=(3k-1)/2`.
- The proof analytically covers `k=3,5,7`; it does not use finite computation
  to establish them.
- The clean-room exact-formula evaluation at odd `k<=21` passed every
  falsification check. Its maximum observed scaled prefix was
  `0.5185449728701349`. This is diagnostic only.
- M232 remains untouched and classified as interrupted before freeze.
- No TCM, WBE, DE, J2, downstream gap/mixing, or Terminal inference is made.
