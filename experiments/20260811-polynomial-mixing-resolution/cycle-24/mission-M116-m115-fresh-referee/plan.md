# M116 plan: fresh referee audit of M115

## Objective and scope

Independently audit the frozen M115 suffix-excess-three theorem for the
auxiliary full nonlazy stationary-flow parking-degree projection in the
minimal-long-cycle sector.  The project target remains uniform on fixed-length
identity words.  Permutations compose as `(pq)(x)=p(q(x))`, with tuple factors
displayed left-to-right.

The only candidate conclusion is the right-heavy auxiliary contraction

```text
H(s,K,K-1,s-3) <= q(1-q),  s>=4, K>=1.
```

No auxiliary gap, ROOT-MEAN LIFT, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing statement, Terminal A, or Terminal B may be inferred.

## Audit gates

1. Verify M115's frozen manifest and record the observed hashes before any
   mathematical comparison.
2. Re-derive the all-`j` recurrence specialization, eight supported ordered
   compositions, seven exceptional canonical basins, exact currents and
   capacities, and ordinary-height subtraction.
3. Check the arbitrary-deficit `L=1` proposition, including its terminal
   dependency and the `H/b` normalization in both parent attachment ranks.
4. Independently enumerate canonical basins and the full finite DAG for the
   smallest decisive contexts, including `(s,K)=(4,1)` and nonfresh children,
   without importing or executing M115 helper code.
5. Reconstruct the finite and five-variable Bernstein coefficients by an
   independent finite-difference/Newton-to-Bernstein transform; verify degree,
   positivity, boundaries, and exact equality only after the fresh run.
6. Issue `ACCEPT` or `REJECT` with numbered material objections, then freeze
   the owned report, exact output, source, and SHA-256 manifest.

## Reproducibility

The independent checker will use exact `fractions.Fraction` arithmetic,
standard-library modules only, and `seed=null`.  Its primary command will be

```text
python3 -B independent_m115_referee.py --output independent_m115_referee.json
```

