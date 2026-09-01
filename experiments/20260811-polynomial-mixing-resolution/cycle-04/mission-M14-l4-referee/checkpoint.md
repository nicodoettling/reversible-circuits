# Halfway checkpoint

The structural proof has passed its first independent audit.

- The cited type-A Hurwitz classification applies to every permutation:
  disjoint-cycle minimal transposition factors witness the parabolic
  quasi-Coxeter hypothesis.  The exact source labels are published Theorem
  18 and Proposition 8(4), with preprint labels Theorem 4.2 and Proposition
  2.7(4).
- For a component containing `q_C` endpoint cycles on `v_C` vertices, the
  target length is `v_C+q_C-2+2g_C`.  Minimal cycle factorizations plus a tree
  of `q_C-1` bridge squares and `g_C` surplus squares realize it.  Fixed
  endpoint cycles are included; an isolated fixed point has weight zero.
- All adjacent position pairs lie in an aligned four-window.  Exposed bridge
  and surplus squares can therefore be replaced one at a time without losing
  access to the remaining exposed squares.  After every square is replaced,
  no unintended cross-cycle edge remains.
- For nonidentity endpoints all excess pairs can be stored on one edge of a
  fixed nontrivial endpoint cycle.  For the identity endpoint every factor
  is exposed in adjacent square pairs and refreshed to one designated edge.
  At minimum length there is no square, but the endpoint-cycle macro is
  already unique.
- The product-path projection lifts every adjacent two-increment move, and
  the microfactorizations above a fixed product path communicate by retaining
  the neighboring increment while changing one chosen ordered pair.
- With `V<=M^8` and `p_*>=1/(3M^4)`, the tree inequality gives
  `gap>=2p_*/[V(V-1)]>=2/(3M^20)`.  The Hamiltonian multiplier is exactly
  three.  Positivity of the average heat-bath operator makes the stated TV
  bound safe (indeed deliberately loose).

The newly frozen all-length addendum uses the same qualitative proof and the
same tree inequality with `V<=M^(2l)` and scan factor `1/(l-1)`.  Its claimed
exponent `4l+4` is arithmetically consistent, but it is superpolynomial when
`l` grows and hence remains nonterminal.  Exact finite calibrations and a
final artifact/status audit remain.
