# M94 halfway checkpoint: bulk-double obstruction isolated

Date: 2026-08-12. Status labels below are controlling.

## Scope and accepted starting point

The target remains the balanced family `n=3k`, odd `k>=3`,

```text
A_k=(0,k,2k),       B_k=(0,1)(k,2k),
eta_k=bar K(B_k,.)-bar K(A_k,.).
```

M91/M93's posterior identity and two-channel Abel reduction were rechecked.
`(BA2)`, direct signed `L1=O(k^-2)`, the general strict-edge lemma, H0, and
all sampler-gap consequences remain unresolved at this checkpoint.

## New exact diagnostic localization (finite only)

`rare_orbit_diagnostic.py` groups the complete signed second-row difference
by invariant target residual data before accumulating L1 or stationary L2.
It exactly uses the accepted kernel construction, then converts to floating
arithmetic.  At `k=3,5,7,9`, it reproduces M91's total TV and `(BA2)` energy.
The scaled `(BA2)` values are

```text
k:                 3        5        7        9
k^4 BA2:       5.2302   3.5773   4.2970   5.9974.
```

At `k=9`, the contributions grouped by minimum target residual size
`d=1,...,9` are

```text
0.642, 0.533, 0.661, 0.792, 0.892, 0.945, 0.859, 0.570, 0.103.
```

Thus the growth is distributed across bulk shells rather than caused by one
exceptional orbit.  Double targets contribute `4.5794`, while triangle
targets contribute `1.4180`.  The coordinator's independent `k=11` run gives
`k^4 BA2=8.7166` and `k^2 TV=0.8054`.  These are **finite empirical
falsification diagnostics only**.  They are consistent with a `k^-3` L2
scale, but support no asymptotic conclusion; direct L1 remains compatible
with `O(k^-2)`.

## Proved analytic progress in preparation

The completion-count kernel admits an exact signed Borel convolution.  With
`b_d=e^-d d^(d-1)/d!`, let `beta_3(x)` be the product of `b_d` over the three
cycles of `x^-1 h`, and `beta_5(x,y)` the analogous product over the five
cycles of `(xy)^-1 h` (zero when the required absolute-order relation fails).
Then

```text
K(x,y)=a(y)/[(n-3)(n-4)] * beta_5(x,y)/beta_3(x).
```

Expanding the quotient orbit sums once, rather than triangle-splitting the
two M91 channels, gives one signed convolution for the score and one positive
outer stationary sum.  A complete proof and all orbit-size factors will be
recorded in `bulk_obstruction.md`.

Two further facts are being proved there:

1. the Borel cumulative coefficients have the bulk scaling
   `sqrt(k) D_floor(xk) -> mathcal D(x)` with an explicit signed density, and
   the boundary scaling `D_u ~ -3 sqrt(u)/(2 sqrt(2 pi) k)` for
   `1<<u<<k`;
2. every fixed compact region of generic double-target four-compositions has
   stationary mass `Theta(1/k)`, whereas a generic bulk orbit has mass
   `Theta(k^-4)`.

Consequently `(BA2)` would force conditional RMS posterior score
`O(k^-3/2)` throughout every such bulk region.  The weaker direct L1 target
only requires mean absolute score `O(k^-1)`.  This is the exact missing
half-power and explains why an L2 failure need not harm signed TV.

## First unresolved step

To refute `(BA2)` rigorously, it now suffices to find a fixed positive-volume
double-composition region on which the fully channel-combined score has one
sign and magnitude at least `c/k`.  Its proved stationary mass `>=c'/k`
would yield `(BA2)>=cc'/k^3`.  The ongoing target-shape audit is locating such
a region; no sign claim is promoted from finite data.
