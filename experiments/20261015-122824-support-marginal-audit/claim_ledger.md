# Support-marginal audit claim ledger

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| The limiting support law weights graphs by compatible circuit counts | proved | Uniform fixed-endpoint circuit law; vertex labels and multiplicities retained | proof.md (1), finite fiber counts | Exact balance checks, same author | keep |
| Arbitrary-pair selection makes the support graph a closed Markov chain | refuted | Actual K_G=I/2+H_G/4+R_G/4 | Minimal N4 and genus-one N4 witnesses (3),(4) | Complete finite channel checks; minimal witness also explicit by hand | promote obstruction provisionally |
| The averaged graph kernel can be iterated from any uniform fiber lift | refuted | Same reversible K_G and raw support projection | Two-step identity (6), 1/288 discrepancy in minimal N4 | Exact within-fiber variance identities in six fibers | keep |
| Fast stationary-flow projection alone ensures fast graph marginal mixing | refuted | General finite uniform reversible lazy chain | Four-state delta example (7) | Rational matrix and finite union-bound checks | keep proof-method obstruction |
| Graph marginal mixing needs the full circuit gap | refuted as a general necessity | Some spectral modes can be invisible to the graph | Invariant observable-space theorem (8)--(10); disjoint m2 example | Self-contained proof, no independent review | keep weaker sufficient criterion |
| S3 all-length graph marginal mixes in polynomial time | proved | Exact actual K_G and feasible endpoints | Prior S3 gap plus data processing | Prior checked actual-chain theorem; current S3 graph row audit | retain scoped positive result |
| Full-cycle N+1 graph marginal mixes in poly(N) steps | unresolved | Growing N, actual K_G, weighted graph target | No observable-space polynomial inequality proved | Nonlumpability does not imply slow mixing | retain user's target |
| Triangle presence separates the selected S3 star witnesses | refuted for that event | w=aaab and v=abaa from the test | Both probabilities are 1/9 in raw output | Exact channel counts | retain negative trial; use actual row witnesses |

All results are same-author work pending independent review. Verdict:
obstruction-progress for the proposed transfer, inconclusive for the
user's marginal-mixing conjecture. Continue the actual-chain investigation;
no replacement sampler or general slowdown claim is made.
