# Final substantive checkpoint

Initial substantive checkpoint: 2026-09-05 15:15 UTC. Updated at
2026-09-05 15:46 UTC: **role proof work and final verification complete;
coordinator line audit accepted with editorial corrections applied**.

For labeled nontrivial support components `(B,k_B)`, the exact fiber size is
`m! product_B C(|B|,k_B)/k_B!`. A canonical least-label component recursion
therefore uses positive integer weights

```
binom(n-1,v-1) binom(k,ell) C(v,ell) Z(n-v,k-ell),
```

including `C(1,0)=1` for an isolated least label. This removes enumeration of
labeled set partitions and preserves the full global law. Its state count is
polynomial in `N,m` given the connected count table.

The DYZ normalization has now been primary-source checked by the
coordinator. Its recurrence becomes a positive integer recurrence for
`C(v,k)`, computable using two binomial convolutions per degree split in
`O(N^2m^2)` arithmetic operations on `O(m log(N+1))`-bit integers. Every
scalar connected count and the complete global macro law are therefore
polynomial-time computable. This does not supply a word-level sampler.

The M112/M119 input gives an exact polynomial-time sampler on a fixed
connected `v`-set at length `2v-2`: sample a uniform Cayley tree and an
independent uniform permutation of `2v-2` edge labels, apply the DPS closure,
and forget the root. The forgetful map is exactly `v`-to-one. This samples
only a declared conditional fiber when embedded in an all-minimal assembly;
it is not the global target except in trivial boundary cases.

New proved global sparse regime: exact DPS minimal-component sampling has
TV error exactly `1-Z0/Z`, and at even `m<=N` at most
`min(1,m^4/[48(N-m+1)^2])`. The coordinator proposed the incidence bound;
this role's fresh nonauthor audit is in `sparse_bound_audit.md`.

Named-method obstruction: the minimal-only sampler's error tends to one
when `m=Theta(N^alpha)`, `2/3<alpha<=1`. This follows from a weighted
forest upper bound and an embedded-subgroup return-count lower bound.
It is not a computational hardness result.

The precise hybrid uses exact component masses, minimal DPS, a connected
support-marked DP under an explicit polynomial state cap, and short/dense
unrestricted bridge rejection only when the exactly computed connected
acceptance probability is at least `1/2`. Its global error certificate is
`1-Z_allowed/Z+epsilon/2`. The unresolved primitive is connected word
generation at positive surplus; the first project-open family is
`g=1,k=2v` at unbounded `v`.

Exact checks pass on required `S3,m4`, `S4,m4,m6`, boundaries, every
per-word macro/connected-DP probability, and all DPS rooted inputs through
`v=4`. A compact exact mass table is retained through `N=48,m=96`; its
finite shape is not extrapolated to an asymptotic theorem. Final details
and dependencies are in `report.md`.
