# M316 formula-level audit of the sole k=13 H2 guard

Date: 2026-08-14 UTC

No new finite run was made.  A no-import reconstruction of the 53,378-state
guard would require independently duplicating M297's permutation and exact
completion engine, so it is not compact; the assignment permits analytic and
formula-level comparison in this case.

The authenticated guard fixes only `K=13`, `DROW=2`.  Line-by-line audit
confirms:

1. exact `p,q` normalize and their interval intersections construct the
   reported 17-cell monotone support, all with `s<=t`;
2. every source/channel split marginal is asserted as
   `alpha_j*base[s]` before marking;
3. `h2_mark` always emits exactly three profiles, using profile zero for
   every non-size-two slot;
4. the two channels are accumulated into each split law before division by
   `scale=3(alpha_1+alpha_2)` and before common-part coupling;
5. the diagonal common part cancels under antisymmetrization, while the
   residual product is oriented once on unordered edges;
6. every cell contribution is multiplied by `scale*pi_(s,t)` and accumulated
   before any edge absolute value;
7. the complete divergence dictionary is asserted equal to the direct
   combined extended profile coefficient before norms are computed;
8. the response norm excludes only profile zero, matching reduced CMPAD.

The authenticated output records exactly the frozen finite facts:

```text
raw ordered pairs A/B                         43,940 / 104,300
physical product states                      53,378
positive quantile cells                      17
nonzero global net profile edges             15,073
k ||J||_edge /(2 b_2)                        3.3053774998628103
k ||mu_nonzero||_TV /(2 b_2)                 2.3951607793712415
```

The maximum edge joins profile zero to the displayed four-impulse H2 profile
and has already-combined contributions only from cells `(1,1),(1,2),(2,2),
(2,3)`.  Exact rational norms, the edge value, cell masses, and contributions
remain in the SHA-gated JSON.  These facts neither prove nor refute an
all-rank absolute constant.
