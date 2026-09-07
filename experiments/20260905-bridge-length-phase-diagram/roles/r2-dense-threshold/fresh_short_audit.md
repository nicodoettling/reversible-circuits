# Fresh nonauthor audit of R1 short exact sampling

Auditor: R2 dense-threshold worker, after finalizing the separate dense theorem. Audited source: `../r1-short-exact/report.md`, author-frozen 2026-09-05 15:33 UTC, read before `../r1-short-exact/short_exact.py`. Audit date: 2026-09-05 UTC. The auditor did not author or edit either R1 file.

**Verdict: ACCEPT**, with the exact scope below. No mathematical or implementation objection requiring revision was found. This is an independent internal audit, not a claim of external certification or novelty.

## Accepted theorem and scope

The positive defect-type dynamic program samples every feasible prescribed-endpoint transposition bridge exactly in expected bit time

```
exp(O(sqrt(min{m,N}))) poly(N,m).
```

The explicit conservative bound (1) in the R1 report is supported by the described arithmetic and inventory. The sparse uniform-polynomial regime includes `m<=A(log N)^2` for each fixed constant `A`; more generally it includes `min(m,N)=O(log^2(N+m))`. Exactness assumes independent fair random bits and has an expected-runtime qualification. The bounded-trial modification has worst-case bounded running time with the stated logarithmic precision overhead, TV error at most the requested epsilon, and zero endpoint or length error.

The separate canonical-pattern sampler is exact for identity endpoints, with weight `(N)_k/2^b`, and has the stated `m^(O(m)) poly(N)` bound. The separate minimal-endpoint splitting sampler is exact and polynomial for `m=N-cycles(g)`.

The exponential inventory lower bound is accepted only for the explicitly enumerated full type table, in the stated even-length regime `m<=N`. It is not computational hardness, and none is inferred. The public identity specialization of the minimal-endpoint result is only `m=0`.

## Independent proof reconciliation

| Claim | Audit finding |
|---|---|
| Defect cone for arbitrary endpoint | Accepted. Removing first factors gives residual `r_i=t_i...t_1 g`, with defect at most `h+i` and remaining completable length at most `m-i`. Starting from any type inside the cone, any subsequent path automatically obeys the forward bound; a successor outside the remaining-length bound has zero completion count. Thus cone truncation does not silently discard valid suffixes, even for non-involutory endpoints. |
| Positive cut/join coefficients | Accepted. Distinct-cycle joins select two cycles and their endpoints; equal lengths require the binomial cycle-pair factor. Unequal cycle splits have `a` unordered edges per cycle and equal halves have `a/2`. Contributions to the same output type must be added, as the implementation does. |
| Counts refer to one labeled permutation | Accepted. The recurrence is equivariant under conjugacy and gives completions from a fixed permutation of each type. No class-size factor belongs in it. Lifting by choosing an individual labeled transposition is therefore correct. |
| Product convention and exactness | Accepted. At termination `t_m...t_1 g=e`; inversion gives `g=t_1...t_m`. The labeled transition probabilities telescope to the reciprocal exact bridge count. |
| Partition inventory upper bound | Accepted. Defect partitions are in bijection with full cycle types after including the fixed-point count. The Euler-product coefficient bound applies to the cumulative partition count as written. The extra cap by `p(N)` is valid. |
| Enumeration overhead | Accepted. Partitions of `D+1` inject into the allowed type set by padding with the fixed number `N-D-1` of singleton cycles; their defects are at most `D`. This justifies charging generation of all partitions through `D` to `(D+1)S(N,D)`. |
| Explicit bit complexity | Accepted as a conservative implementation-independent bound. Counts have `O(m log N)` bits and transitions have `O(log N)`-bit weights. Sorted type lookup, key construction, elementary arithmetic, and labeled-transposition scans fit the polynomial slack in `(m+1)^3[(D+1)^4S+N^3]ell^2`. Using a deterministic sorted lookup instead of Python hashing preserves the theorem's bound. |
| Growing-length regime | Accepted with quantifiers preserved. The implicit constant in `m<=A(log N)^2` is fixed independently of `N`; the resulting polynomial degree may depend on `A`. `N^(O(m))` is nowhere substituted for a uniform polynomial claim. The precision-aware sufficient regime is also correct because its complexity variables include `b=ceil(log2(1/epsilon))`. |
| Active-label bound | Accepted without a component-classification dependency. A label occurring only once cannot be fixed by the whole product; hence an identity word uses at most `m` active labels. |
| First-appearance correction | Accepted. Each simultaneous introduction of two names enforces one order inequality on their images. These pairs of coordinates are disjoint. The free coordinate-swap action has orbit size `2^b`, yielding precisely `(N)_k/2^b`; single-new-label gates impose no comparison with earlier labels. |
| Minimal endpoint recurrence | Accepted. The first transposition must split a cycle. The split multiplicity and the binomial interleaving of the two residual cycles give recurrence (5), including equal halves. Independent endpoint cycles interleave with the multinomial in (6). No unverified Cayley or Dénes formula is required. |
| Bounded-randomness fallback | Accepted. Conditional acceptance of the finite integer draw is uniform; its rejection probability after `R` trials is at most `2^-R`. Coupling to the unbounded exact sampler and returning a valid deterministic original-input word on any cap failure gives the union-bound TV guarantee. There is no postselection on successful completion. |
| Named-method obstruction | Accepted in its exact regime. For `m=2D<=N`, every partition of defect `D` occurs at a positive midpoint. Subsets of `{2,...,floor(sqrt D)}` padded with ones give the stated elementary exponential lower bound. Since `log(N+m)=Theta(log N)` when `m<=N`, the claimed superpolynomial inventory consequence follows. |

No proof depends on the dense theorem, a local-chain mixing result, Hurwitz classification, or an imported enumerative formula. Boundary handling is correct for zero length, odd identity length, length two, degree two, minimal arbitrary endpoints and pair padding; degree one is explicitly isolated.

## Independent exact checks

The auditor implemented new reference calculations in `fresh_short_audit.py`. The reference counts use labeled-permutation endpoint DP and a separately implemented map product and cycle decomposition, not the author's type recurrence. The canonical reference orders labels by first appearance time with numerical tie breaking, instead of the author's streaming implementation.

Exact command from the repository root:

```
python3 experiments/20260905-bridge-length-phase-diagram/roles/r2-dense-threshold/fresh_short_audit.py
```

Environment: repository commit `9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc`, Python 3.12.3, standard library only, deterministic arithmetic, no random seeds. Machine-readable results are in `fresh_short_audit_results.json`.

All checks passed, with zero failures:

- 873 cut/join coefficient checks, one for every permutation through degree six.
- 3,547 exact endpoint-count checks over degrees one through six and lengths zero through ten.
- 90,743 comparisons of **every included cone-layer type count** against unrestricted labeled completion counts. This directly tests the potentially subtle arbitrary-endpoint truncation.
- 873 minimal-endpoint counts compared against independently computed labeled counts.
- Every word at `(N,m)=(3,4),(4,4),(4,6)`, including all feasible endpoints: respectively 81, 1,296 and 46,656 words. Every claimed word probability was exactly the reciprocal labeled count.
- All canonical identity-pattern weights at those instances: 9, 12 and 392 patterns, with identity totals 27, 120 and 3936. The independent observed embedding counts equaled `(N)_k/2^b` exactly.
- Every one of 336 finite random tapes in bounded-trial `S_3,m=2` instances with `accuracy_bits=0,1,2`. The resulting exact TV errors were respectively `1/24`, `1/96` and `1/384`, and every output had the correct endpoint. These match the independently calculated accepted-uniform-plus-fallback mixture.
- The raw-partition generation charging inequality and the midpoint support inclusion for all `2<=N<=30` and `0<=D<N`.

These checks are finite falsification attempts. The universal conclusions rely on the reconciled proof above.

## Objections and remaining limitations

Numbered mathematical objections requiring revision: **none**.

The accepted theorem remains an FPT/subexponential-state algorithm, not an all-length polynomial algorithm. Exact sampling may run beyond every deterministic time bound because of rejection of random-bit integers; the separately proved capped version supplies bounded running time with statistical error. Explicit enumeration becoming superpolynomial is a limitation of this implementation and does not imply a barrier for different exact or approximate samplers.

The Python implementation is a transparent research implementation. The bit theorem permits ordinary equivalent finite data structures for deterministic lookup; the audit does not claim that every Python interpreter operation has the stated abstract bit cost without that translation.

role: r2-fresh-r1-audit
claim: The final R1 defect-type, canonical-pattern and minimal-endpoint claims are accepted with their stated expected-time/accuracy qualifications and method-specific obstruction scope.
status: proved
parameter_regime: All feasible N>=2,m>=0,g for the FPT bound; uniform polynomial regimes and minimal-endpoint specialization exactly as in R1 report.
target_distribution: Uniform prescribed-endpoint transposition bridge; canonical patterns specialize to identity endpoints.
runtime: Accepted R1 bound (1), its exp(O(sqrt(min(m,N)))) summary, and stated bounded-trial logarithmic overhead.
error: Exact sampler TV zero; capped sampler TV<=epsilon; endpoint and length error zero.
assumptions: Explicit permutation maps, independent fair random bits, elementary arithmetic model with polynomial-bit integers.
evidence: Independent proof reconciliation plus fresh_short_audit.py and fresh_short_audit_results.json.
independent_checks: 90,743 cone-layer checks, exhaustive required per-word cases, exact canonical weights, minimal counts and finite random-tape output laws.
first_unproved_step: Removing the partition inventory while preserving positive completion-ratio sampling outside the proved polynomial regimes.
verdict: accept
