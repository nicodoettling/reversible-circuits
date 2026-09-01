# M313 sole `k=13` H2 guard report

Verdict: **finite survival; inconclusive for all-rank MPCF**.

The exact guard uses only `H_2` and the predeclared quantile/common-part
antisymmetric flux, with the controlling fixed-mass normalization in
`normalization_addendum.md`.  It verifies every split/channel marginal and
the exact equality between flux divergence and the direct combined extended
profile coefficient.

```text
k,n                                      13,39
live raw ordered pairs A/B               43,940 / 104,300
physical product states                  53,378
positive quantile cells                  17
nonzero global net profile edges         15,073
k ||J||_edge /(2 b_2)                    3.3053774998628103
k ||mu_nonzero||_TV /(2 b_2)             2.3951607793712415
```

All quantile cells are summed and reverse edges antisymmetrized before the
edge absolute value.  No channel, source, type, phase, seam, or incidence
norm is computed.  The largest net edge is between profile zero and the
displayed four-impulse H2 profile; it receives already-combined contributions
from cells `(1,1),(1,2),(2,2),(2,3)`.  Its finite value supplies no all-rank
formula or obstruction.

The guard therefore neither proves nor refutes MPCF.  No other rank or row is
authorized or used.

