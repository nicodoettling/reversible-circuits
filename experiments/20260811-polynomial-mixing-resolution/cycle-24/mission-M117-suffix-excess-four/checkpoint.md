# M117 halfway checkpoint

Date: 2026-08-12.

## Status

The independent L=4 derivation is structurally complete and the first exact
universal certificate is positive. The result remains provisional until the
literal reset-energy and arbitrary-deficit L=2 audits are completed.

## Exact structure derived

For `B=s-4`, the contextual mean is supported on exactly 16 ordered
compositions:

- eight refinements of prefix total four followed by `B`;
- four refinements of prefix total three followed by `s-3`;
- two refinements of prefix total two followed by `s-2`;
- `(1,s-1)` and `(s)`.

Their positive support comprises 11 `(k,t)` groups. Exactly 15 canonical
basins are exceptional: all eight prefix-total-four basins, all four
prefix-total-three basins, both prefix-total-two basins, and `(1,s-1)`.
Exactly seven groups send retained deep mass:

```text
t=s-3: k=2,3,4 -> all-deficit L=0
t=s-2: k=2,3   -> arbitrary-deficit L=1
t=s-1: k=2     -> j=1 arbitrary-deficit L=2; j=2 right-heavy L=2
t=s:   k=1     -> right-heavy L=3
```

All `j=1,...,k` ranks are retained before aggregation.

## New child lemma

For an arbitrary-deficit `L=2` context, direct support/basin accounting gives
M109's three-exception envelope with `z` replaced by
`p=D/(K_0+1)` and `d` by
`D(D+1)/[(K_0+1)(K_0+2)]`. Its descendants are bounded by

```text
(1-d)(1-y)/3 + (2/3)(1-p) F_(a,y,h)(D/(K_0+2)),
```

where `F` is the accepted arbitrary-deficit L=1 envelope. This is an envelope
for `H/q`, not a contraction assertion for every deficit.

## Provisional universal sign

After clearing the positive denominator

```text
prod_(a=1)^4 (1+a z)^2,
```

the L=4 slack has multidegree at most `(2,2,2,2,2,10)` in the five
consecutive Cayley ratios and `z`. Exact Bernstein calculations currently
give:

- `s=5,...,21`: all `17*11=187` coefficients positive;
- tail box `[1/3,2/5]^5 x [0,1/2]`, with all path heights enlarged to one:
  all `3^5*11=2673` coefficients positive;
- exact tail minimum `742081/227812500` at index `(2,2,2,2,0,0)`.

An exact full-DAG scan through `s=20` and
`K in {1,2,5,64,4096}` has zero reset, resolvent, envelope, or target
failures. These finite rows audit formulas only; the Bernstein certificate is
the proposed analytic completeness argument.

## Remaining audit before freeze

1. compare the grouped reset energy with a literal enumeration of every
   canonical basin on bounded ranks;
2. test the new L=2 envelope over arbitrary reachable deficits, not only the
   two children occurring in L=4;
3. verify Bernstein interpolation identities at independent rational points;
4. write the proof note and nine-field report, rerun exact artifacts, and
   freeze hashes.

## Final checkpoint

All four audit items completed. The literal reset path matches the grouped
recurrence and every active exceptional current/capacity on ten selected
rows. The new child envelope passes 252 arbitrary-deficit contexts. Both
certificate families and their off-grid identities pass with zero
nonpositive coefficients. A fresh standalone `/tmp` rerun is mathematically
identical to the durable JSON after excluding only elapsed time. Final verdict:
`PROMOTE WITH FRESH REFEREE AUDIT`; first open suffix excess is `L=5`.
