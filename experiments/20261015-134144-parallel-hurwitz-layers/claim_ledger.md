# Parallel Hurwitz layers: claim ledger

All new proofs are author-checked and pending independent review. Exact
enumeration checks finite formulas, not asymptotic mixing. Products act
rightmost first; all layer results assume even m and independent uniform
ternary coordinates unless explicitly labeled as the square-bath extension.

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| Literal boundary Hurwitz preserves an arbitrary fixed endpoint | refuted | cyclic pair (last,first), other gates fixed | proof.md section 2; results.jsonl five-cycle witness | exact product calculation; not a second reviewer | reject naive boundary for general g |
| Twisted boundary preserves g and is a length 2m-3 ordinary Hurwitz sequence | proved | fixed endpoint g | proof.md section 2; check.py seam_lift | exhaustive small cases, same author | promote scoped formula |
| Pure layer target is uniform on its ordinary Hurwitz orbit | proved | inverse signs equiprobable; boundary corrected unless literal rule is valid | proof.md section 1 | exact inverse-vector, commutation and component checks | promote orbit scope only |
| Pure layers sample arbitrary global uniform identity words/graphs | refuted | arbitrary initial state, no square bath | all-equal words are frozen; exact identity components | explicit symbolic obstruction | retain negative finding |
| Form comparison (2/3) E_seq <= E_parallel <= (m/2) E_seq | proved | single-slot cyclic seq normalization | proof.md section 3 | complete scalar eigenvalue types through matching size 20; general symbolic proof | promote comparison without rare-vector loss |
| gap_parallel >= (1/48) min(m gap_seq,1) | proved | AAV v3 Lemma 2 / Corollary 3; at most two noncommuting neighbors | proof.md section 4 | source hypotheses and constants checked by author; no independent review | promote provisional theorem |
| Parallel and ordinary linear orbit walks have the same polynomial-mixing status in N,m | proved | uniform finite orbit; time counted in layers versus single updates | proof.md section 5, polynomial stationary-flow comparison | seam lift checked exactly | promote comparison; no claim of a new all-N gap |
| Minimal commuting endpoint family has parallel gap Theta(m^-2) | proved | even m>=4, N>=2m, endpoint a product of m disjoint transpositions; CLR v4 Theorem 1.1 | proof.md section 6 | exact m4 benchmark; primary generator normalization checked | promote nontrivial circuit-order benchmark; support is constant |
| Separate parallel square-bath extension has global uniform target and S3 gap >=1/256 | proved | local kernel I/2+H/4+R/4; previous adjacent connectivity and S3 gap | proof.md section 7; prior nonlocal-lift/cycle-excess proofs | twisted boundary bath checked; inherited S3 theorem, no independent review | keep explicitly separate from pure ternary proposal |
| Growing-N full-cycle m=N+1 polynomial mixing | unresolved | pure orbit or augmented global kernel must be specified; even m covers odd N | first missing lemma in proof.md section 8 | no polynomial sequential gap supplied | do not promote |

Dependency audit: The pure comparison uses the checked arbitrary-projector
detectability lemma, not a tensor-product assumption or a finite-window gap
extrapolation. The commuting benchmark additionally uses the checked
interchange theorem. Only the separately declared square-bath extension
uses prior project irreducibility and S3 results. The support-marginal
nonlumpability obstruction from the previous audit remains in force.
