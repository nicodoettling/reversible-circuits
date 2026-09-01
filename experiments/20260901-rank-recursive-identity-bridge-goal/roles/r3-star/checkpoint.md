# R3 halfway checkpoint

Date: 2026-09-01

## Named claim: positive support decomposition gives a polynomial exact sampler

Fix `N >= 1`.  Permutations are maps with
`(p q)(x)=p(q(x))`, and a displayed word `t_1 ... t_k` has that product.
The star is at `N`, with generators `(i N)`, `i<N`.

For `q in S_N`, let `mu(q)` consist of every nontrivial cycle length of `q`,
together with one part `1` when `q` fixes `N`.  Let `f(q)` be the number of
fixed points of `q` in `[N-1]`.  If `T_k(lambda)` is the number of transitive
length-`k` star factorizations of any permutation of cycle type `lambda` on
`|lambda|` active labels, then the following positive formula is proved by
partitioning words according to their exact support:

```text
A_N(k,q) := [q] J_N^k
          = sum_(s=0)^f(q) binom(f(q),s) T_k(mu(q) union 1^s).       (C1)
```

Féray, *Partial Jucys--Murphy elements and star factorizations*, Theorem
1.2 (arXiv:0904.4854v2; published in EJC 33 (2012), 189--198), gives for
`lambda |- n`

```text
T_k(lambda)
 = (k!/n!) (product_i lambda_i)
   [t^g] f(t)^(n-2) product_i f(lambda_i t),
g = k-(n+ell(lambda)-2),
f(t)=2 sinh(t/2)/t.                                           (C2)
```

This source uses the identical convention
`rho sigma(j)=rho(sigma(j))`; Theorem 1.2 is explicitly arbitrary-length and
transitive.  All coefficients of `f(a t)` are nonnegative rationals, so
(C1)--(C2) are a positive exact count, not a signed character sampler.

Given these counts, partition by the last factor:

```text
A_N(r,q) = sum_(i<N) A_N(r-1, q(i N)).                         (C3)
```

Choose `i` with probability equal to its summand divided by `A_N(r,q)`, set
the prefix endpoint to `q(i N)`, and recurse.  Induction on `r` proves that
the resulting actual labeled word is exactly uniform in the prescribed
endpoint fiber.

## Why (C1) is exact

A word has a unique used set `U subseteq [N-1]`.  Every moved nonpivot label
of `q` must lie in `U`; any other member of `U` is a fixed point of `q`.
On `{N} union U`, using every generator indexed by `U` is exactly transitivity
of the star factorization.  Supports with the same number `s` of optional
fixed points have the same endpoint cycle type, and there are
`binom(f(q),s)` such labeled supports.  This gives the disjoint positive sum.

## Feasibility and minimality

If the cycle containing `N` has length `a` and the nonpivot nontrivial cycles
have lengths `b_1,...,b_r`, then

```text
ell_star(q) = (a-1) + sum_j (b_j+1)
            = (N-cycles(q)) + 2r.                             (C4)
```

For `N>=2`, the fiber is nonempty exactly when
`k>=ell_star(q)` and `k=ell_star(q) mod 2`; append `(1 N)(1 N)` for pair
padding.  For `N=1`, only `(k,q)=(0,e)` is feasible.  This includes `N=2`,
where the sole word is forced by parity.  Irving--Rattan, *Minimal
Factorizations of Permutations Into Star Transpositions*, Theorem 1.1 and
Corollary 1.2 (arXiv:math/0610640v2), agree with (C4) and give the minimal
count obtained from the `s=0,g=0` term of (C1)--(C2).

## Natural orbit DP and its limitation

The `H=S_(N-1)` conjugacy orbit of an endpoint is described exactly by

```text
(a,lambda),
a = length of the cycle containing N,
lambda = partition of the remaining N-a cycle lengths.
```

Right multiplication by a star factor has positive transitions:

- join a nonpivot `j`-cycle to the pivot cycle with multiplicity
  `j*m_j(lambda)`;
- split the pivot cycle into pivot length `b` and nonpivot length `a-b`, once
  for every `1<=b<a`.

These multiplicities total `N-1` and give an exact bridge-count/backward-
sampling DP.  Its state count is exactly

```text
sum_(u=0)^(N-1) p(u),                                         (C5)
```

so this named implementation is partition-scale and superpolynomial.  Formula
(C1) bypasses rather than compresses this full table.

## Complexity checkpoint

Truncate (C2) at degree at most `k`.  A direct convolution uses
`O(N k^2)` rational operations per transitive count and (C1) uses at most `N`
such counts.  Recomputing all `N-1` last-factor weights at all `k` backward
steps therefore takes a conservative `O(N^3 k^3)` exact rational operations.
All intermediate numerators and denominators have polynomial bit length; a
detailed bound and random-bit accounting will be in the final report.

## Exact evidence completed

`run_checks.py` compares (C1)--(C2), the pointed-orbit DP, and direct labeled
endpoint walks for every endpoint through `N=5,k=6`.  Current results:

```text
1071 exact endpoint-count equalities
918 exact last-factor recurrence equalities
153 labeled orbit-transition-multiplicity equalities
```

The boundary table covers `N=1`, `N=2`, `k=0`, parity failures, minimal
lengths, and pair padding.  Fixed-seed word-level sampler smoke tests all
evaluated to the requested endpoint.  The empirical frequencies are only a
diagnostic; exactness comes from (C3).

## Current status

The named R3 claim is **proved, pending independent audit**.  The remaining
lane work is a line-by-line complexity proof, a stronger superpolynomial
state-count bound for (C5), final artifact hygiene, and the required report.
