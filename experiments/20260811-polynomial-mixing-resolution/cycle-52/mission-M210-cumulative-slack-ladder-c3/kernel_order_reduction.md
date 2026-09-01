# M210 full-child-kernel order reduction for cumulative C3 slack

Date: 2026-08-13 UTC.

## 1. Scope and verdict

This note concerns only fresh right-heavy parents in the normalized full
unweighted reset excursion `F=H/q` of the auxiliary nonlazy
minimal-long-cycle parking projection. The project target remains uniform
fixed-length identity transposition words, with `(pq)(x)=p(q(x))` and
displayed factors left-to-right.

The universal cumulative inequality

```text
S_1+S_2+S_3>=X_3
```

is neither proved nor refuted. The exact accounting shows it is *identically
the already open fresh first-Jacobi boundary* `T_1<=1-q`; the three accepted
sector inequalities do not weaken that final obligation.

The proved output is a strict proof-architecture reduction:

1. the exact residual is a positive linear functional of each **full child
   Gram kernel**;
2. it is monotone under PSD kernel domination;
3. no exact recursion on child `T_1`, `C_3`, or `(M,C,||Z||^2)` closes the
   likelihood lifts, by the accepted exact `P_2/P_3` witness; and
4. even the tempting constant rank-one PSD majorant is impossible for a
   nonconstant child kernel.

Thus a new theorem must provide a nonconstant full-kernel majorant or an
equivalent family of all observation-weighted residual moments. No all-`L`,
total-AMV, gap, mixing, or Terminal conclusion follows.

## 2. Exact cumulative identity

For a fresh parent `xi=(B+L,2,1,B)`, let

```text
T_1=T_reset+sum_(h=1)^L T_h,
Delta=1-q-U_1-U_2-U_3,
S_h=U_h-T_h,                         h=1,2,3,
X_3=T_reset+sum_(h=4)^L T_h-Delta,
C_3=S_1+S_2+S_3.
```

The sector sum is exact because reset and every history branch occupy
orthogonal Hilbert copies. Direct substitution gives

```text
C_3-X_3=(1-q)-T_1.                              (2.1)
```

Equation (2.1) is not an inequality or a new amortization identity. It proves
that universal `C_3>=X_3` is logically equivalent to the M162/M165 fresh
all-suffix degree-one Jacobi boundary. Consequently the slack-ladder language
alone does not reduce the theorem target.

## 3. Full-kernel recursion

For any state `zeta`, let `mu_zeta=Beta(D,kappa-D)`, with mean `p_zeta` and
variance `sigma_zeta^2`. On symmetric bivariate polynomial kernels define

```text
Q_zeta[K]
 =integral K(u,u) mu_zeta(du)
  -(1/sigma_zeta^2)
    integral integral (u-p_zeta)(v-p_zeta)K(u,v)
      mu_zeta(du)mu_zeta(dv).                    (3.1)
```

If `K(u,v)=<Phi(u),Phi(v)>`, then

```text
Q_zeta[K]
 =E||Phi(U)||^2
  -||E[(U-p_zeta)Phi(U)]||^2/sigma_zeta^2>=0     (3.2)
```

by Hilbert-valued Bessel/Cauchy--Schwarz. Thus `Q_zeta` is a positive linear
functional on the cone of PSD Gram kernels.

For a live root group `(d,t)` and retained observation `a<d`, put

```text
L_(d,a)(u)=binom(d,a)u^a(1-u)^(d-a),
pi_a=integral L_(d,a)dmu_zeta,

Lift_(zeta,d,a)[K](u,v)
 =L_(d,a)(u)L_(d,a)(v)K(u,v)/pi_a.               (3.3)
```

The killed value `a=d` is absent. Multiplication of a Gram feature by
`L_(d,a)/sqrt(pi_a)` proves that `Lift` maps PSD kernels to PSD kernels.

Let `R_zeta` be the exact reset Gram kernel

```text
R_zeta(u,v)=sum_E J_E(u)J_E(v)/(q_zeta c_E).      (3.4)
```

M157/M160 and M162/M165 give the exact finite recursion

```text
K_zeta
 =R_zeta
  +sum_(live (d,t))sum_(a=0)^(d-1)
     eta_(d,t) Lift_(zeta,d,a)[K_(zeta_a)].       (3.5)
```

Applying (3.1) and using `T_1(zeta)=Q_zeta[K_zeta]` yields the exact residual
recursion

```text
D_zeta:=1-q_zeta-T_1(zeta)
 =1-q_zeta-Q_zeta[R_zeta]
  -sum_(live (d,t))sum_(a<d) eta_(d,t)
      Q_zeta[Lift_(zeta,d,a)[K_(zeta_a)]].        (3.6)
```

At a fresh parent, `D_zeta=C_3-X_3` by (2.1). Equation (3.6) retains every
likelihood-weighted vector cross term and parent covariance subtraction.

## 4. Exact monotonicity

Write `K<=_PSD H` when `H-K` is a PSD kernel. Because `Lift` preserves PSD
and `Q_zeta` is positive on PSD kernels,

```text
K<=_PSD H
 =>Q_zeta[Lift_(zeta,d,a)[K]]
   <=Q_zeta[Lift_(zeta,d,a)[H]].                  (4.1)
```

This is the exact monotone form requested by M210. It is monotone in the
**full child kernel**, not in a scalar child deficit: increasing a child
kernel increases its parent charge and decreases `D_zeta`.

Consequently, a constructive sufficient certificate is:

> For every retained child construct an explicit PSD majorant
> `K_(zeta_a)<=_PSD Khat_(zeta_a)` such that
>
> ```text
> Q_zeta[R_zeta
>   +sum_(d,t,a<d)eta_(d,t)Lift[Khat_(zeta_a)]]
> <=1-q_zeta.                                     (4.2)
> ```

Then (4.1) proves `D_zeta>=0`, hence `C_3>=X_3` at the fresh parent.

## 5. Smallest direct kernel-order statement

Let `J(u,v)=1`, so `Q_zeta[J]=1`. Define the first-Jacobi functional preorder

```text
A <=_(zeta,1) H  iff  Q_zeta[H-A]>=0.             (5.1)
```

The smallest direct kernel-order inequality proving cumulative `C_3` is

```text
R_zeta+sum_(d,t,a<d)eta_(d,t)Lift[K_(zeta_a)]
 <=_(zeta,1) (1-q_zeta)J.                         (5.2)
```

But by (3.5), (5.1), and `Q_zeta[J]=1`, inequality (5.2) is **exactly**
`T_1(zeta)<=1-q_zeta`. It is a coordinate reformulation, not a narrower
lemma. Any genuine proof progress must replace the actual child kernels by
explicit checkable PSD majorants as in (4.2), or exploit another new
inequality with equivalent full likelihood-weighted information.

The stronger-looking PSD comparison

```text
K_zeta<=_PSD(1-q_zeta)J                           (5.3)
```

cannot hold for a nonconstant Gram feature. Indeed, for any two points
`u,v`, the coefficient vector `(1,-1)` has zero quadratic form against `J`,
whereas its form against `K_zeta=<Phi(u),Phi(v)>` is
`||Phi(u)-Phi(v)||^2`. PSD domination by a constant kernel would force that
quantity to vanish for every `u,v`, hence `Phi` would be constant. Thus (5.3)
is not the missing certificate.

## 6. Scalar-summary nonclosure

The accepted M173/M177 witness uses parent `Beta(1,1)`, degree `d=1`, retained
`a=0`, and child `Beta(1,2)`. The normalized child residuals built from

```text
P_2=u^2-(4/5)u+1/10,          ||P_2||^2=1/300,
P_3=u^3-(9/7)u^2+(3/7)u-1/35,||P_3||^2=1/4900
```

have identical

```text
(M,C,||Z||^2,T_1)=(0,0,1,1),
```

but exact unit-exterior lift charges

```text
Q_parent[Lift(K_P2)]=18/35,
Q_parent[Lift(K_P3)]=32/63.                       (6.1)
```

The parent first-mode subtraction is zero in both cases. Therefore those
listed scalar summaries do not determine the positive functional in (3.6)
and cannot close its exact monotone recursion. The same applies to naming
the fresh scalar `C_3`, since by (2.1) it contains only the final scalar
deficit. A summary-only proof would need a genuinely new uniform operator
envelope; it does not follow from the exact recursion.

The witness is unrestricted operator data, not asserted to be a complete
actual-history child. Its valid logical use is nonclosure of the proposed
summaries, not a counterexample to fresh contraction.

## 7. Surviving standalone lemma

> **Full-child-Gram majorant lemma (unresolved).** Construct recursively,
> for every reachable retained child, an explicit nonconstant PSD kernel
> `Khat_zeta` with `K_zeta<=_PSD Khat_zeta`, preserving `(kappa,D)` and all
> killed observations, such that the fresh-parent budget (4.2) holds after
> exact Cayley/root aggregation.

Equivalently one may retain all observation-weighted residual-polynomial
moments queried by (3.6). A fixed scalar state from Section 6 is insufficient.
This is the first precise monotone proof obligation, but it is not yet a
strict logical reduction of the universal boundary: choosing `Khat=K` makes
(4.2) the original target.

## 8. Diagnostics and reproducibility

Run

```text
python3 -B kernel_order_exact.py --output kernel_order_results.json
```

The standard-library `Fraction` checker imports no predecessor and verifies
the accounting signs, both exact nonclosure charges, vanishing first-mode
subtractions, and the constant-kernel Loewner obstruction. It does not scan
fresh parents.

After (3.6) was derived, exploratory exact fresh rows inside the authorized
cap produced no counterexample before the coordinator stopped diagnostics.
Those finite passes are not promoted, are not used in any proof, and do not
support an all-`L` inference.
