# Balanced root mean-lift: exact remaining implication

Date: 2026-08-11.  Write `P_r=Pbar_r` and let `Rroot_r` be the exact
root-composition stationary-flow quotient proved in
`root_composition_projection.md`.  This note proves that one polynomial
mean-lift inequality closes the full parking-projection gap without
multiplying a polynomial loss at every tree depth.

## Standalone proposition still open

For a function `f:J_r->R`, let

```text
F_f(a)=E_pi_r[f | root composition a].
```

> **ROOT-MEAN LIFT.**  There are universal constants `A<infinity` and
> `C<infinity` such that, for every `r>=2` and every `f`,
>
> ```text
> E_(Rroot_r)(F_f,F_f) <= A r^C E_(P_r)(f,f).         (1.1)
> ```

No extra child-variance term is hidden in (1.1).  The one-level target
Radon bound in `root_composition_projection.md` does not prove (1.1): its
error is a conditional variance in the coarse fiber, and paying that error
separately at every level would reproduce the failed multiplicative
recursion.

## Conditional theorem

If ROOT-MEAN LIFT holds, then there are universal `B<infinity` and

```text
D=max{4,C+3}
```

such that

```text
gap(P_r)>=B^(-1) r^(-D)                              (2.1)
```

for every `r>=1`, with the singleton convention at `r=1`.

## Proof of the conditional theorem

The root-composition theorem gives

```text
gap(Rroot_r)^(-1)<=(9e/2)r(r-1)<=(9e/2)r^2.         (2.2)
```

Decompose variance at the root:

```text
Var_pi_r(f)=Var_rho_r(F_f)
            +E_rho_r Var(f | root composition).     (2.3)
```

By (1.1)--(2.2), the first term is at most

```text
A_0 r^(C+2) E_(P_r)(f,f),   A_0=9eA/2.              (2.4)
```

Fix a root composition `a=(a_1,...,a_k)` and put `s_i=a_i-1`.  Its
conditional law is the product `tensor_i pi_(s_i)`.  Product-measure
variance tensorization, followed by the inductive Poincare inequalities in
the child coordinates, gives

```text
Var(f | a)
 <=sum_i E Var_(pi_(s_i))(f | all other children)
 <=B sum_(i:s_i>=2) s_i^D E_(P_(s_i))^(i)(f,f).     (2.5)
```

The exact restriction identity says that the corresponding coordinate form
inside `P_r` has coefficient

```text
q_(r,s)=s(s-1)/[r(r-1)].                             (2.6)
```

Consequently the conditional-variance term in (2.3) is at most

```text
B max_(2<=s<=r-1) {r(r-1)s^(D-1)/(s-1)}
  E_(P_r,internal)(f,f).                             (2.7)
```

For `D>=3`, the expression in braces is increasing in `s`, so its maximum
is attained at `s=r-1`.  For `r>=3`, write

```text
R_D(r)=[(1-1/r)^D]/(1-2/r).
```

Then (2.7) equals at most `B r^D R_D(r)` times the internal form.  Since
`D>=4`,

```text
R_D(r)<=R_3(r)
       =(r-1)^3/[r^2(r-2)]
       <=1-1/(9r).                                   (2.8)
```

The last inequality is equivalent to
`8r^2-25r+9>=0`, which holds for every integer `r>=3`.

Assume inductively that `gap(P_s)^(-1)<=B s^D` for every `s<r`.
Combining (2.3)--(2.8), using `D>=C+3`, gives

```text
Var_pi_r(f)
 <=A_0 r^(D-1) E_(P_r)(f,f)
   +B r^D(1-1/(9r)) E_(P_r,internal)(f,f)
 <=B r^D E_(P_r)(f,f)                               (2.9)
```

provided `B>=9A_0`.  Enlarge `B` once to cover `r=1,2`; the exact `r=2`
two-state rates are `2/3` and `1/3`.  This completes the strong induction
and proves (2.1).

## Relation to the Cayley route

The accepted Cayley basis-exchange projection has law `pi_r` and gap at
least `1/r`.  A polynomial-congestion comparison from that chain to `P_r`
would prove (2.1) directly and is a sufficient alternative to (1.1).
However, `cayley_exchange_geometry.md` shows that a single labelled edge
exchange can require at least `r-4` actual macro moves after child sorting.
Thus a Cayley proof must retain the exchanged labels and control a genuine
linear-or-longer randomized path; it cannot invoke pointwise one-move
domination.
