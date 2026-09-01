# M101 plan: fresh referee of frozen M97

Date: 2026-08-12.

## Objective and frozen package

Independently audit M97's tree--unicycle--tree genus-one cut theorem, exact
cut-refreshed lift, handle obstruction, and marked-deletion obstruction.  The
assigned frozen digests are

```text
73ab5bec4d5ba48bb1b4511099df056525fe1f6b6f1b6caa6f79b7964feb3c99  M97 report.md
6d0c28f8a4414175a3226b77fb1cff3217599f14ad707eaf5a7d3e3470babc4f  M97 freeze_manifest.md
```

The referee will issue `ACCEPT` or `REJECT` with numbered material
objections.  It will not edit M97 or shared durable files.

## Target, convention, and kernel

The audited auxiliary target is uniform on connected-support identity
transposition words of length `2d` on fixed labels `[d]`.  Permutations
compose as `(pq)(x)=p(q(x))`, tuple factors multiply left-to-right, and the
kernel is the half-lazy signed adjacent-Hurwitz walk

```text
P_d=(1/2)I+[1/(4(2d-1))] sum_i (R_i+R_i^(-1)),
R_i(a,b)=(b,bab),  R_i^(-1)(a,b)=(aba,a).
```

This is a within-fiber auxiliary chain, not the global fixed-length
heat-bath sampler.

## Independent checks

1. Re-derive the prefix-genus increment trichotomy, integrality, uniqueness,
   reverse coordinate, and strict inequality `b<h`.
2. Reconstruct the cycle-incidence multigraph and verify connectivity,
   Euler profile, and componentwise genus zero.
3. Audit the lifted stationary law and prove the operator identity `L=UPR`,
   its full spectrum statement, reducible-chain convention, and `d=2` case.
4. Verify the infinite frozen-handle family symbolically and in finite cases.
5. Verify the deletion/insertion bijection, `r`-biased forgetful law,
   polynomial multiplicity, and the exact frozen M92/M95 dependency for zero
   fibers.
6. Run an independently written exhaustive checker at `d=2,3` and, if
   feasible, exhaustive `d=4`; include incidence profiles and lift identities
   not merely M97's handle histograms.

## Expected failure modes

- a convention mismatch in the prefix or reverse handle;
- equality `b=h` surviving because the cycle argument overlooks support;
- a disconnected or multi-cycle incidence graph at an admissible cut;
- an incorrect stationary density or missing eigenvalues in the lift;
- a false singleton/reducible gap convention;
- insertion gaps or overlapping squares breaking the claimed bijection;
- relying on the unmarked family without matching its frozen dependency.

Positive finite observations will be labeled exact finite calibrations, not
asymptotic gap evidence.  No Classification-H or full heat-bath conclusion is
within scope.
