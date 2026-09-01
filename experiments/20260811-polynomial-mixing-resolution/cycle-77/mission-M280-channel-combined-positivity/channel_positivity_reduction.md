# Exact per-channel owner-correlation reduction

Date: 2026-08-14 UTC.

Status: formula identities and implication statements below are exact
consequences of the frozen accepted inputs.  The all-rank sign inequality
`(OCI)` is unresolved unless the final report states an exact counterexample.

## 1. Scope and convention

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Fix odd `k>=3`, put `n=3k`, and use only the first separated
fixed cell of the auxiliary uniform minimal length-`n-1` factorization law
of the long cycle under M73's nonlazy cyclic rank-two quotient kernel.  This
is not the global identity-word law or the lazy exact same-product
`{3,4,5}` heat-bath chain.

Put

```text
h=(0 1 ... n-1),
A=(0,k,2k),                     B=(0,1)(k,2k),
E_r=(r,r+1),                    ell=y+1,
2<=ell<=n-2.
```

## 2. Literal response and channel laws

For a supported rank-two product `s`, put `q_s=s^-1h` and denote its three
residual cycles by `C_a`, with sizes `d_a`.  Define

```text
chi_a^s(r)=1[s(r+1)=r+1 and r in C_a],

kappa_aa(s)=tau(d_a-2)/tau(d_a),
kappa_ab(s)=tau(d_a-1)tau(d_b-1)/[tau(d_a)tau(d_b)]  (a!=b),

C_ab^s(ell)=sum_(r mod n)chi_a^s(r)chi_b^s(r+ell),
F_ell(s)=sum_(a,b)kappa_ab(s)C_ab^s(ell).
```

Invalid shifted sizes are zero.  A same-owner phase `a=b` is classified
literally as `IS` or `IN` by the cyclic order of the four boundary-edge
endpoints in `C_a`; a distinct-owner phase is `X`.  Thus

```text
F_ell=sum_(K in {T,D})sum_(c in {IS,IN,X})F_(ell,K,c)
```

after inserting the product-kind indicator.  This is bookkeeping, not a
triangle inequality.

Let `H_(j,g)` be M91's normalized law of the next pair product conditional
on `j` exterior colors for `g=A,B`, and define

```text
eta_j=H_(j,B)-H_(j,A),                         j=1,2.
```

The common `j=0` law cancels.  M91's source-independent channel masses are

```text
alpha_1=4(k-1)^2/[(3k-3)(3k-4)],
alpha_2=2(k-1)(2k-3)/[(3k-3)(3k-4)].
```

## 3. Exact CP identity

M161/M166 and M261/M264 give

```text
R_ell(s)=W_(k,y)(s)/A_s=F_ell(s)/R_n,
R_n=(n-3)(n-4),

2W_(k,y)(s)/(A_s pi_y)=Lambda_n R_ell(s),
Lambda_n=n^(n-2)/(nF_T)
        =(n-2)(1-2/n)^(-(n-3)).
```

Therefore, with no omitted lift or phase factor,

```text
CP_j(k,y)=Lambda_n/R_n * eta_j(F_ell).              (3.1)
```

For complete normalization visibility, let `p_u,q_u,D_u` be M91's exact
conditioned-Borel laws and cumulative difference, with

```text
D_u=sum_(v<=u)(p_v-q_v),
D_0=D_(k-1)=0,
```

and put `G_ell=Lambda_n F_ell/R_n`.  Applying M91's equality of measures to
this literal response gives the equivalent full gradient/embedding formula

```text
CP_j(k,y)
 =sum_(u=1)^(k-2)D_u[
    Phi_(j,u)(G_ell)-Phi_(j,u+1)(G_ell)]
  +sum_(u<k/2)q_u[
    Phi_(j,u)(G_ell)-Psi_(j,u)(G_ell)].              (3.2)
```

No sign is assigned to either displayed block.  Their sum is exactly
`eta_j(G_ell)`.

The non-Abel raw formulas are equally explicit.  Let

```text
L=(1,...,k-1,2k,...,3k-1),
M=(k,...,2k-1),
F=C_-C_+,
C_-=(0,...,k-1),             C_+=(2k,...,3k-1).
```

With `nu_C` the exact first-factor law and `N_Q(e,f)` the exact ordered
first-two-factor probability,

```text
CP_1=
 sum_(e in T(L))nu_L(e)sum_(f in T(M))nu_M(f)G_ell(ef)
 -1/2 sum_(C in {C_-,C_+})sum_(e in T(C))nu_C(e)
       sum_(f in T(M))nu_M(f)G_ell(ef),             (3.3)

CP_2=
 sum_(e in T(L))sum_(f in T(eL))N_L(e,f)G_ell(ef)
 -sum_(C in {C_-,C_+})sum_(e in T(C))
       sum_(f in T(eF))N_F(e,f)G_ell(ef).           (3.4)
```

The fair first exterior-component choice in `(3.4)` is already inside
`N_F`; no additional `1/2` occurs.  Equations `(3.1)--(3.4)` retain the
same literal three triangle lifts, two double lifts, `IS/IN/X`, all cyclic
phases, both lag endpoints, and all Borel normalizations before asking for
one channel sign.

Since `kappa` is symmetric,

```text
F_ell(s)=F_(n-ell)(s),
CP_j(k,y)=CP_j(k,n-2-y).                            (3.5)
```

The exact repaired sign target is consequently

```text
(OCI) eta_j(F_ell)>=0
      for j=1,2, odd k>=3, and 2<=ell<=n-2.         (3.6)
```

There is a useful exact collision/decorated version.  Put

```text
I_ell(s)=sum_r 1[r+1 in supp(s)]1[r+ell+1 in supp(s)],
rho_ab(s)=e^2 kappa_ab(s)-1,
Q_ell(s)=sum_(a,b)rho_ab(s)C_ab^s(ell).
```

M261/M264's pointwise affine identity gives, after applying the centered
channel laws,

```text
e^2 eta_j(F_ell)
 =2 eta_j(T)+eta_j(I_ell)+eta_j(Q_ell).              (3.7)
```

Channel one always produces a double, so `eta_1(T)=0`.  In channel two,

```text
eta_2(T)
 =3/(2k-1)-3(k-2)/[k(2k-3)]
 =6(k-1)/[k(2k-3)(2k-1)] =:theta_k>0.               (3.8)
```

Thus the first standalone inequalities can be written without hiding the
kind transfer:

```text
(OCI_1) eta_1(I_ell)+eta_1(Q_ell)>=0,
(OCI_2) 2theta_k+eta_2(I_ell)+eta_2(Q_ell)>=0.       (3.9)
```

Collision and decorated owner-ratio terms must remain together.  The
positive `theta_k` does not sign their sum.

## 4. Logical consequence and exact stop

M274/M277 gives

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y).
```

Both masses are positive, so `(OCI)` implies OS+.  OS+ makes the negative
phase mass `N_k` zero and therefore implies MS.  Accepted M266/M268 PCS and
the exact identity

```text
sum_y|kz_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k)
```

then imply FCL1.  PCS is used only at this final closure step.

The first unproved statement in this route is `(OCI)` itself.  The exact
monotone split coupling rewrites its left side as an endpoint expectation,
but no pathwise response order survives the frozen MON/FOSD counterexamples.
Separate kind signing is also invalid: channel one has zero kind transfer,
and in channel two the positive triangle transfer is accompanied by an
unsigned collision/decorated remainder.  A valid weaker fallback is the
cross-channel aggregate negative-mass estimate

```text
k sum_y[-alpha_1 CP_1(k,y)-alpha_2 CP_2(k,y)]_+=O(1),
```

or symmetrically M274/M277's MS.  No claim beyond the first auxiliary cell
follows here.
