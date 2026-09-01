# M196 plan: target-directed exact Q5 pair decisions

## Objective

Decide as many as possible—and preferably all—of M191's 54 named `d=5`,
width-two synchronized quotient targets without constructing the full source
stabilizer orbit. Use only target-directed simultaneous/product search or
exact coset-intersection certificates derived from M191's frozen 8,400-point
action and transversal.

## Target and convention

The exact finite target is diagonal signed-Hurwitz component membership from
source IDs `(16,0)` in `Q_5^2`. The fourteen generator permutations correspond
chronologically to `1,...,7,-1,...,-7` and act on the right.

There is no probability distribution or Markov kernel in this structural
mission.

## Immutable gate and method

1. Verify M191 and M194 manifests completely; never edit them.
2. Rebuild the chronological first-coordinate BFS transversal from frozen
   action rows and derive the adjusted second IDs for all 54 targets.
3. Deduplicate those adjusted targets before searching.
4. Prefer exact target-directed stabilizer-word searches with early stopping.
   A positive result requires an explicit chronological word, direct replay on
   both coordinates, and a compact reproducible certificate.
5. A negative result is allowed only after a complete finite coset/orbit
   decision for that target. No bounded-depth miss is negative evidence.
6. Do not compute or archive the full stabilizer orbit, enumerate `Q_5^2`, or
   call the generic Magma stabilizer.

## Resource cap and exclusions

Cap total computation at five minutes and modest memory. If targets remain
undecided, freeze INCONCLUSIVE with only completed exact positives and no new
negative claims. No every-color, all-`d`, polynomial route length, gap,
mixing, or Terminal conclusion.

## Deliverables

Write `checkpoint.md` before computation, a halfway/cap checkpoint, proof note,
target-directed checker and JSON, nine-field report, freeze manifest, and
hashes. Verdict: ACCEPT only for a complete requested classification; otherwise
INCONCLUSIVE unless a complete exact counterclassification is established.
