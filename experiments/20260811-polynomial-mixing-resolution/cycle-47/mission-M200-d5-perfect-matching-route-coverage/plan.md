# M200 plan: exact d=5 perfect-matching route coverage

## Objective

Determine exactly which members of M181's explicit width-two, full-voltage
source construction are covered by M196/M198's 54 certified positive target
pairs, separately for every M135 perfect-matching color at `d=5` and every
relevant left source orbit.

## Immutable inputs and gates

1. Verify the full frozen manifests of M135/M137, M181/M183, and M196/M198
   before accepting any conclusion. Never edit those missions.
2. Extract the precise M135 color/matching definition, M181 source and target
   construction, and M196 target inventory. Resolve conventions by exact
   canonical tuple reconstruction rather than labels alone.
3. Construct a finite incidence table whose rows identify a color, relevant
   left source orbit, matched DPS target, quotient target IDs, membership in
   the 54-target theorem, and a routed word/certificate reference when covered.
4. Audit exhaustiveness: every relevant color/source incidence must occur
   exactly once. Any uncovered quotient-target class must be listed exactly.

## Verdict rule

Promote an “every `d=5` color has a routed full-voltage pair” theorem only if
the incidence calculation is exhaustive and the full-voltage/source and
matching conditions are verified literally. Otherwise state the exact covered
and uncovered finite classes without qualitative inference.

## Scope and exclusions

There is no probability distribution or Markov kernel in this structural
mission. The target is finite `d=5` incidence and route coverage only. No
all-`d`, polynomial route-length, spectral-gap, mixing, or Terminal claim is
permitted.

## Deliverables

Write this plan and initialized checkpoint first, then immutable-gate and
halfway checkpoints, compact exact checker, machine-readable incidence table,
proof note, nine-field report, freeze manifest/hashes, and fresh-referee
request.
