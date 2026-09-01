# R6 exact red-team plan

## Objective and declared targets

Independently enumerate small fixed-length transposition endpoint fibers and
audit the positive rank disintegration, the prescribed-endpoint star counts,
and precisely specified paired-lift architectures.

The canonical comparison target is the exact uniform law

```text
U(N,L;g) = Uniform{(t_1,...,t_L) in T_N^L : t_1...t_L=g},
```

with the public diagnostic focused on `g=e`.  Permutations will be maps under
`(p q)(x)=p(q(x))`; code will test this convention explicitly.

## Universal claims the finite run can falsify

1. The stable-sort map is product preserving, invertible for every binary
   old/star pattern, and gives the claimed exact `(k,h)` disintegration.
2. The R3 formula/recurrence returns the exact star-fiber size for every tested
   labeled endpoint, including impossible parity and minimal/padded lengths.
3. Exact branch weights reconstruct the full uniform identity law in the
   enumerated cases.
4. Any explicitly named paired, conjugation-symmetrized, or finite-Hurwitz
   architecture has a claimed output law or claimed equality to uniform.

Finite agreement will not prove a universal theorem or asymptotic mixing.
Finite disagreement can refute the corresponding universal identity or exact
sampler claim.

## Exact cases and diagnostics

- Boundary cases: `N=2`, `L=0`; odd identity lengths; minimal endpoint star
  lengths; pair padding.
- Full endpoint/star audits for useful `N,k`, targeting every endpoint through
  `N<=5,k<=6` when cheap.
- Full identity words and exact `(k,h)` branch laws for `(N,L)=(3,4),(4,4),
  (4,6)`; include lower-rank and endpoint count factors separately.
- Exact reconstruction of each word from its pattern, sorted old word, and
  relabeled star word.
- Paired-lift laws defined at word level; exact TV distance and observable
  probabilities under the lift and `U`.
- Exact one-step and short finite-step Hurwitz pushforwards where state size is
  manageable, with orbit-crossing limitations recorded.

## Architecture definitions to test

1. `AdjacentPairInsert`: start from a specified lower-rank identity law,
   choose labeled star pairs and insertion slots according to an explicit
   rule, retaining each inserted pair adjacent.
2. `ConjugationSymmetrizedPairInsert`: apply a uniform simultaneous global
   conjugation to the previous law.
3. `Hurwitz^t` postprocessing: apply exactly `t` steps of a specified lazy
   random right-Hurwitz kernel, including position and laziness probabilities.

The already-known sorted `h=e` fact is only a diagnostic.  An obstruction will
be promoted only if an additional observable has exact separated
probabilities under one of these fully specified laws and `U`; otherwise the
verdict remains a finite warning.

## Implementation and evidence

Use a self-contained Python enumerator rather than importing R1/R3 code.
Write exact rational probabilities as numerator/denominator pairs in JSON.
Record commit, command, Python/dependencies, deterministic parameters, and any
fixed seeds.  Produce `checkpoint.md`, scripts, machine-readable results, and
`report.md` ending in the required schema.

## Expected failure modes

- Naive pair insertion may generate the same word with nonconstant
  multiplicity; its pushforward must aggregate preimages exactly.
- Global conjugation can erase label bias while leaving structural ancestry.
- Hurwitz moves remain inside weighted support-component orbits and finite
  steps cannot be treated as a general mixing theorem.
- Full word enumeration grows as `binom(N,2)^L`; cases beyond `S_4,L=6` may
  require endpoint DP or be omitted with scope stated.
