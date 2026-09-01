# M181 halfway checkpoint

Date: 2026-08-13 UTC.

## Hash gate and predecessor reconciliation

Every assigned immutable manifest passed before use.  The accepted chain is:

- M135/M137: for fixed `(d,i)`, the incidence multigraph has `H`-orbit edges
  and global `G`-orbit vertices; each color is a perfect matching.
- M141/M143 and M146/M148: every nonempty matching subfamily at `d>=5` has
  aligned factor group `P_(d,s)`, with no extra conjugacy-multiset obstruction.
- M154/M158: aligned inner conjugations in `P_(d,s)` are literal braid loops.
- M163/M164 and M169/M172: physical routing is an affine relative-sign
  problem, and `1 -> P_(d,s) -> K_mon -> V_stab -> 1`.
- M175/M176: `V_stab` is exactly the span of actual Schreier fundamental-cycle
  gains; fixed-endpoint zero routing is exactly tree-offset membership.

No predecessor disagreement was found.

## Proved construction

The M175 rank-four pair certificate was corrected by explicit M154 inner
loops to a 200-move anchored six-factor relation.  On the two local patterns

```text
U=(0a)^2(0b)^2(0c)^2,       V=(0a)^2(0b)^2(ac)^2,
```

the same relation has transporters `(b c)` and `id`, respectively.  The odd
transporter fixes the shared anchor `0`; both transporters fix every label
outside the block.

For `r=floor((d-1)/3)`, concatenate `r` such blocks, all sharing `0`, and add
doubled star-edge filler on the remaining labels.  The resulting words have
product one, connected support on all `d` labels, and length exactly `2d-2`.
The pattern words indexed by `0,e_1,...,e_(s-1)` are pairwise globally
nonconjugate.  A shifted block relation gives voltage representative `e_k`
on the corresponding coordinate and zero elsewhere.  Their classes are a
basis of `W_s`, so M175 gives chord rank `s-1`.

## Matching audit and remaining boundary

A perfect matching contains one edge `Q_c` over the left global orbit of
each constructed word.  For a chosen physical representative
`u_c=alpha_c.W_c` of that `H`-orbit edge, `alpha_c` need not lie in `H`.
The same braid relation satisfies

```text
h_k u_c=(alpha_c delta_(c,k) alpha_c^(-1)).u_c,
```

so its sign response is unchanged.  This makes the subfamily genuinely an
M135 matching subfamily without claiming that the matching contains the
literal canonical word.

Full voltage makes every fixed-endpoint tree offset a member of the column
space once a source-to-target quotient route exists.  Establishing that
route, and proving full rank for arbitrary matching subfamilies, remain the
first open obligations.  No polynomial-length, gap, or Terminal claim is in
scope.
