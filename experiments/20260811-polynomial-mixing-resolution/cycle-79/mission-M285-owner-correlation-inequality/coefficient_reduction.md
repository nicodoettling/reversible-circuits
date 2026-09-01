# M285 exact phase/composition coefficient reduction

Date: 2026-08-14 UTC.

Status: Propositions 1--3 below are exact.  The final signed coefficient
inequalities `(GOCI_j)` are unresolved.

## 1. Accepted setting and literal channel coefficients

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`,
`n=3k`, and `2<=ell<=n-2`.  Put

```text
h=(0,1,...,n-1),
L=(1,...,k-1,2k,...,3k-1),
M=(k,...,2k-1),
F=C_-C_+,
C_-=(0,...,k-1),              C_+=(2k,...,3k-1).
```

For a cycle `C` and a chord `e`, let `u_C(e)` be either cut size and

```text
nu_C(e)=tau(u_C(e))tau(|C|-u_C(e))
        /[(|C|-1)tau(|C|)].
```

For a supported rank-two product `s`, let `a(s)=3` for a triangle and
`a(s)=2` for a double.  Set `r=2k-2`, and interpret every incompatible
completion count as zero.  The signed product coefficients of the two
normalized channels are exactly

```text
beta_1(s)
 =sum_(e in T(L), f in T(M): ef=s) nu_L(e)nu_M(f)
  -1/2 sum_(C in {C_-,C_+})
        sum_(e in T(C), f in T(M): ef=s)nu_C(e)nu_M(f),       (1.1)

beta_2(s)
 =a(s)[
   F_(r-2)(s^-1 L)/F_r(L)
   -F_(r-2)(s^-1 F)/F_r(F)].                                (1.2)
```

Here the products in `(1.1)` have one designated exterior and one middle
factor; the two color orders commute and have already been conditioned out.
In `(1.2)`, summing the raw ordered lifts produces `a(s)`.  The full
two-cycle denominator

```text
F_r(F)=r!tau(k)^2
```

already includes the fair first-component choice, so there is no extra
`1/2`.  Likewise `F_r(L)=r!tau(2k-1)`.  Thus

```text
sum_s beta_j(s)=0,
eta_j(G)=sum_s beta_j(s)G(s),              j=1,2.             (1.3)
```

Equations `(1.1)--(1.3)` retain every raw triangle/double lift.

## 2. Positive cyclic compositions and the universal response

For a positive cyclic `q`-composition
`g=(g_1,...,g_q)` of `n`, an anchor `r`, and cumulative support
vertices

```text
v_0=r,   v_i=r+g_1+...+g_i  (mod n),
```

define the supported products

```text
s_T(r,g)=(v_0,v_1,v_2),                         q=3,
s_S(r,g)=(v_0,v_1)(v_2,v_3),                   q=4,
s_N(r,g)=(v_0,v_3)(v_1,v_2),                   q=4.            (2.1)
```

The forward triangle is the unique supported orientation.  Over all
anchors/compositions, every triangle occurs three times.  Summing both
double forms in `(2.1)`, every supported double occurs four times.
Here `r=v_0` is a support vertex, not the independent target-boundary
phase summed later inside `R_K`.

Let

```text
I_i(g)={g_1+...+g_(i-1),...,g_1+...+g_i-2} mod n,
```

an interval of length `g_i-1`; the following position is the null
support-head phase.  The generic-edge owner blocks are:

```text
T: I_1, I_2, I_3 have three different owners,

S: I_1 and I_3 are one-run owners;
   I_2 union I_4 is the two-run owner,

N: I_2 and I_4 are one-run owners;
   I_1 union I_3 is the two-run owner.                         (2.2)
```

Their residual component sizes are respectively

```text
T: (g_1,g_2,g_3),
S: (g_1,g_3,g_2+g_4),
N: (g_2,g_4,g_1+g_3).                                        (2.3)
```

For intervals or unions `U,V`, write the circular overlap

```text
Ov_n(U,V;ell)=|U intersect (V-ell)|.
```

With the exact rooted-tree owner matrix `kappa` from M280/M283, define

```text
R_K(g,ell)=sum_(owners a,b) kappa_ab
                         Ov_n(U_a,U_b;ell).                    (2.4)
```

This is an explicit finite convolution of interval indicators; no
permutation remains in `(2.4)`.

### Proposition 1 (exact phase/composition law)

For `j=1,2`,

```text
eta_j(F_ell)
 =1/3 sum_(r mod n) sum_(g_1+g_2+g_3=n)
       beta_j(s_T(r,g)) R_T(g,ell)

  +1/4 sum_(r mod n) sum_(g_1+...+g_4=n) [
       beta_j(s_S(r,g)) R_S(g,ell)
      +beta_j(s_N(r,g)) R_N(g,ell)].                         (2.5)
```

#### Proof

For `s=s_K(r,g)`, direct residual-cycle inspection gives
`(2.2)--(2.3)`; substituting the owner blocks in the accepted definition
of `F_ell` gives `(2.4)`.  Conversely, a fixed forward triangle has one
positive cyclic gap tuple for each of its three choices of support anchor.
A fixed supported double has one gap tuple for each of four support anchors;
at each anchor exactly one of the displayed `S/N` formulas equals that
double.  Thus the same actual coefficient `beta_j(s)` and the same
`F_ell(s)` occur exactly three or four times—not `n` times.  Dividing by
three/four therefore recovers one copy of every term in `(1.3)`.  QED.

For complete topology retention, split each overlap in `(2.4)` according
to the literal cyclic order of the two target boundary-edge pairs in the
residual owner cycle.  Equal-owner terms partition into
`R_(K,IS)+R_(K,IN)`; unequal-owner terms are `R_(K,X)`.  Therefore
`(2.5)` holds separately before summing the three topology labels.  The
outer `T` versus `S/N` rows retain the intermediate kind.

## 3. Rooted-owner autocorrelation decomposition

Put, with invalid shifts zero,

```text
a_d=tau(d-1)/tau(d),
b_d=tau(d-2)/tau(d),
delta_d=b_d-a_d^2.                                           (3.1)
```

For a supported state `s`, let `o_s(x)` be the residual owner of a
generic phase and null otherwise, and define the scalar owner field

```text
A_s(x)=a_(d_(o_s(x))) 1[o_s(x) is nonnull].                   (3.2)
```

Since `kappa_ab=a_(d_a)a_(d_b)` off the diagonal and
`kappa_aa=b_(d_a)`, direct expansion gives

```text
F_ell(s)
 =sum_x A_s(x)A_s(x+ell)
  +sum_i delta_(d_i) C_ii^s(ell).                            (3.3)
```

### Proposition 2 (nonnegative admissible-lag decomposition)

For every supported `s` and every `2<=ell<=n-2`,

```text
F_ell(s)
 =sum_x A_s(x)A_s(x+ell)
  +sum_(i:d_i>=3) delta_(d_i) C_ii^s(ell),                   (3.4)
```

and every summand in `(3.4)` is nonnegative.  Moreover
`0<=delta_d<=C/d^2` for an absolute constant and all `d>=3`.

#### Proof

The ratios

```text
tau(d)/tau(d-1)=(d/(d-1))^(d-2)
```

increase with `d`: for real `x>2`, the derivative of
`(x-2)log(x/(x-1))` is positive because
`log(1+1/(x-1))>1/x>(x-2)/[x(x-1)]`.  Thus `tau` is log-convex and
`tau(d-2)tau(d)>=tau(d-1)^2`, proving `delta_d>=0` for `d>=3`.
Uniform Taylor bounds for the two displayed rooted-tree ratios give
`delta_d=O(d^-2)` (equivalently,
`delta_d~3e^-2/(2d^2)`).

For `d=2`, `delta_2=-1`, but such a component has at most one generic
phase, so `C_ii(ell)=0` at every `ell != 0 (mod n)`.  The deletion changes
only the zero-lag diagonal.  In particular equality is exact, without an
endpoint exception, at every admissible `2<=ell<=n-2`.  A size-one
component has no generic phase.  Removing these zero terms from `(3.3)`
proves `(3.4)`.  QED.

Equation `(3.4)` is a repaired positive autocorrelation representation:
the apparent size-two failure of positive semidefiniteness is invisible at
the admissible target lags.

### Exact collision/decorated specialization

Let

```text
b_s(r)=1[r+1 in supp(s)],
I_ell(s)=sum_r b_s(r)b_s(r+ell),
rho_ab(s)=e^2 kappa_ab(s)-1,
Q_ell(s)=sum_(a,b)rho_ab(s)C_ab^s(ell).
```

Since `sum_a chi_a^s(r)=1-b_s(r)`, direct expansion gives the pointwise
identity

```text
e^2 F_ell(s)=n-8+2 1[kind(s)=T]+I_ell(s)+Q_ell(s).   (3.5)
```

Applying the centered channel coefficients in `(1.3)` and retaining the
triangle/double transfer yields

```text
e^2 eta_1(F_ell)=eta_1(I_ell)+eta_1(Q_ell),

e^2 eta_2(F_ell)=2 theta_k+eta_2(I_ell)+eta_2(Q_ell),

theta_k=6(k-1)/[k(2k-3)(2k-1)]>0.                   (3.6)
```

Thus collision and decorated owner-ratio terms remain together.  The
positive channel-two triangle transfer does not by itself sign their sum.

### Proposition 3 (Fourier form and exact obstruction)

If `hat{}` denotes the circular Fourier transform, the diagonal-repaired
state sequence

```text
Ftilde_s(ell)
 =sum_x A_s(x)A_s(x+ell)
  +sum_(i:d_i>=3)delta_(d_i)C_ii^s(ell)
```

has nonnegative spectrum

```text
hat Ftilde_s(q)
 =|hat A_s(q)|^2
  +sum_(i:d_i>=3)delta_(d_i)|hat chi_i^s(q)|^2 >=0.           (3.7)
```

It equals `F_ell(s)` throughout the OCI lag range.  However, applying the
centered coefficient `beta_j` gives a signed difference of such spectra,
not a positive mixture.  Whenever `beta_j` is nonzero, its zero total mass
forces both signs.  The frozen exact conditioned-Borel MON/FOSD failures
show that the first-order Borel monotone/TP2 route cannot be asserted
blockwise:

```text
D_u[Phi_(j,u)(F_ell)-Phi_(j,u+1)(F_ell)]
 +q_u[Phi_(j,u)(F_ell)-Psi_(j,u)(F_ell)]
```

cannot be signed blockwise.  Thus neither statewise PSD nor conditioned
Borel stochastic order proves OCI.  QED.

## 4. Narrowest unresolved coefficient inequality

Substitute `(3.4)` into `(2.5)`.  The exact all-rank target is:

> **Gapped owner-correlation inequality `(GOCI_j)` (unresolved).**
> For `j=1,2`, every odd `k>=3`, and `2<=ell<=3k-2`, the explicit
> signed positive-composition coefficient in `(2.5)`, with response
> `(3.4)`, is nonnegative.

All state responses in this inequality are nonnegative interval
autocorrelations; all sign is isolated in the explicit Cayley/Borel
coefficients `beta_j`.  This is narrower than an arbitrary function
comparison between `H_(j,B)` and `H_(j,A)`, but it remains a signed
coefficient theorem.

If `(GOCI_j)` fails or cannot be proved, the weaker correct target is not
termwise Abel control.  It is the cross-channel aggregate

```text
k sum_y[-alpha_1 CP_1(k,y)-alpha_2 CP_2(k,y)]_+=O(1),        (4.1)
```

or, using the accepted common prefactor exactly,

```text
(k Lambda_n/R_n) sum_(ell=2)^(n-2)
 [-alpha_1 eta_1(F_ell)-alpha_2 eta_2(F_ell)]_+=O(1).         (4.2)
```

Since `k Lambda_n/R_n=Theta(1)`, `(4.2)` is equivalently a uniform `O(1)`
bound on the displayed unscaled sum.  This is the accepted minority-sign
target and permits cross-channel cancellation.  No FCL1 or downstream
inference is made here.
