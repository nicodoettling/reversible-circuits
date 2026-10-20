# All-pair interval-gap claim ledger

All proofs are author results pending independent review.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| The arbitrary-position lifted Hurwitz/square walk is uniform-reversible | proved | Uniform pair choice, both signs, transported middle conjugations, fixed endpoint | proof.md Section 1; exact inverse and integer balance checks | Same-author checks only | keep |
| Pure arbitrary-position Hurwitz is globally irreducible for every endpoint | refuted | No square branch | Two different doubled-transposition words at m=2 are frozen; subgroup invariant | Elementary direct check | retain scope obstruction |
| (2/m) E_A <= E_G <= 4m^2 E_A, every N | proved | Exact half-lazy K_A,K_G defined in proof | proof.md Section 2; stationary path marginals and exact weighted occurrence formula | Deterministic count checks through m=100, not independent proof review | promote provisionally |
| S3 transported pair updates act as interval translations on independent ternary prefixes | proved | All feasible endpoints; m>=2 | proof.md Section 3; 3276 words, 299340 channels | Exact exhaustive algebra checks, same author | promote provisionally |
| Auxiliary interval heat bath Q has gap 1/m | proved | F3^(m-1), half laziness and uniform intervals | Fourier diagonalization in Section 4; all modes through m=9 checked | Symbolic completeness proof plus 9832 finite modes | promote provisionally |
| Actual K_G has gap in [1/(2m),3/(4m)] and polynomial mixing | proved | N=3, every feasible endpoint, m>=2 | Channelwise comparison to Q; proof.md Section 4 | Exact interval identities and transition ratios | promote provisionally |
| Full-cycle m=N+1 has inverse-polynomial K_G gap as N grows | unresolved | Same all-pair kernel | No required growing-N Poincare inequality established | Small-case checks are not asymptotic evidence | retain open target |

Decision: proof-progress; continue-local-chain. The strengthened comparison
and S3 proof do not resolve the growing-N conjecture.
