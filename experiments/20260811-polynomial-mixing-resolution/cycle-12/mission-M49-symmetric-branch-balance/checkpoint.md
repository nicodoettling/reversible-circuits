# M49 halfway checkpoint

## Status

The label-symmetric threshold now has a promising direct full-`K` boundary
certificate.  The new ingredient is a canonical **strand deletion** for any
leaf of the prefix join tree.  It avoids replacing the actual weighted
join-tree law by uniform Cayley measure.

## Deterministic tree facts

For a tree `T` on `N` labels, put

```text
b(T)=max_e min(|C_e|,N-|C_e|),
c(T)=min_x max{|C|:C is a component of T-{x}}.
```

Then `b(T)=c(T)`.  If `x` is a centroid, every component of `T-{x}` has
size at most `N/2`; the edge from `x` into a largest component shows
`b>=c`.  Conversely, for any edge, choose its side not containing a
centroid; that side lies in one centroid branch, so its smaller-side size is
at most `c`, proving `b<=c`.

If `q<N/2` and `b(T)>=q`, some tree leaf `v` has
`b(T-v)>=q`: take an edge with both sides at least `q`, choose a side of size
at least `q+1`, and choose a leaf of its induced subtree other than the
bridge endpoint.  If `N=2q` and `b(T)=q`, deleting any tree leaf leaves an
edge split `q-1` versus `q`, hence `b(T-v)=q-1`.

## Canonical strand deletion

Fix a label `v`.  For `sigma in S_N`, let `d_v(sigma)` be the permutation on
`[N]\\{v}` obtained by erasing `v` from its cycle.  Equivalently,

```text
d_v(sigma)(x)=sigma(x)                 if sigma(x)!=v,
             sigma(v)                 if sigma(x)=v.
```

For a prefix path `sigma_j=t_1...t_j`, define

```text
s_j=d_v(sigma_(j-1))^(-1)d_v(sigma_j).
```

Writing a permutation above its deletion by the insertion coordinate
`a in ([N]\\{v}) union {bottom}` (the predecessor of `v`, or `bottom` when
`v` is fixed) proves directly that every `s_j` is either the identity or a
transposition.  If `v` is a leaf of `T_J(w)`, its unique support-join factor
projects to an identity.  Every other join-tree edge survives unchanged, so
the nonidentity projected factors have connected support on `N-1` labels.
They telescope to the identity and therefore have length at least `2N-4`.
The number of deleted identity steps is positive and even, while the original
length is `2N-2`; it is consequently exactly two.  Deleting those two steps
gives a word of `F_(N-1)`, and its join tree is exactly `T_J(w)-v`.

For a fixed deleted word and fixed locations of the two null steps, there are
at most `(N-1)^2` lifts with `v` a join-tree leaf.  There are `N-1` choices
for the insertion coordinate at the first null step.  At a projected
support-join step the lift is forced: using a `v`-incident alternative would
create a second join-tree edge at `v`.  At a projected cut step a strand can
branch into at most two lifts, but the two descendants lie in distinct
permutation cycles inside the same support component.  Minimality forbids a
later transposition from rejoining such cycles.  Thus descendants of one
initial coordinate occupy distinct cycles at every later time, giving at
most `N-1` descendants.  The full deletion fiber is therefore bounded by

```text
L_N=binom(2N-2,2)(N-1)^2.                         (C.1)
```

This argument is being independently checked by exact orbit enumeration.

## Threshold count reduction and candidate conductance bound

Let

```text
H_N(q)=|{w in F_N:b(T_J(w))>=q}|.
```

The deletion facts give, for `q<N/2`,

```text
H_N(q)<=N L_N H_(N-1)(q).                         (C.2)
```

For even `N=2q`, they instead give

```text
H_N(q)<=N L_N H_(N-1)(q-1),                       (C.3)
```

where `q-1` is the maximum possible balance on `N-1` labels.

For a fixed new label, inserting an adjacent square `(v,u)^2` in any of the
`m-1=2N-3` gaps of a base word gives distinct root-marked sources.  In (C.2)
all `N-1` attachments preserve the threshold.  In (C.3), choose canonically
an edge split `q-1,q` and attach to one of the `q-1` labels on its smaller
side; the new tree has a perfectly balanced edge.

Refreshing the marked square by one padded `H3` outcome exits `F_N`, hence
the cut, with exact probability

```text
p_N=1/[6(m-2)D_N],  D_N=(3N^2+N-12)/2.             (C.4)
```

All `H4,H5` flow remains nonnegative.  Combining (C.1)--(C.4) currently gives

```text
Phi_pm^K(B_(N,q)) >= 1/(24N^6)   when q<N/2,
Phi_pm^K(B_(N,N/2)) >= 1/(96N^6) when N is even.    (C.5)
```

The denominator orientation uses only
`min(pi(B),pi(B^c))<=pi(B)`; it does not assume which side is smaller.

## Remaining audit before freezing

1. Verify the insertion-coordinate transition table and the no-reunion
   strand argument at every join/cut type.
2. Exact-check the two-null-step statement, deletion fibers, tree deletion,
   and both threshold endpoint formulas in `F_4` and `F_5`.
3. Audit nonemptiness, `m=4` whole-word `H4`, and the global rather than
   conditional stationary orientation.
4. Freeze the theorem only if the exact checks and constants agree.

No Terminal-A or Terminal-B conclusion is claimed.  If (C.5) survives, it
rigorously rejects this entire label-symmetric branch-balance threshold family
as a superpolynomial bottleneck.
