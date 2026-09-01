# M106 plan: fresh referee of M103 global two-layer reset

## Objective

Independently audit the frozen M103 claim that the pointwise two-layer reset
certificate fails at the fresh reachable context `x=(30,1,0,10)`, while the
complete weighted and unweighted reset resolvents remain positive there.

## Scope and target

- Global target: the uniform fixed-length law on
  `Omega(N,m)={w in T_N^m: eval(w)=id}`.
- Kernel convention: `(pq)(x)=p(q(x))`; tuple factors are multiplied from
  left to right.  The primary chain is the lazy exact same-product
  `{3,4,5}` block heat-bath kernel in `GOAL_SPEC.md`.
- This mission audits only the contextual reset recursion used in the
  projection proof route.  It does not estimate the heat-bath spectral gap.

## Frozen inputs

Read the frozen reports and relevant artifacts from M90, M96, M98, M99, and
M103.  Before relying on M103, verify the required report and manifest hashes
and every manifest entry.

## Independent checks

1. Reconstruct the contextual state space and all-`j` transition operator
   `Q`, then define `A`, `U`, and `r_U` without importing M103 code.
2. Prove algebraically that `(I+Q)r_U=U-A-QA-Q^2U`.
3. Verify fresh reachability and strict descent of the progress variable.
4. Compute the exact `Fraction` numerator and denominator of the two-layer
   expression at `(30,1,0,10)`, retaining every admissible `j`.
5. Compute the exact full weighted and unweighted resolvents and their
   margins at that witness.
6. Reproduce at least one predecessor calibration/direct grouped check if
   feasible.
7. State the exact logical scope: refutation of a sufficient certificate only;
   no slow mode, gap estimate, or terminal result.

## Deliverables

- `checkpoint.md`
- an independently written exact-arithmetic script and machine-readable output
- a final nine-field `ACCEPT`/`REJECT` report with numbered objections
- `SHA256SUMS`, with no cache files and no edits outside this directory

