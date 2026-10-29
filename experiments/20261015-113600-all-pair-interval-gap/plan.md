# all-pair-interval-gap

- Created UTC: 2026-10-15T11:36:00.659462+00:00
- Objective: Prove an S3 all-pair gap and a degree-independent comparison for the actual lifted pair walk
- Target distribution: Uniform ordered length-m transposition words with fixed product g
- Parameters: all feasible endpoints, N>=2 and m>=2 for the comparison; N=3 and all m>=2 for the gap theorem. Products act rightmost first. State-independent uniform pairs, linear boundaries, half laziness.
- Tested claims: the S3 move is an interval translation in independent ternary coordinates; the auxiliary interval heat bath has gap 1/m; the actual K_G has gap between 1/(2m) and 3/(4m); a stationary-path comparison gives (2/m) E_A <= E_G <= 4m^2 E_A at every N.
- Commands: `python3 -B experiments/20261015-113600-all-pair-interval-gap/check.py`.
- Raw data: results.jsonl (one complete deterministic JSON record).
- Expected failure modes: omitting middle conjugation; confusing pure Hurwitz with the mixed chain; wrong prefix signs; incorrect normalization of laziness; treating polynomial comparison as a general gap theorem.
- Validation: exact S3 words at lengths 2 through 7 and Fourier modes through length 9; identity bridges S3,m=4 and S4,m=4,6; exact inverse, endpoint, elementary lift and detailed-balance checks. No stochastic conclusions or random seeds.
- Interpretation: promote only scoped author proofs, pending independent review. No claim for growing-N full-cycle m=N+1.
- Next changes: proof, exact diagnostic, report and claim ledger; map integration with a new provisional record.
