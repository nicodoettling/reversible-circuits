# M248 exact WBE and signed averaged DE theorem

Date: 2026-08-14 UTC.

Status: **proved from frozen, independently accepted inputs, subject to a
fresh audit of this assembly**. This closes exactly WBE and signed averaged
DE for the two literal prefix observables below. It proves no DV, conditional
J2, PCR/WPCR/SCBR, comparison theorem, spectral gap, mixing bound, or
Terminal.

## 1. Exact setting and observables

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
multiplying left-to-right. Let

```text
k >= 3 be odd,       n=3k,       D=2k-1,
R=2k-3,              j=(k-1)/2,  2 <= ell <= (3k-1)/2.
```

The target underlying this fixed-cell calculation is the uniform law on
minimal length-`n-1` transposition factorizations of the ambient cycle
`h=(0,1,...,n-1)`. The B/A objects are M199/M207's normalized literal laws
of two ordered disjoint exterior transpositions in the accepted fixed-cell
response. This is not the global identity bridge and not the lazy
`{3,4,5}` heat-bath kernel.

For a residual permutation after the two exterior transpositions, let
`N_r(d)` count, with multiplicity, its component cycles of size `d` whose
supports have exactly `r` cyclic ambient runs. Define the exact cutoff
observables

```text
X_ell=sum_(2<=d<=ell)[N_1(d)+N_2(d)],
Y_ell=sum_(2<=d<=ell)N_1(d).                       (1.1)
```

Both lie in `[0,3]`. Equal-size faces are counted separately. The literal
laws retain every same/cross kind, both B seams, the X complementary two-run
face, unit gaps, and every collision multiplicity.

## 2. Raw blocks and signed averaged response

Put

```text
b_r=e^(-r)r^(r-1)/r!,
q_s=[k/(k-1)]b_s b_(k-s)/b_k,        1<=s<=j,
gamma_L(s)=2[2-1/s-1/(D-s)]/R,
gamma_F(s)=2[2-1/s-1/(k-s)]/R,
a_L(s)=1-gamma_L(s),
a_F(s)=1-gamma_F(s),
qhat_s=q_s a_F(s).                                  (2.1)
```

The accepted half-convolution gives `sum_s q_s=1`; `qhat` is the original
unnormalized disjoint submeasure and is not divided by its total mass.

For `Z=X_ell,Y_ell`, write the exact raw B/A disjoint numerators as

```text
B_s^Z=a_L(s)Phi_s^D(Z),       A_s^Z=a_F(s)Psi_s^D(Z).
```

Use exactly M217/M222's literal partition

```text
B_s^Z=B_(s,surv)^Z+B_(s,frag)^Z,
A_s^Z=A_(s,surv)^Z+A_(s,frag)^Z.                  (2.2)
```

For Y this separates the displayed one-run surviving terms from the exact
fragmentation/untouched terms. For X, `frag` is defined as the full literal
numerator minus the exact surviving one-run terms; it therefore still
contains the complementary two-run face, every seam and kind, and every
collision multiplicity. Define

```text
S_Z=sum_s q_s[B_(s,surv)^Z-A_(s,surv)^Z],
K_Z=sum_s q_s[B_(s,frag)^Z-A_(s,frag)^Z],
N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z,              (2.3)

DE_Z=sum_s qhat_s[Phi_s^D(Z)-Psi_s^D(Z)].         (2.4)
```

Accepted M217/M222 proves the exact signed identity

```text
DE_Z=S_Z+K_Z+N_Z.                                  (2.5)
```

No absolute value has been moved inside the `s` sum.

## 3. Theorem

For every integer in the domain of Section 1,

```text
|S_(Y_ell)+K_(Y_ell)| <=7000 sqrt(ell)/k,          (3.1)
|S_(X_ell)+K_(X_ell)| <=7160 sqrt(ell)/k.          (3.2)
```

Thus WBE is proved for both exact observables. Moreover,

```text
|N_Z|<=16/k^2,                    Z=X_ell,Y_ell,    (3.3)

|DE_(Y_ell)|<=7004 sqrt(ell)/k,                    (3.4)
|DE_(X_ell)|<=7164 sqrt(ell)/k.                    (3.5)
```

In particular, the common explicit constant `7164` proves signed averaged
DE for both observables.

## 4. Proof of WBE

M226/M229 collects the complete raw surviving and fragmentation terms before
taking any absolute value. With `c^Y_(k,y)` denoting its exact one-run B-minus-A
coefficient, equations (2.1)--(2.6) of that frozen reduction give

```text
S_(Y_ell)+K_(Y_ell)=sum_(y=2)^ell c^Y_(k,y).       (4.1)
```

M239/M246 proves on the full stated domain

```text
|sum_(y=2)^ell c^Y_(k,y)|<=7000 sqrt(ell)/k.       (4.2)
```

Equations (4.1)--(4.2) prove (3.1).

Let `c^T_(k,y)=T^B_(k,y)-T^A_(k,y)` be M226/M229's exact signed raw
coefficient of the unique complementary two-run face. This definition keeps
the original ordered tuple, q weight, same/cross kind, both seams, and each
equal-size occurrence. Its exact X-minus-Y identity is

```text
[S_(X_ell)+K_(X_ell)]-[S_(Y_ell)+K_(Y_ell)]
   =sum_(y=2)^ell c^T_(k,y).                       (4.3)
```

M235/M238 proves

```text
|sum_(y=2)^ell c^T_(k,y)|<=160 sqrt(ell)/k.        (4.4)
```

Equations (3.1), (4.3), and (4.4), followed by one triangle inequality,
give

```text
|S_(X_ell)+K_(X_ell)|
 <=(7000+160)sqrt(ell)/k
 =7160sqrt(ell)/k,
```

which proves (3.2). This is the only triangle inequality used to pass from
the accepted coefficient moments to WBE; it does not split literal kinds or
profiles.

## 5. Explicit normalizer remainder and DE

M217/M222's exact algebra gives, for every `1<=s<=j`,

```text
a_F(s)/a_L(s)-1
 =2(k-1)/[R(k-s)(D-s)a_L(s)].                     (5.1)
```

Here

```text
R>=k,
k-s>=(k+1)/2,
D-s>=(3k-1)/2,
a_L(s)>=1/2.
```

Consequently

```text
a_F(s)/a_L(s)-1
 <=16(k-1)/[k(k+1)(3k-1)]
 <=16/(3k^2),                                      (5.2)
```

where the second inequality is equivalent to
`3k(k-1)<=(k+1)(3k-1)`, whose right-minus-left side is `5k-1>0`.

Since `0<=Phi_s^D(Z)<=3` and `0<=a_L(s)<=1`, one has
`0<=B_s^Z<=3`. Using `sum_s q_s=1` in (2.3), (5.2) yields

```text
|N_Z|<=sum_s q_s [16/(3k^2)]3=16/k^2,             (5.3)
```

proving (3.3). Finally `k>=3` and `ell>=2` imply
`k^2 ell>=18>16`. Squaring only nonnegative quantities shows

```text
16/k^2 <=4sqrt(ell)/k.                             (5.4)
```

Insert (3.1)--(3.3) into the exact identity (2.5), then use (5.4):

```text
|DE_(Y_ell)|<=(7000+4)sqrt(ell)/k,
|DE_(X_ell)|<=(7160+4)sqrt(ell)/k.
```

This proves (3.4)--(3.5). The separate Abel endpoint
`-6(k-1)/[k(2k-1)(2k-3)]` belongs to M192's outer identity, not to DE;
it is neither omitted nor used here.

## 6. Dependency and scope ledger

- **Proved and independently accepted:** M217/M222 exact
  `DE=S+K+N` identity and normalizer estimate; M226/M229 coefficient
  identities, with `G_k` restricted to its corrected used domain;
  M235/M238 TCM with constant `160`; M239/M246 YCM with constant `7000`.
- **New proved step:** exact assembly of YCM and TCM into WBE constants
  `7000,7160`, the explicit `16/k^2` remainder, and signed averaged DE
  constants `7004,7164`.
- **Unproved assumptions used here:** none.
- **Smallest rank:** `k=3` is included in every accepted input and in the
  absorption (5.4); there is no asymptotic threshold.
- **Outside scope:** DV remains open. Therefore this theorem does not infer
  conditional J2, PCR/WPCR/SCBR, any comparison or chain-gap statement,
  polynomial mixing, or either Terminal.

