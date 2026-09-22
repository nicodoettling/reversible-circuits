# R3 restricted sampling theorem — R3-S1.v3

Status: **proved by author, provisional pending current-version nonauthor audit**. This is an exact restricted-law implementation theorem. It does not assert the uniform negligible omitted-mass bound required by global T0. The coordinator and analytic workers own that separate obligation. Products satisfy `(alpha beta)(x)=alpha(beta(x))`; labels and word positions are distinguished.

## Statement and exceptional cases

Let `N>=2`, let `m>=0` be even, and freeze at the original input

```
K=max{1<=v<=N: v^(2v)<=(N+m+2)^4}.
```

Let `C(v,ell)` count connected ordered identity transposition words on a fixed labeled v-set, with `C(1,0)=1` for an isolate. For `v>=2` feasibility is exactly even `ell>=2v-2`; write `g=(ell-2v+2)/2`.

H0 admits isolates, all feasible components with `g<=1`, and all feasible components with `v<=K`. Its allowed set is A0. The separately versioned H1 admits isolates and all feasible components with `v<=K`; its allowed set is A1. Thus `A1 subset A0 subset Omega(N,m)`. The two policies are never conflated in the API or output. A user-specified diagnostic cutoff declares a separately labeled test candidate.

For either policy the implementation returns exactly `Unif(Ai)` in expected bit time polynomial in N,m, assuming independent fair bits and the count/primitive dependencies stated below. Every output has exact length and endpoint. It also returns the exact rational identity

```
TV(Unif(Ai),Unif(Omega(N,m))) = (Z-Zi)/Z.
```

Both sets are nonempty: K>=2 for N>=2, and repetition of one edge an even number of times is allowed, with all other labels isolated. `m=0` gives the empty word; `m=2` gives a uniform repeated edge; `N=2` gives the unique repeated-edge word at every even m. The implementation additionally accepts `N=0/1,m=0` as the unique empty word. Odd m, negative parameters, or N<2 with m>0 are rejected as invalid/empty. No length cutoff m<=2N is imposed; arbitrarily high genus on small support remains included. Complexity is in N, not log2N wires.

## Fixed-support iterative completion DP

For a component of degree v, a state `(q,pi)` records its actual prefix permutation q and the partition pi of its labels into exposed support components. Define

```
F(0,q,pi) = 1{q=id and pi has one block},
F(r,q,pi) = sum_(a<b) F(r-1,q(a b),pi join {a,b}).
```

For each literal suffix, its next edge selects exactly one term and the remaining suffix selects exactly one completion, so this recurrence counts connected identity completions, including all multiplicities. It does not replace support by permutation cycle type. If `blocks(pi)-1>r`, no suffix can connect the support, so the optional zero pruning is exact.

`MarkedCounter.count` evaluates the recurrence with an explicit depth-first continuation stack and a memo table indexed by `(r,q,pi)`. Every dependency strictly decreases r. No Python recursion or recursion-limit modification occurs. Two marked states with the same endpoint q but different exposed partitions remain separate.

Starting from `(id,discrete partition)`, choose each next edge with its exact continuation count divided by the current count. A connected identity word w has probability

```
product_(j=0..ell-1) F(ell-j-1,state_(j+1))/F(ell-j,state_j)
 = 1/F(ell,id,discrete) = 1/C(v,ell).
```

Zero continuation branches are never selected. The proof uses actual conditional counts under the exposed history, not an independence assertion. H1 uses this DP for every nontrivial component. H0 uses it for genus>=2 small components and the checked September7 g0/1 decoder for its other components.

## Exact assembly and the role of a fixed cutoff

For either fixed policy, define `D(v,ell)=C(v,ell)` on its allowed components and zero otherwise. Initialize `Zi(0,0)=1`, `Zi(0,k>0)=0` and compute

```
Zi(n,k)=sum_(1<=v<=n,0<=ell<=k)
 binom(n-1,v-1) binom(k,ell) D(v,ell) Zi(n-v,k-ell).
```

This is the least-label component decomposition: choose the other v-1 labels of its support, choose its ell positions, choose its connected internal word, and choose a remaining allowed word. Restriction of the resulting word to the least label's support uniquely recovers every choice. Therefore there is no extra symmetry quotient even when component sizes coincide. All labels and interleavings are counted.

The sampler chooses `(v,ell)` with the summand as its integer weight; chooses each label subset and position subset uniformly by exact binomial unranking; obtains an exact connected local draw; and repeats on the residual labels/positions. For one fixed final word these factors multiply to

```
[binom(n-1,v-1)binom(k,ell)C(v,ell)Zi(n-v,k-ell)/Zi(n,k)]
 *[1/binom(n-1,v-1)]*[1/binom(k,ell)]*[1/C(v,ell)]
 = Zi(n-v,k-ell)/Zi(n,k).
```

They telescope to `1/Zi(N,m)`. The same *original* K is used in every Zi table cell and sampled subproblem. Recomputing it changes D and invalidates this telescoping proof for the declared subset. The finite regression `(N,m)=(42,12)` has top-level K5, whereas residual `(5,12)` would recompute K4 and wrongly delete its positive size5/genus2 branch. That branch is retained by the implementation.

With Z the same recurrence using unrestricted C, exact total variation follows directly: allowed words contribute `(1/Zi-1/Z)` each and omitted words contribute `1/Z`, giving total variation `1-Zi/Z`. This identity alone provides no uniform asymptotic error estimate.

## Integer and storage accounting, retaining the length factor

Put `M=N+m+2`, `W=M^4`, and use `B=O((m+1)log M)` bits for component and assembly counts. Positive component counts are at most `binom(N,2)^m`; positive recurrence numerators have only polynomial prefactors, and all assembly summands are at most their total. Binomial coefficients actually accessed use label subset sizes at most `m/2`, so their bit lengths also fit B. The imported positive DYZ algorithm and two assembly tables use `O(N^2(m+1)^2)` integer arithmetic operations and polynomial storage; with schoolbook arithmetic a conservative bit bound is `O(N^2(m+1)^2 B^2)` plus polynomial table-initialization costs. Exact rational certificate reduction is polynomial in B.

For v<=K, let `S_v=v! Bell(v)`. The inequality `Bell(v)<=v^v` follows by encoding each block by its least element, and `v!<=v^v`, hence

```
S_v <= v^(2v) <= W.
```

A counter retaining all lengths r<=m has at most `(m+1)S_v` memo entries. Reusing one counter for each v yields at most

```
Q=(m+1) K W
```

entries in total. **The factor m+1 is essential and is not omitted.** A key has `D=O(K log(K+1)+log(m+1)+1)` bits; each value has at most B bits. The memo storage is `O(Q(B+D))` bits. At most m pending depth levels occur, each with at most `binom(K,2)` sibling tasks; their keys cost `O((m+1)K^2 D)` bits. Transition construction makes/joins tuples in O(K) label operations; each table entry scans O(K^2) edges at most a constant number of times. The usual constant-time map model gives `O(Q K^3)` label operations and `O(Q K^2)` B-bit additions. A balanced map contributes a polynomial logarithmic factor.

The shipped Python implementation uses dictionaries. Even without average-case hashing, each dictionary operation is bounded by a linear scan over at most Q resident keys. Thus a deliberately conservative worst-case bit bound for the marked counters is

```
O(Q K^2 [Q D + K log(K+1) + B]),
```

up to a fixed polynomial factor for standard integer/tuple operations. This remains polynomial in N,m. Sampling the already counted transitions adds at most m next-edge scans and cannot change the same polynomial bound. Exact `randbelow(Z)` draws `(Z-1).bit_length()` fair bits and rejects values>=Z; acceptance is greater than1/2 unless Z1 is deterministic. Thus random choices have expected polynomial bit cost, with no approximation or probability rounding.

The September7 g0/1 primitive has conservative expected bit time `O(v^10 log^3(v+1))` and polynomial storage. Since sampled component degrees sum to at most N, their total primitive time is at most `O(N^10 log^3(N+1))`; internal recursion is already an explicit stack. This term applies only to H0. H1 calls neither its endpoint-count formula nor its connected sampler. Exact label/position choices and bookkeeping are polynomial. Computing K by integer binary search uses at most O(log(N+1)) exponent comparisons with at most O(N log(N+1)+log M) bits, also polynomial; floating logarithms are never used.

These bounds establish one polynomial implementation across every even m, so in particular across T0's range. They do not establish practical efficiency for all numerically large polynomial inputs, and do not depend on an accuracy exponent a. Retaining prepared tables across repeatedly requested draws increases no state bound beyond Q for the same fixed input.

For a single simple exponent that also covers the literal Python maps and
binary-search powers, **expected O(M^20) bit time and O(M^10) bit storage**
are conservative bounds for one prepared draw. Indeed K<=M, Q<=M^6 and
B,D=O(M^2), so the displayed dictionary-scan bound is O(M^16).
Even charging an additional O(M^2) for bookkeeping/index arithmetic leaves
O(M^18). The g0/1 term is O(M^13); its largest live allocation table has
O(N^3) integers of O(N log(N+1)) bits, and its fixed-capacity caches,
O(N)-depth continuation stack, and stored child words all fit O(M^8).
Other count tables fit O(M^4) bits. K's binary-search powers have at most
O(M^2) bits, use O(log M) multiplications per comparison, and only
O(log M) comparisons; schoolbook arithmetic fits O(M^6). Even recomputing
each assembly binomial by a polynomial factorial/multiplication routine
within O(M^3) branch visits fits O(M^10). These deliberately loose bounds
dominate the displayed contributions without assuming unit-cost count
arithmetic, average-case hash performance, or a fixed m. They are not
benchmarked performance claims.

## Dependencies and what is new here

- **Imported count theorem:** DYZ, Classical Hurwitz Numbers, Proposition1 Eq(13), with fixed ordered-word normalization from Section1.2 Eqs(19)–(20): `C(d,k)=d! k! h[g,d]`. The historical positive integer implementation is hash-frozen before execution. Root reports a direct primary-source normalization check in this run; exact tests here independently compare its entries to the new marked DP for v1..5 and ell0..14. Counting alone is not used as a decoder.
- **Imported H0-only sampler theorem:** September7 R1-T1.1 / canonical S1.v2, based on Vakil Section1.2 Corollary1.5 and its positive expansion. Its full proof and source were read; root reports renewed source normalization review. The historical decoder is hash-frozen, uses exact integer branching and explicit stacks, and receives fresh complete-word-law checks here. H1 has no mathematical dependence on the g0/1 formulas or decoder, although it reuses their elementary `getrandbits` rejection and subset-unranking utilities.
- **Elementary proved inputs:** connected feasibility by support joins/splits; marked completion recurrence; least-label disintegration; exact subset unranking; TV of a uniform restriction.
- **Implementation contribution:** fixed top-level K, actual iterative arbitrary-length support-marked decoder, one exact API/CLI combining it with the prior decoder, exact certificate, explicitly separate H1 option, and expanded regressions. No claim of a new all-genus large-support decoder is made.
- **First remaining global obligation:** prove an explicit eta(N), negligible uniformly over even `m^5<=N^3`, bounding `(Z-Z0)/Z` (or the larger `(Z-Z1)/Z`). Until the current analytic proof passes nonauthor audit, this deliverable does not achieve global T0.

## Falsification and finite evidence

Current audit-v3 passes all literal-word probabilities for H0 at (3,4),(4,4),(4,6),(3,6),(3,8),(4,8), totaling all required finite laws, and at forced cutoff2(3,8), where only3 of2187 words survive and exact TV728/729. H1 passes full laws at (3,4),(4,4),(4,6),(3,8),(4,8); at(4,6) it retains1056/3936 and at(4,8)9120/140160. These latter poor small cases are outside T0 and are retained as boundary evidence, not hidden.

Tests verify endpoint and length, labeled component multiplicities and interleavings, every literal-word probability, prefix cycle types, position edges, edge multiplicities, adjacent repeats, weighted support components and length3 window products. Diagnostic histograms are exact pushforwards of the fully checked word law and are stored compactly by sizes and SHA256. Counts agree on all75 `(v,ell)` cells v1..5,ell0..14, including odd and infeasible cells. An actual v2 length1200 completion/sample succeeds with no recursion-limit adjustment. Exact integer cutoff is checked on4941 `(N,m)` cells plus the equality threshold `(4,10)`. Three fixed seeds1729,2718,31415 check implementation validity in six sampler cases; these seeded draws are not evidence of exact uniformity on their own.

An actual H0 nonzero omission inside T0 at `(128,16,K5)` is

```
3015538111971730865520000 / 398488912723604665601813065391959.
```

This independently matches R4's separate count implementation. A finite certificate is not an asymptotic theorem. Same-model code review is correlated internal evidence rather than human certification.

## Retained serialization repair, v3

R5 and root independently noted that default Python3.12 decimal integer serialization can fail above4300 digits; e.g.N100000,m1000 is insideT0 and its global count already exceeds that threshold. This affected the old CLI, not the exact API or law. The v3 CLI uses decimal integers/rational strings when safely below the current digit limit and otherwise emits labeled lossless hex integers or hex-rational numerator/denominator objects. It reads but never changes the interpreter digit-limit setting. A20001-bit synthetic exact roundtrip passes. This is an implementation repair with no mathematical kernel change; v1/v2 snapshots retain the historical issue.
