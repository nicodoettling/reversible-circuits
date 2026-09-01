# M208 plan: rooted one-leaf DPS recursion

## Objective

After M203/M205 refuted fixed-filler block locality, seek the corrected
one-leaf transformation for the full rooted DPS matched target.  Determine
whether adjoining a doubled leaf admits an exact symbolic recurrence whose
coupling is confined to the root-to-leaf contour and can be implemented by a
bounded synchronized braid.

## Immutable inputs

Treat M203/M205 and the accepted DPS route chain as read-only. Verify the
relevant frozen inventories before depending on them; never amend predecessor
artifacts.

## Proof program

1. State the rooted DPS descriptor and the exact operation that extends a
   d-label source word by a doubled leaf.
2. Compare the recovered d and d+1 descriptors at the tree, ordering,
   boundary-contour, closure-pairing, and target-word levels.
3. Derive a candidate recurrence allowing all contour-mediated changes, not
   merely a fixed complement.
4. Test it exactly on the fourteen d5-to-d6 witnesses and falsify it on the
   first boundary case if it is not uniform.
5. If a uniform recurrence survives, prove the corresponding synchronized
   braid/correction statement. If not, isolate the precise missing datum or
   exact obstruction and state the narrowest surviving conditional lemma.

## Computation cap

Use compact exact symbolic checks only on the named d5/d6 descriptors. Do not
enumerate `Q_6` or search the d6 quotient graph.

## Scope exclusions

No claim about arbitrary d6 target reachability, every matching color, all-d
routing, polynomial route or voltage-correction length, spectral gap, mixing,
or Terminal follows without a separate proof.

## Deliverables

Initialization and halfway checkpoints, immutable gate, compact checker/raw
JSON, proof or exact obstruction, nine-field report, freeze manifest and
hashes, then a fresh-audit request.

