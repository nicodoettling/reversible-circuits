# M20 plan: midpoint-prefix renewal red team

Date: 2026-08-11  
Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Exact target and convention

Use `(pq)(x)=p(q(x))` and the original lazy exact `r={3,4,5}` kernel on the
global uniform identity bridge.  Search for a literal Terminal-B conductance
family inside connected full support, beginning with a midpoint-prefix
renewal/defect cut that is invisible to support-component data.

The primary candidate uses the explicit dense sequence

```text
N>=3,  k_N=2N^3,  m_N=2k_N=4N^3,
A_N={w in Omega(N,m_N):
     t_1...t_(k_N)=id and the full factorization graph is connected}.
```

## Obligations

1. Derive the exact global stationary mass of `A_N`, orient the smaller side,
   and prove that connected full support has asymptotically full conditional
   mass inside the prefix-renewal event.
2. Count every block window capable of changing the midpoint prefix and track
   laziness, block-size, window, and conditional-fiber normalizations.
3. Seek a superpolynomially small boundary.  If it fails, prove an exact
   inverse-polynomial escape from every state of `A_N`; do not mistake its
   factorially small stationary mass or the generic `O(1/m)` prefix action
   rate for a bottleneck.
4. Test the proof identities on `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` where
   feasible.  Finite calculations may falsify the count, mass orientation,
   or universal exit certificate but cannot prove asymptotics.
5. Preserve a halfway checkpoint and final nine-field report.  If the cut is
   rejected, leave a precise next Terminal-B proposition rather than a proof-
   route obstruction.

## Expected failure modes

- midpoint halves returning to identity have factorially small mass, but
  conductance divides by that same mass;
- the boundary transpositions can coincide, fixing the obvious Hurwitz move;
- restricting to connected full support allows noncrossing windows to leave
  the cut by disconnecting support;
- an unconditioned support coupon-collector estimate may be invalid after
  conditioning on both half returns;
- a prefix-local `O(1/m)` action rate is only polynomial and cannot support
  Terminal B.

