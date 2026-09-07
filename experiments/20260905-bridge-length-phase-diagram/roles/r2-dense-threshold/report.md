# R2: a tunable dense length/error theorem

Date: 2026-09-05 UTC. Status: **proved; final report frozen for fresh nonauthor audit**.

The new input is a sharper bridge-conditioned retained-length bound. The historical proof paid `r!` when transferring an unconditioned count tail to an endpoint bridge. Every discarded branch in question is old-long, so its old completion count is already pointwise smoothed. Summing the exact star projection before conditioning reduces that loss to `O(r)`. No new mixing theorem for a chain on words is used.

## 1. Precise theorem and conventions

Permutations are maps with `(alpha beta)(x)=alpha(beta(x))`; the rightmost displayed factor acts first. For `N>=2`, `m>=0`, and `g in S_N`, the target is the uniform probability law `U_(N,m;g)` on all length-`m` transposition words with displayed product exactly `g`.

**Theorem D (density-parameterized retained-rank sampler; proved).** Let `N>=5`, let `m` be an integer, and let `g in S_N` satisfy

```
sign(g)=(-1)^m,       m >= N-cycles(g).
```

Put

```
q = floor(m/[2N(N-1)]),       a_N = ceil(log_2 N).
```

If `q >= 4a_N`, the algorithm below always outputs exactly `m` transpositions with product exactly `g`, and its output law `Q` satisfies

```
d_TV(Q,U_(N,m;g)) <= min{1, 3N^2 exp(-q/144)}.             (D1)
```

The expected Turing runtime and space are polynomial in `N,m`. A conservative bound is `O(N^4 m^3)` exact arithmetic operations on polynomial-bit integers/rationals. For `2<=N<=4`, a fixed finite-state backward bridge DP is exact for every feasible `m,g`.

**Corollary (proved dense epsilon regime).** For `N>=5`, every `0<epsilon<1`, and every feasible endpoint, it suffices that

```
m >= 2N(N-1) ceil(144 log(3N^2/epsilon))                 (D2)
```

where `log` is natural. This is `O(N^2(log N+log(1/epsilon)))`. Under (D2), the runtime is polynomial in `N,m,log(1/epsilon)` and endpoint error is zero. The algorithm itself uses only integer/rational computations and does not need to evaluate a real logarithm. The theorem's easily checked precondition is `q>=4a_N`; (D2) is a sufficient analytic accuracy guarantee.

At fixed `(N,m)` the bound has an error floor. Spending more runtime in this algorithm has not been shown to meet every smaller epsilon. The theorem therefore does not give all-length or arbitrary-accuracy sampling at a fixed bridge length.

## 2. Imported proved inputs

Only these internally audited inputs are imported:

1. The stable-sort bijection and inverse, manuscript (RR.3)--(RR.5): a binary old/star pattern with old endpoint `h` and star endpoint `z` has endpoint `g=h z`, equivalently `z=h^{-1}g` and `h=g z^{-1}`. An old transposition avoids the pivot `r`; a star transposition is `(i r)`.
2. Exact polynomial prescribed-endpoint star `Count/Sample`, manuscript (RR.6)--(RR.8), based on Féray, *Partial Jucys–Murphy elements and star factorizations*, Proposition 1.1, Theorem 1.2 and Lemma 3.1, arXiv:0904.4854v2. The positive fixed-point-support disintegration is essential. Existing implementation: `experiments/20260901-rank-recursive-identity-bridge-goal/roles/r3-star/star_bridge.py`.
3. Pointwise parity smoothing, manuscript (RR.10)--(RR.13), and the positive two-sided one-rank comparison (RR.15)--(RR.17). The spectral dependency is Caputo--Liggett--Richthammer, *Proof of Aldous' spectral gap conjecture*, JAMS 23(3), 831--851 (2010), Theorem 1.1, DOI `10.1090/S0894-0347-10-00659-4`. Applied to the complete graph and the star, and combined with sign symmetry, this gives the radii displayed below.

Historical proof inspected specifically for the retained floors and telescope: `experiments/20260901-rank-recursive-identity-bridge-goal/roles/r4-r5-closure/report.md`. Its factorial bridge-conditioning estimate is correct but unnecessarily costly for discarded old-long branches. No historical resolution ledger or run log was needed.

The new theorem uses neither Hurwitz transitivity nor local heat-bath irreducibility or mixing. These inputs concern endpoint walks used as completion counts, not dynamics on transposition words.

## 3. The same positive lift, with simpler rational floors

Fix the top-level `N,q`. For `5<=r<=N`, define

```
c_5=1,
c_r=1+sum_(j=6)^r 1/[j ceil(sqrt(j))],
B_4=0,
B_r=ceil(q r(r-1)c_r).                                 (D3)
```

All square roots are integer ceiling square roots and all sums are rational. Since

```
sum_(j=6)^infinity 1/[j ceil(sqrt(j))]
 <= sum_(j=6)^infinity j^(-3/2)
 <= integral_5^infinity x^(-3/2) dx = 2/sqrt(5) < 1,
```

we have `1<=c_r<2`, `B_r>=q r(r-1)`, and

```
B_N <= 2q N(N-1) <= m.                                (D4)
```

The first inequality follows because its right-hand side is an integer strictly above the unrounded argument. Thus the top call is retained. Ranks at most four are handled by exact finite-state DP, with no asymptotic-exception fallback.

For a call `(r,L,g)` with `r>=5,L>=B_r`, set

```
s=L-k,  d=binom(r-1,2),  b=r-1,  x=g^{-1}(r),
A_s(h)=[h] C_(r-1)^s,   B_k(z)=[z] J_r^k.
```

The exact unnormalized branch law is

```
binom(L,k) A_s(h) B_k(h^{-1}g).                       (D5)
```

Let `Z_r(k,x)` count star words with endpoint `z` satisfying `z(x)=r`. For `u_0=1,v_0=0`,

```
u_(j+1)=b v_j,     v_(j+1)=u_j+(b-1)v_j,
Z_r(k,r)=u_k,     Z_r(k,x)=v_k for x!=r.              (D6)
```

Equivalently `u_k=(b^k+b(-1)^k)/r` and `v_k=(b^k-(-1)^k)/r`. In particular

```
0 <= Z_r(k,x) <= b^k.                                 (D7)
```

Use the nonnegative integer weights

```
Wtilde_k = r binom(L,k) d^s Z_r(k,x), if s>=k;
           binom(L,k) d^s b^k,        if k>s.           (D8)
```

For `r>=6`, set the weight to zero on old-long branches with `s<B_(r-1)`. Keep every star-long branch. At rank five make no truncation.

The untruncated pointwise relative completion error is

```
Delta(r,L)=max{
 ((r-1)!-2)/2 * ((r-4)/(r-2))^ceil(L/2),
 (r!-2)/2 * ((r-2)/(r-1))^(floor(L/2)+1)
}.                                                    (D9)
```

## 4. Smoothing and exact feasibility

The precondition `q>=4a_N` implies `q>=12` and `q>=4 log r` for every `5<=r<=N`. From `L>=q r(r-1)`, `1-t<=exp(-t)`, and `r!<=exp(r log r)`, the star term in (D9) is at most

```
exp(r log r - L/[2(r-1)]) <= exp(-q r/4).
```

The old term is at most

```
exp(r log r - L/(r-2)) <= exp(-3q r/4).
```

Consequently

```
Delta(r,L) <= exp(-q r/4) < 1/2.                       (D10)
```

The full rank-`r` endpoint walk has nontrivial absolute radius `(r-3)/(r-1)`. Its parity-relative error at time `L` is at most

```
(r!-2)/2 * ((r-3)/(r-1))^L
 <= exp(r log r-2L/(r-1)) <= exp(-7q r/4) < 1/2.
```

Writing `M=binom(r,2)`, this proves uniformly on the correct parity class

```
|Omega(r,L;g)| >= M^L/r!.                              (D11)
```

Every generated old-long endpoint `h=g z^{-1}` has the correct parity, and `s>=L/2>=r-2` gives feasibility. A retained old child additionally satisfies `s>=B_(r-1)`. Every star-long prescribed endpoint has positive star count because (D10) is a strict relative bound below one. The retained branch normalizer is positive: the all-star branch `k=L` is kept, has positive weight, and has a nonempty exact star fiber. Thus the algorithm is defined even when the final error bound exceeds one.

## 5. Ceiling loss and unconditioned retained-length tail

At rank `r>=6`, an unconditioned length-`L` word has old count

```
A ~ Bin(L,p),       p=(r-2)/r.
```

For a fixed cutoff `B_(r-1)`, the tail `Pr[A<B_(r-1)]` decreases with `L` by the elementary Bernoulli coupling. It suffices to work at `L=B_r`. Put `mu=pB_r`. The ceiling loss is at most one:

```
mu-B_(r-1)
 >= q(r-1)(r-2)(c_r-c_(r-1))-1
 = q(r-1)(r-2)/[r ceil(sqrt(r))]-1.                  (D12)
```

For `r>=6`, `(r-1)(r-2)>=r^2/2` and `ceil(sqrt(r))<=3sqrt(r)/2`. Therefore the last expression is at least `q sqrt(r)/3-1`. Since `q>=12` and `r>=6`, `q sqrt(r)>=12`, whence

```
mu-B_(r-1) >= q sqrt(r)/4 =: t_0.                     (D13)
```

The star count `K=B_r-A` has mean

```
lambda=2B_r/r <=4q(r-1)+2/r <=4qr.                    (D14)
```

For the binomial upper tail, Bernstein gives

```
Pr[A<B_(r-1)]
 <= exp(-t_0^2/[2(lambda+t_0/3)])
 <= exp(-q/144).                                      (D15)
```

Indeed, `t_0/3=q sqrt(r)/12<=qr/24` for `r>=4`, so the denominator is at most `(97/12)qr<=9qr`, while `t_0^2=q^2r/16`. This proves (D15) uniformly for every `L>=B_r`. For completeness, the needed Bernstein inequality follows from `E exp(theta(K-lambda)) <= exp(lambda(exp(theta)-1-theta))` and `exp(theta)-1-theta <= theta^2/[2(1-theta/3)]` for `0<theta<3`; use Markov's inequality with `theta=t/(lambda+t/3)`. The series inequality follows coefficientwise from `1/j! <= 1/(2*3^(j-2))` for `j>=2`. Thus no additional literature dependency is needed. No independence is asserted after endpoint conditioning.

## 6. New bridge-conditioned survival lemma

**Lemma S (proved).** For `r>=6,L>=B_r`, and every feasible `g in S_r`, the exact bridge probability of a discarded old-long branch is at most

```
b_r <= 3r exp(-q/144).                                (D16)
```

**Proof.** Let `D={k: L-k>=k, L-k<B_(r-1)}`. Every `k in D` is old-long, so its old completion satisfies the same uniform pointwise upper bound as in (D9):

```
A_(L-k)(h) <= (1+Delta) 2d^(L-k)/(r-1)!
```

for all parity-compatible `h in S_(r-1)`. Exact disintegration, followed by the exact star projection and (D7), yields

```
# discarded endpoint-g words
 = sum_(k in D) binom(L,k) sum_h A_(L-k)(h) B_k(h^{-1}g)
 <= [2(1+Delta)/(r-1)!]
      sum_(k in D) binom(L,k) d^(L-k) Z_r(k,x)
 <= [2(1+Delta)/(r-1)!] M^L Pr[A<B_(r-1)].            (D17)
```

Divide by (D11), then use (D10) and (D15):

```
b_r <=2r(1+Delta) Pr[A<B_(r-1)]
    <=3r exp(-q/144).
```

This is the decisive improvement over the historical `r!` loss. It does not require discarded child calls to meet the next floor: old-long already gives enough length for their completion counts to be smoothed at the current rank. No discarded child is actually sampled. QED.

## 7. TV telescope

Let `U^G` be the exact bridge conditioned on retention. The exact/flat unnormalized branch likelihood ratio on the retained set is still in `[1-Delta,1+Delta]`. With exact lower children, the retained positive lift therefore differs from `U^G` by at most `Delta/(1-Delta)`. Also `d_TV(U,U^G)=b_r`. Thus the one-rank error, before approximating its child, is at most

```
b_r+Delta/(1-Delta) <=3r exp(-q/144)+2exp(-qr/4).       (D18)
```

At rank five `b_5=0`. At most one child is sampled, and it lies in the next retained domain; star-long branches terminate the rank recursion. If `D_r` is the worst actual TV error over retained calls at rank `r`, exact reconstruction and Markov-kernel contraction give

```
D_4=0,
D_5<=2exp(-5q/4),
D_r<=3r exp(-q/144)+2exp(-qr/4)+D_(r-1), r>=6.         (D19)
```

Consequently

```
D_N <=3 sum_(r=6)^N r exp(-q/144)
      +2 sum_(r=5)^N exp(-qr/4)
    <=2N^2 exp(-q/144)+N^2 exp(-q/144)
     =3N^2 exp(-q/144).
```

Here `3sum_(r=6)^N r <= 3N(N+1)/2 <=2N^2` for `N>=5`, and `2N exp(-5q/4)<=N^2 exp(-q/144)`. This proves (D1). Condition (D2) implies `q>=ceil(144 log(3N^2/epsilon))>=4a_N`, and substitution proves the corollary.

## 8. Executable pseudocode and bit complexity

```
Dense(N,m,g):
    validate the input permutation, nonnegative length, and feasibility
    if m<=2: enumerate the O(N^4) or fewer candidate words and sample the valid fiber exactly
    if N<=4: return exact finite-state backward bridge sample
    q := m // (2*N*(N-1))
    require q >= 4*ceil_log2(N)
    compute rational c_r and integer B_r for r=5,...,N
    return Recurse(N,m,g)

Recurse(r,L,g):
    if r<=4: return exact finite-state backward bridge sample
    x := inverse(g)(r)
    compute the token completion integers Z_r(k,x), k=0,...,L
    form integer weights (D8)
    if r>=6: zero weights having s=L-k>=k and s<B_(r-1)
    draw k exactly from these integer weights; set s=L-k
    if s>=k:
        draw a uniform star word v with eval(v)(x)=r using (D6)
        z := eval(v); h := g*inverse(z)
        u := Recurse(r-1,s,h restricted to labels 1,...,r-1)
    else:
        draw s independent uniform old transpositions, forming word u
        h := eval(u)
        v := exact prescribed-star sampler(r,k,inverse(h)*g)
    draw a uniform binary old/star pattern with s old and k star positions
    return inverse_stable_sort(u,v,pattern)
```

For the token sampler, start its token at `x`, choose each applied star factor with weight equal to the remaining `(D6)` completion count from the updated token, and reverse the applied sequence to obtain the displayed word. This enforces `eval(v)(x)=r` in the fixed multiplication convention.

For the low-rank DP, let `F_0(h)=1[h=e]` and `F_j(h)=sum_t F_(j-1)(h t)` on the at most 24 permutations. At endpoint `h`, choose the last displayed factor `t` with weight `F_(j-1)(h t)`, continue from `h t`, then reverse the collected choices. These exact conditional probabilities telescope to `1/F_L(g)` per valid word.

The denominator of a common rational representation of `c_r` divides the product of `j ceil(sqrt(j))` over `6<=j<=r`, so its bit length is `O(N log N)`. Computing all ceilings has polynomial bit complexity. Branch arrays have `O(L)` integers of `O(L log N)` bits. Exact binary-pattern and integer-weight draws use expected polynomial fair bits. Token sampling, endpoint updates, and the inverse stable sort use polynomial work (at most `O(L^2)` rewrites per rank).

Only one star-long branch can occur on a recursive path. The imported star sampler uses `O(r^3L^3)` rational operations; its truncated coefficient denominators divide products of factorials and powers of two with `O(poly(r,L))` total bit length. In particular the positive truncated series products admit a conservative `O(rL log(r+L))` bit bound on common denominators; numerator sizes are polynomially bounded in bits by the same positive count formulas. A conservative total bound is `O(N^4m^3)` exact arithmetic operations on polynomial-bit operands, polynomial space and polynomial expected fair bits. The constants do not hide an epsilon-dependent finite-rank table. This is expected polynomial Turing time, with Las Vegas integer-range rejection affecting runtime only.

## 9. Boundary and hypothesis audit

- `m=0`: return the empty word exactly for `g=e`; otherwise infeasible. This branch precedes the dense precondition.
- Odd `m`: the public identity target is empty. Arbitrary odd endpoints are feasible under the sign/minimal-length criterion, and the dense theorem applies to them under the same length condition.
- `m=2`: for the identity, draw a uniformly random transposition and output its pair. For arbitrary endpoints, enumerate all `binom(N,2)^2=O(N^4)` pairs and draw uniformly from those with the requested product. The preliminary `m<=2` enumeration branch handles this in polynomial time.
- `N=2`: one transposition, hence one word at every length; its endpoint is dictated by parity.
- `N=1`, if admitted: there are no generators; only `(m,g)=(0,e)` is feasible. The usual sign/length feasibility criterion is stated only for `N>=2`.
- Minimal endpoint length `N-cycles(g)`: exact factorization and pair padding prove feasibility. They do not imply a dense approximation theorem. No dense guarantee is asserted below its explicit rank floors.
- Pair padding: feasibility only; it is not used as a distributional argument.
- Growing `m` is part of the input/output size. Runtime is polynomial in the permutation degree `N` and the requested word length `m`, not in the number `log_2 N` of wires.
- No general computational hardness follows from an uncovered length/accuracy band.

## 10. Deterministic checks and fresh audit

The standard-library deterministic script was run with the exact command

```
python3 experiments/20260905-bridge-length-phase-diagram/roles/r2-dense-threshold/check_dense_threshold.py
```

At repository commit `9cc740b29eda6dd38adfde5f0aadc4a9c4eeb6fc`, Python 3.12.3, using no randomness or nonstandard packages, it passed with zero failures. `results.json` records the command, versions, commit and compact raw results. The tests checked:

- 11,202 exact rational rank-floor cases, including `N=1024` and the smallest admissible `q`; all ceiling gaps exceeded the claimed margin.
- 48,252 words, with exact backward-DP per-word probabilities at every endpoint, exact normalization, product convention and feasibility. This includes `S_3,m=4`, `S_4,m=4`, `S_4,m=6`, `N=2`, zero length, odd length and a minimal nontrivial endpoint length. Identity counts were respectively 27, 120 and 3936 in the three required cases.
- 8,028 exact projection recurrence/convolution equalities and 533,416 orientation equivalences through rank six.
- The new (D17) numerator estimate and exact full-bridge denominator at **every one of the 360 feasible labeled endpoints** for `r=6,q=12,L=B_6=380`, with next floor 240. The exact conditioning loss was at most `0.999999999887`, below the rigorous bound `2r(1+Delta)=12+o(1)`. The exact worst discarded bridge mass was approximately `0.0670209182764`, while the unconditioned cutoff mass was approximately `0.0670209182840`.

The last test deliberately uses small density, where the final asymptotic error bound is loose, to exercise nonnegligible discarded mass and the pivotal conditioning estimate. These finite checks can refute the formulas; the general theorem is proved in Sections 3--7. A fresh nonauthor audit is requested against this frozen report and will be recorded separately by the coordinator.

## 11. Residual open primitive and verdict

The requested dense scale is achieved. The first remaining rank-recursive primitive outside the proved short/dense regimes is the exact or tunably approximate **positive labeled connection sampler**: given feasible `(r,L,g)` and accuracy `epsilon`, draw `(k,h)` with weights (D5) in expected time polynomial in `r,L,log(1/epsilon)` without an `(r-1)!` labeled-endpoint inventory or a partition-scale type table. The new theorem bypasses this primitive only when its retained rank floors provide enough pointwise smoothing. It neither solves nor proves hardness of the intermediate regime.

The most valuable human review target is Lemma S, especially that old-long smoothing applies to discarded branches before they are sampled, and the exact projection in (D17) removes the factorial conditioning cost.

role: r2-dense-threshold
claim: For every feasible endpoint and q=floor(m/[2N(N-1)])>=4ceil(log_2 N), a positive retained-rank sampler has zero endpoint error and TV at most min(1,3N^2 exp(-q/144)); consequently m>=2N(N-1)ceil(144 log(3N^2/epsilon)) is a polynomial-time epsilon sampling regime.
status: proved
parameter_regime: N>=5, m part of the input, feasible g, q>=4ceil(log_2 N); N<=4 handled exactly at every feasible length.
target_distribution: Uniform law U_(N,m;g), including the public identity target at even lengths.
runtime: Conservative O(N^4 m^3) exact arithmetic operations on polynomial-bit integers/rationals; polynomial expected Turing time, space and fair bits.
error: Endpoint and length error zero; TV<=min(1,3N^2 exp(-floor(m/[2N(N-1)])/144)).
assumptions: Imported proved stable-sort bijection, exact Féray-based prescribed-star sampler, and Caputo--Liggett--Richthammer-based pointwise parity smoothing; exact fair random bits.
evidence: Theorem D and Lemma S, equations (D1)--(D19); check_dense_threshold.py and results.json, with zero failures in all deterministic checks.
independent_checks: Coordinator independently identified the same O(r) projection transfer and preliminarily checked (D1)--(D19); fresh final-report nonauthor audit pending and to be recorded separately.
first_unproved_step: Polynomial-time positive labeled connection sampling outside the retained dense domain, or a hybrid primitive covering the resulting intermediate band.
verdict: promote
