# M327 independent proof audit of frozen M324

Date: 2026-08-14 UTC.

Verdict: **ACCEPT at the exact frozen obstruction/reduction scope.**

## 1. Residual graph and one-pivot law

At a compatible pivot tuple `I`, M324 uses exactly M317's finite-action data

```text
H_I={h in Sbar:x_R^h=x_R for R in I},
z_Q^I=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I:x_Q^h=z_Q^I},
V_I={Q in supp(lambda):D_I(Q) nonempty}.
```

The residual incompatibility graph has an edge precisely when two literal
residual signatures have empty intersection.  This is an exact chart-
stabilizer orbital condition and is not M135's coarser paired-generated-
subgroup conflict graph.

Choose `P in V_I` and `h_P in D_I(P)`.  At the child witness
`s_child=h_P;s_I`, a child element `k` fixes `x_P` and sends `x_Q` to
`(z_Q^I)^(h_P^-1)` exactly when `a=k;h_P` belongs to both `D_I(P)` and
`D_I(Q)`.  Conversely every such `a` gives `k=a;h_P^-1`.  Therefore

```text
D_child(Q)=(D_I(P) intersect D_I(Q));h_P^-1.        (1.1)
```

Uniform right translation preserves emptiness.  Consequently

```text
V_child={Q in V_I:D_I(P) intersect D_I(Q) nonempty}
       =C_I(P),                                      (1.2)
```

and, for child vertices `Q,R`,

```text
D_child(Q) intersect D_child(R)
 =(D_I(P) intersect D_I(Q) intersect D_I(R));h_P^-1. (1.3)
```

Thus child bad edges are exactly empty parent triple intersections.  They
need not be the parent graph induced on `C_I(P)`.  The weighted recurrence
`Phi_child=T_I(P)` and normalized formula
`rho_child=2T_I(P)/c_I(P)^2` follow directly.  These claims are exact.

## 2. Why the global compatibility maximizer stalls

For the normalized outer anchor, `x_(Q_0)=y_(Q_0)=c`, every `s_I` and every
element of `H_I` lie in `Sbar`, and hence

```text
D_I(Q_0)=H_I.
```

For every pivot `P in I`, compatibility gives
`y_P^(s_I^-1)=x_P`, while `H_I` fixes `x_P`; thus `D_I(P)=H_I` as well.
More generally, any forced vertex with signature `H_I` meets every nonempty
signature in `V_I`, is isolated in the incompatibility graph, and has

```text
c_I(P)=lambda(V_I)=W_I.                              (2.1)
```

Every endpoint of an incompatibility edge omits at least one strictly
positive support weight from its compatibility neighborhood, so its score is
strictly below `W_I`.  Because the anchor supplies a forced vertex, every
global maximizer of `c_I` is isolated.  Equation (1.2) then gives
`V_child=V_I`: the predeclared strict-shrink mechanism fails.  A forced
choice is only a covariance translate; an isolated nonforced choice may
regenerate higher-intersection edges by (1.3).  M324's correction to active
endpoints is necessary and correctly stated.

## 3. Actual matching size

M135's perfect matching has one edge for every free global-conjugacy orbit.
The accepted minimal-sector count and free `S_d` action give

```text
|M|=|Z_d|/d!=d^(d-3)(2d-2)!/d!.                     (3.1)
```

Uniform positive weights make `U=M`.  Since the factorial ratio is at least
one and `d^(d-3)` eventually exceeds `d^K` for every fixed `K`, no universal
polynomial support-size premise is possible.  Hence even genuine one-vertex
deletion would not by itself prove polynomial pivot depth.  M324's second
obstruction is exact and actual all-rank.

## 4. Strict `d=3` triple-shadow scope

For the authenticated matching `[0,1,2,9]`, the three leaf fibers
`K_0,K_2,K_9` meet pairwise but have empty triple intersection; all three
pairs involving center `1` are empty.  With leaf weights one and center
weight `1/100`, the parent star has

```text
W=301/100,       Phi=3/100,       rho=600/90601.
```

Every maximum active pivot is a leaf.  Pivoting at `0` deletes the center,
but (1.3) makes `{2,9}` a child edge, so

```text
W'=3,            Phi'=1,          rho'=2/9.
```

Thus `log(W/W')>0` while `rho-rho'<0`, refuting a generic graph-only
Lyapunov argument.  This calculation is before outer anchored normalization
and at `d=3`; M324 explicitly uses it only as a boundary firewall.  It does
not prove or refute actual `d>=6` HPRN or AATSD.

## 5. Corrected AATSD formulation

AATSD retains all material quantifiers: universal constants, every nonzero
weighted actual `d>=6` matching, a positive anchor with inverse-polynomial
initial weight, and at each nonterminal actual node an active endpoint whose
exact child obeys both logarithmic weight-loss payment and inverse-polynomial
triple-shadow density decrease.

Conditionally on these unproved clauses, `0<=rho<1` permits at most
`d^B_0+1` pivots.  Summing the logarithmic inequalities telescopes to

```text
W_final>=W_0/d^C_1>=||lambda||_1/d^(C_0+C_1).
```

The final graph is edgeless, giving HPRN with the displayed polynomial
exponents.  This conditional implication is correct.  M324 labels the
initial anchor bound, active triple-shadow inequalities, AATSD, and actual
`d>=6` HPRN as unresolved; none follows from the `d=3` boundary or pair data.

## 6. Numbered objections and firewall

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
3. **Accepted:** exact child signature/neighborhood/triple-shadow recurrence;
   inactive-maximizer obstruction; actual superpolynomial matching-support
   obstruction; strict `d=3` graph-only density obstruction; AATSD as an
   unresolved sufficient formulation.
4. **Unresolved:** AATSD and actual `d>=6` HPRN, APOH, SPBE, PHTC, and WRAD.
5. **No inference:** literal representative length, SSTID, routing, voltage,
   congestion, spectral gap, mixing, or Terminal.

No new rank, census, candidate, or grouping was introduced in this audit.
