# M315 Independent Proof Audit

Date: 2026-08-14 UTC.

Verdict: **ACCEPT M312 at reduction-only scope.**

## Reconstruction

For a fixed anchor, substitute the unique parameterization

```text
beta=alpha_0;s;delta_0^(-1),  s in S
```

into every endpoint fiber. This gives

```text
beta in F_Q  iff  L_Q;s;R_Q in S.
```

A global weighted maximizer has positive score and hence lies in some
positive-weight anchor fiber. Maximizing over such anchors therefore equals
the unrestricted maximum; a fixed arbitrary anchor is only conditional.

For compatible `I`, the chronological right action gives

```text
T_I=H_I;s_I,
x_Q^(h;s_I)=y_Q
 iff x_Q^h=y_Q^(s_I^(-1))
 iff h in D_I(Q).
```

Intersecting the last equation proves the higher-arity law and the one-pivot
update. If `s'_I=g;s_I`, then
`D'_I(Q)=D_I(Q);g^(-1)`. Accepted frame changes give

```text
s'_I=u_0^(-1);s_I;v_0,
H'_I=u_0^(-1);H_I;u_0,
D'_I(Q)=u_0^(-1);D_I(Q);u_0.
```

Thus the witness and frame covariance claims are correctly oriented and all
used predicates are intrinsic.

The equality `D_I(Q)=H_I` is equivalent to `x_Q^s_I=y_Q` together with
pointwise fixation of `x_Q` by `H_I`. Every `h;s_I` therefore satisfies
all of `F(I)`, proving `HSCA => WRAD` through the outer-anchor identity.

For the formal identity matching in the natural `Sym(X)` or `Alt(X)`
action, identity has agreement density one. For an HSCA-eligible distinct
pivot tuple `I` containing the anchor, `H_I` is its pointwise stabilizer.
Its fixed set is exactly `I` when `N-|I|>=2` in `Sym`, or `>=3` in
`Alt`; hence `F(I)=I`. With

```text
N_d=d^(d-3)(2d-2)!/d! >= d^(d-3),
```

every fixed polynomial pivot bound `|I|<=d^B` has
`|I|/N_d<d^(-C)` for every fixed `C` at sufficiently large `d`.
This is exactly a generic-geometry proof-route obstruction. It is not an
actual-M135 realization and makes no actual-M135 negative claim.

If PHTC supplies one
`h in intersection_(Q in G_I(U)) D_I(Q)`, then `h;s_I` satisfies every
constraint in `G_I(U)`; its anchored score proves `PHTC => WRAD`.
The formal identity example survives by taking the positive anchor alone and
the identity residual. In the accepted actual three-edge `d=3` subfamily,
support sizes one and two use the whole support; for support size three, the
greatest-weight pair has singleton transporter, extendable cell exactly that
pair, and at least two-thirds of the weight. These are narrow survival checks,
not a complete rank-three or an actual `d>=6` theorem.

## Numbered objections

Material objections: **none**.

Nonmaterial clarifications:

1. M312 Section 5's displayed `F(I)=I` retains the predeclared HSCA
   quantifier that `I` contains the anchor. If the anchor is omitted, the
   formula is `F(I)=I union {anchor}`; the obstruction is unchanged.
2. The frozen rank-three paragraph states the nontrivial full-support branch.
   The support-size-one and support-size-two branches above complete the claim
   for arbitrary nonzero weights without changing it.

Finite nonemptiness remains separate from polynomial literal braid length.
Actual `d>=6` HSCA/PHTC/WRAD and literal length remain unresolved. No MRAD,
SSTID, routing, voltage, congestion, spectral gap, mixing, or Terminal
conclusion follows.
