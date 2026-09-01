# M340 frozen cross-cell residual-flow candidate

Date: 2026-08-14 UTC

Status: frozen analytically before any M340 computation.

## 1. Complete signed token law

Fix a row `X` and a supported cell `c=(s,t)`.  For profiles `P,Q`, put

```text
a_c(P)=[g_s(P)-f_t(P)]_+,
b_c(Q)=[f_t(Q)-g_s(Q)]_+,
rho_c=sum_P a_c(P)=sum_Q b_c(Q).
```

The exact weight of a positive residual token

```text
omega=(c; xi_A at P, eta_B at Q),       P -> Q,
```

is

```text
w(omega)=c_X pi_c a_c(P)b_c(Q)/rho_c
         *u^A_(s,P)(xi)u^B_(t,Q)(eta),                 (1.1)
c_X=r_X(alpha_1+alpha_2),
r_H=r_A=3, r_C=6.                                     (1.2)
```

Here each `u` is the already-combined raw-fiber probability.  Its literal
label retains source, channel, split, ordered prefix and product, positive
`T/S/N` representation, phase, seam and incidence data, marked owner slot,
every zero slot, response profile, and exact completion weight.  Equation
`(1.1)` is never split into separately normed constituents.

## 2. Frozen source-geometric exception

Use exactly the accepted M335/M336 exception, with no sign-dependent
enlargement:

```text
E_R(zeta_R)=Touch_Sigma(zeta_R) or BadPref_R(zeta_R),
Exc_pf^*(omega)=E_A(xi_A) or E_B(eta_B).              (2.1)
```

`Touch_Sigma` sees only marked-owner support, literal support heads, and the
fixed source seam.  `BadPref_R` says that the retained ordered prefix is not
two successive rank decreases for the opposite raw source.  Off `(2.1)`,
the product/prefix/representation/slot/profile-preserving source switch
`sigma` exists and is a literal raw-label involution.

For an off-exception token define its unique raw switched pair

```text
Phi(omega)
 =(c_sigma; sigma(eta_B)_A at Q,
             sigma(xi_A)_B at P),                    (2.2)
```

where `c_sigma=(s_sigma,t_sigma)` is uniquely recomputed from those two raw
atoms.  Formula `(2.2)` reverses the formal profile order, but it is a
residual token only if

```text
pi_(c_sigma)>0,
a_(c_sigma)(Q)>0,
b_(c_sigma)(P)>0.                                   (2.3)
```

## 3. XCRF transport graph

Fix an unordered literal profile edge `e={P,Q}` and a complete raw-switch
orbit label `lambda`.  The label includes every field in Section 1 modulo
the literal two-element action of `Phi`; in particular it is not a grouping
by final sign, channel, kind, cell mass, or atom order.

Let `U_(e,lambda)` be the off-exception positive tokens in that orbit
oriented `P->Q`, and let `V_(e,lambda)` be its supported off-exception
residual tokens oriented `Q->P`.  Freeze the allowed relation

```text
u R_(e,lambda) v
 iff v=Phi(u), c(v)!=c(u), and v satisfies (2.3).     (3.1)
```

The inequality of cells enforces the requested cross-cell route and excludes
the already-refuted same-cell endpoint swap.  Because every complete raw
label is retained and `sigma` is deterministic, every node in `(3.1)` has
degree at most one.  Allowing an arc to another orbit would change a retained
prefix, product, representation, slot, phase, seam/incidence datum, or raw
completion label.  That would be a different surgery, not the existing raw
source switch plus transport.

The frozen **XCRF assertion** is the existence of nonnegative rational
numbers `theta_(u,v)` on `(3.1)` such that

```text
sum_(v:uRv) theta_(u,v)=w(u)       for every u in U,
sum_(u:uRv) theta_(u,v)=w(v)       for every v in V. (3.2)
```

Thus XCRF transports the whole exact compatible signed measure, before any
norm, and pairs only canonical residual tokens of opposite orientation.

## 4. Exact Hall criterion

For `A subseteq U`, let `N(A)` be its neighbor set in `(3.1)` and write
`mu^+(A)=sum_(u in A)w(u)`, `mu^-(B)=sum_(v in B)w(v)`.  Since all weights
are rational, the finite transportation theorem gives the exact criterion

```text
mu^+(U)=mu^-(V),
mu^+(A)<=mu^-(N(A)) for every A subseteq U.          (4.1)
```

Equivalently one may include the symmetric demand inequalities.  In the
present degree-at-most-one graph, `(4.1)` reduces orbitwise to the three
literal clauses

```text
Phi(u) is a supported reverse residual token,
c(Phi(u))!=c(u),
w(u)=w(Phi(u)).                                     (4.2)
```

Rationally splitting a token does not weaken `(4.2)`: a singleton component
has nowhere else to send its remaining mass.

## 5. Cell marginals and divergence

For the fixed `(e,lambda)`, define exact cell masses

```text
M_c^+=sum_(u in U:c(u)=c)w(u),
M_c^-=sum_(v in V:c(v)=c)w(v),
F_(c,c')=sum_(u:c(u)=c, v:c(v)=c')theta_(u,v).       (5.1)
```

Any XCRF flow necessarily obeys

```text
sum_(c'!=c)F_(c,c')=M_c^+,
sum_(c'!=c)F_(c',c)=M_c^-,                          (5.2)

sum_(c in C)M_c^+
 <=sum_(c' in N_cell(C))M_c^-       for every C,    (5.3)

M_c^+-M_c^-=div F(c),
sum_c(M_c^+-M_c^-)=0.                               (5.4)
```

The last equality says that the compatible coefficient in this literal
edge/orbit class is zero.  It is a necessary marginal condition, not an
available estimate; assuming it would be circular.  The atom-refined Hall
conditions `(4.1)` are stronger than the coarse cell cuts `(5.3)` and are
the exact conditions for the frozen graph.

No computation is authorized unless these identities leave a fixed clause
undecided.  No final-sign mass match, same-cell swap, constituent bound, or
downstream inference is part of XCRF.
