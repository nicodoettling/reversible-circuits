# I2 exact-version theory review v1

Frozen 2026-10-28. Reviewer `/root/i2_theory_review`, a nonauthor of the frozen I2 arguments. This is **NONBLIND**: the worker inherited coordinator conversation and the assignment explicitly supplied candidate proofs, prior findings and the coefficient repair. It is a same-model Astra/ultra review, correlated with the other agents. Requested/inherited service tier is default; no separate server-returned worker tier observation was available. The project sampler and mathematical-proof-audit skills, including both audit/probability references, were applied.

**Review verdict:** ACCEPT the exact analytic argument of R1 proof-v1 for the moment bounds and its implications on both separately frozen sparse ranges; ACCEPT R3 A3-v2 as a correctly repaired conditional-cost implication; REJECT and retain the original A3-v1 coefficient assertion; ACCEPT the proof of EC-OBSTR.v1 at its envelope-only scope. The complete sampler theorem remains conditional here on the actual exact-law and cost interfaces in R2, assigned to a separate implementation review. No code execution, asymptotic theorem certification, central status change or mission completion is implied by this report. GLOBAL-T0 remains OPEN. The coordinator must reconcile all current reviews and reproduction evidence before accepting the composed theorem.

## 1. Frozen statements and exact inputs

The probability space is the full uniform law U_(N,m) on ordered length-m transposition words on canonical labels [N] with identity product, N>=2 and even m>=0. Products act rightmost first. Outputs list all factors. Independent fair bits supply randomness. Put P=N+m+2.

R1's claimed algorithm is one unrestricted exact macro sampler followed by on-demand connected quotient decoding. Its output law is claimed exact on every even input, with one expected O(P^14) bit bound on each of two separately preserved regimes:

* ES.v1: m^3<=N^2.
* ES-LOG.v1: m<=N^(2/3) ln(N)/4.

No polynomial worst-case time or space claim is made. The fixed algorithm tests neither inequality and drops no component. Its exact law, when established, supplies TV0 for every b without a b-dependent choice. Degree N, explicit m and the number log2(N) of wires must not be conflated.

The source-integrity-v1.json receipt checks 36 entries against the supplied R1/R3 manifests; every checked hash matches. Key exact files:

| Input | SHA256 |
| --- | --- |
| R1 statement-v1.md | 24ddaa1f86f9b52fc3e848502a96df8c46488313adcfabc179c4b670836e64a9 |
| R1 proof-v1.md | 06c0537531169afd10e47d9df15c2344619b1b57ec1e0c9c23e91a0ed2dec2e5 |
| R2 statement-v1.md | a2f6951296cc2f10930b660194366710eb6cdd0a39f1e418d5a300b0b78d119b |
| R2 proof-v1.md | 5ee643ed2c795ec569c40bd0ff514131ecd4e58cd1ed952f9ec1763eba3d2598 |
| R2 exact_sampler-v1.py (interface provenance; no source audit claimed here) | 93d38c75d25446dc7287cd65ea0ec4f05c5f3855fe96b3ee26fe6a9444bb33a0 |
| R3 falsification-proof-v1.md, rejected coefficient retained | d435b7c6a4127909310be7c543a281fbc8c027f9fa5443ae1aa9147d41bc9874 |
| R3 falsification-proof-v2.md, reviewed repair | ee8b1cc8e9c53159dcd4c190fc0cef4ddd9eb9947819a29f719e40ec251e5199 |
| R3 correction-v2.md | ffbd57b34703dfe279761fe240f359752201f873a370c19a22433fdcfb3a1c1f |
| R3 scope-obstruction-v1.md | 830d9849857d5f567556dc453e3ccebdf1628366fda23d82d01d5d479b048732 |
| SG canonical proof.md | f788eaecebefd53373c56a7c0c41d104c34897c4a6aba6c775f5f1ce80ec8da2 |
| SB canonical proof.md | 3a54f12e4d172cfdfc5ef6f8e7b84c067e86eba8d10a2f387496ff7bd435d611 |
| I1 R3 mass proof-v1.md | cdfcc097d50a8ed070c27fcc5b8ae700e0472769578f7ccd6ab7e5ac85178aef |

All R1/R3 listed arguments and reports and the R2 statement/proof were read in full. The SG/SB canonical proofs and closed claim ledgers, SG source_checks.md, R1 resource-conditioning clarification, current I2 recovery/claims/tasks, current cap, and the operator policy2 note were read. The DYZ primary-source verification is inherited from the exact local source checks; this reviewer did not newly open the primary PDF. That provenance is an explicit imported theorem dependency, not a new external source audit or a claim of independent mathematical origin.

## 2. Exact normalization, feasibility and fresh pairs

For a connected component of degree v>=2, identity requires equal numbers of permutation-cycle joins and splits. Connecting its support requires at least v-1 joins. Thus its length is 2q=2v-2+2g, g>=0; repeated equal pairs along a spanning tree, followed by extra equal pairs, realize every such length. An isolate is only (v,ell)=(1,0).

Let C(v,2q) be the literal connected count, A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!, S(n,k)=Z(n,2k)/(2k)!, and m=2k. A macro of disjoint labeled components and genera has normalized weight product A_g(v). Once internal words are selected, the interleaving factor (2k)!/product(2q)! is exactly the missing position multiplicity. There is no equal-size symmetry mistake because the blocks are actual disjoint label sets and every literal word has a unique component decomposition.

Marking an actual component of size v and cost q gives

    E X_(v,q) = binom(N,v) binom(2k,2q) C(v,2q) Z(N-v,2k-2q)/Z(N,2k)
              = binom(N,v) A_(q-v+1)(v) S(N-v,k-q)/S(N,k).

Every component supplies one mark, including equal-sized components. The denominator is the complete bridge count. This identity is not an unconditioned graph estimate.

For 2k<=N put D=N-2k+1. Embed a base macro on the complement of the specified removed v-set as a macro on all N labels, with those v labels isolated. Cost k-q uses at most 2(k-q) labels, so at least I=N-2k+2q labels remain isolated. There are (I)_(2q)/(2^q q!) ways to add q unordered disjoint pairs, and each added length-two component has normalized weight 1/2. Therefore weighted extensions per base weight are at least D^(2q)/(4^q q!). Conversely, deleting a chosen q-subset of the at most k minimal pairs recovers at most binom(k,q) bases; demanding that the removed v-set become isolated only reduces this multiplicity. The same final weight is counted on both sides. Hence

    S(N-v,k-q)/S(N,k) <= 4^q q! binom(k,q)/D^(2q)
                       = 4^q (k)_q/D^(2q).

This is valid for q0 with empty products; zero residual counts contribute zero. Adding pairs may use some of the originally removed labels, which is allowed; the reverse condition enforces precisely the intended preimage. No independence of components or support edges has entered.

## 3. All-genus majorant and both inherited tails

The accepted DYZ normalization is C(v,ell)=v! ell! h_(g,v), with the recurrence recorded in SG Section2 and the source receipt. After division by v^(v-3)t^(2v-2), the recurrence expresses H_v as a convex combination of L(at)H_aH_b, a+b=v, where L(z)=2(cosh(z)-1)/z^2. The coefficient of z^(2j) is 2/(2j+2)!, bounded by 1/(12^j j!): equality holds for j0,1 and the consecutive ratio is 12(j+1)/[(2j+4)(2j+3)]<=1. With b_v=(v^3-v)/36,

    b_v-b_a-b_b=abv/12>=a^2/12.

Thus each inductive summand is coefficientwise at most exp(b_v t^2), and positivity yields A_g(v)<=v^(v-3)b_v^g/g! for every v>=2,g>=0. This argument includes degree1 convention b1=0 and does not use convergence of an infinite-degree generating series or probability independence.

Combining marking and fresh-pair bounds and putting x=4k/D^2 gives

    E X_v <= binom(N,v) v^(v-3) x^(v-1) exp(b_v x).

Feasibility v<=k+1 implies b_v x=v(v^2-1)k/(9D^2)<=v k^2(k+2)/(9D^2)=vz. Since v!>=(v/e)^v, this yields

    E X_v <= N c rho^(v-1)/v^3, c=exp(1+z), rho=cNx.

The stronger finite genus calculation retains (k)_q. With h=k-v+1>=0,

    sum_(g=0..h) (k)_(v-1+g)(4/D^2)^(v-1+g)b_v^g/g!
      = (k)_(v-1)(4/D^2)^(v-1)(1+4b_v/D^2)^h.

This is an exact finite binomial expansion of the majorized genus sum, not an approximation of the normalization. Writing s=v/(9D^2)^(1/3), the remaining factor is bounded by exp(3ks)=exp(z_new v) because 4b_v/D^2<=s^3, 1+s^3<=(1+s)^3, and ln(1+s)<=s. Thus the same marked tail holds with c_new=exp(1+z_new), rho_new=c_new Nx, z_new=3k/(9D^2)^(1/3). The two tails have the same full bridge law, and their only finite-input prerequisite used here is 2k<=N (with m0 separate).

## 4. Exponential cost moment and the two ranges

For fixed a>=2, define W_a=sum_(nontrivial B) a^|B|=sum_(v>=2) a^v X_v. Finite-sum linearity under U gives, when a rho<1,

    E W_a <= Nc sum_(v>=2) a^v rho^(v-1)/v^3
          <= Nc a^2 rho/[8(1-a rho)].

The extension to an infinite positive series is valid, and v^-3<=1/8 for every nontrivial v. If a rho<=1/2, the result is at most aNc/8. No union bound is being substituted for an expectation and no component-stage probabilities are multiplied. At m0, W_a=0. For every N,m, deterministically W_a<=N a^N; it needs no sparse assumption.

For ES, N>=64 and m^3<=N^2 imply m<=N/4, D>=3N/4. Let u=N^(2/3)>=16. Then k<=u/2 and k+2<=5u/8, giving

    z <= [(u^2/4)(5u/8)]/[9(3N/4)^2] =5/162<1/16.

Using e<11/4 and exp(1/16)<=16/15 gives c<44/15<3. Therefore rho<(32/3)N^(-1/3). At N>=(32a)^3, a rho<1/3 and the moment is <3aN/16. For a9 the sufficient threshold is 288^3; all inequalities are strict in the indicated directions even at that endpoint.

For ES-LOG, take M=2^2048, N>=M and L=ln N>1000. The function exp(L/3)/L is increasing there and L<=exp(L/3), so the stated length bound implies m<=N/4 and D>=3N/4. Direct substitution yields z_new<=m/N^(2/3)<=L/4 and Nx<=4m/N<=L exp(-L/3). Thus c_new<=eN^(1/4), while

    ln rho_new <=1+ln L-L/12 <=-L/24.

The last inequality follows from 1+ln L<=L/24 at L1000 and its increasing margin thereafter. Hence rho_new<=N^(-1/24), and 9rho_new<=9*2^(-2048/24)<1/2. Consequently

    E W9 <= (9e/8)N^(5/4)<(27/8)N^(5/4)<4N^2.

The two ranges are distinct at finite N and have not been equated. No rare high-genus component is omitted. For N<M the deterministic W9<=N9^N<=N9^M suffices at every length. Therefore K=1+9^M supplies E W9<=KN^2 throughout the union. K is one finite proof constant, independent of all inputs. The algorithm neither computes K nor branches at M, so the enormous constant is not a hidden lookup table or a nonuniform algorithm. It destroys any practical interpretation of the displayed numerical constant, not the quantified polynomial assertion.

## 5. Correct conditional resource composition and repair cone

R2's needed interfaces are: unconditional E T_pre<=A P^12 for scalar preparation and complete macro generation, and for every positive-probability complete macro M,

    E[T_dec|M]<=A P^12(1+W9(M)).

The latter includes deterministic table construction, all actual bit operations and fresh decoder randomness; additive1 covers isolates/output overhead. Under those exact interfaces,

    E T <=A P^12(2+E W9)<=A(2+K)P^14.

This is the coefficient R1 actually charges. The claimed P14 exponent follows from P12 and N^2<=P^2; it is conditional on the independently audited R2 cost proof, not on a quotient-state count alone.

I freshly checked the R3 repair rather than inheriting a prior conclusion. If E T_pre<=K0P^s and E[T_dec|M]<=K1P^s(1+H(M)), then

    E T <=P^s[K0+K1(1+EH)] <=(K0+K1)P^s(1+EH).

The second inequality has exactly the nonnegative slack K0 EH. Original A3-v1 omitted the separate K0 cost when both were written as K; it is false as an exact coefficient assertion. A targeted finite boundary witness is the unique m0 macro H0 with deterministic preparation and remainder costs each P^s, K0=K1=1. The original bound is P^s and the allowed total is 2P^s; v2 is exact. This test concerns the changed premise/conclusion, not an unrelated rerun of sampler counts.

A second hand check uses the actual U_(4,4) macro law below, for which EH=12231/20. With K0=K1=1 and both cost interfaces saturated, E T/P^s=2+12231/20=12271/20. The rejected v1 expression is 12251/20, short by1. The corrected precise v2 expression is 12271/20 and its coarser coefficient expression is 24502/20. This confirms the repair with nonzero, nonconstant H as well as isolates. General nonnegative H is already covered by the exact algebra, so no numerical grid can replace that proof.

Changed dependency cone: A3-v2 -> conditional cost paid by moment -> ES/ES-LOG expected-runtime consequence. The moment identities, finite-degree bounds and EC proof do not depend on the rejected coefficient. R1's final split independently retains both costs. Its earlier stronger request to condition all macro-generation cost on the completed rare macro is unnecessary and remains preserved as an earlier draft; it is not used by final proof-v1. I find no missing cost in the corrected analytic composition. Actual P12 implementation accounting remains the separately assigned premise.

## 6. Fair-bit filtration and resource interpretation

At each logical uniform integer draw, the bound Z is determined by the already exposed history. If Z1 no bits are needed; otherwise r=ceil(log2 Z) gives conditional success probability Z/2^r>1/2 and expected fewer than two trials. The type of the chosen component, selected labels and positions may be adaptive, but the pointwise conditional cost bound holds on every actual positive-mass history. A polynomial bound on the number of calls and their bit lengths gives the unconditional macro-generation expectation by summing conditional expectations. There is no need to condition its running time on the final macro.

The end of macro generation is an almost-surely finite stopping time for the fair-bit tape: each finite stopping prefix is determined by its consumed bits. Conditioned on any such prefix, the unused suffix is fresh independent fair bits. Summing these cylinder statements over prefixes compatible with a fixed macro preserves the fresh-tail law conditional on that macro. Subsequent decoded components may be included in the history; the same argument applies to the next integer call. R2's fresh per-component counter and no unseen random cache are consistent with this interface. A test-only exact_index hook is not a production source of free arbitrary random integers.

A finite number of finite tables plus almost-surely terminating rejection draws proves almost-sure termination. Expected polynomial time does not imply worst-case polynomial time or space. W9 is an upper envelope for the work of selected components; exponential work on rare large components is allowed. No large table for an unselected component can be charged to this macro expectation. Even a shared-table implementation would need a separate cross-term bound; it is not the specified fresh-counter design. A finite expected space bound could follow from an explicit space envelope, but it cannot become a worst-case guarantee.

## 7. EC-OBSTR.v1 at the new cutoff

This is a separate negative statement about W9, not the sampler's actual runtime. Set integer j>=64, N=2^(8j), m=2^(6j), k=m/2, J=2^(3j), epsilon=2^(-1-jm/2). The imported I1 Section2 lemma is genuinely an arbitrary-J finite lemma, not merely its subsequently specialized logarithmic-cutoff theorem. It states that the event all components satisfy g<=G OR v<=J has count

    Z_(G,J) <=m!(N^2/k)^k exp(8k)

whenever 1<=J<=N, x=k/N^2, q=3Nx<=1/2, b_Jx<=1 and 6G^3x<=1/16. The proof majorizes its entire permitted component series, replaces falling label factors by powers, and bounds a positive exponential generating function. For G0 its positive-genus sum is empty, so no positive-G endpoint problem arises.

At the newly declared J with G0,

    x=2^(-10j-1), q=3*2^(-2j-1)<=3/8,
    b_Jx <=2^(-j)/72<1, 6G^3x=0.

All finite hypotheses hold directly. Every word with largest nontrivial component at most J belongs to the enlarged genus0-or-size<=J event. This is the correct direction of containment. It is not inferred from a smaller cutoff's rejected policy.

The same I1 proof's denominator is independent of J. For r=floor(m/(6j)), midpoint symmetry and Cauchy-Schwarz on its parity class give Z(N,m)>=2*binom(r,2)^m/r!. Since r>=m/(12j), binom(r,2)>=r^2/4 and r!<=m^(m/(6j))=2^m,

    Z(N,m)>=2[m^2/(1152j^2)]^m.

Combining with m!<=m^m yields the event ratio at most (1/2)[1152 sqrt(2) exp(4) j^2 2^(-j)]^m. Its constant is below2^18, and 2^18 j^2<=2^(j/2) for j>=64: the base case has2^30<=2^32 and the right/left ratio increases thereafter. Thus P(Vmax<=J)<=epsilon at the new J.

On its complement integer Vmax>=J+1, so W9>=9^(J+1). Averaging gives

    E W9>=9^(J+1)(1-epsilon).

Since P=N+m+2<=2N and epsilon<1/2, for any fixed C,d>0 the ratio of this expectation to C P^d is at least 9^(2^(3j)+1)/(2C*2^((8j+1)d)), tending to infinity. It refutes a polynomial expectation bound for this exponential envelope at the3/4 sequence. An upper bound on work cannot yield a work lower bound from its own large expectation; no optimized runtime impossibility or global sampling impossibility follows. The sequence eventually lies outside both positive sparse ranges, so there is no inconsistency.

## 8. Boundaries, probability counterexamples and existing computation

At m0 the word is empty, W9=0 and isolate scanning remains charged. Odd m has no identity target and must reject. At m2 every word repeats one uniformly chosen edge and W9=81. For N2 at any positive even length the only word repeats its sole edge, again W9=81, independently of genus. Singleton positive-length components are impossible; zero-count branches never normalize. At v=k+1 only genus0 is feasible. The finite genus sum has h0 and correctly retains just that term.

The actual U_(4,4) counts provide a useful hand-check of both marking and invalid stage multiplication. There are96 words with one connected size3 component (four label triples,24 connected minimal words each),6 words with one size2 component at length4, and18 words with two disjoint size2 components (three perfect matchings, six interleavings each). They total120. Thus W9 has masses4/5 at729,1/20 at81 and3/20 at162, giving EH=12231/20. Let E1 be that the first nontrivial component in least-label order has size2, and E2 that a second such component exists. Then P(E1)=1/5, P(E2)=3/20 and P(E1 intersection E2)=3/20>3/100. The conditional second probability is3/4. These are exact bridge-law facts, not independence assumptions.

CP-1 is also retained: after the designated conditioning, each A_b has mass21/2000, each C_b has mass1/20 and D has879/1000; p(x)=1/10, p(e_b)=121/2000 and p(f_b)=21/2000. The matching two-hit probability is21/2000>1/100 while the later residual incidence is21/221<1/10. That rejects marginal-product reasoning after support restriction and renormalization. The current proof avoids this implication by exact marked counts, full-macro conditioning and additive expectations; it does not claim independent component sizes.

The square-insertion zero fibers including (ab)^3, unweighted-graph bias, exposed-support81-versus80, marked-cut parallel-core multiplicities, H0/H1/H2 policy obstructions and fixed-cutoff42/12->5/12 witness remain valid against their original mechanisms. This new algorithm's analytic proof has no insertion or cut grammar, retains all component types and uses the full bridge normalizer. Exactness still depends on its decoder preserving the exposed support; that is an implementation obligation, not something the moment proof establishes by itself.

Existing finite evidence was read, not rerun: R3 moment-results-v1.json (SHA25616c3f60f31f32483dcb12cfe8ff52033d134cb6870db5b28b8d7b0fe9a252a16) reports52 literal cells,404 marked-moment cells,238 finite-binomial cells and44 rational certificates. Its positive rare genus2 contributions at N82,m14 and N128,m16 are preserved as nonzero exact rationals. These checks support normalization and do not establish asymptotics.

During this review the coordinator completed fresh current-attempt I2-J3 with exit0. The complete production-audit-attempt000003-v1.json (SHA256515dc16e3789bc6c9f82d8ef1179cc083b5ff1603970ddc2326e0413c8d09ebd) was read. It reports full categorical laws on S3m4,S4m4,S4m6,S3m8 with27,120,3936,2187 words, each equal probability; the selected v6,ell14,g2 example creates no counter before macro completion and releases its276-key counter. This is useful finite production evidence, with proof/code audit still separate. The old I2-J2 did not launch and is not retroactively relabeled a successful run.

## 9. Claim-by-claim disposition and remaining obligations

| Claim or implication | This exact review | Dependencies and remaining scope |
| --- | --- | --- |
| Marked-component identity and fresh-pair normalization | ACCEPT exact argument | Full bridge count, weighted incidence; all multiplicities checked |
| DYZ-derived all-genus majorant and finite binomial bound | ACCEPT downstream argument | Inherited checked DYZ normalization; no new primary-PDF audit |
| EM and deterministic finite-degree bound | ACCEPT exact argument | Nonnegative finite-sum linearity, geometric series, no independence |
| ES and ES-LOG uniform moment bounds | ACCEPT exact argument separately | Explicit finite thresholds and one proof constant; no algorithm threshold test |
| R3 A3-v1 coefficient with separately charged preparation | REJECT, retain | Empty-macro and actual nonconstant-macro witnesses above |
| R3 A3-v2 and changed expected-cost dependency cone | ACCEPT exact repaired implication | Separate K0/K1, actual conditional decoder envelope remains a premise |
| R1 expected O(P14) consequence | ACCEPT conditional argument | R2 exact law plus actual P12 bit-cost interfaces, independently reviewed elsewhere |
| EC-OBSTR.v1 | ACCEPT exact envelope argument | Arbitrary-J I1 finite lemma plus direct hypotheses and subgroup denominator |
| Actual optimized decoder expected cost at3/4 | UNRESOLVED | Large upper-envelope expectation is not a lower bound on work |
| Full all-length polynomial sampler mission | OPEN | Neither sparse result nor EC limitation closes it |

I found no mathematical repair needed in these frozen analytic arguments beyond the already supplied A3-v2 correction, now freshly checked. I did not audit the production source line by line, measure its operation complexity or claim an independent execution of its tests. Full sampler acceptance still requires the current nonauthor implementation review, fresh blind report, coordinator reconciliation and any affected clean reproduction gates. That remaining integration is explicit rather than an unproved analytic lemma concealed in ES/ES-LOG.

## 10. Operational and artifact record

The review read the current attempt000003 cap: wrap18:28:42.273052UTC, hard18:38:42.273052UTC; the assigned review ends14:45UTC with report due14:00UTC. Current helper v0.4.0 and sealed attempt000003 remain the only permitted computation path. The operator policy2 note resolves the specifically named old admission typo; no new safeguard is waived. No mathematical job was launched by this role. Hand derivations and metadata/hash verification are distinguished from experiments.

Only roles/r5-theory-review was written, using complete temporary files and atomic renames. Full input, plan, halfway checkpoint, source-integrity receipt, this immutable report and its manifest are retained. No author, central, source, protected or other-role file was edited; no stage/commit, descendant, separate CLI session, package install, model/tier or permission change occurred. Shared worktree changes remain coordinator-owned and were preserved.
