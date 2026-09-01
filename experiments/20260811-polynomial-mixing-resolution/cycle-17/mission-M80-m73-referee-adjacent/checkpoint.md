# M80 checkpoint: frozen M73 referee decision

Date: 2026-08-12.

## Decision

**ACCEPT, with zero numbered objections.** The acceptance is scoped to M73's
proved exact cyclic-product reduction and finite certificates. It does not
accept the unresolved shared-factor influence inequality, an `H_0` gap, a
fixed-long-cycle bridge gap, or Terminal A/B.

## Frozen integrity

- Requested report SHA-256:
  `bfb427ff4cc8649c2f5dda61f64fd0ba5364143f3cc93c2bcbe61810392a6692`;
  independently matched.
- Requested manifest SHA-256:
  `da76521810b9ec668ef0e09fab80237d5cea715f9a40878548663d35f8ddf60f`;
  independently matched.
- `sha256sum -c` from the repository root passed all 35 frozen entries.
  No `__pycache__` or `.pyc` entry was present in the frozen directory.

## Independent mathematical audit

1. With `(pq)(x)=p(q(x))` and left-to-right factors, fixing one pair product
   `g` leaves the minimal completion `g^-1 h`; fixing two ordered pair
   products leaves `(gs)^-1 h`. Dénes plus disjoint-cycle interleaving gives
   exactly the displayed `F_r`, `pi`, `J`, and `K`. Centrality of the squared
   transposition sum justifies independence of the chosen two coordinate
   locations. Orbit pushforward uses literal orbit sizes. The twisted pair
   symmetry becomes ordinary symmetry after cyclic-orbit summation, so the
   exact quotient detailed balance is valid.
2. On the invariant block `K=K*`, an eigenvalue `kappa` is real. The `l`
   coordinate evaluations have covariance
   `(1-kappa)I+kappa 11*`; positivity gives
   `kappa>=-1/(l-1)`. Combining this with M16's accepted scalar Gram formula
   leaves only the largest positive invariant eigenvalue.
3. Oriented three-cycles give cyclic positive 3-compositions, including the
   unique balanced orbit stabilizer. Oddness makes every double-transposition
   orbit free. Lagrange inversion gives the stated `T^3` and
   `T^4/(1-T)` normalizations, hence masses `3/n` and `(n-3)/n`.
4. Conditioning the first two residual factors on their component colors
   gives exactly the interleaving weights in the four schemas
   `I3,IS,IN,X`. Fixing one edge or one pair product in a minimal cycle
   factorization gives the stated `nu_d` and `mu_d`. After uniformly orienting
   an edge, the factor `d/2` from oriented anchors converts `nu_d` exactly to
   two critical Borel variables conditioned on their sum. The smaller-part TV
   identity and `Theta(d^-1/2)` loss follow.
5. The diameter proof covers both chord-placement cases. If the shorter chord
   fits strictly inside the larger arc cut by the first chord, their product
   is a noncrossing double transposition. Equality can fail only at arc lengths
   `(n+1)/2,(n-1)/2`; sharing an endpoint in cyclic order produces the
   admissibly oriented 3-cycle. The intermediate lift shares one raw factor
   with each endpoint orbit.
6. A path of at most two adjacent source edges turns the proposed local TV
   bound into `delta(bar K^2)<=2C/n^2`. Dobrushin contraction bounds every
   nonconstant eigenvalue of `bar K^2`; self-adjointness of `bar K` therefore
   gives `|kappa|<=sqrt(2C)/n`. This implication has no missing laziness,
   orbit-mass, or square-root factor.

## Independent computation

`independent_exact_audit.py` was written from scratch in this directory; it
imports no M73 code. It exactly reconstructs the marginal, quotient kernel,
stationary masses, detailed balance, `K^2`, shared-factor graph, constructive
chord placement, and Borel entries. Results:

```text
n  support  quotient  graph edges  diameter  max adjacent TV(K^2)
5       20         4            6         1  1
7      105        15           95         2  7185517/30375000
9      336        38          553         2  2094407996609/19603684800000
```

It also found zero constructive chord-placement failures among respectively
`100,441,1296` ordered chord pairs and checked every conditioned-Borel entry
through `d=n` exactly. Independently rerunning M73's schema verifier reproduces
all `400` (`n=5`) and `11025` (`n=7`) entries. Its output is byte-identical to
the frozen schema JSON. Independently rerunning M73's kernel script reproduces
both rational adjacent maxima, the dimensions, graph edges, and diameters.

## Referee caveats retained

- M73's sixteen-schema cancellation is an exact decomposition, not a bound:
  defining `E_g` with an `n^2` prefactor proves no uniform control of `E_g`.
- The Borel small-fragment coupling is explicitly too weak.
- Exact checks through `n=21` are finite evidence only.
- The common-factor residual-forest description is an interface for a future
  coupling, not itself a coupling theorem.

## Continuation result

The arbitrary shared-factor graph can be replaced by the stricter graph in
which the two differing chords must also share an endpoint. This stricter
graph has **proved universal diameter at most four**: every double orbit is
one such move from an oriented-three-cycle orbit, and the three-cycle-orbit
subgraph has diameter at most two via a shared positive gap. Therefore an
`O(n^-2)` two-step TV bound only for these three-cycle cut/join edges still
implies `|kappa|=O(n^-1)`. The local TV bound itself remains open.
