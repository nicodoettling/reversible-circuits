# Plan: Rank-Recursive Identity-Bridge Goal

Status: prepared, not started

## Objective

Determine whether the exact positive `S_(N-1) subset S_N` rank disintegration
can be converted into an exact or negligible-error polynomial-time sampler for
uniform transposition identity bridges, with top-level length `L_N=2N^3`.

## Named obligations

- `R0`: complete transposition support under the dense identity-bridge law
- `R1`: arbitrary-endpoint stable-sort bijection and coefficient identity
- `R2`: positive weighted branch sampler for `(k,h)`
- `R3`: prescribed-endpoint star-factor sampler
- `R4`: polynomial arbitrary-endpoint recursive closure
- `R5`: dense approximation and summable total-variation error
- `R6`: exact red team and paired-lift diagnostics

## Outcome classes

```text
sampler-theorem | strict-reduction | architecture-obstruction | inconclusive
```

## Expected failure modes

- signed character formulas do not yield positive sampling probabilities;
- endpoint orbit compression has superpolynomially many states;
- star-factor formulas cover only transitive or minimal factorizations;
- unconditioned mixing estimates do not survive bridge conditioning;
- finite agreement is mistaken for an asymptotic sampler theorem;
- pair insertion is rejected only by its already-known `h=e` bias;
- workers drift back to the unrelated local heat-bath mixing proof.

## Reproducibility

The coordinator records the start commit/status, exact command, model,
reasoning effort, UTC times, Python version, dependency versions, and seeds in
`run_manifest.md`.  Every computational role stores scripts and
machine-readable results in its role directory.
