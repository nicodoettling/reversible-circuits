# M99 halfway checkpoint: M98 counterfamily independently reproduced

Date: 2026-08-12. Scope: the auxiliary full nonlazy stationary-flow
parking-degree projection in the minimal long-cycle sector, not the original
lazy exact same-product `{3,4,5}` heat-bath chain. Permutations compose as
`(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.

## Provisional decision

```text
PROVISIONAL VERDICT: ACCEPT M98 WITH ZERO MATERIAL OBJECTIONS.
```

The assigned report and manifest hashes match, and all eight frozen manifest
entries verify. A fresh standard-library implementation imports no M98 or
predecessor Python module.

## Decisive independent checks

- Literal ordered compositions reproduce the Cayley root grouping through
  rank eight. The full attachment law `j=0,...,k` normalizes exactly in 320
  checks; every live rank `j=1,...,k` is retained in the transformed operator.
- The contextual formula specializes on `R=K-1` to
  ```text
  H(k,B)=k!/product_(i=1)^(k-1)(K+i),
  H(k,t)=q_(t-1,B)[1-k!/product_(i=1)^k(K+i)]  (t>B),
  ```
  and the finite root mean is exactly `q_(s,B)`.
- The basin coefficient is reproduced from literal compositions and from the
  exact beta-integral expansion. Literal endpoint/refinement sums reproduce
  grouped reset energies in six checks; limiting energy coefficients agree
  literally through ranks two to eight.
- With `D(K)=product_(i=1)^16(K+i)`, the script directly constructs
  `P(K)=D(K)^2 r_U(16,K,K-1,4)` coefficient-by-coefficient in `Q[K]`. This is
  not interpolation. Its actual degree is `32`, and its leading coefficient
  is exactly M98's negative limiting defect.
- Exact recurrence and polynomial evaluation both give positive defect at
  `K=709` and negative defect at `K=710`. Every forward difference
  `Delta^dP(710)` for `0<=d<=32` is strictly negative and `Delta^33P=0`,
  reproducing all frozen Newton coefficients. Thus the negative tail for
  every integer `K>=710` is rigorous.
- The witness is reachable from fresh `(K+15,1,0,4)` using the positive root
  composition `(1^(K-2),17)` and attachment rank `K-1`, whose conditional
  probability is exactly `1/K`.
- Independent finite-DAG recursion at `K=710` reproduces the exact weighted
  and unweighted ratios `.4080533675...` and `.5988444278...`, both below
  one. Hence the local sign fails, but neither full resolvent is refuted.

The final report will preserve the narrow scope: the fresh/global two-layer
conditions, universal full resolvents, auxiliary gap, original heat-bath gap,
and both terminal outcomes remain unresolved.
