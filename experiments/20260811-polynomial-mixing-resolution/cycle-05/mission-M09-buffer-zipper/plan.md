# M09 plan: polynomial-width randomized defect-buffer zipper

## Exact target

For `E=T_N^2`, with `p(a,b)=ab` and multiplication convention
`(pq)(x)=p(q(x))`, compare the whole-fiber heat bath on

```text
Omega_l(h)={x in E^l:p(x_1)...p(x_l)=h}
```

to the adjacent two-increment exact heat-bath chain, uniformly for every
feasible `h` and `l<=C_0 N log(N+1)`.  A successful comparison must have
path length and directed edge congestion bounded by `(Nl)^C` with a universal
exponent.  The proposed route stores the nonabelian zipper defect in an
`r=O(N)` increment buffer.

## Audit order

1. Formalize buffer-shift legality and the exact source/target data erased by
   a width-`r` shift.
2. Prove a bridge-count/congestion obstruction for canonical or polynomial-
   size defect codebooks, using pointwise smoothing only where its hypotheses
   are available.
3. Determine the minimum codebook size needed to avoid the obstruction and
   whether randomized fixed-product buffer encodings can supply it without
   hiding `|E|^{Theta(r)}` metadata.
4. State the smallest balanced randomized-transport lemma that would make the
   zipper comparison work, including all endpoint-count ratios and local-path
   congestion.
5. Attack that lemma on minimum-length endpoints, fixed points, and the
   `N=3,4` surjective-support calibrations.

## Inherited facts and exclusions

- The one-letter surjective-support zipper has independently accepted gap
  `l^-3|E|^-3`; it applies to `E=T_N^2` only for `N=3,4`.
- For `N>=5`, `p(E)` is only the identity, 3-cycles, and double
  transpositions.
- Every feasible arbitrary-endpoint aligned fiber is connected, but the known
  all-length tree bound has exponent growing with `l`.
- Fixed canonical hubs have exponential congestion.  No conclusion about the
  actual chain follows from failure of this buffer architecture.

## Deliverables

Maintain `checkpoint.md` and `report.md` with the required nine fields.  Any
obstruction will be scoped to a precisely defined route class, and the first
surviving proposition will be stated without assuming the desired base gap.

