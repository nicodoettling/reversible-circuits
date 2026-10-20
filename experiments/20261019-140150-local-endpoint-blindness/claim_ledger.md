# Claim ledger

All proofs are same-author work. Finite checks are separate falsification
attempts, not independent review or evidence for an unproved asymptotic gap.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| Exact marginal formula for any specified subset of gates | proved | all transpositions, uniform fixed-product fiber | proof.md Proposition 1; 23,823 integer checks | no independent reviewer; exhaustive finite checks | keep |
| Dense uniform bridges hide their endpoint locally with exp(-Omega(N^2)) error at m>=N^3, k=O(N) | proved | parity; CLR Theorem 1.1 with displayed normalization | proof.md (2)--(4); primary theorem checked | imported theorem; algebraic transfer shown | keep |
| Locally blind starts can retain pinned prefixes and global TV near 1-2/N! | proved | independent long subbridges | proof.md (5)--(7); dense exact counts through S5 | exact S3 k-wise witness, all three even endpoints | keep |
| Local blindness persists within a random influence interval | proved | state-independent finite-range scan, iid-preserving local branches | proof.md (8); 19,805 interval geometry checks | deterministic geometry falsification only | keep |
| Many hidden prefix pins require order m log q updates to erase | proved scoped lower bound | separated interior cuts, long segments, q/N! small | proof.md (9); exact moment inequalities | polynomial bound only, not a slow-mixing refutation | keep |
| A locally invisible slowest eigenmode exists for Q2 in S3 | proved | S3 independent prefix coordinates; half-lazy Q2 | proof.md (10)--(11); exact time-0 through time-3 distributions | all three even endpoints at m8; Q345 also checked | keep |
| Long overlapping exact block heat baths mix for every endpoint in O(q log(q/epsilon)) updates | proved | eta_L<=1/16; exact block oracle; q=floor(m/L)>=2 | proof.md Theorem 5; exact S4 conditional laws | conditional-weight check, no independent proof referee | keep; declared alternative kernel |
| Actual K_A gap >=(2L-1) gamma_*/[16(m-1)] | conditional | uniform all-endpoint local block gap gamma_* in lengths 2L through 4L-2 | proof.md Proposition 6; 8,029 normalization checks | algebraic slot-count audit | keep conditional |
| Identity mixing plus local endpoint blindness implies all-endpoint mixing of the same small-move kernel | unresolved | user's proposed hypothesis, precise initializer restriction still matters | proof.md Sections 6--7 | no counterexample or completed reduction | retain as research question |
| Local blindness alone eliminates every slow spectral mode | refuted | exact local matching to stationarity | S3 Q2 slowest-mode witness | rational eigenfunction/distribution checks | reject this intermediate inference |

The large-overlap strategy was already present in archived M10 and its
referee. The new note must not be cited as first discovery of HB-BASE or as
a solution of its arbitrary-endpoint base-gap obligation.
