# Bounded endpoint error claim ledger

All new proofs are author results pending independent review. The word
`proved` below describes the supplied argument, not external certification.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| Half-lazy accepted single-gate refresh is uniform-reversible | proved | All transpositions, fixed N,m, fixed endpoint ball; no claim of irreducibility from symmetry | proof.md Section 1 | Exhaustive reverse-channel checks in results.jsonl | keep |
| Even-length budget 1 equals budget 0; budget 2 is unrestricted in S3/S4 | proved | Identity center | Cycle parity and maximal even defect; boundary checks | Separate full labeled enumeration | keep; add procedural warning to experiment guide |
| Every exact identity word communicates with every other inside the defect-two space | proved | N>=2, even m; full transposition gate library | proof.md Section 3, self-contained vertex sweep and two-edit simulation | 62,571 exact Hurwitz/square channels checked in audit.jsonl | keep; no congestion claim |
| All states of defect <=k-2 reach the exact core inside the k-ball | proved | Identity center, even m | proof.md Section 3 | Symbolic normalization/triangle-inequality argument; no new quantitative claim | keep; boundary shell remains |
| Every nonexact word admits a strict-descent single-gate edit | refuted | Already fails at N4,m4,k2 | Explicit witness and defect path 2,2,0 in proof.md Section 4 | All 20 replacements inspected in audit.jsonl | retain negative finding |
| Full relaxed connectivity at k2 for every N and even m<=6 | proved, computer-assisted | Support bound and complete relabeling quotient; exact core connectivity | proof.md Section 4; quotient.py and quotient.jsonl | Five labeled/quotient graph agreements and nine independent labeled endpoint counts | keep provisionally; fixed lengths only |
| Every defect-two word is at most two edits from an exact word, for all lengths | conjectured | Suggested only by the completed small-length checks | All checked distances <=2 | No all-length proof or length-eight result | do not promote |
| At m4,k2,N>=14, gap<=5/binom(N,2), and mixing time >=floor(binom(N,2)/10) | proved | Precisely the half-lazy rejection kernel | proof.md Section 5, repeated-first-pair cut | Eight exact quotient cut calculations, N4 through N100 | keep; polynomial slowdown only |
| Two numerical finite gap estimates are positive constants | empirical, uncertified | 300 centered power iterations, two fixed seeds | spectral.jsonl | Residuals and seed discrepancies retained; no certified lower bound | do not infer asymptotic mixing |
| Relaxed uniform k2 law gives exact endpoint with probability >=1/[1+2C(N,3)+3C(N,4)] | proved | Identity center, even m | proof.md Section 6; convolution Cauchy--Schwarz | 231,160 finite count inequalities; probability checks | keep |
| Polynomial mixing at k2 would imply polynomial-time near-uniform exact-functionality sampling at every feasible length | conditional | Worst-case polynomial mixing of the relaxed chain; independent restarts | proof.md Section 6 | Conditioning error/acceptance arithmetic checked | retain beside its unproved hypothesis |
| Polynomial mixing at k2 or at k=C log N | unresolved | Needs connectivity and a growing-N,m gap bound | proof.md Section 7 | Finite spectra do not settle it | keep as a research candidate, not a theorem |

No minority/negative result was discarded. The aborted length-eight
generation is recorded in plan.md and supports no mathematical claim.
