# Independent proof audit: irreducibility, pair domination, and squares

## Common convention

Permutations are maps on `[N]`, and `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`. A word evaluates as `t_1...t_m`. Write
`T=T_N`, `M=|T|=binom(N,2)`, and let `F_r(g)` be the number of ordered
length-`r` transposition words with product `g`.

The target is the uniform law on

```text
Omega(N,m)={w in T^m:t_1...t_m=id}.
```

For `N>=3` and even `m>=4`, `K` is exactly the kernel in `GOAL_SPEC.md`.

## A. Irreducibility audit

### A.1 Convention translation

Ben-Itzhak--Teicher, arXiv:math/0110110v1, Definition 1.3, uses

```text
R_k:(a,b) -> (aba^{-1},a).
```

This preserves `ab` in the present multiplication convention. Its inverse is

```text
(a,b) -> (b,b^{-1}ab),
```

the project right-Hurwitz generator. The generated equivalence relations are
therefore identical.

Their Theorem 3.4 states, for two factorizations of `id in S_N` with the same
number of factors, all factors transpositions, that they are Hurwitz-equivalent
if and only if their factorization graphs have matching labeled vertex sets
and total factor counts (weights) component by component. Definition 3.1 fixes
the graph vertex set to all of `[N]`, so isolated labeled vertices are included.
These are exactly the hypotheses needed below; no simultaneous conjugation or
unlabelled relabeling is present in the theorem.

### A.2 Every Hurwitz move is an `H_3` transition

For a pair at positions `j,j+1`, if `j<=m-2`, select the window
`j,j+1,j+2` and retain the third factor. If `j=m-1`, select the window
`m-2,m-1,m` and retain the first factor. Rewriting the selected adjacent pair
by either Hurwitz generator preserves its two-factor product, hence preserves
the padded triple product. The desired triple is in the exact conditional
fiber and has positive transition contribution

```text
1/[2 |R_m| (m-2) F_3(h)].
```

This covers both endpoints. Since choosing the first two transpositions
determines the third if it exists, `F_3(h)<=M^2`; hence every nontrivial chosen
rewrite has contribution at least `1/[6(m-2)M^2]`. This probability bound does
not bound the number of rewrites supplied by the classification.

### A.3 A paired representative exists in every Hurwitz class

Partition the factors of `w` by the connected components of its support graph.
Factors in different components commute. Reordering only across components
shows that the subword on each nonisolated component `C` has product identity:
the component products have disjoint supports, and their product is identity,
so restriction to `C` is identity.

Let `v=|C|` and let `k_C` be its number of factors. The sign gives `k_C`
even. For completeness, `k_C>=2(v-1)` follows directly. Along the component
subword, multiplication by a transposition either merges two cycles of the
current prefix permutation or splits one cycle. The prefix begins and ends at
identity, so the numbers of merges and splits agree and each is `k_C/2`.
Before the support graph becomes connected, each of the `v-1` edges that first
joins two current support-graph components has endpoints in distinct prefix
permutation cycles, and is therefore a merge. Thus `k_C/2>=v-1`.

Choose a labeled tree on `C` with edges `e_1,...,e_{v-1}` and set

```text
q_C=(e_1,e_1,...,e_{v-1},e_{v-1},
     e_1,e_1,...,e_1,e_1),
```

where the tail has `(k_C-2(v-1))/2` square pairs. It is an identity word of
length `k_C`, and its support graph has exactly vertex set `C` and weight
`k_C`. Concatenating these words over all nonisolated components preserves all
labeled components, all component weights, and all isolated vertices. Theorem
3.4 therefore supplies a finite Hurwitz path from `w` to this paired word.
Section A.2 turns it into a positive-probability `K` path.

### A.4 Every adjacent square is refreshable by `H_4`

Every adjacent position pair in a word of length at least four lies in a
contiguous length-four window. Within such a window,

```text
A (t,t) B = A B = A (s,s) B
```

for any transpositions `s,t`, including when either `A` or `B` is empty inside
the window. Keeping the two other factors fixed gives a legal `H_4`
replacement with contribution

```text
1/[2 |R_m| (m-3) F_4(h)] > 0.
```

Since `F_4(h)<=M^3`, this is at least `1/[6(m-3)M^3]`. At `m=4`, this is the
whole-word update `H_{1,4}`; its coefficient among updates is exactly `1/4`.

### A.5 Conclusion

Refresh every adjacent square in the paired representative to
`tau=(1,2)`. This reaches the universal word
`(tau,tau,...,tau,tau)` in at most `m/2` nontrivial square refreshes. Exact
heat-bath replacements are reversible within their conditional fibers, so any
two states communicate through this word. Hence `K` is irreducible for every
`N>=3` and even `m>=4`.

The classification path length, an algorithm for finding it, and its
congestion are not quantitatively bounded. The universal word is only a
connectivity device and cannot be used as a polynomial-congestion hub.

## B. Adjacent-pair Dirichlet comparison audit

Define

```text
J=(1/2)I + [1/(2(m-1))] sum_{j=1}^{m-1} H_{j,2}.
```

Each `H_{j,2}` is an exact heat bath for the same uniform bridge law, so `J`
is reversible for that law.

### B.1 The scan index of an off-diagonal `J` transition is unique

Suppose the old pair is `(a,b)`, the new pair is `(c,d)`, and `ab=cd`. If
`a=c`, left cancellation gives `b=d`; if `b=d`, right cancellation gives
`a=c`. Therefore a nontrivial pair replacement changes both coordinates. If
`x!=y` is generated at scan `j`, its discrepancy set is exactly `{j,j+1}`,
which determines `j` uniquely. Thus the full off-diagonal point probability is

```text
J(x,y)=1/[2(m-1)F_2(p)],
```

not merely the contribution from one of several scans.

### B.2 Padding and the exact ratio

For the unique scan `j`, pad the pair on the right by the unchanged factor at
`j+2` when `j<=m-2`, and on the left by the unchanged factor at `m-2` when
`j=m-1`. The corresponding `H_3` fiber contains `y`, so

```text
K(x,y) >= 1/[2|R_m|(m-2)F_3(h)].
```

Fixing the final transposition gives, with the present convention,

```text
F_3(g)=sum_{c in T} F_2(gc).
```

Choosing the first factor of a length-two word determines the second, so
`F_2(u)<=M` and `F_3(g)<=M^2`. Feasibility gives `F_2(p)>=1`, while

```text
(m-1)/[|R_m|(m-2)] >= 1/3
```

for every `m>=4` (at `m=4`, `|R_m|=2`; otherwise it is at most three).
Therefore every off-diagonal ordered pair satisfies

```text
K(x,y)/J(x,y) >= 1/(3M^2).
```

Both chains have the same stationary law. Summation in the reversible
Dirichlet forms and minimization over nonconstant functions give

```text
E_K(f,f) >= E_J(f,f)/(3M^2),
gap(K) >= gap(J)/(3M^2).
```

The same classification argument actually proves qualitative irreducibility
of `J`: its `H_2` updates directly realize Hurwitz moves and directly refresh
an adjacent square. This observation supplies no quantitative gap bound.

The known `L=2` warning in the large-block route concerns simulation using
subwindows contained *inside* a two-letter block, where no `{3,4,5}` window
exists. The comparison here uses a third, unchanged factor outside the chosen
pair (inward at an endpoint). It is a one-step global-word domination, not an
internal length-two block simulation.

## C. Stationary adjacent-square audit

Let `P` be simple random-transposition walk and `p_k=P^k(id,id)`. Since every
word has iid probability `M^{-m}` before endpoint conditioning,

```text
|Omega(N,m)|=M^m p_m.
```

For any fixed `j`, deletion of an adjacent `(t,t)` and insertion at the same
position are inverse bijections between

```text
Omega(N,m-2) x T
```

and identity words with a square at `j,j+1`. Consequently

```text
Pr_pi(t_j=t_{j+1})
  = M |Omega(N,m-2)|/|Omega(N,m)|
  = p_{m-2}/(M p_m).
```

The count for each fixed label `t` is exactly `|Omega(N,m-2)|`, so the label
conditional on a square is uniform.

The matrix `P` is a self-adjoint contraction in counting-measure `l^2(S_N)`.
For its positive spectral measure at `delta_id` and even `m`,
`lambda^m<=lambda^{m-2}` on `[-1,1]`; hence `p_m<=p_{m-2}` and the displayed
probability is at least `1/M`. A stationary `J` step first survives the
explicit one-half holding choice, then selects a position uniformly, and on a
square chooses one of `M` labels uniformly. Its exact changed-square rate is

```text
(1/2) [p_{m-2}/(M p_m)] (1-1/M),
```

and is at least `(1/2)(1/M)(1-1/M)`.

This is an average under stationarity. It neither asserts that every word has
a square nor lower-bounds the boundary flow of an arbitrary cut.
