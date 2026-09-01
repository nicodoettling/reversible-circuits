# M215 Checkpoint

## Start checkpoint

- The owned M215 directory and plan were initialized before substantive work.
- M211 is immutable and has not yet been used; its complete hash gate is next.
- The audit is limited to the claimed pointwise IKBE-b asymptotic witness.
- IKBE-a/DV, signed averaged DE, conditional J=2, and every downstream claim
  remain open at start and outside this audit's promotion scope.

## Immutable gate

- sha256sum -c SHA256SUMS passed for all eight frozen M211 artifacts.
- Every fresh file hash agrees with M211's manifest; the SHA256SUMS digest is
  79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225.
- The immutable gate is complete. M211 remains unedited.

## Halfway substantive checkpoint

- Independently set D=2k-1, R=2k-3 and
  W_r(f)=sum_(d<r)(r-d-1)b_d b_(r-d)f(d)/(R b_r).
  Regrouping the frozen M199 formula gives the same B/A decomposition used
  by M211, with exact denominators h(s)+h(D-s) and
  h(s)+h(k-s)+u.
- On k=12q-1,s=3q,l=4q, the two-seam atoms give exactly
  F_l(s)=1-s/D and F_l(D-s)=0. The contiguous law gives
  J_l(s)=1-s/k and J_l(k-s)=0.
- A clean-room tail proof uses c m^-3/2<=b_m<=C m^-3/2.
  For M<d<=r/2 the W tail is O(M^-1/2); for d>r/2, writing c=r-d,
  it is O(R^-1 sum c b_c)=O(k^-1/2). Fixed d then gives
  W_(rho k)->(rho/2) beta.
- Independently, the tree equation T(z)=z exp(T(z)) at z=e^-1 gives
  sum_d b_d=T(e^-1)=1, so beta=sum_(d>=2)b_d=1-e^-1.
- The B kernel limits beta/8+7beta/8 and A limits
  beta/8+3beta/8+beta/2 are equal. Denominators tend to one.
  The remaining terms are 49/64 and 42/64, hence defect 7/64, while
  sqrt(l)/k tends to zero.
- No material objection has emerged. This derivation refutes only pointwise
  IKBE-b/the IKBE conjunction; IKBE-a/DV and signed averaged DE remain open.

## Final checkpoint

- The independent q=1 formula-only checker passes and reproduces M211's exact
  rational defect, approximately 0.09224121091748724.
- Verdict: ACCEPT M211's refutation, with zero material objections and two
  nonmaterial exposition qualifications.
- The universal conclusion rests on the clean-room Borel-tail derivation and
  exact 7/64 limit, not the finite calibration.
- M211 remains immutable. IKBE-a/DV, signed averaged DE, conditional J=2,
  and all downstream claims remain open.
