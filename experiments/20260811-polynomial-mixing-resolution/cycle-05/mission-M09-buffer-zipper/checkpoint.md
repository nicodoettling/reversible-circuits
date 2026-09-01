# Halfway checkpoint

## Current reduction

A width-`r` zipper shift necessarily has the product equation

```text
p(B) p(X) = p(Y) p(B'),
p(B') = p(Y)^(-1) p(B) p(X),
```

for `B,B' in E^r` and payloads `X,Y in E`.  Thus legality alone asks for a
representation of every encountered defect by `r` paired increments.  The
harder comparison issue is distributional: replacing a buffer by one fixed
canonical representative, or by only polynomially many representatives per
defect, forces every routed demand through a tiny cylinder set once a
complementary segment has pointwise mixed.

Let `q=|E|=M^2`, let `G=A_N`, and let `F_r(d)` be the set of `r`-increment
words with product `d`.  If a route has a synchronized phase at which its
buffer belongs to codebooks `C_r(d) subset F_r(d)`, with
`sum_d |C_r(d)|=S`, then under a fixed-endpoint bridge with a pointwise-mixed
complement the stationary mass of that phase cylinder is `Theta(S/q^r)`.
Any unit all-pairs comparison flow forced through it has vertex/edge
congestion at least `Theta(q^r/S)`.  In particular one canonical buffer per
defect pays at least `q^r/|G|`, which is superpolynomial for linear `r`.

This does **not** refute randomized buffer encodings using a macroscopic
fraction of each `F_r(d)`.  The surviving issue is to couple such large
codebooks across
`d -> p(Y)^(-1)d p(X)` and locally route the coupling with polynomial
congestion.  That elementary shift is itself an arbitrary-endpoint
length-`r+1` bridge transport, so invoking its spectral gap would be circular.
The final report will make both the obstruction and the noncircular surviving
lemma exact, with constants and boundary qualifications.

