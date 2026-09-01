# M258 Checkpoint

## Halfway checkpoint

Status: **TAV proved with constant 500, subject to fresh audit**.

- Scope is locked to the unweighted literal TAV inequality in `plan.md`.
- All six named immutable inventories (M199/M207, M235/M238, M251/M255)
  pass `sha256sum -c`; no dependency was edited.
- `tav_cyclic_coefficient.md` proves the exact cyclic-start coefficient.
  For retained length `t`, the four seam-pattern counts are
  `D-2t+j,t-j,t-j,j`. After the placement sum, every simultaneous-seam
  dependence is confined to
  `J_(r,t)[1{t=ell}-1{t=ell-k}]/D`; the remainder is the explicit scalar
  head coefficient `(t-1)Q_ell(t)`.
- The exact unweighted profile is
  `Theta_s=[T_s+T_(D-s)]/H_s`, with both parent orientations retained and
  no `q` or `qhat` averaging.
- The base term uses the reflected operator
  `Wtilde_r(f)=sum_t(t-1)K(r,t)f(t)`, not M251's forward `W_r`. Its head
  response is proved independently by exact unimodality, with constant 26.
- The exact pair list proves that short-parent overlap vanishes and that a
  long-parent spike is supported only when `c<t`. A coarser uniform Borel
  mass estimate gives normalized spike response at most `160sqrt(t)`.
- The scalar cutoff variation is at most `4sqrt(ell)`, giving base response
  `104sqrt(ell)`. The two signed spikes give at most `320sqrt(ell)`, so TAV
  holds with safe constant 500.
- The restricted standard-library checker passes 4,960 assertions at exactly
  `k=3,5,7`; this is finite falsification only.
- Full DV and every J2/WPCR/SCBR/response/gap/mixing/Terminal consequence
  remain outside this mission and are not claimed.
