# Regression registry

All old negative cases are retained; old files were not edited. Current exact runs use Python3.12.3 standard-library arithmetic. Finite checks test implementations and can falsify inequalities, but do not establish asymptotic estimates.

| ID | Exact issue / expected outcome | Current evidence and disposition |
|---|---|---|
| POLICY-SCOPE | Minimal-only above exponent2/3 and genus<=1-only at m2N do not imply H0 failure | R2-O1 newly bounds the FULL H0 numerator, including every genus on v<=K; old negative reports preserved |
| T0-P0-P1 | Failure of H1 alone is insufficient; failure of H0 is not hardness | Canonical obstruction proves H0 failure, implies H1 failure by containment, leaves T0 existence unresolved |
| FINITE-NOT-ASYMPTOTIC | Nonzero error at finite N does not refute negligible error | AtN28,m12,K4 H0 excludes type(5,12,g2); only the analytic sequence proves non-negligibility |
| FULL-VS-ALLOWED | Literal genus<=1 mass, H0 mass and H1 mass differ | Exact certificates in R3 boundary-results.json label each policy separately |
| FIXED-K | top(42,12) hasK5; residual(5,12) would recomputeK4 | Both frozen H0/H1 retain the original allowed branch in R3 sampler-regression-results.json |
| SUPPORT-HISTORY | Endpoint identity alone does not determine connected completion counts | Old decoder and QC retain exposed support; QC distinguishes((1,1),) from((1,),(1,)) atzero remaining length |
| SQUARE-OMISSION | Adjacent pair insertion misses ((12)(23))^3 | No literal square-insertion sampler is used; counting incidence is not a generation claim |
| GRAPH-BIAS | Uniform support graphs or scalar counts do not give uniform words | Actual forward laws atS3m4,S4m4,S4m6 and newQC S3m8 are exact; decoder maps explicit |
| ZERO-BOUNDARY | m0,m2,odd,N1,N2, near-minimal and zero-count branches | R3 frozen tests, R4 new decoder tests and canonical statements agree; empty targets rejected |
| STACK-LENGTH | Small support may have arbitrary length/genus, including length1400 | Explicit-stack execution succeeds for old sampler andQC |
| CLI-DIGITS | Decimal integer conversion can fail past default4300digits | Oldv4 uses losslesshex; R3 tests5001digit serialization without changing configuration |
| CLI-POLICY | Generic A label once confused H0 andH1 | Frozenv4 predicates and certificates are policy-specific; no wrapper edits |
| FINITE-GENUS | Extending genus to infinity and replacing(k)_q byk^q loses useful length dependence | New finite-binomial identity tested53,300 term cells and7,300 sums/identities; canonical positive proof is analytic |
| EXP-TEST-v1 | First diagnostic usedbinom(N,v), while R2 relaxed exponent usesN^v/v! | Root identified mismatch; oldscript/results retained; v2 checks BOTH with exact rational bounds on150 eligible cases |
| EXP-CONVERGENCE | Infinite all-genus/all-degree series may diverge | Obstruction uses finite degree sum, entire fixed-degree series; final majorizing degree sums are geometric withq<=1/2 |
| CP-1 | Marginal probability bounds cannot be multiplied after selected histories | Not invoked: proofs use exact weighted incidence, positive coefficients or conditional component coupling. No sequential marginal product appears |
| QC-CUTOFF | New cutoffL must remain top-level, distinct fromK | H2 named/versioned; top(100,38) retainsv17 at residual(17,38), despite smaller residualL |
| QC-T0 | More exact small-support states alone need not rescue the full regime | R2 generic-cutoff corollary and root audit show H2-QC error also tends toone on the same sequence |
| CANON-DISPATCH | Initial canonical prose could imply H0 only usesg01 on large components | R5 direct source comparison found actual ALLg<=1 branch; revised proof states exact routing; fresh R4/R5 v2 acceptance closes presentation repair |

Root decisive rerun: coordinator_checks.py / coordinator-checks.json gives55 factorial-majorant cells,80 profile-coefficient comparisons,390 subgroup bounds,197 finite-binomial bounds and512 exact sequence/cutoff checks. The all-j proof uses monotonic inequalities, not extrapolation from those512 instances.

No mathematical claim required a repair after rejection in this run. The exponent diagnostic scope was repaired with a new version and checked by root plus R3. Canonical positive integration added explicit normalization notation/integerJ and then repaired the H0 dispatch description; exact-hash fresh nonauthor review is recorded in the ledger. Prior integration bytes are preserved in proof-integration-v1.md.
