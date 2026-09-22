# Nonauthor audit of global consequence G1.v1

**Verdict: ACCEPT G1-COUNT, G1-SAT, and G1-OMIT as stated; ACCEPT G1-SAMPLE as the explicitly conditional assembly theorem.** The exact integrated implementation remains conditional on the frozen R1 primitive audit, including subset unranking. No mathematical repair to the global consequence is required. Two optional wording clarifications appear below.

This report audits the coordinator's exact supplied version, not a reconstruction inferred from my blind report. The complete followup input is in `global-audit-assignment.txt`. Full review inputs and the imported count dependency are preserved in `global-review-input/`. The following hashes were checked before reading the contents:

| input | SHA-256 |
|---|---|
| global_consequence.md | 9f92ca07ebf04fb46c6e613801224411d170297df917d22b5ccff546d59af9f9 |
| global_mass.py | ef0b588811798c861a8af3609ee0215e3a20c7e4a5fcc1c0656cb2c539bd0d80 |
| global_mass_results.json | 29344a82da6cf58ff990cde65dd924b8218ee3f1b33b60abe4e965ba5a823a4b |
| sample.py | bf4e11bdde4ad918225cc050aaf4ab070ded63bbdec9e0be4c5938d477b23a8f |
| imported component_audit.py | a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2 |

My blind report remains unchanged at SHA-256 e638cecd1c337a8d740be59f09aa7d9b895778616419dbcf85b3c9befde2250c. This is a same-model nonauthor review, not independent statistical evidence.

## G1-COUNT.v1 — ACCEPT / proved using checked published input

I checked [Dubrovin–Yang–Zagier's primary PDF](https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf), Proposition 1, equation (13), and §1.2, equations (19)–(20) and the monodromy interpretation immediately after (20). The source identifies d! H*_(k,d) with ordered transposition tuples having identity product. Its exponential connected/disconnected relation separates connected tuples, so C(d,k)=d! k! h_(g,d) when k=2d-2+2g. Connected monodromy and connected support agree. This checks both label and position normalization; no additional quotient is present. The identity target is unchanged by reversing factor order.

In (13), substitute a+b=d, r=2 ell, and k_i=2d_i-2+2g_i. Its genus condition g_1+g_2+ell=g+1 becomes k_1+k_2+r=k. Multiplication by d!k! changes 1/(a!b!k_1!k_2!r!) to binom(d,a) times the stated multinomial factor. The resulting positive recurrence is exactly the one in G1-COUNT. The denominator d^2(d-1) is used only for d>=2. C(1,0)=1 and all other C(1,k)=0 supply the base. Negative-genus and odd-length cells vanish, consistently with direct support/cycle reasoning.

The imported `connected_counts` implements two separate binomial convolutions: first combine the child lengths, then convolve with the positive even-r power term. `max_degree=min(N,floor(m/2)+1)` is justified by minimum connected identity length 2d-2. Its binomial tables are truncated only where connected counts are structurally zero. Every integer division is checked for exactness. The arithmetic count O(N^2(m+1)^2) is valid; positive partial sums cannot exceed the final positive numerator. Table allocation, precomputation, and operand lengths are polynomial in N,m. For N>=1 the stated O((m+1)log(N+1)) operand bound is safe, including m=0. The N=0 extension is trivial and should be treated separately if that exact bound is quoted there.

For the least-label recurrence, a word uniquely identifies the component containing the smallest remaining label, its vertex subset, the ordered positions of its factors, its connected internal word, and the residual word. The branch weight has exactly binom(n-1,v-1) possible vertex subsets and binom(k,ell) position subsets. After uniform choices and a uniform internal draw, its per-word contribution is

```
[binom(n-1,v-1) binom(k,ell) D(v,ell) Z_D(n-v,k-ell) / Z_D(n,k)]
 / [binom(n-1,v-1) binom(k,ell) D(v,ell)]
 = Z_D(n-v,k-ell) / Z_D(n,k).
```

The recursive ratios telescope to 1/Z_D(N,m). This is an exact conditional probability on each positive-mass branch. Isolated labels have v=1,ell=0, one empty internal word, and contribute no positions; they still remove one label, so termination holds. Equal block sizes do not create an extra factorial: actual vertex sets distinguish the blocks. The macro weight m! product_B C(|B|,ell_B)/ell_B! is therefore correct.

## G1-SAMPLE.v1 — ACCEPT / conditional on accepted connected primitives

The claim explicitly assumes exact expected-polynomial connected samplers at genera zero and one. Under that assumption, the selector just verified gives the uniform law on the declared restricted subset A_01. At most N component calls occur, and every component has size at most N and length at most m, so their expected times add to a polynomial. The selector uses integer weights, fair-bit bounded-integer rejection with acceptance greater than one half, and uniform finite subsets. No assumption about an efficient sampler for higher genera is smuggled into the argument.

For Z_01>0 and a nonempty global fiber, a direct calculation gives

```
TV(Unif(A_01),Unif(Omega)) = 1-Z_01/Z.
```

On A_01 the density difference sums to 1-Z_01/Z; off A_01 the missing global mass is the same, and the factor one half in TV cancels the duplication. The code returns this exact rational certificate and labels the output as conditional. It does not claim the restricted law is globally uniform unless the covered mass is one.

For approximate primitives, expose the actual component-selection history and already generated internal components. Use an exact maximal coupling for the next pair of component draws conditional on every surviving shared history. The hypothesis bounds each such conditional failure probability by epsilon/(2N); after the first failure no further agreement claim is necessary. A union bound on at most N first-failure opportunities gives epsilon/2, including support restrictions or zero-probability branches. Triangle inequality then gives the stated 1-Z_01/Z+epsilon/2 bound. There is no multiplication of marginal estimates. The implementation currently uses exact primitives; this approximate extension is a separate conditional mathematical statement.

The actual `sample_restricted_components` rejects negative parameters, odd length, a positive-length fiber on fewer than two labels, and every zero restricted mass. Its m>2N guard is valid because each permitted nontrivial component contributes at most twice its size. A singleton vertex is allowed only as an isolate and is sent to the primitive with genus zero. In particular N=2,m=6 is correctly rejected although the unrestricted global fiber has one word. N=0,m=0 returns the unique empty word with covered mass one. N=1,m=0 and every N,m=0 work by empty singleton components. At N>=2,m=2 the exact law is a repeated uniform transposition.

The actual integration code's internal permutation call, label mapping, and position selection have the right structure; final acceptance of its leaf sampler and `unrank_subset` is deferred to the separate frozen R1 audit. Support smoke checks below exercised the real integration code and its currently frozen dependency.

## G1-SAT.v1 — ACCEPT / proved

Let s be the number of labels in nontrivial support components, k their number, and G their genus sum. Each internal endpoint is identity, so its length is 2v-2+2g. Summing gives m=2s-2k+2G. For the restricted family, each genus is zero or one, so G<=k and s<=N. At m=2N both inequalities must be equalities: s=N and G=k. Thus there are no isolates and every nontrivial component has genus one. Conversely any partition into nontrivial genus-one identity components contributes total length 2N.

The saturated recurrence follows by selecting the least-label block exactly as before, with length fixed at 2v. A(0)=1 is the empty residual assembly, while A(1)=0 because a singleton cannot be a nontrivial genus-one component. These bases are necessary and correct. For every N>=2, one connected genus-one component provides positive restricted mass.

## G1-OMIT.v1 — ACCEPT / proved; scope is exactly the named restricted method

The genus-one identity specialization of the checked Vakil formula has only nonnegative subtracted terms, so a_v=C(v,2v)/(2v)! <= v^v/24. The elementary bound v!>=(v/e)^v and e<3 imply a_v<=3^v v!. These are upper bounds on complete counts, not a claim that signed formula summands define positive sampling branches.

For a set partition into blocks of size at least two, multiplying those bounds gives 3^N product_B |B|!. To count the latter weights, temporarily order the k labeled blocks. For each ordered composition (v_1,...,v_k), there are N!/product v_i! labeled allocations, so its weighted contribution is N!/k! after forgetting the order of the k actual blocks. This division by k! remains correct when block sizes repeat. Dropping the divisor and allowing all positive compositions gives the bound N!2^(N-1). Hence Z_01<= (2N)!6^N N!, as stated for N>=2.

For every integer 2<=r<=N, words on one fixed r-subset inject into the global fiber. The N-step all-transposition walk on S_r has inversion-symmetric endpoint probabilities: reversal of each sequence is a bijection between paths to q and q^-1. Its endpoint support lies in a parity class of size r!/2. Therefore its 2N-step identity return probability is sum_q p_N(q)^2, at least 2/r! by Cauchy–Schwarz. Multiplying by binom(r,2)^(2N) proves the lower bound on Z. No connectivity or mixing assumption is used in this walk bound; r=2 is valid and gives the lower bound one.

For sufficiently large N, r=floor(N/log N) satisfies 2<=r<=N. Then log(r!)<=r log r=O(N), and

```
2N log binom(r,2) = 4N log N - 4N loglog N + O(N).
log((2N)!N!6^N) <= 3N log N + O(N).
```

Subtracting proves the stated -N log N+4N loglog N+O(N) exponent, which tends to minus infinity. The floor only changes the O(N) remainder. Thus the covered fraction tends to zero and the exact restricted sampler's global TV tends to one. Any other law supported on A_01 has at least the same omitted-mass error by testing the event A_01's complement. This does not constrain a hybrid with higher-genus support and is not a hardness result.

## Independent checks

I wrote `global_check.py` independently of the supplied counting implementation. It derives a separate total-count recurrence from DYZ equation (22). Writing A_d(x)=sum_k Z(d,k)x^k/(d!k!), coefficient extraction of ZH D^2ZH-(DZH)^2 gives

```
2d^2 Z(d,k) = 2H(d,k)-F(d,k),
F(d,k)=sum_(a+b=d,a,b>=1) binom(d,a)(a-b)^2
         sum_j binom(k,j) Z(a,j)Z(b,k-j),
H(d,k)=sum_(a+b=d-1,a,b>=0) d binom(d-1,a)
         sum_(j+h+r=k) multinomial(k;j,h,r)(a-b)^r Z(a,j)Z(b,h).
```

For even k, only even j,h,r survive. This independently computes total counts without using the candidate's connected recurrence or its assembly step. Restricted counts use my frozen blind fixed-endpoint formula and a newly implemented least-label recurrence. Both routes use named established formulas, while direct endpoint/support DP supplies a separate finite check.

Exact command, Python 3.12.3, standard library only:

```
timeout 60s python3 -B experiments/20260907-genus-one-sampler/roles/r3-referee/global_check.py
```

Recorded runtime: 3.657 seconds. `global-check-results.json` records:

- All 369 exact rational table rows through N=64,m=128 agree, including every decimal rendering.
- All 48 endpoint/support DP cells for 1<=N<=6 and 0<=m<=2N agree with the independently computed total counts.
- All 2,016 subgroup bounds for 2<=r<=N<=64 pass, as do the connected and global upper inequalities at m=2N.
- Actual integration smoke tests for N=0,...,8, m=0,...,2N+4, under seeds 17,101,20260907: 132 valid draws pass endpoint, length, permitted support-genus, and exact mass-certificate checks; 219 zero-mass or invalid boundary calls are correctly rejected. These seeded checks claim support only, not empirical uniformity.
- Exact two-stage binary conditional-kernel tests on the probability grid {0,1/4,1/2,3/4,1}: 125 models at delta=0, 2,197 at delta=1/4, and 6,859 at delta=1/2 satisfy the joint-TV bound 2 delta. Zero-support branches are included. Maxima found are 0,7/16,3/4 respectively. These finite tests supplement the conditional-coupling proof; they do not establish the universal theorem by themselves.

The compact table values are correct: 1 at N=2, 80/81 at N=3, and 4375/4672 at N=4. The N=4 numerator is 131250, not just the 131040 connected words: the additional 210 words come from three labeled two-pair partitions, each with 70 interleavings of two four-letter genus-one words. The larger decimals quoted at N=8,16,32,48,64 also match the independently computed exact fractions.

## Nonblocking clarifications and claim ledger

1. In the N=2 boundary paragraph, “all feasible even words are singletons” and “those singleton components” should be rewritten as “every feasible even-length global fiber has one word; its nontrivial support component has size two.” A singleton **vertex** component can only have length zero. The intended meaning is clear from the definitions and code, and no theorem is affected.
2. The O((m+1)log(N+1)) operand expression is intended for N>=1. If advertising the N=0 software extension under the same displayed formula, use log(N+2) or mention the separate constant-size case. The polynomial bit-complexity claim is unaffected.

| claim | status | assumptions | evidence | action |
|---|---|---|---|---|
| G1-COUNT.v1 | ACCEPT / proved | checked DYZ normalization and recurrence; binary integer model | source translation, code inspection, independent total-table route | retain |
| G1-SAMPLE.v1 | ACCEPT / conditional | accepted exact genus-zero/one connected primitives; positive restricted mass | explicit per-word ratios and conditional coupling | retain conditional label until primitive audit closes |
| G1-SAT.v1 | ACCEPT / proved | literal genus<=1 restriction and m=2N | equality in both length inequalities, singleton bases | retain |
| G1-OMIT.v1 | ACCEPT / proved | checked Vakil count formula; no sampler hypothesis needed | factorial/composition bound and subgroup CS estimate | retain with named-method scope |
| actual sample.py integration | CONDITIONAL, otherwise code structure passes | frozen R1 `sample`, `randbelow`, `weighted_choice`, `unrank_subset` | 132 valid and 219 rejected support/boundary calls | close in candidate audit |

No negative mathematical finding is suppressed. The first remaining uncompleted obligation is the primitive implementation audit, not a gap in G1-COUNT, G1-SAT, or G1-OMIT. All writes in this wave are confined to this role directory.
