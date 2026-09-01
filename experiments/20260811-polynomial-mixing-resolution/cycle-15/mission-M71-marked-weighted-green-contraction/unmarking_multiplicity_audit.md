# Audit of current-mark aggregation on actual edges

Date: 2026-08-12.  Scope: the full nonlazy minimal-long-cycle parking
projection `Pbar_r`, not the identity chain `K`.

## 1. What the current context remembers

M56's constrained-shuffle locality says that after an active branch is
embedded in a fixed outside tree, the normalized suffix-cut statistic on
that branch depends on the outside word only through its attachment-chain
context.  M65 makes this explicit: after the deleted factors are summed,
the statistic is `Phi_(K,R;B)`.  Here `K` is the number of retained outside
attachments, `R` is the number before the active attachment, and `B` is the
fixed suffix size.  The pointwise deep inheritance is

```text
Phi_(K,R;B)=sum_(j=1)^k nu_(K,R,k)(j)
              Phi_(K+k,R+j;B).                    (1.1)
```

Thus, within this exact disintegration, no earlier sequence of `j` values
survives after two histories reach the same current `(K,R,B)` on the same
standardized active macro.  The current contextual observable is identical,
and those amplitudes may be added before its lower-rank routing is chosen.

This statement is limited to the marked suffix-cut class proved in M56/M65.
It would be false for an arbitrary positional statistic not covered by the
deletion/insertion theorem.

## 2. Ambient feasibility bounds the mark set

Let the ambient tree have rank `r`, and suppose an active branch initially
has local rank `s_0`.  Its outside attachment count satisfies

```text
K_0+s_0<=r.                                         (2.1)
```

At a deep step, let the current root composition have `k` parts and last
part `t`; the next local rank is `s'=t-1`, while `K'=K+k`.  The other
`k-1` positive parts have total size `s-t`, so

```text
s-s'=s-t+1>=k.                                     (2.2)
```

Induction using (2.1)--(2.2) gives

```text
K+s<=K_0+s_0<=r                                    (2.3)
```

through every pure-deep segment.  A quotient reset has
`K=k-1<=s-1` directly.  Hence every current mark satisfies

```text
1<=s<=r, 1<=K<=r, 0<=R<K, 1<=B<=s.                (2.4)
```

There are fewer than `r^4` numerical tuples `(s,K,R,B)`.

## 3. Embeddings consistent with one actual edge

A parking macro determines its preorder plane tree.  An active recursive
subproblem is a rooted descendant subtree obtained by repeatedly entering
the last root branch.  If an actual macro edge is used by the internal route
of such a subproblem, its active root must be an ancestor of an endpoint of
the rotated tree edge.  A rooted tree of rank `r` has at most `r+1` such
ancestors.  For a fixed active root, the descendant subtree and its
standardization are unique.

Therefore a fixed actual edge is consistent with at most

```text
(r+1) r^4                                           (3.1)
```

pairs `(active embedding,current mark)`.  If one additionally retains the
orientation of the actual edge, the initial one-split refinement, and the
last canonical quotient-reset edge as source-recovery metadata, each has at
most a polynomial number of choices; the conservative bound remains
`O(r^9)`.  There cannot be exponentially many distinct *current* embeddings
or marks on one actual edge.  Exponentially many historical sequences may
coalesce to one of these labels, but (1.1) says they define the same current
observable and should be aggregated before routing.

## 4. One-shot Cauchy lemma

The following deterministic lemma is immediate.  Suppose, for every label
`lambda`, a flow `F_lambda` is already a valid actual-edge flow, and every
actual edge occurs under at most `M_r` labels.  Then

```text
sum_e [sum_lambda F_lambda(e)]^2/Q(e)
 <=M_r sum_lambda sum_e F_lambda(e)^2/Q(e).          (4.1)
```

Indeed, apply Cauchy--Schwarz once to the labels using a fixed edge, then
sum over edges.  With the conservative count above, `M_r=O(r^9)` is
polynomial.  This loss is incurred once globally, not once per recursive
depth.

## 5. The remaining qualification

Equations (1.1)--(4.1) prove a polynomial **multiplicity** statement, but
they do not by themselves construct the labelled actual-edge flows assumed
in (4.1).  The canonical quotient current is aggregated exactly at the
root-composition level.  After its fine disintegration, however, the coarse
endpoint has the nonconstant contextual density

```text
Pbar_s(y,F_refined)/R_s(coarse,refined).
```

Those right-heavy residuals must still have finite total marked occupation.
If CANONICAL RIGHT-HEAVY RESET OCCUPATION from
`canonical_weighted_reduction.md` is proved in a way that routes each
aggregated `(embedding,K,R,B)` demand on actual internal edges, then (4.1)
does close the unmarking step with one polynomial factor.  Without that
occupation theorem, summing historical amplitudes before routing is a
definition of the desired construction, not yet an energy estimate.

Thus the answer to the multiplicity audit is positive and scoped:

- M65 leaves no extra historical positional datum beyond current
  `(K,R,B)` for its contextual class;
- a fixed actual edge has only polynomially many distinct current
  embedding/mark/source labels;
- this removes exponential *label multiplicity* as an independent
  obstruction;
- the separated polynomial reset-occupation estimate remains the single
  missing analytic input before (4.1) can be invoked.
