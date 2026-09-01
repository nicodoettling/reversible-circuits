# M286 fresh proof audit of frozen M282

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
VERDICT: ACCEPT M282 AS FROZEN.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

M282 proves exactly the channel-two scalar-Abel bounded-variation statement
`CSBV` for every odd `k>=3` in the balanced first fixed cell of the
auxiliary uniform minimal-long-cycle factorization law.  The convention is
`(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.  This is
not the global identity-word law and is not the lazy exact same-product
`{3,4,5}` heat-bath chain.

This audit proves no `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, `FD`, `FCL1`,
bridge/local spectral gap, polynomial mixing, or Terminal A/B statement.

## 2. Immutable provenance

The independently computed SHA-256 digest of M282's checksum file is

```text
cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7.
```

Every one of its nine named payloads passes.  The directory contains exactly
those nine files and `SHA256SUMS`; there is no unmanifested payload.

Every payload in each declared predecessor ledger also passes.  Their
independently recomputed checksum-file digests are

```text
M272 af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
M276 882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M279 3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
M192 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
M195 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M248 c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8
M249 9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7
```

M272 remains rejected as a frozen package for its unrelated channel-one
near-tail proof gap.  M276's append-only repair, accepted by M279, does not
alter the exact channel-two interface reused here.  No predecessor was
edited.

## 3. Independent Abel reconstruction

Put

```text
D=2k-1,             R=D-2=2k-3,
a_L(s)=1-gamma_L(s),       a_F(s)=1-gamma_F(s),
A_s=p_s a_L(s)-q_s a_F(s).
```

The accepted split laws are probability laws on `1<=s<=k-1`, with `q_s=0`
outside `s<k/2`.  The disjoint submeasures have masses `p_s a_L(s)` and
`q_s a_F(s)`.  If

```text
E_u=sum_(s<=u) A_s,
```

then `A_s=E_s-E_(s-1)`, `E_0=0`.  Finite summation by parts therefore gives
coordinatewise

```text
E_(k-1) Phi_(k-1)^D
 +sum_(u=1)^(k-2) E_u(Phi_u^D-Phi_(u+1)^D)
 =sum_(s=1)^(k-1) A_s Phi_s^D.                    (3.1)
```

The endpoint is not set to zero.  The exact shared masses give

```text
sum_s A_s
 =[1-3/D]-[1-3(k-2)/(kR)]
 =-6(k-1)/(kDR).                                   (3.2)
```

Thus M282's first collapse has the correct sign and retains the complete
nonzero endpoint.

## 4. Independent support-pair disintegration

Let

```text
b_r=e^(-r)r^(r-1)/r!,
K_R(r,x)=b_x b_(r-x)/(R b_r),       1<=x<r.
```

After a first chord, a residual component of size `r` is selected with
rank weight `(r-1)/R`; a specified internal chord of cyclic split `x` then
has raw probability `K_R(r,x)`.  The probability that this chord avoids the
marked first endpoint, summed over the component, is

```text
h(r)=(r-1)(r-2)/(rR).
```

Fix the ordinary interval representation of that component.  At abstract
displacement `x`, the ordered second-edge endpoints contribute

```text
F_r(x)=1[x<=r-2](r-x-1)K_R(r,x).                  (4.1)
```

There are `r-x-1` admissible chords with both endpoints different from the
mark.  For a nonmarked vertex, the raw endpoint intensity is
`2(r-1)/(rR)`; deleting the mark-vertex chord subtracts `K_R(r,x)`.
The two boundary first endpoints therefore give

```text
C_r(x)=4(r-1)/(rR)-2K_R(r,x).                     (4.2)
```

This remains correct at an even midpoint: the two coincident vertex
incidences represent two distinct ordered cross pairs and must retain their
multiplicity.  Hence

```text
U_r(x)=F_r(x)+C_r(x),
```

with zero extension outside `1<=x<r`.  Reverse orientations contribute
`U_r(D-d)` at abstract displacement `d`.

For a first split `s`, division by its disjoint normalizer is the only
conditional normalization.  Thus with

```text
W_s=A_s/a_L(s)
```

the signed abstract ordered-support-pair intensity is exactly

```text
c_d=A_min(d,D-d)
 +sum_(r=1)^(D-1) W_min(r,D-r)[U_r(d)+U_r(D-d)].   (4.3)
```

The sum over `r` lists both residual component sizes `s,D-s`; it is not an
extra factor two.  Equation (4.3) immediately gives `c_d=c_(D-d)` and
retains all twelve ordered pairs of four distinct support vertices.

## 5. Literal two-seam embedding

The abstract exterior cycle is embedded by

```text
lambda(t)=t+1,        0<=t<=k-2,
lambda(t)=t+k+1,      k-1<=t<=D-1.
```

An oriented interval of abstract length `d` crosses the wrap seam with
extra ambient displacement `1` and the long seam with extra displacement
`k`.  For `1<=d<=k-1`, the counts of phases crossing neither, wrap only,
long only, and both are `(D-2d,d,d,0)`.  For `k<=d<=D-1`, they are
`(0,D-d,D-d,2d-D)`.  Using `c_d=c_(D-d)` yields, with only notational
padding `c_0=c_k=0`,

```text
J_l=[(D-2l)c_l+(l-1)c_(l-1)]/D,        1<=l<=k,

J_l=[(l-k)c_(l-k)+(2k-l)c_(2k-l)]/D,   k+1<=l<=2k-1,

J_(n-l)=J_l.                                           (5.1)
```

The first seam junction has
`J_(k+1)-J_k=c_1/D`; its reflected junction has the opposite increment.
Writing adjacent differences inside each displayed piece as differences of
`c` plus coefficient increments gives

```text
sum_(ell=2)^(n-3)|J_(ell+1)-J_ell|
 <=C TV(0,c_1,...,c_(k-1),0)
   +(C/D)sum_(s=1)^(k-1)|c_s|.                    (5.2)
```

No endpoint from (3.2) is involved in the padding.  Since each normalized
`Phi_s^D` collision profile has mass twelve,

```text
sum_d|c_d|<=12sum_s|A_s|<=24.                     (5.3)
```

Consequently the abstract coefficient BV estimate is sufficient for the
exact restricted CSBV lag norm.

## 6. One-component stabilization, including all boundaries

The Borel adjacent ratio

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2)
```

satisfies `r_j=1+O(1/j)`, `Delta r_j=O(1/j^2)`,
`b_j=Theta(j^-3/2)`, and `|Delta b_j|<=Cb_j/j`.  Therefore, for

```text
Q_r(d)=b_(r-d)/b_r,       d<=r/2,
```

one has uniformly `Q_r(d)<=C`, `|Q_r(d)-1|<=Cd/r`, and
`|Delta Q_r(d)|<=C/r`.

Define, on `d=1,...,k-1` and with zero endpoints,

```text
Z_r(d)=U_r(d)+U_r(D-d),
B_r(d)=(r/R)b_d+4/R.
```

For `r=1`, `U_r` is empty; for `r=2`, its only value is `U_2(1)=0`.
In both cases the endpoint-inclusive variation of `Z_r-B_r` is `O(1/R)`.

Assume `r>=3`.  On `1<=d<r`, direct subtraction gives

```text
U_r(d)-B_r(d)=[e_r(d)-4/r]/R,
e_r(d)=b_d[(r-d-3)Q_r(d)-r].                      (6.1)
```

For `d<=r/2`, the bracket in (6.1) has size `O(d+1)` and adjacent
difference `O(1)`.  Multiplication by `b_d`, using
`|Delta b_d|<=Cb_d/d`, gives `|Delta e_r(d)|<=Cb_d`; its sum is `O(1)`.

For the other half put `a=r-d<r/2`.  Then

```text
e_r(r-a)=(a-3)b_a[b_(r-a)/b_r]-r b_(r-a).         (6.2)
```

The sequence `(a-3)b_a` has size `O(a^-1/2)` and adjacent difference
`O(a^-3/2)`.  The ratio in brackets is bounded and has adjacent difference
`O(1/r)`.  Product variation is therefore

```text
O(1)+(1/r)sum_(a<=r/2)O(a^-1/2)=O(1).
```

The second term of (6.2) has total variation at most
`r b_(ceil(r/2))=O(r^-1/2)`.  These bounds overlap at the midpoint, so the
midpoint jump is included.

If `d>=r`, the direct-row error is `-[r b_d+4]/R`.  Its internal variation
is `O(1/R)`.  At `d=r-1/r`, (6.2) with `a=1` gives an `O(1)` bracket on the
active side, while `r b_r+4=O(1)` on the inactive side; the cutoff costs
`O(1/R)`.  At `d=1`, `r[Q_r(1)-1]=O(1)` controls the zero-endpoint jump.
At `d=k-1`, either the row is inactive or (6.1)--(6.2) bounds its value by
`O(1/R)`, so the other zero endpoint is also safe.

The reflected row is active only when `d>D-r`.  With

```text
a=d-(D-r)=r-(D-d),
```

the restriction `d<=k-1`, `D=2k-1`, `r<=D-1` gives `a<r/2`.  Its bracket is

```text
4(r-1)/r+(a-3)b_a b_(r-a)/b_r.
```

The same first-half product estimate has total variation `O(1)` and
bounded values at both support endpoints.  Division by `R` therefore
controls its internal, support-cutoff, and zero-endpoint variation by
`O(1/R)`.  This proves uniformly

```text
TV(Z_r-B_r)<=C/R.                                  (6.3)
```

For a split `s`, put `V_s=Z_s+Z_(D-s)`.  Since the two reference slopes add
to `D/R`,

```text
TV(V_s-B)<=C/R,
B(d)=(D/R)b_d+8/R.                                (6.4)
```

The endpoint-inclusive variation of `B` is
`2(D/R)b_1+16/R=O(1)`.

## 7. Exact signed cancellation

On the support of `q`, direct subtraction of the two disjoint normalizers
gives

```text
delta_s:=a_F(s)/a_L(s)-1
 =2(k-1)/[R(k-s)(D-s)a_L(s)].                     (7.1)
```

Here `a_L(s)>=1/2` on that restricted support.  The statement is not being
made for every `1<=s<=k-1`; the full-range lower bound needed elsewhere is
`2/9`.  The elementary denominator bounds yield

```text
0<=delta_s<=16/(3k^2).                            (7.2)
```

Because both original split laws normalize,

```text
sum_s W_s
 =sum_s p_s-sum_s q_s(1+delta_s)
 =-sum_s q_s delta_s,                             (7.3)
```

so `|sum W_s|<=16/(3k^2)` and `sum|W_s|<=3`.

For `M=sum_s W_sV_s`, the common profile is canceled before a norm:

```text
M=(sum_sW_s)B+sum_sW_s(V_s-B).
```

Equations (6.4) and (7.3) give

```text
TV(M)<=C/k^2+C/R=O(1/k).                          (7.4)
```

This is the decisive signed step; bounding the raw `V_s` rows separately
would retain the `Theta(1)` variation of `B` and would not prove CSBV.

## 8. First-edge coefficient BV, including `k=3`

The exact laws can be written

```text
p_s=[D/(D-1)]b_s b_(D-s)/b_D,
q_s=[k/(k-1)]b_s b_(k-s)/b_k.
```

For `j=(k-1)/2` and `1<=s<=j`, write `A_s=b_sH_k(s)`.  The ratio-product
form is

```text
H_k(s)=[D/(D-1)]Q_D(s)a_L(s)
       -[k/(k-1)]Q_k(s)a_F(s).                    (8.1)
```

Both products are bounded.  Their difference is `O(s/k)`, each adjacent
increment is `O(1/k)`, the prefactor difference is `O(1/k)`, and the
rational normalizers have increments
`O(1/(ks^2)+1/k^3)`.  Hence

```text
|H_k(s)|<=Cs/k,
|H_k(s+1)-H_k(s)|<=C/k                            (8.2)
```

on the required internal low-range edges.  Together with the Borel
adjacent bound, (8.2) gives

```text
|A_(s+1)-A_s|<=Cb_s/k,
```

whose low-range sum is `O(1/k)`.

For `j<s<=k-1`, `q_s=0`, and both Borel indices in `p_s` are comparable to
`k`.  Thus

```text
p_s=O(k^-3/2),             |Delta p_s|=O(k^-5/2).
```

Here `a_L=O(1)` and `Delta a_L=O(k^-3)`, so this entire bulk has variation
`O(k^-3/2)`.  Both values at the `j/j+1` junction are `O(k^-3/2)`.
The zero endpoints cost `A_1=O(1/k)` and `A_(k-1)=O(k^-3/2)`.

At the minimal rank the formulas are explicit:

```text
k=3:       A_1=-26/75,       A_2=2/25,
TV(0,A_1,A_2,0)=64/75.
```

This is bounded by an absolute constant times `1/k`, so no asymptotic
threshold or omitted small case is present.  Therefore

```text
TV(0,A_1,...,A_(k-1),0)=O(1/k).                   (8.3)
```

## 9. ACBV, CSBV, and clean-room falsification

On the half profile, (4.3) is exactly `c_s=A_s+M(s)`.  Equations (7.4) and
(8.3) prove

```text
TV(0,c_1,...,c_(k-1),0)=O(1/k).
```

Equations (5.2)--(5.3) then prove the exact restricted CSBV vector norm
`O(1/k)` for every odd `k>=3`.

`cleanroom_csbv_audit.py` imports no M282 or predecessor code/data.  It
constructs ordered first-two-factor laws directly from minimal-completion
counts.  At `k=3,5`, it exactly recovers `p,q,a_L,a_F`, (3.1)--(3.2), every
support-pair coefficient in (4.1)--(4.3), every literal ambient coefficient
in (5.1), and the full restricted derivative vector.  In particular it
finds

```text
k=3: CSBV l1=8/25,
k=5: CSBV l1=41858899310941/244990049472000.
```

Its separate high-precision boundary scan tests every `r` through `k=65`;
the largest observed `R TV(Z_r-B_r)` is below `10.20`, including explicit
`r=1,2`, midpoint, cutoff, reflected-support, and zero-endpoint cases.  This
is finite falsification only; Sections 3--8 are the universal proof.

## 10. Numbered objections and exact stop

1. **Material objections to M282:** none.
2. **Nonmaterial objections to M282:** none.
3. **Scope guard:** ACCEPT promotes only `CSBV`.  `CEBV`, `CIBV`, `DOR`,
   `SET`, `PBV`, `FD`, `FCL1`, every bridge/local gap, polynomial mixing,
   and Terminal A/B remain unresolved.

Final verdict: **ACCEPT M282 AS FROZEN AT CSBV SCOPE ONLY.**
