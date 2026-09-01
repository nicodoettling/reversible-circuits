# M31 halfway checkpoint: logarithmically growing shells still leak polynomially

## Frozen scoped theorem

Use `(pq)(x)=p(q(x))` and words `t_1...t_m`.  Put

```text
M=binom(N,2),  E=binom(N-1,2),  m=4N^3+4,
a_*(N)=max(3,floor(log N)),
V^(0)={w:c(w)>=2},
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.
```

For the original lazy exact `{3,4,5}` heat-bath chain and every `N>=5` and
`1<=a<=a_*(N)`, the proof below gives universal `C_0=5,000,000` with

```text
pi(V^(a)) <= exp(-4N^2) < 1/2,
Phi_pm^K(V^(a))
 >= 1/[288 N C_0^a (m-4) M^4 E^5]
 >= N^(-60).                                             (C.1)
```

Thus a genuinely growing family of shells is not a superpolynomial
bottleneck.  This is not a conclusion about radii larger than logarithmic.

## Structural product-cluster envelope

Fix a path of at most `a` local updates from a disconnected word and choose a
nontrivial vertex cut `P` between its initial support components.  Decompose
the update intervals into connected components under overlap.  If a component
contains `q` intervals, its hull has length at most `4q+1`.  Its hull product
is unchanged through the path and therefore belongs to the cut subgroup
`H_P`.  Inactive components can be discarded because all their final factors
are internal.  Consequently every `y in V^(a)` has disjoint active hulls
`J_1,...,J_c`, positive integers `q_j` with `sum q_j<=a`, such that

```text
|J_j|<=4q_j+1,
product(y|J_j) in H_P,
all P-crossing factors of y lie in union_j J_j.          (C.2)
```

Conversely, if at most `a` disjoint intervals of lengths in `{3,4,5}` cover
all crossings and each displayed block has an internal same-length
factorization of its ordered product, resampling those intervals reaches a
disconnected word.  This gives a rigorous inner/outer sandwich with the
endpoint-product condition retained; a support-only cover is not asserted to
be sufficient.

For a cut with `e` internal and `x=M-e` crossing transpositions, the number of
active length-`l` blocks is

```text
A_l(P) <= l^2 x M^(l-2).                                (C.3)
```

Indeed, mark the first and last crossing positions.  Choose the first
crossing edge and every factor except the last crossing edge.  The suffix
after that edge is internal.  On the cut side as a set, subgroup membership
then forces the last transposition to exchange the unique symmetric-difference
pair, if such a transposition exists.  Hence it has at most one choice.

## Constant-per-radius shell count

Let the smaller cut side have size `s`.  For fixed active hull products, the
outside internal segments combine because the internal transposition sum is
central in `H_P`.  Splitting an outside length `t` into two nearly equal
parts and applying Cauchy--Schwarz, together with the frozen dense direct-
product trace estimate, gives uniformly

```text
[g]T_P^t <= 4e^t/|H_P|.                                 (C.4)
```

The density hypothesis holds since `t>=m-5a_*`.

The cost of a cluster charged with `q` updates is at most

```text
sum_{l=2}^{4q+1} m l^2 x M^(l-2)/e^l
 <= s (2,100,000)^q.                                    (C.5)
```

Here `mx/M^2<=26s`, `M/e<=5/2` for `N>=5`, and
`q^3<=8^q`.  Summing ordered compositions of at most `a` gives at most
`3(C_0s)^a`, where `C_0=5,000,000`.  Therefore the words charged to a fixed
cut are at most

```text
12(C_0s)^a e^m/|H_P|.                                  (C.6)
```

Writing `e_s=binom(s,2)+binom(N-s,2)`, summing labeled cuts relative to an
isolate cut gives

```text
sum_s [binom(N,s)^2/N] (C_0s)^a (e_s/E)^m
 <= 2N C_0^a.                                          (C.7)
```

For `s>=2`, use
`E-e_s=(s-1)(N-s-1)` and `m/E>=8N`.  The logarithm of each non-isolate
summand is at most

```text
2s log N + a log(C_0s)-8N(s-1)(N-s-1) <= 0.            (C.8)
```

For `5<=N<=54`, `a<=3`; for `N>=55`, `a<=log N`.  In both ranges the last
inequality follows already from the endpoint `s=2`; the displayed positive
part is bounded by `N log N+3log(C_0N)` in the first range and by
`N log N+log N log(C_0N)` in the second.  The isolate term is `NC_0^a`, and
there are fewer than `N` remaining sizes.  Thus

```text
|V^(a)| <= 24N C_0^a E^m/(N-1)!.                       (C.9)
```

Since `|Omega(N,m)|>=2M^m/N!` and `E/M=1-2/N`, (C.9) yields

```text
pi(V^(a))<=12N^2C_0^a(1-2/N)^m<=exp(-4N^2).            (C.10)
```

## Boundary family under final audit

Let `z=N`, `s=(z,1)`, and `q=(2,3)`.  For `L=4a-4`, choose arbitrary
internal `c_1,...,c_L`, put `g=c_1...c_L`, and take a robust internal tail
of length `n=m-(4a+1)` and product `(qg)^(-1)`.  Starting from the disconnected
prefix `q^5,c_1,...,c_L`, one `H_5` replaces `q^5` by
`(s,q,q,q,s)` and `a-1` further `H_5` moves push the last crossing factor
through the `c`'s four at a time.  The resulting source has its only crossing
positions at `1` and `4a+1` and lies in `V^(a)`.

The final audit is checking that:

1. at least half of every parity-compatible endpoint fiber consists of tails
   remaining connected after deletion of any `a` five-windows;
2. pushing the last crossing through the first four tail factors places it at
   `4a+5`, and the product-cluster envelope rules the target out of `V^(a)`;
3. the source count is `(1/2)E^(m-5)/(N-1)!`, independent of `a` apart from
   the robustness range; and
4. the exact original-chain transition probability is at least
   `1/[6(m-4)M^4]`.

No finite computation is used.  The universal claim being audited is (C.1),
not finite convergence or a fixed-radius extrapolation.
