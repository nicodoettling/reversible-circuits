# M260 Plan — Fresh Referee of M257

## Objective

Independently referee the immutable six-payload M257 root-seam-transducer
reduction. Verify its complete inventory, top digest, predecessor gates, and
the locked DPS source before auditing the raw cyclic CP-1--CP-6 contour and
context reduction.

## Scope and prohibitions

- Treat M257 and every cited predecessor artifact as immutable.
- Reconstruct the DPS contour symbolically: `kappa(v)=L_v`, cyclic child
  order including post-wrap children, off-path substitution/commutation, the
  reversed base row, and the root-seam new child `d` with all labels.
- Check that the remaining CPR metric O/C row lemma and RST endpoint tables
  are logically separate, and that M257 makes no RSPT, IDL, fixed-edit,
  routing, gap, mixing, or Terminal claim.
- Do not run a finite replay, rank census, or numerical calibration.

## Method

1. Read the mandated project sources and the relevant frozen proof artifacts.
2. Recompute all six M257 payload hashes and the SHA-256 digest of its
   `SHA256SUMS`, expected
   `9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1`.
3. Verify every predecessor inventory/digest and the locked DPS PDF gate.
4. Parse CP-1--CP-6 from the source definitions and independently derive the
   contour/context identities, including all cyclic boundary rows.
5. Issue a binary ACCEPT/REJECT verdict with numbered material objections and
   freeze the referee proof, report, manifest, and checksums.

## Expected failure modes

- Confusing a vertex's reversed-child incidence with canonical child
  incidence, changing `kappa(v)` from `L_v` to `R_v`.
- Omitting children encountered only after cyclic wrap.
- Commuting an incomplete off-path block through the path context.
- Treating CPR or RST as already proved, or silently promoting their
  conjunction to RSPT/IDL.
- Losing the new child `d`, a root label, an empty interval, or the exhausted
  unnamed-label boundary.
