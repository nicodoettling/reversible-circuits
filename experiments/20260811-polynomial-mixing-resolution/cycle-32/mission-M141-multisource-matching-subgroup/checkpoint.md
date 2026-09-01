# M141 halfway checkpoint

Date: 2026-08-13 UTC.

Status: universal `d>=5` theorem proved; exceptional-rank audit complete;
final self-audit and freeze remain.

## Proved theorem

Fix `d>=5`, an adjacent DPS edit `tau_i`, and any perfect matching in
M135's orbit-incidence multigraph.  Choose one source representative `u^q`
for each matching edge and put `v^q=tau_i(u^q)`.  For every nonempty
subfamily `I` of `s` matching edges, define the aligned position-tuple groups

```text
Gamma_U(I)=<(u_j^q)_(q in I):1<=j<=2d-2> <= S_d^s,
Gamma_V(I)=<(v_j^q)_(q in I):1<=j<=2d-2> <= S_d^s.
```

Then both groups equal the literal common-parity subgroup

```text
P_(d,s)={(g_q):sgn(g_q) is independent of q}.
```

The proof is independent of the chosen representatives and matching
decomposition.  A matching has distinct left and right endpoints, so M135's
accepted pair dichotomy gives `P_d` in every two-coordinate source projection
and every two-coordinate target projection.  Each tuple generator is
odd in every coordinate, hence `Gamma<=P_(d,s)`.  For
`N=Gamma intersect A_d^s`, every two-coordinate projection is `A_d^2`.
A self-contained induction proves that a subgroup of a direct power of a
nonabelian simple group with every pair projection full must be the full
direct power.  Therefore `N=A_d^s`; one odd generator supplies the other
parity coset and gives `Gamma=P_(d,s)`.

The smallest ranks cause no hidden exception inside the theorem.  `A_5` is
nonabelian simple.  `A_6` is also nonabelian simple; a diagonal coupling via
an exceptional automorphism would have a graph, not full, two-coordinate
projection.  M135/M137 already exclude the outer automorphism of `S_6` when
establishing the input pair dichotomy because it does not preserve the
transposition class.

## Exact exceptional-rank audit

The deterministic checker verifies the frozen M137 checker hash, rebuilds
the accepted `d=3` DPS matchings, and closes every aligned subgroup exactly.
For all three adjacent edits and all three colors in that deterministic
decomposition:

- every one-source group is `S_3` of order `6`;
- every pair group is `P_3` of order `18`;
- every triple group still has order `18`, not `|P_(3,3)|=54`;
- every four-source group still has order `18`, not `|P_(3,4)|=162`;
- each full source subgroup differs literally from its full target subgroup.

Thus nonabelian simplicity is essential.  The checker also constructs the
smallest abstract warning at arity three: the order-`18` extension of
`{(x_1,x_2,x_3) in A_3^3:x_1x_2x_3=id}` by one simultaneous odd tuple has
all pair projections equal to `P_3` but is proper in `P_(3,3)` of order `54`.
At `d=4`, M135's pair premise itself can fail (`96 -> 288`) and its uniform
coloring theorem uses singletons, so no rank-four extension is claimed.

## Remaining obligation

The theorem removes every generated-subgroup obstruction, at every arity,
from a `d>=5` matching.  It does **not** produce a common braid.  The exact
remaining problem is still nonemptiness of the simultaneous action-coset
intersection `intersection K_Q`, followed by a polynomial signed-braid word
length bound.  The number of matching edges can be enormous, and no compact
matching evaluator or schedule is supplied.
