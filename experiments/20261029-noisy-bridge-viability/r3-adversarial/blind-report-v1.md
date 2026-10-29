# Blind adversarial reconstruction B1

Frozen 2026-10-29 before reading candidate algorithms, r1 work, r2 analysis, or coordinator claim summaries. Inputs: M0 version 1, campaign mission and plan, project operating instructions, sampler/proof-audit skills and references, and the permitted 20261028 projection report/checker. No new mathematical computation executed. This is same-model correlated review, not independent certification. All new derivations below are **provisional, not externally audited**.

## Game and test conventions

N>=2, even L>=0, 0<=k<=L, q=binom(N,2), mu uniform on all transpositions. Products act rightmost first. U is uniform on all labeled ordered identity words. Q_k replaces a uniformly selected k-subset by independent mu draws; positions and draws remain hidden. Identical public setup A is exposed in both worlds. Reused setup keeps hidden K but uses independent word and noise tapes for every reply. There is no decoder oracle. Advantage is the absolute difference of acceptance probabilities, not success probability. Every attack below is polynomial in explicit N,L if its stated subroutine is polynomial; this says nothing about polynomiality in log N.

## B1.1 Local relation counting, beyond gate equality

Let r>=4 be even, r<=L. A known collection of B disjoint length-r windows has product identity before scrambling. After s adjacent Hurwitz moves, at least B-2s of those windows retain identity product: moves inside a window preserve its product, and a boundary-crossing move can affect at most two designated windows. Global simultaneous conjugation preserves every identity relation. At most k designated windows are hit by Q_k. Thus a complete-word adversary counting identity windows accepts at threshold B-2s-k whenever this threshold is positive, with structured probability one. This does not presume independent survival events.

If a cyclic shift hides the partition offset, scan all L cyclic length-r windows instead. The same B-2s-k witness windows remain among the scan, provided the scrambling and cyclic shift order are explicitly as just described (or the count of damaged witnesses is reproved). If only linear windows are scanned, lose at most one witness crossing the boundary. If block lengths vary over a fixed finite set, scan that set and sum the corresponding reference means. Do not infer a hidden identity subsequence merely from a Hurwitz-invariant support relation.

Here is an exact matched-reference mean. Write p_a=mu^{*a}, p_0=delta_id. For a fixed ordered r-subset and h in S_N, define

    beta(N,L,k,r)
      = sum_s [binom(r,s) binom(L-r,k-s) / binom(L,k)]
          * sum_h p_s(h^{-1}) p_(r-s)(h) p_(L-r+s)(h^{-1}) / p_L(id),

where invalid binomial coefficients vanish. This is the probability that the product of the observed r gates equals identity under Q_k(U). Proof: condition on the s replaced positions in the subset. Averaging fresh central mu gates moves their convolution to one end. The remaining r-s old gates have global-U ordered-subsequence product law p_(r-s)(h)p_(L-r+s)(h^{-1})/p_L(id), by the permitted stable-sort bijection. Average the resulting identity probability and the hypergeometric s law. Cyclic windows have this same law by cyclic invariance of the identity-word measure and Q_k; the cyclic order is not silently identified with sorted order.

For M scanned windows, E_reference[X]=M beta. Markov gives reference acceptance at threshold t>0 at most min(1,M beta/t), and hence attack advantage at least max(0,1-M beta/t). No second-moment or independence claim is needed. This is already a finite-parameter attack theorem conditional only on the explicit identity-window witnesses. Whether its bound is useful for a candidate requires beta and its exact witness count.

One sufficient long-completion estimate is the following. Suppose every parity-allowed p_a(g), for a in {L-r,...,L}, has relative error <=epsilon<1 from 2/N!. Then the r-gate U marginal has TV <=epsilon/(1-epsilon) from mu^r; Q_k restricted to these gates preserves mu^r and contracts TV. Consequently

    beta <= p_r(id)+epsilon/(1-epsilon) <= 1/q+epsilon/(1-epsilon).

The last inequality follows for even r>=2 from p_r(id)=||p_(r/2)||_2^2 and convolution contraction, giving ||p_(r/2)||_2<=||mu||_2. The precise asymptotic completion-mixing estimate is a separate dependency; do not import it without checking parameters. A concrete candidate schedule must state N(lambda),L(lambda),k(lambda),r(lambda),s(lambda), and ensure both positive threshold and vanishing reference bound. This report does not claim that all structured samplers expose these witnesses.

## B1.2 Robust support and partition leakage

Each replaced gate removes at most two previously touched labels and adds at most two new labels. Thus |support(W')|-|support(W)| lies in [-2k,2k]. A candidate always supported on at most v labels yields |support(W')|<=v+2k. Reference acceptance of that test is at most

    Pr_U[|support(W)|<=v+4k]
      <= min(1, binom(N,a) |Omega(a,L)| / |Omega(N,L)|), a=v+4k<=N.

The union bound includes every support of size <=a by enlarging it to an a-set. For a>=2, |Omega(a,L)|=binom(a,2)^L p_L^{(a)}(id). Degenerate a=0,1 and L=0 need direct conventions. The estimate becomes vacuous when a>=N. Setup conjugation hides label names but not this count. A useful asymptotic result requires this count ratio to be small; that estimate is not supplied here.

The full support-component partition gives other Hamming-robust tests. Removing and adding one edge changes the number of connected components on the full N-vertex graph by at most two. Any stronger weighted-component claim must account explicitly for destroyed/merged components; global conjugation and cyclic shifts alone do not erase size/weight profiles.

## B1.3 Public support / low-entropy code test

For public A suppose D_(A,K) is supported in a known set S_A of identity words. An adversary that can decide d_H(y,S_A)<=k in polynomial time accepts every noisy structured reply. If it accepts Q_k(U), then the original U word lies within Hamming distance <=2k of S_A. Therefore reference acceptance is at most

    min(1, |S_A| * sum_(j=0)^min(2k,L) binom(L,j)(q-1)^j / |Omega(N,L)|).

This is an information-theoretic bound and an efficient attack only with an efficient neighborhood-membership procedure. Low entropy by itself does not provide that procedure, and Shannon entropy is not an upper bound on support size. Hidden K requires union over allowed keys unless a learning phase recovers enough of K. Meet-in-the-middle is relevant only after the actual candidate's factorization/code representation is specified.

## B1.4 Reused setup leakage that one sample misses

Fix a position j. Let pi_K be its conditional unnoised gate law under retained setup, with public A held fixed. Under Q_k the marginal is pi'_K=(1-k/L)pi_K+(k/L)mu for L>0. Two fresh replies are conditionally independent given K. Their coordinate-j collision probability exceeds the reference 1/q by

    (1-k/L)^2 E_K[sum_t (pi_K(t)-1/q)^2].

The identity follows pointwise in K from sum pi_K=1; it does not require average-setup pi_K=mu. Testing disjoint pairs of replies estimates this bounded event using O(delta^-2 log(1/eta)) independent pairs conditional on a fixed key when its own gap is >=delta. Average-setup nonnegligible expectation alone does not guarantee that gap for every key or high probability over setup; key-mass quantifiers must be stated.

Example regression: sample K uniformly from Omega(N,L) at Setup and repeat exactly K on every call (fresh tapes may be unused). At k=0 one-sample output is exactly U after averaging setup; two-sample equality has probability one instead of 1/|Omega|. For k<L, a fixed-coordinate two-reply collision excess is (1-k/L)^2(1-1/q). This is a reused-setup counterexample to a one-sample-to-multisample implication, not the main within-word pair control.

More generally, any keyed mean statistic can be learned across fresh replies. The analysis must condition on K throughout; unconditional replies are a mixture of product laws, not a product of their averaged marginal.

## Boundary and counterexample ledger

- Odd L: U is undefined/empty and must be rejected. L=0: k=0, both words empty; every distinguisher has advantage zero.
- N=2: one gate, every even-length word equal; Q_k changes nothing; every advantage is zero. Here beta=1 for even r and all proposed upper bounds are correspondingly vacuous.
- L=2: every identity word is a doubled gate. There is no r>=4 local-relator attack; the reference itself has the doubled syntax. Tests must not compare with unconditioned words.
- k=L: every coordinate becomes iid mu, independently of the source and setup; complete-word laws coincide. All valid positive advantage bounds must vanish or become vacuous.
- k=0: no attenuation; beta=p_r(id)p_(L-r)(id)/p_L(id).
- r=0: beta=1. r odd: no product of r transpositions is identity, in either world.
- A single repeated uniform gate has the p_2 endpoint for k=1 yet remains word-distinguishable; endpoint equivalence does not close a full-word claim.
- Global sign, distance<=2k and support<=4k of the endpoint are shared restrictions and give no matched-world attack alone.
- Product bounds over untouched windows are disallowed without the exact without-replacement joint law. Markov above deliberately uses only the first moment.
- Connected conditioning invalidates the global completion formula; no connected reference is used here.

## Needed candidate information and next checks

For each frozen candidate: exact setup exposure, secret reuse, identity construction, relator-window witnesses, transformations and order, number of adjacent moves, support constraints, entropy/support and implementable membership test. Then compute beta and complete noisy-word distributions in S3L4/S4L4 and feasible S4L6 using exact integer/Fraction arithmetic, include k=0,1,L and N2/L0, and record every statistic against Q_k(U). Whole-word TV and a predeclared attack's advantage are different outputs. No attack selection based on a finite diagnostic may be advertised as a held-out security test.

Verdict: **keep** these attack templates and exact obligations for candidate-specific examination; no candidate has yet been inspected and no generic impossibility or security claim follows.
