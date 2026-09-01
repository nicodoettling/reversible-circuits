# M62 plan: macro-closed core-lift red team

## Exact target

Use `(pq)(x)=p(q(x))`, `m=2N-2`, and the exact lazy same-product
`r in {3,4,5}` chain.  For a path join tree, let `Core` delete its two
original leaves, let `A` be one component or a balanced union of components
of the reducible leaf-cell invariant, and analyze

```text
S =F_N^c union A,
S'=F_N^c union (F_N minus A).
```

Prove inverse-polynomial two-sided conductance with exact mass orientation and
kernel normalization, or construct a literal Terminal-B sequence.

## First audit: complement symmetry

Before new routing, audit the direct consequence of M60:

```text
S^c       =F_N minus A subseteq F_N,
(S')^c    =A subseteq F_N,
Phi_pm(B) =Phi_pm(B^c).
```

If valid, M60's arbitrary-`B subseteq F_N` theorem already resolves the whole
assigned family, despite absorbing the macro exits from `A`.  Record this as
an append-only correction to M60's stated next gap, with all exact masses.

## Exact calibration

At N=5 use the eight exact path-core component sizes

```text
1068,1068,997,997,997,997,842,842.
```

Choose both a single component and the exactly balanced path-fiber union
`1068+997+997+842=3904=7808/2`.  Use `|Omega(5,8)|=1,770,940` and
`|F_5|=1,008,000` to state both side masses exactly.  No finite flow is used
as asymptotic proof.

## Failure modes to audit

- Confusing `Q/pi(A)` with two-sided conductance when `A` is the larger side.
- Applying M60 to `S` itself rather than to its minimal-macro complement.
- Omitting H4/H5 normalization; the inherited proof uses one H3 outcome but
  retains all other flow as nonnegative.
- Empty extreme `A`; state nonempty/proper hypotheses explicitly.

