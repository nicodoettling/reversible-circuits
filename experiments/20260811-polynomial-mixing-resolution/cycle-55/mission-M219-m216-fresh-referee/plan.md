# M219 plan: fresh referee of frozen M216

## Objective

Independently audit the frozen M216 degree-cap diagonal Bernstein PSD-envelope construction and issue an `ACCEPT` or `REJECT` verdict with numbered objections.

## Source lock and scope

- Source mission: `cycle-54/mission-M216-full-kernel-psd-majorant/`.
- Expected source `SHA256SUMS` digest: `2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414`.
- Treat every M216 artifact as immutable.
- Audit only: degree cap `L`; diagonal Bernstein PSD envelope; saturated likelihood closure; unsaturated degree elevation and its named diagonal domination using `ee^T <= (sum e) diag(e)`; exact `eta/pi` including killed `a=d`; the necessary condition `diag(c)-A >= 0`; and the rational `B=1,L=6,kappa=2,D=1` witness with positive actual contraction slack.
- Exclude all-degree Bernstein dictionaries, arbitrary nondiagonal/Jacobi/Green kernels, any general contraction or gap/mixing conclusion, and Terminal A/B.

## Independent checks

1. Verify the frozen source inventory and its checksum-file digest.
2. Read the proof and implementation only after locking checksums.
3. Reconstruct the named rational row with a clean-room exact-arithmetic checker that imports no M216 code or data.
4. Check the claimed PSD inequalities by exact principal-minor/eigenvalue-equivalent arithmetic appropriate to the row.
5. Compare the reconstruction to the frozen report and raw results; classify discrepancies as material or nonmaterial.
6. Freeze `report.md`, proof audit, checker, results, manifest, and `SHA256SUMS`; report exact hashes.

## Claim labels and expected failure modes

- Algebraic identities proved by exact derivation/checking will be labeled `proved` within the stated finite-dimensional ansatz.
- The rational row is an exact finite certificate, not an all-parameter theorem.
- A source checksum mismatch, hidden import, incorrect killed-boundary treatment, non-PSD necessary-condition residual, or nonpositive actual contraction slack is material and forces `REJECT`.

