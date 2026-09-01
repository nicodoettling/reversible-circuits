# M310 independent proof audit

Date: 2026-08-14 UTC.

## Verdict and scope

```text
ACCEPT M305 AT FROZEN REDUCTION-ONLY SCOPE.
MATERIAL OBJECTIONS: ZERO.
NONMATERIAL CLARIFICATIONS: TWO.
```

The scope is the accepted auxiliary centered first-pair law, odd `k>=3`,
`n=3k`, `h=(k-1)/2`, and `(pq)(x)=p(q(x))`.  It is not the global bridge
law or the lazy exact `{3,4,5}` chain.

## 1. Exact `CBPV => SOCL`

For circular correlation,

```text
TV Corr(f,g)<=min(||f||_1 TV(g),TV(f)||g||_1).
```

This follows by expanding one circular difference and summing in either
order.  An owner indicator has mass `d` and variation at most four; the
support-head indicator has mass at most four.  Hence the literal response
profiles satisfy

```text
||P^H||_1<=32,
||P^A||_1<=4d,
||P^C||_1<=4min(d,e).
```

Restriction to differences `2<=ell<=n-3` cannot increase full circular
variation.  Since each exact row is `sum_P mu(P)P` after the complete signed
`Omega_T/Omega_S/Omega_N` coefficient and all incidences are grouped, one
triangle inequality over profile classes turns CBPV into

```text
||Delta H_d||_1<=C d b_d/k,
||Delta A_d||_1<=C d^2 b_d/k,
||Delta C^off_(d,e)||_1<=C d e b_d b_e/k.
```

Thus the implication is exact and never norms sources, channels, kinds,
phases, seams, or incidences separately.

## 2. All-rank scalar Borel BV

Direct cancellation gives

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2).
```

Uniformly for `j>=2`, elementary logarithmic bounds give
`0<=log r_j<=C/j` and adjacent log difference `O(j^-2)`.  Therefore, for
`R_m(q)=prod_(t<q)r_(m-t)` on `q<=floor(m/2)`, one obtains

```text
1<=R_m(q)<=C,
|R_m(q)-1|<=Cq/m,
|R_m(q+1)-R_m(q)|<=C/m,
|R_(m+1)(q)-R_m(q)|<=Cq/m^2.
```

For `D=2k-1`, the exact normalized split laws are

```text
p_s=[D/(D-1)]b_sR_D(s),              1<=s<=k-1,
q_s=[k/(k-1)]b_sR_k(s),              1<=s<=h,
q_s=0,                               h<s<=k-1.
```

On the low half, `a_s=p_s-q_s=b_sH_k(s)` with
`|H_k(s)|<=Cs/k` and adjacent difference `O(1/k)`.  Together with
`|b_(s+1)-b_s|<=Cb_s/s`, this makes the low internal and zero-boundary
variation `O(k^-1)`.

For `h<=s<=k-1`, both Borel indices are comparable to `k`, so uniform
Stirling gives `p_s=O(k^-3/2)`.  The exact ratio

```text
p_(s+1)/p_s=r_(D-s)/r_(s+1)
```

makes internal differences `O(k^-5/2)`.  The junction and terminal checks
are explicitly

```text
|a_(h+1)-a_h|<=p_(h+1)+p_h+q_h=O(k^-3/2),
|a_k-a_(k-1)|=p_(k-1)=O(k^-3/2).
```

Thus, with `a_0=a_k=0`,

```text
sum_(s=0)^(k-1)|a_(s+1)-a_s|<=C/k
```

for every odd `k>=3`.  The absolute constant absorbs the finite `k=3`
endpoint.  This independently covers `s=h`, `h+1`, and `k-1`.

## 3. Generic multiplier shortcut is refuted

M91's accepted sign theorem has `a_s<0` below the cut, `a_s>0` above it,
and `sum|a_s|=Theta(k^-1/2)`.  On a two-point profile space, map all negative
indices to `delta_-` and positive indices to `delta_+`.  Every kernel has
TV mass one, but

```text
||sum_s a_sF_s||_TV=sum_s|a_s|=Theta(k^-1/2).
```

This disproves only the generic inference from scalar BV plus bounded
arbitrary kernels.  It is not an actual owner-profile construction and does
not refute CBPV.

## 4. Marked Abel identity and unresolved boundary

M91 proves in each live channel `j=1,2`

```text
H_(j,B)-H_(j,A)
 =sum_(u=1)^(k-2)D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_(s=1)^h q_s(Phi_(j,s)-Psi_(j,s)).
```

Here `D_(k-1)=0` because `p,q` normalize, so no endpoint term is absent.
The literal owner-incidence mark is a finite linear kernel and is
translation invariant on cyclic product orbits.  Pushing the identity
through that mark, multiplying by `alpha_1,alpha_2`, and combining channels
gives exactly

```text
mu^X
 =sum_u D_u(F^X_u-F^X_(u+1))
  +sum_s q_s(F^X_s-G^X_s).
```

The `Phi/Psi` laws already contain all raw ordered lifts.  At state level,
the exact triangle `1/3` and combined-double `1/4` representation averages
return one physical incidence mark; summing all actual owner incidences is
invariant under representation relabeling.  Consequently both channels,
all `T/S/N` kinds, phases, and seams remain combined before the norm.

This is an equality, not a bound.  The three norms asserted by CMPAD remain
unproved; scalar BV cannot supply them because the mark changes with `s`.

## 5. Small sizes and target endpoints

- `d=1`: no generic phase, so every response row with an index one is zero;
  formal `u_1=0` is harmless.
- `d=2`: at most one generic phase, hence `Delta A_2=0`.
- `d=3`: the one-run case has two consecutive generic phases and the
  two-run case at most one.  Its autocorrelation is supported only at
  `0,1,n-1`, hence `Delta A_3=0`.
- The target differences compare coordinates only in `2,...,n-2`, so no
  endpoint is omitted.
- `H_2,H_3` and off-diagonal rows at sizes two or three remain unresolved.
- At `k=3`, `h=1`, so the SOCL range contains only zero size-one rows.

## 6. Sole finite replay

The authorized deterministic `k=11` replay is identical to the frozen JSON
after deleting only `elapsed_seconds`.  It reproduces `27,060` states,
`91,110` positive representations, raw A/B counts `23,595/52,845`, and
normalized maxima `2.3542421864832535`, `0.8658065231265041`, and
`4.929342656484796` for H, A, and C.  These are finite-only facts.

## 7. Numbered objections

1. **Material objections:** none.
2. **Nonmaterial clarification, zero profile:** the initial literal
   pushforward can carry nonzero signed coefficient mass at response profile
   zero, as the `k=11` rows show.  Deleting it is response-equivalent but not
   norm-equivalent.  Thus “CMPAD is the exact formulation of CBPV” should be
   read as “CMPAD is the exact response-relevant reduced formulation.”
3. **Nonmaterial clarification, junction:** the `h -> h+1` jump contains
   `p_(h+1)-p_h` in addition to dropped `q_h`.  All three terms are
   `O(k^-3/2)`, so M305's scalar theorem is unchanged.
4. **Firewall:** CMPAD, CBPV, SOCL, SOCT, BODT, DOR, PBV/FD/FCL1, every gap
   or mixing theorem, and both Terminals remain unresolved.

