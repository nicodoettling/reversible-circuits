# M174 checkpoint

Date: 2026-08-13 UTC.

## Initial checkpoint

- Initialized the owned M174 directory before substantive predecessor work.
- Re-read the complete project skill and `GOAL_SPEC.md`; located frozen M91,
  M94/M100, M155/M159, M161/M166, and M168/M171.
- Fixed the sole target as odd-`k` PCS-bound
  `k*|sum_y z_k(y)|=O(1)`.
- Fixed the anti-loss rule: triangle/double components and both signed source
  channels remain separate until the final scalar summation.
- Fixed the computation cap at odd `k<=7`; no broad quotient matrix, shell
  scan, FD-bound work, finite-positivity promotion, or gap inference.
- No mathematical or computational conclusion has yet been made.

## Next

Verify immutable hashes, reconstruct the exact PC/PCS formula and conventions,
then derive the scalar generating-function or coefficient problem before any
calibration.

## Halfway checkpoint

Status: **proved exact scalar/covariance reduction; asymptotic bound still
open**.

- All named frozen predecessor checksum manifests pass. No predecessor or
  coordinator artifact has been edited.
- Put `P_g(s)=a(s)C_g(s)/A_g` and `f_k(s)=S(s)/A_s`. The M168 PCS and cell
  event identities collapse exactly to

  ```text
  Delta_k(C_k)=E_(P_B) f_k-E_(P_A) f_k,
  sum_y z_k(y)=2 Delta_k(C_k)/pi_y.
  ```

  Thus PCS-bound is exactly `n^2|Delta_k(C_k)|=O(1)`, because
  `pi_y=2/(n-2)(1-2/n)^(n-3)` and `n=3k`.
- Split each source pair law into M91's common `J=0` law and the two signed
  channels `J=1,2`. For
  `mu_j=(P_(B,j)+P_(A,j))/(2 alpha_j)` and
  `sigma_j=(P_(B,j)-P_(A,j))/(P_(B,j)+P_(A,j))` (zero on a zero
  denominator), the exact signed formula is

  ```text
  Delta_k(C_k)=2 sum_(j=1)^2 alpha_j
                    Cov_(mu_j)(f_k,sigma_j).
  ```

  Here `E_(mu_j)sigma_j=0`; `J=0` cancels as a measure. This is the fixed
  scalar covariance interface requested by the coordinator, and it keeps the
  two channels combined until the displayed final sum.
- Derived an exact Borel/cycle-index form for `f_k`: each one-run residual
  component of size `d` contributes
  `U=(d-1)tau(d-1)/tau(d)` and
  `V=(d-2)(d-3)tau(d-2)/tau(d)`; a two-run component with positive run sizes
  `a,b`, `d=a+b`, contributes
  `U=(d-2)tau(d-1)/tau(d)` and
  `V=((d-2)(d-3)-2[(a-2)_+ +(b-2)_+])tau(d-2)/tau(d)`.
  In both triangle and double cases,

  ```text
  f_k(s)=1/((n-3)(n-4)) [sum_i V_i+2 sum_(i<j)U_iU_j].
  ```

  With `T(z)=sum_(d>=1)tau(d)z^d=ze^{T(z)}`, the one-run decorations obey
  `sum tau(d)U_d z^d=z^2T'(z)` and
  `sum tau(d)V_d z^d=z^4T''(z)`.
- Added a narrow ordered-lift exact calibration, capped at `k=3,5,7`, which
  retains `J=0,1,2` and triangle/double contributions. It reproduces M168's
  exact signed sums. The observed `n^2 Delta` values are approximately
  `2.66440,1.51186,1.19283`; these are finite calibration only.

The remaining proof obligation is the channel-combined scalar estimate

```text
n^2 |sum_(j=1)^2 alpha_j Cov_(mu_j)(f_k,sigma_j)|=O(1).
```

No FD-bound, broad quotient computation, sign promotion, L1/H0/gap, or
Terminal inference has been made.
