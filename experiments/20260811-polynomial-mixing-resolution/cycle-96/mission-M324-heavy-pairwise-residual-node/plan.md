# M324 plan: heavy pairwise residual node

Date: 2026-08-14 UTC

This file and `checkpoint.md` are created before any substantive predecessor
payload is opened.  M324 writes only in this directory.

## Objective and fixed scope

Attack only the actual `d>=6` HPRN gate from M317/M320.  The ambient target
remains the global fixed-length uniform identity bridge for the lazy exact
same-product `{3,4,5}` heat-bath chain, but this mission concerns only the
finite signed-Hurwitz chart action for one actual M135 matching.

For every nonzero weight vector `lambda>=0`, retain M312's outer
positive-weight anchor.  HPRN must have universal constants `B,C`: it must
produce a compatible pivot tuple `I`, `|I|<=d^B`, such that, for
`U=supp(lambda)` and `V=G_I(U)`,

```text
lambda(V)>=||lambda||_1/d^C
```

and every two residual signatures in the whole `V` intersect.  A heavy
proper compatible subcell proves WRAD directly but is not HPRN or PHTC.

## Exact graph to reconstruct

At a compatible node define the residual incompatibility graph

```text
Gamma_I: vertex set V=G_I(U),
{Q,R} is an edge iff D_I(Q) intersect D_I(R)=empty.
```

It is not the M135 paired-generated-subgroup conflict graph.  Put

```text
W_I=lambda(V),
Phi_I=sum_{{Q,R} in E(Gamma_I)} lambda_Q lambda_R,
rho_I=2 Phi_I/W_I^2,
c_I(P)=sum_{Q in V: {P,Q} not an incompatibility edge} lambda_Q.
```

## Predeclared analytic candidate: maximal-neighborhood pivot with
## weighted conflict decay (MN-WCD)

After source-locking the exact normalization, start from an accepted
positive-anchor compatible node whose weight loss and pivot count are charged
explicitly.  Whenever `Gamma_I` is nonempty, choose `P in V` maximizing
`c_I(P)` (ties by the frozen matching order), extend the node through one
witness in `D_I(P)`, and require universal constants `A,K` such that

```text
log(W_I/W_(I,P))
 <= A log(d) (rho_I-rho_(I,P)),                       (MN-WCD)
|U|<=d^K.
```

The exact child-neighborhood identity must first be proved from the frozen
right-action formulas.  If MN-WCD holds, every nonterminal pivot strictly
shrinks the finite residual vertex set, so there are at most `d^K` pivots;
telescoping gives total multiplicative loss at most `d^A`.  Combining the
anchored start cost with this loss yields explicit universal `B,C` and an
edgeless final `Gamma_I`, hence HPRN.

MN-WCD is a falsifiable candidate, not an imported theorem.  The first audit
target is whether pivoting can create new exact incompatibility edges from
higher intersections, invalidating `rho` decay.  If it fails, freeze the
first exact local obstruction and state a strictly narrower actual-specific
source-local lemma sufficient to repair the recurrence.

## Firewalls

- no inference from M135 conflict independence, transitivity, or pair moments;
- retain both exact `d=3` boundary firewalls without extrapolating to `d>=6`;
- no broad `d=6` action census; at most one symbolic local obstruction after
  the recurrence is fixed;
- no APOH, common full extension, literal length, routing, voltage,
  congestion, spectral gap, mixing, or Terminal inference;
- no predecessor, coordinator, manuscript, handoff, goal, guide, or skill
  edits.

## Decision rule

Freeze either a complete HPRN proof with explicit universal exponents, or the
first exact weighted-pivot obstruction to MN-WCD together with the strongest
strictly stated next lemma.  Request genuinely fresh audit.
