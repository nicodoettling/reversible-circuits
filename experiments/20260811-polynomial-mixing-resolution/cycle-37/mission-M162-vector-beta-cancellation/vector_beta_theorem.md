# M162 actual-history vector beta/Jacobi cancellation

Date: 2026-08-13 UTC.

## 1. Scope and status

This note concerns only the normalized full unweighted reset excursion
`F=H/q` in the auxiliary nonlazy minimal-long-cycle parking projection.  The
project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
left-to-right.

The following are **proved**:

1. an explicit finite actual-history feature map whose Gram kernel is the
   accepted M157/M160 signed two-beta kernel;
2. an exact vector-valued shared-observation posterior recursion, including
   exact removal of the killed observation;
3. a finite shifted-Jacobi Parseval identity and the universal truncated
   off-diagonal bounds `T_r>=F`; and
4. an exact one-step recursion for the first centered Jacobi energy which
   preserves the constant/centered cross term.

The capped result `T_1<=1-q` for `B<=3,L<=6,kappa<=8,D=1` is **exact
finite**, not a universal theorem.  The all-suffix degree-one boundary,
every gap, and both project terminals remain unresolved.

## 2. Coordinates and the actual-history feature map

Write a state as

```text
xi=(s,kappa,D,B),  s=B+L,  mu_xi=Beta(D,kappa-D),
q_xi=w_(s+1-B)w_B/w_(s+1).
```

For a root group of degree `d` and last part `t`, let

```text
m_s(d,t)=w_t c(s-t,d-1)/[d! w_(s+1)].              (2.1)
```

These masses sum to one.  A group is deep and live only when `t>B` and
`t-1>=2`.  For `a=0,...,d`, define

```text
L_(d,a)(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=integral L_(d,a) dmu_xi,
mu_a=Beta(D+a,kappa-D+d-a),                        (2.2)
```

and, for retained `a<d`, the child

```text
xi_a=(t-1,kappa+d,D+a,B).
```

The value `a=d` is exactly attachment rank `j=0`; it is killed.  Put

```text
eta_(d,t)=m_s(d,t) q_(xi_a)/q_xi,                  (2.3)
```

where the child split does not depend on `a`.

Let `E_xi` be the active canonical reset endpoints, `J_E(u)` their accepted
point currents, and `c_E` their capacities.  Define the finite history
Hilbert space recursively by the orthogonal direct sum

```text
H_xi = R^(E_xi)
       direct-sum_(live (d,t), a<d) H_(xi_a)^(d,t,a).          (2.4)
```

Each superscript denotes a distinct copy.  The actual-history feature map is

```text
Phi_xi(u)
 = direct-sum_E J_E(u)/sqrt(q_xi c_E)
   direct-sum_(live (d,t),a<d)
     sqrt(eta_(d,t)/pi_a) L_(d,a)(u) Phi_(xi_a)(u).             (2.5)
```

Suffix excess strictly decreases in every child, so (2.4)--(2.5) are finite.
The feature degree is at most `L`: reset currents have degree at most `L`,
and on a branch the likelihood degree plus the child degree is at most `L`.

> **Theorem 2.1 (proved actual-history Gram representation).**
> For the exact M157 kernel,
> ```text
> K_xi(u,v)=<Phi_xi(u),Phi_xi(v)>_(H_xi),            (2.6)
> F(xi)=H(xi)/q_xi=||integral Phi_xi dmu_xi||^2.    (2.7)
> ```

**Proof.**  The reset coordinates in (2.5) give exactly
`sum_E J_E(u)J_E(v)/(q c_E)`.  Each descendant block gives

```text
eta_(d,t) L_a(u)L_a(v)K_(xi_a)(u,v)/pi_a,
```

which is precisely the shared-observation kernel recursion.  Bayes' rule is

```text
L_a(u)mu_xi(du)=pi_a mu_a(du).                     (2.8)
```

Thus the mean of a descendant feature block is
`sqrt(eta*pi_a) M_(xi_a)`, where
`M_y=integral Phi_y dmu_y`.  Squaring and summing orthogonal blocks gives the
exact reset plus `sum eta*pi_a F(xi_a)`, which is the normalized nilpotent
recurrence.  Induction on suffix excess proves (2.6)--(2.7).  QED.

Equation (2.8) has one `pi_a`, not `pi_a^2`, because the two beta copies
share the same observation.  The killed value `a=d` is absent from both
(2.4) and (2.5); no conditioning on survival is used.

## 3. Shifted-Jacobi decomposition and truncated bounds

For each state, let `P_(xi,n)` be the unique monic degree-`n` polynomial
orthogonal to lower degrees in `L2(mu_xi)`, and put

```text
h_(xi,n)=integral P_(xi,n)^2 dmu_xi,
A_(xi,n)=integral P_(xi,n)(u)Phi_xi(u)dmu_xi(u)/sqrt(h_(xi,n)). (3.1)
```

Here `P_(xi,0)=1`.  With the standard Jacobi convention whose weight on
`[-1,1]` is `(1-z)^alpha(1+z)^beta`, these are monic multiples of

```text
P_n^((kappa-D-1),(D-1))(2u-1).                     (3.2)
```

The order of the two parameters in (3.2) is important.  The checker avoids
convention risk by exact Gram--Schmidt from beta moments separately at every
`(kappa,D)`.

> **Theorem 3.1 (proved finite vector Parseval).**
> If `r<=L`, then
> ```text
> S_xi:=integral ||Phi_xi(u)||^2 dmu_xi(u)
>      =sum_(n=0)^L ||A_(xi,n)||^2,                 (3.3)
> F(xi)=||A_(xi,0)||^2,                             (3.4)
> T_r(xi):=S_xi-sum_(n=1)^r ||A_(xi,n)||^2
>         =F(xi)+sum_(n=r+1)^L ||A_(xi,n)||^2
>         >=F(xi).                                  (3.5)
> ```

**Proof.**  Expand each coordinate of the finite vector polynomial
`Phi_xi` in the orthogonal basis.  Sum scalar Parseval over the finite
history coordinates.  Since `P_0=1`, the constant coefficient is the mean
feature.  QED.

This is an actual-history inequality, not the generic canonical-basin frame
refuted by M123/M128.  It is also not pointwise polarization, diagonal
trace alone, positive part, or absolute value.  For `r=L`, (3.5) is the
tautological exact equality `T_L=F`; no claim is made from that endpoint.
For a fixed small `r`, (3.5) is a genuine upper bound which retains the
first `r` signed off-diagonal beta modes.

## 4. Exact first-mode recursion

Put

```text
p_xi=D/kappa,
sigma_xi^2=D(kappa-D)/[kappa^2(kappa+1)],
C_xi=integral (u-p_xi)Phi_xi(u)dmu_xi(u).           (4.1)
```

Then `P_(xi,1)=u-p_xi` and

```text
||A_(xi,1)||^2=||C_xi||^2/sigma_xi^2,
T_1=S_xi-||C_xi||^2/sigma_xi^2.                   (4.2)
```

For a retained observation `a`, set

```text
p_a^post=(D+a)/(kappa+d),
delta_a=p_a^post-p_xi,
M_a=integral Phi_(xi_a)dmu_a,
C_a=integral (u-p_a^post)Phi_(xi_a)dmu_a.          (4.3)
```

Bayes' rule gives the vector identity

```text
integral (u-p_xi)L_a(u)Phi_(xi_a)(u)dmu_xi(u)
 =pi_a[delta_a M_a+C_a].                           (4.4)
```

Because the feature blocks are orthogonal, (4.4) proves the exact recursion

```text
||A_(xi,1)||^2
 =E1_reset(xi)
  +sum_(live (d,t),a<d)
    eta_(d,t)pi_a/sigma_xi^2
      ||delta_a M_a+C_a||^2,                       (4.5)

E1_reset(xi)
 =sum_E {integral (u-p_xi)J_E(u)dmu_xi(u)}^2
        /(q_xi c_E sigma_xi^2).                    (4.6)
```

In particular (4.5) retains the signed cross term
`2 delta_a <M_a,C_a>`.  Dropping or taking the absolute value of that term
would be a different, looser argument.  Again, `a=d` is absent exactly.

For completeness, diagonal feature energy obeys

```text
S_xi=S_reset(xi)
 +sum_(live (d,t),a<d) eta_(d,t)
    integral L_a(u)||Phi_(xi_a)(u)||^2 dmu_a(u).   (4.7)
```

Equations (4.2), (4.5), and (4.7) are a universal exact one-step recursion
for `T_1`.  It is not yet a closed scalar induction: (4.7) contains a
likelihood-weighted child diagonal, and (4.5) contains the child
constant-centered cross term.  No universal inequality charging the
remaining modes `n>=2` to killed mass has been proved.

## 5. Exact capped result

The standalone checker exhausts

```text
B=1,2,3; L=0,...,6; kappa=2,...,8; D=1,...,kappa-1.
```

Across 588 states it verifies the feature/kernel value, shifted-Jacobi
Parseval, nonnegativity of every modal energy, all truncated upper bounds,
and the first-mode recursion (4.5), with zero failures.  The transfer audit
adds 12,096 monomial-pair identities and 168 retained/killed mass rows.

On the 147 right-heavy rows `D=1`, `T_1<=1-q` in every case.  The diagonal
trace `T_0` already passes 143.  The first Jacobi mode is necessary for the
other four:

| `(s,kappa,D,B)` | `T_0` | first-mode energy | `T_1` | `1-q` |
|---|---:|---:|---:|---:|
| `(8,2,1,2)` | 0.81369335 | 0.32053466 | 0.49315869 | 0.80322013 |
| `(7,2,1,3)` | 0.85528212 | 0.30754586 | 0.54773626 | 0.84979630 |
| `(8,2,1,3)` | 0.93988222 | 0.33818353 | 0.60169870 | 0.86343545 |
| `(9,2,1,3)` | 1.00558139 | 0.36121508 | 0.64436630 | 0.87293908 |

At the last and tightest nontrivial right-heavy row in the cap,

```text
T_1-(1-q)
=-5718955000293768669169116499127774106813103462903129
 /25020280686787951720856746375249920000000000000000000
 approximately -0.2285727755.                              (5.1)
```

This capped pass is exact finite evidence.  It cannot establish the
all-suffix statement.  The 94 exact local-budget failures elsewhere in the
full grid all have arbitrary deficit; local contraction is not the target
there, and M147/M151 already show why such children require amortization.

## 6. Remaining standalone lemma

The new theorem target is precise:

> **All-suffix degree-one Jacobi boundary (unresolved).**  For every
> `B>=1`, `L>=0`, and right-heavy attachment state `D=1` (with arbitrary
> `kappa>=2`), prove
> ```text
> T_1(B,L,kappa,1)<=1-q_(B,L).                     (6.1)
> ```

Together with (3.5), (6.1) would prove the right-heavy all-suffix excursion
contraction.  A proof must control the high-Jacobi tail or close the mixed
terms in (4.5)--(4.7); finite `L<=6` checks do neither.  No fixed-`r`
statement beyond `r=1` has been tested at `L>=7`, and no such extrapolation
is made.
