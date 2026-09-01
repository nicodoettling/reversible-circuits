# M122 plan: rooted-product local comparison

Date: 2026-08-12. Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact scope

The target is the uniform law on

```text
Z_d = {w=(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                                  support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed tuple factors multiply
left-to-right.  The physical kernel is the half-lazy signed adjacent-Hurwitz
walk

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_i (R_i+R_i^(-1)),
R_i(a,b)=(b,bab), R_i^(-1)(a,b)=(aba,a).
```

M112/M119 prove the exact rooted DPS bijection
`rooted Z_d <-> UST(K_d) x S_(2d-2)` and an inverse-polynomial ideal product
gap.  This mission attacks only the missing **ROOTED PRODUCT LOCAL
COMPARISON**.  It does not claim anything for arbitrary-product `Gamma_0`,
the global bridge law, or the `{3,4,5}` heat-bath chain.

## Named claim under test

For every ideal adjacent-value permutation swap and valid UST basis exchange,
construct a distribution on signed adjacent-Hurwitz paths whose length and
stationary edge congestion are `d^O(1)`, accounting for the exact uniform
white-root quotient.  In particular seek a recoverable descriptor consisting
of the changed ideal coordinate, the affected tree path/face interval, path
time, and root, with polynomial source multiplicity.

If this cannot be proved, rigorously refute a precisely stated local routing
scheme by an explicit infinite family or an exact minimal counterexample;
mere global closure, long finite distance, or failed implementation is not a
refutation of the comparison lemma.

## Work plan

1. Reconstruct DPS closure/inverse and record how an ideal coordinate edit
   changes the rooted Hurwitz tree before closure.
2. Derive locality formulas for adjacent face-label swaps and tree basis
   exchanges.  Test whether only a bounded union of contour/stack intervals
   changes, paying special attention to nested stack cascades and repeated
   identical face transpositions.
3. Implement independent exact audits for all rooted pairs at `d=3,4`; add
   exhaustive structural summaries or fixed-seed samples at `d=5` where
   feasible.  Store machine-readable JSON.
4. Attempt randomized path construction without canonical hubs.  Prove path
   validity, polynomial length, endpoint correctness, and descriptor
   recoverability/source multiplicity; then calculate stationary congestion
   including the `d` roots.
5. If a step fails, isolate and falsify the narrowest named locality/routing
   assertion, retaining minority/negative evidence.  Write a halfway
   checkpoint, proof note, report, reproducible commands, manifest, and hashes.

## Expected failure modes

- A local edit of the open Hurwitz tree triggers a linear-depth hairy-closure
  cascade; linear depth alone is not fatal, but loss of source information may
  be.
- Repeated equal face transpositions make the changed ideal labels
  unrecoverable from a physical edge and time.
- Lexicographic shortest paths have polynomial length in small ranks but hide
  exponential asymptotic multiplicity.
- Root refreshing is silently treated as a physical move or the exact
  `d`-to-one quotient is omitted.
- A theorem is accidentally asserted only from finite `d<=5` data.

## Verdict standard

`promote` only for a complete polynomial comparison proof with explicit
normalizations.  `keep` for a rigorous new structural lemma or a decisive
refutation that strictly narrows the first open obligation.  Otherwise
`inconclusive`.
