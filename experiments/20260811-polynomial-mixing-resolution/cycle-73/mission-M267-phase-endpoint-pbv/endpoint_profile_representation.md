# Literal endpoint-profile representation for PBV

Date: 2026-08-14 UTC.

Status: Propositions 1--3 below are **proved exact identities**.  The signed
endpoint transport estimate `(SET)` is **unresolved**.  No finite computation
was used to derive the identities.

## 1. Scope and accepted notation

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Put `n=3k`, where `k>=3` is odd, and

```text
h=(0 1 ... n-1),             E_r=(r,r+1)  (mod n).
```

The target here is only the uniform minimal length-`n-1` factorization law
of `h` under M73's nonlazy cyclic rank-two quotient kernel.  It is not the
global identity-word law and not the lazy exact same-product `{3,4,5}`
heat-bath chain.

For a supported rank-two product `s`, let `q_s=s^-1 h`, let
`mathcal C_s` be its three residual cycles, and let `K(s)` be its intermediate
kind `T` or `D`.  Extend M261's owner map by a null owner:

```text
o_s(r)=C in mathcal C_s,  if s(r+1)=r+1 and r lies in C,
o_s(r)=empty,             otherwise.                 (1.1)
```

Thus `o_s(r)` is the owner of the generic boundary edge `E_r`; the null
positions are exactly the support heads of `s`.  For residual owners `C,D`,
put

```text
kappa_s(C,C)=tau(|C|-2)/tau(|C|),
kappa_s(C,D)=tau(|C|-1)tau(|D|-1)/[tau(|C|)tau(|D|)]  (C!=D),
kappa_s(C,empty)=kappa_s(empty,D)=0,                  (1.2)
```

with an invalid shifted size interpreted as zero.  This keeps the literal
same-owner/cross-owner rooted-tree coefficient; it is not replaced by its
`e^-2` limit.

## 2. Jump-owner formula

For `2<=ell<=n-3`, define the charge at the literal cyclic location `x` by

```text
e_(ell,x)(s)
 =kappa_s(o_s(x-ell),o_s(x+1))
  -kappa_s(o_s(x-ell),o_s(x)).                       (2.1)
```

### Proposition 1 (proved: literal endpoint law)

M261's endpoint observable is exactly

```text
E_ell(s)=sum_(x mod n)e_(ell,x)(s).                  (2.2)
```

Only jump locations `x`, for which `o_s(x)!=o_s(x+1)`, contribute.  Formula
`(2.2)` retains the positive and negative endpoint of every one-run/two-run
owner interval, the displacement `ell`, and the owner-pair coefficient
`kappa_s`.

#### Proof

M261's accepted definition is

```text
E_ell(s)=sum_(C,D in mathcal C_s) kappa_s(C,D)
          sum_x 1[o_s(x-ell)=C]
                {1[o_s(x+1)=D]-1[o_s(x)=D]}.
```

At fixed `x`, the `C` sum selects `o_s(x-ell)` when it is nonnull.  The two
`D` sums select respectively `o_s(x+1)` and `o_s(x)`.  The null-owner
extension in `(1.2)` covers all remaining cases and gives `(2.1)--(2.2)`.
If the two endpoint owners agree, the two terms cancel.  QED.

This formula is strictly finer than a residual size/run-count profile.  It
asks which owner occurs at the three literal positions

```text
x-ell, x, x+1,
```

not merely how many components of each size have one or two ambient runs.

## 3. Phase-averaged endpoint-profile coefficients

For a fixed `s,ell,x`, let `sigma_s(ell,x)` record

```text
K(s); the full residual size multiset;
the null/non-null status and sizes of
  C=o_s(x-ell), A=o_s(x), B=o_s(x+1);
the equality pattern among C,A,B; and the literal lag ell.               (3.1)
```

This finite signature determines the exact charge

```text
w(sigma)=kappa(C,B)-kappa(C,A).                       (3.2)
```

For a probability law `nu` on cyclic product orbits, define its literal
phase-averaged endpoint profile, separated by intermediate kind, as

```text
Gamma_(nu,K,ell)(sigma)
 =E_(s~nu)[1[K(s)=K] (1/n) sum_(x mod n)
                         1[sigma_s(ell,x)=sigma]].    (3.3)
```

The all-`n` average in `(3.3)` is well-defined on quotient orbits: a short
orbit is repeated by exactly its stabilizer, just as in M91's all-phase
posterior formula.  No orbit-size correction is missing.  Its total mass is
`nu(K)`, and the two kind profiles together have mass one.

### Proposition 2 (proved: exact coefficient normalization)

For every probability law `nu`,

```text
nu(E_ell)=n sum_(K in {T,D}) sum_sigma
                    w(sigma) Gamma_(nu,K,ell)(sigma). (3.4)
```

#### Proof

Insert `(2.1)` into `(2.2)`, group equal signatures, and divide/multiply by
the `n` phases in `(3.3)`.  Kind `T` and kind `D` partition the supported
products.  QED.

The exact normalized M91 conditional laws enter `(3.3)` literally.  For
example, with M91's chord sets and first-edge laws,

```text
Gamma_(Phi_(1,u),K,ell)
 =p_u^-1 sum_(e in E_L(u))nu_L(e)
          sum_(f in T(M))nu_M(f)
             1[K(ef)=K] Gamma_(delta_[ef],K,ell),

Gamma_(Psi_(1,u),K,ell)
 =q_u^-1 (1/2)sum_(C in {C_-,C_+})
          sum_(e in E_C(u))nu_C(e)
          sum_(f in T(M))nu_M(f)
             1[K(ef)=K] Gamma_(delta_[ef],K,ell).     (3.5)
```

Channel two is the same substitution into M91 `(4.4b)` with the exact
ordered-factor completion probability `N_Q(e,f)`:

```text
Gamma_(Phi_(2,u),K,ell)
 =p_u^-1 sum_(e in E_L(u))sum_(f in T(eL))
           N_L(e,f) 1[K(ef)=K] Gamma_(delta_[ef],K,ell),

Gamma_(Psi_(2,u),K,ell)
 =q_u^-1 sum_(C in {C_-,C_+})sum_(e in E_C(u))
          sum_(f in T(e C_- C_+))
           N_(C_- C_+)(e,f) 1[K(ef)=K]
           Gamma_(delta_[ef],K,ell).                 (3.6)
```

As in M91, the fair exterior-component choice in the last line is already
in `N_(C_- C_+)`.  Equations `(3.5)--(3.6)` sum raw ordered factors before
quotienting, so three triangle lifts, two double lifts, both cyclic seams,
and all collisions remain literal.

## 4. The exact signed endpoint transport tensor

For `j=1,2`, define the adjacent-split and embedding profile differences

```text
A_(j,u,K,ell)=Gamma_(Phi_(j,u),K,ell)
              -Gamma_(Phi_(j,u+1),K,ell),

B_(j,u,K,ell)=Gamma_(Phi_(j,u),K,ell)
              -Gamma_(Psi_(j,u),K,ell).              (4.1)
```

Define the complete signed endpoint transport tensor

```text
T_(K,ell)
 =sum_(j=1)^2 alpha_j {
    sum_(u=1)^(k-2) D_u A_(j,u,K,ell)
   +sum_(u<k/2)q_u B_(j,u,K,ell)}.                   (4.2)
```

All objects in `(4.1)` are signed measures on the signature space.  Both
M91 channels and both `T/D` kinds are combined in `(4.2)` before the scalar
absolute value below.

### Proposition 3 (proved: PBV coefficient law)

With `Xi_(j,ell)` as in accepted M261 `(3.7)`, one has exactly

```text
alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)
 =eta(E_ell)
 =n sum_(K in {T,D}) <w,T_(K,ell)>.                 (4.3)
```

Here `eta=P_B-P_A` is the full centered first-row law.  In particular, PBV
is equivalent to

```text
sum_(ell=2)^(n-3)
 |sum_K <w,T_(K,ell)>| =O(n^-2).                    (SET-full)
```

#### Proof

Apply the linear profile map `(3.3)` to M91's measure-valued Abel identity,
then combine the two channels with their exact source-independent masses
`alpha_j`.  This gives `(4.2)`.  Apply `(3.4)` and use M261's exact
`alpha_1 Xi_1+alpha_2 Xi_2=eta(E_ell)`.  The outside factor `n` in `(4.3)`
makes `(SET-full)` exactly equivalent to PBV, with no hidden normalization.
QED.

There is also an exact coupling reading of `(4.2)`.  Let `P_ell(s)` be the
probability measure on endpoint signatures obtained by choosing `x`
uniformly in `Z/nZ`.  For any couplings of each pair

```text
(Phi_(j,u),Phi_(j,u+1)),       (Phi_(j,u),Psi_(j,u)),
```

the corresponding profile difference is the expectation of
`P_ell(s)-P_ell(t)`.  Therefore `(4.2)` is a signed transport of literal
jump locations for every such choice of couplings.  A proof may sum these
signed transported endpoint coefficients before absolute values.  Taking
absolute values separately in `u`, in `j`, in `K`, or in endpoint signatures
would be a stronger statement and is not licensed here.

## 5. Pointwise reflection and the half-profile target

Let

```text
F_ell(s)=sum_(C,D)kappa_s(C,D)
                 sum_r 1[o_s(r)=C]1[o_s(r+ell)=D].   (5.1)
```

Symmetry of `kappa_s` and the change of variable `r -> r-ell` give

```text
F_ell(s)=F_(n-ell)(s).                               (5.2)
```

M261's derivative identity is `E_ell=F_(ell+1)-F_ell`.  Hence, pointwise
for every supported product,

```text
E_ell(s)=-E_(n-ell-1)(s).                            (5.3)
```

Since `n` is odd,

```text
E_((n-1)/2)(s)=0.                                    (5.4)
```

Thus `(SET-full)` is exactly equivalent to the first standalone half-profile
estimate

> **Signed endpoint transport `(SET)` (unresolved).**  There is an absolute
> constant `C` such that, for every odd `k>=3`,
>
> ```text
> sum_(ell=2)^((n-3)/2)
>  |sum_(K in {T,D}) <w,T_(K,ell)>| <=C/n^2.         (SET)
> ```

This is the first unproved step in the endpoint-profile representation.

## 6. A deterministic lag-variation envelope

The following bound is useful for coupling errors, although it does not
supply the signed factor `1/n` required by `(SET)`.

### Proposition 4 (proved: uniform statewise endpoint `l1`)

For every supported triangle or double `s`,

```text
sum_(ell=2)^(n-3)|E_ell(s)| <=1232/e^2.              (6.1)
```

#### Proof

If `A,B` are circular binary sets, each a union of at most two intervals,
and

```text
C_AB(ell)=sum_r 1_A(r)1_B(r+ell),
```

then discrete differentiation in `B`, and symmetrically in `A`, gives

```text
sum_(ell mod n)|C_AB(ell+1)-C_AB(ell)|
 <=4 min(|A|,|B|).                                   (6.2)
```

Indeed a two-interval binary word has at most four jumps; sum first over the
other set and then over all lags.  Each generic-owner set in this problem is
one or two circular intervals, so `(6.2)` applies to every `C_ij`, with
`|A|=g_i<=d_i` and `|B|=g_j<=d_j`.

Put `rho_ij=e^2 kappa_ij-1` as in M261.  Elementary logarithmic bounds give,
for all component sizes (including invalid shifts),

```text
|rho_ii|<=20/d_i,
|rho_ij|<=20(1/d_i+1/d_j),             i!=j.         (6.3)
```

For completeness, if `a_d=tau(d-1)/tau(d)` and `d>=2`, then

```text
1/(d-1) <= 1+(d-2)log(1-1/d) <=2/d,
```

so `|e a_d-1|<=4/d`; multiplying two such factors proves the cross-owner
bound with room to spare.  For `d>=4`,

```text
0 <=2+log(1-1/d)+(d-3)log(1-2/d) <=5/d,
```

and the cases `d<=3` are immediate, proving the same-owner bound.

Now `(6.2)--(6.3)` imply

```text
sum_ell |Delta Q_ell|
 <=3(4d_i)(20/d_i)
   +sum_(i!=j)4 min(d_i,d_j)20(1/d_i+1/d_j)
 <=240+960=1200.                                    (6.4)
```

Here the first displayed term abbreviates the sum over the three diagonal
owners.  Finally `I_ell` is the circular difference histogram of the support
heads, whose cardinality is at most four.  Hence

```text
sum_ell |Delta I_ell|<=2 sum_ell I_ell
                       =2|supp(s)|^2<=32.            (6.5)
```

M261's exact affine derivative `e^2E_ell=Delta I_ell+Delta Q_ell`, followed
by restriction from all circular lags to `2,...,n-3`, proves `(6.1)`.  QED.

The bound `(6.1)` shows that a local endpoint coupling never incurs a hidden
factor `n`.  It still does not close PBV: applying it after total variation
or after separate absolute values in the Abel coefficients loses the signed
transport cancellation and does not yield `O(1/n)`.

## 7. Firewall and possible sign-regularity route

M264's accepted witness remains decisive.  At `k=3`,

```text
s_1=(0,2)(6,7),       s_2=(1,8)(6,7)
```

have the same complete residual size/run profile
`((1,1),(2,1),(6,2))` but distinct `E_2` values.  Their signatures in
`(3.1)` differ at literal jump locations.  Consequently no replacement of
`T_(K,ell)` by the accepted `X_D,Y_D` cutoff profiles is valid.

Reflection permits, but does not prove, a variation-diminishing alternative.
If the combined half-lag increments `eta(E_ell)` had at most an absolute
number of sign changes and the corresponding response sequence
`eta(R_ell)` had oscillation `O(n^-3)`, then its total variation would be
`O(n^-3)` and `(n-3)(n-4)` times that variation would prove PBV.  Both the
sign-regularity and range statements are unresolved.  No generic total
positivity/PF shortcut is invoked.

A particularly sharp version exposed by the literal locations is

> **One-threshold sign regularity `(SR)` (unresolved).**  On the first half
> of the lag range,
>
> ```text
> eta(E_ell)<=0,       2<=ell<=k-2,
> eta(E_ell)>=0,       k-1<=ell<=(n-3)/2.            (SR)
> ```

This is vacuous in its first range at `k=3`.  Put `G_ell=eta(R_ell)` and
`m=(n-3)/2`.  Since

```text
eta(E_ell)=(n-3)(n-4)[G_(ell+1)-G_ell],              (7.1)
```

`(SR)` and reflection would give the exact telescoping identity

```text
sum_(ell=2)^(n-3)|eta(E_ell)|
 =2(n-3)(n-4)
   [G_2+G_((n-1)/2)-2G_(k-1)].                       (7.2)
```

The bracket is nonnegative under `(SR)`.  Thus, conditional on `(SR)`, PBV
is equivalent to the three-point range estimate

```text
G_2+G_((n-1)/2)-2G_(k-1)=O(n^-3).                   (TPR)
```

Equivalently, since `z_k(y)=Lambda_n G_(y+1)` and `Lambda_n=Theta(n)`,

```text
z_k(1)+z_k((n-3)/2)-2z_k(k-2)=O(n^-2).              (TPR-z)
```

Both `(SR)` and `(TPR)` are unresolved.  They are stated separately because
bounded sign changes alone does not provide the required range, and a range
bound alone does not control total variation.

## 8. Scope stop

No `(SET)`, PBV, FD-bound, minority-sign theorem, FCL1, gap, mixing, or
Terminal claim is proved here.  The exact advance is the literal finite
endpoint-profile coefficient law, its signed coupling interpretation, the
pointwise reflection reduction to half the lags, and the uniform statewise
lag-variation envelope `(6.1)`.
