# M283 independent reconstruction of M280

Date: 2026-08-14 UTC.

Status: the identities below are independently derived exact identities.
The inequalities `(CP)`/`(OCI)` remain unresolved.

## 1. Scope and convention

Use `(pq)(x)=p(q(x))`, with displayed factors multiplied left-to-right.
Fix odd `k>=3`, put `n=3k`, and write

```text
h=(0,1,...,n-1),
A=(0,k,2k),                    B=(0,1)(k,2k),
E_r=(r,r+1),                   ell=y+1 in {2,...,n-2}.
```

The target is only the first separated fixed cell of the auxiliary uniform
minimal length-`n-1` factorization law of `h` under the nonlazy cyclic
rank-two quotient kernel.  It is not the global identity-word law and not
the lazy `{3,4,5}` heat-bath chain.

## 2. Completion-count derivation of the owner response

For a permutation `Q` of transposition rank `r` and cycle sizes `d_i`,

```text
F_r(Q)=r! product_i tau(d_i),
tau(d)=d^(d-2)/(d-1)! = d^(d-1)/d!,  tau(1)=1.
```

For a supported rank-two product `s`, let `q_s=s^-1h` have three cycles
`C_a` of sizes `d_a`.  A boundary edge `E_r` can lower the rank exactly
when its head is fixed by `s`; in that case it is the directed residual
edge `q_s(r)=r+1`.  Define

```text
chi_a^s(r)=1[s(r+1)=r+1 and r in C_a].
```

Two target boundary edges are disjoint throughout the displayed lag range.
If their owners agree, cutting the two directed edges replaces
`d_a` by `(1,1,d_a-2)`.  If their owners differ, it replaces
`(d_a,d_b)` by `(1,d_a-1,1,d_b-1)`.  Consequently the two completion-count
ratios are exactly

```text
1/[(n-3)(n-4)] * tau(d_a-2)/tau(d_a),

1/[(n-3)(n-4)]
  * tau(d_a-1)tau(d_b-1)/[tau(d_a)tau(d_b)].
```

With invalid shifts zero, put

```text
kappa_aa=tau(d_a-2)/tau(d_a),
kappa_ab=tau(d_a-1)tau(d_b-1)/[tau(d_a)tau(d_b)]  (a!=b),
C_ab^s(ell)=sum_(r mod n)chi_a^s(r)chi_b^s(r+ell),
F_ell(s)=sum_(a,b)kappa_ab(s)C_ab^s(ell),
R_n=(n-3)(n-4).
```

Thus, directly from the completion counts,

```text
W_(k,y)(s)/A_s=F_ell(s)/R_n.                         (2.1)
```

No asymptotic approximation occurs in `(2.1)`.

## 3. Target lift, cell mass, and `Lambda_n`

The target is a double and has raw lift two.  Its cyclic phase orbit is free
and has mass

```text
pi_y=2nF_T/n^(n-2),
F_T=F_(n-3)(E_0E_2 h).
```

The response used by M274/M277 is therefore

```text
g_ell(s)=2W_(k,y)(s)/(A_s pi_y)
        =Lambda_n F_ell(s)/R_n,                      (3.1)

Lambda_n=n^(n-2)/(nF_T).
```

Because the target residual sizes are `(1,1,n-2)`,
`F_T=(n-2)^(n-4)`, and hence

```text
Lambda_n=(n-2)(n/(n-2))^(n-3)
        =(n-2)(1-2/n)^(-(n-3)).                      (3.2)
```

The target lift two cancels only its identical factor in `pi_y`; it does
not cancel any source intermediate lift.

## 4. Normalized channels and direct raw formulas

Let `H_(j,g)` be the normalized M91 law of the first pair product given
`j` exterior colors, and put

```text
eta_j=H_(j,B)-H_(j,A),              j=1,2.
```

The common `j=0` measures agree.  The live source masses are

```text
alpha_1=4(k-1)^2/[(3k-3)(3k-4)],
alpha_2=2(k-1)(2k-3)/[(3k-3)(3k-4)].
```

Equations `(2.1)--(3.2)` give exactly

```text
CP_j(k,y)=eta_j(g_ell)
         =Lambda_n/R_n * eta_j(F_ell).               (4.1)
```

This independently confirms every scalar in M280's principal identity.

For the direct raw form, put

```text
L=(1,...,k-1,2k,...,3k-1),
M=(k,...,2k-1),
F=C_-C_+,
C_-=(0,...,k-1),             C_+=(2k,...,3k-1).
```

The first channel is one exterior factor and one independent middle factor;
the two color orders commute.  Thus

```text
CP_1=
 sum_(e in T(L))nu_L(e)sum_(f in T(M))nu_M(f)g_ell(ef)
 -1/2 sum_(C in {C_-,C_+})sum_(e in T(C))nu_C(e)
       sum_(f in T(M))nu_M(f)g_ell(ef).              (4.2)
```

For a residual `Q`, let

```text
N_Q(e,f)=F_(r(Q)-2)((ef)^-1Q)/F_(r(Q))(Q).
```

Then the second channel is

```text
CP_2=
 sum_(e in T(L))sum_(f in T(eL))N_L(e,f)g_ell(ef)
 -sum_(C in {C_-,C_+})sum_(e in T(C))
       sum_(f in T(eF))N_F(e,f)g_ell(ef).            (4.3)
```

The first factor under `N_F` already chooses either equal-rank exterior
component with probability `1/2`; the outer sum simply partitions its
support.  An additional `1/2` in `(4.3)` would halve the normalized A-side
law and is therefore wrong.  Multiple raw `(e,f)` atoms with the same
product automatically retain the three triangle lifts and two double lifts.

## 5. Abel normalization

For the smaller split of the first exterior chord, let

```text
p_s=(2k-1)nu_(2k-1)(s),              1<=s<=k-1,
q_s=k nu_k(s),                       1<=s<k/2,
q_s=0 otherwise,
D_u=sum_(s<=u)(p_s-q_s).
```

Both `p` and `q` normalize, so `D_0=D_(k-1)=0`.  Conditioning the raw laws
in `(4.2)--(4.3)` gives normalized measures `Phi_(j,s),Psi_(j,s)` with

```text
H_(j,B)=sum_s p_s Phi_(j,s),
H_(j,A)=sum_s q_s Psi_(j,s).
```

Add and subtract `sum_s q_s Phi_(j,s)` and sum the scalar difference by
parts.  For every test function `G`,

```text
eta_j(G)
 =sum_(u=1)^(k-2)D_u[Phi_(j,u)(G)-Phi_(j,u+1)(G)]
  +sum_(u<k/2)q_u[Phi_(j,u)(G)-Psi_(j,u)(G)].        (5.1)
```

Taking `G=Lambda_n F_ell/R_n` proves M280's full Abel formula.  It is an
equality of signed measures: neither the gradient block nor the embedding
block has a separately asserted sign.

## 6. Kind/topology retention, endpoints, and reflection

The source laws retain product kind `T/D`.  For each state and phase, an
equal-owner term partitions into the two literal noncrossing `IS/IN`
classes; unequal owners give `X`.  Therefore

```text
F_ell=sum_(K in {T,D})sum_(c in {IS,IN,X})F_(ell,K,c)
```

statewise, before applying `eta_j`.  This is a partition, not a triangle
inequality.  The raw formulas retain the same partition through their
ordered lifts.

The exact lag range is `2<=ell<=n-2`; both disjoint-edge endpoints are
present.  Since `kappa_ab=kappa_ba`, changing variables in the circular
correlation gives

```text
C_ab^s(n-ell)=C_ba^s(ell),
F_(n-ell)(s)=F_ell(s).                               (6.1)
```

Thus reflection is statewise and consequently holds separately in each
channel:

```text
CP_j(k,y)=CP_j(k,n-2-y).
```

## 7. Collision/decorated form and `theta_k`

Let `b_s(r)=1[r+1 in supp(s)]`, and define

```text
I_ell(s)=sum_r b_s(r)b_s(r+ell),
rho_ab(s)=e^2 kappa_ab(s)-1,
Q_ell(s)=sum_(a,b)rho_ab(s)C_ab^s(ell).
```

Removing the owner labels gives the pointwise identity

```text
sum_(a,b)C_ab^s(ell)
 =sum_r(1-b_s(r))(1-b_s(r+ell))
 =n-8+2 1[kind(s)=T]+I_ell(s).
```

Since every conditional difference `eta_j` has total mass zero,

```text
e^2 eta_j(F_ell)
 =2eta_j(T)+eta_j(I_ell)+eta_j(Q_ell).               (7.1)
```

Channel one always uses disjoint exterior and middle factors, so
`eta_1(T)=0`.  In channel two, the merged cycle has triangle probability
`3/(2k-1)`.  On the split side the first two colors agree with probability
`(k-2)/(2k-3)` and then form a triangle with probability `3/k`.  Therefore

```text
eta_2(T)
 =3/(2k-1)-3(k-2)/[k(2k-3)]
 =6(k-1)/[k(2k-3)(2k-1)]
 =theta_k>0.                                         (7.2)
```

Because the prefactor in `(4.1)` is positive, per-channel positivity is
equivalent to the unresolved inequalities

```text
(OCI_1) eta_1(I_ell)+eta_1(Q_ell)>=0,
(OCI_2) 2theta_k+eta_2(I_ell)+eta_2(Q_ell)>=0.       (7.3)
```

The collision and decorated terms in `(7.3)` cannot be signed separately.
In particular, the positive `theta_k` is not a proof of `(OCI_2)`.

## 8. Exact implication hierarchy

The full channel-combined score is

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y),
```

with both masses positive.  Hence pointwise `(CP_1,CP_2>=0)` implies
`OS+: z_k(y)>=0`.  If

```text
P_k=sum_y(z_k(y))_+,       N_k=sum_y(-z_k(y))_+,
```

then OS+ sets `N_k=0` and implies MS.  Finally,

```text
sum_y|kz_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).                  (8.1)
```

Accepted M266/M268 proves PCS,
`k|sum_y z_k(y)|=O(1)`, at precisely this auxiliary first-cell scope.
Thus MS implies FCL1 through `(8.1)`.  PCS is used only in this final
closure.  None of these implications proves CP, OS+, MS, or FCL1.

## 9. Compact clean-room falsification and frozen evidence audit

`cleanroom_cp_audit.py` imports no M280 code and newly enumerates only the
predeclared compact rank `k=3`.  It reconstructs raw ordered source pairs
from minimal-completion counts before reading M280's frozen JSON.  Exact
checks include:

- source and conditional channel normalization, with
  `(alpha_0,alpha_1,alpha_2)=(1/15,8/15,2/5)`;
- split laws `p=(16/25,9/25)`, `q=(1,0)`, and `D_1=-9/25`;
- all twelve channel-lag instances of the direct/Abel equality;
- reconstruction from every `T/D` by `IS/IN/X` piece;
- channel-two's normalized full-`F` law without an extra `1/2`;
- exact reflection and both endpoints;
- `eta_1(T)=0`, `eta_2(T)=theta_3=4/15`;
- the pointwise and centered collision-affine identities.

All twelve exact `k=3` channel values are positive.  This is a compact
falsifier survival only.

After the clean-room calculation, the script reads frozen M280 output only
for integrity/self-consistency.  Its JSON digest is exactly

```text
d08c8b0d9b2abe61e26752033d91438e0e9c912397c087734cc9b4fe10a10f93.
```

All 60 frozen channel-lag scores equal their six exact pieces, all are
positive, reflection/endpoints hold, both minima are tied at `y=9,22`, and
`eta_2(T)=theta_11=20/1463`.  The reconstructed value

```text
11 sum_y z_11(y) = 1.9771508086589047...
```

agrees with M280's report.  M283 did not enumerate `k=11`; these checks
validate only the integrity and internal exact arithmetic of frozen finite
evidence.

## 10. Exact stop

The owner-correlation identities, direct and Abel normalizations,
collision/decorated reformulation, and implication hierarchy are exact.
They do not establish either inequality in `(7.3)`.  CP/OCI, OS+, MS,
FCL1, every later cell, direct L1/H0, gap, mixing, and both Terminals remain
unresolved.
