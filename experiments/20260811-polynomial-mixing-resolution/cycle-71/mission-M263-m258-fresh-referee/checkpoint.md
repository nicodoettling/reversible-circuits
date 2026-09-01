# M263 Initial Checkpoint

Status: `in progress`.

The project skill and required project sources were read before substantive
work.  `AGENTS.md` names `references/experiments.md`, but the existing file is
`.codex/skills/reversible-circuit-sampler/references/experiments.md`; the latter
was read and this path discrepancy is recorded rather than silently ignored.

Assigned source is frozen M258 at
`cycle-70/mission-M258-two-run-tav/`.  This referee will leave that directory
unchanged.  The audit is restricted to the exact TAV theorem and its local
lemmas; it will not infer full DV or any later chain consequence.

Next: reproduce the freeze, read the complete inventory, independently derive
the six named proof points, and build the compact falsification checker.

## Substantive verdict checkpoint

Status: `provisional ACCEPT of TAV`; compact `k=3,5` falsification remains.

The immutable gate passes.  `sha256sum -c SHA256SUMS` reports `OK` for all
ten frozen payload entries, and the top digest is exactly
`753ef6932c3e5e5d69df7f429e8740710d77269357749d505dca0cf31e109ef8`.

The universal analytic audit independently certifies the two sensitive
estimates:

- For `c_r(t)=(t-1)K(r,t)`, direct division gives
  `c_(r+1)(t)/c_r(t)=rho_(r+1)/rho_(r+1-t)<=1`.  Hence the reflected head is
  `h(r)` through `r=u+1` and coefficientwise decreasing afterwards.  Its
  full `r`-variation is at most `2u/R`.  The short and reversed-long edges
  used by an adjacent `s` increment are disjoint subsets of that variation;
  after exact normalization this gives `26 sqrt(u)`.  No forward-M251 `W`
  increment bound is reused.
- Stirling gives
  `b_v/b_(t+v)<=2(1+t/v)^(3/2)<=4(1+(t/v)^(3/2))` and
  `b_t<=1/(2t^(3/2))`.  Thus
  `sum_r K(r,t)<=4/t^(3/2)+6/k`.  With `J<=t(t-1)`, `D>=k`, and
  `x=t/k<3/2`, the spike mass is at most
  `4 sqrt(t)/k+6x^2<=16 sqrt(x)`.  Positivity is invoked only after forming
  the exact paired numerator, giving raw response `32 sqrt(t)` and normalized
  response `160 sqrt(t)`.

The seam inclusion--exclusion, signed two-spike identity, cutoff endpoints,
ambient pair list, denominator bounds, and empty-domain conventions also pass
the algebraic audit.  Details are in `proof_audit.md`.  No full-DV or
downstream inference is made.

