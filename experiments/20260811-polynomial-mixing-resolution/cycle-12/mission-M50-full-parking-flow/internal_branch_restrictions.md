# Exact rejected-exit restrictions under root composition

Date: 2026-08-11.  The convention and the chain `Pbar_r` are those in
`root_composition_projection.md`.

## 1. Product restriction theorem

Fix an ordered root composition

```text
a=(a_1,...,a_k),  sum_i a_i=r,
```

and put `s_i=a_i-1`.  Let `F_a` be the degree trees with this root
composition, and let `R_a` be the rejected-exit restriction of `Pbar_r` to
`F_a`.  Delete the root edge of branch `i` and standardize its consecutive
preorder interval.  This identifies

```text
F_a = product_(i=1)^k J_(s_i),                       (1.1)
pi_r(.|F_a)=product_(i=1)^k pi_(s_i).                (1.2)
```

Here `J_0,J_1` use their singleton conventions.  For `s_i>=2`, let
`Pbar_(s_i)^(i)` update coordinate `i` and leave every other coordinate
fixed.  Then the restriction has the exact Dirichlet form

```text
E_(R_a)
 =sum_(i:s_i>=2) [s_i(s_i-1)/(r(r-1))]
      E_(Pbar_(s_i)^(i)).                            (1.3)
```

Consequently, if at least one factor is nontrivial,

```text
gap(R_a)
 =min_(i:s_i>=2)
   [s_i(s_i-1)/(r(r-1))] gap(Pbar_(s_i)).            (1.4)
```

If every factor is a singleton, `F_a` is a singleton and its gap is one.

## 2. Proof

The weight factorization is immediate.  A tree in `F_a` has root weight
`1/k!`, while the branch-subtree weights are independent products.  The
normalizing sum for branch `i` is `Z_(s_i)`.  Cancelling these factors in
the conditional law proves (1.1)--(1.2).

For the kernel statement, fix one branch interval `I` with `s` internal
edges.  In every noncrossing factor chord tree, the edges wholly inside
`I` form a noncrossing spanning tree of that interval.  Retaining their
relative factor order and standardizing the consecutive vertex names gives
a minimal factorization of the local long cycle.  This follows directly
from the convention-checked Goulden--Yong characterization: deleting the
outside chords preserves all clockwise-decreasing incident-edge
inequalities, and those inequalities are sufficient.  The local lower
sequence is the subsequence of the global parking word whose values lie in
`I`, shifted by the left endpoint of `I`.

Conditional on a global degree macro, Stanley--Biane makes the global
parking word uniform over all permutations of its multiset.  Hence the
induced local subsequence is uniform over all permutations of the local
parking multiset and has exactly the local `pi_s` law after projection.
Choose the global scan site uniformly from its `r-1` possibilities.  For a
fixed one of the `s-1` gaps between consecutive entries of the local
subsequence, the uniform interleaving of its `s` entries with the `r-s`
outside entries has no outside entry in that gap with probability `s/r`.
If the gap is empty, its two local entries occupy one global scan site, which
is then selected with probability `1/(r-1)`.  Hence every fixed local scan
site is selected with probability

```text
s/[r(r-1)],
```

and the total probability of selecting two consecutive local entries is

```text
(s-1)s/[r(r-1)]=(s)_2/(r)_2.                         (2.1)
```

Conditional on that event, the local scan site is uniform among its `s-1`
possibilities.  (This uniformity is generally false if one first fixes the
global scan position; the averaging over the actual uniform scan is
essential.)  The selected two-factor product is supported inside `I`, and
every transposition decomposition in its exact two- or three-state fibre is
also supported inside `I`.  Thus the conditional update is literally
`Pbar_s`, including its `1/(s-1)` scan and fibre normalization.  Multiplying
by (2.1) proves the off-diagonal part of (1.3); rejected root-changing and
other-branch exits add only holding.

Different branch coordinates are independent under (1.2).  The generator
in (1.3) is therefore a weighted sum of commuting product-coordinate
generators.  Its nonzero eigenvalues are sums of coordinate eigenvalues,
so the smallest is exactly (1.4).  QED

## 3. What this closes and what it does not

The standard rejected-exit restrictions are connected whenever all smaller
`Pbar_s` are connected, and their action-rate loss is exactly quadratic,
not exponential.  A giant branch `s=r-1` is updated at rate `(r-2)/r`, so
there is no hidden `r^-r` slowdown along unary-root fibers.

This still does not close the full gap by a black-box decomposition theorem.
The root-composition map is not a strong lumping in the reverse direction.
For a refined/coarse quotient edge, the crossing target law inside the
coarse fiber is not its stationary conditional law.  The pointwise Radon
bound in `root_composition_projection.md` is polynomial for one level, but
inserting that bound into a worst-case JSTV recursion at each depth would
multiply polynomial losses along a path of depth `Theta(r)`.  That produces
no fixed inverse polynomial.

The smallest surviving proposition is therefore the exact `ROOT-MEAN LIFT`
inequality stated in `balanced_mean_lift.md`.  That note proves that a clean
bound

```text
E_(Rroot_r)(F_f,F_f)<=A r^C E_(Pbar_r)(f,f)
```

closes the full projected gap by a balanced strong induction.  The proof
uses the additive product variance here and the exact action rate (1.3); it
does not multiply a fresh polynomial loss at each depth.

A direct Cayley-basis-exchange comparison is an alternative.  The uniform
Cayley lift removes factorial density ratios, but a single labeled edge
exchange can reorder a linear number of preorder subtrees after child
sorting; it is not a pointwise local `Pbar_r` move and still requires a
randomized flow with recoverable labels.
