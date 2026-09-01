# M35 plan: general parking-multiset flow

## Exact target

Let

```text
J_r={m in N^r: sum_i m_i=r and sum_(i=0)^k m_i>=k+1 for 0<=k<r}.
```

The stationary parking-macro mass is proportional to
`1/product_i m_i!`.  Compare the inherited gap-`1/r` polarized
`M`-convex down-up chain, whose positive unit-exchange rates are at least
`1/r^2`, to the stationary-flow projection of the nonlazy adjacent
raw-pair same-product heat bath on reduced long-cycle factorizations.

Prove a polynomial path length and congestion bound for every feasible unit
exchange, or isolate an exact weighted-linear-extension obstruction.  A
direct rare edge is not an obstruction if it has polynomial aggregate
bypass flow.

## Lanes

1. Independently audit the `M`-convex exchange argument and the exact
   polarized down-up projection/rates.
2. Separate the easy comparison from arbitrary unit exchange to adjacent
   unit transfers on `J_r`, retaining the factorial stationary ratios.
3. Express each macro as the preorder outdegree sequence of a rooted plane
   tree and each actual macro-changing heat-bath edge as a triangle flip
   between Goulden--Yong-compatible consecutive factor edges.
4. Audit Anand--Feng--Freifeld--Guo--Jerrum--Wang, SoCG 2025, Lemmas
   15--18 (full-version numbering), especially whether their shift path
   flips can be refined to triangle flips with compatible edge orders.
5. If literal lifting fails, prove the smallest exact failure and seek a
   fractional aggregate route.  Count linear extensions rather than using
   the nonuniform raw-tree marginal as though it were uniform.

## Named falsifiers

- A flip in the SoCG path for which every triangle refinement forces a
  non-cover pair in the Goulden--Yong incident-edge poset refutes literal
  liftability of that path.
- A family where compatible source linear extensions have exponentially
  small fraction, with no polynomial detour, refutes a canonical
  tree-path comparison but not the projected gap.
- Exact finite enumeration may falsify a universal rate or recovery claim;
  it cannot prove asymptotic flow without a completeness argument.

## Deliverables

Write a halfway checkpoint and a nine-field final report in this directory.
Use convention `(pq)(x)=p(q(x))` and left-to-right tuple products.  Keep
full scan, fiber, stationary-mass, path-length, and congestion factors.
