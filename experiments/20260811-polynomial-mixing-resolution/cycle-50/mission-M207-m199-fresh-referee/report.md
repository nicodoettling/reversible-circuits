# M207 report: fresh referee of immutable M199

Date: 2026-08-13 UTC.

## 1. Verdict and scope

ACCEPT M199'S STRICT EXACT LITERAL-PROFILE REDUCTION.

IKBE, DV, DE, CONDITIONAL J=2, PCR/WPCR, SCBR/BIR/BR/PCS, AND ALL
DOWNSTREAM CLAIMS REMAIN OPEN.

Material objections: none. Two nonmaterial exposition qualifications are
numbered in Field 8.

## 2. Immutable gate

All eight M199 entries pass sha256sum -c SHA256SUMS. Fresh hashes agree;
the frozen checksum-file digest is
1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed.
M199 was never edited.

## 3. Target and convention

Target: normalized literal ordered-double laws in the B long exterior cycle
and A two exterior k-cycles under uniform minimal factorizations, n=3k,
odd k>=3. Composition is (pq)(x)=p(q(x)); displayed factors are
left-to-right. This is only the conditional J=2 coefficient reduction.

## 4. Normalization

Proved: after the first exterior factor, residual rank is R_*=2k-3. For a
fixed second placement cutting r into d,r-d, the completion ratio is exactly
b_d b_(r-d)/[(2k-3)b_r]. Direct completion recurrence sums these placement
masses to one.

## 5. B tuple and faces

Proved: (i,r,d,a), with r in {s,2k-1-s} and
1<=a<=r-d-1, indexes each disjoint ordered pair exactly once. The two
one-run faces have M199's directed complementary-piece and second-subarc
gaps; their complement is the two-run face. The outer denominator is
2k-1, with no missing factor two. Both three-atom seam laws are exact.

## 6. A mass and literal bookkeeping

Proved: the untouched k-cycle has raw mass (k-1)/(2k-3); the marked
nonincident mass is h_*(r). A-full and A-Y partition all second placements.
The offset domains delete exactly the shared endpoints. All four B
same/cross kind strata, both run channels, and repeated component atoms
remain; collision multiplicity is not collapsed.

## 7. Four-part map and IKBE implication

Proved: explicit triangular domains T_r show exactly added short-boundary
placements, deleted long-boundary placements, common-tuple kernel/gap edits,
and the gamma normalization edit. IKBE-a is DV. Pointwise IKBE-b implies
DE by q_hat subprobability averaging. With M192's accepted Abel identity,
EW, endpoint, and triangle term, these would imply only conditional J=2.

## 8. Diagnostics, objections, and open obligations

Independent clean-room k=3,5 checks pass 649 exact assertions. At k=3 they
retain 4 B and 10 A collision events; at k=5, 60 B and 72 A events. Finite
checks make no universal inference.

Numbered objections:

1. Nonmaterial exposition only: M199 should display the T_r common/add/delete
   domains and say explicitly that the seam edit carries the complementary
   X face. The asserted four-part map is nevertheless exact.
2. Nonmaterial exposition only: IKBE reaches conditional J=2 only jointly
   with M192's accepted inputs, not in logical isolation. M199's context
   already supplies that dependency.

First open step: prove or refute IKBE. No part of IKBE, DV, or DE is promoted.

## 9. Artifacts and action

Artifacts: plan/checkpoint, proof audit, independent checker and JSON output,
summary JSON, report, and freeze files. Python 3.12.3, standard library,
seed null. Action: freeze ACCEPT with the two qualifications and request a
fresh immutable audit; keep every named downstream obligation open.
