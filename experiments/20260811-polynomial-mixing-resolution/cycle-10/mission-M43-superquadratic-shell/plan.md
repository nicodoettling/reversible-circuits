# M43 plan: entropy-matched superquadratic shell action

## Objective

Use `(pq)(x)=p(q(x))`, ordered words, `m=4N^3+4`, and the literal lazy
`r in {3,4,5}` exact same-product heat-bath chain.  For the graph
neighbourhoods `V^(a)` of the disconnected macro, either:

1. prove `pi(V^(a))<=1/2` and inverse-polynomial full-`K` conductance at
   `a=floor(N^(2+delta))` for some fixed `delta>0`; or
2. prove an explicit shell sequence has superpolynomially small conductance,
   with exact mass orientation and every `H_3,H_4,H_5` contribution.

The primary target is `delta=1/4` and
`a_N=floor(N^(9/4)/100)`.  A theorem uniform for every `a<=a_N` is
preferred.

## Exact obstruction inherited from M42

M42 already proves the required alternative-cut exclusion, global
orientation, and genuine `H_5` boundary surgery through
`a=N^2 log log N/100`.  Those mechanisms remain effective for
`a=o(m)`.  Its only superpolynomial source/outer loss at
`a=N^(2+delta)` is the primitive-excursion ratio

```text
(M/(M-1))^(4a)=exp(Theta(a/N^2)).
```

This comes from forbidding intermediate returns of the prefix action to
`Stab(z)`.  Failure of that source family alone is not a conductance upper
bound.

## Work programme

1. Define the canonical first-return decomposition of every isolate-active
   word and derive the exact minimum connected-window-hull cost, including
   gaps and endpoint-product constraints.
2. Test the proposed segmentation identity against bounded binary crossing
   patterns.  A finite witness may refute the universal identity but cannot
   prove the shell theorem.
3. Replace primitive blocks by endpoint-conditioned crossing blocks allowing
   intermediate returns.  Compare their exact count with the cumulative
   outer encoding using hard-rod placement counts, not a per-position union
   bound.
4. Preserve the M42 robust-core exclusion for all other cuts and the exact
   final `H_5` surgery.  Recheck that no endpoint-dependent loss is hidden.
5. If the segmentation identity fails, isolate the weakest exact boundary
   layer statement sufficient for a polynomial source/shell ratio and try a
   renewal-reward or randomized-source proof.
6. Audit primary renewal, polymer, Markov-renewal, and one-dimensional
   hard-core sources against that exact statement.  State every normalization
   and hypothesis mismatch.
7. Freeze a halfway checkpoint and a final report with the required nine
   fields, including full `Q_3+Q_4+Q_5` accounting and exceptional-case
   calibration.

## Falsifiable universal claims

- **SEGMENTATION-COST:** the minimum number of length-at-most-five
  product-preserving window changes needed to eliminate isolate crossings is
  the minimum over partitions of canonical excursions into consecutive
  groups of the sum of their connected-hull costs.
- **RETURN-PUSH:** moving the last crossing four positions right raises that
  minimum by exactly one for the selected boundary sources.
- **ENTROPY-MATCHED LAYER:** at radius `a<=N^(9/4)/100`, a polynomial fraction
  of the exact isolate outer volume lies in an explicitly pushable boundary
  layer satisfying the alternative-cut prefix certificate.

## Expected failure modes

- intermediate prefix returns permit two distant nominal excursions to be
  removed more cheaply by an overlapping-window braid;
- the exact metric depends on transposition labels, not only the binary
  crossing pattern;
- endpoint conditioning destroys a renewal factorization;
- the cumulative shell is entropically concentrated far inside its nominal
  radius;
- an abstract polymer theorem assumes multiplicative activities,
  compatibility, positivity, or insert/delete dynamics absent here.

No finite convergence or failure of a proof route will be promoted to
Terminal B.
