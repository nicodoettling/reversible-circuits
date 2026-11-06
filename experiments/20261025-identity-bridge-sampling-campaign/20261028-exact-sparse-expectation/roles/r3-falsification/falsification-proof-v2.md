# I2 R3 analytical falsification and scope results — v2

Frozen repaired author argument,2026-10-28. Status: A3 and its conditional sparse descendants are REPAIRED-PENDING-RECHECK after the explicit preparation-cost correction in correction-v2.md. Other supporting lemmas and EC-OBSTR.v1 retain author-proved/provisional status pending fresh scope-matched review. Original v1 remains unchanged. This role does not certify the production sampler or its final polynomial exponent. All probabilities below concern the full uniform ordered length-m transposition identity law U_(N,m), canonical labels, rightmost-first maps. There is no Markov kernel.

## A. Exact moment and valid conditioning

For a>=1 let

    H_a(w)=sum_(B nontrivial support component of w) a^|B|,
    X_v(w)=number of such components of size v.

The exact identity H_a=sum_(v>=2) a^v X_v gives

    E_U H_a=sum_(v>=2) a^v E_U X_v.                 (A1)

This is linearity of expectation under one fixed global law; it requires no independence among components, no sequential event products and no tail conditioning. The canonical marked-count formula is

    E X_(v,q)=binom(N,v) A_(q-v+1)(v) S(N-v,k-q)/S(N,k),
    m=2k, S(n,t)=Z(n,2t)/(2t)!.

Its normalization is the actual full identity-bridge count. Scalar counts plus this identity do not independently supply a literal decoder.

Suppose an actual algorithm samples the entire labeled component/position macro M exactly from its full bridge marginal. Suppose, uniformly on every positive-probability macro, its conditional expected remaining bit cost is at most

    K P^s [1+sum_(B in M,|B|>=2) 9^|B|],   P=N+m+2,              (A2)

where the coefficient K in(A2) is now named K1, and s,K1 are absolute constants independent of M,N,m,b. Suppose the entire count/macro preparation, including fair-bit macro draws, has unconditional expected cost at most K0 P^s, with another absolute K0>=0. If that cost was already included in(A2), take K0=0. Then total expectation, conditioning first on the whole macro for the remaining work, gives

    E work <=P^s [K0+K1(1+E_U H_9)]
           <=(K0+K1)P^s [1+E_U H_9].             (A3-v2)

In later references to(A3), use this corrected(A3-v2). The original v1 displayed the coefficient K without enlarging it when preparation was charged separately; that exact coefficient assertion is rejected. The revised global coefficient is K0+K1, and no exponent or regime changes.

Thus a uniform bound for(A1) pays the actual work, if(A2) has genuinely been proved. No product of unconditional per-stage estimates can replace(A2). Exact fair-bit integer generation generally has no finite worst-case time, so(A2) is a conditional expectation even if deterministic table construction is bounded separately. Independent fresh fair-bit suffixes after each macro choice justify the stated conditional draws; no externally observable hidden cache state is needed.

A shared table does not automatically invalidate base9: if Q_i is the table inventory for component i, a bound proportional to(sum_i Q_i)^2 is at most N sum_i Q_i^2. That extra N is polynomial. However, building tables for unselected components cannot be charged to(A1). The proposed production design samples the complete macro first and discards a fresh local quotient counter after each selected component; the inspected pre-freeze code follows this design. Its final exact-version implementation/cost audit remains separate.

## B. Finite exponential-moment lemma

Assume for feasible v>=2 that

    E X_v <=N c rho^(v-1)/v^3,

where c>0,rho>=0 are deterministic functions of the original input. If a*rho<1, then

    E H_a <=N c a sum_(v>=2)(a*rho)^(v-1)/v^3
          <=N c a^2 rho/[8(1-a*rho)].             (B1)

The second step uses v^3>=8; extending the finite support sum only increases it. If a*rho<=1/2,

    E H_a <=N c a/8.                              (B2)

The m0 case is H_a=0 and is handled without dividing by a positive-length bridge count. There is no maximum-event probability substituted for an expectation: the inherited input bounds each E X_v directly.

A rational sufficient certificate for the old canonical tail is available. Put D=N-m+1, k=m/2, x=4k/D^2, z=k^2(k+2)/(9D^2), with2k<=N and k>=1. The old theorem supplies c=exp(1+z),rho=cNx. If z<=1, then e<3 gives c<9; use cbar9 and rhobar9Nx in(B1)/(B2). Alternatively, if z<=1/16, then c<3: e<11/4 and exp(1/16)<=1/(1-1/16)=16/15 imply exp(17/16)<44/15<3. For completeness e<11/4 follows by summing through1/3! and bounding the tail from1/4! by(1/24)/(1-1/5)=5/96, giving e<8/3+5/96=87/32<11/4. Therefore cbar3,rhobar3Nx is also a rigorous rational certificate. Its denominator1-a*rhobar must remain explicit when only a*rhobar<1 is assumed.

The exact finite checks implement both conservative certificates with their stated sufficient conditions. They do not claim failure of the moment when a sufficient condition fails.

## C. Sparse regimes and finite exceptions: no obstruction found

ES.v1 and ES-LOG.v1 are distinct targets, particularly at small degrees. This argument does not silently identify their ranges. Conditional on(A2), the inherited bounds suffice for both with one fixed constant threshold, for example N0=2^2048.

For ES.v1 (even m with m^3<=N^2), the canonical SG-T1 proof gives c<8 and rho<=64N^(-1/3) for sufficiently large N, in particular every N>=N0. Then9rho<=576N^(-1/3)<1/2, and(B2) gives

    E H_9 <=9N.

For ES-LOG.v1 (even m<=N^(2/3)ln(N)/4), the canonical SB-T1 proof gives c_new<=eN^(1/4),rho_new<=N^(-1/24) for N>=N0. Since N0>=2^2016,9rho_new<=9*2^(-84)<1/2. Consequently

    E H_9 <=(9e/8)N^(5/4) <(27/8)N^(5/4).

These inputs already bound exact component expectations and are inherited, not claimed as new tail theorems. They include all genera. There is no cutoff-defined loss of bridge mass.

For every finite N<N0 and every even m, on each word

    H_9(w) <=N*9^N <=N*9^N0.                     (C1)

Indeed there are at most N nontrivial components, all with size at most N. This deliberately loose constant is finite and independent of input N,m,b. It even handles all lengths at those finite degrees; no m-dependent lookup or precomputation is required. The same uniform on-demand algorithm is used. Combined with(A3), a constant such as9^N0 can be absorbed into one polynomial bound; its numerical size is enormous and supplies no practical onset claim. A reviewer must not confuse a finite exceptional input set with an unrecorded input exclusion, and must not insist that a worst-case polynomial bound follows on rare macro draws.

Therefore the normalization/finite-exception part of the ES and ES-LOG route survives this role's adversarial checks. The remaining premise here is the actual uniform cost envelope(A2) and exact production law; these are assigned to the decoder role and subsequent exact-version review. This report alone is not a sampler construction theorem.

## D. Actual bridge counterexample to unconditional stage multiplication

Under U_(4,4), there are120 identity words. Their nontrivial component types split as follows:

-96 words have one connected size3 minimal component: choose its3 labels in4 ways and one of24 connected identity words on them.
-6 words have one size2 genus1 component: choose one edge and repeat it4 times.
-18 words have two disjoint size2 minimal components: choose one of3 perfect matchings and one of6 interleavings of the two equal-edge pairs.

These cases exhaust every component type of half-length2. Order nontrivial components by their least label. Let E1 mean the first component has size2, and E2 mean a second component exists and has size2. Then

    P(E1)=24/120=1/5,
    P(E2)=18/120=3/20,
    P(E1 intersection E2)=3/20 >3/100=P(E1)P(E2).

Conditioning on E1 changes the second-event probability to3/4. The exact cost expectation, however, is additive:

    E H_9=(96*9^3+6*9^2+18*2*9^2)/120=12231/20.

This is a concrete bridge-law regression against replacing the exact macro argument by a product of marginal stage bounds. It is not a counterexample to(A1)–(A3); those steps explicitly avoid the failed implication. The separate CP-1 cached-prefix counterexample likewise remains valid.

## E. Separately frozen EC-OBSTR.v1: the envelope fails at the3/4 benchmark

Scope was frozen in scope-obstruction-v1.md before this proof. For integer j>=64 put

    N=2^(8j), m=2^(6j), k=m/2,
    J=2^(3j), Vmax=max nontrivial component size,
    epsilon=2^(-1-jm/2).

**Claim EC-OBSTR.v1.**

    P_U(Vmax<=J)<=epsilon,
    E_U H_9 >=9^(J+1)(1-epsilon).                 (E1)

In particular no one polynomial in N,m bounds E_U H_9 on this sequence.

Proof. The accepted I1 finite numerator lemma, Section2 of R3 proof-v1.md (SHA256cdfcc097d50a8ed070c27fcc5b8ae700e0472769578f7ccd6ab7e5ac85178aef), holds for any fixed integer cutoff1<=J<=N and G>=0 under

    x=k/N^2, q=3Nx<=1/2, b_J*x<=1,6G^3*x<=1/16,
    b_J=(J^3-J)/36.

It bounds the genus<=G OR size<=J event count by m!(N^2/k)^k exp(8k). Its same-paper subgroup comparison proves ratio<=epsilon on the current sequence once those finite conditions hold. This invokes the accepted finite lemma and its explicit hypotheses, not the old logarithmic policy conclusion.

Set G=0 and J=2^(3j). Then1<=J<=N, x=2^(-10j-1), q=3*2^(-2j-1)<=3/8, and

    b_J*x <=2^(9j)/(72*2^(10j))=2^(-j)/72<1.

The genus condition is0. Every word with Vmax<=J belongs to that enlarged genus0-or-small-support event, so its probability is at most epsilon. On the complementary event, integer Vmax>=J+1 and H_9>=9^(J+1). Averaging proves(E1).

Since epsilon<1/2 and N+m+2<=2N, for any fixed constants C,d>0,

    E H_9/[C(N+m+2)^d] >=9^(2^(3j)+1)/[2C*2^((8j+1)d)] ->infinity.

This proves the stated envelope limitation. It supplies NO lower bound on actual optimized decoder work, whose9^v bound is an upper envelope. A different implementation or tighter resource analysis might still have polynomial expectation; a different global algorithm remains possible. The ES/ES-LOG ranges are unchanged and do not include this asymptotic sequence. No all-length impossibility or computational hardness conclusion is justified.

## F. Boundaries and retained failed routes

Odd identity lengths have no target; m0 gives H_a=0; m2 gives exactly one size2 component and H_a=a^2; N2 has that same fixed H_a at every positive even length, regardless of how large its genus becomes. High genus alone therefore does not force an exponential support cost. Singleton positive length and negative component genus remain infeasible. Near-minimal length v=k+1 has only genus0 and is retained.

The actual rare marked component(v6,ell14,g2) has positive exact expected count at N82,m14, and related positive examples occur at N128,m16. Those contributions are included by the full moment calculation; no small mass is rounded away. The previous fixed42/12->5/12 cutoff regression is inapplicable as an eligibility failure here because every component remains eligible, but it remains a valid counterexample to recomputing old cutoffs. H0/H1/H2, zero-square insertion,(ab)^3,81-versus80, unweighted graph bias, parallel cut multiplicities and CP1 retain their old dispositions. This route neither uses nor repairs those mechanisms.

## Dependencies and review boundary

A/B: exact component marking and nonnegative summation; valid whole-macro total expectation under explicit(A2). C: inherited SG-T1/SB-T1 component-expectation bounds plus(B); explicit finite constant. D: elementary exact S4m4 type counts, independently checked in finite output. E: accepted I1 finite numerator/denominator proof at its arbitrary-J scope plus checked new J substitution. No new external source is imported. All supporting/limitation claims in this document remain provisional until fresh blind and exact-version review; the full global sampler mission remains OPEN.
