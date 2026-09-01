# M313 exact common-flux reduction

Date: 2026-08-14 UTC.

Status: Propositions 1--3 are proved exact.  MPCF is unresolved.

## 1. Quantile endpoint coupling combines both Abel terms

Let `P_t=sum_(r<=t)p_r`, `Q_s=sum_(r<=s)q_r`, with `P_0=Q_0=0`, and define

```text
pi_(s,t)=length((Q_(s-1),Q_s] intersection (P_(t-1),P_t]).   (1.1)
```

M91 proves that `p` stochastically dominates `q`, so this common-uniform
quantile coupling has support only on `s<=t`.  Its marginals and cut
crossings are exactly

```text
sum_t pi_(s,t)=q_s,
sum_s pi_(s,t)=p_t,
sum_(s<=u<t)pi_(s,t)=-D_u.                            (1.2)
```

For any profile-measure sequences `F_t,G_s`, telescope each coupled endpoint
path:

```text
F_t-G_s=(F_s-G_s)+sum_(u=s)^(t-1)(F_(u+1)-F_u).
```

Multiplying by `pi_(s,t)` and using `(1.2)` gives

```text
sum_(s,t)pi_(s,t)(F_t-G_s)
 =sum_s q_s(F_s-G_s)
  +sum_u D_u(F_u-F_(u+1)).                            (1.3)
```

Thus the two M305 Abel sums are the divergence of one endpoint coupling;
they are not two objects to estimate.

## 2. Literal zero-slot extension

For each physical product state define an extended mark:

- H or A at size `d`: three labeled owner slots;
- C at sizes `(d,e)`: six labeled ordered distinct-owner slots.

A slot has its literal derivative profile when its size condition holds and
profile `0` otherwise.  A genuinely zero response also stays at `0`.  Write
the resulting mark kernels as `Mtilde^X`.  Their total masses are fixed:

```text
r_H=r_A=3,       r_C=6.                              (2.1)
```

Define, before any coupling or norm,

```text
Ftilde_s=alpha_1 Mtilde_*Phi_(1,s)+alpha_2 Mtilde_*Phi_(2,s),
Gtilde_s=alpha_1 Mtilde_*Psi_(1,s)+alpha_2 Mtilde_*Psi_(2,s).
```

Both have the same mass `c_X=r_X(alpha_1+alpha_2)` for every split.  The
nonzero-profile restriction of their endpoint difference is exactly the
M305 response-relevant measure `mu^X`.  This makes the zero-profile
clarification in M310 literal rather than informal.

## 3. Canonical common-part endpoint coupling

Normalize `g_s=Gtilde_s/c_X` and `f_t=Ftilde_t/c_X`.  For each supported
quantile pair `(s,t)`, put

```text
c_(s,t)(P)=min(g_s(P),f_t(P)),
lambda_(s,t)=sum_P c_(s,t)(P),
a_(s,t)=g_s-c_(s,t),
b_(s,t)=f_t-c_(s,t).                                 (3.1)
```

The residual masses both equal `rho_(s,t)=1-lambda_(s,t)`.  Define the
canonical coupling

```text
kappa_(s,t)(P,Q)
 =1[P=Q]c_(s,t)(P)
  +1[rho>0] a_(s,t)(P)b_(s,t)(Q)/rho_(s,t).          (3.2)
```

It has first marginal `g_s` and second marginal `f_t`.  Each profile atom
can be lifted proportionally to its complete literal raw-state,
positive-representation, and owner-slot fiber.  Since `Ftilde,Gtilde` were
formed after the `alpha_1/alpha_2` sum, this is one coupling of both live
channels, not two channelwise bounds.  Raw ordered lifts are already in
`Phi/Psi`; state-level marking is exactly the average of three triangle or
four combined-double representations, retaining `1/3`, `1/4`, all `T/S/N`
kinds, phases, seams, and incidences.

Form the single antisymmetric net edge flux

```text
J(P,Q)=c_X sum_(s,t)pi_(s,t)
       [kappa_(s,t)(P,Q)-kappa_(s,t)(Q,P)].           (3.3)
```

All summands in `(3.3)` are combined before any absolute value.

### Proposition 1 (proved: exact divergence)

With `div J(P)=sum_Q J(Q,P)`, one has

```text
div J=sum_t p_t Ftilde_t-sum_s q_s Gtilde_s.          (3.4)
```

**Proof.**  For a fixed `(s,t)`, summing `(3.3)` into `P` gives
`c_X[f_t(P)-g_s(P)]`.  Apply the two marginals of `pi`.  QED.

By `(1.3)`, `(3.4)` is also exactly the sum of both marked Abel terms.

### Proposition 2 (proved: response restriction)

Deleting the zero coordinate from `div J` gives M305's `mu^X` exactly.

**Proof.**  Slot mismatches and zero responses contribute the zero vector to
the row, while every nonzero matching slot occurs once.  Linearity and the
accepted state-level representation average finish the identification. QED.

### Proposition 3 (proved: MPCF suffices for CMPAD)

For an antisymmetric finite edge flux,

```text
||div J||_TV<=2 sum_(unordered {P,Q})|J(P,Q)|.        (3.5)
```

Restriction away from profile zero can only decrease the left side.  Hence
the three Borel-scaled MPCF edge bounds predeclared in `plan.md` imply the
three CMPAD bounds.

## 4. Exact unresolved point and strongest self-attack

The common-part coupling `(3.2)` is explicit and falsifiable, but its
pairwise residual masses need not be small.  MPCF asks for cancellation only
after all quantile pairs are added and reverse profile edges in `(3.3)` are
antisymmetrized.  No accepted theorem controls this circulation.  In
particular:

- `sum|D_u|=Theta(sqrt(k))` prevents a scalar path-length estimate;
- the tail crossing mass is `Theta(k^-1/2)`, too large for the target;
- bounding `rho_(s,t)`, either channel, or any kind separately would violate
  the mission and can lose the needed reverse-edge cancellation.

The first unproved statement is exactly MPCF for the one net edge table
`(3.3)`.  A sole exact `k=13` guard may now test this fixed flux, but cannot
prove an all-rank bound.

