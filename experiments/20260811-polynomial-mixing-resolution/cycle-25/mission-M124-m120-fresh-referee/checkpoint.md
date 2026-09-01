# M124 halfway checkpoint: universal algebra survives fresh audit

Date: 2026-08-12 UTC.

## Scope and integrity

The five assigned M120 SHA-256 digests match exactly.  The target under audit
is the auxiliary reversible chain `A_d` on realizable connected-unicyclic
keys, with

```text
rho(kappa)=|C_kappa|/Z_inc,
Q_A(kappa,lambda)=|C_kappa intersect C_lambda|/(2Z_inc),
```

and unused row mass held.  This is not the uniform law on identity words.
The direction coin `1/2` is retained throughout.

## Independent algebra

For a nonidentity key, let `A` be a cycle of length `a>=2`, take
`t=(x,p^{-1}(x))`, and let the right block containing `A` have `b` labels
and `s` cycle-atoms.  Moving the cut right and splitting off `{x}` gives,
from the independent one-side counts,

```text
A_d(kappa,lambda)
 = 1/[2(2d-j)] * ((a-1)/a)^a * ((b-1)/b)^(s-3).
```

The factorial, atom, and block factors agree exactly with M120.  Since
`2d-j<=2d`, `((a-1)/a)^a>=1/4`, and the block factor is at least `1/4`,
this single edge has probability at least `1/(64d)`.

At `p=id`, the connected unicycle on `d>=3` vertices has an incidence vertex
with two label-edges going to distinct opposite vertices; otherwise its
underlying simple connected graph has maximum degree one and at most two
vertices.  Joining the corresponding singleton cycles is a valid reverse
edge.  If the common block has `b` labels, its exact rate is

```text
2/(j b)  or  2/((2d-j)b),
```

hence at least `1/d^2`.  Thus M120's aggregate
`1/(64d^2)` conclusion for all states and `d>=3` follows.

For `R=d-c(p)`, every adjacent edge changes `R` by exactly one.  The preceding
split proves the statewise downward rate `>=1/(64d)`.  When `R<=d-3`, the
incidence graph has at least three vertices and supplies a join of atoms of
lengths `a,b` with common block size `B` and relevant side length `k`.  Its
exact rate is

```text
h(a+b)/[2kB h(a)h(b)].
```

Writing `n=a+b`, direct factorial cancellation gives

```text
h(n)/(h(a)h(b))
 = [n/(ab)]/[binom(n,a)(a/n)^a(b/n)^b]
 >= n/(ab) >= 4/n >= 4/d.
```

The bracketed denominator is exactly a binomial point probability.  With
`k<=2d` and `B<=d`, the upward rate is at least `1/d^3`.  All levels
`0,...,d-2` are realizable by the one-left-block construction stated by M120.

## Boundary and finite falsification status

The fresh checker imports no mission code and reconstructs keys and flows
directly.  Through `d=5` it finds key/edge counts
`(1,0),(9,12),(101,324),(1420,7520)`, one component in every case, all defect
levels, and zero formula, existence, row, defect-direction, detailed-balance,
or bound failures.  At `d=2` there is one key, no off-diagonal edge, and only
defect level zero, so the theorem's explicit exception is necessary.

## Gap self-attack

An exact rational realization with `delta=1/8` confirms M120's reversible
valley example: every nonzero directional rate is at least `delta`, while
the stationary masses fall by `2delta=1/4` per edge to the middle and the
middle-cut conductance is `Theta((2delta)^L)`.  Therefore directional rate
floors alone do not prove a gap.

Current referee posture: **ACCEPT**, subject only to final report and freeze.
No material objection has appeared.  M120 consistently leaves the no-valley
lemma, fixed-defect two-step gaps, `gap(A_d)`, `beta(d)`, and the original
heat-bath mixing question unresolved.
