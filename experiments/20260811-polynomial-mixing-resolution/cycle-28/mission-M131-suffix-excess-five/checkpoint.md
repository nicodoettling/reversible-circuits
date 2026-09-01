# M131 halfway checkpoint

Date: 2026-08-13 UTC.

## Decisive state

The literal all-`j` recurrence and the first closed `L=5` envelope have been
implemented independently of predecessor source. The exact structure is:

```text
supported ordered compositions: 32
exceptional canonical basins:    31
positive root groups:            16
live deep groups:                11
```

The first inherited envelope, using only `beta_E<=degree(E)`, is **refuted as
a certificate**: at `(s,K)=(7,4096)` its normalized value is about
`1.01949`, while the exact resolvent ratio is about `.40251`. This is not a
counterexample to `H<=q(1-q)`.

## New structural sharpening

For a canonical endpoint of degree `k` and first total `A`, write
`lambda(A,k)=beta(A,k)/k`. Exact telescoping gives

```text
lambda(A,2)=A/(A+1),
lambda(A,k)<=2A/[k(A+1)]  for k>=2.
```

More importantly, the script evaluates the exact all-basin coefficient

```text
C_s=sum_(all canonical endpoints e) rho(B_e)^2/[degree(e)rho(e)]
   =sum_e degree(e)rho(e)lambda(e)^2.
```

Inactive endpoints are included as harmless nonnegative upper-bound terms;
the closed endpoint-degree marginal is for this all-endpoint convention.

Using `C_s` and subtracting the exact supported exceptional occurrences
turns the root reset estimate into a much sharper closed envelope. All tested
rows through `s=12`, `K in {1,2,5,64,4096}` pass; the largest envelope ratio
is about `.99862`, and the largest exact-resolvent ratio about `.67196`.
The new arbitrary-deficit `L=3` recursion also passes literal checks, while
the same generic implementation reproduces the accepted `L=1` and `L=2`
formulas exactly.

## Current first unproved step

The finite exact Cayley ranks admit positive one-variable Bernstein
certificates. A tail tensor certificate is positive on

```text
[4/11,187/500]^6 x [0,1/2]
```

after replacing path heights by one, **conditional on `C_s<=3/4`**. This box
contains every six-ratio tuple for `s>=100`. The remaining scalar lemma is:

> For every `s>=100`, the exact canonical-basin coefficient `C_s` above is
> at most `3/4`.

Exact values increase from about `.66829` at `s=30` to `.71454` at `s=100`
and `.72488` at `s=200`, so no counterexample is visible; finite values do
not prove the lemma. If a clean generating-function/coefficient proof is not
found, the final verdict will freeze this strict one-dimensional reduction,
not claim universal `L=5` contraction.

No generic basin-frame/Bessel, raw one-step, or two-layer sign argument is
used. No gap, ROOT-MEAN LIFT, mixing, or project-terminal inference is made.
