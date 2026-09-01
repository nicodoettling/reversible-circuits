# M263 clean-room proof audit of frozen M258 TAV

Date: 2026-08-14 UTC.

Provisional verdict before the bounded falsifier: **ACCEPT TAV**.  This note
audits only the exact theorem

```text
sum_(s=1)^(k-2) sqrt(s)|Theta_(s+1)(ell)-Theta_s(ell)|
 <=500 sqrt(ell)
```

for odd `k>=3` and `2<=ell<=(3k-1)/2`.  It does not audit or infer full DV,
J2, WPCR, SCBR, a response theorem, a gap, mixing, or a Terminal.

## 1. Immutable gate

M258's `SHA256SUMS` contains exactly the ten files named by its freeze
manifest.  All ten pass `sha256sum -c`.  The checksum-file digest is exactly

```text
753ef6932c3e5e5d69df7f429e8740710d77269357749d505dca0cf31e109ef8.
```

The M258 directory was not edited.

## 2. Cyclic seam count and signed spikes

Fix a retained set `E subset Z_D` of cardinality `t` and place the two seams
at `0` and `k`.  Under all `D` translations, each seam belongs to the
translated set exactly `t` times.  The number of translations containing
both is, after undoing the translation,

```text
j=#{x in E:x+k in E mod D}.
```

Inclusion--exclusion therefore gives, in the order neither, small only,
large only, both,

```text
D-2t+j,  t-j,  t-j,  j.
```

The corresponding sizes are `t,t+1,t+k,t+k+1`.  Multiplying by their cutoff
heads and collecting the coefficient of `j` gives

```text
1{t<=ell}-1{t<=ell-1}-1{t<=ell-k}+1{t<=ell-k-1}
 =1{t=ell}-1{t=ell-k}.
```

Summing the `t-1` placements thus gives exactly

```text
(t-1)Q_ell(t)+(J_(r,t)/D)(1{t=ell}-1{t=ell-k}).
```

This derivation keeps simultaneous hits.  The parent enters only through
`E` and `J`, so it applies separately to `r=s` and `r=D-s`; the later sum
keeps both orientations and all placement multiplicities.  Kernel symmetry
under `d<->t=r-d` is exact.  Hence the normalized decomposition into the
reflected base and the two signed `Z` spikes is correct.

## 3. Reflected operator, not the forward operator

Let

```text
c_r(t)=(t-1)b_t b_(r-t)/(R b_r).
```

For fixed admitted `t`, direct division--not a forward-head lemma--gives

```text
c_(r+1)(t)/c_r(t)=rho_(r+1)/rho_(r+1-t),
rho_m=b_(m-1)/b_m.
```

The accepted logarithmic-derivative calculation says `rho_m` decreases, so
this ratio is at most one.  If `r<=u+1`, every admitted `t` is in the head
and `G_r(u)=Wtilde_r(1)=h(r)`; `h` is increasing.  Once `r>u+1`, no new head
coefficient is admitted and every existing coefficient decreases.  Thus
`G_r(u)` is unimodal with peak at most `h(u+1)<=u/R`, even when the sequence
is truncated at `D-1`.  Therefore

```text
TV_r G_r(u)<=2u/R.
```

For an adjacent rank, the short edges are `r=1,...,k-2` and the reversed
long edges are `r=k,...,D-2`.  They are disjoint subsets of the full
variation (the middle edge is omitted).  Pairing the two increments before
absolute values and using `sqrt(s)<=sqrt(k)` gives raw variation at most

```text
2u sqrt(k)/R <=2u/sqrt(k)<=3sqrt(u),
```

because `u<3k/2`.  With `H_s>=2/9`, normalized values in `[0,1]`, and
`sum_s sqrt(s)|Delta H_s|<=8/3`, the exact quotient identity yields

```text
(9/2)(3sqrt(u)+8/3)<=26sqrt(u).
```

Also `Wtilde_r(1)=h(r)`, so the normalized constant response is exactly one
and adjacent differences annihilate constants.  This resolves the critical
orientation issue without identifying `Wtilde` with M251's forward `W`.

## 4. Cutoff endpoints and Abel expansion

Directly from the three heads defining `Q_ell`:

- if `ell<=k`, it is `(D-t)/D` through `t=ell-1`, equals
  `(D-2ell)/D` at `t=ell`, and is zero later;
- if `ell>k` and `a=ell-k`, it is one through `a`, then `(D-t)/D`
  through `ell-1`, equals `(D-2ell)/D` at `ell`, and is zero later.

This includes `ell=k` in the first case.  At `k=3,ell=4>D-2`, the special
atom lies outside the operator's used domain and therefore removes, rather
than adds, variation.  Empty or coincident ranges behave the same way.

There are at most three endpoint jumps of magnitude at most one and one
slope interval of magnitude `1/D` per edge.  Since `ell<D` and every used
weight is at most `sqrt(ell)`, their total weighted variation is at most
`4sqrt(ell)`.  Finite Abel expansion is on exactly `t=1,...,D-2`; after
constant annihilation, multiplication by the independently proved head
constant `26` gives the base response `104sqrt(ell)`.

## 5. Exact `J` support and pair list

For `r<=k-1`, `[0,r)` contains no directed distance-`k` pair.  For
`r=k+c`, `0<=c<=k-2`, splitting according as addition by `k` wraps gives
the complete list

```text
(u,u+k),     0<=u<c,
(u+k-1,u),   0<=u<=c.
```

There are `2c+1` pairs and no others.  If `t<=c`, the two retained intervals
have fewer than `k` entries, so a pair cannot be internal.  A first-to-second
crossing would require both `u<=a-1` and `u>=a+c-t`; a wrapped crossing would
require both `u<=a-1` and `u>=a+c-t+1`.  Both are impossible.  Hence
`J_(k+c,t)=0` for `t<=c`.  Independently, each of `t-1` placements contains
at most `t` directed pairs, so `0<=J<=t(t-1)`; counting against the ambient
list also gives `J<=(t-1)(2c+1)`.

## 6. Borel/Stirling spike mass

Put `r=t+v`.  The two-sided Stirling bounds imply, uniformly for `v,t>=1`,

```text
b_v/b_(t+v)
 <=[e/sqrt(2pi)](1+t/v)^(3/2)
 <2(1+t/v)^(3/2)
 <=4[1+(t/v)^(3/2)].
```

Also `b_t<=1/(2t^(3/2))`, `sum_v v^(-3/2)<=3`, `D/R<=2`, and `R>=k`.
Consequently

```text
sum_(r=t+1)^(D-1) K(r,t)
 <=4b_t/R[D+3t^(3/2)]
 <=4/t^(3/2)+6/k.
```

Using `J<=t(t-1)<=t^2` and `D>=k`, and writing `x=t/k<3/2`, gives

```text
sum_r S_r(t)
 <=4sqrt(t)/k+6x^2
 <=4sqrt(x)+12sqrt(x)
 =16sqrt(t/k).
```

The second inequality uses `k>=1` in the first term and
`x^(3/2)<(3/2)^(3/2)<2` in the second.  Empty sums when `t>D-2` are zero.

## 7. Paired raw response and normalization

For fixed `t`, form the exact paired numerator first:

```text
(S_(s+1)-S_s)+(S_(D-s-1)-S_(D-s)).
```

Only then use positivity.  Each `S_r` appears at most twice, so the weighted
raw variation is at most

```text
2sqrt(k) sum_r S_r(t)<=32sqrt(t).
```

Moreover `J/D<=t-1` on the active domain, hence
`S_r(t)<=(t-1)K(r,t)` and the normalized profile satisfies `0<=Z_s(t)<=1`.
The same exact quotient identity and the exact `H` bounds therefore give

```text
(9/2)(32sqrt(t)+8/3)<=160sqrt(t).
```

The displayed inequality is valid already at `t>=1` (and the theorem uses
`t>=2`).  At `k=3`, the denominator values are `H_1=1/2` and `H_2=2/9`, so
the endpoint is covered explicitly.

## 8. Assembly and domain

The base contributes `104sqrt(ell)`, the `t=ell` spike contributes at most
`160sqrt(ell)`, and the `t=ell-k` spike is either empty (`ell-k<2`) or at
most `160sqrt(ell-k)<=160sqrt(ell)`.  Thus the total is

```text
424sqrt(ell)<=500sqrt(ell).
```

All sums have the exact domains `2<=r<=D-1`, `2<=t<=r-1`, and
`1<=a<=t-1`.  Values with `r<=1`, `t>D-2`, or an inadmissible spike are
zero by empty-sum convention.  No rank threshold beyond odd `k>=3` is used.

