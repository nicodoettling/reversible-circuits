# Nonauthor audit of R1-T1.1 and the frozen explicit-stack implementation

**Verdict: ACCEPT R1-C1 through R1-C6 and R1-T1 under the stated fair-random-bit and canonical permutation-array model.** No mathematical or implementation repair is required for the frozen candidate. This acceptance also closes the connected-primitive condition in my earlier `global_audit.md` for the frozen `sample.py` integration. The global consequence remains exact sampling of the declared restricted component family, with its stated omitted-mass error.

The exact review request is preserved in `candidate-audit-assignment.txt`. All five candidate files were copied in full into `candidate-review-input/` after their expected hashes were checked. This is a nonauthor review following an isolated blind construction; agreement of same-model agents is not independent statistical evidence. My own blind report has not been edited.

| reviewed candidate | SHA-256 |
|---|---|
| proof.md, R1-T1.1 | c779902224eaab4ebe2837fbb0d4aaaf9850aa4aede5443cd86259a746f6b9ba |
| sampler.py, actual explicit-stack version | d9f7acf9365199a3a78a805a71307b4945f8babf1f765f77fba1bb10301f270d |
| audit.py | eb2aeffb1e4c4c2efd95245e407257461c8e2f79cb4e541646f6a72d10899930 |
| results.json | 930c2b945168216bbd81b5eaef213140f4b2fc60f470eedd71a1eff336785722 |
| report.md | 8e49c40ea29b2275cc8d4d3937bd8963a5f3c05e5438cbd3c7f79ddabf1d6bbb |

## R1-C1: positive fixed-endpoint formula — ACCEPT / proved

My blind source check already established the fixed-permutation normalization of Vakil §1.2 and Corollary 1.5, directly from the [primary PDF](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf). I did not assume the candidate's additional positive-moment formula from agreement with my own signed implementation. I derived it anew as follows.

Let e_j be elementary symmetric functions of the cycle lengths, v their sum, and S_j the sum over j-subsets of the product of selected lengths times their sum. Expanding v e_j separates the selected lengths from the unselected lengths. Every (j+1)-subset appears j+1 times in the latter term, giving

```
S_j = v e_j-(j+1)e_(j+1).
Q = sum_i a_i(a_i-1)=v^2-v-2e_2.
```

Substitute these identities into the candidate's positive bracket

```
P=v^(k-2)Q + sum_(j=2)^k (j-1)! v^(k-1-j)S_j.
```

The e_2 coefficient is -2+1=-1. For e_l with l>=3, the coefficient is (l-1)!-l(l-2)!=-(l-2)!. The endpoint e_(k+1) vanishes. Thus

```
P=v^k-v^(k-1)-sum_(j=2)^k (j-2)! e_j v^(k-j),
```

which is exactly the checked signed bracket. Every summand in the positive representation is nonnegative; negative powers are powers of positive component sizes and hence positive rationals. This proves the candidate's formula without needing an unchecked graph-encoding multiplicity from Proposition 3.2.

The common factor is product a_i^a_i/(a_i-1)!, including the product a_i needed to turn the source's G count into its fixed-permutation c count. There is no label, cycle-equality, cyclic-shift, conjugacy-class, or position-factorial quotient beyond the one explicitly normalized in C_g/r!. The code's `normalized_count`, `marked_symmetric`, and `count` implement these formulas correctly. Its bounded count cache changes neither the values nor the probability law.

Singleton checks are exact: genus zero gives one empty word; genus one gives zero because Q and every relevant S_j vanish. A single v-cycle gives C_0=v^(v-2). I independently compared all genus-zero and genus-one counts for every integer partition through degree 18: 3,192 formula queries matched my blind signed oracle.

## R1-C2 and R1-C3: genus and deletion bijection — ACCEPT / proved

The join/split calculation is sound. Starting at the identity on v vertices, J joins and S splits give r=J+S and endpoint cycle count k=v-J+S. A factor crossing current support components necessarily joins permutation cycles, so connectivity forces J>=v-1. Therefore g=(r-v-k+2)/2=J-v+1 is a nonnegative integer.

For the last factor tau=(x,y), x<y, the code computes pi=sigma tau by swapping the two entries of sigma. If x,y belonged to different cycles of sigma, the merged pi-cycle contains both vertices; a disconnected predecessor would put them in different components and could not contain that cycle. The predecessor is therefore connected, with unchanged genus. If x,y belonged to the same sigma-cycle, a connected predecessor has genus g-1, and a disconnected predecessor has exactly two components with genera summing to g.

In the disconnected case, the two cut cycles are put first in `cut_cycles`, oriented by x in side A and y in side B. Other cycles are individual labeled objects. Assignments preserve entire cycles, ensuring each component domain is invariant under pi. Child words on disjoint domains commute across the two components, so an interleaving has the prescribed endpoint. Appending tau gives sigma. Every resulting word recovers its final edge, predecessor support components, child subsequences, genera, and position subset uniquely. The binomial interleaving factor is exact, and there is no factor 1/2. Equal cycle lengths do not remove the labels distinguishing the cycles.

The code scans actual transpositions of the current labeled permutation, computes connected and split branches with the corresponding genera, filters zero weights, and checks that the sum is the parent count. This count-sum assertion is a diagnostic; the mathematical normalization comes from the disjoint bijection.

## R1-C4: positive E/S/Q allocation DP — ACCEPT / proved and independently checked

For a fixed tracked side, a table state (size,number) groups assignments with the same tracked total vertex count and cycle count. Its E_j and S_j arrays are sums of the corresponding marked-subset statistics over those assignments; Qsum is the sum of Q. E_0 is the number of assignments. The update when a new cycle of length a joins the tracked side is correct:

- A marked subset either omits the cycle or includes it, giving E'_j=E_j+aE_(j-1).
- In the included case, its old product is multiplied by a and its marked sum increases by a. Consequently S'_j=S_j+aS_(j-1)+a^2E_(j-1).
- Q increases by a(a-1) separately for each assignment, giving Qsum'=Qsum+a(a-1)E_0.

Sending the cycle to the other side copies all tracked quantities. Each free cycle permits both transitions, while an arbitrary forced choice permits only one. Equal-size cycles are processed separately and therefore accumulate the correct multiplicities when state keys collide. At a fixed destination cycle count, the coefficient arrays have the same length, so the implementation's in-place vector addition on a collision is safe.

If side B has genus one, `tracked_side=1` swaps which moments are stored. The remaining side is genus zero and needs only its complementary size and cycle count. A total genus at most one is essential: the argument would not justify a branch with genus one on both sides, which could require mixed moments. The input assertion excludes that case.

The two anchor cycles are always forced to opposite sides, so both component sizes are positive. The factor `(r-1)! product q(a_i)` is allocation independent after cancellation of the interleaving factorials. Multiplying the aggregate moments by the displayed powers therefore gives exactly the sum of the literal branch counts. The genus-one singleton has all positive moment contributions zero and receives zero mass, correctly omitted by the selector.

Fresh checks go beyond comparing completed masses: `candidate_check.py` explicitly enumerates marked subsets and computes each E vector, S vector, and Q scalar directly for every consistent full allocation. It then aggregates them under every partial assignment, including non-prefix constraints, and compares the entire table with `allocation_table` for each tracked side. Across 171 oriented cycle inventories of total size at most eight, all 7,754 full table comparisons pass. On the same forced inputs, 11,631 completed masses match my independently written blind allocation oracle, whose coefficient representation differs from R1's positive moments.

For sequential allocation, the exact sets counted with the next cycle fixed to A and to B partition the current set. Hence w_A+w_B=current_mass on the actual exposed history. The code checks this equality and updates the surviving mass after each decision. The conditional probability of a completed allocation is its literal weight divided by the initial aggregate, by telescoping exact conditional ratios. There is no independence premise about already allocated cycles.

## R1-C5: law, random draws, unranking, and the actual continuation stack — ACCEPT / proved

`randbelow` requests exactly `(bound-1).bit_length()` bits, accepts values below bound, and repeats with fresh bits otherwise. Under the fair-bit model, every accepted value has conditional probability 1/bound, with acceptance greater than one half; bound one requests zero bits and returns zero. `weighted_choice` uses consecutive intervals of the declared nonnegative integer weights. Zero-weight intervals are empty, so impossible branches are never selected.

`unrank_subset` correctly scans positions in increasing order. Its `including=binom(n-i-1,k-1)` counts subsets containing the next position; subtracting it when excluding that position gives the exact next rank. The output is sorted and has exactly k positions. Empty subsets and full subsets are handled. Thus uniform ranks yield uniform interleavings, including zero-length singleton child words.

The executable `sample` has no recursive call to itself. I checked the edited stack mechanics directly:

1. A connected branch pushes an `append` continuation followed by its child `sample` task. LIFO execution completes the child before appending the parent edge.
2. A split pushes `merge`, then the B child, then the A child. Thus A completes first, B second, and `merge` correctly pops B before A.
3. Each child is sampled on the index set of its own sorted vertex list. At merge, the correct `aa` or `bb` map converts local indices back to parent labels. Sorting each transposition's endpoints changes only its representation, not its action.
4. Interleaving is selected after both child words are complete. The two lengths are fixed by the selected branch and allocation, so the uniform subset law is the required conditional law. Fresh unused fair bits after finite rejection stopping remain independent of the exposed choices.

The strong-induction probability calculation is therefore implemented faithfully. In a split branch, the factors are D/C_parent, W/D, 1/C_A, 1/C_B, and the reciprocal interleaving binomial. Their product is 1/C_parent. In a connected branch the child count cancels directly. Every factor is conditional on the selected parent state and allocation; a marginal product bound is neither needed nor used.

To test the actual edited function rather than just its mathematical recursion, I reconstructed exact integer-choice tapes from prescribed target words. Each tape tells the real `sample` call which accepted rank to receive at every branch, allocation choice, and shuffle. The oracle verifies the requested bit width and complete tape consumption. It uses both the first and last integer in every selected branch interval for all S_3 cases and generated S_4 cases. All 588 connected genus-zero/one S_3 words were replayed through the actual function, as were 168 additional target words from my blind sampler on arbitrary endpoints through degree twelve. The 1,488 executions reproduced their prescribed words exactly, covering 11,595 integer-draw calls.

A separate mechanical fixture exercised 1,200 positive-length continuation steps on a degree-600 star-square word. Count, branch, and assignment oracles were explicitly replaced by deterministic fixture oracles; this is **not** a degree-600 performance or distribution test of the real counting algorithm. The real continuation machinery reconstructed the exact 1,200-letter word, reached 1,797 pending tasks, and used exactly one Python `sample` call frame throughout. No interpreter recursion limit was changed. This newly targets the explicit-stack repair; it cannot be inherited from a proof of the former recursive implementation.

## R1-C6: expected bit complexity — ACCEPT / proved

A child degree is at most the initial N and every connected genus-zero/one length is at most 2N. Each positive-length node consumes one factor, and split-child lengths sum to the parent length minus one. Therefore the execution has exactly r<=2N positive-length nodes and singleton base leaves on disjoint vertex sets, at most N in total.

Each allocation table uses O(N^3) scalar storage and O(N^4) arithmetic operations. Enumerating O(N^2) final transpositions costs O(N^6) per node. The selected allocation uses O(N) additional oracle calls and is dominated by that bound. Power and factorial evaluation in the literal Python code does not defeat the bound: the terminal scalar formulas have O(N^3) summands, and even computing each bounded power or factorial in O(N) elementary arithmetic steps stays within O(N^4). Direct count evaluation is also lower order. Concatenating and relabeling output words adds lower-order polynomial work.

Every DP coefficient has O(N log(N+1)) bits by the stated assignment/subset/product bounds. The cycle-local factorial denominators divide N!. Negative exponents in the genus-zero factor are at least -2, and in the genus-one factor at least -1. Thus the proposed universal common denominator 24(N!)^5 is more than sufficient, including the powers contributed by both components. Its bit length is O(N log(N+1)). All positive summands have exp(O(N log(N+1))) magnitudes; partial sums cannot hide unbounded cancellation. Reduced numerator and denominator lengths, and the immediate products before reduction, have the same asymptotic order.

O(N^7) rational operations on B=O(N log(N+1))-bit operands therefore fit the conservative O(N^7 B^3)=O(N^10 log^3(N+1)) schoolbook bound. The random integer calls have fewer than two expected trials and use polynomially many O(B)-bit attempts. No b-dependent approximation is needed. Bounded LRU caches and explicit task/value stacks require polynomial storage; no cache of all endpoints or all cycle subsets is assumed.

The input encoding in this accepted bound is a permutation array on canonical labels [N] (the implementation uses 0,...,N-1). Arbitrary external vertex names can be relabeled, with their input/output encoding cost added if those names themselves have unbounded bit length. This standard representation clarification does not affect frozen target T0.

## Boundaries, negative findings, and regression retention

- N=1 at length two is infeasible; the genus-zero singleton empty word is only an internal base. Genus-one singleton branch mass is exactly zero.
- N=2 at length four has exactly one output; its recursive split into two empty singleton words is correctly counted once.
- Odd identity length is impossible. At m=0 connected support requires one vertex. At m=2 a connected identity word requires N=2.
- S_3,m=4 has 24 connected words among 27 identity words; S_4,m=4 has no connected word; S_4,m=6 has 2880 connected words among 3936. The distinction between all bridge counts and connected counts is maintained throughout.
- The square-free word `((01),(12))^3` and its fourth-vertex square extension retain positive exact probabilities, respectively 1/240 and 1/131040. An adjacent-square-only construction would omit the first word; R1 does not use that construction.
- Counts alone still do not decode a word, prescribed exposed-prefix connectivity is still a different problem, and fixed genus still does not make all endpoint partitions a polynomial inventory. R1 discharges the allocation step explicitly instead of relying on any of those implications.
- R1's positive implementation differs from my blind signed-coefficient method. Their outputs were compared only after the exact R1 files were frozen; shared conclusions were not treated as automatic implementation certification.

No counterexample or implementation failure was found in this frozen version. No negative finding from the received candidate was discarded after the stack repair. The CP-1 marginal-product obstruction remains rejected; the accepted law uses explicit conditional masses and does not make the premise CP-1 falsifies.

## Clean rerun and artifacts

Python 3.12.3; standard library only. No package installation, global configuration change, network computation, or shared-file edit was used. Primary-source browsing was read only. Commit and intake dirty state remain recorded in `provenance.json`; both audit requests and every frozen review input are preserved in this role directory.

Fresh nonauthor check:

```
timeout 60s python3 -B experiments/20260907-genus-one-sampler/roles/r3-referee/candidate_check.py
```

Output: `candidate-check-results.json`; recorded runtime 1.187 seconds. The seed-dependent target generation uses 17,101,20260907 only for validity/replay diversity; the full moment, count, and literal-word checks are deterministic exact comparisons.

I also reran the supplied exhaustive audit in a fresh process from the copied, hash-verified candidate directory:

```
cd experiments/20260907-genus-one-sampler/roles/r3-referee/candidate-review-input
timeout 60s python3 -B audit.py --forced-max 10 --endpoint-max 6 --word-max 4 --output ../candidate-author-audit-rerun.json
```

All stages passed in 13.924 seconds. This reproduces the 112,698 forced-assignment queries, all 1,745 arbitrary-endpoint comparisons through S_6, and the complete small-word reconstruction and probability checks. The X_4 digest is unchanged at `b8ca6359bda6e14f7edc5684871948e647da99898dc556f03e9895abf84a1f87`. The rerun's full raw output is preserved, rather than replaced by this summary. Running the author's checks is a clean reproducibility check; the separate nonauthor moment tables and actual-stack replays are the newly targeted evidence.

## Final claim ledger

| claim | status | assumptions | evidence | action |
|---|---|---|---|---|
| R1-C1 | ACCEPT / proved | checked Vakil fixed-endpoint formula | independent telescoping derivation; 3,192 formula comparisons | retain |
| R1-C2 | ACCEPT / proved | finite transposition words and stated convention | join/split and support-component argument | retain |
| R1-C3 | ACCEPT / proved | canonical endpoint labels; connected support | unique inverse deletion/reconstruction | retain |
| R1-C4 | ACCEPT / proved | total genus <=1; forced opposite anchors | full moment-vector comparisons and blind-oracle cross-checks | retain |
| R1-C5 | ACCEPT / proved | independent fair bits; positive target count | exact conditional law; 1,488 actual-function tapes; deep stack fixture | retain |
| R1-C6 | ACCEPT / proved | binary permutation-array model; exact rational arithmetic | operation, denominator, cache and stack bounds | retain |
| R1-T1 / frozen T0 | ACCEPT / proved | R1-C1–C6, no new hypothesis | complete proof and fresh audit | coordinator may promote exact frozen version |
| frozen sample.py integration | ACCEPT under the same randomness model | accepted R1 primitive and global G1-COUNT | previous boundary tests plus now-accepted unranking and primitive | close earlier conditional implementation gate |

**First unproved step:** none identified for the exact frozen theorem and model. This acceptance does not certify a future edited dependency, higher-genus primitive, all-length global sampler, local-chain gap, or polynomial cost in log N. The coordinator retains final responsibility for synthesis and any changed final artifact.
