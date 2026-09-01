# Mission M184 checkpoint

Date: 2026-08-13 UTC.
Status: halfway independent derivation complete; clean-room checker next.

- Ownership is limited to the M184 directory, and M179 has not been edited.
- M179 immutable gate passed: all seven payloads verify, its inventory matches
  `freeze_manifest.md`, and frozen `SHA256SUMS` has digest
  `edaf37e884fbd4fb970a38ce626ef850b5eac2490fa8083ed78eb92a73c2c03d`.
- The complete required project source lock was read. The frozen ledgers for
  every cited accepted dependency M109/M114, M115/M116, M147/M151,
  M157/M160, M162/M165, and M173/M177 also pass.
- A fresh `h=2` child has state `(B+1,d+2,a+1,B)` and suffix excess one.
  The accepted degree bound therefore makes its actual-history feature
  exactly affine, so `Z=0` and
  `S=E_child||Phi||^2=||M||^2+||C/sqrt(v)||^2`.
- Direct Bayes rederivation gives
  `(eta/pi)E_parent[L^2||Phi||^2]=eta E_child[L||Phi||^2]` and parent
  covariance `sqrt(eta*pi)(delta M+C)`. Thus the exact branch, divided by
  `eta`, is the claimed `2x2` form with the mean--covariance cross term
  intact; killed `a=d` is absent before taking norms.
- For `d=1,a=0`, the matrix is `diag(1/2,1/5)`. For `d>=2`, replacing
  `lambda_0` by `(d+1)/(2d+1)` is valid in Loewner order because the
  likelihood matrix divided by `lambda_0` is a second-posterior affine
  moment matrix. Independent algebra reproduces the two diagonal factors and
  the determinant numerator `P_d(x)=A_0+A_1x-A_2x^2`. It is concave on
  `0<=x<=d^2`; both endpoint factors are positive for every `d>=2`, giving
  the uniform `2/3` bound against child trace `S` (not child `T_1` or `F`).
- Reconstructing the suffix-one history gives one exceptional reset
  coordinate `u-b/2`, constant ordinary coordinates totaling at most
  `b(h-b/2)`, and one descendant coordinate
  `(1-u)Phi_0/sqrt(1-p)` with `||Phi_0||^2<=1-y`. This yields M179's exact
  actual-history envelope. The `d=1` reduction gives `S<=3/4`; convexity in
  retained `p` and Cayley-ratio bounds give `S<=1` for `d>=2`. At `B=1`,
  reset and unary targets are rank-one inactive, so `S=0`.
- Direct root/split cancellation with `n=L-2,r=d-1` gives
  `eta=c(n,r)/[(r+1)!w_(n+3)]`. The separate `n=0` row has `eta=2/3` and
  charge at most `1/4`; for `n>=1`, including `r=n`, the first moment is
  `(n+1)^n(n+2)/(n+3)^(n+1)<=3/8`, hence the aggregate is at most `1/4`.

Final checkpoint:

- `independent_exact.py` is a clean-room standard-library `Fraction` checker
  with no predecessor imports. It reports `status=pass`, `failures=[]` on
  one new asymmetric Bayes/cross-term row, eight Loewner rows, eight
  definition-level actual-history trace rows, five eta cancellations, and
  four exterior moments through `L=6`.
- `proof_audit.md` independently proves every uniform step and records two
  nonmaterial proof-detail clarifications. No material objection remains.
- `report.md` contains nine fields and an explicit **ACCEPT** verdict limited
  to the fresh actual-history `h=2` sector.

Next: remove the generated cache, perform a byte-identical temporary rerun,
then write the freeze manifest and SHA ledger. M179 remains immutable.
