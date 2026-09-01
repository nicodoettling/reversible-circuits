# M279 fresh proof audit of M276's append-only M272 salvage

Date: 2026-08-14 UTC.

## 1. Split verdict and strict scope

```text
M276 APPEND-ONLY SALVAGE: ACCEPT.
MATERIAL OBJECTIONS TO M276: NONE.
NONMATERIAL OBJECTIONS TO M276: NONE.

M272 AS FROZEN: REMAINS REJECTED FOR ITS MATERIAL J1 BV PROOF GAP.
```

M276 proves the corrected channel-one collision derivative `O(1/k)` and
correctly retains only the unaffected exact coupling, phase, and channel-two
reductions from M272.  This does not mutate or rehabilitate M272's frozen
self-contained proof package.

The setting is odd `k>=3`, `n=3k`, the balanced first fixed cell of the
auxiliary uniform minimal-factorization law, and the nonlazy cyclic rank-two
quotient kernel.  Composition is `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.  This is not the global identity-word target or its lazy exact
same-product `{3,4,5}` heat-bath chain.

## 2. Immutable provenance

Every payload in every cited inventory verifies.  The independently computed
inventory-file digests are

```text
M276  882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M272  af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270  6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
```

The dependency boundary is respected.  M91 supplies the normalized
two-channel/Borel decomposition and exact measure Abel identity; M94 supplies
the Borel coefficient scales; M261/M264 supply the exact PBV and affine
collision/decorated reduction; M267/M270 supply the literal endpoint-profile
normalization and PBV/SET equivalence.  None supplies M276's new tail proof.

## 3. M272's material near-end error

M272 defines, for the short exterior cycle,

```text
rho_A(a)=(k-a)nu_k(a),       1<=a<k.
```

At the last point before the endpoint,

```text
rho_A(k-1)=nu_k(k-1)=nu_k(1)
 =(k-1)^(k-3)/k^(k-2)
 =(1/k)(1-1/k)^(k-3).                              (3.1)
```

Thus `k rho_A(k-1)->e^-1`, whereas
`k^(3/2)rho_A(k-1)` diverges like `e^-1 sqrt(k)`.  This term is
`Theta(1/k)`, not `O(k^-3/2)`.

The point `a=k-1` lies in M272's asserted range `k/2<a<=k`, where it says
all Borel indices are comparable to `k` and every summand is
`O(k^-3/2)`.  Its next displayed estimate begins only at `a>k`, where
`rho_A=0`, and therefore does not cover the missing short-cycle tail.  The
omitted bound is essential to M272's Proposition 3.  M276 correctly treats
this as a material rejection of M272 as frozen.

## 4. Independent weighted-Borel repair

Write

```text
b_j=e^-j j^(j-1)/j!,
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2),
R_k(c)=b_(k-c)/b_k=product_(i=0)^(c-1)r_(k-i).
```

The logarithmic expansion gives, uniformly for `j>=2`,

```text
log r_j=O(1/j),
r_j=1+O(1/j),
|r_(j+1)-r_j|=O(1/j^2).                            (4.1)
```

For `1<=c<k/2`, summing `(4.1)` over `k-c+1,...,k` shows

```text
R_k(c)=O(1),
|R_k(c+1)-R_k(c)|=R_k(c)|r_(k-c)-1|=O(1/k).         (4.2)
```

Stirling gives `b_c=O(c^-3/2)`.  If `h_c=c b_c`, then

```text
h_(c+1)/h_c=(1+1/c)/r_(c+1)=1+O(1/c),
```

so

```text
h_c=O(c^-1/2),
|h_(c+1)-h_c|=O(c^-3/2).                           (4.3)
```

By symmetry of `nu_k`, the omitted tail is exactly

```text
g_k(c):=rho_A(k-c)=c nu_k(c)
       =h_c R_k(c)/(k-1),       1<=c<k/2.           (4.4)
```

Combining `(4.2)--(4.4)` gives

```text
g_k(c)=O(1/[k sqrt(c)]),
|g_k(c+1)-g_k(c)|
 =O(1/[k c^(3/2)]+1/[k^2 sqrt(c)]).                (4.5)
```

The two series in `(4.5)` sum respectively to `O(1/k)` and
`O(k^-3/2)`.  The endpoint `g_k(1)=O(1/k)` closes against
`g_k(0)=0`.  Hence the complete short-cycle `A` tail, including its endpoint
jump, has total variation `O(1/k)`.

## 5. The other ranges and both junctions

For `1<=a<=h=(k-1)/2`, direct substitution gives M272's exact

```text
delta rho(a)=b_a H_k(a).
```

On this range all `R_m(a)` are bounded, and
`R_m(a+1)=R_m(a)r_(m-a)`.  The leading constants in the three terms of
`H_k` cancel; affine coefficient differences, `(4.1)`, and the difference
between the `m=k` and `m=2k-1` products give

```text
|H_k(a)|=O(a/k),
|H_k(a+1)-H_k(a)|=O(1/k).
```

Since `|b_(a+1)-b_a|=O(b_a/a)` and `sum_a b_a<infinity`, this low range,
including the zero boundary, contributes `O(1/k)` variation.

For the long-cycle `B` contribution on `h<a<=k`, all four Borel indices in
its two fragments really are comparable to `k`.  A per-chord mass is
`O(k^-5/2)` and an adjacent difference is `O(k^-7/2)`.  The counts are
piecewise linear, have value `O(k)` and adjacent difference `O(1)`, so this
whole central range has value `O(k^-3/2)`, adjacent difference
`O(k^-5/2)`, and total variation `O(k^-3/2)`.

For `k<a<=2k-1`, setting `c=2k-a` gives exactly

```text
rho_B(a)=c nu_(2k-1)(c).
```

Here `1<=c<=k-1<(2k-1)/2`, so the proof of `(4.5)` applies with denominator
`2k-2`; this tail and its zero endpoint have variation `O(1/k)`.

At the low/near-tail junction, both neighboring values are
`O(k^-3/2)`.  At the central/far junction one has the stronger exact equality

```text
rho_B(k)=(k-1)nu_(2k-1)(k-1)=rho_B(k+1),            (5.1)
```

using symmetry of `nu_(2k-1)`.  The only `Theta(1/k)` jump near `a=k` is
the short-cycle endpoint already included through `g_k(0)=0`.

Consequently M276 correctly proves

```text
sum_a |Delta[rho_B-rho_A](a)|=O(1/k).               (5.2)
```

## 6. Corrected channel-one/J1 theorem

For disjoint exterior and middle chords the collision profile expands
exactly as

```text
eta_1(I_ell)=delta rho(ell)+delta rho(n-ell)
 +(delta a*m)(ell)+(m*delta a)(ell).                (6.1)
```

The two face terms have circular variation at most twice `(5.2)`.  The
literal endpoint intensities give

```text
||delta a||_1=2/k,           ||Delta m||_1=4/k.
```

Therefore each convolution derivative costs at most `8/k^2`, and both cost
at most `16/k^2`.  Restricting circular lags to `2,...,n-3` cannot increase
the norm.  Hence the append-only corrected result is

```text
sum_(ell=2)^(n-3)
 |eta_1(I_(ell+1)-I_ell)|=O(1/k).                  (6.2)
```

This theorem is proved by M276, not by frozen M272.

## 7. Unaffected raw laws, coupling, and phase

For a residual permutation `Q` of transposition rank `r`, cycle sizes
`d_i`, and `tau(d)=d^(d-2)/(d-1)!`, exact completion counting gives

```text
F_r(Q)=r! product_i tau(d_i),
nu_Q(e)=F_(r-1)(e^-1Q)/F_r(Q),
N_Q(e,f)=F_(r-2)((ef)^-1Q)/F_r(Q).
```

Summing completions proves `sum_e nu_Q(e)=1` and
`sum_f N_Q(e,f)=nu_Q(e)`.  Thus every `Phi,Psi` law is normalized.  In
channel two for `F=C_-C_+`, the fair first-component choice is already in
`N_F`; adding another `1/2` would double-count it.

The color probabilities

```text
alpha_0=m(m-1)/[3m(3m-1)],
alpha_1=4m^2/[3m(3m-1)],
alpha_2=2m(2m-1)/[3m(3m-1)]
```

sum to one, and the `J=0` law is literally common.  The odd-cycle split laws

```text
p_s=(2k-1)nu_(2k-1)(s),
q_s=k nu_k(s)  for s<k/2
```

also normalize.

With `D_u=sum_(s<=u)(p_s-q_s)<0`, the common-uniform quantile coupling has
`S<=T` and

```text
Pr(S<=u<T)=Pr(S<=u)-Pr(T<=u)=-D_u.                 (7.1)
```

Maximal initial embedding couplings and the normalized adjacent kernels may
be disintegrated and composed.  Every reached level has its declared
`Phi_u` marginal, so telescoping gives, with the correct sign,

```text
E[g(X_T)-g(Y_S)]
 =sum_s q_s[Phi_s-Psi_s](g)
  +sum_u D_u[Phi_u-Phi_(u+1)](g).                  (7.2)
```

Equation `(7.2)` is an expectation identity, not a pathwise response order.

For the null-extended owner charge,

```text
E_ell(a)=sum_x[kappa(o(x-ell),o(x+1))
                  -kappa(o(x-ell),o(x))].
```

Averaging the `n` literal phases gives exactly `E_ell(a)/n`.  A short cyclic
orbit is repeated by its stabilizer, so there is no additional orbit-size
factor.  Applying this profile map to `(7.2)` gives

```text
sum_K<w,T_(K,ell)>
 =1/n sum_j alpha_j E_j[E_ell(X_T)-E_ell(Y_S)].     (7.3)
```

The good/bad first-edge indicators literally partition the two raw source
spaces before absolute values.  Their sum is the complete response; the
finite nonzero good vector refutes a seam-only equality but not any future
signed seam inequality.

## 8. Unaffected channel-two/J2 reduction

After a first chord of smaller split `s`, the two marked residual components
have sizes `s` and `d-s`.  A size-`r` component is selected for the second
factor with probability `(r-1)/(2k-3)`, and its marked vertex has endpoint
intensity `2/r`.  Therefore

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                (8.1)
```

Equivalently counting ordered adjacent pairs in the one-tree and two-tree
Cayley models gives

```text
sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].             (8.2)
```

Each shared-endpoint product is a triangle whose restricted collision
derivative has `l1<=12`.  Applying a triangle inequality only to the two
positive shared submeasures in `(8.2)` proves the complete shared contribution
is `O(1/k)`.

For the disjoint masses

```text
p_hat_s=p_s(1-gamma_L(s)),
q_hat_s=q_s(1-gamma_F(s)),
E_u=sum_(s<=u)(p_hat_s-q_hat_s),
```

the unequal total masses give the indispensable endpoint

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].                   (8.3)
```

Adding and subtracting `sum q_hat_s Phi_s^D` and summing by parts
coordinatewise gives the exact vector identity

```text
R_D=E_(k-1)Phi_(k-1)^D
 +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D)
 +sum_(s<k/2)q_hat_s(Phi_s^D-Psi_s^D).             (8.4)
```

The endpoint `(8.3)` cannot be dropped.  The accepted cumulative Borel bound
and the `O(1/k)` shared masses give `|E_u|=O(sqrt(u)/k)`, but termwise
absolute values in `(8.4)` would require an unproved stronger derivative
norm.  M276 correctly makes no such inference.

## 9. Clean-room checks, objections, and exact stop

M279's `cleanroom_salvage_check.py` imports no project/predecessor module and
reads no M276/M272 data.  It independently checks:

- first and ordered-first-two completion normalization for a 7-cycle and a
  `3+4` residual;
- normalized `p,q`, quantile order, and every `-D_u` crossing at
  `k=3,5,9`;
- the phase `1/n`, both shared masses, endpoint `(8.3)`, and vector Abel
  identity at the same ranks; and
- the exact flaw, `g_k` identity, both endpoint closures, and full
  `delta rho` variation at `k=3,5,9,31,101`.

All checks pass.  The normalized result digest is

```text
39f879bc696d59f5d850ad7d39c9352eb7626353d0d4d18480feaefd8f649cf9.
```

The raw result file has SHA-256
`70d04754804085daa453339013edd4de72945b32dc6a2011f84eb962cc87c718`.
These are finite calibration only.

M276's own checker has only standard-library imports and a single write to
its requested output path; it reads no file.  Replaying it to `/tmp` produces
the frozen result byte-for-byte, with SHA-256
`99611a4d3fa23cb6d092f89da9fbeff0ff5ef2d828d3fd2b1440d1bc09b16f09`.

### Numbered objections

1. **Material objections to M276:** none.
2. **Nonmaterial objections to M276:** none.
3. **Material objection to M272:** the frozen near-end `A`-tail gap in
   Section 3 remains; M276's append-only proof does not alter that verdict.

The exact surviving hierarchy is

```text
CSBV + CEBV => CIBV,
CIBV + DOR  => PBV <=> SET.
```

`CSBV`, `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, `FD`, `FCL1`, every bridge or
local sampler gap, polynomial mixing, and both Terminals remain unresolved.
No M276 statement licenses their promotion.
