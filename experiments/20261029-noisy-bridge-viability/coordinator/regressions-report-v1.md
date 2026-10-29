# Exact regression receipt v1

Bounded J001 completed exit 0 in 3.3495 seconds, Python 3.12.3, stdlib, no randomness. Exact command and resource estimate: job-registry.json. Raw results: regressions-v1.json. Input projection checker was imported without invoking its main() and was not changed. It uses composition p[q[i]], consistent with rightmost-first products.

Ten even small cases, including S3,L4=27, S4,L4=120 and S4,L6=3936 global bridges, pass inherited projection/replacement checks. Empty words and N=2 pass. Four odd cases have zero identity words. Exact pair-equality smoke checks include k=0,1,L and q=1. For k=L, every full observed word has iid mu law by construction; this is an analytic complete-word equality, not merely an endpoint claim.

LC1 finite tests cover 108 (q,s,L,k) cases for q in {1,2,3}, s in {1,2,3}, L in {s,s+1,s+2}, all k. They verify T*g=f on every alphabet point for every indicator-basis function whenever k<=L-s, and exact annihilation of the centered top component when k>L-s. Each inverse bound is checked pointwise. This finite gate corroborates the symbolic proof and does not prove its unrestricted theorem.

CP-1 reproduces posterior masses and 21/2000>1/100; the invalid marginal-product argument is rejected. Support removal and renormalization are retained as the failure mechanism. The recorded 21/221 second-hit incidence is checked against the threshold; no general sequential bound is inferred.

No stochastic security statement, approximate reference, long-word enumeration, nonstandard dependency or system resource change was used. Remaining task: exact-version author-distinct review and candidate-specific tests.
