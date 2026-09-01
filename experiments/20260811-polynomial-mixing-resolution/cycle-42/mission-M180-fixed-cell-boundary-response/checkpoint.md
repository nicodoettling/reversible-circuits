# M180 checkpoint

Date: 2026-08-13 UTC.

- Initialized the owned directory before substantive predecessor work.
- Fixed the sole target as the channel-combined `(BR)` coefficient.
- Fixed the scope firewall and anti-loss rules in `plan.md`.
- Re-read the project skill and core source-of-truth documents; full
  predecessor reconstruction and hash verification are next.

## Halfway checkpoint

Status: **proved a strict one-dimensional boundary-charge reduction; the
remaining coefficient bound is open.**

- Every named frozen predecessor manifest from M91 through M178 passes.
- Reconstructed all required exact source channels, target normalization,
  collision warnings, fixed-cell phase collapse, and M174/M178 affine
  response before estimating.
- Sharpened the exact Cayley-ratio centers, uniformly in positive sizes:

  ```text
  u_1(d)=  7/(24d)+O(d^-2),
  u_2(d)=-29/(24d)+O(d^-2),
  v_1(d)=-5/3+O(d^-1),
  v_2(a,b)=1/3-2(1[a=1]+1[b=1])+O(d^-1).
  ```

  The earlier transient `7/5` affine interpretation remains rejected;
  `L_T=0,L_D=-2` are retained.
- For every intermediate `s`, if `Q(s)` is the sum of `u_type(d)` over its
  three residual components and `I_D(s)` counts unit runs in its unique
  two-run component, derived exactly

  ```text
  B_k(s)=2n Q(s)-7/2-2I_D(s)+R(s),
  sup_s |R(s)|<infinity.
  ```

  Thus `(BR)` is equivalent to `n*eta(Q)=O(1)`; all kind/indicator terms and
  `R` already have bounded signed expectation.
- Let `M_(r,k)(d)` be the channel- and kind-combined signed expected number
  of residual components of run type `r` and size `d`. Then

  ```text
  eta(Q)=sum_d[M_(1,k)(d)u_1(d)+M_(2,k)(d)u_2(d)].
  ```

  Exact moment cancellations are `sum M_1=eta(T)`,
  `sum M_2=-eta(T)`, and `sum d(M_1+M_2)=0`.
- Components with `d>n/2` contribute `O(1/n)` absolutely, using the uniform
  `u_r(d)=O(1/d)` bound and total component mass at most six. The only open
  step is therefore a one-dimensional small-component signed coefficient
  estimate for `d<=n/2`.
- Exact `k=3,5` calibration verifies every formal identity. It gives
  `n eta(H)=2.07254,1.48209` and projected type-combined charge L1 scales
  `7.48081,5.25470`; these are finite checks only.

Next: record the exact cyclic-Borel coefficient formula and the equivalent
single boundary-incidence observable, then freeze the strict reduction with
the small-component lemma explicitly open if it cannot be closed.
