# Qualitative Irreducibility of the Exact Local Heat-Bath Chain

## Statement

Let `N>=3` and let `m>=4` be even. Let `T_N` be all transpositions of `S_N`,
let

    Omega(N,m)={w=(t_1,...,t_m) in T_N^m:t_1...t_m=id},

and let `K_{N,m}` be the exact lazy random-scan same-product heat-bath kernel
with block sizes `R_m={r in {3,4,5}:r<=m}` and the normalization in the run
manifest. Then `K_{N,m}` is irreducible on `Omega(N,m)`.

The same conclusion holds for `N=2` and even `m>=4` because the state space is
a singleton. Odd `m` gives an empty state space. The cases `m=0` and `m=2`
are outside the stated kernel regime; the former is a singleton, while for
`N>=3` the latter has multiple states and no allowed block update.

## Convention

Permutations act as maps on `[N]`, and `pq` means `p` after `q`:
`(pq)(x)=p(q(x))`. A word evaluates to `t_1...t_m` in this notation. The
project right Hurwitz rewrite is

    (a,b) -> (b,b^{-1}ab),

and its inverse is

    (a,b) -> (aba^{-1},a).

Both preserve the ordered product `ab`. The second displayed move is the
generator called `R_k` by Ben-Itzhak--Teicher.

## Lemma 1: Hurwitz rewrites are positive length-three updates

For `m>=4`, every adjacent right or inverse Hurwitz rewrite is a
positive-probability transition of a suitable `H_{i,3}` update.

Proof. Consider a pair at positions `j,j+1`. If `j<=m-2`, use the window
`j,j+1,j+2` and leave its third factor fixed. Replacing `(a,b,c)` by
`(b,b^{-1}ab,c)`, or by the corresponding inverse rewrite, preserves the
three-factor product because the first two factors retain product `ab`. If
`j=m-1`, use the window `m-2,m-1,m`, leave its first factor fixed, and rewrite
the last two. The proposed new window lies in the same nonempty conditional
fiber. The chain chooses `r=3` with weight `1/(2|R_m|)`, the selected window
with weight `1/(m-2)`, and that particular new word with probability
`1/F_3(h)>0`, where `h` is the window product. Thus the transition probability
is at least

    1/(2|R_m|(m-2)F_3(h))>0.

This also covers pairs at the left boundary. QED.

## Lemma 2: every state reaches an adjacent-square representative

For a word `w`, form its support graph on the fixed labeled vertex set `[N]`.
For each nonisolated connected component `C` of size `v`, let `k_C` be the
number of factors supported on `C`. Factors on distinct components commute.
After grouping components, the total product is a product of permutations
with pairwise disjoint supports; because it is the identity, each component
product is the identity. Hence `k_C` is even. The standard transitive
factorization lower bound gives `k_C>=2(v-1)`.

Choose a tree on the labeled vertices of `C`, with ordered edges
`e_1,...,e_{v-1}`. Define

    q_C=(e_1,e_1,...,e_{v-1},e_{v-1},
         e_1,e_1,...,e_1,e_1),

using `(k_C-2(v-1))/2` surplus copies of the final square pair. (When there is
no surplus, omit that tail.) This is a length-`k_C` identity word with support
component exactly `C`, and every factor appears in an adjacent equal pair.
Concatenate the `q_C` over components in a fixed order, obtaining `q(w)`.
Isolated labeled vertices remain isolated, so `q(w)` and `w` have exactly the
same labeled connected components and component weights.

Ben-Itzhak--Teicher, Theorem 3.4 of arXiv:math/0110110v1, says that two
identity factorizations of the same length into transpositions are
Hurwitz-equivalent exactly when those labeled component sets and weights
match. Its generator is the inverse project generator, so the equivalence
relations coincide. Therefore `w` is connected to `q(w)` by Hurwitz rewrites,
and Lemma 1 realizes the whole path inside `K_{N,m}`. QED.

## Lemma 3: adjacent square refreshes are positive length-four updates

Suppose positions `j,j+1` contain `(t,t)`. Because `m>=4`, there is a
contiguous length-four window containing both positions. Leave the other two
entries of that window fixed and replace `(t,t)` by `(s,s)` for any
transposition `s`. Since `t^2=s^2=id`, the ordered product of the window is
unchanged, irrespective of whether the pair is at the beginning, middle, or
end of the window. The proposed window therefore belongs to the same
conditional fiber. Its transition probability is at least

    1/(2|R_m|(m-3)F_4(h))>0.

For `m=4`, this is precisely the whole-word `H_{1,4}` update. QED.

## Proof of the theorem

Fix `tau=(1,2)` and define the universal square word

    c_m=(tau,tau,tau,tau,...,tau,tau)

with `m/2` adjacent pairs. Given any `w`, Lemmas 1 and 2 connect `w` to the
paired word `q(w)`. Apply Lemma 3 successively to its `m/2` adjacent pairs,
refreshing each to `(tau,tau)`. This connects `q(w)` to `c_m`.

Every heat-bath transition used above is reversible at the support-graph
level: the old and new windows lie in the same exact conditional fiber, so the
reverse replacement also has positive probability. Thus any two states
`w,w'` communicate through `w -> c_m -> w'`. The chain is irreducible. QED.

## What this proof does not show

The classification supplies a finite Hurwitz path but no polynomial
path-length, edge-load, or functional-inequality bound. Routing all states
through `c_m` would have congestion at least of order `1/pi(c_m)` and is
therefore unusable for rapid mixing. This theorem is qualitative and is not a
terminal resolution of the polynomial-gap question.
