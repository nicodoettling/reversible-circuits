# M12 Intermediate-Density Plan

## Exact target

For the uniform law on `Omega(N,m)` and the exact lazy random-scan
`{3,4,5}` same-product heat-bath kernel, settle the remaining total-surplus
threshold window

```text
N>=3, m even,
2(N-1)<m<2+4binom(N,2)log(2N).
```

Since `G=m/2-N+c`, these are exactly support-component-count thresholds.
Seek either a universal inverse-polynomial two-sided conductance bound with
exponent independent of the threshold/surplus, or an explicit infinite
sequence with superpolynomially small conductance and complete stationary-mass
and full-`K` boundary-flow accounting.

Permutations compose as maps with `(pq)(x)=p(q(x))`; words evaluate as
`t_1...t_m`.  Every transition estimate retains laziness, block selection,
window scan, and exact conditional-fiber size.

## Work program

1. Refine the partition trace formula below its uniform mixing scale by
   retaining the leading trivial/sign/standard representation modes rather
   than treating all nonextremal modes with one error factor.
2. Combine exact feasibility and genus allocation with the component-size
   profile: partitions containing many small blocks have large minimum word
   length, while partitions with a giant block have stronger character gaps.
3. Seek a layer-tail comparison that is orientation-aware.  Use deterministic
   partition merges only when their exact-support count ratio is controlled;
   otherwise attempt a Hurwitz recursion or a direct word surgery with
   explicit multiplicity.
4. Reuse the proved actual-`H_3` merge flow through deletable internal squares,
   but replace the dense theorem's factor-four exact-support estimate by a
   bound valid at intermediate lengths.
5. Red-team any apparent obstruction: a rare pendant bridge-square statistic
   is not a cut unless it controls the smaller-side mass and every `r=3,4,5`
   boundary transition.

## Required calibration

Audit odd `m`, `m=0`, `N=2`, excluded `m=2`, all three exact smoke cases,
the whole-word `r=4` update at `m=4`, near-minimal doubled-tree states,
disconnected color interleavings, and size-two parity modes.  Do not infer a
universal conclusion from finite arithmetic.

## Deliverables

- `checkpoint.md`: a genuine halfway theorem or exact obstruction.
- proof/audit notes with every representation and multiplicity factor.
- `report.md`: the required nine-field schema and exact verdict.

