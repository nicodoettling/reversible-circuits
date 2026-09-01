# M177 Fresh Referee Plan

## Objective

Perform a clean, immutable, independent audit of frozen mission M173, limited to the identities and boundary cases assigned by the coordinator.

## Ownership and scope

- Own only `cycle-41/mission-M177-m173-fresh-referee/`.
- Never edit M173 or coordinator-owned files.
- First verify M173's frozen manifest and hashes.
- Audit the trace normalization; all six AMV vector terms; covariance subtraction and killed observation; the unrestricted Beta(1,2) finite-summary obstruction; the all-degree tail bound and base cases; the exact exterior factorial sum including `r=n`; and the actual-history `h=1` normalization, coefficientwise positivity, maximum domination, all-deficit norm bound, and `L=1`, `B=1` boundaries.
- Do not run L7, broad scans, global AMV work, gap work, or Terminal experiments.

## Method

1. Freeze-check all M173 payload hashes and manifest entries.
2. Read the required project sources and M173 payloads.
3. Independently rederive each assigned algebraic identity, using a compact exact rational/symbolic script only where useful.
4. Record numbered objections and a scoped verdict in a nine-field report.
5. Freeze M177 with a manifest and SHA-256 checksums; verify repository hygiene.

## Expected failure modes

- A normalization silently changes between conditional and joint expectations.
- A covariance term or the killed `a=d` observation is omitted.
- A finite-summary counterexample is asserted only numerically or only for normalized inputs.
- A factorial sum drops the `r=n` endpoint.
- Positivity or maximum domination is used outside its coefficientwise domain.
- Boundary cases use an absent Jacobi mode.

