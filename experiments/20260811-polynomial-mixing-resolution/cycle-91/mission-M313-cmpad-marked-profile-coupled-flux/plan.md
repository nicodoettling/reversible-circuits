# M313 plan: marked-profile coupled flux

Date: 2026-08-14 UTC.

## Scope and target

Work only in the accepted M91/M297 auxiliary centered first-pair law, with
odd `k>=3`, `n=3k`, `h=(k-1)/2`, and `(pq)(x)=p(q(x))`.  The global project
target remains the uniform fixed-length identity-word law, but this mission
does not directly analyze that law or the lazy `{3,4,5}` heat-bath kernel.

The accepted starting identity is

```text
mu^X=sum_(u=1)^(k-2) D_u(F^X_u-F^X_(u+1))
     +sum_(s=1)^h q_s(F^X_s-G^X_s),                 (1)
```

for `X=H_d,A_d,C_(d,e)`, after both live channels and every source/type,
phase, seam, and owner incidence have been combined.

## Exact common coupling fixed before substantive work

Let

```text
P_t=sum_(r<=t)p_r,   Q_s=sum_(r<=s)q_r,
pi_(s,t)=Leb((Q_(s-1),Q_s] intersection (P_(t-1),P_t]).
```

The accepted stochastic order gives `pi_(s,t)=0` unless `s<=t`, with row
marginal `q_s`, column marginal `p_t`, and crossing mass
`sum_(s<=u<t)pi_(s,t)=-D_u`.  Thus `(1)` is exactly the endpoint divergence
of paths from `G_s` to `F_t`, combining both Abel sums before a norm.

Use fixed owner slots to handle zero profiles literally:

- `H_d,A_d`: three owner slots; a slot not of size `d`, or having zero
  response, receives profile `0`;
- `C_(d,e)`: six ordered distinct-owner slots; a mismatched or zero response
  receives profile `0`.

The extended marked laws consequently have equal fixed mass.  Combine the
two live channels with their exact `alpha_1,alpha_2` weights before coupling.
For each `(s,t)`, define the canonical common-part coupling of the normalized
extended laws: match `min(G_s(P),F_t(P))` on `(P,P)`, then couple the two
equal residual measures by their normalized product.  Lift each profile atom
to its complete literal raw state/representation/slot fiber proportionally;
this retains raw lifts, exact triangle `1/3`, combined-double `1/4`,
`T/S/N`, phases, seams, incidences, and zero slots.

Aggregate all oriented profile edges with coefficient `pi_(s,t)`, then
antisymmetrize only after the full sum:

```text
J^X(P,Q)=sum_(s,t)pi_(s,t)
          [kappa^X_(s,t)(P,Q)-kappa^X_(s,t)(Q,P)].    (2)
```

No Abel term, channel, source, type, phase, seam, or incidence is normed
separately.

> **Marked Profile Coupled Flux (MPCF), predeclared.**  There is an absolute
> `C` such that the one net flux `(2)` obeys
>
> ```text
> sum_(unordered {P,Q}, P!=Q)|J^H_d(P,Q)|
>     <=C d b_d/k,
> sum_(unordered {P,Q}, P!=Q)|J^A_d(P,Q)|
>     <=C d b_d/k,
> sum_(unordered {P,Q}, P!=Q)|J^C_(d,e)(P,Q)|
>     <=C max(d,e)b_db_e/k.                          (MPCF)
> ```

The divergence of `(2)` is the zero-slot extension of `mu^X`; deleting the
zero coordinate and using `||div J||_TV<=2||J||_edge` makes MPCF sufficient
for CMPAD.

## Decision rule

Prove MPCF analytically, or freeze the first exact obstruction to this
specific common flux.  Do not replace it with a norm on either Abel sum or
any constituent.  At most one exact `k=13` guard is allowed after source
locking and analytic work.  No CMPAD/CBPV/SOCL/BODT/DOR or downstream
inference is licensed absent a proof.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

