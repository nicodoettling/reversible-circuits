# M316 independent analytic audit

Date: 2026-08-14 UTC

## Scope

The object is only the accepted M91/M297 auxiliary centered first-pair law,
for odd `k>=3`, `n=3k`.  The global identity bridge and local heat-bath chain
are not analyzed.

## Quantile coupling and the one endpoint identity

Let `P_u=sum_(t<=u)p_t`, `Q_u=sum_(s<=u)q_s`, and

```text
pi_(s,t)=Leb((Q_(s-1),Q_s] intersect (P_(t-1),P_t]).
```

Both half-open interval families partition `(0,1]`, proving row marginals
`q_s` and column marginals `p_t`, including coincident endpoints.  Accepted
stochastic dominance is `P_u<=Q_u`, so common-quantile support has `s<=t`.
On this support,

```text
sum_(s<=u<t) pi_(s,t)=Q_u-P_u=-D_u,
```

because `D_u=P_u-Q_u`.  Telescoping

```text
F_t-G_s=(F_s-G_s)+sum_(u=s)^(t-1)(F_(u+1)-F_u)
```

and applying the marginals/crossing mass proves exactly

```text
sum_(s,t)pi_(s,t)(F_t-G_s)
 =sum_s q_s(F_s-G_s)+sum_u D_u(F_u-F_(u+1)).
```

Thus both Abel sums form one endpoint divergence; neither is normed alone.

## Literal fixed-slot extension

Every residual product has three owners.  H/A mark each of the three owner
slots; C marks each of the `3*2=6` ordered distinct-owner slots.  A size
mismatch or genuinely zero response maps to profile zero instead of removing
the slot.  Hence a probability law pushed through the extended mark has mass
exactly `r_H=r_A=3` or `r_C=6` for every split.

After first combining both live channels,

```text
Ftilde_s=alpha_1 Mtilde_*Phi_(1,s)+alpha_2 Mtilde_*Phi_(2,s),
Gtilde_s=alpha_1 Mtilde_*Psi_(1,s)+alpha_2 Mtilde_*Psi_(2,s),
```

both masses are exactly
`c_X=r_X(alpha_1+alpha_2)`.  For `m=k-1`, the accepted channel weights give

```text
alpha_1+alpha_2=2(4m-1)/(3(3m-1))<1,
```

so `c_X<=6`.  Deleting profile zero only after forming the signed endpoint
difference recovers the response-relevant reduced M305 measure; it need not
preserve its measure norm, and M313 does not assume that it does.

## Common-part coupling after combination

Normalize `g=Gtilde/c_X`, `f=Ftilde/c_X`, put `c(P)=min(g(P),f(P))`, and
let `a=g-c`, `b=f-c`, each of mass `rho`.  Then

```text
kappa(P,Q)=1[P=Q]c(P)+1[rho>0]a(P)b(Q)/rho
```

has first marginal `g` and second marginal `f`; when `rho=0`, the diagonal
common part is already the full coupling.  This construction is applied to
the channel-combined, slot-marked laws.  Proportional lifting inside each
profile fiber preserves the accepted raw lifts, state-representation weights,
owner incidences, kinds, phases, and seams without taking a constituent norm.

## Global flux, divergence, and normalization

Using the controlling corrected definition

```text
J(P,Q)=c_X sum_(s,t)pi_(s,t)[kappa_(s,t)(P,Q)-kappa_(s,t)(Q,P)],
div J(P)=sum_Q J(Q,P),
```

antisymmetry is immediate.  For each cell, summing into `P` yields
`c_X(f_t(P)-g_s(P))`; applying both quantile marginals yields

```text
div J=sum_t p_t Ftilde_t-sum_s q_s Gtilde_s.
```

The endpoint identity identifies this with the zero-slot extension of both
marked Abel terms.  The factor `c_X` is essential here.

For the unordered-edge convention,

```text
||div J||_TV
 <=sum_(P,Q)|J(P,Q)|
 =2 sum_(unordered {P,Q})|J(P,Q)|.
```

Restricting away from profile zero cannot increase total variation.  Thus
the corrected MPCF edge bounds imply the three CMPAD bounds with only the
absolute factor two.  This implication is exact; MPCF itself remains open.

Verdict on all analytic claims: **proved at their frozen scope**.
