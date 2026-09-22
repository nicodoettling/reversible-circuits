# Coordinator review notes — not a substitute for complete worker audits

2026-09-07, first reading approximately 21:20 UTC. All candidate conclusions
remain provisional until the current implementation/proof passes nonauthor
review. No candidate argument was sent to the blind referee before its
blind report is frozen.

## R1-T1 first reading

The primary Vakil source was checked directly at Section 1.2, Corollary 1.5,
and Proposition 3.2. The count factor q(a)=a^a/(a-1)! equals the alternative
a^(a+1)/a! convention. Multiplying G by the cycle-length product gives the
number of ordered factorizations of one fixed permutation. There is no
unaccounted sheet-label, equal-cycle, or position quotient in C_g.

I rederived the three final-transposition cases. Removing the last edge
from a connected support graph leaves at most two components. If its two
endpoints belong to different final permutation cycles, right composition
merges those cycles, forcing the endpoints into one predecessor support
component, and hence the whole predecessor is connected. A same-cycle final
transposition gives either a connected genus-(g-1) predecessor or two
connected components with genus sum g. In the latter case the lower-labeled
endpoint distinguishes A, removing a possible factor-of-two ambiguity.

For the allocation DP I checked the identities

    e_j(alpha+a)=e_j(alpha)+a e_(j-1)(alpha),
    S_j(alpha+a)=S_j(alpha)+a S_(j-1)(alpha)+a^2 e_(j-1)(alpha).

Summing these over genuine partial assignments gives the stated update;
E_0 counts assignment multiplicity. A forced A/B prefix changes the allowed
DP transitions, so the next decision uses the actual conditional mass. The
proof does not reuse an unconditional marginal after restriction. CP-1 is
therefore recorded as inapplicable to this exact telescoping argument,
rather than run as an unrelated exercise.

The factorial cancellation in interleaved child counts is exact even when
a genus-one child would be the zero-count singleton: those masses vanish
in the positive formula. Recursive length drops by one across the sum of
children at each positive node, so there are exactly r such nodes and at
most N singleton leaves. This controls the visited states without an
exponential memoization inventory.

Rational powers have smallest exponents -2 for genus zero and -1 for the
genus-one marked terms. The claimed denominator 24(N!)^5 is a conservative
common multiple across all split choices. Products of cycle factorials
divide N!, and size-power denominators divide the remaining factorial
powers. The bounded caches in the implementation do not hide an unbounded
endpoint table.

Implementation observation sent to author: the first sample() version used
Python recursion, which can hit interpreter depth limits despite a polynomial
abstract algorithm. An explicit work stack is preferable to altering process
or machine recursion settings. This is an implementation correction request,
not a counterexample to the combinatorial theorem; the final implementation
must receive a review after the change. Initial code otherwise matches the
disjoint branch and allocation formulas at this reading.

Pending decisive tests: full per-word law or reconstruction multiplicities,
forced-prefix allocation sums against a separately computed count formula,
N=1 and singleton branches, bounded random-integer correctness, and the final
stack implementation. A successful read-through is not certification.

## R2-C1 first reading

The independently derived genus-zero endpoint primitive agrees with R1 at
the word-decomposition level. M97 cut existence was rechecked by the
prefix/suffix genus and incidence Euler characteristic argument. Uniform
decorated-cut forgetting weights a word by |J(w)|, so the proposed reciprocal
rejection corrects the right multiplicity and its acceptance is at least
1/(2N-1) once the proposal law is uniform on cut incidences.

The outer unicyclic grammar is more elaborate than R1 and needs a separate
code/multiplicity audit. In particular preserve checks for the two-edge
parallel core, empty hanging forests, degree-one size-one vertices, ordered
child factorials, 2s core encodings and intermediate truncation ranges. No
acceptance is inferred merely from matching total decorated counts.

## Global G1.v1

global_consequence.md records the complete coordinator proof and conditional
assembly theorem. Independent exact total counts and component extraction
matched the inherited positive DYZ table; every allowed word's macro sampling
probability was checked in the prescribed tiny cases. The saturated m=2N
characterization and asymptotic omission bound are new proof candidates,
separate from the finite certificate table, and await nonauthor review.

## Final mathematical reconciliation — 2026-09-07 21:59 UTC

The provisional observations above are preserved review chronology. I read
the complete final R2 recursive_audit.md, R3 candidate_audit.md and
global_audit.md, and R1 structural_audit.md. All accept their exact frozen
inputs. The recursion-depth concern is repaired in the reviewed explicit
stack implementation; both nonauthors tested its actual forward sampler.
The conservative rational arithmetic bound was weakened before the freeze;
all final audits accept O(N^10 log^3(N+1)). No late unchecked mathematical
repair is promoted.

I reran the full author X4/forced-assignment audit, R2's new forward-stack
test, and R1's new structural-parser test in bounded fresh processes. All
passed. Raw results and logs are at this experiment's root. The structural
review checks actual parser conditionals and output laws, not just totals.

R3's initial G1-SAMPLE acceptance was conditional because the connected
primitive was then awaiting review. Its candidate audit and R2's review now
discharge that exact dependency. G1.v1.1 clarified N0 and size-two wording;
G1.v1.2 closes the certification gate. S1.v2 adds canonical input/fair-bit
conventions and current status to unchanged R1-T1.1 mathematics. The
integration file changed only its introductory description from provisional
to audited after review.

No mathematical disagreement remains on T0. Negative findings are retained
in the registry and full reports. Same-model agreement alone certifies
nothing: source normalization, decomposition, DP identities, exact
conditional probabilities and bit bounds are written out, with finite
tests as falsification attempts. Final artifact consistency remains a
separate nonauthor delivery check.
