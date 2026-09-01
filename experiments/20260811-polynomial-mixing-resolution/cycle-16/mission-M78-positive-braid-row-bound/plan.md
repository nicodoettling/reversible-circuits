# M78 plan: positive-braid worst-row bound

## Objective and target

Work with permutation composition `(pq)(x)=p(q(x))`, left-to-right word
products, and right Hurwitz generators

```text
R_i(...,a,b,...)=(...,b,bab,...).
```

The target law is uniform on `Omega(N,m)`.  The literal ambient regime is
`N>=5,m=2N-2`; the literal chain is the lazy exact same-product `{3,4,5}`
heat bath fixed in `GOAL_SPEC.md`.  This mission attacks only M75's frozen
two-component obligation:

```text
inf_(x in Gamma) Pr_(pi uniform in S_m)
  [beta_pi x has a globally adjacent square whose deletion leaves the
   positive-genus component connected] >= (Nm)^(-C).
```

Here `beta_pi` is exactly M75's canonical bubble-sort positive lift.  A
positive result must be a literal all-parameter theorem.  A negative result
must be an exact zero row, an asymptotic superpolynomial row family, or a
precisely delimited falsifier of a proposed intermediate lemma.  Finite
positive incidence is calibration only.

## Inherited frozen inputs

1. M75 Theorem 2.1 and its endpoint specialization: any polynomial
   worst-row marked probability gives arbitrary-partial-macro boundary flow
   with no braid-support cardinality loss.
2. M75/M77's exact `m!`-regular incidence double count is average-only and
   cannot substitute for a row minimum.
3. Once a connected two-deletion certificate is chosen, M75's positive
   null-push has polynomial length and actual-edge source recovery.
4. The direct-certificate radius-one cover is refuted at `N=6,m=10`; the
   positive-simple-braid law survives that witness.

No frozen predecessor directory or coordinator-owned file will be edited.

## Work lanes

1. Derive the canonical positive lift as a uniform random elimination
   process, including exact conditions for consecutive output factors to be
   equal and for deletion connectivity to be preserved.
2. Search exact minimum rows where enumeration is possible.  Prioritize
   all-distinct genus-one identity words, since they kill the most immediate
   duplicate-pair lower bound.
3. Use deterministic, fixed-seed orbit search at larger sizes to look for
   zero or rapidly decaying rows; exactly enumerate every tractable proposed
   falsifier.
4. Test named repaired state-independent laws only after the canonical law
   or a needed intermediate lemma fails.  Keep their length and literal
   bijectivity accounting explicit.
5. Attempt a theorem from a bounded-depth elimination certificate.  Do not
   infer one from average DYZ incidence or finite row values.

## Expected failure modes

- all-distinct identity words have no depth-zero duplicate pair;
- the first safe duplicate may require a growing elimination depth, making a
  prescribed-prefix argument superpolynomial;
- simple positive braids may have a zero row despite positive average
  incidence;
- a repaired two-sided simple-braid law may merely restate an unproved
  spectral-gap problem;
- Monte Carlo may miss a thin marked set and therefore cannot certify a
  positive lower bound.

## Deliverables

Produce `checkpoint.md`, auditable scripts and machine-readable results, and
a nine-field `report.md`: exact claim/convention; full argument;
probability/runtime/path/congestion accounting; dependencies; first unproved
step; strongest self-attack; boundary/calibration results;
artifacts/reproduction; and one verdict `PROVED`, `REFUTED`, or
`OPEN AT A NAMED STEP`.
