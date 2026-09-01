# M263 report — fresh immutable referee of M258 TAV

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M258 TAV AS FROZEN.
NO FULL-DV OR DOWNSTREAM INFERENCE.
```

For every odd `k>=3` and integer `2<=ell<=(3k-1)/2`, M258 proves

```text
sum_(s=1)^(k-2) sqrt(s)
 |Theta_(s+1)(ell)-Theta_s(ell)| <=500sqrt(ell).
```

This audit accepts only that literal normalized B-side two-run theorem.  It
does not infer full DV, conditional J2, WPCR, SCBR, a response theorem, a
spectral gap, mixing, or either Terminal.

## Immutable gate

All ten payload files in M258's frozen inventory pass `sha256sum -c`.  The
checksum file itself has the assigned digest

```text
753ef6932c3e5e5d69df7f429e8740710d77269357749d505dca0cf31e109ef8.
```

M258 remained immutable.

## Independent mathematical audit

Translating a retained `t`-edge set through all cyclic starts gives the exact
seam counts `D-2t+j,t-j,t-j,j`.  The overlap coefficient is the elementary
head difference

```text
1{t=ell}-1{t=ell-k},
```

so summing the `t-1` placements yields exactly the base cutoff term plus two
signed spikes.  Both parent branches and the literal `H_s` normalization are
preserved.

The base operator is genuinely reflected.  Direct division gives

```text
c_(r+1)(t)/c_r(t)=rho_(r+1)/rho_(r+1-t)<=1.
```

Thus its head equals increasing `h(r)` until saturation and then decreases
coefficientwise.  Its full variation is at most `2u/R`.  The short and
reversed-long rank edges are disjoint portions of this variation, so exact
pairing followed by the accepted denominator bounds gives `26sqrt(u)`.
No forward-M251 `W` response lemma is reused.

The piecewise `Q_ell` profile and all endpoints pass, including `ell=k` and
the exceptional used-domain geometry `k=3,ell=4>D-2`.  Its weighted cutoff
variation is at most `4sqrt(ell)`, hence the base response is
`104sqrt(ell)`.

For `r=k+c`, the complete directed distance-`k` pair list is

```text
(u,u+k), 0<=u<c;       (u+k-1,u), 0<=u<=c.
```

It proves `J=0` on short parents and on long parents when `t<=c`, while
`J<=t(t-1)` universally.  The audited Stirling comparison gives

```text
sum_r K(r,t)<=4/t^(3/2)+6/k,
sum_r S_r(t)<=16sqrt(t/k).
```

Positivity is used only after forming the exact short/long paired numerator.
The raw response is at most `32sqrt(t)`; `H_s>=2/9`,
`sum sqrt(s)|Delta H_s|<=8/3`, and `0<=Z_s<=1` give the normalized bound
`160sqrt(t)`.  Therefore `104+160+160=424<=500`.

Empty sums cover `r<=1`, `t>D-2`, and an inadmissible `ell-k` spike.  No
unstated rank threshold is used.

## Independent falsification

`cleanroom_tav_referee.py` imports no M258 code and reads no M258 data.  It
checks exactly `k=3,5`, all allowed cutoffs, ranks, parents, retained sizes,
and placements.  All 442 assertions pass.  The largest observed TAV ratio is
approximately `0.338913`; this is finite falsification only, not the
universal proof.

Reproduction from this directory:

```text
python3 cleanroom_tav_referee.py --output cleanroom_results.json
python3 -m compileall -q cleanroom_tav_referee.py
```

Python `3.12.3`, standard library only, deterministic, `seed=null`.

## Numbered objections

1. **Material objections:** none.
2. **Nonmaterial objections:** none.

Final action: accept M258 TAV as frozen at its exact scope and retain every
named downstream obligation as open unless separately audited.

