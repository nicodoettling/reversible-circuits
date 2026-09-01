# M312 substantive checkpoint

Date: 2026-08-14 UTC.

Status: `analytic stop reached; preparing freeze`.

## Proved exact laws

For nonzero weights, unrestricted WRAD is the maximum over positive-weight
anchors of the anchored stabilizer score

```text
max_(s in S) sum_Q lambda_Q 1[L_Q;s;R_Q in S].
```

A fixed arbitrary anchor gives only the corresponding conditional maximum;
the outer anchor is material.

At a compatible pivot tuple `I`, with witness `s_I`,

```text
T_I=H_I;s_I,
T_(I union J)
 ={h;s_I:h in intersection_(Q in J)D_I(Q)}.
```

Witness changes right-translate every `D_I(Q)` by the same element, while
frame changes conjugate them all by the same reference factor.  Hence the
signature nonemptiness, forced-cell, and common-intersection predicates are
intrinsic.

## First obstruction

The predeclared HSCA forced-cell condition would imply WRAD.  However, in
the natural `Sym/Alt` identity matching, a polynomial-size pivot tuple has
forced cell equal only to its pivots, although the identity action agrees
with every constraint.  Thus HSCA is not a consequence of general
transitivity, uniform fibers, and transporter-coset geometry.  This is a
formal proof-route obstruction, not an actual-M135 counterexample; actual
HSCA remains unresolved.

## Surviving reduction

PHTC replaces pointwise forced agreement by an exact higher-arity collapse:
among the positive-weight constraints individually extendable from a
polynomial-size compatible node, an inverse-polynomial-weight cell must
have one common residual transporter.  The recursive law proves
`PHTC => WRAD`.  PHTC survives both the `Sym/Alt` identity matching and the
accepted actual `d=3` triple, but remains unresolved at actual `d>=6`.

No `d=6` computation is being run because the analytic stop was reached.
Literal representative length remains separate, and no downstream theorem
is inferred.
