# M65 plan: contextual quotient absorption

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; factor tuples
multiply left-to-right.

## Target

For every contextual suffix-cut observable `f=alpha_s phi`, root
conditional mean `h(C)=E[f|C]`, suffix size `B`, and accepted
root-composition quotient `R_s`, prove or refute

```text
||h-Eh||_(-1,R_s)^2
 <= E[f 1_(last root branch size=B)].
```

This is a scoped statement for the minimal long-cycle parking projection,
not the identity bridge chain `K`.

## First tests

1. Compute the exact normalized quotient-generator defect
   `G_0 h(C)=sum_D R_s(C,D)/alpha_s [h(D)-h(C)]` on
   `{C:last(C)>B}`.
2. Classify each bounded contextual example as harmonic,
   superharmonic (`G_0h<=0`), subharmonic, or mixed; test committor
   boundary normalization separately.
3. If literal harmonicity fails, isolate the signed defect by merge/split
   direction and seek a universal comparison that implies either exact
   absorption or `delta+a<=1+O(1/s)`.
4. Address marked-source recovery only after the scalar inequality closes.

Exact calculations through ambient `r<=7` are falsifiers, not proofs.
All universal conclusions require a separate algebraic argument.
