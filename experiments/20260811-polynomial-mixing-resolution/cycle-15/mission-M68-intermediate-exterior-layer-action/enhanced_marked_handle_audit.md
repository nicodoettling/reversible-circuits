# M68 audit: enhanced marked-Hurwitz handles

## 1. What the colors-only lift does prove

Fix a connected positive-genus identity-factorization component of length
`k`.  Start from every paired representative with one adjacent surplus square
marked, and transport the two marks as branch-point colors under the right
Hurwitz generators and their inverses.  Let `H_col` be the resulting finite
colored orbit.

The forgetful projection `H_col -> Gamma` is surjective: every uncolored word
in the macro is Hurwitz-equivalent to a paired representative, so transport
one marked surplus pair along an inverse equivalence path.  A word has at
most `binom(k,2)` unordered colored lifts.  Hence uniform measure on `H_col`
projects to the uniform word law tilted by a density between `1` and
`binom(k,2)`.  This part really has only polynomial Radon--Nikodym distortion.

Under a uniformly scanned adjacent Hurwitz generator, the two color positions
evolve exactly as two cards in the adjacent-transposition/interchange chain:
the generator swaps the branch-point colors irrespective of the current
factors.  Thus the position marginal has the usual polynomial time scale
(discrete scan gap of order `k^-3`).

These facts do **not** yield a deletion-cell endpoint, because cancelability
is not a property of two branch-point positions alone.

## 2. Exact two-generator refutation

Use `S_3` edges

```text
0=(01), 1=(02), 2=(12),
```

and start at the connected genus-one identity word

```text
(1_M,1_M,0,0,2,2),                                  (2.1)
```

where the two copies of `(02)` are marked.  Deleting them leaves
`(01)^2(12)^2`, a connected minimal identity word on all three labels.

Apply the inverse project Hurwitz generator at zero-based pair `1`, followed
by the right generator at pair `0`.  With

```text
R(a,b)=(b,bab),       R^-1(a,b)=(aba,a),             (2.2)
```

and transporting the colors with their branch points, the exact result is

```text
(2,0_M,1_M,0,2,2).                                  (2.3)
```

The two marks are adjacent, but their factors are `(01)` and `(02)`, not an
equal square.  Deleting them leaves product `(12)(01)`, the nonidentity
3-cycle recorded as `[2,0,1]` in the permutation convention.

The deterministic BFS artifact `colored-handle-audit.json` discovers this
after two generators and independently verifies the full word product is
still identity.  Therefore:

> **REFUTED:** transporting only two marked positions/branch-point colors
> preserves the property that adjacency certifies an equal deletable handle.

This also explains the N=5 direct two-deletion failures: the valid canceling
pair may carry nontrivial connecting-arc/framing data that is invisible in
its two positions.

## 3. Why retaining the full arc loses polynomial multiplicity

One can preserve cancelability topologically by marking not only the two
branch points but an isotopy class of connecting arc.  Under the same braid
action the arc is transported, and a standard unwound adjacent arc indeed
certifies an equal pair.  However, the forgetful fibers of this full lift are
infinite already for a fixed word.

For example, in `S_4` take

```text
a=(01), b=(23), c=(12),
w=a_M a_M b b c c a a.                              (3.1)
```

This is a connected genus-one identity word; deleting the marked `a^2`
leaves the connected minimal word `b^2 c^2 a^2`.  The second marked branch
point and the following unmarked `b` have disjoint, hence commuting,
transpositions.  The pure braid `sigma_2^2` around those two branch points
fixes the entire factor tuple and returns every color to its original
position: for commuting factors, one Hurwitz move swaps them and the second
swaps them back.  Topologically, `sigma_2^2` is a Dehn twist around the two
punctures.  Its powers give pairwise distinct isotopy classes of the marked
connecting arc (their twisting/intersection number about that two-puncture
curve differs), all above the same word and colored positions.

Thus the literal full-arc lift has infinite, not polynomial, forgetful
multiplicity.  A stationary uniform lift and a polynomial RN comparison do
not exist on that unreduced state space.

This does not rule out a carefully chosen finite quotient of arc/framing
data.  It proves that such a quotient is an additional theorem, not supplied
by the two-card interchange marginal.

## 4. Exact surviving proposition

The enhanced-handle route now stops at:

> **FINITE HANDLE-FRAMING QUOTIENT.**  Construct a finite marked lift of every
> positive-genus connected factorization fiber with all four properties:
>
> 1. its projection to unmarked words is surjective and has multiplicity
>    `k^O(1)`;
> 2. every adjacent Hurwitz generator acts locally and bijectively on the
>    lift;
> 3. a polynomially hittable marked subset certifies an actual adjacent equal
>    square whose deletion leaves the component connected; and
> 4. the hitting/flow congestion, after projection to literal H3 edges, is
>    polynomial.

The colors-only lift satisfies (1)--(2) but fails (3) by (2.3).  The full arc
lift satisfies the topological form of (2)--(3) but fails finite polynomial
multiplicity by Section 3.  No conclusion about the conductance of `K` follows
from this route obstruction alone.
