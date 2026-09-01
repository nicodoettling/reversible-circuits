# M324 final report

Date: 2026-08-14 UTC

## Verdict

```text
OBSTRUCTION-PROGRESS.
PREDECLARED MN-WCD: REFUTED AS A PROOF MECHANISM.
ACTUAL d>=6 HPRN: UNRESOLVED.
```

## Proved progress

For an active pivot `P` and witness `h_P in D_I(P)`, M324 proves

```text
D_(I union {P})(Q)
 =(D_I(P) intersect D_I(Q));h_P^(-1).
```

Hence the child `G`-cell is exactly the parent compatibility neighborhood of
`P`, while child incompatibility edges are exactly empty parent triple
intersections with `D_I(P)`.  The exact child weighted conflict mass is the
corresponding triple-shadow sum.  This is the strongest surviving recurrence.

## Numbered obstructions to MN-WCD

1. **Inactive maximizer.**  The positive anchor and every forced pivot have
   signature `H_I`, are isolated in the exact incompatibility graph, and
   have compatibility-neighborhood weight `W_I`.  A global maximizer of
   that weight is therefore isolated; it does not strictly shrink `V` and
   can be a pure covariance step.
2. **False polynomial cardinality premise.**  Uniform positive weights have
   `U=M`, with
   `|M|=d^(d-3)(2d-2)!/d!>=d^(d-3)`.  Thus no universal `K` gives
   `|U|<=d^K`; one-vertex deletion cannot certify polynomial pivot depth.
3. **Triple-shadow regeneration.**  The exact `d=3` raw matching
   `[0,1,2,9]`, with leaf weights one and center weight `1/100`, makes a
   maximum active leaf pivot increase normalized conflict density from
   `600/90601` to `2/9`.  This is a boundary obstruction to a generic
   graph-only Lyapunov proof, not a counterexample to actual `d>=6` HPRN.

## Strict next lemma

`pivot_recurrence_obstruction.md` states AATSD: choose a positive anchor with
inverse-polynomial initial weight and then only active incompatibility
endpoints, with exact triple-shadow density paying every logarithmic weight
loss and decreasing by an inverse polynomial at each nonterminal child.
This would telescope to explicit universal
`B=B_0+1`, `C=C_0+C_1` and prove HPRN.  AATSD is unresolved and requires
new actual-specific three-signature structure.

## Firewalls

M135 conflict independence, transitivity, pair moments, and the `d=3`
boundary facts do not prove actual pair compatibility.  No broad `d=6`
census or symbolic search was run.  A heavy proper compatible subcell remains
a direct WRAD route only; it is not HPRN/PHTC.  APOH, literal length, routing,
gap, mixing, and all downstream theorems remain outside this mission.
