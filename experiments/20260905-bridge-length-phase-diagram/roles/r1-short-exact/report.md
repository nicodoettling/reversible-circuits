# R1 Final Report

Status: final, author-frozen 2026-09-05 15:33 UTC; ready for nonauthor audit.

## Result

**Proved.** Every feasible transposition bridge has a direct exact sampler in expected bit time

    exp(O(sqrt(min{m,N}))) poly(N,m).

This is exact fixed-parameter sampling in length m. For every fixed constant A, it is polynomial in N on m <= A(log N)^2, and polynomial in m at fixed N. More generally it is polynomial in (N,m) whenever min{m,N}=O(log^2(N+m)). An explicit random-bit truncation gives bounded-time epsilon-close sampling with polynomial overhead in log(1/epsilon), always returning the requested endpoint. Exactness has an expected-time qualification; bounded-time sampling has distributional error only.

The theorem includes arbitrary endpoints, with a sharper defect cutoff for the public identity endpoint. Minimal arbitrary endpoints additionally admit polynomial exact sampling without a partition-state factor. Neither theorem is a Markov-chain mixing statement.

There is **no computational hardness result**. Enumerating the cycle-type table becomes superpolynomial beyond the proved sparse regime; this limits the named implementation, not other samplers.

## Precise theorem and bit complexity

Let N>=2, m>=0, and let g be an explicit permutation map on [N]. Multiplication is composition of maps: (alpha beta)(x)=alpha(beta(x)); the rightmost displayed factor acts first. Put h=N-cycles(g). The fiber is feasible exactly when m>=h and m=h modulo 2. Infeasible inputs are reported as empty fibers.

For feasible inputs define

    D = min{N-1, floor((m+h)/2)},
    S(N,D) = #{partitions mu: |mu|<=D, |mu|+length(mu)<=N},
    ell = ceil(log2(N+m+2)).

There is an exactly uniform sampler on Omega(N,m;g) that outputs the exact length and endpoint and, under independent fair random bits, has the conservative expected bit bound

    O((m+1)^3 [ (D+1)^4 S(N,D) + N^3 ] ell^2).            (1)

The bound permits a naive lift that enumerates every labeled transposition at each output position. Table counts have at most

    L = 1 + m ceil(log2(max{2,binom(N,2)}))

bits. There are at most (m+1)S(N,D) table entries and O(S(N,D)(D+1)^2) transition records with O(D log(D+2))-bit type keys. Space is S(N,D) poly(N,m) bits. The output uses O(m log(N+1)) bits and an explicit permutation map uses O(N log(N+1)) bits. Polynomial time in N is not polynomial time in a wire count log2 N.

For identity bridges, D=min{N-1,floor(m/2)}. For D>=1,

    S(N,D) <= min{ sum_{d=0}^D p(d), p(N) }
           <= min{ exp(pi sqrt(2D/3)), exp(pi sqrt(2N/3)) }.   (2)

For arbitrary endpoints, h<=m implies D<=min{N-1,m}, yielding the same exp(O(sqrt(min{m,N}))) asymptotic bound. Constants in (1) are absolute; fixing m<=A(log N)^2 fixes A independently of N, and the polynomial degree may depend on A.

For any integer b>=0, a worst-time bounded variant has TV error at most 2^-b and cost (1) multiplied by O(b+log(m+1)+1). Choose b=ceil(log2(1/epsilon)) for 0<epsilon<1. Since exact cost is independent of b, the precision-aware condition min{m,N}=O(log^2(N+m+b)) is another sufficient polynomial regime.

## Positive recurrence and exactness proof

A transposition joins two cycles or splits one cycle, changing defect d(p)=N-cycles(p) by exactly one. Defect equals minimum transposition length: each step changes it by one, and splitting every nontrivial cycle reaches identity in d(p) steps. Sign is (-1)^d(p). These observations give necessity of feasibility. Minimal cycle factorizations padded with identical transposition pairs give sufficiency for N>=2.

Encode a cycle type by a partition mu with one part a-1 for each nontrivial cycle of length a. Then |mu|=d, its nonfixed support size is d+length(mu), and its fixed-point count is c_1=N-d-length(mu). Let c_a denote the number of a-cycles. This is a bijection with the types counted by S(N,D); retaining c_1 is essential.

For a fixed permutation of type mu, the number K(mu,nu) of individual transpositions giving next type nu follows these positive rules, adding weights when resulting types coincide:

* Join distinct lengths a<b: replace a,b by a+b, with weight a b c_a c_b.
* Join equal lengths a: replace two a-cycles by one 2a-cycle, with weight a^2 binom(c_a,2).
* Split an a-cycle into b<a-b: replace a by b,a-b, with weight a c_a.
* Split an even a-cycle equally: weight (a/2)c_a.

For joins, choose two cycles and one endpoint in each. For a split, circular pairs at separation b number a, except equal halves count every unordered pair twice. These cases exhaust transpositions, so sum_nu K(mu,nu)=binom(N,2). The coefficients apply to either multiplication side: conjugating the selected transposition by the current permutation interchanges left and right updates.

All completion counts here refer to **one fixed labeled permutation** of the indicated type. They do not aggregate over its conjugacy class. There is no conjugacy-class-size factor in the recurrence.

Remove successive first factors by keeping residuals

    r_0=g,   r_(i+1)=t_(i+1) r_i.

After i steps, d(r_i)<=h+i. A residual completable in m-i steps also satisfies d(r_i)<=m-i. The maximum of this cone is floor((m+h)/2). Define B_i(mu) to count suffixes from one fixed residual of type mu for

    |mu| <= min{h+i,m-i,N-1},   |mu| = h+i modulo 2.

Set B_m(empty)=1 and

    B_i(mu) = sum_nu K(mu,nu) B_(i+1)(nu),                (3)

treating missing entries as zero. From a type inside the cone, any one-step successor automatically has defect <=h+i+1. A successor with defect >m-i-1 admits no valid suffix. Thus truncation removes no valid completion; backward induction proves (3).

At residual r_i, choose an individual labeled transposition t with weight B_(i+1)(type(t r_i)). The total is B_i(type(r_i)). These probabilities telescope to 1/B_0(type(g)) for every valid word and zero for every invalid word. Finally

    r_m=t_m ... t_1 g=e  implies  g=t_1 ... t_m,

which verifies the output product convention. This proves exactness independently of spectral or mixing results.

Every count is at most binom(N,2)^m. There are O((D+1)^2) candidate split/join rules per type, polynomial-size keys, and m+1 layers. Schoolbook integer arithmetic and sorted-key lookup give (1). At sampling time, computing every candidate next cycle type uses O(N^3) map operations per step; summing L-bit weights stays within (1). The deliberately loose (D+1)^4 factor absorbs key construction, generation, and sorting. Generating all partitions up to D and then filtering costs only another polynomial factor: sum_{d<=D}p(d)<=(D+1)p(D+1)<=(D+1)S(N,D). For the last inequality, embed partitions of D+1 as cycle types on N labels by adding fixed points; D+1<=N and their defects are at most D.

The partition bound is self-contained. For t>0 the Euler product yields

    sum_{d<=D}p(d) <= exp(tD) product_{j>=1}(1-exp(-tj))^-1,
    log product_{j>=1}(1-exp(-tj))^-1
      = sum_{k>=1} [k(exp(tk)-1)]^-1 <= pi^2/(6t).

Choose t=pi/sqrt(6D) to obtain (2). D=0 has one type. The cap p(N) is the number of conjugacy types of S_N.

## Random bits: exact expected time and bounded approximation

To select an integer below W>1, draw ceil(log2 W) fair bits and reject values at least W; W=1 needs no bits. Each trial succeeds with probability greater than one half. Hence fewer than two trials are needed in expectation, proving the exact expected-time claim. A uniformly bounded number of fair random bits cannot implement arbitrary rational probabilities exactly; no such claim is made.

For bounded running time, cap each of at most m random-integer choices at

    R = b + bit_length(max{1,m})

trials. On a cap failure discard the partial word and return a deterministic valid word for the original input, obtained by minimal cycle factorization and pair padding. Couple to the exact sampler with the same random tape. The outputs can differ only after a cap failure, whose probability is at most m 2^-R <=2^-b. Therefore TV error is at most 2^-b, with the endpoint exact on every execution. There is no conditioning on successful output.

## Canonical first appearances and their weights

**Proved.** Every active label in an identity word occurs in at least two transposition factors. If x occurred only in (x y), write the word as A(x y)B. Since A and B fix x, its image is A(y), which is not x. Thus at most m labels are active, since there are 2m endpoint occurrences. This proves the support bound without a connected-component classification.

Scan the word in time order, sorting each actual endpoint pair numerically before assigning first-appearance names 1,2,... . A pattern uses k<=m names. Let b be the number of gates introducing two unseen labels simultaneously; these give disjoint pairs of consecutive canonical names. For an injection phi:[k]->[N], each such pair requires its first image to be smaller than its second. There are exactly

    weight_N(pattern) = (N)_k / 2^b                      (4)

embeddings, zero when k>N. Coordinate swaps on these disjoint pairs give equal numbers for all 2^b orderings. Conversely each embedding satisfying these inequalities recovers exactly that canonical pattern. The naive weight (N)_k is incorrect: already the unique length-two pattern has binom(N,2) embeddings.

Enumerate canonical identity patterns, choose one with weight (4), and choose a uniform constrained embedding. A uniform injection followed by sorting the images within introduction pairs samples the latter law. Pattern probability times embedding probability is the reciprocal total word count. There are O(m^2) extensions at each step, so this costs m^(O(m)) poly(N), with O(m log(N+m))-bit integers. It proves the requested elementary fixed-parameter result and is implemented, but its m=O(log N/log log N) polynomial regime is superseded by the cycle-type theorem.

## Minimal arbitrary endpoints

**Proved.** At m=h=N-cycles(g), every removed first factor must reduce defect, so it splits a cycle. All factors stay within cycles of the original endpoint. Let f_a count minimal factorizations of a specified a-cycle, with f_1=1. The split argument gives a positive integer recurrence

    f_a = sum_{j=1}^{floor(a/2)} s(a,j) binom(a-2,j-1) f_j f_(a-j),
    s(a,j)=a for j<a-j, and a/2 for j=a-j.                (5)

After a split, the two cycles require j-1 and a-j-1 factors, and the binomial counts their interleavings. If g has cycle lengths a_1,...,a_c, its minimal factorization count is

    H(g) = h! product_i f_(a_i) / product_i (a_i-1)!.      (6)

Compute f_a positively, choose each defect-reducing labeled transposition t with weight H(tg), and recurse. The same telescope proves exact sampling. Counts have O(N log(N+1)) bits; a naive implementation has expected bit cost O(N^6 log^2(N+2)). Bounded-randomness modification works as above. No use of the closed formula f_a=a^(a-2), or of Dénes's theorem, is required. For the public identity endpoint this primitive covers only m=0, but it is useful internally.

Pair padding proves feasibility and supplies fallback words. Padding a uniform shorter word does not generally give a uniform longer word; no sampling regime is inferred from padding alone.

## Boundaries and named-method obstruction

* m=0: the empty word is unique if g=e, otherwise the fiber is empty.
* Odd m at identity: empty fiber. Odd lengths at odd endpoints remain covered.
* m=2,g=e,N>=2: choose t uniformly and output (t,t), exactly as the DP does.
* N=2: the only transposition repeated m times is the unique feasible word.
* N=1: only m=0,g=e is feasible. The usual sign-and-defect criterion needs this exception because no padding pair exists. Rank zero is outside the stated input domain.
* m=h: equations (5)-(6) give a separate polynomial exact primitive.
* m=h+2k: padding supplies a witness; uniform sampling uses the stated DP.

**Proved obstruction to explicit full type enumeration.** Let m be even with m<=N, and D=m/2. Every partition of D is a positive midpoint state: it uses at most 2D labels, has a minimal length-D factorization, and its reverse completes an identity bridge. Thus the table has at least p(D) states. For k=floor(sqrt(D)), every subset of {2,...,k}, padded with ones to total D, is a different partition. Consequently p(D)>=2^(k-1) when k>=1. The state count is exp(Omega(sqrt(m))). For m=omega(log^2 N), m<=N, this explicit enumeration is superpolynomial in (N,m). This neither rules out compressed or approximate methods nor proves computational hardness.

## Exact validation and dependencies

Command from the repository root:

    python3 experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/short_exact.py --output experiments/20260905-bridge-length-phase-diagram/roles/r1-short-exact/results.json

Repository commit: 9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc.
Environment: Python 3.12.3, standard library only. The command python was unavailable; python3 was used. Exact arithmetic supplies every distributional check. Seeds 7, 20260905, and 4103 are used only for extra endpoint smoke tests.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| Defect-type DP with labeled lift | Global fixed-length uniform | Yes | Every weighted support class has its exact global mass | Every word at required cases | promote |
| First-appearance patterns | Global fixed-length uniform | Yes | Same exact global support | All embedding weights checked | keep; slower |
| Minimal-endpoint splits | Minimal arbitrary-endpoint uniform | Correct endpoint | Not a local-chain question | All endpoints through S6 | keep |

Required identity counts are 27,120,3936 for S3,m4; S4,m4; S4,m6. Every word has respectively probability 1/27,1/120,1/3936, summing to one. Exact prefix-cycle, per-position-edge, multiplicity, adjacent-repeat, weighted-component, and two-gate-window laws match enumeration. Weighted-component classes number 4,13,17. There are 9,12,392 canonical patterns, with every observed embedding count equal to (4).

Additional checks compare cut/join coefficients against every permutation through S6; every word probability at selected S3/S4 lengths for every feasible endpoint; and minimal-length counts and valid samples for every endpoint through S6. Boundary checks cover all endpoints through S5 at lengths 0,1,2,3,h,h+1,h+2,h+4. A forced-rejection random-bit object confirms fallback endpoint validity. Finite tests support the implementation; the self-contained proofs establish the quantified claims.

No unresolved project classification, Hurwitz transitivity, dense theorem, or imported enumerative theorem is used. Cycle splitting, coefficients, partition estimates, and telescopes are proved above. The coordinator supplied the project source lock; the worker additionally read AGENTS.md, the rank-recursive HANDOFF section, next_steps.tex, target discipline in GOAL_SPEC.md, and the project skill/references. No historical ledger or old run log was consulted. No claim of literature novelty is made.

## First open step and proposed durable patch

There is no unproved step in the fixed-parameter theorem. Extending this route would need the following standalone lemma:

> Given a feasible endpoint type on N labels and a remaining length r, compute its nonnegative integer completion count in time polynomial in (N,r), or directly sample a labeled first transposition from the exact completion-count ratios in that time, without enumerating exponentially many partition states.

The alternatives matter: inability to evaluate exact counts would not prove inability to sample. This is an open step for the present route, not the coordinator's proposed strict component/surplus reduction.

After human review, add the positive defect-type theorem and exact m=O(log^2 N) regime to the direct-sampling discussion, including expected-time exactness and the bounded-time valid-endpoint fallback. Keep the method limitation and the distinction between padding feasibility and uniform sampling. No protected project document was edited.

Artifact inventory: plan.md, checkpoint.md, report.md, short_exact.py, results.json. A fresh nonauthor audit remains the coordinator's responsibility; the finite checks here were authored by R1.

role: r1-short-exact
claim: Positive defect-type DP samples every feasible bridge exactly in exp(O(sqrt(min{m,N}))) poly(N,m) expected bit time; bounded-time sampling has TV error at most epsilon and polynomial overhead in log(1/epsilon).
status: proved
parameter_regime: All feasible N>=2,m>=0,g for the parameterized bound; polynomial at m=O(log^2 N), at fixed N for arbitrary m, or when min{m,N}=O(log^2(N+m)); minimal endpoints separately polynomial.
target_distribution: Uniform on Omega(N,m;g), publicly g=e.
runtime: Expected exact bound (1); bounded approximate bound (1) times O(log(1/epsilon)+log(m+1)+1); explicit length-m output.
error: Zero for exact sampling; at most epsilon for bounded-time sampling; endpoint error always zero.
assumptions: Explicit permutation-map input and independent fair random bits; no unresolved mathematical hypotheses.
evidence: Self-contained proof, short_exact.py, results.json, exhaustive required cases, coefficient checks through S6.
independent_checks: Different finite encodings compare labeled enumeration to the type recurrence; fresh nonauthor proof audit not yet recorded.
first_unproved_step: Removing the partition-state factor while preserving positive completion-ratio sampling in the uncovered regime.
verdict: promote
