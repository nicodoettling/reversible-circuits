# M27 plan: base-scale exceptional modes

## Objective

For the complete raw-pair heat-bath bridge on `E=T_N^2` with arbitrary
endpoint `h in A_N`, prove an inverse-polynomial spectral gap throughout the
base range `3 <= l < C_mix N log(N+1)`, or reduce the problem to a strictly
smaller explicit comparison proposition.  The permutation convention is
`(pq)(x)=p(q(x))`; tuple products are evaluated left-to-right.

## Proof lanes

1. Audit the sufficient correlation estimate `mu_l^* <= A/l`, using the
   exact normal scalar Gram blocks from M16.  Isolate exceptional additive
   modes by reflection surplus `g=l-(N-#cycles(h))/2`.
2. Prove a quantitative bound for the square-coordinate additive mode at
   bounded surplus and identify what it does and does not control.
3. In the minimal sector `g=0`, translate full-cycle factorizations through
   noncrossing maximal chains, parking functions, Pollak's diagonal quotient,
   and tree encodings.  Prove the ideal quotient-coordinate heat-bath gap.
4. Audit whether quotient-coordinate refresh, Pruefer refresh, or uniform
   spanning-tree basis exchange can be simulated by Hurwitz/complete-pair
   moves with polynomial path length and recoverable polynomial metadata.
   Explicitly test the named claim that a local rank/Hurwitz move is a single
   exchange under the relevant tree bijection.
5. Record the smallest surviving comparison proposition, including exact
   stationary weights and congestion requirements; do not infer a theorem
   from finite spectra.

## Named falsifiers and failure modes

- A high-correlation endpoint/eigenmode with `l mu_l` unbounded falsifies the
  uniform `A/l` route.
- A local factorization move whose encoded trees differ by more than one edge
  falsifies direct edge-by-edge domination of the UST basis-exchange chain.
- Coordinate swaps alone preserve the parking-function entry multiset and
  therefore cannot establish irreducibility.
- The raw factorization graph is not assumed to be a uniform Cayley tree; all
  uses of Dénes/Goulden--Yong encodings must track the actual bijection.

## Deliverables

`halfway_checkpoint.md` will freeze proved reductions and the exact remaining
comparison. `report.md` will use the required nine-field schema. Any finite
calculation will include its exact command and the universal claim it can
falsify.
