# M102 halfway checkpoint: signed bulk profile, no sign theorem yet

Date: 2026-08-12. Controlling status: `(BD)` remains **unresolved**.

## Locked scope and exact interface

The target, convention, sources, quotient kernel, and event are exactly those
of frozen M94/M100: `n=3k`, odd `k>=3`,

```text
A_k=(0,k,2k),       B_k=(0,1)(k,2k),
E_k={double targets with all four support gaps >=(k+1)/2}.
```

Write

```text
R^Phi_(j,k)(s)=Phi_(j,s)(K 1_E),
R^Psi_(j,k)(s)=Psi_(j,s)(K 1_E),       j=1,2.
```

Then M91's exact Abel identity gives the channel-combined scalar formula

```text
Delta_k(E_k)
 =sum_(j=1)^2 alpha_(j,k) {
    sum_(u=1)^(k-2) D_(u,k)[R^Phi_(j,k)(u)-R^Phi_(j,k)(u+1)]
   +sum_(s<k/2)q_(s,k)[R^Phi_(j,k)(s)-R^Psi_(j,k)(s)] }.
```

No channelwise absolute value or targetwise square occurs here.  The first
bracket is `Gradient_k` and the second is `Embedding_k`.

## Bounded finite probe and falsification findings

`bulk_score_probe.py` independently reconstructs the frozen quotient kernel
and records all event-orbit scores at `k=7,9`.  It is deterministic,
floating, and finite only.  It reproduces

| `k` | `k pi(E_k)` | `k^2 Delta_k(E_k)` | `k Delta/pi(E)` |
|---:|---:|---:|---:|
| 7 | .07314864 | .04320591 | .59065907 |
| 9 | .07224023 | .04216567 | .58368673 |

The probe refutes a tempting pointwise-sign shortcut: at `k=7` three of 28
event orbits have negative scores, and at `k=9` seven of 60 do.  At `k=9`,
`k z_k(t)` ranges from `-.4102` to `1.3503`.  The negative targets lie in a
separated-color corner such as gaps `(5,5,5,12)`, while the nested-color
representatives in this finite probe are positive.  Thus the total positive
defect cannot be proved by claiming `z_k>=0` on all of `E_k`.

The central event has the useful exact excess parameterization

```text
(x,y,z,w)=((k+1)/2+a, ..., (k+1)/2+d),
a+b+c+d=k-2.
```

This turns its stationary mass into a compact simplex Riemann sum, but the
score still depends on color and ordered embedding, not only on the residual
size triple.

## Analytic scaling isolated

M94 already proves, in the bulk, `sqrt(k)D_floor(kx)->mathcal D(x)` and
`k^(3/2)q_floor(kx)->Q(x)`.  Therefore a proof of `(BD)` can be reduced to
second-order response profiles for the two displayed `R` families.  The
leading `k^-3/2` contribution must be shown to cancel before a `k^-2`
constant can be read off; treating `Phi` and `Psi` by total variation loses
this cancellation.  The finite split data are consistent with a nonzero
`k^-2` constant, but do not prove whether the Abel gradient is lower order or
contributes a smaller signed constant.

The current analytic target is a coefficient-transfer lemma: establish
uniform second-order expansions of the channel-combined responses on compact
`x=s/k` intervals, plus a Borel boundary envelope, and obtain

```text
k^2 Delta_k(E_k) -> C_bulk
```

as an explicit signed integral over the split variable and the central-event
simplex.  A certified proof that `C_bulk != 0` would settle `(BD)`.  Merely
quadraturing finite `k` rows will not be promoted.

## Controlling scope

No exhaustive calculation beyond `k=9` will be run.  `(BA2)`, direct signed
`L1`, H0, all bridge/identity-chain gaps, and both Terminals remain open.
