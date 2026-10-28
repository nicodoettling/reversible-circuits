# R3 frozen plan v1

Date: 2026-10-28. Base commit d8893491e04aff74ff3185f7054470ffa24a44a4. Target law: uniform global fixed-length transposition identity words, canonical labels [N], ordered positions, rightmost-first map composition. No Markov kernel is involved.

## Frozen candidate FG.v1 (before new derivation)

For every fixed integer G>=0, seek an explicit finite J(G) such that for every integer j>=J(G), with N=2^(8j), m=2^(6j), P=N+m+2 and L=max{1<=v<=N:3^v<=P^4}, the uniform bridge probability of the event E_(G,L) that every nontrivial support component has genus at most G OR size at most L is at most 2^(-1-jm/2). Consequently any law supported on E_(G,L) has TV error at least one minus that bound. The G=2 specialization answers M2. Constants and quantifiers beyond this target, especially all-N quantifiers, require a separately frozen statement.

This is a new enlarged-event bound, not the invalid implication that H0/H2 failure persists under enlargement. It does not refute the mission sampler or certify a local mixing obstruction. A fixed-genus decoder remains useful as a primitive even if this global policy fails.

## Dependencies and derivation plan

1. Read exact historical DYZ recurrence/count normalization and its coefficientwise factorial majorant; rederive the envelope, keeping the published recurrence as an explicit dependency.
2. Use exact labeled component assembly with top-level fixed L. Do not multiply marginal event probabilities.
3. Extend the finite H0 numerator bound to g<=G, directly summing the added genus terms. Bound a geometric power moment uniformly for q<=1/2.
4. Reuse the elementary embedded-subgroup denominator with a complete proof under the current convention. Determine an explicit J(G).
5. Falsify finite auxiliary inequalities, count normalizations and edge cases using deterministic exact arithmetic under a coordinator-reserved bounded job only. Write scripts first; submit resource estimate/command. No stochastic claims or seeds beyond deterministic seed=0 metadata.
6. Freeze proof, statement and full report; worker status remains provisional pending blind and exact-version nonauthor review.

## Historical regressions and scope checks

Read old obstruction.md, source_checks.md, roles/r2-obstruction/corollary-h2-v1.md, roles/r5-referee/blind_report.md and roles/r4-construction/reduction.md under experiments/20260922-sparse-boundary. The all-N blind claim is retained provisional, never imported as accepted. Old H0/H1 and enlarged-cutoff failures remain scoped negative findings.

Other historical regressions remain active: zero-square (ab)^3 insertion, exposed-support 81 versus80, support-graph bias, marked-cut multiplicities, adaptive normalizers and CP-1. This argument uses exact cardinalities, no insertion/cut decoder or sequential marginal products. Boundary tests classify odd m, m=0, m=2, N=2, minimum connected length and singleton positive genus correctly. No sampler logic is changed.

Expected resource use: analytic proof first; finite exact table checks at v<=8 and modest lengths, plus exact polynomial-identity/constant comparisons, well below1GiB and180s if admitted. No exhaustive large word enumeration. Detailed data to a unique role artifact; console under1KiB. One heavy job campaign-wide.
