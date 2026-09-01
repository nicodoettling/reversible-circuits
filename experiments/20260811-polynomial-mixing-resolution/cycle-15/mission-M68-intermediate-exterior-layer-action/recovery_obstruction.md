# M68 source-recovery audit

## 1. Fixed-word translate cover: the exact sufficient mechanism

Fix one two-component exterior macro `Gamma` at `m=2N-2`.  Its component
genera sum to one, so call the genus-one component `U`.  Let `G_Gamma` be the
set of words having a globally adjacent square `e,e` in `U` such that deleting
that pair leaves `U` connected.

A **fixed Hurwitz word** is a state-independent product of adjacent project
Hurwitz generators.  It acts bijectively on `Gamma`; every prefix is also a
bijection.  Suppose there are fixed words

```text
beta_1,...,beta_L,       length(beta_j)<=D,           (1.1)
```

such that

```text
Gamma=union_(j=1)^L beta_j^(-1) G_Gamma.             (1.2)
```

Then every subset `S subseteq Gamma` has

```text
sum_(x in S) K(x,Omega minus S)
 >= |S|/[6(m-2)M^2 L D],                             (1.3)
M=binom(N,2).                                         
```

Here `Omega minus S` may be replaced by the union of the within-`Gamma`
boundary and `F_N minus A`, so (1.3) remains useful when `S=C_k intersect
Gamma`.

To prove this, assign `x` to the least `j` with `beta_j x in G_Gamma` and
follow the prefixes of `beta_j`.  If the endpoint is outside `S`, charge the
first crossing.  If it remains in `S`, refresh its deletable square to one
cross edge between the two support components whose resulting minimal join
tree is not the one fixed tree underlying `A`.  Such a safe edge exists:
there are at least `N-1` cross edges and at most one produces the fixed tree.

One Hurwitz step, padded on an available side, is one specified H3 outcome.
For an arbitrary three-transposition product its conditional fiber has size
at most `M^2`, so its literal K probability is at least

```text
p_H=1/[6(m-2)M^2].                                   (1.4)
```

The final square refresh has exact probability
`1/[6(m-2)D_N]>=p_H`.  For fixed `(j,t)`, the prefix action is a bijection, so
a directed boundary edge recovers at most one assigned source.  There are at
most `LD` pairs `(j,t)`.  A final refresh endpoint has at most one preimage
for each `j`, hence at most `L<=LD`.  Charging all `|S|` sources proves (1.3).
This is the desired M60-style recovery accounting: the edge, fixed-word
index, and prefix time recover the source.

## 2. Why direct two-deletion would have supplied the cover

For positions `i<j`, let `beta_(i,j)` right-bubble factor `i` across the
intervening factors until it is next to factor `j`.  This is a fixed Hurwitz
word of length `j-i-1`.

Write the relevant component subword around those positions as

```text
P x U y S.
```

Deleting `x,y` preserves its identity product exactly when

```text
U y U^(-1)=x.                                        (2.1)
```

After the right bubble, `x` has become `U^(-1)xU=y`, so the endpoint has the
adjacent square `y,y`.  If the deletion core is connected, it is a member of
`G_Gamma`.  Thus the proposition

```text
every genus-positive component word has a connected
identity-preserving direct two-deletion pair              (2.2)
```

would give (1.2) with `L=binom(m,2)` and `D<=m`, hence a completely explicit
polynomial partial-macro conductance bound.

The literal proposition (2.2) is false.  At `N=5,m=8`, with the lexicographic
edge indexing used by the exact harness, the word

```text
[0,1,2,1,0,1,2,1]
= (01)(02)(03)(02)(01)(02)(03)(02)                  (2.3)
```

is an identity word with one connected genus-one component on
`{0,1,2,3}` and isolated label `4`.  Of its 28 position pairs, exactly
`(0,4)` and `(2,6)` preserve the identity after deletion, and both deletion
cores are disconnected.  Every other pair leaves a nonidentity product.
The exact product and connectivity table is stored in
`exact-n5-two-deletion.json`.  Exhaustively, 240 of the 762,940 exterior
states at this size fail (2.2).  This finite calculation rigorously refutes
the universal direct-deletion template; it is not asymptotic evidence.

## 3. An infinite obstruction to bounded local square exposure

For `q>=7`, put `N=2q` and let

```text
e_i=(2i-2,2i-1),             1<=i<=q,
R_a=e_1 e_2 ... e_a,
w_q=R_q R_q R_(q-1) R_(q-1).                         (3.1)
```

The `e_i` are pairwise disjoint.  Each `e_i`, `i<q`, occurs four times and
`e_q` occurs twice, so

```text
product(w_q)=id,
length(w_q)=4q-2=2N-2.                               (3.2)
```

Its support has `q` two-vertex components.  The first `q-1` have genus one,
the last has genus zero, and `sum g_i=q-1=c-1`, as required.

Successive copies of a fixed factor are separated by `q` or `q-1` positions,
at least six.  Therefore every window of length `r<=5` contains `r` distinct
pairwise disjoint transpositions.  Its product has reflection length `r`.
Every length-`r` transposition factorization of that product is reduced, and
each of its `r` disjoint two-cycles must be its own support component; hence
the conditional fiber consists only of the `r!` permutations of those same
factors.

An update can move one factor by at most four positions.  Since equal factors
start at distance at least six, every first-step window is reduced and its
heat bath only permutes its distinct factors.  Hence no one-step target has
an adjacent square, and in particular no target is in the marked deletion
set.  More generally, until two equal factors first lie together in a window,
all updates merely permute reduced windows and the minimum equal-factor
separation decreases by at most four per step.  Once two equal factors do
share a window, that update or the next can be the first nonreduced update;
this only weakens the elementary distance bound to

```text
dist_K(w_q,{words with an adjacent square})
 >= ceil((q-2)/4).                                   (3.3)
```

This proves that neither one-step domination nor a universal bounded-radius
deletion-cell cover can repair (2.2).  The lower bound is only linear, so it
is not a slow-mixing or Terminal-B theorem.

## 4. The four-null strand variant also fails literally

A tempting repair is: either a genus-one word already has a deletable
adjacent surplus square, or deleting one label yields exactly four null
prefix-erasure increments and a connected minimal base.  Four nulls could be
canonicalized as two insertion-coordinate excursions with a polynomial
`binom(m,4)(N-1)^4` overcount, extending M60.

Exact enumeration of all 657,610 distinct genus-one component words occurring
through ambient `N=5,m=8` finds 37,200 counterexamples to this disjunction.
The first is

```text
(01)(12)(01)(12)(01)(12)(13)(13).                   (4.1)
```

Its only displayed adjacent square is the bridge pair `(13)^2`; deleting it
disconnects label `3`.  No label has four null increments with a connected
minimal projection.  The complete prefix-erasure calculation is in
`exact-n5-four-null.json`.  Many such examples have a two-null deletable leaf
whose removal leaves a smaller genus-one word, so a *recursive* strand route
may still exist.  The failure is specifically of the one-level cell
partition.

## 5. Exact terminal-collision obstruction to recursive coalescence

Even a recursive scheme cannot send **all** exterior states to minimal words
while retaining only polynomially many terminal marks per minimal word.
The accepted exact count and character lower bound give, for `N>=6`,

```text
|F_N|/|Omega(N,2N-2)| <= U_6 theta^(N-6),
U_6=114688/234375<1/2,
theta=16 exp(-23/8)<1.                               (5.1)
```

Consequently

```text
|F_N^c|/|F_N| >= U_6^(-1)theta^(-(N-6))-1
              >2 theta^(-(N-6))-1.                  (5.2)
```

Let a deterministic coalescence construction terminate in
`F_N x H_N`, where `H_N` is any auxiliary history alphabet of polynomial
size.  Pigeonhole gives one terminal marked state with at least

```text
[2 theta^(-(N-6))-1]/|H_N|                           (5.3)
```

exterior preimages, which is superpolynomial.  The same obstruction applies
more strongly to targets in `F_N minus A`.

Thus a proof cannot globally erase all component-merge history into only
polynomial terminal metadata and then claim M60-style source recovery.
Successful marked merges are locally recoverable—the refreshed bridge square
and its position recover the immediately preceding split up to polynomial
edge data—but iterating them to the exponentially smaller minimal macro must
either retain exponentially rich randomized histories, stop and charge a
first exterior boundary before terminal coalescence, or exploit a genuine
one-radius expansion inequality.  This is a counting obstruction to the
named routing template, not a conductance upper bound for `K`.

## 6. Surviving proposition

The smallest route-specific open statement is:

> **SHORT BIJECTIVE MARKED-COVER / COAREA.**  For every exterior macro portion
> created by an M64 ball, either give a polynomial family of polynomial-length
> fixed Hurwitz/local-heat-bath words whose bijective prefixes cover it by
> marked surplus-square states with polynomial first-crossing load, or prove
> a one-radius coarea inequality charging a polynomial fraction of its mass
> directly to `L_(k+1)`.  Across component mergers, the charge must stop at
> the first exterior boundary; it cannot coalesce all exterior mass into
> `F_N` with only polynomial terminal metadata because of (5.2)--(5.3).

This proposition is sufficient to address the exact partial-macrofiber gap
left in the main checkpoint.  It remains open.
