# M273 halfway checkpoint

The immutable predecessor gate and DPS source digest verified. Before any
finite replay, the root seam was fixed in cyclic coordinates:

```text
s=m-R_v,
old root slot  = (q_(s-1),q_s)     = (alpha,beta),
new child d    = (q_(s-1),q_s)     = (alpha,beta),
new root slot  = (q_(s+1),q_(s+2)) = (gamma,delta).
```

The new child is an individual canonical macro, not a count or anonymous
side. Its `beta` then `alpha` rows both have distance three against `x_1`.
For an open root lens the old/new root complements give the top rows

```text
alpha -> x_v,       gamma -> x_v,
```

and all lower root-white/lens-black rows have distance one.

The port analysis was corrected before the proof was frozen: a smaller
direct-child port does not necessarily discharge at `x_1`. It discharges at
the first width crossing, whose current parent can be nonroot. The position
shift `t^+=t+2` below `v` makes that individual endpoint rank-stable. Exactly
the larger direct children persist through an open root and reach the final
root.

The four-case guard was predeclared only after these formulas were fixed.

