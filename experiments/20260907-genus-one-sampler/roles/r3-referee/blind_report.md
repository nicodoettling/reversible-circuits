# Frozen blind report: an exact sampler via connected deletion and cycle-allocation DP

**Mathematical verdict: proved, using the checked published genus-zero/one fixed-endpoint counting theorem stated below. Audit disposition: PROVISIONAL / keep for nonauthor review.** This is a complete independently derived candidate construction, not an acceptance of an unseen coordinator proof. No unresolved mathematical step was found in this derivation. Final project certification still requires another reviewer to check the exact argument.

## Input and scope

The exact assignment is preserved in `operational-assignment.txt`; the complete frozen mathematical brief is preserved byte for byte in `blind-brief.md`. This agent was spawned with `fork_turns=none`. Its context excluded the coordinator's argument, other workers' reports, and claimed outcome. The general repository guide and the expressly permitted skills were read for standards. No HANDOFF, historical research report, old mathematical verdict link, coordinator summary, or other role artifact was inspected before this report was frozen. Standards documents contained old project facts, but none is used here. Same-model review is not independent statistical evidence.

The target is exactly T0: for each integer N>=2, return an ordered length-2N word of transpositions on labeled [N], whose product is identity and whose support graph is connected, with the uniform law. Rightmost displayed factors act first. Repeated edges are allowed. A fair-random-bit algorithm with expected running time polynomial in N suffices; it has total variation error zero and therefore meets every positive integer precision parameter b. This polynomial bound is in N, not in log N or the number of wires.

The internal problem is uniform **connected** factorization of an arbitrary endpoint permutation sigma, at genus g in {0,1}. It never replaces a connected factorization count by an unrestricted bridge count. No Markov chain, laziness parameter, stationarity, or spectral-gap claim is involved.

## Claim B1: the counted internal family — proved

Let V be a nonempty labeled vertex set of size d, let sigma be a permutation of V with k cycles, and put r=d+k+2g-2. Write C_g(sigma), or C_g(alpha), for the number of ordered r-tuples of transpositions on V with product sigma and connected support, where alpha lists the k cycle lengths. Cycles of equal size are distinct cycles of the fixed labeled permutation. Empty words are permitted only for the singleton, identity, genus-zero base case.

Connectivity of the transposition graph is equivalent to generation of the full symmetric group on V. Every generator preserves every graph component. Conversely, transpositions along a connected graph generate every transposition by conjugating along paths. Thus the source's transitivity condition agrees with our support condition.

Every connected factorization has a nonnegative integer genus g=(r-d-k+2)/2. To see this without topology, as factors are appended let J be the number of mergers of permutation cycles and S the number of splits. Then r=J+S and k=d-J+S, giving g=J-d+1. At least d-1 factors merge previously distinct support components; each such factor also merges permutation cycles because permutation cycles lie inside support components. Hence J>=d-1. This also proves the parity and minimal-length restrictions used below.

## Claim B2: exact fixed-endpoint counts — proved published input, source checked

For a cycle-length list alpha=(a_1,...,a_k), let d=sum a_i, and let e_j(alpha) be its elementary symmetric polynomial, with e_0=1. Define

```
Q(alpha) = product_i a_i^(a_i)/(a_i-1)!
F_0(alpha) = d^(k-3)
F_1(alpha) = [d^k - d^(k-1)
              - sum_(j=2)^k (j-2)! e_j(alpha) d^(k-j)] / 24.
```

Then

```
C_g(alpha) = (d+k+2g-2)! Q(alpha) F_g(alpha),   g=0,1.       (1)
```

This is Corollary 1.5 after the normalization in §1.2 of [Vakil's primary paper](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf): its displayed G count must be multiplied by product_i a_i to obtain its fixed-permutation c count. No extra factorial or automorphism divisor is inserted. Reversal of a transposition word inverts its endpoint, so a difference in displayed multiplication order does not change this cycle-type count. The algorithm itself uses sigma t when removing a rightmost transposition.

For d=k=1, (1) gives C_0=1 and C_1=0. Negative powers in F_0 are exact rationals; they occur only at k=1 or 2. F_1 is written above without negative exponents. The apparent subtraction in F_1 is handled by exact arithmetic; its individual summands are not treated as probabilities.

## Claim B3: a disjoint deletion decomposition — proved

Consider a nonempty connected factorization w with product sigma and last transposition t=(a,b), choosing the orientation a<b once and for all. Let u be the prefix and rho=sigma t. There are exactly the following possibilities.

1. **a and b belong to different cycles of sigma.** Multiplication by t joins those cycles, so rho has k-1 cycles. The support of u must remain connected. If u had two components, t would join a cycle from each, making a and b belong to the same cycle of sigma, a contradiction. Its genus is g. The number of words in this branch is C_g(rho).
2. **a and b belong to the same cycle of sigma, and u is connected.** Multiplication by t splits that cycle into two cycles of rho, and rho has k+1 cycles. The prefix has genus g-1. This branch exists only when g=1 and has weight C_0(rho).
3. **a and b belong to the same cycle of sigma, and u is disconnected.** Removing one edge from a connected multigraph creates at most two components, and this case has exactly two. Let the component A contain a and B contain b. The two cycles produced by the split lie in A and B respectively, anchoring this ordered pair of components. Every other cycle of rho lies wholly in one component and may be assigned to either side.

For any assignment, let alpha_A,alpha_B be the respective cycle lists, d_A,d_B their vertex counts, k_A,k_B their cycle counts, and g_A,g_B the genera of their connected factor subwords. Their lengths are

```
r_A=d_A+k_A+2g_A-2,   r_B=d_B+k_B+2g_B-2.
```

The equality r_A+r_B=r-1 is equivalent to g_A+g_B=g. Both genera are nonnegative, so the possibilities are only (0,0) for g=0 and (1,0),(0,1) for g=1. The exact number of prefixes for this assignment and genus choice is

```
binom(r-1,r_A) C_(g_A)(alpha_A) C_(g_B)(alpha_B).           (2)
```

Indeed, choose a connected word on each side, then choose the positions occupied by A's letters. Since A and B are disjoint vertex sets, their transpositions are disjoint types and commute across sides. The resulting prefix has exactly the desired two components and endpoint rho. Its two subwords and interleaving can be recovered uniquely from the prefix. Appending t connects the support and produces sigma. This proves both surjectivity and multiplicity one.

The orientation a<b prevents double counting the two components. Equal cycle lengths do not permit quotienting cycles: their labeled vertex sets remain distinct. The connected and disconnected cases are disjoint. Thus the sum of all branch weights is exactly C_g(sigma), by a combinatorial partition of the family, independently of numerical checks of (1).

## Claim B4: polynomial evaluation of every allocation mass — proved

A naive implementation of case 3 enumerates 2^(k-1) allocations. The following explicit DP avoids that enumeration.

Fix the endpoint rho, the two anchored cycles, a genus pair with total at most one, and any additional cycles already forced to sides A or B. Write L and R for the nonempty lists of cycle lengths already forced to A and B, and U for the distinct undecided cycles. Let alpha_all be the concatenated list L,R,U, with total size d and cycle count K. Let M(L,R,U;g_A,g_B) be the sum of (2) over all remaining allocations. Set

```
s = r_A+r_B = d+K+2(g_A+g_B)-4.
```

Substituting (1) into (2) cancels both child factorials against the binomial coefficient. Therefore

```
M = s! Q(alpha_all)
      sum_allocations F_(g_A)(alpha_A) F_(g_B)(alpha_B).    (3)
```

The factor outside the sum is independent of the allocation. At most one component has genus one. This is the decisive simplification.

Process the undecided cycles in a fixed deterministic order. For each possible total A-size x and A-cycle count q among the processed and forced cycles, store two coefficient vectors

```
A_(x,q)(z) = sum_consistent_assignments product_(c in A)(1+|c|z)
B_(x,q)(z) = sum_consistent_assignments product_(c in B)(1+|c|z).
```

Both constant coefficients equal D_(x,q), the number of assignments in that state. Initialize the one state (sum L, |L|) with the polynomials for L and R. For a free cycle of size v:

- Assigning it to A sends (x,q) to (x+v,q+1), multiplies A(z) by (1+vz), and leaves B(z) unchanged.
- Assigning it to B leaves (x,q) unchanged, leaves A(z) unchanged, and multiplies B(z) by (1+vz).
- Add vectors when destinations coincide.

These are exact counting identities for distinct cycle assignments, including repeated lengths. Each coefficient vector has degree at most d, and there are O(d^2) states. Processing at most d cycles takes O(d^4) integer operations and O(d^3) storage. Forced cycles can be arbitrary; they only alter the initial state and polynomials.

At the end, the B-size and cycle count are y=d-x and p=K-q. If both genera are zero, the state's contribution to the sum in (3) is

```
D_(x,q) x^(q-3) y^(p-3).                                  (4)
```

If A has genus one, its aggregate F_1 over all assignments in that state is

```
H_A = [D_(x,q)(x^q-x^(q-1))
       - sum_(j=2)^q (j-2)! [z^j]A_(x,q)(z) x^(q-j)] / 24. (5)
```

The state contributes H_A y^(p-3). If B has genus one, exchange A and B in (5) and multiply by x^(q-3). Formula (5) uses linearity of F_1 in the elementary symmetric coefficients. It would not suffice for a hypothetical case in which both components had genus one, because cross moments would then be needed; that case is excluded by g_A+g_B<=1.

Equations (3)–(5) give an exact rational expression equal to the nonnegative integer allocation count M. This includes M=0, notably when a singleton component is required to have genus one. There is no numerical approximation or cancellation-error assumption.

## Claim B5: exact random choices and conditional allocation law — proved

Let W=C_g(sigma)>0 for the current internal problem. Enumerate the O(d^2) possible last transpositions and the at most three applicable case/genus branches for each. Give each connected branch its child count, and each disconnected genus branch the value M from B4. Choose a branch with probability equal to its nonnegative integer weight divided by W; omit zero-weight branches.

For a chosen disconnected branch, let L,R,U be its current allocation state. If c is the next undecided cycle of size v, define

```
M_A=M(L+[v],R,U\{c};g_A,g_B),
M_B=M(L,R+[v],U\{c};g_A,g_B).
```

The exact partition of the assignment set gives M_A+M_B=M(L,R,U;g_A,g_B). Conditionally on every positive-mass revealed allocation prefix, send c to A with probability M_A/(M_A+M_B), or to B with the complementary probability. A zero-mass alternative is never selected. Recompute this same polynomial-time oracle for each of at most d cycles.

After the allocation is complete, the probability of that allocation conditional on the chosen branch is exactly (2)/M_initial: the product of these **conditional ratios** telescopes. This statement does not multiply marginal probability bounds or assert independence after conditioning. The filtration consists of the selected last-edge branch and the actual sequence of cycle-side choices; each denominator is the mass remaining on that precise positive-probability history.

Recursively sample the two child connected words using fresh fair bits, then choose a uniform interleaving of their lengths. One exact interleaving implementation chooses an A-letter with probability a_remaining/(a_remaining+b_remaining) at each position. Every completed binary interleaving has probability r_A!r_B!/(r-1)!, including cases where a subword is empty. Append t.

Integer-weight selection uses only fair random bits. To draw uniformly below a positive integer H, take ceil(log_2 H) bits and reject numbers at least H, using zero bits when H=1. The acceptance probability is greater than one half (one at powers of two); conditioned on acceptance every value has probability 1/H. Independent new bits make the number of trials geometric with mean below two. Cumulative sums then select a weighted branch. This is a finite-support conditional-law calculation, not a real-arithmetic oracle.

## Claim B6: complete algorithm and exact uniformity — proved

```
SampleConnected(sigma,g):
    require g in {0,1}, a nonempty labeled domain, and C_g(sigma)>0
    r := d + number_of_cycles(sigma) + 2g - 2
    if r=0: return the empty singleton word
    enumerate last-edge branches and compute their exact weights
    select one by its weight / C_g(sigma)
    if it is connected:
        return SampleConnected(sigma*t, child_genus) followed by t
    otherwise:
        allocate the remaining cycles using the conditional masses from B5
        sample the two child connected words on their actual labeled domains
        interleave them uniformly and append t

SampleT0(N):
    if N=1: report infeasible
    return SampleConnected(identity_on_[N], 1)
```

Prove correctness and uniformity by strong induction on the word length r. The singleton base has its unique law. In a connected branch, an individual output word has probability (C_child/W)(1/C_child)=1/W. In a disconnected branch, write m for its aggregate mass and a for the selected allocation weight (2). The unique decomposition from B3 gives an individual output word probability

```
(m/W) * (a/m) * (1/C_A) * (1/C_B) * (1/binom(r-1,r_A))
 = 1/W.
```

The child probabilities are conditional on the exact branch and allocation, and their random tapes are fresh. Every multiplicative factor is therefore the required conditional probability. Zero counts never occur on a selected branch. Every recursive child has smaller word length, so the induction is well founded. B3 proves that every word in the target has exactly one representation in this calculation, and that all produced words have the correct endpoint and connected support. Thus the law is exactly uniform and normalized.

The CP-1 cached-prefix regression does not target an assumption made here: there is no cache, oracle transcript, marginal-lightness estimate, or transfer of an observation. The proof's sequential products are explicit conditional mass ratios and exact induction identities. Dedicated finite-support tests below check those identities directly.

## Claim B7: expected bit complexity — proved, conservative bound

All quantities are represented by exact integers or reduced rational pairs in binary. N is the maximum domain size. All child lengths are at most the initial 2N. Precompute factorials through 2N and powers d^j for 1<=d<=N, 0<=j<=N. At one recursive call:

- There are O(N^2) candidate last edges and O(1) branch types per edge.
- An allocation mass needs O(N^4) arithmetic operations; thus all branch weights need O(N^6).
- Sampling an allocation needs at most N additional forced-allocation queries, giving O(N^5), already dominated.
- Child relabeling, endpoint updates, and shuffling cost lower-order polynomial work.

Each nonbase call consumes one output transposition; at a split, child lengths sum to r-1. Hence there are exactly 2N nonbase calls for T0 and at most 2N+1 base leaves. Total arithmetic work is O(N^7).

The bit lengths are polynomial, not unit-cost assumptions. Every word count is at most binom(N,2)^(2N). Polynomial-DP coefficients count at most 2^N assignments, with elementary coefficient sums bounded by 2^N product_i(1+a_i)<=4^N. Factorials and powers used in (1)–(5) have O(N log(N+1)) bits. The rational denominators cause no exponential blowup: Q has denominator dividing N!, and each negative power in F_0 has exponent at least -2. Every term in an allocation sum has denominator dividing

```
Delta_N = 24 (N!)^5.
```

This common denominator also bounds denominators of partial sums after reduction. Numerators are bounded by the term magnitudes times Delta_N and a polynomial number of states, so all intermediate reduced operands have B=O(N log(N+1)) bits. Immediate products before reduction have the same asymptotic bound.

Even using schoolbook integer arithmetic and the coarse O(B^3) bound for rational reduction, the deterministic arithmetic uses O(N^7 B^3)=O(N^10 log^3(N+1)) bit operations. Weighted random draws use O(B) expected bits each and fewer than two expected trials; there are polynomially many of them. Therefore the complete sampler has a conservative expected bit bound O(N^10 log^3(N+1)), with polynomial space. No attempt is made to optimize this bound. Its dependence on b is constant because the output law is exact.

## Boundaries and falsification attempts

**Proved boundary classifications.** For N=1, T0 would require length two, but no transposition exists, so it is infeasible. The internal singleton genus-zero empty word is valid and must not be confused with T0 at N=1. For N=2, every transposition is (1,2), and T0 has exactly the unique fourfold repetition. For N=3, T0 has 240 words: all 243 length-six identity words except the three words repeating one edge six times. Odd-length identity words are impossible by sign. At length zero, connected support is possible only on a singleton. At length two, connected identity support is possible only for N=2. For N>=2 the length-2N target is nonempty: take each edge of a spanning star twice consecutively, then append any transposition twice. Minimum connected identity length 2N-2 follows from B1 and is attained by the same star construction before appending the extra pair.

**Refuted substitution: connected counts equal unrestricted bridge counts.** On S_3, a fixed transposition has 81 length-five factorizations, but only 80 connected ones. The all-same-edge word is the missing disconnected factorization. The distinction is already necessary in a genus-one internal endpoint problem.

**Refuted representation shortcut: choose the connected simple support graph uniformly.** On S_3 at length six, each of the three two-edge trees supports 20 connected identity words, while the complete graph supports 180. Uniform choice among these four graphs would give the complete graph probability 1/4; the desired word law gives it 3/4. The exact histogram is in `law-results.json`. This does not refute any correctly weighted graph/map bijection.

**Rejected incomplete argument: a closed total Hurwitz count supplies a sampler.** A total count alone omits conditional completion counts. The present proof supplies a separate connected deletion bijection and the forced-allocation DP. Likewise, a raw cut-and-join recursion enumerating all cycle assignments may be exponential; the polynomial bound depends specifically on B4.

**Rejected probability shortcut: sample signed formula terms as mixture components.** The genus-one formula has subtractions. Only its complete nonnegative integer branch counts are sampled. Exact cancellation does not itself establish a positive combinatorial mixture of summands.

No failed sampler is treated as a hardness result. No finite count or successful test is used as an asymptotic mixing argument.

## Exact finite checks and implementation evidence

All checks use the standalone `check.py`, written in this role directory without importing another project implementation. Python is 3.12.3; no nonstandard dependencies were used. `provenance.json` records commit 20e86f665f69053031fe7eec0c3388458affb1fc and the dirty intake state. Exact commands are in `commands.log`. Each command had a 60-second external timeout and completed in less than one second in the recorded runs.

1. **Allocation DP:** every integer partition of every total size 2 through 8, every pair of distinct anchor cycles (including equal sizes), and genus pairs (0,0),(1,0),(0,1): 1,008 exact cases matched an explicit subset sum. Every available one-cycle conditioning split also satisfied M=M_A+M_B. See `allocation-results.json`.
2. **Endpoint and last-edge branch counts:** an independent DP over the actual endpoint permutation and support partition counted every word length from 0 through 2N, for 1<=N<=5. All positive connected genus-zero/one endpoint instances matched (1), and all last-edge connected/disconnected aggregate branches matched B3/B4. There were 305 positive endpoint/genus instances and 3,409 nonzero last-edge branches. The disconnected comparison sums the two possible genus placements; it does not separately observe their lengths in that reference DP. The subset oracle test separately verifies individual genus placements. See `count-results.json`.
3. **Exact induced laws:** for S_3, all 588 connected words in the genus-zero/one endpoint families at lengths 1 through 6 had the exact algorithmic probability 1/C_g(sigma), reconstructed using its branch choice, sequential allocation ratios, recursive child laws, and shuffle probability. Each of the 12 endpoint/genus laws summed to one. All three disconnected length-six identity words had probability zero. The target law gives probability 1/240 to every member of X_3. Also checked every integer-sampling acceptance support H=1,...,256 and all 511 binary shuffles of total length up to eight. See `law-results.json`.
4. **Prototype support smoke tests:** for every N=2,...,8, three samples under each of seeds 17,101,20260907 (63 words total) all had length 2N, identity endpoint, and connected support. This is only an implementation-support check using Python's deterministic PRNG, not a claim of fair-bit exactness or empirical evidence of uniformity. The mathematical algorithm and the exact-law calculation use the fair-bit model. See `sample-results.json`.

The exact reference counts include the required small cases:

| N | length | all identity words | connected identity words |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | 4 | 1 | 1 |
| 3 | 4 | 27 | 24 |
| 3 | 6 | 243 | 240 |
| 4 | 4 | 120 | 0 |
| 4 | 6 | 3936 | 2880 |
| 4 | 8 | 140160 | 131040 |
| 5 | 10 | 169271260 | 142732800 |

The full X_3 diagnostic output records per-position edge frequencies, edge multiplicities, adjacent repeats, prefix cycle types, connected simple support graphs, and every window product type for lengths 2 through 5. Every position gives each transposition count 80 out of 240. There is a single weighted support component ([3],6) under T0 by definition. This direct sampler has no within-orbit restriction; it targets every member of the connected family through the proved unique recursion. No assertion about the number of Hurwitz orbits is needed.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| connected deletion with genus-zero/one cycle-allocation DP | Unif(X_N), exact fair-bit model | proved; finite checks pass | direct full-family sampler; orbit classification unnecessary | counts through N=5; all S_3 laws; allocations through size 8 | keep / promote candidate for nonauthor audit |

## Dependency ledger and first unproved step

| claim | status | assumptions | evidence/artifact | independent check | action |
|---|---|---|---|---|---|
| B1: connected genus domain | proved | finite transposition words, stated product convention | elementary cycle-merger proof above | boundary enumeration | retain |
| B2: exact genus-zero/one counts | proved published input; scope and normalization checked | Vakil Corollary 1.5 and §1.2 | source-checks.md, equation (1) | direct endpoint/support DP through S_5 | retain as named dependency |
| B3: deletion is disjoint and multiplicity one | proved | B1, endpoint rho=sigma t | explicit inverse decomposition above | all small last-edge branches | retain |
| B4: allocation oracle is polynomial | proved | B2; g_A+g_B<=1 | equations (3)–(5), exact coefficient DP | 1,008 subset comparisons | request nonauthor arithmetic review |
| B5: conditional laws are normalized | proved | positive current integer mass; fair independent bits | exact conditional-ratio and rejection calculations | exact finite laws and shuffle tests | retain |
| B6: recursive sampler is uniform | proved relative to named published input | B1–B5, no new hypothesis | strong induction and unique representation | all 588 S_3 family words | request nonauthor full-proof review |
| B7: expected polynomial bit cost | proved with conservative bound | binary exact arithmetic, fair bits | operation and denominator bounds | implementation smoke tests are only diagnostics | request nonauthor complexity review |
| T0 | proved by this construction; audit PROVISIONAL | B1–B7 | this frozen report and prototype | no nonauthor review yet | coordinator to audit exact version |

**First unproved mathematical step:** none identified after accepting the explicitly checked published formula B2 as a standard theorem. **First uncompleted certification obligation:** a nonauthor must inspect the exact allocation-DP derivation, disjoint decomposition, and bit bound. If B2 is unavailable or its normalization is rejected, the downstream theorem is conditional on that precisely stated counting input; finite checks cannot replace it.

## Manuscript-ready candidate paragraph, pending nonauthor certification

The uniform law on connected identity transposition words of length 2N admits an exact sampler in expected time polynomial in N in the fair-random-bit model. More generally, connected transposition factorizations of a fixed endpoint can be sampled exactly at genus zero or one. Deleting the last transposition leaves either a connected factorization of genus at most one or two connected factors whose genera sum to the original genus. The genus-zero and genus-one Hurwitz formulas make each two-factor allocation weight a product of cycle-local factors and a function linear in one component's elementary symmetric polynomials. A dynamic program over component size, cycle count, and symmetric-polynomial degree computes and conditionally samples all labeled cycle allocations in polynomial bit time. Exact weighted choices, recursive sampling, and a uniform interleaving then give a multiplicity-one uniform construction.

This paragraph states the candidate result justified above; it must not be copied into a final accepted manuscript solely on this author's own verdict. The report is ready for the required nonauthor audit.
