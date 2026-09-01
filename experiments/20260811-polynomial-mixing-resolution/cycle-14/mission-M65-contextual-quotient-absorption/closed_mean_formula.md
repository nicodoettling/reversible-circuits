# Exact contextual conditional-mean formula

Date: 2026-08-12.  This note concerns only the nonlazy minimal-long-cycle
parking projection.  It does not concern the identity-bridge chain `K`.
Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply
left-to-right.

## 1. Statement

Fix an outer root composition with `K>=1` branches and split its branch
`i` into a left part and a suffix of size `B>=1`.  Let

```text
R=K-i-1
```

be the number of outer branches to the right of the split branch.  In the
standardized split branch, condition on the inner root composition

```text
C=(c_1,...,c_k),       t=c_k.
```

Let `phi` be the contextual split rate divided by
`alpha_r=2/[3r(r-1)]`, and put

```text
w_a=a^(a-1)/a!.
```

**Theorem (closed contextual mean).**  For every ambient rank, every
outer context above, and every feasible inner composition,

```text
E[phi | C] = 0,                                      t<B,

E[phi | C] = T_(K,R)(k),                            t=B,

E[phi | C] = [w_(t-B)w_B/w_t] D_(K,R)(k),           t>B,       (1.1)
```

where

```text
T_(K,R)(k)
 =K binom(k+K-R-2,K-R-1)/binom(k+K-1,K-1),          (1.2)

D_(K,R)(k)
 =1-binom(K,R+1)/binom(K+k,R+1).                    (1.3)
```

Thus the conditional mean depends on the outer context only through
`(K,R)`, and on the inner composition only through `(k,t)`.

## 2. Uniform two-chain deletion lemma

For a fixed parking macro, Stanley--Biane identifies its factor words
with all permutations of its lower-endpoint multiset.  Occurrences of a
vertex label are the attachment factors of its ordered children, in the
reverse child order.  Consequently, after deleting every factor except
the `K` outer-root attachments and the `k` inner-root attachments, the
remaining word is a uniformly random shuffle of two ordered chains

```text
O_1<...<O_K,       I_1<...<I_k.                     (2.1)
```

Here `O_(R+1)` is the attachment of the outer branch being split and
`I_1` is the attachment of its last inner root branch.  The positions of
the `K+k` retained factors among all `r` factor positions are uniform and
independent of their binary order.  Hence any fixed adjacent pair in the
binary restriction is adjacent in the full word with probability

```text
(K+k)/r.                                            (2.2)
```

These statements remain true after fixing all other branch macros:
deletion has the same number of inverse insertions for every binary word.
This is also the direct multiset-word version of the constrained-shuffle
bijection used in M56.

## 3. Terminal count `t=B`

At equality, the cut factor is `I_1`.  The two coarse rank-two outcomes
put `O_(R+1)` and `I_1` in the two possible orders.  They are adjacent in
the binary restriction precisely when it starts with either

```text
O^R O I       or       O^R I O.
```

After this displayed prefix is removed, the remaining word has `k-1`
inner and `K-R-1` outer letters.  Therefore the number of favourable
binary words is

```text
2 binom(k+K-R-2,K-R-1),                             (3.1)
```

out of `binom(K+k,K)`.

For each favourable word, (2.2) gives full-word adjacency.  The scan
selects that site with probability `1/(r-1)`, and the exact three-state
rank-two heat bath selects the split outcome with probability `1/3`.
After division by `alpha_r`, the normalized rate is

```text
[r/2] [(K+k)/r]
 [2 binom(k+K-R-2,K-R-1)/binom(K+k,K)]

=K binom(k+K-R-2,K-R-1)/binom(k+K-1,K-1),
```

which is (1.2).  This calculation retains both coarse orientations and
does not add an extra factor two for the single split target.

## 4. Deep count `t>B`

Now the marked cut factor lies strictly inside the last inner branch.
Let `J` be the number of inner attachment factors which precede
`O_(R+1)` in the uniform two-chain shuffle.  A marked opportunity can
continue into the last branch exactly when

```text
I_1 precedes O_(R+1), equivalently J>=1.            (4.1)
```

Conditionally on `J=j>=1`, marked deletion and insertion identify the
last-branch statistic with a synthetic child attachment context having
`K+k` attachments and `R+j` before the same active factor.  The exact
negative-hypergeometric weights and pointwise recursion are proved in
`marked_context_inheritance.md`.  In particular this is a mixture of child
contexts, not a scalar multiple of the ordinary `(k,0)` child.

The complement of (4.1) says that the first `R+1` symbols of the uniform
binary shuffle are all outer symbols.  Sampling these symbols without
replacement gives

```text
P(I_1 precedes O_(R+1))
 =1-(K)_(R+1)/(K+k)_(R+1)
 =1-binom(K,R+1)/binom(K+k,R+1).                    (4.2)
```

Every synthetic child context has the same stationary mean: summing its
marked opportunities is exactly the stationary-flow split from the
one-part composition `(t)` to `(t-B,B)`.  M50's exact reverse root-split
formula says that its rate divided by the relevant `alpha` is

```text
w_(t-B)w_B/w_t.                                    (4.3)
```

Summing the marked child mixture multiplies (4.3) by (4.2), proving the
deep line of (1.1).  If `t<B`, the right-spine suffix cannot fit in the
last branch, giving the first line of (1.1).

## 5. Exact bounded falsification and scope

`closed_mean_formula.py` compares (1.1) with every exact contextual mean
through ambient `r=7`.  The computation may refute (1.1) but cannot prove
it.  The universal proof is the marked multiset deletion/insertion count
above.

The theorem removes the unknown contextual shape dependence from M56's
scalar problem.  It does **not** prove contextual quotient absorption:
the remaining obligation is the explicit weighted-composition inequality

```text
||H-E H||_(-1,R_s)^2
 <= E[phi 1_(last part=B)],                         (5.1)
```

with `H(C)` given by (1.1).  Nor does it solve M56's separate actual-edge
marked source-recovery problem.  It is therefore auxiliary and
nonterminal for both the parking projection and `K`.
