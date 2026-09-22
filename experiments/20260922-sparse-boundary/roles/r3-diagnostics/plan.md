# Plan

Target: exact finite U_(N,m)=uniform labeled, ordered all-transposition identity words. Composition (alpha beta)(x)=alpha(beta(x)); rightmost first. H0 admits each component with genus<=1 OR support<=K; H1 admits support<=K only. K=max{v<=N:v^(2v)<=(N+m+2)^4} is fixed at top level. No Markov kernel is involved.

1. Hash-frozen intake and inspect exact connected/assembly counting primitives.
2. Timed <=90-second m<=16 pilot; verify known exact totals and boundary support events.
3. Increase only to resolve named decision: first nonzero H0 error inside m^4<=N^3, compare H0/H1 omitted classes, or falsify an identified inequality.
4. Reuse/audit changed algorithm regressions and preserve fixed-cutoff and arbitrary-genus cases.
5. Save raw JSON early; checkpoint every ten minutes/major findings; maintain report with exact scope and no asymptotic inference from finite values.

Expected failures: cutoff mistakes, genus<=1 confusion with H0, finite ratios misread as asymptotic proof, factorial count normalization, missing support history, large-int decimal serialization, expensive exact counting. Standard-library deterministic arithmetic; stochastic seeds 1729,2718,31415 only if needed.

Repository source-of-truth disagreement: GOAL_SPEC/HANDOFF concern local-chain mixing and predate sparse sampling. Frozen user-approved brief supersedes objective while proof/safety standards remain.

Environment: command python unavailable; use python3 -B.
