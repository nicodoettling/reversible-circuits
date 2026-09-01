# M58 plan: macro-closed profile rectangles and arbitrary join-tree families

## Assigned target

For `(pq)(x)=p(q(x))`, `N>=4`, `m=2N-2`, and the literal lazy exact
`{3,4,5}` chain, prove a uniform inverse-polynomial two-sided conductance
bound for both placements of `F_N^c` beside every nontrivial rectangle

```text
{w in F_N:q_1<=ell(T_J(w))<q_2,
            r_1<=b(T_J(w))<r_2},
```

starting with a fixed `(ell,b)` cell, or produce a literal Terminal-B family
with exact global mass and complete `H3,H4,H5` flow.

## Stronger proposed theorem

The rectangle-specific compatibility issue disappears if strand deletion
records the deleted leaf's neighbor.  Let `A_N` be any relabeling-invariant
family of labeled trees on `[N]`, with no regularity or relation across `N`,
and put

```text
R_A={w in F_N:T_J(w) in A_N}.
```

For fixed new label `N`, define the valid attachment-pair set

```text
P_A={(z,u):z in F_(N-1), u in [N-1],
             T_J(z)+{N,u} in A_N}.
```

The target is the stronger claim that both

```text
F_N^c union R_A,
F_N^c union (F_N minus R_A)
```

have `Phi_pm>=1/(24N^7)` whenever nontrivial.

## Counting route

1. Choose one join-tree leaf `v` in each target word.  Strand-delete it and
   record its old join-tree neighbor `u`, the two null positions, and the
   deleted label.
2. For fixed deleted label, base word, attachment neighbor, and null
   positions, M49's lift multiplicity remains at most `(N-1)^2`.
   Relabeling invariance makes the number of valid `(base,u)` pairs equal to
   `|P_A|` for every deleted label.  Hence

   ```text
   |R_A|<=N binom(m,2)(N-1)^2 |P_A|.
   ```
3. Conversely, for every pair in `P_A`, insert `(N,u)^2` into each of the
   `m-1` gaps.  The source recovers pair and gap and has the requested join
   tree, so there are exactly `(m-1)|P_A|` distributed sources.
4. Refresh the square with the exact padded `H3` outcome into `F_N^c`.
   Apply the same argument independently to `A_N^c`, orient by literal global
   profile-side mass, and retain all other block flow as nonnegative.

## Critical audit questions

- Does recording `u` interact with the `(N-1)^2` insertion-coordinate lift
  bound?  Conditioning further can only reduce a fiber, but the neighbor must
  be recoverable from every original join tree.
- Are valid pair counts identical for all deleted labels?  This uses only
  relabeling invariance of `A_N`, not shape-uniformity of the word law.
- Does square insertion at an arbitrary gap always add exactly the join-tree
  leaf `{N,u}`?  The first new transposition joins fixed `N`; the second cuts
  it back, and later base factors avoid `N`.
- Can two valid pairs or gaps create the same source?  The only appearances
  of `N` are the marked adjacent square, which recovers all data.

## Computation policy and limitation

Finite enumeration is unnecessary for the universal counting identity, but
an exact `N=4,5` audit may falsify pair counts, lift recovery, or source
injectivity.  It cannot prove the theorem.  Even the stronger theorem says
nothing about cuts inside one fixed join-tree fiber, surplus words outside
`F_N`, or the global spectral gap.

## Strengthening after multiplicity audit

Relabeling invariance is not needed. For each possible deleted label `v`, let `P_A^(v)` be the valid `(base,u)` pairs on `[N] minus {v}`. Deletion gives

```text
|R_A|<=binom(m,2)(N-1)^2 sum_v |P_A^(v)|.
```

Generate sources from every `v`. A literal source has at most one representation for each `v`, because its two `v`-incident factors identify the marked square, gap, attachment, and base. Thus source multiplicity is at most `N`, and the number of distinct sources is at least

```text
(m-1)sum_v |P_A^(v)|/N.
```

The same ratio follows for an entirely arbitrary subset of labeled trees. The final theorem will therefore cover every join-tree-measurable subset of `F_N`, not only invariant rectangles.
