# R2 claim ledger

claim | status | assumptions | evidence/artifact | independent check | action
---|---|---|---|---|---
Subgroup denominator(L) | proved | positive even m,2<=r<=N | obstruction-v1.md; September5 report |4960 finite exact checks; root read | reuse
Finite numerator(U) | proved by author, provisional | q<=1/2,x<=1,b_Kx<=1; factorial genus majorant | obstruction-v1.md |root complete read; R3 exact150-cell checks | formal R1 audit
R2-O1 | proved by author, provisional | imported factorial genus majorant; exact H0 | obstruction-v1.md |root read; author exact parameters | nonauthor audit
P0 false | conditional on acceptance R2-O1 | unchanged H0 | explicit m_star subsequence |pending R1 | promote if accepted
P1 false | conditional on acceptance R2-O1 | B subset A | set inclusion |elementary | keep separate
T0 existence | unresolved | permits other algorithms |sampler-specific obstruction does not apply |scope check | preserve unresolved

## Update 2026-09-22 09:44 UTC

claim | status | assumptions | evidence/artifact | independent check | action
---|---|---|---|---|---
R2-O1 current hash a6716e... | proved; internal nonauthor audits accept | explicit majorant, source checked by root | obstruction-v1.md |R1 obstruction_audit.md; R3 r2-obstruction-audit-v1.md | coordinator reconciliation
P0,P1 | refuted by internally audited R2-O1 | unchanged policies | exact benchmark subsequence |R1,R3 | retain distinct T0 scope
UPPER.v2 current hash b76f706... | accepted mathematical audit | imported exact count/marking, decoder dependencies separate | r1-audit.md |3850 genus/rising,1045 binomial,409 boundary checks | report root
R2-O2.v1 H2 corollary | proved; R4 nonauthor audit accepts | R2-O1 finite lemma, H2 exact policy | corollary-h2-v1.md |R4 h2-obstruction-audit.md; exact parameters | coordinator reconciliation
