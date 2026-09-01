# M192 Plan — Fully Combined Channel-Two Prefix Response

## Objective

Attack only M186/M189's first open coefficient lemma: the fully combined
`J=2` contribution to `(PCR)` or the weaker `(WPCR)`. Derive the exact
`Lambda_L-Lambda_F` shared-endpoint/collision contribution and either prove a
signed prefix/Abel estimate, find an exact counterexample to `(PCR)`, or freeze
a strictly narrower rigorous reduction.

## Target and convention

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` for odd
`k>=3`, `h=(0,1,...,n-1)`, `A=(0,k,2k)`, and
`B=(0,1)(k,2k)`. The target is the uniform minimal-factorization law of `h`
under the fixed-cell nonlazy cyclic rank-two coordinate kernel. It is not the
global identity bridge or the lazy `{3,4,5}` heat-bath chain.

## Immutable gate

Verify M180/M182 and M186/M189 checksum manifests before adopting claims.
Never edit those missions.

## Exact claim under attack

For M186's already channel-, kind-, and collision-combined prefixes

```text
A_D=sum_(2<=d<=D)[M_1(d)+M_2(d)],
C_D=sum_(2<=d<=D)M_1(d),             2<=D<=(n-1)/2,
```

prove `(PCR)`, `|A_D|+|C_D|=O(sqrt(D)/n)`, or its exact weighted sufficient
form `(WPCR)`. The `J=1` estimate may be retained as a proved input, but a
final `(SCBR)` claim may not be obtained by separately taking absolute values
of `J=1` and `J=2` unless the full signed combination is justified.

## Method

1. Classify ordered `J=2` pairs from `L` and `F` into shared-endpoint
   triangles, same-run doubles, cross-run doubles, and all boundary collisions.
2. Write exact prefix observables directly under `Lambda_L-Lambda_F`, then
   disintegrate by the first smaller split without deleting embedding terms.
3. Seek a signed cumulative identity or a weighted Abel bound. If unavailable,
   isolate the smallest explicit coefficient kernel whose bound is equivalent
   or sufficient.
4. Use compact exact diagnostics only for odd `k<=7`; distinguish exact finite
   results from universal proof and infer no asymptotics from signs.

## Prohibitions and deliverables

No broad quotient/shell computation, channelwise final triangle inequality,
finite-sign promotion, PCS/FCL1/direct-L1/H0/gap/mixing/Terminal inference,
or edits outside the owned directory. Write start/halfway/final checkpoints,
a compact derivation or obstruction, exact checker/results if used, a
nine-field report, hashes/manifest, and request fresh immutable audit when
frozen.
