# M31 plan: growing-radius shell red team

## Objective

For `N>=5`, `m=4N^3+4`, analyze the graph neighborhoods

```text
V^(0)={c>=2},
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}
```

at radii growing with `N`.  Use `(pq)(x)=p(q(x))` and the original lazy exact
`r=3,4,5` chain.  Seek a literal superpolynomial bottleneck; failing that,
prove a uniform inverse-polynomial action rate over a genuinely growing
range, avoiding an `N^{-O(a)}` fixed-radius bound.

## Structural route

Given a path from a disconnected word, fix a bipartition between its support
components.  The update windows decompose into overlap-connected clusters.
For every active cluster:

- its hull has length at most `4q+1` if it contains `q` updates;
- its final ordered product lies in the cut subgroup, because its initial
  factors were internal and every update preserves the local product;
- it contains at least two crossing factors.

Prove an active-block count

```text
A_l(P)<=l^2 x(P) M^(l-2),
```

by exposing the first crossing factor and observing that, after all other
factors are fixed, the last crossing transposition is forced by subgroup
membership.  This cancels the `m=Theta(N^3)` placement entropy for isolate
cuts.

## Boundary route

For radius `a`, start with `(s,q,q,q,s)` and push its last crossing factor
through `4a-4` arbitrary internal factors in `a-1` actual `H_5` moves.  Append
an arbitrary-endpoint tail on the other `N-1` labels which remains connected
after deletion of any union of `a` five-windows.  One further `H_5` push
creates a cluster span requiring `a+1` overlap-connected updates.

Tail robustness rules out every different initial cut.  Count the arbitrary
internal factors and endpoint tails so that the source family loses only a
fixed `E^5`, independent of `a`.

## Target theorem

For every

```text
1<=a<=a_*(N):=max(3,floor(log N)),
```

prove

```text
pi(V^(a))<1/2,
Phi_pm^K(V^(a))>=c C_0^(-a)N^(-25)>=N^(-C)
```

with universal constants.  This is inverse-polynomial uniformly over a
growing logarithmic range, rather than `N^{-O(a)}`.

## Failure modes

- Inactive/preparatory updates must not be charged as active clusters.
- A cluster block may have arbitrary parity; use neighboring even-time
  Cauchy--Schwarz for outside coefficients.
- A product-preserving active block cannot have exactly one crossing factor;
  prove the last-crossing uniqueness carefully for general bipartitions.
- A target with two separated crossing factors can delete both using two
  windows; exclude paths by cluster subgroup products, not only support
  deletion.
- Robustness is still needed to rule out a path starting from another cut.
- A `C_0^{-a}` loss is polynomial only through `a=O(log N)`; do not overstate
  the mesoscopic range.

## Computation

No finite computation is planned.  The deliverable is a universal counting
and flow theorem.
