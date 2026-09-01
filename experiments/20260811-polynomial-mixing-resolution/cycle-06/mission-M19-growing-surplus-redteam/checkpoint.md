# Halfway checkpoint: isolated-label phase cut has polynomial full-K escape

## Exact scoped theorem

Fix `N>=3`, even `m>=4`, and a label `v`.  Let

```text
A_v={w in Omega(N,m):v occurs in no transposition factor}.
```

With `M=binom(N,2)` and `M_-=binom(N-1,2)`, the current proof gives

```text
Phi_pm^K(A_v)
 >=1/[3(m-2)(N-2)D_N]
 >=1/(6mN^3),
D_N=(3N^2+N-12)/2.                                    (C.1)
```

This holds at every surplus, including every genuinely growing `g` in the
assigned intermediate window.  It rejects one exact refinement of the
disconnected component phase, not the whole bottom-layer cut and not
Terminal B.

## Exact stationary mass and orientation

Write `Z_(d,k)=|Omega(d,k)|`.  Avoiding `v` identifies `A_v` bijectively with
`Omega(N-1,m)`, so

```text
pi(A_v)=Z_(N-1,m)/Z_(N,m).                             (C.2)
```

The oriented smaller side is `A_v` if `2Z_(N-1,m)<=Z_(N,m)` and its
complement otherwise.  The common boundary flow is divided by

```text
min{pi(A_v),1-pi(A_v)}
=min{Z_(N-1,m),Z_(N,m)-Z_(N-1,m)}/Z_(N,m).
```

No component-count unimodality or asymptotic mass guess is used.

## Adjacent-square incidence

Conditional on `A_v`, the word is uniform on `Omega(d,m)` for `d=N-1`.
Let `S(w)` be its number of adjacent equal pairs.  Deleting a marked pair is
a bijection with a length-`m-2` identity word, one of `M_-` transpositions,
and one of `m-1` insertion gaps.  Hence

```text
E[S]=(m-1)M_- Z_(d,m-2)/Z_(d,m),
Pr[S>=1]>=M_- Z_(d,m-2)/Z_(d,m).                       (C.3)
```

If `p_d(k)` is the return probability of the uniform-transposition walk,
then `Z_(d,k)=M_-^k p_d(k)`.  For even `m`,

```text
p_d(m)=(1/d!) sum_(lambda partition d)(f^lambda)^2
        r_lambda^m,
```

where every real character ratio satisfies `|r_lambda|<=1`.  Therefore
`p_d(m-2)>=p_d(m)`, and (C.3) is at least `1/M_-`.

## Exact original-K exit and all block sizes

Choose the first square.  Pad it on the available side to an `H_3` window and
replace `(e,e,a)` by `(f,f,a)`, or `(a,e,e)` by `(a,f,f)`, where `f` contains
`v`.  This preserves the ordered block product and exits `A_v`; all `N-1`
choices of `f` containing `v` are distinct exit outcomes.

The full lazy kernel decomposes its boundary flow into `r=3,4,5` terms.
Laziness contributes zero, the `r=4,5` terms are nonnegative, and the
summed `r=3` exit probability has the lower bound

```text
(N-1)/[2*3*(m-2)D_N].                                 (C.4)
```

Here the factors are laziness/block-size normalization, window scan, and the
exact transposition-product triple-fiber size

```text
D_N=M+3[2(N-2)]+2 binom(N-2,2)=(3N^2+N-12)/2.
```

Multiplying (C.3)--(C.4), using
`M_-=(N-1)(N-2)/2`, proves (C.1); dividing by the exact oriented smaller mass
can only increase the conditional escape bound.  Finally `D_N<=2N^2` gives
the displayed `1/(6mN^3)` simplification.

## Calibration and remaining red-team step

The exact masses are `1/27` at `(N,m)=(3,4)`, `27/120=9/40` at `(4,4)`,
and `243/3936=81/1312` at `(4,6)`.  At `m=4`, `|R_m|=2`, so the use of
`|R_m|<=3` is conservative and the whole-word `H_4` remains present.

The first unresolved phase proposition is still the growing-`g` connected
bottom-layer cut `F_(N,g)` or a nonnormal cut inside it.  Pendant-leaf density
cannot be assumed uniform in genus, and the isolated-label theorem does not
control unions or correlations of many missing labels.
