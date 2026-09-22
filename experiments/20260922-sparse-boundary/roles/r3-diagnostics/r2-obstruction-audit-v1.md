# Nonauthor audit of R2-O1

Status: **accept the internal argument under its explicit imported uniform genus-majorant dependency**. This is a same-model nonauthor review, not external human certification or an independent probability of correctness. The coordinator owns final theorem acceptance. Reviewed source hash: `a6716e623768ded49b5ba1a2441abdddc8cb18c61be52d8a96b79387fe68b33f`. The exact source snapshot is `audit-input-r2-v1.md`; imported proof hash is in `audit-input-hashes.json`.

## Claim and verdict scope

For every integer j>=64, N=2^(8j), m=2^(6j), unchanged H0 has retained mass Z_A/Z<=2^(-1-jm/2). Therefore its global total-variation error is at least1-2^(-1-jm/2) on the exact benchmark boundarym^4=N^3. H1 inherits failure becauseB subsetA. This refutesP0 andP1, not existenceT0 and not sampling hardness. The result concerns polynomial time inN,m, and makes no wire-efficient claim.

No internal unproved step or finite counterexample was found. The explicit external mathematical dependency is the all-genus count majorant A_g(v)<=v^(v-3)((v^3-v)/36)^g/g!, from the hash-frozen previous proof. Its algebraic derivation was reread; primary-source DYZ normalization is being audited by the coordinator. Sampler law/error identities are separate hash-frozen imported inputs validated here on finite instances.

## Count and conditioning audit

For multiplicities a_(v,g) of nontrivial component types, let s=sum v*a and k=sum(v-1+g)*a. Choosing unordered disjoint labeled blocks and interleaving their internally ordered words gives exactly

    (N)_s product [A_g(v)/v!]^a / a!

for the count divided bym!. No omitted isolate factorial remains: unused labels contribute the factor(N)_s=N!/(N-s)!. Replacing(N)_s byN^s and dropping s<=N only adds nonnegative terms. Thus the relaxed exponent usesN^v/v!, exactly as inR2-O1. The earlier diagnosticsv1 tested the smallerbinom(N,v) sum; this was a scope mismatch, not a counterexample. Version2 tests both separately and the relaxed one passes.

Everyv<=K component admits everyg>=0 in the exponent; largev keepsg0 andg1. Hence the proof is genuinely aboutH0, not the already refuted genus<=1-only candidate. K is fixed once at the top input.

No conditional marginal probabilities are multiplied. The totalZ normalizes the literal endpoint-conditioned word law. The denominator lower bound embeds one fixedr-label subgroup. It does not multiply by the number of possible subgroups, which would double count words with smaller support.

For the uniform transposition walk onS_r, symmetry givesPr(return at2k)=sum_sigma p_k(sigma)^2. Sincep_k lives on one parity class, Cauchy-Schwarz yields>=2/r!, includingr2. ThusZ>=2*binom(r,2)^m/r! is valid at every positive evenm.

## Numerator arithmetic

Atx=k/N² andq=3Nx, the imported majorant gives the small-support genus sum<=exp(b_Kx), and the large-support sum<=1+b_vx. Bounding their union byexp(b_Kx)+b_vx preserves all allowed terms. Underb_Kx<=1, exp(b_Kx)<3.

The factorial boundv!>(v/3)^v yields

    S0 <=3N sum_(v>=2) q^(v-1)/v³ <=9k/[8(1-q)],
    S1 <=sum_(v>=2) q^v(1-1/v²)/36 <=kx/[4(1-q)].

Withq<=1/2 andx<=1,3S0+S1<=27k/4+k/2=29k/4<8k. These constants were rederived; all powers ofN,x and thev³ normalization agree. Coefficient positivity then givesZ_A<=m!x^-k exp(8k). One may truncate component costs at k throughout the coefficient argument; terms of greater cost cannot affect its coefficient. This avoids any need to evaluate a divergent unrestricted all-genus generating function.

## Explicit sequence and constants

OnN=2^(8j),m=2^(6j),k=m/2, x=2^(-10j-1),q=3*2^(-2j-1)<=3/8. The elementary P<=2N andK>=2 implyK<=16j+2. The boundb_Kx<=(16j+2)^3/[72*2^(10j)] is<1 atj1 and decreases, because its consecutive numerator ratio is<8 while the denominator ratio is1024.

Forr=floor(m/(6j)),m/(6j)>=2 givesr>=m/(12j)>=2 andr<=N. Thenbinom(r,2)>=r²/4>=m²/(576j²), andr!<=m^r<=2^m. ThereforeZ>=2[m²/(1152j²)]^m.

The numerator becomesZ_A<=[sqrt(2)exp(4)N sqrt(m)]^m. Dividing and usingN/m^(3/2)=2^(-j) gives half the mth power of1152sqrt(2)exp(4)j²2^(-j). Its constant is below1152*2*81=186624<2^18. Forj>=64,2^18j²<=2^(j/2), verified at64 and maintained because((j+1)/j)^4<2. The claimed retained-mass bound follows. No asymptotic rounding of m_*(N) is used: this m is exactly the integer boundary.

## Falsification evidence and limitations

- 53,300 exact R1 per-component bound cells;7,300size sums and finite-binomial identities passed. These support implementation/algebra, not the universal proof.
- 150 R2 cases throughm64 andN10^6 passed exact relaxedS_m<=8k and the stronger RHS comparison using a20-term Taylor LOWER bound forexp(b_Kx). `allowed-exponent-results-v2.json` preserves the domain and exact rationals.
- Pilot passed91 total/connected/active count cells and23weighted-support cases. Known totals27,120,3936 were recovered. H0/H1 exact omitted classes differ as required.
- FixedtopK paths, arbitrary-genus small support, empty/odd targets and support history passed; large-integer hex serialization passed. No source/sampler changes were made.
- The minimum nonzero finite H0 omission at the selected boundary is not the obstruction theorem; the latter comes only from the count proof above.
- N1positive/odd targets are empty;m0,m2,N2 are harmless exact exceptions. Near-minimalg0/g1 branches are retained in the numerator.
- CP1 cached-prefix regression is inapplicable here because no sequential marginal-product assertion occurs. The exact conditioning normalizer is kept throughout.

A later edit to the reviewed proof reopens this audit; no verdict is inherited by a new hash.
