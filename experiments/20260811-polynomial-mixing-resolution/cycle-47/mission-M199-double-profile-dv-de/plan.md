# M199 Plan — Double-profile DV/DE

## Objective

Resolve exactly M192/M195's two remaining conditional `J=2` profile lemmas:

```text
(DV) sum_(u=1)^(k-2) sqrt(u)
       |Phi_u^D(Z)-Phi_(u+1)^D(Z)| <= C sqrt(l),

(DE) |sum_(s<k/2) q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)]|
       <= C sqrt(l)/k,
```

for `Z=X_l,Y_l`, odd `k>=3`, and `2<=l<=(3k-1)/2`. Derive a literal
deletion/merge coupling for the normalized disjoint ordered-double laws and
an analytic universal bound, or exhibit the first exact counterexample and
state a corrected narrower lemma.

## Target and convention

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k`,
`h=(0,1,...,n-1)`, `A=(0,k,2k)`, and `B=(0,1)(k,2k)`. The target is the
uniform minimal-factorization law of the long cycle under the fixed-cell
nonlazy cyclic rank-two coordinate kernel. This is not the global identity
bridge or the lazy `{3,4,5}` heat-bath chain.

## Immutable-input gate

Before conclusions, verify the complete frozen M192 and M195 manifests and
the accepted predecessor chain used by their interfaces. Never edit those
missions. Treat their exact gamma, triangle, disjoint Abel, endpoint, and
`E_u` results as inputs only after the gate passes.

## Proof route

1. Write the conditioned disjoint double profiles as explicit critical-Borel
   chord sums, retaining same/cross-run kinds, both double colors, unit gaps,
   shared-endpoint deletion, and repeated component-size multiplicities.
2. Construct the exact adjacent-split deletion/merge transfer
   `Phi_u^D -> Phi_(u+1)^D`; identify all boundary correction terms.
3. Bound its weighted prefix response analytically to prove or refute `(DV)`.
4. Construct the exact A-to-B embedding/deletion map under signed `q_hat_s`
   weights and prove or refute `(DE)`.
5. Only if both estimates close, record the conditional `J=2` consequence;
   make no full `PCR`, `SCBR`, or downstream claim before a fresh audit.

## Diagnostics and expected failure modes

Use deterministic exact diagnostics only at odd `k<=9`, as calibration or
counterexample search. Finite signs or ratios cannot certify a universal
bound. Expected failure modes are an unbounded adjacent-split oscillation,
an endpoint/normalization term absent from the proposed transfer, an
`A/B` ambient embedding boundary response of order larger than
`sqrt(l)/k`, or an illicit absolute split of double kinds/collisions.

## Deliverables

Maintain a halfway checkpoint; write a precise proof or obstruction, compact
checker/results, nine-field report, numbered open obligations, hashes and
freeze manifest, then request a fresh immutable audit.
