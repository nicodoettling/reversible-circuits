# Mission M238 report: fresh referee of M235 TCM

Date: 2026-08-13 UTC.

## Verdict

**ACCEPT M235 AS FROZEN.**

M235 proves, for every odd `k>=3` and integer
`2<=ell<=(3k-1)/2`,

```text
|sum_(y=2)^ell c^T_(k,y)|<=160sqrt(ell)/k.
```

This closes exactly TCM.  It does not prove YCM, WBE, DE, conditional J2,
any downstream response, a gap, mixing, or a Terminal.

## Independent mathematical audit

The frozen M235 inventory and every cited accepted dependency inventory pass.
The B raw law has exactly `D=2k-1` first chords per split, not `2D`; its two
post-first parent branches and `t-1` second-edge placements enumerate every
ordered disjoint pair once.  The complementary two-run face is the retained
union of `t` source edges, so its exact size is

```text
t+k 1{large seam retained}+1{small seam retained}.
```

This includes simultaneous seam hits.  Cyclic averaging puts the large seam
in the retained union exactly `t` times and proves M235's placement bound.

On the A side, the marked law has seam-free mass `(k-t)/k`; the seam-hit atom
is above every allowed cutoff.  In the untouched law, the `x=s` first face
cannot qualify, while `x=k-s`, `y=k-c` gives exact size `k+s+c` and raw mass
`cK_R(k,c)`.  This rederives M235 (5.3) with its exact range.

Every analytic constant survives audit.  The B bounds are `24+4+4+52=84`.
The only use of `D-t=s+d` is the long-parent high-t branch `r=D-s`; its
`42/sqrt(k)` estimate converts to constant 52 because nonemptiness forces
`ell>(3k-1)/4>=2k/3`.  The A bounds are `12+12+17+20=61`; the long marked
convolution has `u=k-t>=2` and the untouched dependent range is extended
only after nonnegativity is established.  The case `k=3` is included.

Thus positivity gives constant `145`, hence the stated constant `160`.

## Clean-room check

`cleanroom_tcm_referee.py` is standard-library only and imports no M235 code
or data.  Literal permutation coefficients match independent B and A formulas
at `k=3,5,7`.  All 1,458 B tuple/cutoff placement inequalities pass.  The
rooted-tree convolutions pass through size 31, and all component bounds pass
at 360 allowed parameter pairs with odd `k<=31`.  These are finite
falsification checks, not the universal proof.

## Numbered objections

1. **Material objections:** none.
2. **Nonmaterial objections:** none.

Recommended coordinator action: promote TCM as proved and independently
accepted; keep YCM and all downstream claims open.
