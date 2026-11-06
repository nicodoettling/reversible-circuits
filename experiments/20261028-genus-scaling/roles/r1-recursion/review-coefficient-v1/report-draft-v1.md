# Exact nonauthor coefficient review — draft v1

Reviewer: r1-recursion. Scope: coordinator-authored COEFF-EXP.v1 and the generated-coefficient integration. **Nonblind and correlated:** this reviewer authored the downstream marker/decoder theorem, discussed the coefficient construction with the coordinator, and sent an author collaboration cross-check before this formal audit. This report is not a nonauthor audit of the reviewer's own decoder. R2's separate audit is required for that part. No new worker's proof or blind report was used.

Analytical verdict: **ACCEPT COEFF-EXP.v1 in its stated source-dependent mathematical scope, subject to the pending targeted finite check and final hash verification.** No first unproved algorithmic step has been identified. The published ELSV polynomiality and GJV rational structure remain explicit imported theorems. This draft does not certify T0 or replace coordinator reconciliation. It does not assert that the reference Python runtime implements an unrestricted mathematical machine for arbitrarily large inputs.

## Exact versions and inputs

All16 expected hashes in coordinator/coefficient-freeze-v1.json and the R1 author manifest matched at intake. The coefficient proof hash is b152819ed84e460fe1d9248e2d178b7575104232b32551ef7466d518ec5ec610; coefficient code hash is886bcb74ed39b18ff72b8b9ec4ad6f9e79b0fe6f09e406bdc2001a470e86cedc. `intake-hashes-v1.json` also binds the unified theorem and integrated adapter/audit/result. Full audit instructions are retained as input-v1.md. The entire coefficient proof, coefficient implementation/result, integrated adapter/audit/result, and R1 dependency proof were read, with the authorship limitation above.

Primary sources were inspected directly before and during this review activity: GJV revised22Dec2000 Section2.3 equation13, Definition2.2, Theorem3.2 and its multiplicity-indexed proof; GJ torus Section2 and equation2. The exact URL and convention translation are retained in the R1 source verification. A failed PDF screenshot was not misrepresented as visual inspection.

## C1 — normalization and source scope

Accept. GJ identifies the cover coefficient as C_h(alpha)/z_alpha, with z_alpha=(product ai)Aut(alpha). Multiplying the ELSV cover expression by z_alpha cancels its Aut(alpha) divisor and turns product ai^ai/ai! into Q(alpha)=product ai^ai/(ai−1)!. Therefore the ELSV integral is precisely B_h=C_h/(r!Q), not an ordinary bridge count and not a class-aggregated count.

For h>=2 and every positive integer cycle tuple, the stable ELSV polynomial has total degree D=3h−3+k. Expanding the geometric factors gives the coefficient of a1^theta1...ak^thetak as the signed Hodge integral with lambda=3h−3+k−sum theta. Distinct variable labels remain distinct even when theta repeats. The rational generating series divides that coefficient by Aut(theta) exactly once. The allowed theta support follows from0<=lambda<=h and theta_i>=2. Consequently d<=3h−3, each theta_i<=3h−2, and total theta degree<=6h−6. Genus0/1 are handled separately, so no unstable low-genus ELSV instance is silently imported.

The fixed endpoint convention is rightmost-first. A source convention reversal changes endpoint to its inverse, which has the same cycle type and connected factorization count. The explicit DP and decoder use right multiplication by the last transposition, so their literal convention agrees internally. Transitive support equals connected transposition support; no Hurwitz transitivity classification theorem is needed.

## C2 — ordinary and connected finite counts

Accept. If sigma is the fixed endpoint and the last letter is tau, the predecessor endpoint is sigma tau. Conjugation makes the predecessor count constant on its type. Thus summing A(type(sigma tau),ell−1) over actual tau gives the fixed-endpoint count, with no conjugacy-class size factor. The initial condition and sign/distance pruning are valid; n0/n1 and length0 are explicit.

For the connected extraction, every support component is invariant under the endpoint, hence a union of its individual cycles. The component containing the chosen anchor cycle is unique. Its word, the arbitrary complement word, and the positions of its letters in the original word are uniquely determined. Conversely these data reconstruct the literal word. The term U=S has an empty complement and yields the desired C(S,ell); all other terms are disjoint disconnected cases. Empty subsequences and isolated fixed points are essential and present. Intermediate subtraction sums remain bounded by the ordinary total because the underlying cases are disjoint.

The implementation groups anchored subsets with the same child cycle lengths. Its multiplicity is product_a binom(m_a_remaining,c_a), which is exactly the number of actual indexed choices, including repeated cycles. The anchor itself is selected once before grouping. There is no extra factor1/2 and no automorphism quotient of the two children. Its singleton child restriction to length0 is correct. Minimum child and complement lengths only prune impossible summands.

## C3 — simplex completeness and source coefficient extraction

Accept. For d<=3h−3, the positive sample a=1+b with |b|<=D=3h−3+d has total degree n<=d+D<=9h−9 and target length r=n+d−2+2h<=14h−14. The number of lower-simplex points is binom(D+d,d)<=2^(9h). These are all finite count queries on exact labels; there is no connected conditioning oracle.

The tensor products of binomial(b_i,beta_i), |beta|<=D, form a basis of all multivariate polynomials of total degree<=D. Finite differences at the origin recover the basis coefficients. Every gamma<=beta stays in the lower simplex, so all requested finite-difference values were sampled. Conversion by b_i=a_i−1 is explicit. This proves completeness and uniqueness; numerical success is not the reason interpolation is valid.

The implementation computes only the desired monomial coefficients. A term binomial(a_i−1,beta_i) has degree beta_i, so beta_i<theta_i cannot contribute. The loop beta=theta+eta with |eta|<=D−|theta| therefore retains every contributing term, and the simplex routine enumerates all such eta, not merely the top shell. Symmetry permits sorting beta before mixed difference evaluation: the normalized count polynomial is symmetric in its labeled variables and the origin is fixed by coordinate permutations. This saves work without changing multiplicities.

## C4 — uniformity, counting loops and bit complexity

Accept. A fixed h uses only degrees<=9h and lengths<=14h. Ordinary cycle-type tables have at most2^(9h) states up to polynomial factors. For one sample, anchored subset extraction has at most3^d subset pairs, with d<=3h. The number of samples and interpolation terms is2^(O(h)); multiplying finitely many such factors leaves C^h for an absolute constant. Dense interpolation's stated S_d^3 bound is loose but sufficient. The implementation's grouped subprofiles and symmetry do not increase the theoretical bound. Summing over d and over2<=h<=g introduces polynomial factors in g, absorbable into a larger fixed exponential base.

The coefficient proof also pays for rational bit sizes. Let M=9h and L=14h. A normalized count has denominator dividing (L!)^(M+1), since r! divides L! and product ai^ai divides (L!)^sum ai. Converting the Newton basis contributes product beta_i! dividing D! and hence one further L!. Dividing the final coefficient by Aut(theta) contributes a divisor of(3h)! and one more L!. Thus a single denominator (L!)^(M+3) covers all output coefficients. It has O(h²log(h+2)) bits.

Ordinary and connected counts have O(hlog(h+2)) bits. Finite-difference binomials and univariate expansion coefficients have polynomial h bit length, and sums have at most2^(O(h)) terms, adding only O(h) bits beyond a bound on absolute term size. Signed cancellation cannot hide a large unaccounted denominator: all terms share the displayed factorial denominator. Schoolbook rational arithmetic therefore costs polynomial h per operation, and the whole finite coefficient precomputation is A0 C0^(h+1)(h+2)^a0 bit time for absolute constants. This is a uniform algorithm whose loops and finite inputs are derived from h; there is no per-genus advice, unspecified symbolic solver, or Hodge software.

## C5 — integrated binding and downstream interface

Accept the binding, with the explicit implementation scope below. The adapter imports the diagnostic decoder, removes every installed genus>=2 specification, and clears count/branch caches. It then calls the uniform recover(h) routine for every missing h, installs c=K/Aut(theta), and only then invokes the literal decoder. It preserves genus0/1 formulas, builds all lower genera needed by recursive calls, and reuses already generated lists without altering their values. No supplied genus2/3 value survives into the integrated sampling computation.

The coefficient output contract satisfies the R1 frozen interface: both coefficient count and bit length have a fixed exponential bound in g, and preprocessing has the same bound after absorbing polynomial g factors. The marker proof's signed complete-mass convention is therefore compatible with the generated list. This is an interface check, not a fresh nonauthor certification of the reviewer's own marker, posterior, literal-law or exponent15 arguments. Those require R2 review and coordinator reconciliation.

The coefficient reference uses recursive Python functions with memoization, while the mathematical proof specifies finite tables and subset orderings. Standard interpreter recursion and resource limits mean the file is a research reference, not a practical execution guarantee for all g. Both the adapter header and unified theorem state this. The mathematical claim is an existence theorem on exact bit operations and can execute those finite tables bottom-up; this implementation limitation does not introduce an unproved mathematical lemma.

## C6 — retained regressions and exclusions

The connected/ordinary81/80 mismatch remains a mandatory rejection of substituting A for C. The new extraction explicitly subtracts every other support component. Repeated cycles are distinguished before grouping and retain their binomial multiplicity. Zero length on a singleton contributes1; singleton positive length contributes0; identity odd length is sign-forbidden. Equal-child/parallel-cut multiplicities are not forgotten in the binding.

No sampling from a graph, insertion-only decoder or signed term is introduced, so the graph-weight and (ab)^3 counterexamples remain valid against their original methods without refuting this construction. No adaptive marginal product appears: the coefficient stage is deterministic; the downstream stage uses complete conditional integer masses. CP1 remains a live objection to any replacement by marginal lightness. The growing-genus/small-support policy obstruction remains valid, because C^g cost on a prescribed component does not imply polynomial expected cost under every global bridge law. There is no local heat-bath, global all-length, or wire-polynomial conclusion.

## New falsification and final gate

Pending coordinator execution: check-v1.py uses an independent literal permutation/support DP on N5,N6 through identity genus4 lengths, then compares all ordinary/connected endpoint profile counts to the reviewed routines. Separately it reconstructs the complete ELSV polynomial for one/two cycles and genera2/3/4 and evaluates outside the original interpolation simplex. This tests repeated-cycle extraction and the full interpolation degree/shift beyond the author's original N<=4 checks. The polynomial extrapolation still uses reviewed exact count values, so it is an implementation regression, not an independent proof of ELSV.

Final report will retain the exact command, raw results, reservation receipt, before/after hashes and any failure. Finite success does not prove asymptotic complexity. No repair is proposed on the present analytical evidence; all frozen author bytes remain intact.
