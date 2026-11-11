# Claim ledger

All proof statuses refer to the self-contained foreground arguments, not an
independent review. Independent checks below mean a separately implemented
same-agent computation unless explicitly stated otherwise.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
| --- | --- | --- | --- | --- | --- |
| Inverse stable sorting of two uniform bridges samples exact D1 | proved; efficiency conditional | Global all-transposition bridges, all k-subsets, ideal uniform draws; shorter bridge samplers for efficiency | proof.md section 1; check.py | Full conditional fibers at S3m4/S4m4/S4m6 compared with literal enumeration | Keep exact reduction; no all-length efficiency claim |
| Likelihood is X_k/E X_k and all fixed-I probabilities coincide | proved | Same frozen game | proof.md sections 1–2; exact mask counts | Mandatory literal mask enumeration and separate S4m8 histogram | Keep diagnostic normalization |
| Repeated-gate threshold exposes most TV in N5/6/8,m8,k4 | proved exact finite fact | Only listed finite parameters and exact D1 | results.json, feature-histograms.json.gz | Separate S4m8 attack confirms the implementation route | Reject these finite cases as evidence for a hard gap |
| k=m-2 admits transported repeat counting; TV symmetric in k,m-k | proved | Identity words, involutory transpositions, prefix conjugations | proof.md section 3; check.py | All orbit checks at k=m-2 and selected complete mask checks | Treat both short sides as attack controls |
| Repetition is not universally the strongest observable | proved exact finite fact | N3,m12,k6 | results.json: repeat marginal 0.002845 versus full TV 0.016486 | No separate audit of this larger histogram | Retain minority finding; do not generalize small central attacks |
| Fixed even m,k gives TV=O_(m,k)(1/N) | proved | Fixed lengths; constants may depend on m,k | proof.md section 4; support coefficients | Independent leading-coefficient count and lower-N cross-checks | Keep fixed-length obstruction to a computational interpretation; no growing-length inference |
| Search hardness follows with negligible null witness existence | conditional | Computational indistinguishability and rarity at an explicit efficient schedule | proof.md section 5 | Direct verifier reduction; null rarity fails in tested central cases | Keep conditional consequence, not an application |
| Recursive planting yields computationally uniform global identity descriptions | conditional | Exact short bridge decoder; nonuniform planting indistinguishability uniformly at every internal length | proof.md section 6 | Exact finite recursive laws in recursive-results.json; no independent security-proof review | Keep a concrete conditional application; original uniform single-sample assumption does not yet justify the hybrid |
| Recursion can amplify detectable bias from short leaves | proved exact finite fact | N3/N4,m4/6/8, exact base length two versus four | recursive_check.py, recursive-results.json | One-level laws match the independent main experiment | Reject silently replacing recursive children by uniform children |
| Some growing-length schedule yields useful computational hiding | unresolved | Efficient generation and nonnegligible statistical separation still needed | First unproved obligation in proof.md | None | No hardness assumption endorsed; no manuscript promotion |
