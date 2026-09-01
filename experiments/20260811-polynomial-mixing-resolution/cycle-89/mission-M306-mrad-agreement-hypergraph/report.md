# M306 Report: MRAD Weighted Dual and Moment Obstruction

Date: 2026-08-14 UTC

## Verdict

```text
PROVED: exact RCOM conditional-moment identity and RCOM => MRAD.
PROVED: MRAD/WRAD/fractional-cover polynomial equivalence with O(d log d) loss.
REFUTED: RCOM as a polynomially equivalent or generic symmetry-based MRAD route.
UNRESOLVED: actual-M135 MRAD/WRAD for d>=6 and literal braid length.
```

## Strongest new result

For actual fibers, averaging over a uniformly chosen action in one anchor
fiber gives exactly

```text
E[r_U(a) | a in K_P]
 =(1/|K_P|)sum_(Q in U)|K_P intersect K_Q|.
```

This proves the predeclared RCOM condition sufficient for MRAD without a
Helly step.  It also exposes point-stabilizer dilution: in the natural full
symmetric or alternating action on `N` points, the identity matching has a
one-action cover, but every full-family anchored score equals `2`.  With
`N=d^(d-3)(2d-2)!/d!`, this is a superpolynomial separation.  Thus even
maximal monodromy would not justify RCOM by conditional averaging.

The corrected target is weighted residual agreement.  For every
`lambda_Q>=0`, seek

```text
max_a sum_(Q in E_a)lambda_Q >= ||lambda||_1/d^C.    (WRAD)
```

Finite LP duality identifies WRAD exactly with polynomial fractional
action-cover number.  Thresholding sorted weights shows that ordinary MRAD
implies WRAD with only the harmonic loss
`H_|M|=O(d log d)`; indicators give the converse.  This is a genuine
weighted-orbit obstruction/certificate on the actual edge set.

## Rank-three guard

M301/M304's actual triple `[0,2,9]` remains controlling.  Its fibers have
size nine, its three pair intersections are distinct singletons
`45,49,89`, and its triple intersection is empty.  Therefore each anchored
RCOM score is `11/9` while maximum agreement is exactly two.  No pairwise
Helly inference appears anywhere in the proof, and complete-matching MT2H
remains vacuous at `d=3`.

## Exact stop

This mission does not refute actual RCOM or MRAD.  It proves that RCOM is an
extra, potentially superpolynomially stronger property and cannot be derived
from transitivity, uniform point fibers, or even full symmetric/alternating
monodromy.  Actual `d>=6` WRAD is the first valid extremal weighted-action
lemma.

Even WRAD/MRAD would close only finite-action nonemptiness.  Polynomial
literal representatives, SSTID, every-color routing, voltage, congestion,
every gap/mixing theorem, and both Terminals remain open.

