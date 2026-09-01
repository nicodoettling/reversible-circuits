# M321 Independent Proof Audit of M319

Date: 2026-08-14 UTC.

Verdict: **ACCEPT at the exact analytic-obstruction scope.**

## 1. Fully combined token expansion

Fix one H/A/C row and one supported quantile cell `(s,t)`. The normalized
extended laws `g_s,f_t` are formed only after both live channels, all
`T/S/N` kinds, phases, seams, owner incidences, representation averages,
raw lifts, and literal zero slots have been combined. Their common-part
coupling has residual profile masses

```text
a(P)=[g_s(P)-f_t(P)]_+,
b(Q)=[f_t(Q)-g_s(Q)]_+,
rho=sum_P a(P)=sum_Q b(Q).
```

To make the raw lift explicit, disintegrate each profile atom over its finite
complete raw fiber. Proportionally give a raw `g` atom over profile `P`
residual mass `a(P)` times its conditional fiber weight, and similarly give
a raw `f` atom over `Q` residual mass `b(Q)` times its conditional
fiber weight. For `rho>0`, the product of these residual raw masses,
multiplied by

```text
c_X pi_(s,t)/rho,
c_X=r_X(alpha_1+alpha_2),
```

is a positive token directed `P->Q`. Summing over both raw endpoint fibers
recovers exactly

```text
c_X pi_(s,t) kappa_(s,t)(P,Q).
```

When a denominator profile mass is zero, its residual mass is zero and there
is no token. The diagonal common part contributes no unordered off-diagonal
edge. This construction retains every cell and complete raw label, including
profile zero, and takes no constituent norm.

## 2. Exact edge coefficient

Fix the canonical orientation `P<Q` of `e={P,Q}`. Summing all positive
tokens directed `P->Q` and all negative tokens directed `Q->P` gives

```text
L_e^+=c_X sum_(s,t) pi_(s,t) kappa_(s,t)(P,Q),
L_e^-=c_X sum_(s,t) pi_(s,t) kappa_(s,t)(Q,P).
```

The corrected M313 flux definition therefore gives, with no omitted cell,
slot, or normalization,

```text
J_e=L_e^+-L_e^-.
```

For the residual-product formula this is also the difference of
`[-delta(P)]_+[delta(Q)]_+ / rho` and its reverse. Edges incident to
profile zero are ordinary edges in the same identity.

## 3. Atom-split involution and boundary

Concatenate the positive and negative token atoms in the frozen order and
identify them with disjoint weighted intervals `[0,L_e^+)` and
`[0,L_e^-)`. Split atoms at the required coordinates. On
`[0,min(L_e^+,L_e^-))`, exchange `(+,u)` with `(-,u)`. This map is an
involution, preserves weight and the unordered edge, and reverses
orientation.

The only unpaired interval is on the larger side, so exactly

```text
mass(Boundary_e)
 =L_e^++L_e^--2 min(L_e^+,L_e^-)
 =|L_e^+-L_e^-|
 =|J_e|.
```

Summing once over unordered edges yields

```text
sum_e mass(Boundary_e)=sum_e |J_e|=||J||_edge.
```

There is no factor of two; that factor appears only later in the divergence
inequality `||div J||_TV<=2||J||_edge`.

## 4. Circularity verdict

The qualitative pairing uses only two finite positive masses. It exists for
every finite signed edge table and is therefore tautological after the
orientation totals have been computed. Its order-relative adjective
"canonical" supplies no intrinsic grading or localization.

Because its total boundary is identically `||J||_edge`, each quantitative
PEBP bound is exactly the controlling corrected MPCF bound with the same
H/A/C scale. Quantitative PEBP is not false; it is unresolved because it is
MPCF itself. Hence PEBP is correctly rejected only as a narrower proof
reduction.

The two-profile construction `g_s=delta_P,f_t=delta_Q` gives
`|J_e|=c_X` under the abstract coupling axioms. It correctly shows that the
Borel coupling data alone supplies no `O(1/k)` scale, but it is not an
actual owner-profile counterexample.

## 5. Source-local raw coboundary formulation

M319's proposed next obligation is genuinely stronger in form: before
consulting final edge surpluses, a fixed source-local surgery must pair
nonexceptional raw tokens within the same unordered edge with reversed
orientation, and a source-local exceptional predicate must have the three
required Borel-scale masses. Read "weight coboundary identity" as exact
signed-measure cancellation, including all multiplicities, on the
nonexceptional set.

Such a certificate would localize the surviving flux and imply the desired
edge bound from exceptional mass. M319 supplies no surgery, exceptional-set
bound, or theorem establishing it. It is correctly recorded only as a
falsifiable formulation.

## 6. Numbered objections and scope

Material objections: **none**.

Nonmaterial objections: **none**.

The arbitrary atom order can move which pieces are called boundary but cannot
change its mass; M319 explicitly records this. No computation, new rank, or
alternate pairing is needed. MPCF, CMPAD, CBPV, SOCL, and every routing,
voltage, congestion, gap, mixing, or Terminal claim remain unresolved.
