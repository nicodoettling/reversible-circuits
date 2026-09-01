# M276 clean-room proof audit of M272

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
VERDICT ON M272 AS A FROZEN SELF-CONTAINED PACKAGE: REJECT.

MATERIAL OBJECTION: THE CLAIMED CHANNEL-ONE BOUNDED-VARIATION PROOF
OMITS THE SHORT-CYCLE A-TAIL AND MAKES A FALSE BULK-SIZE ASSERTION.

APPEND-ONLY M276 SALVAGE: THE OMITTED TAIL HAS VARIATION O(1/k), SO THE
CHANNEL-ONE THEOREM ITSELF IS PROVED HERE WITH THE GAP REPAIRED.
```

All other audited M272 identities survive.  The setting is odd `k>=3`,
`n=3k`, the balanced first fixed cell of the auxiliary uniform
minimal-factorization law of the long cycle, and M73's nonlazy cyclic
rank-two quotient kernel.  Composition is `(pq)(x)=p(q(x))`, with displayed
factors left-to-right.  This is not the global identity-word law or the lazy
same-product `{3,4,5}` heat-bath chain.

The mission-level target remains

```text
sum_(ell=2)^((n-3)/2) |sum_K <w,T_(K,ell)>|=O(n^-2). (SET)
```

It is not proved here or in M272.

## 2. Immutable provenance

The SHA-256 digest of M272's checksum inventory is exactly

```text
af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3.
```

Every named M272 payload passes.  The declared M91, M94, M261, M264, and
M267 inventories also pass, with the digests recorded in `checkpoint.md`.
The transitive M270 inventory passes and its frozen report accepts M267 only
at its stated endpoint-profile scope.  No predecessor was modified.

## 3. Raw laws and channel normalizations

For a residual permutation `Q` of transposition rank `r`, with cycle sizes
`d_1,...,d_c`, the exact minimal-factorization count is

```text
F_r(Q)=r! product_i tau(d_i),
tau(d)=d^(d-2)/(d-1)!,  tau(1)=1.
```

Consequently the first-factor and ordered-first-two-factor laws are

```text
nu_Q(e)=F_(r-1)(e^-1 Q)/F_r(Q),
N_Q(e,f)=F_(r-2)((ef)^-1 Q)/F_r(Q).                 (3.1)
```

Summing the completion count over the legal next transposition gives

```text
sum_e nu_Q(e)=1,             sum_f N_Q(e,f)=nu_Q(e). (3.2)
```

Thus M272's channel-two conditional law

```text
c_(u,r)(f)=N_L(e_(u,r),f)/nu_L(e_(u,r))
```

is normalized.  For channel one, conditioning a chord of the odd
`(2k-1)`-cycle `L` on smaller split `u` leaves a uniform phase among its
`2k-1` chords and an independent normalized middle factor.

Put `m=k-1`, `R=3m`.  Sampling the first two residual colors without
replacement gives

```text
alpha_0=m(m-1)/[R(R-1)],
alpha_1=4m^2/[R(R-1)],
alpha_2=2m(2m-1)/[R(R-1)].                          (3.3)
```

The `J=0` law is literally common.  The live normalized laws are

```text
H_(1,B)=Law(E_L E_M),       H_(1,A)=Law(E_F E_M),
H_(2,B)=Law(first two of L),
H_(2,A)=Law(first two of F),                            (3.4)
```

where `F=C_-C_+`.  In channel one the `F` edge chooses the two equal-rank
components fairly.  In channel two that fair choice is already contained in
`N_F`; inserting another `1/2` would be wrong.

For a specified chord of an odd `d`-cycle, let

```text
nu_d(s)=tau(s)tau(d-s)/[(d-1)tau(d)].                (3.5)
```

There are `d` chords of smaller split `s`, hence

```text
p_s=(2k-1)nu_(2k-1)(s),       1<=s<=k-1,
q_s=k nu_k(s),                 1<=s<k/2.             (3.6)
```

Both normalize.  Dividing the raw laws by `p_s` or `q_s` therefore makes
every `Phi_(j,s),Psi_(j,s)` a probability law, including channel two's
ordered lifts and completion weights.  This independently confirms the raw
laws and all channel normalizations used by M272.

## 4. Quantile transport, crossing sign, and telescoping

Let

```text
D_u=sum_(s<=u)(p_s-q_s).
```

M91/M94's likelihood-ratio calculation gives `D_u<0` for
`1<=u<=k-2` and `D_(k-1)=0`.  Therefore

```text
Pr(T<=u)=sum_(t<=u)p_t <=sum_(s<=u)q_s=Pr(S<=u).
```

The common-uniform quantile coupling has `S<=T` almost surely.  Since this
order makes `{T<=u}` a subset of `{S<=u}`,

```text
Pr(S<=u<T)=Pr(S<=u)-Pr(T<=u)=-D_u.                  (4.1)
```

The adjacent channel-one coupling shares phase and middle chord.  The
adjacent channel-two maximal coupling has the normalized conditional laws
from (3.2) as its two marginals.  At the initial embedding level, maximal
coupling on the common ambient raw-atom space gives the required
`Psi_(j,s),Phi_(j,s)` marginals; channel one may share the independent
middle factor.

Disintegrate these couplings to Markov kernels and compose from `S=s` to
`T=t`.  Every reached `X_u` has marginal `Phi_(j,u)`, while `Y_s` has
marginal `Psi_(j,s)`.  Telescoping a test function `g` along the path and
using (4.1) gives exactly

```text
E[g(X_T)-g(Y_S)]
 =sum_s q_s[Phi_(j,s)-Psi_(j,s)](g)
  +sum_u D_u[Phi_(j,u)-Phi_(j,u+1)](g).             (4.2)
```

Thus M272's sign is correct: a crossed edge contributes
`(-D_u)(Phi_(u+1)-Phi_u)=D_u(Phi_u-Phi_(u+1))`.
Combining (4.2) with (3.3)--(3.4) proves

```text
eta(g)=sum_(j=1)^2 alpha_j E_j[g(X_T)-g(Y_S)].       (4.3)
```

This is an expectation identity, not pathwise response order.

## 5. Owner charge and the outside phase factor

For a supported product `a`, extend the residual-cycle owner by a null owner
at support heads.  With null-owner `kappa=0`, define

```text
e_(ell,x)(a)
 =kappa(o_a(x-ell),o_a(x+1))-kappa(o_a(x-ell),o_a(x)),
E_ell(a)=sum_(x mod n)e_(ell,x)(a).                  (5.1)
```

Choosing the literal cyclic phase uniformly and retaining the intermediate
kind gives

```text
P_(K,ell)(a)=1[K(a)=K](1/n)sum_x delta_(sigma_a(ell,x)),
sum_K<w,P_(K,ell)(a)>=E_ell(a)/n.                   (5.2)
```

The all-`n` phase average repeats a short quotient orbit by precisely its
stabilizer, so (5.2) needs no extra orbit correction.  Applying the profile
map to (4.3) yields the audited normalization

```text
sum_K<w,T_(K,ell)>
 =1/n sum_(j=1)^2 alpha_j
      E_j[E_ell(X_T)-E_ell(Y_S)].                   (5.3)
```

The factor is `1/n`, not `n` or `1/o_a`.  Both kinds and both channels
remain inside the final scalar.

## 6. Literal phase partition and exact refutation

For `U_-={1,...,k-1}` and `U_+={2k,...,3k-1}`, the indicators

```text
b_B(e)=1[e joins U_- to U_+],
b_A(e)=1[0 is an endpoint of e]                     (6.1)
```

partition the respective first-edge spaces.  Grouping the complete raw
channel law by (6.1) proves

```text
eta(E_ell)=eta_good(E_ell)+eta_bad(E_ell)            (6.2)
```

before every absolute value.  There is no cancellation premise in this
identity.

The clean-room checker reconstructs (6.2) directly from (3.1), with no M272
input.  At `k=3,ell=2` it obtains

```text
eta_good(E_2)=8042647144727/367569090000000 !=0,
eta_bad(E_2) =308462023343/73513818000000.
```

Hence the universal seam-only equality is refuted exactly.  This does not
refute a future seam-weighted inequality.

## 7. Channel-one collision law

For the exterior face not containing the middle block, direct chord
classification gives

```text
rho_A(a)=(k-a)nu_k(a),

rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1),  (7.1)
```

with M272's displayed `S_k,C_k`.  The endpoint intensities are

```text
a_B=2/(2k-1) on U_- union U_+,
a_A=1/k on {0} union U_- union U_+,
m=2/k on {k,...,2k-1}.                              (7.2)
```

Thus `||a_B-a_A||_1=2/k` and `||Delta m||_1=4/k`.  Expanding the support
collision profile of two disjoint channel-one chords proves

```text
eta_1(I_ell)=delta rho(ell)+delta rho(n-ell)
 +(delta a*m)(ell)+(m*delta a)(ell).                (7.3)
```

The exact clean-room check verifies (7.3) at every circular lag for
`k=3,5`.

### Material defect in the frozen M272 proof

M272 next claims that, throughout `k/2<a<=k`, all Borel indices in (7.1)
are comparable to `k` and every summand is `O(k^-3/2)`.  This is false for
the short-cycle term.  At the endpoint,

```text
rho_A(k-1)=nu_k(1)
 =(k-1)^(k-3)/k^(k-2)=Theta(1/k),                   (7.4)
```

not `O(k^-3/2)`.  M272's displayed far-tail estimate (3.7) is stated only
for `k<a<=2k-1`, where `rho_A=0` and
`rho_B=c nu_(2k-1)(c)`.  It does not literally cover (7.4) or prove the
variation of the omitted `A` tail.  Because that tail bound is essential to
the claimed proposition, this is a material self-contained-proof objection
under the frozen-package standard.

### Append-only corrected bounded-variation theorem

The theorem is nevertheless true.  Here is the missing proof, combined
with a clean partition of all ranges.

Let

```text
b_j=e^-j j^(j-1)/j!,
r_j=b_(j-1)/b_j,
R_d(c)=b_(d-c)/b_d=product_(i=0)^(c-1)r_(d-i).
```

Stirling and the logarithmic expansion give, uniformly for `j>=2`,

```text
b_j<=Cj^-3/2,
r_j=1+O(1/j),
|r_(j+1)-r_j|<=C/j^2.                               (7.5)
```

For `1<=a<=k/2`, substitution in (7.1) yields M272's exact
`delta rho(a)=b_a H_k(a)`.  The product formula in (7.5), cancellation of
the constant terms, and one adjacent difference give

```text
|H_k(a)|<=Ca/k,             |H_k(a+1)-H_k(a)|<=C/k.
```

Since `|b_(a+1)-b_a|<=Cb_a/a`, this range contributes `O(1/k)` to
`TV(delta rho)`.

For the omitted short-cycle tail, put `c=k-a`, so

```text
rho_A(k-c)=g_k(c):=c nu_k(c)
 =c b_c R_k(c)/(k-1),        1<=c<k/2.              (7.6)
```

The products `R_k(c)` are uniformly bounded for `c<=k/2`, and

```text
|R_k(c+1)-R_k(c)|<=C R_k(c)/k,
|(c+1)b_(c+1)-c b_c|<=C c^-3/2.
```

Therefore

```text
g_k(c)<=C/(k sqrt(c)),
|g_k(c+1)-g_k(c)|
 <=C/[k c^(3/2)]+C/[k^2 sqrt(c)].                  (7.7)
```

Including the boundary `g_k(0)=0`, summing (7.7) proves that the complete
omitted `A` tail has variation `O(1/k)`.

On `k/2<a<=k`, the two `rho_B` Borel fragments really do have all indices
comparable to `k`.  A per-chord mass is `O(k^-5/2)` and its adjacent
difference is `O(k^-7/2)`; multiplying by the piecewise-linear counts gives
value `O(k^-3/2)`, adjacent difference `O(k^-5/2)`, and total variation
`O(k^-3/2)`.  For `k<a<=2k-1`, put `c=2k-a`; then
`rho_B(a)=c nu_(2k-1)(c)`, and the same calculation as (7.6)--(7.7) gives
variation `O(1/k)`.  The junction values obey the neighboring bounds.

Combining the low cancellation range, the corrected `A` tail, the `B` bulk,
and the `B` far tail proves

```text
sum_a |delta rho(a+1)-delta rho(a)|=O(1/k).          (7.8)
```

Finally, (7.2)--(7.3) and
`||Delta(f*g)||_1<=||f||_1||Delta g||_1` show that the two cross terms cost
at most `16/k^2`.  Hence the append-only corrected theorem is

```text
sum_(ell=2)^(n-3)|eta_1(I_(ell+1)-I_ell)|=O(1/k).   (7.9)
```

Equation (7.9) is proved in M276, but it requires fresh audit before
coordinator promotion.

## 8. Channel-two triangle and vector Abel audit

Let `Lambda_G(e,f)=N_G(e,f)` for `G=L,F`.  Condition on the smaller first
split `s`.  After the first chord, its two endpoint marks lie in components
of sizes `s` and `d-s`.  A size-`r` residual component is chosen for the
second factor with probability `(r-1)/(2k-3)`, and the marked vertex has
endpoint intensity `2/r`.  Therefore

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                 (8.1)
```

Equivalently counting an ordered adjacent edge pair in the Cayley tree gives

```text
sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].              (8.2)
```

Each shared-endpoint product is a triangle.  Its nonzero collision profile
has mass six, so the restricted derivative vector has `l1<=12`.  Applying a
triangle inequality only to the two positive shared-endpoint submeasures in
(8.2) proves their complete signed difference is `O(1/k)`.

For the disjoint submasses set

```text
p_hat_s=p_s(1-gamma_L(s)),
q_hat_s=q_s(1-gamma_F(s)),
E_u=sum_(s<=u)(p_hat_s-q_hat_s).                    (8.3)
```

The unequal total disjoint masses give the required endpoint

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].                   (8.4)
```

Adding and subtracting `sum_s q_hat_s Phi_s^D`, then applying ordinary
summation by parts coordinatewise, gives

```text
R_D=E_(k-1)Phi_(k-1)^D
 +sum_(u=1)^(k-2)E_u(Phi_u^D-Phi_(u+1)^D)
 +sum_(s<k/2)q_hat_s(Phi_s^D-Psi_s^D).              (8.5)
```

The endpoint (8.4) may not be deleted.  The bound
`|E_u|<=C sqrt(u)/k` follows from the accepted local bound on `D_u` and the
`O(1/k)` total shared masses.  It does not license termwise absolute values
in (8.5).

The independent checker verifies (8.1)--(8.5) exactly at `k=3,5`; both
M272 reruns reproduce their frozen `k=3,5,7` result arrays exactly.
No asymptotic conclusion is drawn from those rows.

## 9. Exact remaining hierarchy

After the append-only channel-one repair, the channel-two shared-endpoint
part is proved and the following signed vectors remain open:

```text
(CSBV)
||E_(k-1)Phi_(k-1)^D
 +sum_u E_u(Phi_u^D-Phi_(u+1)^D)||_1=O(1/k),

(CEBV)
||sum_(s<k/2)q_hat_s(Phi_s^D-Psi_s^D)||_1=O(1/k).  (9.1)
```

If both estimates in (9.1) hold,
the complete channel-two collision coefficient is `O(1/k)`.  Together with
(7.9), this would prove the channel-combined collision obligation `(CIBV)`.
It would still leave the decorated owner-ratio obligation

```text
(DOR) sum_(ell=2)^(n-3)|eta(Delta Q_ell)|=O(1/k)    (9.2)
```

or a joint collision/decorated estimate.  Therefore

```text
CSBV + CEBV  => CIBV,
CIBV + DOR   => PBV <=> SET,
```

while every premise displayed on the left remains unresolved except the
repaired channel-one and shared-triangle pieces.

No FCL1, direct L1, H0, bridge gap, local sampler gap, polynomial mixing, or
Terminal conclusion follows.
