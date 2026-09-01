# M49 plan: full actual parking flow

Date: 2026-08-11.  Convention: permutations compose as
`(pq)(x)=p(q(x))`; minimal long-cycle factor tuples multiply left-to-right.

## Exact target

Let `A_r^ideal` be the adjacent-value restriction of the accepted
Lorentzian down-up parking chain and `bar P_r` the full nonlazy uniform scan
of adjacent exact rank-two heat baths.  Prove a fractional comparison

```text
E_(A_r^ideal) <= r^C E_(bar P_r)
```

for a universal `C`, with polynomial path length, total stationary-flow
congestion, and recoverable metadata.  Alternatively, refute one named
aggregate-buffer template and state the smallest surviving proposition.

## Frozen inputs and corrections

- `gap(A_r^ideal)>=r^-7`.
- Actual aggregate departure from a duplicated label `h` is exactly
  `2m_h(m_h-1)/[3r(r-1)]`.
- The leaf-rotation subchain is superpolynomially slow and cannot be the
  comparison target.
- The full projection bypasses the leaf-rotation maximum-degree cut at
  inverse-polynomial flow.
- Balanced binary and `0^a12^b` families refute direct and two-hop
  deterministic comparisons; randomized high buffers remain necessary.

## First approach

Derive an exact marked-outcome description of the full projected edge flow
in terms of duplicated source labels and destination labels.  Seek a
randomized duplicate-buffer routing of each adjacent ideal commodity whose
random buffer subset is recoverable from an actual used edge plus polynomial
metadata.  Track aggregate rather than per-destination probabilities.

Any exact computation is a bounded falsifier only and will be recorded with
deterministic commands and machine-readable output.
