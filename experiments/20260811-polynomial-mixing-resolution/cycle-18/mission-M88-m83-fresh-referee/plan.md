# M88 plan: fresh referee of M83 balanced one-step theorem

Date: 2026-08-12.

## Scope and target

Audit the frozen M83 report and manifest without editing any M83 or shared
artifact.  The background target is the uniform minimal length-`n-1`
transposition bridge to `h=(0 1 ... n-1)`, compressed to rank-two products
and then to simultaneous-`h`-conjugacy orbits.  It is not the identity bridge.

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.

## Claim under review

For `n=3k`, odd `k>=3`, audit the strict `Lambda_n` neighbors

```text
A_k=(0,k,2k),   B_k=(0,1)(k,2k),
```

the cyclic-invariant far-singleton event `F_k`, the identities
`bar K(A_k,F_k)=0` and `bar K(B_k,F_k)>=p_k`, the exact formula for `p_k`,
the conditioned-Borel identity and chord multiplicities, the asymptotic
`p_k~4/(9e sqrt(pi k))`, and the explicit lower bound
`p_k>=2/(27e^2 sqrt(k))`.

## Independent checks

1. Verify the assigned report and manifest digests, then all manifest entries.
2. Reconstruct the residual cycles, strict endpoint-sharing adjacency,
   quotient invariance, and no-overcount interpretation from definitions.
3. Enumerate **all** admissible rank-two targets at `k=3,5`; check exact row
   normalization, the full event zero for `A_k`, the selected `B_k` subset,
   and equality with the closed rational formula.
4. Independently derive the Borel identity, multiplicities, Riemann-sum
   constant, and explicit inequality.
5. Audit scope: the conclusion refutes only uniform `O(1/n)` one-step local
   influence.  It must not claim or refute the open `O(n^-2)` two-step lemma,
   a gap theorem, or Terminal A/B.

## Expected failure modes

- a phase-specific event mistaken for a quotient event;
- target-orbit overcount in the selected cross schema;
- the selected-set certificate failing to establish the full `A`-row zero;
- an endpoint or central-chord multiplicity error;
- an unjustified endpoint-dominated Riemann sum;
- leakage of the one-step obstruction into an unsupported two-step or mixing
  conclusion.

The final report will use nine numbered sections and give an `ACCEPT` or
`REJECT` verdict with numbered material objections, exact hashes,
reproduction metadata, and repository hygiene.
