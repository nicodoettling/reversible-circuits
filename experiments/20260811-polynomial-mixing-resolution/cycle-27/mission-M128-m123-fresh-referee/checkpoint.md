# M128 halfway checkpoint

Date: 2026-08-13 UTC.

The frozen M123 `SHA256SUMS` verifies completely.  Fresh reruns reproduce the
rank-five JSON byte-for-byte, the literal collision JSON byte-for-byte, and
the history scan with zero complete-mass, signed-frame, right-heavy-target,
or multitype-target failures in its declared bounded ranges.

Independent exact reconstruction currently confirms:

- the selected `s=5` unrestricted `C-O` determinant
  `-27125/235092492288` and Rayleigh quotient
  `421891/418853>1`;
- the witness direction is not centered, while the centered frame matrix is
  positive definite through `s=5` in the natural endpoint coordinates;
- the first centered generic-frame failure is at `s=6`.  For the supplied
  integer composition function `z`, its mean is `-642/16807`; after centering,
  the exact energy/norm quotient is
  `18980340276465329/18038257962480000>1`;
- the collision at `(4,1,0,1)`, both nested active basins, and the normalized
  literal ambient rate `1/30`.

The centering fact is a required scope supplement.  It does not make M123's
explicitly unrestricted theorem false, and the stronger `s=6` witness still
refutes a generic Bessel argument even after centering.  The final verdict
will keep the unrestricted, centered, success-weighted, cross-prefix, and
actual contextual-function operators distinct.

