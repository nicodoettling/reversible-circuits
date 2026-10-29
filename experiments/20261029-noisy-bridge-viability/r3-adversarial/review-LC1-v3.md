# Exact-version referee addendum: LC1-v3

Reviewer r3-adversarial, 2026-10-29. This addendum preserves and resolves the two objections in `review-LC1-v1-v2.md`. It does not overwrite that report or the earlier statements. The underlying identity was independently reconstructed blind in BS1. I am the reviewer who raised the issues; a separate fresh reviewer remains part of coordinator certification.

## Exact inputs

| Artifact under experiment root | SHA256 |
|---|---|
| coordinator/local-channel-statement-v3.md | 439f7744357ca1e78a582b427143cedbc33f8f2058cad209038c5aae9708c7ca |
| coordinator/local-channel-proof-v3.md | ca4e2ce94108182d111add869078a9db3507438d08281b0611617d8cac002ae1 |
| coordinator/final-decisive-v1.py | 1b33ad99ba79c15adc1f6c3411ca1d819e2f3cafafdd0145635889b12565a586 |
| coordinator/final-decisive-v1.json | fdb1c68b040c32427b73173753e3414291f4f823230d646c1acdab81ae59e87a |

These complete files were read. The earlier 108-case checker/result hashes and assessment are in the preserved review. The new targeted script was executed by the coordinator as J005; I inspected rather than duplicated the mathematical run.

## Resolution

The finite probability identity, positive-eigenvalue domain, affine normalization and [0,1] range are unchanged and remain proved. The explicit operand bound from v2 remains correct by the denominator-product argument reviewed earlier. V3 now places public uniform polynomial-time f evaluation, polynomial output bit bound b (or a charged polynomial-size table), and publicly computable positions next to the efficient M0 corollary. This closes the missing access/cost assumption. It correctly allows arbitrary rational f only for the finite identity, not automatically for an efficient adversary.

The proof's example f=2^(-2^lambda), written with its ordinary explicit rational denominator, explains why a small coordinate dimension does not ensure a small value representation. The separate hidden-key lookup example explains the public-interface condition. No arbitrary rational oracle or uncharged advice is assumed. Fixed-s polynomiality follows because q^s,4^s and the repaired bit bound are polynomial under the explicitly stated parameter/evaluation assumptions. The expected-time and fair-bit qualifications remain accurate.

The targeted denominator regression uses q=2 and s=1,...,6 with distinct prime denominators. It confirms that all those primes survive in the mean denominator; at s=6 the maximum individual denominator has 9 bits but the mean denominator has 497 bits. For s<=4 it explicitly checks T g=f, h in [0,1], and divisibility by the constructed common denominator. This targets the actual v1 omission. These finite numbers are not a proof of any general complexity lower bound; the symbolic denominator accounting proves the v3 upper bound.

The same decisive script evaluates literal gates by applying the reversed list to each input point, independent of the array-right-multiplication implementation, and recovers the required S4,L6 bridge count 3936. It also checks a disjoint-doubled-edge count at S6,L4. These support the coordinator's smallest decisive recheck requirements for the broader report without becoming new assumptions of LC1.

## Verdict

**Recommend acceptance of LC1-v3 in its exact stated scope.** Both review objections are resolved in this version. No further mathematical or efficiency-interface repair is requested. Fresh author-distinct recheck and final coordinator ledger closure remain procedural gates, and same-model agreement is correlated. This lemma only transfers an available public local bias; it does not supply such a bias for every candidate, infer general repeated-key amplification, or certify cryptographic hardness.
