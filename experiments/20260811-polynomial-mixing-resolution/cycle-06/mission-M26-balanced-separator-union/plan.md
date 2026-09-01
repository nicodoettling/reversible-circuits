# Cycle 06 M26 plan: balanced-separator union and largest component

## Exact target and convention

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  The target is the
global uniform bridge law and `K` is the exact lazy same-product heat bath
with block sizes `{3,4,5}` and every normalization retained.

Put `a=floor(N/2)` and define

```text
B_(N,m)=union_(|S|=a){w:no factor crosses (S,S^c)},
C_(N,m)={w:largest support-component size<=N/2}.
```

Unlike a fixed separator, these are profile unions.  Seek a literal
superpolynomial full-`K` bottleneck; failing that, identify the exact
stationary boundary layer and prove or refute a uniform escape mechanism.

## Exact-overlap formulation

Index states by their exact labeled support-component partition `P`, with
isolated labels included as singleton blocks and exact word count `E_P(m)`.
Then `B` is the disjoint macro sum over partitions whose block-size multiset
has a subset sum `a`; `C` is the sum over partitions with maximum block size
at most `N/2`.  This counts every exponentially overlapping separator event
once and fixes the exact smaller-side orientation.

## Deep-interior audit

Let `V(w)` be the set of labels used by a factor and, for `N>=24`, define

```text
D={w:|V(w)|<=a-10}.
```

An `r<=5` update can introduce at most `2r<=10` labels.  Hence every output
from `D` still uses at most `a` labels, has at least `a` isolated labels,
and remains in both `B` and `C`.  Use this to:

1. refute a worst-state/aggregated-fixed-cut escape lemma;
2. localize the complete `Q_3+Q_4+Q_5` boundary to the exact shell
   `B minus D` or `C minus D`;
3. state the precise stationary shell-mass estimate which would yield a
   Terminal-B sequence, and test whether any available enumeration proves
   or rejects it.

## Calibration and deliverables

Compute exact union masses in `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`, retain
whole-word `H_4`, color ordering, and exact orientation.  Write a genuine
`checkpoint.md` and a nine-field `report.md`; finite calculations, if any,
may only falsify a named lemma and require reproducible metadata.
