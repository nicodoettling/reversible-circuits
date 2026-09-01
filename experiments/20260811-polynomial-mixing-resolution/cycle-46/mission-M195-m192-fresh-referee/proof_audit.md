# M195 proof audit: fresh referee of immutable M192

Date: 2026-08-13 UTC.

Status: **ACCEPT** M192's frozen strict reduction. There are no material
objections and no nonmaterial qualifications. This audit does not prove
`(DV)`, `(DE)`, the conditional `J=2` prefix estimate, `(PCR)/(WPCR)`,
`(SCBR)), or any downstream claim.

## Proposition 1: completion convolution and shared endpoints

Put
```text
tau(r)=r^(r-1)/r!,             T(z)=sum_(r>=1) tau(r)z^r.
```
The tree-function equation `T=ze^T` and Lagrange inversion give
```text
[z^r]T^2=(2/r)[u^(r-2)]e^(ru)=2 r^(r-2)/(r-2)!
       =2(r-1)tau(r)/r.
```
Therefore
```text
sum_(c=1)^(r-1)tau(c)tau(r-c)=2(r-1)tau(r)/r.       (1)
```

After the first exterior edge splits its active source cycle into components
of sizes `a,b`, each of its two endpoints is a mark, one in each component.
For a marked component of size `r`, sum the second-edge completion ratio
over the `r-1` internal partners of the mark. Using (1), this is
```text
2(r-1)/[r(R-1)].
```
Here the initial exterior rank is `R=2k-2`, hence the second-step denominator
is `R-1=2k-3`. Summing the two marked components gives exactly
```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                 (2)
```
The untouched A-side `k`-cycle contributes to the remaining rank and
completion denominator but has no marked endpoint; no extra numerator term
belongs in `gamma_F`.

For one `(2k-1)`-cycle the probability that the first two factors form a
triangle is `3/(2k-1)`. For two `k`-cycles, the second factor remains in
the first factor's source cycle with probability `(k-2)/(2k-3)`, and its
conditional triangle probability is `3/k). Thus
```text
sum p_s gamma_L(s)=3/(2k-1),
sum q_s gamma_F(s)=3(k-2)/[k(2k-3)].                (3)
```
Each literal prefix observable counts three residual components with
multiplicity and lies in `[0,3]`. Hence the complete signed shared-endpoint
response is bounded by three times the sum of (3), namely `O(1/k)).
This argument does not delete repeated-size collision faces.

## Proposition 2: disjoint submeasures and exact Abel identity

Define without renormalizing
```text
p_hat_s=p_s(1-gamma_L(s)),       q_hat_s=q_s(1-gamma_F(s)),
E_u=sum_(s<=u)(p_hat_s-q_hat_s).
```
Then the disjoint totals are not equal. Directly from (3),
```text
E_(k-1)=[1-3/(2k-1)]-[1-3(k-2)/(k(2k-3))]
       =-6(k-1)/[k(2k-1)(2k-3)].                   (4)
```
Thus the endpoint is negative, not zero, and is `O(k^-2)`.

For any disjoint-product test `Z`, add and subtract
`sum_s q_hat_s Phi_s^D(Z)`. Since
`p_hat_s-q_hat_s=E_s-E_(s-1)` and `E_0=0`, finite summation by parts gives
```text
sum_s(p_hat_s-q_hat_s)Phi_s^D
 =E_(k-1)Phi_(k-1)^D
  +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D).
```
Adding the embedding contrast gives precisely M192's `(DA)`, with the sign
and endpoint in (4). No probability normalization is silently imposed on
the disjoint submeasures.

## Proposition 3: uniform scalar cumulative estimate

Let `b_s=e^-s tau(s)` and `D_u=sum_(s<=u)(p_s-q_s)`. The exact first-split
laws are
```text
p_s=[(2k-1)/(2k-2)] b_s b_(2k-1-s)/b_(2k-1),
q_s=[k/(k-1)] b_s b_(k-s)/b_k.
```
Uniform Stirling inequalities give `b_m asymp m^-3/2). More specifically,
for `1<=s<=m/2`,
```text
b_(m-s)/b_m=1+O(s/m)
```
after retaining the harmless prefactor ratios; finite bounded `m` are
absorbed into the universal constant. Consequently, for `s<=k/2`,
```text
p_s+q_s<=C b_s,                  |p_s-q_s|<=C(s/k)b_s.
```
Since `b_s<=Cs^-3/2`,
```text
|D_u|<=C k^-1 sum_(s<=u)s b_s<=C sqrt(u)/k
```
when `u<=k/2`.

When `u>k/2`, the q-law has ended and both original laws have total mass
one, so
```text
D_u=-sum_(s>u)p_s.
```
Uniform Stirling bounds yield
```text
p_s<=C k^(3/2)/[s^(3/2)(2k-1-s)^(3/2)].
```
Here `s>k/2` and `2k-1-s>=k); summing at most `k` terms gives
`|D_u|<=C/sqrt(k)<=C sqrt(u)/k`.

Finally (2) implies `0<=gamma_L,gamma_F<=C/k` uniformly. Therefore
```text
E_u=D_u-sum_(s<=u)[p_s gamma_L(s)-q_s gamma_F(s)]
```
and the correction has absolute value at most `C/k`. This proves
```text
|E_u|<=C sqrt(u)/k
```
for every odd `k>=3` and `1<=u<=k-1`. This proof is universal; it does
not infer the bound from finite signs.

## Exact implication of the two open profile lemmas

For either prefix observable, `0<=Phi_s^D(Z)<=3`. If M192's `(DV)` and
`(DE)` hold, (4) makes the endpoint term `O(k^-2)), while the scalar
Abel term is at most
```text
(C/k) sum_(u=1)^(k-2)sqrt(u)
       |Phi_u^D(Z)-Phi_(u+1)^D(Z)|
 <=C sqrt(l)/k.
```
The signed embedding term is `O(sqrt(l)/k)` by `(DE)`; Proposition 1
handles shared endpoints. This proves exactly the claimed *conditional
`J=2`* prefix estimate and nothing more.

The profiles are normalized expectations under the literal ordered-pair laws
before applying the component-count observable. They therefore retain both
double colors, same/cross-run choices, unit gaps, and all repeated component
sizes. The two proposed lemmas do not lose a kind or collision stratum.
They also do not control the separate `J=1` channel, so they cannot by
themselves prove full `(PCR)/(WPCR)`. M192 states this restriction correctly.

## Numbered objections

1. **Material objections:** none.
2. **Nonmaterial qualifications:** none.

The first open steps remain `(DV)` and `(DE)`. Accordingly the conditional
`J=2` prefix estimate, `(PCR)/(WPCR)`, `(SCBR)`, and all downstream
claims remain unresolved.
