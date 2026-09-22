# R1 independent proof candidate v1

Frozen 2026-09-22 05:55 UTC, before receiving R2's proof. Status: **proved by author, provisional pending nonauthor audit and finite checks**. Task `/root/r1_combinatorial`; target and cutoff are exactly T0/H0. No sampling implementation claim is certified by this document alone.

## 1. Law, normalizers, and scope

Products compose rightmost first. Let `m=2k`, `N>=2`, and `0<=2k<=N`. Let `Z(N,2k)=|Omega(N,2k)|`. Throughout, probabilities are under the global uniform law `U_(N,2k)`, equivalently independent uniform transpositions conditioned on product identity. This condition has already been paid for by the exact denominator `Z(N,2k)`; no unconditioned random-graph law is used.

Write `C(v,ell)` for the number of connected identity words on one fixed labeled set of size `v`. Set `C(1,0)=1` for an isolated label. For `v>=2`, the only feasible lengths are `ell=2(v-1+g)`, `g>=0`. Necessity follows by counting prefix permutation-cycle joins and splits; connectivity requires at least `v-1` joins, while identity requires equally many splits. A doubled spanning tree followed by repeated-edge pairs proves sufficiency.

Set

```
A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!,
S(n,j)=Z(n,2j)/(2j)!.
```

A labeled support macro is an unordered set of disjoint nontrivial blocks `B`, each with a genus `g_B`, with isolates implicit. Its normalized weight is

```
w(alpha)=product_B A_(g_B)(|B|),
cost(alpha)=sum_B (|B|-1+g_B).
```

There are exactly `(2j)! product_B C(|B|,ell_B)/ell_B!` ordered words with this macro: choose each internal ordered word and then one of `(2j)!/product ell_B!` order-preserving interleavings. Components commute and restriction to each block recovers these choices. Thus `S(n,j)=sum_(cost=j) w(alpha)` on the fixed `n`-label set.

For `X_(v,q)` the number of support components with `v` vertices and `2q` factors, exact marking gives

```
E X_(v,q)
 = binom(N,v) binom(2k,2q) C(v,2q) Z(N-v,2k-2q)/Z(N,2k)
 = binom(N,v) [C(v,2q)/(2q)!] S(N-v,k-q)/S(N,k).       (1)
```

The first binomial chooses the literal component labels. The second chooses its literal positions. A marked component has no extra `v!`, `q!`, or equal-component divisor. When a word has several components of the same type it is counted once for each mark, exactly as required by `X`.

H0 omits only components with **both** `v>K` and `g>=2`. It therefore suffices to bound the stronger event that any nontrivial component has `v>K`, with every genus included. Here `K` is always the original top-level cutoff.

## 2. Imported recurrence and convention check — R1-C1.v1

The only count input is Dubrovin--Yang--Zagier, *Classical Hurwitz numbers and related combinatorics*, Proposition 1 equation (13), with the ordered-word normalization in Section 1.2 equations (19)--(20). Their connected coefficients satisfy `C(v,ell)=v! ell! h_(g,v)`. The paragraph following equation (20) explicitly relates the disconnected counts, multiplied by `v!`, to ordered transposition tuples with product identity; the exponential formula then gives the same connected normalization. Connectivity is transitivity of edge-generated permutations. Word reversal translates the opposite multiplication convention bijectively if needed. The genus-zero value is `h_(0,v)=v^(v-3)/v!`, Section 1.3 immediately after equation (28).

Primary source checked directly on 2026-09-22:
https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf

Define `F_v(t)=sum_ell C(v,ell)t^ell/ell!`, with `F_1(t)=1`. Equation (13), or equivalently its equation (17), gives

```
v^2(v-1) F_v(t)
 = 2 sum_(a+b=v; a,b>=1) binom(v,a) a b^2
       (cosh(a t)-1) F_a(t) F_b(t).                    (2)
```

All coefficients are nonnegative; the splits are ordered. Also `A_0(v)=v^(v-3)` for `v>=1`, including `A_0(1)=1`.

## 3. Factorial genus majorant — R1-C2.v1

For every integer `v>=1`, put `B_v=(v^3-v)/36`. Then coefficientwise in `t^2`,

```
F_v(t) <= v^(v-3) t^(2v-2) exp(B_v t^2).              (3)
```

In particular, for all feasible `v>=2,g>=0`,

```
A_g(v) <= v^(v-3) B_v^g/g!.                          (4)
```

Proof. Let `H_v=F_v/[v^(v-3)t^(2v-2)]`, using `H_1=1`. Divide (2) by its genus-zero term to obtain

```
H_v(t)=sum_(a+b=v) p_(a,b) L(a t) H_a(t) H_b(t),
L(z)=2(cosh z-1)/z^2,
p_(a,b)=binom(v,a) a^a b^(b-1)/[(v-1)v^(v-1)].        (5)
```

Every `p` is nonnegative and `sum p=1`, either by extracting the genus-zero coefficient of (2), or the corresponding elementary Abel identity. The apparent quotient in `L` has constant term one.

Coefficientwise, `L(z)<=exp(z^2/12)`: for `j>=0`,

```
2/(2j+2)! <= 1/(12^j j!).                             (6)
```

Equality holds at `j=0,1`; the ratio of left/right at `j+1` divided by the same ratio at `j` is `12(j+1)/[(2j+4)(2j+3)]<=1`.

Induct on `v`. Products preserve coefficientwise inequalities for nonnegative series. For every split,

```
B_v-B_a-B_b = abv/12 >= a^2/12,
```

because `b(a+b)>=a` for `a,b>=1`. Therefore each summand of (5), apart from its probability `p`, is bounded coefficientwise by `exp(B_v t^2)`. Averaging proves (3). The proof controls all `g` simultaneously; it does not multiply marginal probability estimates.

## 4. Endpoint-conditioning ratio by fresh pairs — R1-C3.v1

For any fixed removed label set `V` with `|V|=v`, any `0<=q<=k`, and `D=N-2k+1>0`,

```
S(N-v,k-q)/S(N,k)
 <= binom(k,q) 4^q q!/D^(2q)
 <= (4k/D^2)^q.                                      (7)
```

Proof. Regard a macro `alpha` on `[N]\V` of cost `k-q` as a macro on `[N]` by isolating all labels in `V`. A nontrivial component on `s` labels has cost at least `s-1>=s/2`. Thus `alpha` uses at most `2(k-q)` labels and has `I>=N-2k+2q` isolates. Add `q` disjoint unordered pair components on these isolates. There are exactly

```
(I)_(2q)/(2^q q!)
```

matchings, and each new pair has normalized weight `A_0(2)=1/2`. Consequently the total final weight of these extension incidences from `alpha` is

```
w(alpha) (I)_(2q)/(4^q q!)
 >= w(alpha) D^(2q)/(4^q q!).                         (8)
```

This remains valid for `q=0`, with empty products. Conversely a final cost-`k` macro `beta` can have at most `k` pair components, and each preimage is specified by the `q` pair components deleted. Thus it has at most `binom(k,q)` preimages. The extra requirement that every label in `V` be isolated after deletion only reduces this number. The weight of an incidence is exactly the weight of `beta`, namely `w(alpha)2^(-q)`. Sum (8) over bases and count by final macros to obtain the first inequality. The second uses `q! binom(k,q)=(k)_q<=k^q`. Every factor in (7) is now accounted for without dividing by a guessed return probability.

## 5. Finite tail bound — R1-C4.v1

Assume `1<=k`, `2k<=N`; put

```
x=4k/D^2,
a=k^2(k+2)/(9D^2),
c=exp(1+a),
rho=c N x.
```

For every integer `J>=1`, if `rho<1`,

```
P[there exists a nontrivial support component with v>J]
 <= min(1, N c rho^J /[(J+1)^3(1-rho)]).               (9)
```

The left side is zero when `J>=k+1`, so that case needs no condition on `rho`.

Indeed combine (1),(7),(4), sum `q=v-1+g` (extending the nonnegative sum to all `g>=0`), and use the entire exponential series:

```
E X_v <= binom(N,v) v^(v-3) x^(v-1) exp(B_v x).       (10)
```

Only `v<=k+1` is feasible. For those `v`,

```
B_v x = v(v^2-1) k/(9D^2) <= v a.
```

The factorial bound `v!>=(v/e)^v` and `binom(N,v)<=N^v/v!` then give

```
E X_v <= N c rho^(v-1)/v^3.                          (11)
```

Sum (11) over `v>=J+1`, replace `v^-3` by `(J+1)^-3`, extend the geometric sum, and apply Markov's inequality to the total number of marked components. This is a union bound under the already normalized bridge law.

For H0 use `J=K(N,2k)`. Since `A` contains all words with components of size at most K, (9) bounds `1-Z_A/Z` directly. No g<=1-only assertion is being used.

## 6. Explicit negligible error — T0 and stronger separately versioned T1

Define the single explicit function, with natural logarithms,

```
eta(N)=1,                                         2<=N<2^160,
eta(N)=exp(-(log N)^2/[10 loglog N]),               N>=2^160.   (12)
```

For every `N>=2` and every feasible even `m` satisfying **T0** `m^5<=N^3`, H0's exact conditional law has global TV at most `eta(N)`.

In fact the same statement holds in the stronger separately named **T1** regime `m^3<=N^2`. Thus this proof would achieve the stretch range `m<=N^(2/3-delta)` for every fixed `delta>0`, with the same eta and cutoff, and includes the endpoint exponent `2/3`. T0 is retained unchanged.

Proof. Below the displayed threshold use the universal TV bound one. For `N>=2^160`, write `L=log N>=100`, and assume `m<=N^(2/3)`. Then `m<=N/2`, `D>=N/2`, and

```
k<=N^(2/3)/2,
k+2<=(5/2)N^(2/3),
a=k^2(k+2)/(9D^2)<=5/18<1,
c<e^2<8,
rho<=64 N^(-1/3)<=N^(-1/6)<=1/2.                    (13)
```

The penultimate bound uses `N>=64^6=2^36`.

For the exact top-level cutoff, the integer

```
v0=floor(2L/log L)
```

satisfies `1<=v0<=N`, `v0<=L`, and `2v0 log v0<=4L`. Thus `v0^(2v0)<=N^4<=(N+m+2)^4`, so `K>=v0>=L/log L`. The latter floor inequality follows from `L/log L>=1`.

Discarding the helpful cubic denominator in (9),

```
TV <=16 N exp(-K L/6)
   <=exp(log 16+L-L^2/[6 log L])
   <=exp(-L^2/[10 log L]).                           (14)
```

For the last step, `log L<=L/20` for `L>=100`: it holds at 100 and the ratio `(log L)/L` decreases thereafter. Hence `L^2/(15 log L)>=(4/3)L>=L+log16`, exactly the required gap between `1/6` and `1/10`.

Finally `(log N)/(10 loglog N)` tends to infinity. Therefore for every fixed `b>0`, (12) is at most `N^(-b)` for all sufficiently large N. The algorithm, cutoff, polynomial exponent, and error function do not change with b.

## 7. Boundaries, sampler dependency, and remaining audit obligations

- `m=0`: return the empty word exactly; all components are isolates.
- `m=2`: choose one uniform edge and repeat it. For `N>=2`, K>=2, so every component is allowed and the error is zero.
- `N=2`: every even-length bridge is the unique repetition of `(1 2)`; H0 includes it because K=2. T0 and T1 only need the feasible length subset but the boundary is exact for every even length.
- `N=1`: no positive-length bridge exists; `m=0` is the empty word.
- Odd `m`: the bridge space is empty by sign and no target uniform law exists.
- The H0 conditional sampler is nonempty at every even m for N>=2, because one repeated edge is an allowed size-two component.
- All approximation here is omission of exact identity words. No numerical approximation or local-chain convergence is used.

This tail proof does not itself verify the implementation of H0's g0/1 primitive or support-marked DP. Its mathematical sampler consequence depends on their exact uniformity and expected polynomial bit complexity, being audited by the coordinator/R3. Alternatively the stronger event bound supports the versioned subset allowing only components of size <=K, using only support-marked DP; that optional algorithm change is not silently substituted for H0 here.

No open mathematical step is identified in R1-C2--C4 by the author. Required next checks are finite rational normalization/falsification and a nonauthor audit of this frozen v1, including pair-extension reverse multiplicity. Claimed novelty here is the factorial genus majorant and its quantitative sparse maximum-component consequence; no literature novelty priority is asserted. The imported result is the DYZ count recurrence and genus-zero normalization.
