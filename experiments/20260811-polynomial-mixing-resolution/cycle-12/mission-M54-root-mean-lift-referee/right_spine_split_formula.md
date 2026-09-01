# Universal right-spine split support and rate-formula obstruction

Date: 2026-08-11. Permutations compose as `(pq)(x)=p(q(x))`, and
factor tuples multiply left-to-right. The chain is the full nonlazy
adjacent-rank-two parking projection `Pbar_r`, not the identity bridge
chain `K`.

## Theorem (support and uniqueness)

Fix `r>=2`, a parking degree macro `d`, and one root branch of its preorder
plane tree. A transition which splits that branch into ordered sizes
`(A,B)`, `A,B>=1`, has positive rate if and only if the root of the
`B`-subtree is a last child of a vertex on the branch's rightmost spine.
Equivalently, `B` is the size of a proper suffix subtree encountered on
that spine. When positive, the cut edge and the target degree macro are
unique: if the cut parent is `j`, the target is

```text
d+e_0-e_j.
```

### Proof

Reverse the proposed split. In the refined tree, the two new branches of
sizes `A,B` are adjacent root children. M50 Lemma 2.1 proves that every
upward transition across this child boundary attaches the later branch
`B` at a vertex `j` on the rightmost spine of the earlier branch `A`, and
that every such right-spine attachment is in the support. Because `B` is
attached as the last child of `j`, the rightmost spine of the merged
branch enters the root of `B`; hence `B` is exactly a suffix subtree of
the merged branch. Reversing the surgery detaches this last-child subtree
and places it immediately after the remainder at the root, proving both
directions.

Subtree sizes strictly decrease down a spine. Therefore a prescribed
positive suffix size `B` selects at most one cut edge. The surgery changes
only the outdegrees of `0` and the cut parent `j`, so the target macro is
uniquely `d+e_0-e_j`. QED

This proof uses the already accepted universal child-boundary lemma; the
bounded script is only an independent falsifier. It reports no support or
uniqueness failure through `r=7`.

## Refutation of a local numerical rate formula

The support theorem does not make the individual rate a function only of
`(A,B)`, the cut-parent degree, and its number of children. At `r=4`, put
`alpha_4=2/[3*4*3]=1/18`. The exact projected kernel has

```text
(0,0,1,1) -> (0,0,0,1)  at rate (2/3) alpha_4,
(0,0,2,2) -> (0,0,0,2)  at rate (4/3) alpha_4.
```

In both cases the coarse branch has size `3`, the split is `(2,1)`, and
the cut parent has degree and child count both equal to `2`. Thus every
universal formula depending only on those data is refuted. The missing
information is the marked-factor/interleaving geometry outside that
local tuple.

## Exponentially small individual-rate pattern (finite evidence only)

For every tested `2<=r<=7` and `1<=z<r`, the source

```text
d_(r,z)=(0 repeated z times,z,z+1,...,r-1)
```

has root composition `(1 repeated z-1 times,r-z+1)`. Splitting the final
leaf of the long path gives the exact observed rate

```text
Pbar_r(d_(r,z),d_(r,z)+e_0-e_(r-1))
  =alpha_r/binom(r-1,z).
```

The central values are exponentially small in `r`. The exact marked
parking words observed in small cases suggest a direct Stanley-inverse
bijection, but no universal bijection is proved here. This displayed
family is therefore labelled **empirical exact finite evidence**, not a
theorem. It nevertheless warns that an argument requiring a polynomial
lower bound on every positive split rate is structurally implausible.

## Consequence for the frontier

Right-spine support is now proved and a shape-local rate formula is
refuted. What remains is an aggregate functional inequality for the
right-spine suffix-cut bias functions, stated precisely in `report.md` as
**SPINE-BIAS H-minus-one BOUND**.
