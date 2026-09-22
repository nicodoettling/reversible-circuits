# R2 obstruction report

Verdict: **promote R2-O1; current proof accepted by R1 and R3 nonauthor
audits, coordinator owns final certification**. The unchanged H0 sampler has
TV error tending to one at the exact proposed boundary along
N=2^(8j),m=2^(6j),j>=64. More precisely,

    TV(H0,U_(N,m)) >=1-2^(-1-jm/2).

The proof is obstruction-v1.md. H0 is unchanged: every small component
v<=K retains arbitrary genus, while larger components retain genus0/1.
The target is global fixed-length uniform identity words, with rightmost
factor acting first. The obstruction compares exact included/total counts;
it does not rely on upper-bound vacuity or extrapolation of finite data.

Candidate | target | identity valid | global support coverage | exact checks | status
---|---|---|---|---|---
H0 unchanged | Unif(A), compared with Unif(Omega) | yes, imported exact sampler | tends to zero on explicit sequence | coefficient/denominator checks pass | P0 refuted, internal mathematical audits accepted
H1 unchanged | Unif(B), B subset A | yes, imported exact sampler | at most H0 | subset implication | P1 refuted by same obstruction
Another algorithm | full global negligible approximation | unresolved | unresolved | outside obstruction | T0 unresolved

The numerator uses the positive component exponential formula, replacing
the exact falling label factor(N)_s by N^s. The factorial genus majorant
bounds the allowed component exponent at x=k/N^2 by8k. The September5
embedded-subgroup denominator is independently reconstructed by midpoint
symmetry and Cauchy-Schwarz. Its previous minimal-only consequence is not
silently upgraded; the new ingredient is the complete H0 numerator bound.

All internal inequalities have explicit constants and finite hypotheses.
There is no identified unproved internal step. The remaining certification
obligation is coordinator reconciliation. R1's obstruction_audit.md and
R3's r2-obstruction-audit-v1.md accept the current hash, with no requested
repair. Root reported a full read and direct source audit with no issue.
Same-model checks are correlated internal review, not human certification.

Reproduce author tests from repository root:

    timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r2-obstruction/check_obstruction.py

results.json records4960 denominator checks, coefficient comparisons,
16 finite numerator bounds,381 retained high-genus small-support terms,
and exact benchmark/cutoff checks through j256. Tests are deterministic,
standard library only; no random seed is used. Required counts27,120,3936
and m0,m2,odd m,N1,N2 branches pass. Runtime was under0.1s. Neither sampler
logic nor its imported files were changed. Input SHA256s, commit and Python
version are in input_hashes.json/environment.json/results.json.

Negative/minority findings retained: earlier minimal-only and literal
genus<=1 obstructions do not suffice for H0; the previous finite tail
becoming vacuous is not a lower bound; this sampler-specific result does
not imply hardness or disprove the existence target T0.

Additional authorized work: the nonauthor audit r1-audit.md accepts the
frozen positive UPPER.v2 theorem at hash b76f706..., proving negligible
error through m<=N^(2/3)ln(N)/4 with its explicit eta. Independent exact
checks passed3850 genus/rising comparisons,1045 finite-binomial identities,
and409 near-minimal zero cases. Decoder/runtime imports remain assigned
to R4, so this report does not certify their implementation.

A separately versioned corollary, corollary-h2-v1.md, proves the same
boundary obstruction for R4's H2-QC size cutoff L=max{v:3^v<=P^4} and
its genus0/1 hybrid. It follows from the finite numerator lemma with
L<=32j+4 and b_Lx<=1; exact parameter checks are saved. R4's nonauthor
h2-obstruction-audit.md accepts this corollary. R2-O1 and H0 are unchanged.
