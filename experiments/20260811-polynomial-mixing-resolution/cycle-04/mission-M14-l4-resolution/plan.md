# Cycle 04 M14 plan: universal l=4 product-path resolution

## Exact target and convention

Use `(pq)(x)=p(q(x))`.  Put `M=binom(N,2)`, let `P_N` be uniform on
transpositions, and let `Q_N=P_N^2`.  A pair-length-four microfactorized
bridge is a length-eight transposition word with fixed even product `h`.
The nonlazy aligned chain is

```text
B_4=(1/3)(H_{1,4}+H_{3,4}+H_{5,4}),
```

where each heat bath is exactly uniform on its same-product four-factor
fiber.  Prove or refute connectivity for every `N>=3` and every feasible
endpoint, and if it is connected prove an explicit inverse-polynomial gap
in `N`.

## Proof program

1. Translate the checked Douvropoulos--Lewis arbitrary-product Hurwitz-orbit
   classification to the exact aligned windows: verify every adjacent
   Hurwitz generator and every required square refresh is a positive `H_4`
   outcome, including boundary positions.
2. Reprove locally that quotienting each ordered transposition pair to its
   `Q_N` increment preserves connected components.  This makes the
   microfactor theorem exactly equivalent to universal product-path
   connectivity.
3. Once qualitative connectivity is established, avoid an unquantified
   classification path: use the fixed state-count bound `V<=M^8`, minimum
   positive transition probability `1/(3M^4)`, and an arbitrary spanning
   tree to obtain complete path/load/Poincare accounting.
4. Cross-check against the exact all-endpoint `N<=7` artifacts from the
   frozen M14 mission.  These are falsification checks, not a proof input.

## Expected bound and failure modes

The proposed crude bound is

```text
gap(B_4;u,v) >= 2/(3M^20) >= (2/3)N^{-40}.
```

It is valid only if the qualitative translation is exact.  The main failure
modes are an arbitrary-product Hurwitz orbit invariant not changed by square
refresh, failure of a boundary Hurwitz move to lie in an aligned window, or
an omitted microfactor multiplicity.  A fixed-length polynomial bound does
not imply the uniform base result for `l<=O(N log N)` and is nonterminal for
the global goal.

## Calibration

Retain the `1/3` scan normalization, all endpoint cycle types, ordered
microfactor labels, and exact same-product probabilities.  Audit `l=2` as a
whole-word heat bath, `N=2` as elementary, original odd/zero/`m=2` cases,
the 27/120/3936 counts, near-minimal endpoint factorizations, and the fact
that a slow auxiliary `B` chain alone cannot refute `K`.

## Deliverables

Write a genuine halfway `checkpoint.md` and a final `report.md` with the
required nine-field schema.  Do not modify the frozen l=3 mission or shared
durable files.
