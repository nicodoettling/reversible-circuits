# ES.v1 and ES-LOG.v1: exact sparse bridge sampling by expected cost

DRAFT v1, 2026-10-28. Status PROVISIONAL. The moment proof below is complete by author; the exact current decoder/cost artifact, finite falsification and fresh reviews remain integration obligations. This draft is not proof acceptance. The global all-length polynomial-time mission remains OPEN.

## 1. Statements and input model

Write T_N for the transpositions on canonical labels [N], and
Omega(N,m)={(t_1,...,t_m) in T_N^m : t_1...t_m=id}.
Products act rightmost first. Every output explicitly lists all m factors. Randomness consists of independent fair bits. Let P=N+m+2.

The proposed algorithm is one unrestricted exact least-label macro sampler, followed by on-demand all-genus quotient decoding of the components actually selected. It is defined on every N>=2 and even m>=0; odd m is rejected. It computes no logarithmic regime test and no component cutoff. The two separately admitted claims are:

* ES.v1: if m^3<=N^2, its output is exactly uniform on Omega(N,m), in expected bit time polynomial in N,m.
* ES-LOG.v1: if m<=N^(2/3) ln(N)/4, the same conclusion holds for the same algorithm.

The two ranges are not silently equated for small N. Exactness means TV0 for every requested b>=1; an accuracy argument is unnecessary. The claim is polynomial in degree N and explicit length m, not in log N wires. No polynomial worst-case running-time or worst-case space theorem is asserted.

For a fixed finite constant A and exponent d, the required decoder interface is the following pointwise resource envelope. Conditional on any full sampled macro M, including its labeled blocks and assigned positions,

    E[T | M] <= A P^d (1 + sum_{B nontrivial in M} 9^{|B|}).       (RC)

The expectation in (RC) is only over the exact fair-bit choices still used by decoders and other elementary sampling primitives. The deterministic count/transition work is included. R2 is deriving (RC) with a specific exponent for the actual current source. Sections 2–7 prove that (RC), together with the exact decoder/assembly law, yields both claimed expected-polynomial bounds. A standalone implication with explicit constants is given in Section 7; it is not a substitute for verifying R2's implementation.

## 2. Macro law and bridge normalization

For a connected identity word on a fixed labeled v-set, v>=2, its length is ell=2v-2+2g with integer g>=0. The feasibility proof counts permutation-cycle joins: identity requires equally many joins and splits, and connecting v vertices requires v-1 joins. Conversely, repeated pairs on a spanning tree and any extra repeated edge pairs realize all such even lengths. Isolates have (v,ell)=(1,0), separately.

Let C(v,ell) count the literal connected words on one fixed v-set, A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!, Z(n,2j)=|Omega(n,2j)|, and S(n,j)=Z(n,2j)/(2j)!. For a support macro with disjoint labeled nontrivial blocks B and genera g_B, its cost is sum_B(|B|-1+g_B) and its normalized weight is product_B A_{g_B}(|B|). Interleaving the component words proves this identity: after multiplication by (2j)!, the result counts all literal words with that macro. Restriction to support blocks recovers every internal word and its positions uniquely.

Put m=2k and let X_{v,q} be the number of components with v vertices and length 2q in a uniform global bridge. Marking one actual component, choosing its labels and positions, and choosing both its internal and complementary identity words gives exactly

    E_U X_{v,q}
      = binom(N,v) binom(2k,2q) C(v,2q) Z(N-v,2k-2q)/Z(N,2k)
      = binom(N,v) A_{q-v+1}(v) S(N-v,k-q)/S(N,k).       (M)

The marked object is an actual connected component, so equal-sized components are counted separately. The denominator is the full identity-bridge count. There is no claim that support edges or components are independent.

For completeness, if 2k<=N and D=N-2k+1, the inherited fresh-pair incidence gives

    S(N-v,k-q)/S(N,k) <= 4^q (k)_q/D^{2q} <= (4k/D^2)^q.       (I)

To recheck its normalization, embed each base macro of cost k-q on the complement of the fixed removed v-set by isolating that set. Such a base uses at most 2(k-q) labels, so it has at least N-2k+2q isolates. Add q disjoint unordered pairs, each with its unique length-two identity word and normalized component weight 1/2. For a base of weight w, total weighted extensions are at least w D^{2q}/(4^q q!). A final cost-k macro has at most k minimal two-vertex components and at most binom(k,q) choices of which ones to delete. Deleting specified marked pairs recovers its base uniquely; requiring the removed v-set to be isolated only reduces this number. Comparing the weighted incidences gives (I). The q=0 case has empty products and zero residual branches contribute zero.

## 3. Inherited count and marked expectation bounds

The load-bearing literature input is the DYZ exact connected Hurwitz recurrence with its already checked ordered-word normalization. The canonical source record is experiments/20260922-sparse-global-sampler/source_checks.md: Dubrovin–Yang–Zagier, Proposition 1 Eq(13), Section 1.2 Eqs(19)–(20), genus-zero value after Eq(28), with C(v,ell)=v!ell!h_{g,v}. This role inherits those primary-source checks and rechecks the downstream formulas; it does not claim a new direct reading of the primary PDF.

The canonical SG proof derives, uniformly for all v>=2 and g>=0,

    A_g(v) <= v^{v-3} b_v^g/g!,       b_v=(v^3-v)/36.       (H)

Brief derivation: after dividing the DYZ series recurrence by v^{v-3}t^{2v-2}, it becomes a convex positive combination of L(at)H_a(t)H_b(t), a+b=v, where L(z)=2(cosh z-1)/z^2. Its nonnegative coefficients satisfy L(z)<=coef exp(z^2/12), because 2/(2j+2)!<=1/(12^j j!). The exponential budgets satisfy b_v-b_a-b_b=abv/12>=a^2/12. Induction proves (H). This is a deterministic coefficientwise comparison, not probabilistic independence.

Write X_v=sum_q X_{v,q}. Combining (M), (I), (H), and extending the nonnegative genus sum yields

    E_U X_v <= binom(N,v) v^{v-3} x^{v-1} exp(b_v x),
    x=4k/D^2.

Feasibility gives v<=k+1. Thus b_v x<=v z for z=k^2(k+2)/(9D^2), and v!>=(v/e)^v gives

    E_U X_v <= N c rho^{v-1}/v^3,
    c=exp(1+z), rho=c N x.                              (SG)

For the separately admitted logarithmic range, keep the falling factorial in (I). Since q=v-1+g and 0<=g<=k-v+1, the finite binomial theorem gives the stronger inherited bound

    E_U X_v <= binom(N,v)v^{v-3}(k)_{v-1}(4/D^2)^{v-1}
                 * (1+4b_v/D^2)^{k-v+1}.                (FG)

Indeed (k)_{v-1+g}=(k)_{v-1}(k-v+1)_g, and the genus sum is exactly the binomial expansion. For s>=0, 1+s^3<=(1+s)^3 and ln(1+s)<=s. It follows that the last factor is at most exp(z_new v), where

    z_new=3k/(9D^2)^{1/3}, c_new=exp(1+z_new), rho_new=c_new N x.

Therefore the canonical SB proof gives

    E_U X_v <= N c_new rho_new^{v-1}/v^3.                (SB)

All these expectations refer to the same exact global bridge law. SG and SB are inherited component bounds, not new claims of this investigation. The new use below is to pay the real decoder work without discarding any component.

## 4. Exponential component-moment lemma

Let a>=2 be a fixed integer. Suppose m>0, 2k<=N, and either (SG) or (SB) holds with parameters c,rho. Define the nonnegative random variable

    W_a(M)=sum_{B nontrivial component of M} a^{|B|}
          =sum_{v=2}^{min(N,k+1)} a^v X_v.

If a*rho<1, finite-sum linearity, the marked bound, v^{-3}<=1/8 for v>=2, and a geometric series prove

    E_U W_a <= N c a^2 rho/[8(1-a*rho)].                 (EM)

Explicitly, sum_{v>=2} a^v rho^{v-1}=a^2 rho/(1-a*rho). Replacing the finite feasible sum by this infinite positive series only increases it. If a*rho<=1/2, then

    E_U W_a <= a N c/8.                                (EM-half)

No event-intersection probability is multiplied. No macro component is assumed independent of any other component. There is no reweighting by the decoder runtime: the macro is sampled first under its ordinary exact law, and (EM) is an expectation of a fixed nonnegative function of that macro.

The m=0 case has W_a=0 and needs no positive-rho formula. At any feasible input, with no restriction on m, the deterministic fallback bound is

    W_a <= N a^N.                                     (F)

There are at most N nontrivial components and each has at most N vertices. The loose bound intentionally avoids any probabilistic assumptions and is sufficient for finite-degree exceptions.

## 5. ES.v1 constants

Assume m^3<=N^2 and N>=64. Then m<=N^{2/3}<=N/4, so D>=3N/4. Put u=N^{2/3}>=16. We have k<=u/2 and k+2<=5u/8; hence

    z <= (5N^2/32)/(81N^2/16) =5/162 <1/16.

Using e<11/4 and exp(1/16)<=1/(1-1/16)=16/15 gives

    c=exp(1+z)<44/15<3,
    rho=c N(4k/D^2)<(32/3)N^{-1/3}.                  (ES-C)

For a>=2 and N>=(32a)^3, this implies a*rho<1/3. In (EM), (a*rho)/(1-a*rho)<1/2, so

    E_U W_a <3aN/16.                                 (ES-M)

In particular, for the decoder base a9, the threshold is (288)^3. Every degree below that fixed threshold is covered by (F), for the same algorithm. No hidden choice of an exponent depends on N,m or an accuracy request.

## 6. ES-LOG.v1 constants

Let M=2^2048 and suppose N>=M, L=ln N, m<=N^{2/3}L/4. Then L>1000. As rechecked in the canonical SB proof, L<=exp(L/3), so m<=N/4 and D>=3N/4. Consequently

    z_new=3m/[2(9D^2)^{1/3}] <=m/N^{2/3}<=L/4,
    N x=2Nm/D^2<=4m/N<=L exp(-L/3).

For L>=1000, 1+ln L<=L/24. Therefore

    c_new<=e N^{1/4},
    ln rho_new<=1+ln L-L/12<=-L/24,
    rho_new<=N^{-1/24}.                              (LOG-C)

At N>=M, 9*rho_new<=9*2^{-2048/24}<1/2. Applying (EM-half) with a9 gives

    E_U W_9 <=(9e/8)N^{5/4}< (27/8)N^{5/4}<4N^2.     (LOG-M)

All constants here are absolute. The threshold M is deliberately inherited and conservative, not an empirical onset estimate.

## 7. One uniform expected-time polynomial

Take M=2^2048 and K=1+9^M. These are proof constants, not values computed or stored by the algorithm. Since M>(288)^3, Sections 5 and 6 show that for N>=M satisfying either separately stated length condition,

    E_U W_9 <=K N^2.

For 2<=N<M, (F) gives W_9<=N9^N<=N9^M<=K N^2 at every length. Thus uniformly throughout the union of ES.v1 and ES-LOG.v1,

    E_U W_9 <=K N^2.                                 (UNIF)

This is one bound with one finite constant. The same unrestricted algorithm handles small and large degrees. There is no finite lookup table, precomputed exception catalogue, changed error parameter, or algorithm branch at M. The coefficient is astronomically conservative, which limits any practical interpretation but does not weaken the quantified polynomial theorem.

Assuming the pointwise cost envelope (RC), the law of total expectation gives

    E T = E_M E[T|M]
        <= A P^d (1+E_M W_9)
        <= A(1+K) P^{d+2}
        = A(2+9^{2^2048}) P^{d+2}.                   (TIME)

This proves the analytic expected-cost implication with completely explicit degree dependence and a fixed coefficient. It does not equate the count of quotient states with bit cost: RC must charge transitions, lookups, integer arithmetic, canonicalization, stacks, and exact fair-bit selection. R2 is responsible for the current literal implementation and that deterministic envelope.

Fair-bit rejection costs are controlled pointwise. An exact integer in [0,Z) is drawn using ceil(log_2 Z) bits and rejection; conditioned on any positive-mass history and integer Z, acceptance is greater than 1/2 (or deterministic at Z1). Thus its conditional expected attempts are fewer than two. Every future fresh random block is independent of the past, and the bound holds on each actual history, including adaptive states. A fixed polynomial upper bound on the number of integer draws and their bit lengths conditional on M yields RC by iterated expectation. This is not multiplication of unconditional marginal success probabilities.

The algorithm terminates almost surely: every macro and every component has finite deterministic tables, decreasing remaining-length recurrence, and a finite number of almost-surely terminating rejection samplers. A finite full-macro expectation follows from (TIME). Only an exponential worst-case envelope in support size is provided for the quotient decoder. No polynomial worst-case space conclusion follows merely from the moment estimate. Under a standard bit-operation model in which allocating or writing a bit costs time, expected peak work space is bounded by input storage plus expected time; this observation must not be relabeled a worst-case space theorem.

## 8. Exact law, dependencies, and preserved regressions

Exact unrestricted least-label assembly uses D(v,ell)=C(v,ell) at every feasible type, with isolates D(1,0)=1:

    Z_D(n,t)=sum_{v,ell} binom(n-1,v-1)binom(t,ell)
                         C(v,ell)Z_D(n-v,t-ell).

It samples the least label's component type by these integer weights, its other labels and positions uniformly, and continues until the full macro is fixed. This stage performs only polynomial scalar work; no quotient table for an unselected component may be built. The connected decoder then retains actual prefix permutation and exposed support partition while consulting counts on their simultaneous-conjugacy quotient. Its literal-edge branch weights telescope to 1/C(v,ell). Combined with assembly, every word has probability exactly 1/Z(N,m). Labels and interleavings are actual choices with their full binomial factors; scalar counts alone are not called a sampler.

The exact implementation/current source and RC must be frozen and reviewed separately. The elementary quotient invariant and 3^{v-1} state bound are inherited QC inputs; a new unrestricted use does not inherit the old cutoff runtime claim unchanged. The squared inventory from deterministic linear scans is what yields base9, and remains a live review obligation until R2's proof is frozen.

Dependencies:

* D0, inherited accepted: DYZ ordered-word normalization and positive scalar connected-count recurrence, as recorded in the canonical source checks and closed ledgers.
* D1, inherited accepted/rechecked here: exact marking (M), fresh-pair incidence (I), all-genus majorant (H), and the SG/SB expectation bounds, with their precise conditions.
* D2, new PROVISIONAL: exponential-moment (EM), finite-degree bound (F), explicit regime substitutions (ES-M)/(LOG-M), and common bound (UNIF).
* D3, current R2 PROVISIONAL/pending artifact: exact full macro/quotient decoder and pointwise bit envelope RC for its implementation.
* D4, new PROVISIONAL: total expectation implication TIME and both ES conclusions, depending on D0–D3. Fresh blind and exact-version reviews and finite checks remain pending.

Boundary and historical regression obligations:

* m0: empty word; W9=0. Odd m: sign obstruction, reject. m2: repeated uniformly chosen transposition, exactly. N2: unique edge at every even length, whether or not that input lies in either runtime range.
* v1 supports only the empty isolate; zero-count branches are never selected. Near-minimal v=k+1 only genus0 is feasible; all higher feasible genera on smaller v remain eligible.
* The S3 length5 transposition-endpoint 81-versus80 witness requires retaining exposed support in suffix states. The quotient must preserve support-block data, not just cycle type.
* (ab)^3 zero-square insertion and support-graph weighting failures remain failures of those mechanisms. This decoder enumerates all literal-edge continuations and never inserts squares or samples an unweighted graph.
* Marked-cut multiplicities and parallel-core corrections belong to different constructions; they are not discarded or implicitly transferred here.
* The old (42,12)->(5,12) fixed-cutoff failure, H0/H1, and enlarged-cutoff H2 obstructions are preserved. This algorithm imposes no component cutoff and has no excluded support event; the old obstruction sequences do not lie in the claimed sparse runtime regime asymptotically.
* CP1 retains posterior masses 21/2000 for A_b,1/20 for C_b,879/1000 for D; p(x)=1/10,p(e_b)=121/2000,p(f_b)=21/2000, and the matching two-hit probability is21/2000>1/100. Thus the old marginal product claim is rejected. The present proof conditions on the complete actual macro, bounds all residual fair-bit costs on actual positive-mass histories, and averages a nonnegative sum; no CP1-invalid product is present.

No failed mechanism is a refutation of the unrestricted all-length sampler objective. The first unclosed integration obligation in this draft is the exact R2 cost/interface proof and its current source, followed by required fresh reviews. No claim is accepted solely because a process ended or a report was saved.
