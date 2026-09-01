# Cycle 04 M14 plan: fixed-endpoint aligned-H4 falsification

## Exact target

Use `(pq)(x)=p(q(x))`.  Let `P_N` be uniform on transpositions and
`Q_N=P_N^2`.  A microfactorized pair-length-`l` bridge from `e` to
`h in A_N` is an ordered length-`2l` transposition word with product `h`.
The local chain resamples aligned four-factor windows starting at original
positions `1,3,...,2l-3` exactly uniformly within their same-product fibers.

The universal qualitative statement under falsification is:

> For every `N>=3`, `l>=2`, and every `h in A_N` with
> `Q_N^l(e,h)>0`, the microfactorized fixed-endpoint fiber is connected under
> the aligned length-four heat baths.

A single exact disconnected fiber refutes this statement and makes M10's
worst-endpoint base constant zero.  Finite connectedness cannot prove the
statement or any polynomial gap.

## Exact pair-length-three quotient

At `l=3`, write a state as three ordered transposition pairs `(A,B,C)` with
pair products `(a,b,c)` and `abc=h`.  The left aligned heat bath preserves
`C,h`; the right one preserves `A,h`.  Therefore states are edges of a
bipartite incidence multigraph:

- left vertices are ordered microfactor pairs `A`;
- right vertices are ordered microfactor pairs `C`;
- `A--C` is present iff `a^{-1}hc^{-1}` belongs to `supp(Q_N)`.

All possible middle microfactorizations on an incidence edge form one
heat-bath clique.  Connected components of this bipartite support graph are
therefore exactly connected components of the aligned-H4 state graph.
Simultaneous conjugation by `S_N` makes the component count depend only on
the ordinary cycle type of `h`, including endpoints from split `A_N` classes.

This encoding replaces `M^6` words by at most `M^2` vertices on each side,
or further by the `O(N^4)` pair-product support because copies with the same
product have identical neighborhoods.

## Program

1. Implement both the ordered-microfactor graph and the product-support
   quotient.  Assert that their component counts agree in calibration cases.
2. Test every feasible endpoint cycle type at `N=6,l=3`, recovering exact
   six-transposition witnesses if a component splits.
3. If it survives, extend only along the same named claim to larger `N` at
   `l=3`, where endpoint defect is at most six, and to the smallest new
   `l=4` quotient/SAT encoding if feasible.
4. Record component sizes, graph diameters, and endpoint types only as bounded
   diagnostics.  They cannot prove a uniform diameter or gap.
5. Test a named canonical-reduction lemma only if it is needed to compress
   the search; do not route a universal comparison through a hub.

## Calibration and failure modes

- `l=2` is a whole-interval heat bath and must be connected.
- Reproduce the prior all-endpoint conclusions for `N=3,l=3`, `N=4,l=3`,
  and `N=5,l=3`, including identity sizes `27`, `3936`, and applicable
  `m=4` counts from the original chain.
- `N=2` is singleton; odd original word lengths are empty; original `m=2`
  is excluded for K and distinct from this fixed-product auxiliary chain.
- Retain ordered microfactor labels.  Product-level quotienting is valid only
  after proving that copies with the same product have identical nonempty
  neighborhoods.
- A slow or disconnected auxiliary B fiber does not by itself refute K;
  `K>=B/12` transfers only lower gap bounds.
- The exact kernel probabilities are irrelevant to connectivity but will be
  stated: scan probability `1/(l-1)`, then uniform over the aligned
  four-factor conditional fiber.

## Deliverables

- `plan.md`, genuine `checkpoint.md`, and final `report.md`.
- Deterministic source plus compact JSON, with commit, Python version, exact
  commands, no seed, and the precise universal claim each run could falsify.
