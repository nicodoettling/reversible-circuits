# M305 plan: combined Borel coefficient route to SOCL

Date: 2026-08-14 UTC.

## Scope, convention, and immutable gates

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.
Put

```text
n=3k,       k>=3 odd,       h_0=(k-1)/2.
```

The target is M297/M302's complete centered first-pair law in the auxiliary
uniform minimal-factorization model.  It is not the global fixed-length
identity-word law and not the lazy exact same-product `{3,4,5}` heat-bath
chain.

Before fixing the candidate below, the two immediate packages reproduced:

```text
M297 SHA256SUMS  a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792
M302 SHA256SUMS  1009b8d3fbe40dc75aa9a10d3071d74a978ab6a97951a270e57a01916b9fdd27
```

Every payload row in both manifests passes.  All further cited inventories
will be checked byte-for-byte and recorded before they are imported.

## Accepted interface

For each positive `T/S/N` composition and support anchor, M297 forms the
already-combined coefficient

```text
Omega_T(g)=(1/3)sum_r omega(s_T(r,g)),
Omega_S(g)=(1/4)sum_r omega(s_S(r,g)),
Omega_N(g)=(1/4)sum_r omega(s_N(r,g)),
```

where `omega=P_B-P_A` already includes both live channels and all raw lifts.
No source law, channel, topology kind, phase, or seam may be normed
separately.

M297/M302 reduce SOCL to the three complete rows `H_d`,
`C^off_(d,e)`, and `A_d`.  Size-one owners have no generic phase, so every
row with an index one is exactly zero; set the formal undefined amplitude
`u_1:=0`.  The self rows satisfy `Delta A_2=Delta A_3=0` on the target lag
range, while `H_2,H_3` and off-diagonal rows with sizes two or three remain.

## Analytic candidate fixed before computation

For an owner occurrence `i`, let its exact literal response profiles be

```text
P^H_(K,g,i)=Delta[Corr(chi_i,B)+Corr(B,chi_i)],
P^A_(K,g,i)=Delta Corr(chi_i,chi_i),
P^C_(K,g,i,j)=Delta Corr(chi_i,chi_j),   i!=j.
```

For a profile vector `P`, push the full signed coefficient through the
literal profile map, combining all `T/S/N`, both channels, all anchors,
phases, seams, and owner incidences before taking absolute values:

```text
mu^H_(k,d)(P)
 =sum_(K,g,i:d_i=d, P^H_(K,g,i)=P) Omega_K(g),

mu^A_(k,d)(P)
 =sum_(K,g,i:d_i=d, P^A_(K,g,i)=P) Omega_K(g),

mu^C_(k,d,e)(P)
 =sum_(K,g,i!=j:d_i=d,d_j=e, P^C_(K,g,i,j)=P) Omega_K(g).
```

Write `b_d=e^(-d)d^(d-1)/d!`.  The predeclared stronger coefficient target
is:

> **Combined Borel profile variation (CBPV).**  There is an absolute `C`
> such that, uniformly for `1<=d,e<=h_0`,
> ```text
> ||mu^H_(k,d)||_TV <= C d b_d/k,
> ||mu^A_(k,d)||_TV <= C d b_d/k,
> ||mu^C_(k,d,e)||_TV
>      <= C max(d,e)b_d b_e/k.                     (CBPV)
> ```

The candidate is coefficient/divergence-level: its intended proof is to
write each already-combined profile coefficient as a critical-Borel factor
times a complementary-gap discrete divergence, using

```text
r_j=b_(j-1)/b_j=1+O(1/j),
|r_(j+1)-r_j|=O(1/j^2),
```

with constant terms cancelled only after the complete `A/B`, channel,
`T/S/N`, phase, and seam sum is formed.

The deterministic profile bounds

```text
||P^H||_1=O(1),
||P^A||_1=O(d),
||P^C||_1=O(min(d,e))
```

would make CBPV imply exactly the three SOCL bounds.  This implication will
be proved before attempting the coefficient estimate.

## One finite guard, only if needed

After CBPV is fixed here, at most one compact exact rank may be used:

```text
k=11, n=33.
```

It may only falsify/calibrate CBPV by reconstructing the complete combined
coefficient before profile grouping and norms.  No finite row will be used
to prove an all-rank constant.

## Decision rule

- If CBPV is proved, derive all three SOCL rows with `d=1,2,3` handled
  exactly, then stop for fresh audit before any downstream inference.
- If CBPV fails, freeze the first exact combined profile and Borel-ratio
  obstruction, and state the narrower surviving rowwise divergence lemma.
- If the full coefficient table cannot be closed, isolate the first missing
  complementary-gap identity without splitting signed source/type rows.

No BODT, DOR, PBV/FD/FCL1, gap, mixing, or Terminal inference is allowed
without the full theorem, and any claimed full theorem still awaits fresh
audit.
