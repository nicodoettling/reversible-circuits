# M303 halfway checkpoint

Date: 2026-08-14 UTC.

## Immutable gates

The supplied M300 `SHA256SUMS` digest is exactly

```text
24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8.
```

All fourteen listed M300 payloads pass.  The cited M274, M277, M280, M283,
M285, M287, M295, and M298 top digests also match the values in M300's
dependency audit, and every entry in all eight inventories passes.

## Independent analytic reconstruction

Use `(pq)(x)=p(q(x))`, odd `k>=3`, `n=3k`, and the designated first-cell
channel-one law only.  The normalized merged law draws independent exterior
and middle chords.  The normalized split law first chooses either exterior
component with probability `1/2` and then draws independent exterior and
middle chords.  Expanding these laws atom by atom gives

```text
eta_1(G)=sum_f nu_M(f) sum_e gamma_k(e)G(ef),
gamma_k=nu_L-(nu_C-+nu_C+)/2.
```

The two commuting raw color orders have already been summed in this
conditional product law.  Thus there is no further `1/2`.  The scalar
`beta_1(ef)=gamma_k(e)nu_M(f)` is safe only because this support designates
the unique exterior cycle and unique middle cycle of the double; it is not
an unrestricted ordered-lift formula.

For an odd middle cycle, every unordered chord has one and only one form
`{m_a,m_(a+u)}` with `1<=u<k/2`.  There are `k` chords in each class and
their common mass is `v_k(u)`, so `sum_u k v_k(u)=1`.  This directly gives
the claimed cut-class phase decomposition.

For the exterior law, let `D=2k-1`, with contiguous blocks of sizes `k-1`
and `k`.  At canonical `L` cut `c`, exactly `2c` of the `D` chords cross
the blocks and `D-2c` stay internal.  Cross chords have coefficient
`v_D(c)>0`; seam chords have `-v_k(c)/2`; internal chords have
`v_D(c)-v_k(c)/2`.  With `r_d=tau(d-1)/tau(d)`, strict decrease of `r_d`
gives

```text
2v_D(c)/v_k(c)=product_(j=0)^(c-1) r_(D-j)/r_(k-j)<1,
```

including `c=k-1`.  Hence the support split and its `k(k-1)` positive and
`k(k-1)` negative counts are exhaustive.

Writing the positive and negative cut masses as `x_c` and `y_c`, direct
collection gives

```text
x_c=2c v_D(c),
y_c=(D-2c)(v_k(c)/2-v_D(c))+v_k(c)/2,
r_c=x_c-y_c=Dv_D(c)-(k-c)v_k(c).
```

The odd-cycle chord normalization gives `sum_c Dv_D(c)=1`; pairing `c`
with `k-c` gives `sum_c(k-c)v_k(c)=1`.  Thus `R_(k-1)=sum_c r_c=0`, and
ordinary discrete summation by parts produces every term and endpoint of
`EHA_1`.  This proves the identity only; it gives no sign.

## Remaining audit

One standard-library, no-import `k=7` reconstruction will independently
check the 54 class cells, 378 fixed-middle cells, reflection, exact minima,
and the finite mixed sign of `R_c`.  No second rank will be evaluated.

The source path `references/experiments.md` named in `AGENTS.md` is absent;
the skill-owned file at
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was
read.  This is a documentation discrepancy, not a mathematical objection.
