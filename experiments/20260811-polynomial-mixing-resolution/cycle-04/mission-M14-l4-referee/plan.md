# Cycle 04 M14 l=4 referee plan

## Frozen claim

Audit, independently of the author, the theorem in
`cycle-04/mission-M14-l4-resolution/report.md`: with multiplication
`(pq)(x)=p(q(x))`, `M=binom(N,2)`, and

```text
B_4=(H_{1,4}+H_{3,4}+H_{5,4})/3
```

on every nonempty length-eight transposition fiber of an arbitrary feasible
endpoint, both the micro chain and its four-increment `Q_N` projection are
irreducible,

```text
gap(B_4)>=2/(3M^20),
Lambda_N(4;u,v)>=2M^-20,
```

with the stated worst-case total-variation bound.

The later `general_length_addendum.md` is audited separately as the
nonterminal extension

```text
gap(B_l)>=2/[(l-1)M^(4l+4)],
Lambda_N(l;u,v)>=2/M^(4l+4).
```

## Audit obligations

1. Check the Douvropoulos--Lewis hypotheses and use the corrected numbering:
   published Theorem 18 and Proposition 8(4), preprint Theorem 4.2 and
   Proposition 2.7(4).
2. Check the square-tree canonicalization for arbitrary endpoint cycle
   unions, fixed points, minimum length, and square transfers between
   components.
3. Check that every Hurwitz and square move is contained in an aligned
   four-factor heat-bath window, including endpoints.
4. Check the microfactor/product-path quotient in both directions.
5. Recompute the scan probability, conditional-fiber lower bound, spanning
   tree Poincare constant, Hamiltonian normalization, and TV estimate.
6. Rerun the smallest exact finite quotient cases only as falsification
   calibration; finite output is not a proof dependency.

## Expected failure modes

- an endpoint fixed point silently omitted from the component cycle count;
- a bridge square whose removal fails to split after surplus edges are added;
- an unaligned middle or boundary pair;
- failure to connect distinct microfactorizations above one product path;
- loss of a factor of two, three, `V`, or `l-1` in the gap conversion;
- treating the all-length state-count bound as polynomial uniformly in `l`.

## Verdict rule

Return `ACCEPT` only if every universal qualitative statement is proved and
