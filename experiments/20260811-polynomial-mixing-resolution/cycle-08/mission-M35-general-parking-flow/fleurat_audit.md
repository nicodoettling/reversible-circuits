# Fleurat weighted-growth audit

Date: 2026-08-11.  This audit concerns William Fleurat, *Growing
conditioned BGW trees with log-concave offspring distributions*,
arXiv:2411.03065v3 (2025), especially Theorem 4 and its proof through
Proposition 3.2.

## Exact applicability

Take the simply-generated weight sequence

```text
w_k=1/k!,  k>=0.
```

It has `w_0 w_1>0`, no internal zeros, and is log-concave because

```text
w_k^2/(w_(k-1)w_(k+1))=(k+1)/k>=1,  k>=1.
```

For a plane tree with `r` edges and preorder outdegree vector
`m=(m_0,...,m_r)`, its simply-generated weight is

```text
product_v w_(deg^+(v))=1/product_i m_i!.
```

Thus Fleurat's `SG^w_(r+1)` is exactly the parking-macro law `pi_r`.
Indeed its normalizing constant is `(r+1)^(r-1)/r!`, by the
Stanley--Biane orbit count already used in this mission.

Fleurat Theorem 4 therefore gives Markov kernels `G_r` from `pi_(r-1)`
to `pi_r`, supported on adding one right-leaning (rightmost-child) leaf.
Their time reversals

```text
D_r(t,s)=pi_(r-1)(s) G_r(s,t)/pi_r(t)
```

are deletion kernels supported on removing such a leaf and satisfy the
two exact balance identities

```text
sum_s D_r(t,s)=1,
sum_t pi_r(t)D_r(t,s)=pi_(r-1)(s).
```

This is the weighted analogue of the row/column identities in
Caraceni--Stauffer Proposition 5.1.  In a fractional-flow argument the
weighted column identity can telescope after all source masses are kept
inside the sums; no pointwise lower bound on `D_r` is intrinsically needed
for that particular telescoping step.

## Quantitative limitation

The cited theorem does **not** supply a usable polynomial lower bound on
its positive transition probabilities.  For infinite-support `w`, which
includes `1/k!`, the proof obtains admissibility by finite truncation and
compactness (Lemma 2.4); Proposition 3.2 then defines the tree kernel from
conditional probabilities in recursively selected composition couplings.
Neither statement bounds a positive entry from below, and a limiting
coupling may have arbitrarily small positive entries.

This does not invalidate the aggregate-balance use above, but it prevents
directly declaring a polynomial-time/gap comparison from the theorem.
Moreover the Caraceni--Stauffer construction uses uniform plane-tree
weights and a bounded-preimage pivot map.  In the present law, splitting
off a root child changes the root weight by

```text
w_d/w_(d-1)=1/d,
```

so their unweighted state-count argument is not literal.  A weighted
randomized pivot/load lemma must be proved.  Finally, a delete/replant move
must be routed through the exact leaf rotations of
`leaf_rotation_count.md` with polynomial total stationary-flow congestion;
geometric reachability or an `O(r)` path length alone does not provide that
bound.

## Verdict

**ACCEPT as a qualitative and aggregate-balance input.**  It removes the
existence problem for a balanced deletion kernel under `pi_r`, but it does
not prove ADJACENT-VALUE PARKING FLOW or a polynomial gap for the weighted
leaf-rotation chain.

Primary source: <https://arxiv.org/pdf/2411.03065v3>.

