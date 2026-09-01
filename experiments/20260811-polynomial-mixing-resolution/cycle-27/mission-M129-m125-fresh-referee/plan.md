# M129 plan: fresh referee of M125 defect-mass recurrence

Date: 2026-08-13 UTC.

## Objective and scope

Independently audit the frozen M125 claim package without modifying it.  The
target is the auxiliary connected-unicyclic incidence-cell mass

```text
rho(kappa)=|C_kappa|/Z_inc,
M[d,r]=sum_{R(kappa)=r}|C_kappa|,
```

not the uniform identity-word bridge law.  The audit covers only:

1. the rooted one-colour set-partition recurrence;
2. the connected two-colour extraction and the `L+R=c` unicyclic diagonal;
3. the cycle-type formula, including the cut factorials and `c=1` exclusion;
4. exact multiset aggregation with equal cycle lengths;
5. direct partition checks and the primitive `d=4` ULC counterexample;
6. the exact finite scope of ordinary log-concavity and unimodality through
   `d=22`.

No continuation proof attack on universal log-concavity or DEFECT NO-VALLEY is
authorized.

## Frozen source

Immutable directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/
```

The coordinator supplied SHA-256 hashes for the report, proof, checker, raw
JSON files, manifest, and checksum file.  This referee first checks those
hashes and then treats the payload as immutable.

## Independent method

- Derive the recurrences on paper from a root-block decomposition and a
  join-component decomposition.
- Write a fresh checker in this directory.  It will not import M125 code.
- Directly enumerate pairs of set partitions for all integer-partition cycle
  types through `d=6`, compare with an independent subset recurrence, and
  compare an independently coded multiset recurrence.
- Independently compute exact defect rows through `d=22`, checking integrality,
  boundary support, unimodality, ordinary log-concavity, ULC, and the reported
  closest log-concavity ratio.
- Compare fresh rows and diagnostics with M125's frozen JSON only after the
  independent values have been produced.

## Parameters and reproducibility

- Python 3 standard library only; exact `fractions.Fraction` arithmetic.
- Deterministic exhaustive calculations; `seed=null`.
- Repository commit and Python version are recorded in the final report.

## Expected failure modes

- accidental double-counting of indexed equal-size cycles;
- omission of the root-subset binomial multiplicity;
- confusing connectedness of the incidence graph with connectedness of each
  colour partition;
- admitting impossible `c=1` keys;
- swapping `L` and `R` in the two factorials;
- normalizing a row before testing exact log-concavity;
- promoting finite `d<=22` checks to a universal theorem.

## Verdict rule

`ACCEPT` only if the derivations and fresh exact checker reproduce all scoped
claims with zero material objections.  Otherwise issue `REJECT` with numbered
objections.  The final report will explicitly preserve the unresolved status
of universal ordinary log-concavity, DEFECT NO-VALLEY, and every spectral-gap
claim.
