# M37 plan: primitive-excursion zipper at quadratic-over-log radius

## Objective

For `N>=10^6`, `m=4N^3+4`, and the actual graph neighborhoods `V^(a)` of
all disconnected identity words, prove an inverse-polynomial full-kernel
conductance floor through

```text
A_N=floor(N^2/[100 log(N+1)]).
```

This is the prioritized quadratic-over-log scale.  Use the original lazy
exact `r={3,4,5}` kernel and global uniform bridge law.

## New algebraic route

For the isolate cut, a block whose first and last factors cross the cut is
called primitive when none of its proper prefixes after the first crossing
returns to the isolate subgroup.  Track

```text
X_j=(prefix product)^(-1)(z).
```

From every non-isolate state `X_j`, exactly one of the `M` transpositions
sends `X_j` to `z`; hence each middle step has exactly `M-1` safe choices.
Primitive length-`l` blocks therefore number exactly

```text
(N-1)(M-1)^(l-2).
```

This matches the outer forced-last-crossing upper bound
`(N-1)M^(l-2)` up to `(M/(M-1))^(l-2)`.

## Zipper lemma

For any five-transposition product `g`, choose a transposition `tau` such
that `h=tau g` lies in the isolate subgroup and has Cayley transposition
length at most four.  If `g` moves `z`, take
`tau=(z,g(z))`; it splits the cycle of `g` containing those two vertices.  If
`g` fixes `z`, split any nontrivial internal cycle.  Factor `h` into exactly
four internal transpositions.  Thus every five-window can be replaced by

```text
(tau,a_1,a_2,a_3,a_4)
```

with the same product.  Sweeping from right to left makes four new positions
internal per update.  Every subgroup-valued block of length `<=4q+1`, padded
on the right to length `4q+1`, becomes internal in `q` actual `H_5` moves.

## Boundary family

Use total minimal budget exactly `a`, primitive blocks separated by at least
three internal positions, four trailing internal positions, and a long
outside internal sequence robust against deletion of `a` five-windows.
Primitivity forces every subgroup-valued active cluster beginning at the
leftmost uncovered crossing to contain whole consecutive primitive blocks.
One final `H_5` push delays the last return of the rightmost primitive block
by four positions, increasing every possible cluster cover from total budget
`a` to at least `a+1`.

## Entropy comparison

M33's shrunken-cluster outer encoding remains valid.  For block budget `q`,
the four allowed lengths contribute a common geometric factor.  Exact-`a`
primitive sources and cumulative-`<=a` outer configurations have identical
composition/layout coefficients.  The only entropy losses are

```text
[M/(M-1)]^(4a)=exp(O(a/M))=O(1),
```

and the sparse-layout correction at the relevant
`c=O(sqrt(a))`, also `O(1)`.  Large `c` has a geometric coefficient tail.

Non-isolate cuts retain exponential factorial suppression; robust outside
words exist because `a log m<=0.03N^2`, far below the dense-tail exponent.

## Failure modes

- Prove the zipper factor `tau` reduces Cayley length; do not merely show
  coset correction.
- Primitive means no intermediate return to the isolate subgroup, not a
  parity condition.
- Count endpoint-compatible outside words before subtracting nonrobust ones.
- Treat layouts with large cluster count separately so the placement
  correction does not become `exp(O(a^2/m))`.
- Include all non-isolate cuts, exact global orientation, and all
  `Q_3+Q_4+Q_5` flow.
- A fixed-state or auxiliary-chain slowdown is nonresponsive.

## Computation

No finite computation is planned.  The universal claims are exact algebraic
and enumerative identities.
