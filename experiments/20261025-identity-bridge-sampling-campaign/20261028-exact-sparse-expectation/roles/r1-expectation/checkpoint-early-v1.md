# Early checkpoint, 2026-10-28 11:59 UTC

Read canonical SG-T1.v1 proof Sections1-10, claim_ledger.md, source_checks.md, QC.v1 proof, and the exact construction/algorithm audits. The component tail is already normalized under the uniform bridge law.

Provisional analytic finding: for m=2k>0, 2k<=N, and the canonical D,x,z,c,rho, every fixed a>=2 with a*rho<1 satisfies

E_U sum_{nontrivial components B} a^{|B|} <= N*c*a^2*rho/[8(1-a*rho)].

This follows by linearity from E X_v<=N*c*rho^(v-1)/v^3, summing v>=2 and using v^-3<=1/8. No component independence or adaptive product estimate is used. For m^3<=N^2, rho=O(N^-1/3) and c is bounded above by an absolute constant for N>=64. Hence any fixed decoder exponential base can be absorbed in expected cost for all sufficiently large N. For finitely many smaller N, the same unrestricted decoder has a finite explicit worst-case exponential factor, giving one global polynomial with a possibly huge absolute multiplicative constant.

Outstanding: R2 actual bit-cost exponent/base; derive and freeze explicit constants and complete conditioning/resource proof. No mathematical computation has run.
