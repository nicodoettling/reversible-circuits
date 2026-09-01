# Mission M184 plan: fresh referee of immutable M179

Date: 2026-08-13 UTC.

## Objective

Perform a clean, independent referee audit of frozen M179's claimed fresh
actual-history `h=2` descendant bound.  Determine whether the complete
retained `h=2` sector at a fresh right-heavy parent is rigorously at most
`1/4`.

## Ownership and immutable gate

- Own only `cycle-43/mission-M184-m179-fresh-referee/`.
- Never edit M179 or any predecessor, coordinator, manuscript, skill,
  package, configuration, commit, or remote state.
- Before drawing any conclusion, verify M179's complete `SHA256SUMS` ledger
  and inventory against its freeze manifest.
- Read the required project source lock and accepted dependencies after
  initialization; report any disagreement rather than choosing silently.

## Independent audit obligations

1. Rederive the suffix-one feature-degree collapse `Z=0`.
2. Rederive the exact retained-branch `2x2` quadratic form, including Bayes'
   normalization, the covariance subtraction and cross term, and exact
   omission of killed `a=d`.
3. Check the `1/2` degree-one factor and the uniform `2/3` Loewner proof,
   including the determinant polynomial and endpoint positivity.
4. Reconstruct the actual-history-only suffix-one trace envelope and verify
   `S<=3/4` for `d=1`, `S<=1` for `d>=2`, and `B=1` inactivity.
5. Independently cancel `eta=m_group q_child/q_parent`, including `n=0` and
   `r=n`, and check that aggregation gives `h=2<=1/4`.

## Method and prohibitions

- Use a clean-room standard-library `Fraction` checker with no M179 imports.
- Limit exact checks to named decisive boundary/interior rows; no broad scan,
  `L=7`, `h>=3`, or reset aggregation.
- Do not infer a total AMV inequality, all-suffix theorem, gap, original-chain
  result, polynomial mixing, Terminal A, or Terminal B.
- Record numbered material/nonmaterial objections and an explicit
  `ACCEPT`/`REJECT` verdict.

## Deliverables

- This plan and a substantive halfway `checkpoint.md`.
- An independent proof audit and compact exact checker/output.
- A nine-field final report, freeze manifest, SHA-256 ledger, hygiene record,
  and immutable handoff.

