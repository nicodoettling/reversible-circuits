# M324 exact pivot recurrence and first obstruction

Date: 2026-08-14 UTC

Status: **exact child identities proved; predeclared MN-WCD refuted as a
proof mechanism; actual `d>=6` HPRN remains unresolved.**

## 1. Scope, target, and quantifiers

Fix `d>=6`, one adjacent edit index, one actual M135 perfect matching `M`,
and a nonzero vector `lambda>=0`.  Keep M312's outer positive-weight anchor
`Q_0`.  Write `U=supp(lambda)`.  Signed Hurwitz actions are chronological
right actions.

At a compatible pivot tuple `I`, with witness `s_I`, use the authenticated
finite chart-stabilizer data

```text
H_I={h in Sbar:x_P^h=x_P for P in I},
z_Q^I=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I:x_Q^h=z_Q^I},
V_I=G_I(U)={Q in U:D_I(Q) nonempty}.
```

The exact residual incompatibility graph is

```text
Gamma_I=(V_I,E_I),
{Q,R} in E_I iff D_I(Q) intersect D_I(R)=empty.       (1.1)
```

It is not M135's generated-subgroup conflict graph.

## 2. Exact one-pivot recursion

Let `P in V_I`, choose `h_P in D_I(P)`, put `I'=I union {P}`, and use
`s_(I')=h_P;s_I`.  Then for every `Q in U`,

```text
D_(I')(Q)
 =(D_I(P) intersect D_I(Q));h_P^(-1).                (2.1)
```

### Proof

If `k in D_(I')(Q)`, then `k` fixes `x_P` and
`x_Q^k=(z_Q^I)^(h_P^(-1))`.  Thus `k;h_P` sends `x_P` to `z_P^I` and
`x_Q` to `z_Q^I`, so it lies in both parent signatures.  Conversely, if
`a` lies in both parent signatures, then `k=a;h_P^(-1)` fixes `x_P` and
sends `x_Q` to the new target.  This is exactly the child signature.  QED.

Consequently, defining the parent compatibility neighborhood

```text
C_I(P)={Q in V_I:D_I(P) intersect D_I(Q) nonempty},
c_I(P)=lambda(C_I(P)),
```

gives the exact identities

```text
V_(I')=C_I(P),               W_(I')=c_I(P).           (2.2)
```

For `Q,R in V_(I')`, (2.1) also gives

```text
D_(I')(Q) intersect D_(I')(R)
 =(D_I(P) intersect D_I(Q) intersect D_I(R));h_P^(-1).
                                                               (2.3)
```

Thus the child edge relation is the empty **parent triple-intersection**
relation.  It need not be the graph induced from `Gamma_I`.

Put

```text
Phi_I=sum_{{Q,R} in E_I} lambda_Q lambda_R,
rho_I=2 Phi_I/W_I^2,
T_I(P)=sum_{{Q,R} subset C_I(P)} lambda_Q lambda_R
       1[D_I(P) intersect D_I(Q) intersect D_I(R)=empty].       (2.4)
```

Then the strongest exact weighted recurrence is

```text
Phi_(I')=T_I(P),
rho_(I')=2T_I(P)/c_I(P)^2.                            (2.5)
```

These formulas are witness- and frame-invariant by uniform right translation
and conjugation.

## 3. First actual formula-level obstruction: the maximizer is inactive

The outer anchor satisfies `C_(Q_0)=Sbar`.  At every compatible node,
`s_I in Sbar`, `H_I<=Sbar`, and therefore

```text
D_I(Q_0)=H_I.                                        (3.1)
```

Likewise, for every `P in I`, compatibility gives `z_P^I=x_P`, while
`H_I` fixes `x_P`, so `D_I(P)=H_I`.  More generally call `P` forced when
`D_I(P)=H_I`.

Every forced vertex is isolated in `Gamma_I` and has

```text
c_I(P)=W_I.                                          (3.2)
```

Because every vertex in `V_I` has positive weight, each vertex incident to
an incompatibility edge has `c_I(P)<W_I`.  Hence maximizing `c_I(P)` over
all of `V_I`, as MN-WCD predeclared, always selects an isolated vertex, never
an endpoint of the edge that must be removed.  Equation (2.2) gives
`V_(I')=V_I`, contradicting the plan's asserted strict vertex shrink.

If the selected isolated vertex is forced, (2.1) is only the accepted
witness-covariance translate and the graph is unchanged.  If it is not
forced, (2.3) can expose new higher-intersection defects.  Thus neither
vertex shrink nor conflict-density descent follows from maximal neighborhood
weight.  A corrected pivot rule must restrict to an **active endpoint**

```text
A_I={P in V_I:deg_(Gamma_I)(P)>0}.                    (3.3)
```

This obstruction is an exact consequence of the actual normalized formulas;
it uses no finite-rank census.

## 4. Second actual obstruction: matching cardinality is not polynomial

The accepted actual perfect matching has

```text
|M|=d^(d-3)(2d-2)!/d!.                               (4.1)
```

Take positive uniform weights, so `U=M`.  Since `|M|>=d^(d-3)`, no fixed
`K` satisfies `|U|<=d^K` for all `d`.  Therefore even a repaired rule that
strictly deleted one residual vertex per pivot would not prove
`|I|<=d^B`.  The `|U|<=d^K` clause in the predeclared MN-WCD candidate is
false on the actual all-rank family.

## 5. Exact weighted edge-regeneration guard at `d=3`

This subsection is a boundary falsification of a generic graph-only decay
argument, not an actual `d>=6` HPRN counterexample.

For the authenticated raw matching `[0,1,2,9]`, the exact result table has
three nonempty and three empty pair intersections.  M301/M304 gives all
three nonempty pairs among `[0,2,9]`; hence the remaining three pairs, from
edge `1` to those vertices, are empty.  The raw incompatibility graph is a
three-leaf star centered at `1`.  Moreover

```text
K_0 intersect K_2={45},
K_0 intersect K_9={49},
K_2 intersect K_9={89},
K_0 intersect K_2 intersect K_9=empty.                (5.1)
```

Give weights `lambda_0=lambda_2=lambda_9=1` and `lambda_1=1/100`.  Then

```text
W=301/100,
Phi=3/100,
rho=600/90601.
```

Every maximum-compatibility active pivot is a leaf, with `c(P)=3`.  Pivoting
at leaf `0` deletes the center but (2.3) turns the empty triple in (5.1) into
the child edge `{2,9}`.  Thus

```text
W'=3,       Phi'=1,       rho'=2/9,
600/90601 < 2/9.                                      (5.2)
```

The predeclared inequality has a positive left side
`log((301/100)/3)=log(301/300)` and a negative right side for every
`A>=0`.  So normalized weighted conflict density is not a Lyapunov function
of the formal pivot identities.

This witness is at `d=3` and is written before the outer anchored
normalization.  It neither proves nor refutes the repaired actual `d>=6`
statement.  It does prove that M135 conflict independence, pair data, and
the accepted abstract transporter geometry cannot supply decay; a genuinely
actual-specific higher-intersection input is necessary.

## 6. Strict next lemma: anchored active triple-shadow descent

The first source-local candidate that avoids both exact failures is:

> **ANCHORED ACTIVE TRIPLE-SHADOW DESCENT (AATSD).**  There are universal
> constants `B_0,C_0,C_1` such that every nonzero weighted actual `d>=6`
> matching has a positive anchor for which the initial residual node obeys
> `W_0>=||lambda||_1/d^C_0`.  Whenever its selected path has
> `Gamma_(I_t)` nonempty, there is an active endpoint
> `P_t in A_(I_t)` such that, with the exact child quantities (2.2)--(2.5),
> ```text
> log(W_t/W_(t+1))
>  <= C_1 log(d) (rho_t-rho_(t+1)),                  (6.1)
> ```
> and, unless the child graph is edgeless,
> ```text
> rho_t-rho_(t+1) >= d^(-B_0).                       (6.2)
> ```

AATSD is **UNRESOLVED**.  It is exact and falsifiable using only one-, two-,
and three-signature data at each actual source node.  It does not select a
proper subcell: every child is exactly `G_(I_t union {P_t})(U)` by (2.2).

If proved, (6.2) and `0<=rho<1` permit at most `d^B_0+1` pivots.  Summing
(6.1) telescopes and gives `W_final>=W_0/d^C_1`.  The final graph is
edgeless, so HPRN follows with, for example,

```text
B=B_0+1,       C=C_0+C_1.                            (6.3)
```

The initial heavy-anchor clause, triple-shadow decay, and polynomial stopping
rate are all material.  No one of them follows from transitivity, pair
moments, or M135 conflict independence.

## 7. Exact stopping line

```text
one-pivot child-signature identity                    proved
child vertex set = exact compatibility neighborhood  proved
child edges = empty parent triple intersections       proved
MN-WCD maximum-neighborhood strict shrink             refuted
MN-WCD polynomial support-size premise                 refuted actually
rho as a formal pivot Lyapunov                         refuted at d=3 boundary
actual d>=6 AATSD                                      unresolved
actual d>=6 HPRN                                      unresolved
```

A heavy proper pairwise-compatible subcell could prove WRAD directly, but
it is not the exact child `G_I(U)` demanded by HPRN/PHTC.  No APOH, common
full extension, literal length, routing, congestion, gap, mixing, or Terminal
inference is made.
