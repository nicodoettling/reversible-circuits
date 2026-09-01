# M211 report: interval-kernel boundary edit

Date: 2026-08-13 UTC. Commit
502a6f031c6d5a4bc0064ee5b370a4fa3914f993.

## 1. Verdict and scope

REFUTE POINTWISE IKBE-b AND THEREFORE THE TWO-CLAUSE IKBE LEMMA.

IKBE-a/DV and the original signed averaged DE lemma remain open.
Conditional J=2, PCR/WPCR, SCBR/BIR/BR/PCS, and all downstream claims remain
open. No such inference is made.

## 2. Immutable gate

Every checksum entry in M192/M195 and M199/M207 passed before use. Their
SHA256SUMS digests are recorded in checkpoint.md. None was edited.

## 3. Target and convention

Target: normalized literal disjoint ordered-double B/A laws under the
uniform minimal-factorization fixed-cell coordinate calculation, n=3k,
odd k>=3. Composition is (pq)(x)=p(q(x)); displayed factors are
left-to-right. The tested observable is the one-run prefix Y_l.

## 4. Exact obstruction

For q>=1 take

    k=12q-1, s=3q, l=4q.

M199's exact closed formulas and seam law reduce the surviving first faces
to F_l(s)=1-s/(2k-1), F_l(2k-1-s)=0,
J_l(s)=1-s/k, and J_l(k-s)=0.

## 5. Uniform analytic certificate

Uniform Stirling bounds b_d asymp d^(-3/2) prove the critical-Borel tail
lemma

    W_(rho k)(f_k) -> (rho/2)(1-e^-1)

whenever f_k(d)->1{d>=2} for every fixed d. The proof controls
M<d<=r/2 by O(M^-1/2) and d>r/2 by O(k^-1/2). The untouched A term tends
to (1-e^-1)/2. Thus the full fragmentation contribution has the same limit
1-e^-1 on B and A.

## 6. Limiting mismatch

Both disjoint normalizers tend to one. The remaining B first-face term tends
to (7/8)^2=49/64, whereas the A marked-plus-untouched term tends to
(7/8)(3/4)=42/64. Hence

    Phi_(3q)^D(Y_(4q))-Psi_(3q)^D(Y_(4q)) -> 7/64.

Since sqrt(4q)/(12q-1)->0, no universal pointwise IKBE-b constant exists.

## 7. Corrected route

This does not refute DE. DE is the signed quantity

    sum_s q_hat_s(Phi_s^D-Psi_s^D),

and may use small macroscopic-split mass and cancellation across s. The
strict corrected route is the original signed averaged DE itself, without
the false pointwise strengthening. IKBE-a/DV is untouched and remains open.

## 8. Diagnostics and first open step

The independent exact formula-only checker is capped at k=3,5,7,9,11 and
performs no topology reconstruction. At (k,s,l)=(11,3,4) it gives a positive
exact defect approximately 0.0922412; finite values are calibration only.

First open steps: prove/refute IKBE-a/DV and prove/refute signed averaged DE.
The pointwise route is closed by the theorem above.

## 9. Artifacts and action

Artifacts: plan/checkpoint, rigorous obstruction proof, formula-only checker
and JSON output, summary JSON, report, and freeze files. Reproduction:

    python3 ikbe_formula_check.py ikbe_formula_results.json

Python 3.12.3, standard library, seed null. Action: freeze the refutation and
request a fresh immutable audit focused on the Borel tail lemma and 7/64
constant. Do not promote conditional J=2 or downstream claims.
