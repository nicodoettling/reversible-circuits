# M319 exact global profile-edge coefficient identity

Date: 2026-08-14 UTC
Status: proved exact

Fix one H/A/C row and retain M313's corrected
`c_X=r_X(alpha_1+alpha_2)`.  For a supported quantile endpoint `(s,t)`, put

```text
delta_(s,t)(R)=f_t(R)-g_s(R),
rho_(s,t)=sum_R [delta_(s,t)(R)]_+
          =sum_R [-delta_(s,t)(R)]_+.
```

The common diagonal part of `kappa` has no off-diagonal edge contribution.
For distinct profiles `P,Q`, the residual-product definition gives

```text
kappa_(s,t)(P,Q)-kappa_(s,t)(Q,P)
 =1[rho>0]/rho * (
    [-delta(P)]_+[delta(Q)]_+
    -[-delta(Q)]_+[delta(P)]_+).                    (1)
```

Thus, for a fixed canonical orientation `P<Q` of `e={P,Q}`,

```text
J_e=c_X sum_(s,t)pi_(s,t)
       [kappa_(s,t)(P,Q)-kappa_(s,t)(Q,P)].         (2)
```

Equations `(1)--(2)` are formed only after the two channels and complete
extended marks have been combined.  They do not bound a residual mass, cell,
channel, kind, or orientation.

## Literal token expansion

Proportionally lift every off-diagonal residual-product atom through its full
raw profile fibers.  Let `Omega_e^+` be all resulting weighted tokens directed
`P->Q`, and `Omega_e^-` those directed `Q->P`, including every quantile cell
and all literal representation/slot labels.  Their total masses are

```text
L_e^+=c_X sum_(s,t)pi_(s,t)kappa_(s,t)(P,Q),
L_e^-=c_X sum_(s,t)pi_(s,t)kappa_(s,t)(Q,P).         (3)
```

Consequently the strongest exact edge identity is

```text
J_e=L_e^+-L_e^-.                                    (4)
```

This identity retains zero-profile edges and the full corrected normalization.
It is an exact coefficient formula, not an MPCF bound.
