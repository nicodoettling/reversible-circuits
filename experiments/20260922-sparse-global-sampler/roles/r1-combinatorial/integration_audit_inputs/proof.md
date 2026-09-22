# Global sparse identity-bridge sampling — SG-T1.v1

This is the canonical mathematical synthesis. Current-version audit disposition and exact reviewed hashes are recorded in `claim_ledger.md`; internal agent review is not external human certification. T0 is preserved verbatim in `intake_user_prompt.md`. T1 below strengthens its length range, without altering the original H0 cutoff or algorithm.

## Theorem and explicit error

Let `T_N` be all transpositions of `S_N`, with distinguished labels and positions, and products `(alpha beta)(x)=alpha(beta(x))`. For `N>=2` and even `m>=0`, let

```
Omega(N,m)={w in T_N^m: product(w)=id},  U_(N,m)=Unif(Omega(N,m)),
P=N+m+2,
K=max{v in {1,...,N}: v^(2v)<=P^4}.
```

Keep K fixed at this top-level value throughout all subproblems. A nontrivial connected support component of size v and length ell has `ell=2v-2+2g`, with integer `g>=0`. Isolated vertices have `(v,ell)=(1,0)` separately.

H0 admits a nontrivial component iff `g<=1 or v<=K`; let A be its word set. The separately versioned H1 admits a nontrivial component iff `v<=K`; let B be its word set. Thus `B subset A subset Omega`. The supplied H0 sampler remains the default and the requested candidate; H1 is an additional simpler construction.

**SG-T1.v1.** There are single uniform algorithms H0 and H1 which, on every such input, return an exact member of their respective sets, exactly uniformly, in expected `O(P^20)` bit time and `O(P^10)` bit storage in the exact binary-arithmetic model with independent fair random bits. In particular, for every even m with `m^3<=N^2`, both output laws Q satisfy

```
TV(Q,U_(N,m)) <= eta(N),
eta(N)=1                                      if 2<=N<2^160,
eta(N)=exp(-(ln N)^2/[10 ln ln N])             if N>=2^160.       (T1)
```

The same eta and algorithms therefore achieve the unchanged **T0** range `m^5<=N^3`, and every requested stretch range `m<=N^(2/3-delta)` for fixed `0<delta<2/3`, with no delta-dependent change in constants or runtime. There is no accuracy parameter or exponent-dependent algorithm. For every fixed `a>0`, eta(N)<=N^(-a) eventually; for example it suffices that `ln N>=max(160 ln2,100a^2)`, since `ln L<=sqrt(L)` for L>=100. These are conservative effective constants, not practical onset estimates.

H0 and H1 also compute their exact per-instance global error as `1-Z_A/Z` and `1-Z_B/Z`. Outside T1 their conditional uniformity and polynomial runtime remain valid, but this theorem asserts no uniform negligible-error bound there. Runtime is in degree N and length m, not in `log_2 N` wires.

## 1. Feasibility, component weights, and exact marking

Appending a transposition either joins two permutation cycles or splits one. Along an identity word the numbers of joins and splits agree. Each merger of distinct exposed support components is a permutation-cycle join, so a connected component on v labels requires at least v-1 joins. Hence its length is even and at least 2v-2. Conversely, concatenate adjacent equal pairs along a spanning tree and then any extra repeated-edge pairs. This proves feasibility and defines g without a geometric assumption.

Let C(v,ell) count connected identity words on one fixed labeled v-set, with C(1,0)=1 and other singleton entries zero. Set

```
A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!,
S(n,j)=|Omega(n,2j)|/(2j)!.
```

A support macro is an unordered collection of disjoint labeled nontrivial blocks, each with a genus; unused labels are isolates. Its cost is `sum_B (|B|-1+g_B)` and its normalized weight is `product_B A_(g_B)(|B|)`. The literal word count at cost j is `(2j)!` times this weight: choose the internal words and order-preservingly interleave their positions. Restriction to each support block uniquely recovers all these choices. Thus S(n,j) is exactly the sum of these macro weights. No component-size symmetry factor is omitted.

Let m=2k, and X_(v,q) count components on v vertices with 2q factors under the *global identity-conditioned law* U_(N,2k). Choosing their labels, their positions, and both internal and complementary words gives

```
E X_(v,q)
 = binom(N,v) binom(2k,2q) C(v,2q) Z(N-v,2k-2q)/Z(N,2k)
 = binom(N,v) [C(v,2q)/(2q)!] S(N-v,k-q)/S(N,k).       (1)
```

Every actual component supplies one mark, including when several have equal sizes. Equation (1) includes the full endpoint-conditioning normalizer; no random-graph independence or guessed return probability is used.

## 2. Checked imported count theorem

Dubrovin–Yang–Zagier, *Classical Hurwitz numbers and related combinatorics*, Proposition 1 Eq(13), Section1.2 Eqs(19)–(20), and the genus-zero value after Eq(28), give the following exact inputs:

- `C(v,ell)=v! ell! h_(g,v)` for `ell=2v-2+2g`;
- `A_0(v)=v^(v-3)`, including A_0(1)=1 by convention;
- for `F_v(t)=sum_ell C(v,ell)t^ell/ell!`, F_1=1 and

```
v^2(v-1) F_v(t)
 = 2 sum_(a+b=v; a,b>=1) binom(v,a) a b^2
       (cosh(a t)-1) F_a(t) F_b(t).                  (2)
```

[Primary source](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf). The labeled-tuple interpretation following Eq(20) restores sheet labels by v!, and its exponential formula separates connected supports. Positions are ordered; the ell! normalization is explicit. Connected monodromy is exactly connected transposition support. Reversal transfers opposite composition conventions and preserves identity and component data. The source was checked directly in this run; `source_checks.md` and the complete role audits record the normalization.

This is an imported established count theorem, not a new decoder or a fixed-genus asymptotic estimate. All subsequent genus bounds are uniform in g. The argument never evaluates a divergent two-variable Hurwitz generating function.

## 3. Factorial genus majorant

For all v>=1 put `b_v=(v^3-v)/36`. Coefficientwise in t²,

```
F_v(t) <= v^(v-3) t^(2v-2) exp(b_v t^2),
A_g(v) <= v^(v-3) b_v^g/g!.                          (3)
```

To prove this, divide (2) by its lowest nonzero term. With `H_v=F_v/[v^(v-3)t^(2v-2)]` and H_1=1,

```
H_v(t)=sum_(a+b=v) p_(a,b) L(a t) H_a(t) H_b(t),
p_(a,b)=binom(v,a)a^a b^(b-1)/[(v-1)v^(v-1)],
L(z)=2(cosh z-1)/z^2.
```

The p's are nonnegative and sum to one by the genus-zero coefficient of (2). Also coefficientwise `L(z)<=exp(z²/12)`, since

```
2/(2j+2)! <= 1/(12^j j!)  for j>=0.
```

Equality holds at j=0,1; the consecutive ratio is `12(j+1)/[(2j+4)(2j+3)]<=1`. Finally

```
b_v-b_a-b_b=abv/12 >= a^2/12
```

for every positive ordered split a+b=v. Induction and positivity therefore bound each summand by `exp(b_v t²)`, proving (3). This is a coefficientwise deterministic comparison, not a product of marginal probability bounds.

## 4. Fresh-pair incidence pays for endpoint conditioning

Suppose `0<=q<=k` and `2k<=N`, and write `D=N-2k+1>0`. For any specified removed v-set,

```
S(N-v,k-q)/S(N,k)
 <= 4^q q! binom(k,q)/D^(2q)
 <= (4k/D^2)^q.                                      (4)
```

Embed a base macro on its complement by isolating the removed labels. Its cost k-q uses at most 2(k-q) vertices because `v<=2(v-1+g)` for every nontrivial component. It consequently has I>=N-2k+2q isolated labels. Choose q disjoint unordered pairs among them, in exactly `(I)_(2q)/(2^q q!)` ways, and make each a length-two component. Its normalized component weight is A_0(2)=1/2. The total weight of these extensions from a base of weight w is therefore

```
w (I)_(2q)/(4^q q!) >= w D^(2q)/(4^q q!).
```

Conversely, a final cost-k macro has at most k minimal size-two components. Deleting a specified q-subset uniquely recovers a preimage, so there are at most binom(k,q) preimages. Requiring the removed v-set to be isolated after deletion only decreases the number. The incidence weight is exactly the final macro weight `w 2^(-q)`. Summing by bases and by final macros proves (4), including q=0 with empty products. Zero residual branches contribute zero. This argument compares exact weighted counts on the bridge space and introduces no independent-edge assumption.

## 5. Explicit finite maximum-component tail

For `1<=k`, `2k<=N`, define

```
x=4k/D^2,
z=k^2(k+2)/(9D^2),
c=exp(1+z),
rho=c N x.
```

For any integer J>=1, if rho<1 then

```
Pr_U[there is a nontrivial support component with v>J]
 <= min(1, N c rho^J /[(J+1)^3(1-rho)]).             (5)
```

If J>=k+1 the event is empty and needs no condition on rho. Otherwise, sum (1), (3), and (4) over feasible q=v-1+g. Extending the nonnegative genus sum gives

```
E X_v <= binom(N,v) v^(v-3) x^(v-1) exp(b_v x).
```

Feasibility implies v<=k+1 and hence `b_v x<=v z`. Using `v!>=(v/e)^v` gives

```
E X_v <= N c rho^(v-1)/v^3.
```

Summing v>=J+1, bounding `v^-3<=(J+1)^-3`, and using Markov's inequality for the total marked count proves (5). Every expectation is under U, not an unconditioned walk. H0's excluded event requires both v>K and g>=2, and is contained in this stronger maximum-size event. H1's omitted event is exactly that maximum-size event.

## 6. Uniform negligible bound through T1

For N>=2^160 put L=lnN>100 and assume m<=N^(2/3). Then m<=N/2, D>=N/2, and

```
k<=N^(2/3)/2,
k+2<=(5/2)N^(2/3),
z<=5/18<1,
c<e^2<8,
rho<=64N^(-1/3)<=N^(-1/6)<=1/2.                     (6)
```

The penultimate inequality uses N>=64^6=2^36. The integer `v0=floor(2L/lnL)` satisfies `1<=v0<=N`, `v0<=L`, and `2v0 ln v0<=4L`. Thus `v0^(2v0)<=N^4<=P^4`, so the actual integer cutoff has `K>=v0>=L/lnL`. Discarding the helpful cubic denominator in (5),

```
Pr(max size>K) <=16N exp(-K L/6)
              <=exp(ln16+L-L^2/[6lnL])
              <=exp(-L^2/[10lnL]).                  (7)
```

The last step follows from `lnL<=L/20` for L>=100, so `L²/(15lnL)>=(4/3)L>=L+ln16`. For smaller N the universal bound one applies. The m=0 case is exact. This proves the single explicit eta for every length in T1, hence T0, without changing an algorithm or polynomial exponent with the requested inverse-power a.

## 7. Exact support-marked connected decoder

For a fixed v, retain the actual prefix permutation p and its exposed support partition pi. Let

```
G(0,p,pi)=1{p=id and pi has one block},
G(r,p,pi)=sum_(a<b) G(r-1,p(a b),pi join {a,b}).       (8)
```

The initial state is `(id,discrete partition)`. Each next literal edge selects one summand, and the remaining suffix selects one completion, so (8) counts exactly the suffixes which end at identity and connect the exposed support. In particular, prefix connectivity is not discarded in favor of the endpoint alone. Pruning when `number_of_blocks(pi)-1>r` is valid.

Fill the recurrence iteratively or by the supplied explicit continuation stack, with memo keys `(r,p,pi)`. Dependencies strictly decrease r; there is no interpreter recursion. Choose a next edge by its integer continuation weight. For a connected word of length ell the product of its actual conditional probabilities telescopes to `1/G(ell,id,discrete)=1/C(v,ell)`. Zero branches are never chosen. This supplies H1's entire connected decoder and H0's arbitrary-genus small-support decoder.

H0 additionally uses the September7 exact g=0/1 connected decoder for any v. Its strengthened interface samples connected factorizations of any specified endpoint sigma at length `v+cycles(sigma)-2+2g`, with g=0 or1, in expected `O(v^10 log³(v+1))` bit time. The constructive proof deletes the final transposition: the predecessor is connected, or splits into two anchored support components whose genera sum to g. Positive genus-zero/one fixed-endpoint count formulas allow the remaining labeled cycles to be assigned by a polynomial dynamic program of size, cycle count and symmetric moments. Branches, child words and their interleavings reconstruct each word uniquely. This exact primitive, its positive conditional allocation masses and its explicit-stack implementation were reread and freshly checked during this run; full proof remains in the read-only September7 `proof.md`, with direct [Vakil Section1.2, Corollary1.5 and Proposition3.2](https://math.stanford.edu/~vakil/files/g01hurwitz.pdf) normalization recorded in `source_checks.md`. It is an imported project construction, not an assumed unspecified sampler. H1 has no mathematical dependence on this primitive.

## 8. Least-label assembly and exact global error

For either policy let D(v,ell) equal C(v,ell) on its allowed components and zero elsewhere, with the one fixed original K. Initialize `Z_D(0,0)=1`, `Z_D(0,t>0)=0`, and compute

```
Z_D(n,t)=sum_(v=1..n,ell=0..t)
 binom(n-1,v-1) binom(t,ell) D(v,ell) Z_D(n-v,t-ell). (9)
```

Select the least remaining label's component size and length by these exact integer weights. Choose its other labels and positions uniformly by binomial unranking, draw its connected word exactly, and continue on the remaining labels and positions. The literal component decomposition is unique. For any fixed final word its first-stage probability, including both subsets and its internal word, cancels to `Z_D(n-v,t-ell)/Z_D(n,t)`. Induction gives exactly `1/Z_D(N,m)`.

No step recomputes K. In particular top input (42,12) has K5, while residual (5,12) would incorrectly recompute K4 and omit an allowed genus-two component. Actual forward execution of both policies passed this regression.

K>=2 for N>=2, so repeating one edge any even number of times proves nonemptiness. For any positive restricted count, summing uniform probabilities on the included and excluded words gives exactly

```
TV(Unif(A),U)=1-Z_A/Z,
TV(Unif(B),U)=1-Z_B/Z.                               (10)
```

Equations (5)–(7) bound these errors, completing the global theorem. Scalar counts alone would not complete this proof; the literal decoders and assembly provide the required sampling maps.

## 9. Bit time, storage, and executable artifact

All count integers have `O((m+1)log P)` bits, up to polynomial prefactors in the positive connected recurrence. Multiplying (2) by factorials yields a positive integer recurrence; binomial convolutions compute all needed connected counts in `O(N²(m+1)²)` arithmetic operations. Equation (9) has the same polynomial operation bound. Exact total/restricted counts give a rational certificate with polynomial bit cost.

For v<=K there are at most `v!Bell(v)<=v^(2v)<=P^4` permutation/partition states. Retaining every remaining length and every eligible v uses at most

```
Q=(m+1)K P^4 <=P^6
```

memo entries; the factor m+1 is essential. Keys have `O(Klog(K+1)+log(m+1)+1)` bits and values have `O((m+1)log P)` bits. The explicit DFS stack has at most m depth levels, each with O(K²) pending siblings. Each unique memo entry scans O(K²) edges a constant number of times. Even charging a linear scan of all Q keys for every Python dictionary operation, and polynomial bit cost for tuple construction/comparison, remains bounded by the conservative O(P^20) time/O(P^10) storage envelope. The complete dominance calculation and import accounting are in the frozen `roles/r3-sampler/proof-v3.md`. H0's g0/1 work is bounded by `sum_components O(v^10 log³(v+1))<=O(N^10 log³(N+1))`, also covered. K is computed by exact integer comparisons, not floating logarithms.

Exact uniform integers are drawn with `(Z-1).bit_length()` fair bits and rejection above Z; expected trials are fewer than two unless Z1 is deterministic. There is no precision approximation. The repaired CLI represents very large certificate integers/rationals in lossless hexadecimal, avoiding Python's decimal-digit conversion cap without changing interpreter settings.

The default executable is `sample.py`, forwarding to hash-frozen `roles/r3-sampler/sampler-v3.py`; APIs are `sample_h0`, `sample_h1`, and `PreparedSampler`. The implementation intentionally labels its conditional target and returns the exact certificate; this theorem supplies its global negligible-error interpretation within T1.

## 10. Exceptions, dependencies, and falsification

- m=0: the unique empty word, exactly.
- m=2,N>=2: a uniform transposition repeated twice, exactly.
- N=2: the unique edge repeated at every even length, exactly; T0/T1 only require their stated length subsets.
- N=1: only m=0 is feasible; odd m and positive lengths at N<2 have empty targets and are rejected.
- Near-minimal connected lengths and arbitrary high genus on v<=K are included exactly.

The only non-elementary literature dependency for H1 is the checked exact Hurwitz recurrence/minimal count used in the tail. H0 additionally uses the fully specified, rechecked September7 g0/1 decoder and its checked Vakil formula. Neither uses Hurwitz transitivity, any local-chain mixing theorem, random-graph independence, or a conjectured completion oracle. The first remaining mathematical obligation for T0/T1 is **none once the current audit ledger is closed**. General longer ranges and efficient all-genus large-support decoding are outside the claim; no hardness or sharp-threshold result is asserted.

Exact tests include complete literal laws at S3,m4; S4,m4; S4,m6; S3,m6; S3,m8; S4,m8; deliberately excluded components; high-genus small supports; cutoff equality/frozen-recursion cases; large-length explicit stacks; and exact full-minus-allowed counts. Root exhausted actual forward production choices for all140160 words of S4,m8, each probability1/140160. Actual nonzero omitted mass inside T0 is independently certified at N82,m14,K5 and N128,m16,K5. Tests target falsification and implementation; they are not the asymptotic proof.

Historical negative findings remain in `regression_registry.md`: the old minimal-only fixed-error bound, its larger-power obstruction, genus<=1-only failure at m2N, square-insertion omissions, unweighted graph bias, exposed-support omissions, and the new CLI serialization defect. The old genus<=1 obstruction does not refute H0. No sequential marginal probabilities are multiplied here, so the cached-prefix independence regression is inapplicable to this proof's deterministic incidence argument.
