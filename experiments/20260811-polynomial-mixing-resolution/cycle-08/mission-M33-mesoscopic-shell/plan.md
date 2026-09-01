# M33 plan: entropy-matched mesoscopic shell action

## Exact objective

Use `(pq)(x)=p(q(x))`, `m=4N^3+4`, and the original lazy exact
`r={3,4,5}` chain.  For the graph neighborhoods `V^(a)` of the disconnected
set, move beyond the M31 `C_0^{-a}` comparison and analyze the genuinely
mesoscopic range

```text
1<=a<=A_N=floor(N log(N+1)/100).
```

The endpoint `A_N/log N` tends to infinity.

## Outer-shell encoding

For a path certificate, shrink every active overlap cluster to its first and
last crossing factors.  Its ordered product remains in the cut subgroup.
If its length is `l`, charge the minimal budget

```text
q=ceil((l-1)/4),  so l in {4q-2,4q-1,4q,4q+1}.
```

For a cut with `e` internal and `x` crossing transpositions, a fixed interval
has at most `x M^(l-2)` blocks: the first crossing is free and the last is
forced.  Exact disjoint-interval placement contributes `m^c/c!`, rather than
the `m^c` loss in M31.

## Entropy-matched source family

For the isolate cut, put exactly two crossing factors at each interval's
endpoints and fill its middle from the internal alphabet.  If the first
crossing is `s` and the middle product is `g`, use `g^(-1)sg` last; the block
product is exactly `g`.  Such a block of minimal budget `q` can be eliminated
in `q` actual heat-bath moves by shifting the last crossing left four slots at
a time and then internally resampling the final length-`3,4,5` window.

Require adjacent intervals to have at least two internal positions between
them and four trailing internal positions.  Require the excursion states of
the isolate vertex to be distinct.  Then every subgroup-valued interval that
contains crossings begins at the first crossing of one pair and ends at the
second crossing of a later pair.  Hence no alternative regrouping can reduce
the sum of the minimal budgets.

Use total budget exactly `a`; one final `H_5` move shifts the rightmost last
crossing four positions and raises the unavoidable budget to `a+1`.

## Counting target

Let `d=N-1`, `E=binom(d,2)`,

```text
beta= m d/E^2,
w_{a,c}(lambda)=binom(a-1,c-1)lambda^c/c!,
lambda=4beta.
```

Outer layouts have the cumulative weight over `Q<=a`.  Source layouts have
the exact-`a` weight, a falling-factorial correction `(d)_c/d^c`, and a
negligible placement correction.  For
`c<=2sqrt(80a)`, the falling-factorial loss is at most `N^5`; above this
threshold the ratio `w_{a,c+1}/w_{a,c}` is at most `1/4`.  Thus the complete
outer shell is at most a fixed power of `N` times the boundary-source family.

Non-isolate cuts retain the `exp[-Omega(N^2(s-1))]` factorial suppression;
the mesoscopic layout entropy is only `exp[O(N log N)]` and cannot offset it.

## Failure modes to audit

- A subgroup-valued crossing interval can contain three crossings; distinct
  excursion states, not parity, must exclude the shortening regrouping.
- The length-two endpoint case must be eliminated using a padded `H_3`, not a
  false standalone `L=2` simulation.
- Erasing crossing coordinates must send every hypothetical five-window to
  one contiguous internal-skeleton interval.
- The exact-`a` source coefficient must dominate every cluster count `c`,
  including the large-`c` tail.
- All non-isolate cuts and the exact global smaller-side orientation must be
  included before dividing flow.
- Only a genuine one-step `H_5` output will be charged in the full kernel.

## Computation

No finite computation is planned.  Every estimate is an exact enumeration or
an analytic bound; finite spectra cannot establish the claim.
