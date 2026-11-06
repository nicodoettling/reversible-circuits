# Blind halfway checkpoint

2026-10-28, approximately 11:20 UTC. No construction or other referee material read.

## A

Working conclusion: provable from the allowed genus-two generating formula. Delete the last transposition. A prefix is either connected (genus unchanged when two endpoint cycles join; genus decreases by one when a cycle splits) or has exactly two components (child genera sum to the parent genus). For the disconnected case, label every cycle separately and anchor the two new cycles to opposite children.

The remaining obligation was polynomial computation of partition masses, rather than enumeration of cycle subsets. Lagrange inversion turns each positive-genus normalized count into a constant number of terms consisting of at most four marked cycles, a denominator-allocation count q, and independent per-cycle factors. For fixed child degrees, a DP tracks degree assigned to the first child and the two denominator-allocation counts. Forced membership decisions support sequential exact conditional sampling. No inventory has exponentially many states. Full details and signed-coefficient handling are being written.

## B

Working conclusion: provable with margin. The DYZ recurrence yields

`h(g,v) <= h(0,v) v^(2g) binom(v+g-2,g)`.

Set `x = 2^(-5j-6)`. The sum of allowed connected component weights `h(g,v) N^v x^(2v-2+2g)` is at most `2m`: bound low-genus terms using `h(g,v) <= exp(4v) 2^(3jg)`, and small-degree terms by summing the all-genus majorant with the unchanged top-level cutoff `L <= 33j`. Consequently the event numerator is at most `2^((11j+9)m)`.

For `k=floor(m/(8j))`, a Cauchy–Schwarz return-count lower bound inside the fixed subgroup `S_k` gives bridge denominator at least `2^((12j-2log2(j)-43/4)m)`. Their ratio is at most `2^(-(j/2+1/4)m)` for `j>=64`, stronger than the stated target. Constants and boundaries are being rechecked in the report.

## Reserved finite check

Coordinator reservation I1-J5 completed with wrapper exit 0; 65 fixed-permutation count comparisons passed over 65,835 enumerated word prefixes, and 42 DYZ-majorant comparisons passed. Raw data are in `check-results.json`. No retry or other computation occurred. The finite check corroborates normalizations only; it does not substitute for the general proofs.
