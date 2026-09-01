# M300 plan: all-middle channel-one pairing

## Objective

Independently reconstruct the exact channel-one disintegration

```text
eta_1(F_l) = sum_f nu_M(f) sum_e gamma(e) F_l(e f),
```

with the designated-beta shorthand and collision cases separated, then either
prove an all-rank cancellation theorem implying `GOCI_1` or freeze the first
exact coefficient reduction/obstruction to one named all-middle pairing
candidate.

## Scope and target

- Target law: the coefficient law inherited from M274/M277, M280/M283,
  M285/M287, and M295/M298; this mission does not alter the Markov kernel.
- Primary target: `GOCI_1`, channel one only.  Channel two is in scope only if
  the same exact argument applies without a new hypothesis.
- Prohibited shortcuts: fixed-middle positivity, signed-PSD dominance, `MON`,
  `FOSD`, raw atomwise positivity, and any unproved promotion to OCI/CP/OS+,
  MS/FCL1, a gap, mixing, or Terminal status.

## Method

1. Audit the frozen claims and exact scripts of M274/277, M280/283,
   M285/287, and M295/298.
2. Write a convention-safe disintegration distinguishing a designated beta
   endpoint from the summed collision multiplicities in `gamma`.
3. Before computation, name and freeze one all-middle Abel/reflection pairing
   candidate, with its exact coefficient inequality.
4. Test at most one compact rank, avoiding `k=5` unless a formula identity
   strictly requires it.
5. If the candidate fails, preserve a rational counterexample and isolate the
   first corrected all-middle coefficient statement.  If it survives, attempt
   an all-rank proof and state the first unresolved lemma exactly.
6. Produce dependency audit, halfway checkpoint, proof/obstruction report,
   reproducible exact artifacts if used, freeze manifest, and hashes.

## Expected failure modes

- Confusing `beta=(1,k+1)` as a designated summand with the multiplicity-two
  collision coefficient at the same resulting edge.
- Illegally conditioning on one middle chord after the signed mass over all
  middle chords is required for cancellation.
- Treating compact-rank positivity as an all-rank theorem.
- Reusing the already-refuted fixed-middle or signed-PSD routes under a new
  name.

## Verdict vocabulary

`proved`, `conditional`, `refuted`, or `unresolved`, with every dependency and
exception stated locally.
