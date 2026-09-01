# Contextual branch-local reduction for the spine-bias functional

Date: 2026-08-11.  This note concerns the full nonlazy minimal-sector
parking projection `Pbar_r`.  It is not a statement about the identity
bridge chain `K`.

## 1. Contextual locality theorem

Fix a coarse root composition `b=(c_1,...,c_k)` and a one-split refinement
`a` obtained by replacing `c_i` by `(A,B)`.  A state in the coarse fibre is
an ordered tuple of independent local branch macros

```text
d=(u_1,...,u_k),  u_j in J_(c_j-1).
```

Write `p_(b,a)(d)=Pbar_r(d,F_a)`.

**Theorem 1 (contextual split locality).**  For fixed `(r,b,a,i)`, there is
a function
> `phi_(r,b,a,i)` on `J_(c_i-1)` such that
> ```text
> p_(b,a)(d)=alpha_r phi_(r,b,a,i)(u_i).             (1.1)
> ```

### Proof

Let `I_j` be the preorder interval of root branch `j`.  In the noncrossing
factor tree, all edges of this branch lie in `{0} union I_j`, and there is
exactly one edge from `0` into `I_j`.  Restrict a numbered chord diagram to
those edges, close the factor-number gaps, and standardize `I_j`.  The
Goulden--Yong clockwise inequalities are preserved.  The accepted
sufficiency theorem therefore identifies the restriction as a minimal
factorization on `c_j+1` vertices whose root degree is one and whose
nonroot local macro is `u_j`.

Conversely, take one such root-unary local factorization for each branch.
Their chord diagrams occupy disjoint cyclic intervals and meet only at
`0`.  Shuffle their factor orders while preserving each local order and
requiring the `k` distinguished root-attachment factors to appear in the
reverse of the root-child order.  Local clockwise inequalities remain
valid, and the displayed order is exactly the only new inequality at
`0`.  Goulden--Yong sufficiency gives a unique global factorization with
root composition `b`.  Restriction and union are inverse.  This proves the
root-branch constrained-shuffle bijection.

For a fixed local macro `u_j`, its local root-unary orbit has size

```text
|O^+_(u_j)|=c_j!/product_(v in I_j)d_v!.             (1.2)
```

Its lower-label multiset contains exactly one zero.  Stanley--Biane says
that every permutation of that multiset occurs once, so the distinguished
root-attachment factor occupies each of the `c_j` local word positions in
exactly

```text
|O^+_(u_j)|/c_j                                      (1.3)
```

local words.  In particular this position law is independent of the shape
and degree multiplicities inside the branch.

A transition from `b` to the fixed refinement `a` uses a pair consisting
of branch `i`'s root-attachment factor and one factor in the same local
diagram.  Cutting the resulting last-child suffix subtree is the universal
right-spine support theorem.  Record the local word, the local positions of
the pair, and one favourable rank-two outcome.  A global shuffle realizes
this marked transition precisely when it leaves the two marked local
factors consecutive and puts every distinguished root factor in the
required order.  For fixed local positions, the number of such shuffles
depends only on `(r,b,i)` and those positions, not on any local chord shape.

Now fix the marked local word in branch `i` and sum the extensions over all
local words in every branch `j!=i`.  Equation (1.3) shows that this number
is

```text
[product_(j!=i)|O^+_(u_j)|] times
a combinatorial factor depending only on (r,b,i) and the marked positions.
                                                               (1.4)
```

On the other hand the unrestricted orbit size is

```text
|O_d|=r!/[k! product_v d_v!]
     ={r!/[k! product_j c_j!]}
       product_j |O^+_(u_j)|.                       (1.5)
```

Divide the marked favourable-outcome count by
`3(r-1)|O_d|`, the exact pair-fibre, scan, and source-orbit normalization.
All factors involving `u_j`, `j!=i`, cancel between (1.4) and (1.5).
What remains is a weighted sum over marked local words of branch `i`, with
weights determined by `(r,b,a,i)` and their local positions.  It is a
function only of `u_i`.  Dividing by the fixed `alpha_r` defines `phi` and
proves (1.1).  The argument counts ordered favourable outcomes, so it does
not lose a factor when a pair has two macro-identical outcomes.  QED

The exact audit independently finds no fixed `(b,a,i,u_i)` collision through
`r=7` and no contextual-versus-unary support mismatch.

A stronger scalar reduction to the unary-root split function is false.
Even for fixed `(b,a,i)`, the ratio between the contextual normalized rate
and the unary normalized rate varies with `u_i`; the exact `r=7` report has
many such failures.  Across all positive tested entries the ratio ranges
from `1/5` to `2`, but this finite range is not a universal bound.

## 2. Exact H-minus consequence

Put

```text
s=c_i-1,
gamma_i=s(s-1)/[r(r-1)],
bar phi=E_(pi_s) phi.
```

The M50 product restriction gives

```text
pi(.|b)=tensor_j pi_(c_j-1),
E_b=sum_j gamma_j E_(Pbar_(c_j-1)).                 (2.1)
```

The bias functional is

```text
ell_(b,a)(g)=alpha_r E[(phi(u_i)-bar phi)g].         (2.2)
```

Conditional expectation over every coordinate other than `i` preserves
(2.2) and cannot increase (2.1).  Conversely a local test function attains
the local dual supremum.  Hence

```text
||ell_(b,a)||_(-1,b)^2
 =alpha_r^2/gamma_i
   ||phi-bar phi||_(-1,Pbar_s)^2.                   (2.3)
```

Since `q_(b,a)=alpha_r bar phi` and

```text
alpha_r/gamma_i=2/[3s(s-1)]=alpha_s,                (2.4)
```

division gives

```text
||ell_(b,a)||_(-1,b)^2/q_(b,a)
 =alpha_s ||phi-bar phi||_(-1,Pbar_s)^2/bar phi.    (2.5)
```

Equivalently, if `p^ctx_s=alpha_s phi`, the right side is exactly

```text
||p^ctx_s-E p^ctx_s||_(-1,Pbar_s)^2/E p^ctx_s.      (2.6)
```

Thus the global normalization cancels completely: no factor depending on
`r` is lost in passing to the split branch.  This is the effective-resistance
form in which a recursive proof could be additive rather than multiplying a
Radon--Nikodym loss at every depth.

For `s<=1` the local fibre is a singleton and both sides vanish, so (2.3)
has the natural zero convention rather than a division by `s(s-1)`.

## 3. Why this does not yet prove the target

The contextual local observable `phi` is not a scalar multiple of the
ordinary unary split observable, and no universal shuffle formula has been
proved which converts its position-weighted marked sum to an already bounded
coboundary.  Consequently (2.6) is a full-chain dual norm of a contextual
rate function, not one of the already bounded quotient modes.  Bounding it
by the unknown full spectral gap is circular and loses the powers needed by
the balanced induction.

The smallest surviving constructive proposition is therefore:

> **CONTEXTUAL SPINE COBOUNDARY.**  Construct, for every position-weighted
> contextual rate `p^ctx_s` produced by Theorem 1, an internal `Pbar_s`
> flow routing
> `pi_s(p^ctx_s-Ep^ctx_s)` with energy at most
> `s^C E p^ctx_s`; the sums over all contextual splits must obey the same
> polynomial bound.

Together with (2.3)--(2.6), this proposition proves M54's SPINE-BIAS
H-minus-one BOUND.  The exact audit can refute locality or a proposed
uniform ratio, but its passes cannot prove this proposition.

## 4. Recursive suffix filtration

The constrained-shuffle proof above has a second consequence which is
useful for attacking the remaining coboundary.  It is important here to
retain the positional weights: the false scalar reduction to the ordinary
unary split is not being reinstated.

Fix one contextual function `phi` from Theorem 1, and write `B` for the
size of the suffix subtree which is cut from the augmented unary branch.
For `u in J_s`, let

```text
C(u)=(c_1,...,c_k)
```

be the root composition of its inner tree.  If `c_k>B`, let `v_k` be the
standardized macro of its last root branch.

**Theorem 2 (recursive contextual locality).**  Conditional on a fixed
inner root composition `C`, the following hold universally.

1. If `c_k<B`, then `phi(u)=0`.
2. If `c_k=B`, then `phi(u)` is constant as `u` ranges over the whole
   root-composition fibre `F_C`.
3. If `c_k>B`, then `phi(u)` is a function only of `v_k`.  That function
   is again a position-weighted contextual suffix-cut statistic, now on
   the augmented last branch and with the same suffix size `B`.

### Proof

Expose the unique external root-attachment factor of the augmented unary
branch as a distinguished singleton.  Conditional on `C`, split every
remaining factor into the `k` root-branch subsequences.  The same
Goulden--Yong argument as in Theorem 1 identifies the augmented word with
a constrained shuffle of this singleton and the `k` local words: local
orders are preserved and the `k` root-attachment factors occur in reverse
child order.

The right-spine support theorem says that the rightmost spine enters the
last root branch and never visits an earlier one.  A suffix subtree of size
`B` therefore cannot exist when `c_k<B`, proving part 1.

When `c_k=B`, the cut factor is exactly the distinguished attachment factor
of the last root branch.  For fixed local positions of the external
singleton and all distinguished root factors, the number of constrained
shuffles depends only on the part sizes and those positions.  In each local
orbit the distinguished attachment position is uniform, by the unique-zero
argument (1.3).  Summing over positions and over the local words contributes

```text
product_j |O^+_(v_j)|
```

times a factor depending only on the fixed composition and the inherited
positional weights.  Division by the augmented orbit size cancels every
`|O^+_(v_j)|`; hence the normalized statistic is constant throughout
`F_C`.  This proves part 2.

When `c_k>B`, the marked cut factor lies inside the last branch.  Hold its
local word and marked positions fixed, then sum all words and attachment
positions in the other `k-1` branches.  Exactly as in (1.3)--(1.5), those
orbit factors cancel after normalization.  What remains is a weighted sum
over the last-branch word in which the weights depend only on the fixed
outer context, `C`, and the marked local positions.  This is precisely a
new position-weighted contextual statistic on `v_k`; no other branch macro
remains.  This proves part 3.  QED

Thus recursion follows one strictly smaller last branch; it does not branch
over every child.  Its terminal term is a function of root composition
alone.  The exact falsifier
`recursive_contextual_locality.py` finds no failure of any of the three
claims through `r=7` (272 top groups and 679 deep groups at `r=7`).  These
finite counts are calibration only; the theorem is the constrained-shuffle
argument above.

Theorem 2 narrows the open step but does not by itself bound energy.  A
quotient flow for the terminal composition function, when disintegrated
over actual fine edges, creates target-bias charges of exactly the same
contextual class.  Bounding each disintegration by a fixed factor and then
multiplying down a depth-`Theta(s)` spine would still be exponential.
The sharp remaining form is:

> **ADDITIVE CONTEXTUAL SPINE COBBOUNDARY.**  Lift the root-composition
> flow for the terminal terms in Theorem 2 so that every fine target-bias
> charge is routed recursively down its unique active last branch, with
> total (not per-level) energy at most `s^C E p^ctx_s`.  Equivalently,
> prove CONTEXTUAL SPINE COBBOUNDARY with an additive occupation bound for
> the one-active-branch recursion.

This is strictly smaller than arbitrary ROOT-MEAN LIFT: universal support,
contextual locality, exact normalization cancellation, one-active-branch
closure, and top-fibre constancy are now proved.  What remains is the
additive effective-resistance estimate.
