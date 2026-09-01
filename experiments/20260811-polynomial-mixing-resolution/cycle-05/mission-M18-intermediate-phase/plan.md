# Cycle 05 M18 plan: intermediate component phase

## Objective and exact target

Work with maps on `[N]`, composition `(pq)(x)=p(q(x))`, and word product
`t_1...t_m`. The target is the global uniform law on `Omega(N,m)`, and the
kernel is the original lazy exact `{3,4,5}` same-product heat bath, with all
window and block-size normalizations retained.

The literal terminal target is either an explicit infinite superpolynomial
conductance cut for this `K`, or an inverse-polynomial rejection of a named
support-component phase family in

```text
2(N-1)<m<2+4 binom(N,2) log(2N).
```

## Named family

For fixed surplus genus `g>=1`, take

```text
m=2(N-1)+2g,
F_(N,g)={connected exact-full-support words on [N]}.
```

At this length `F_(N,g)` is exactly the bottom component-count layer `c=1`
and total-surplus layer `G=g`. It is therefore a sharpened version of the
possible component-phase cut, not an auxiliary-chain cut.

## Proof route

1. Use the proved DYZ ratio
   `a_(g,d)/a_(g-1,d)<=d^3/12` for
   `a_(g,d)=C_g(d)/(2d-2+2g)!`.
2. Lower-bound `C_g(N-1)` by an explicit injection from genus-zero words,
   and upper-bound `C_g(N)` by iterating the DYZ ratio.
3. Count marked adjacent leaf-square incidences exactly between
   `C_g(N-1)` and `C_g(N)`.
4. From every marked state, use a boundary-safe `H_3` outcome to remove the
   marked label. Bound the exact transition probability using the original
   laziness, block scan, window scan, and conditional fiber size.
5. Divide the global stationary flow by the smaller stationary side. Do not
   assume which side has mass at most one half; use
   `min(pi(F),pi(F^c))<=pi(F)`.

## Expected scope and failure modes

The anticipated bound is polynomial for every fixed `g`, with an exponent
depending on `g`. It therefore rejects all bounded-surplus versions of this
bottom-layer phase cut but does not settle growing `g`, arbitrary component
thresholds, or internal cuts. In particular, iterating the DYZ estimate for
growing `g` is allowed to lose a superpolynomial factor and will not be
advertised as a universal result.

No computation is planned. The universal claim is purely enumerative and
will be checked against the exact small cases and the known fixed-degree,
large-genus failure of a uniform pendant-square lower bound.
