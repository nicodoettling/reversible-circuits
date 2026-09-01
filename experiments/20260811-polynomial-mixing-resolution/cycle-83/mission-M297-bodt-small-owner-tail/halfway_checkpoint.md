# M297 halfway checkpoint

Date: 2026-08-14 UTC.

- All twelve required M261/M264 through M290/M293 immutable inventories pass.
- The exact BODT positive-composition vector has been reconstructed with the
  complete coefficient `omega`, triangle factor `1/3`, double `S/N` factors
  `1/4`, all phases, owner seams, and topology incidences.
- The analytic candidate was fixed before computation: collapse the support
  anchor, then Abel-control the signed rows indexed by a small owner size.
- A new all-rank step is proved: inside every boundary state, all fields from
  owners larger than `(k-1)/2`, including their cross terms with small owners,
  have lag variation `O(1/k)`.  Hence BODT is equivalent to the strictly local
  small-owner field `(SODT)`.
- Expanding `(SODT)` produces the exact scalar profiles `H_d`,
  `C^off_(d,e)`, and `A_d`.  The first open coefficient lemma `(SOCL)` is the
  rowwise Borel estimate stated in `proof.md`.
- The sole fixed-rank calibration is `k=9`; no new rank was added.  It verifies
  the phase collapse and is consistent with the proposed row scales, but is
  not an asymptotic theorem.

No BODT, DOR, PBV/FD/FCL1, gap, mixing, or Terminal conclusion is claimed.

