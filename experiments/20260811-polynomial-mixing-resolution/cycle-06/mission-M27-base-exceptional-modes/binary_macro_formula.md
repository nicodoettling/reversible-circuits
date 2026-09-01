# Exact binary parking-macro formula and two-hop bypass

## Statement

Fix integers `a,b>=1`, put `r=a+b` and `n=r+1`, and use the
long-cycle endpoint `c=(0 1 ... r)`.  Permutations compose as
`(pq)(x)=p(q(x))`, and factor tuples multiply left-to-right.  Let `L_n`
be the nonlazy random-scan heat bath which chooses one of the `r-1`
adjacent raw transposition pairs and resamples it uniformly conditional on
its ordered product.  Project `L_n` by the sorted Stanley parking labels,
and call the projected kernel `bar L_n`.

Define

```text
alpha = 0^a 1^b,
beta  = 0^(a+1) 1^(b-1).
```

Then

```text
bar L_n(alpha,beta)
  = 2/[3(r-1) binom(r,a)].                              (1)
```

Thus (1) is exponentially small when `a` and `b` are balanced.  It
rigorously refutes direct polynomial-rate domination of this Dyck lowering
edge.

This rare edge has a polynomial two-hop bypass.  If `b>=2`, put

```text
gamma = sort(0^a 1^(b-1) b).
```

Then

```text
bar L_n(alpha,gamma)
  = 2b/[3r(r-1)],                                       (2)

bar L_n(gamma,beta)
  = 2/[3r(r-1)] [1-1/binom(r-1,a)]
  >= 1/[3r(r-1)].                                      (3)
```

Consequently the balanced binary family is not a bottleneck of the projected
chain merely because its direct Dyck edge is rare.

## Proof

### 1. The only two raw noncrossing trees

Every transposition in a factorization with parking-label multiset
`0^A1^B` has smaller endpoint zero or one.  Hence every vertex
`j>=2` is adjacent only to `0` or `1`.  Connectivity and acyclicity
leave exactly two possibilities for connecting the two centers:

1. the edge `(0,1)`; or
2. a unique common neighbor `k`, with edges `(0,k),(1,k)`.

Noncrossing forces a threshold.  In the first case, vertices
`2,...,B+1` attach to `1` and vertices `B+2,...,r` attach to
`0`.  In the second case, all vertices below `k` attach to `1`
and all vertices above `k` attach to `0`; the counts force
`k=B+1`.  Denote these trees by `T_E(A,B)` and `T_V(A,B)`.

The Goulden--Yong cyclic-neighbor order gives the following edge posets.
Precisely, this is the local order from Goulden--Yong, Theorem 2.2(f3),
together with Proposition 2.4 and Lemma 2.5: after numbering factors in word
order, incident edge numbers decrease clockwise across the interior, and
these local inequalities characterize the valid numbered noncrossing chord
diagrams.  We use the zero-based cyclic relabeling of their vertices and the
same right-to-left permutation-composition convention.
For `T_E`, all edges form one chain, whose unique parking-label word is
`0^A1^B`.  For `T_V`, write the zero-edge chain and one-edge chain as

```text
z_1 < ... < z_A,
o_1 < ... < o_B.
```

The sole cross relation is

```text
o_1 < z_A.                                              (4)
```

Thus the linear extensions of `T_V` are all binary words with `A`
zeros and `B` ones except `0^A1^B`.  Their number is
`binom(A+B,A)-1`; together with the unique `T_E` extension this gives
the required parking-orbit size `binom(A+B,A)`.

These assertions can also be checked directly from the cyclic order at
vertices `0,1,B+1`: the zero edges occur in decreasing larger endpoint,
the one edges occur in decreasing larger endpoint, and the common-neighbor
edges impose (4).  No further cross relation exists because the unique path
between the two edge chains passes through those two common-neighbor edges.

### 2. The exponentially rare direct edge

For `alpha`, use `A=a,B=b`.  A rank-two fiber changes one zero label
and one one label into two zero labels precisely when it flips the triangle
on vertices `0,1,b+1`.

In `T_E(a,b)`, the relevant factors are the final zero edge `(0,1)`
and the first one edge `(1,b+1)`; they are adjacent in the unique linear
extension.  In `T_V(a,b)`, they are `z_a=(0,b+1)` and
`o_1=(1,b+1)`.  Relation (4) and the two chain orders make them adjacent
in exactly one extension:

```text
0^(a-1) 1 0 1^(b-1).
```

Hence exactly two of the `binom(r,a)` source words can cross to `beta`.
For either word there is one relevant scan position; its two-transposition
fiber has size three, and exactly one outcome has macro `beta`.  Averaging
gives (1).

### 3. First bypass edge

The transition `alpha -> gamma` flips two one-labeled edges into one
one-labeled edge and one `b`-labeled edge.  In `T_E(a,b)` the first
two one edges are adjacent, giving one favorable word.

In `T_V(a,b)`, require `o_1,o_2` to be adjacent and contract them.
There remain `a` zero objects and `b-1` one objects.  Relation (4)
requires the contracted first-one object to occur before `z_a`.  Of the
`binom(r-1,a)` interleavings, exactly the all-zeros-before-all-ones word
violates this.  Thus `T_V` contributes `binom(r-1,a)-1` and the two
trees together contribute `binom(r-1,a)` favorable source words.

From a special three-state fiber, both nonspecial outcomes have macro
`gamma`, so each favorable word contributes probability
`2/[3(r-1)]`.  Since

```text
binom(r-1,a)/binom(r,a)=b/r,
```

equation (2) follows.

### 4. Second bypass edge

Now view `beta` as `0^A1^B` with `A=a+1,B=b-1`.  Its
`T_E` tree has no relevant special pair.  In `T_V`, the common
neighbor is `k=b`, and the last two zero edges
`z_{A-1}=(0,b+1)`, `z_A=(0,b)` form the special pair whose two
nonspecial outcomes have macro `gamma`.

Contract these two zero edges.  The same two-chain count gives
`binom(r-1,a)-1` favorable `beta` words.  Therefore

```text
bar L_n(beta,gamma)
 = 2[binom(r-1,a)-1]/
   [3(r-1)binom(r,a+1)].                               (5)
```

Uniform stationary mass is proportional to orbit size, and

```text
|gamma|=(a+1)|beta|.
```

Detailed balance in (5), together with

```text
(a+1) binom(r,a+1) = r binom(r-1,a),
```

proves (3).  The displayed lower bound follows because `b>=2`, so
`1<=a<=r-2` and `binom(r-1,a)>=2`.

## Scope and calibration

The argument is exact for every `a,b>=1` in (1), and every `a>=1,b>=2`
in (2)--(3).  It keeps the scan normalization `1/(r-1)`, the three-state
rank-two fiber normalization `1/3`, and both nonspecial target outcomes.
As a raw long-cycle-factorization theorem it allows either parity of `r`;
its application to the paired-increment bridge requires `r=2l`, equivalently
an odd `n=r+1`, because every two-transposition increment is even.
For `(a,b)=(2,2),(2,3),(3,2)`, respectively, the direct rates are
`1/27,1/60,1/60`; the two bypass rates are
`(1/9,1/27),(1/10,1/36),(1/15,1/40)`.  These values agree with exact
enumeration.  This result rejects one proposed projected bottleneck; it is
not a general polynomial-congestion theorem for all parking multisets.
