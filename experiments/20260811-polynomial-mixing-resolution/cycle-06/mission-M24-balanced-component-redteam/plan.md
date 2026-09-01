# Cycle 06 M24 plan: balanced component-separator red team

## Exact target and convention

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  The target is the
uniform law on `Omega(N,m)`, and `K` is the exact lazy `{3,4,5}`
same-product heat bath with every block-size, window, and fiber
normalization retained.

Fix a balanced labeled bipartition `[N]=S disjoint union S^c`, with
`|S|=floor(N/2)`, and define

```text
A_S={w:no transposition factor crosses (S,S^c)}.
```

This is the exact event that every support component refines a nontrivial
balanced separator.  It does not single out or require an isolated label.
Seek a superpolynomial full-`K` bottleneck; failing that, prove an
inverse-polynomial two-sided conductance bound at every even length.

## Main proof lane

1. Compute the exact mass of `A_S` as the identity-return count for the
   internal generator set of `S_|S| x S_|S^c|`, including the color
   interleaving convolution.  Orient by the exact minimum of this count and
   its complement.
2. For the uniform internal-generator bridge, count marked adjacent squares
   by deletion.  Prove even return monotonicity spectrally for this product-
   group walk, giving a square with probability at least the reciprocal of
   the number of internal transpositions.
3. Refresh one square in an actual boundary-safe `H_3` window to every edge
   crossing the balanced separator.  Track exact `D_N`, laziness,
   block/window scans, and the full `Q_3+Q_4+Q_5` flow.
4. Audit why the proof does not automatically pass to the union over all
   balanced separators or the largest-component threshold; record that
   overlap problem as the next proposition rather than union-bounding fixed
   cuts.

## Calibration and deliverables

Check odd/zero/`m=2`, `N=2`, `S_3,m=4`, `S_4,m=4`, `S_4,m=6`, whole-word
`H_4`, doubled-tree words, ordered component colors, and exact mass
orientation.  Write `checkpoint.md` and a nine-field `report.md`.  Any
computation may only falsify a named claim and must be reproducible.
