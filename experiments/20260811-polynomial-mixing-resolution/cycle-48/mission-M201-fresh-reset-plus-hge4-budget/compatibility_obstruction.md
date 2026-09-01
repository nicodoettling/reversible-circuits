# M201 exact fresh-budget compatibility obstruction

Date: 2026-08-13 UTC.

## 1. Scope and verdict

This note treats only a fresh right-heavy parent
`xi=(B+L,2,1,B)` in the normalized full unweighted reset excursion `F=H/q`
of the auxiliary nonlazy minimal-long-cycle parking projection. The project
target remains uniform fixed-length identity transposition words, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right.

The outcome is a **strict exact route obstruction**:

> Reserving the accepted actual-history `h=1,2,3` sector upper bounds at the
> same parent and asking reset plus `h>=4` to fit in the residual budget is
> false already at `(B,L)=(2,4)`.

This is not a counterexample to the true parent inequality. At the same state,
the complete exact actual-history `T_1` remains far below `1-q`. The surviving
lemma must jointly amortize actual unused lower-height slack against reset and
the high-height tail.

No all-state/all-`L`, total AMV, gap, original-chain, mixing, or terminal
statement is made.

## 2. Compatible same-parent reservations

Put

```text
q=q_(B,L)=w_(L+1)w_B/w_(B+L+1),
q0=w_B/w_(B+1).                                    (2.1)
```

For `L>=2`, accepted M173/M177 gives the same-`L` terminal bound

```text
U_1(B,L)=(1-q0)A_1(L-1),

A_1(n)=sum_(r=1)^n eta^(1)_(n,r)R_(r+1),
eta^(1)_(n,r)=c(n,r)/[(r+1)!w_(n+2)].              (2.2)
```

This retains the exact `q0` and operator coefficient rather than replacing
them by the global quarter bound. The exceptional `L=1` value is
`U_1=(1-q0)/2`, while `U_1=0` at `L=0`.

For height two, accepted M179/M184 gives

```text
U_2(L)=0                                      (L<2),
       =1/4                                   (L=2),
       =(2/3)M_2(L-2)                         (L>=3),

M_2(n)=(n+1)^n(n+2)/(n+3)^(n+1).                  (2.3)
```

The `L=2` row is the separate `n=0,d=1` boundary. For `L>=3`, `2/3` is the
accepted branch Loewner factor and `M_2` is the exact exterior first moment,
including `r=n`.

For height three, accepted M193/M197 gives the compatible reservation

```text
U_3(L)=0                                      (L<3),
       =3/8                                   (L=3),
       =(3/4)M_3(L-3)                         (L>=4),

M_3(n)=(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).        (2.4)
```

At `L=3`, the exact matrix/history argument is in fact strictly sharper than
`3/8`; (2.4) uses the accepted simple boundary constant. At `L>=4`, `3/4`
is the full three-mode Loewner factor and `M_3` is the exact exterior first
moment, again including `r=n`.

Thus the exact residual after these compatible *upper-bound reservations* is

```text
Delta_(B,L)=1-q-U_1(B,L)-U_2(L)-U_3(L).            (2.5)
```

This is not obtained by adding the incompatible global constants
`(1-q0)/4,1/4,3/8`. Each exterior is evaluated at the same `L`, and the
height-one `q0` factor is retained.

## 3. Minimal high-tail state

An `h>=4` descendant first exists at `L=4`. Choose `B=2`. Direct Cayley
calculation gives

```text
q=q_(2,4)=3750/16807=26250/117649,
q0=2/3.                                             (3.1)
```

The exact accepted coefficients at this same parent are

```text
A_1(3)=3299/18750,
U_1(2,4)=3299/56250,
U_2(4)=(2/3)M_2(2)=24/125,
U_3(4)=(3/4)M_3(1)=27/125.                         (3.2)
```

Therefore

```text
Delta_(2,4)=293289307/945393750
            ~=0.3102297926128663.                  (3.3)
```

Every multiplicity in (3.2) is the accepted exact exterior normalization;
there is no added observation or survival factor.

## 4. Exact actual-history reset and branch decomposition

The clean-room checker reconstructs the finite history Hilbert feature from
canonical reset currents and every retained descendant block. For a branch
of degree `d`, it uses

```text
sqrt(eta/pi_a)L_a Phi_child,
pi_a=E L_a,
a=0,...,d-1,                                        (4.1)
```

and omits killed `a=d` before the orthogonal direct sum. Parent `T_1` is then
computed exactly from the full Gram kernel as

```text
T_1=E||Phi||^2-||E[(U-1/2)Phi]||^2/(1/12).         (4.2)
```

Thus every Hilbert/Jacobi mode, likelihood-weighted cross term, and covariance
subtraction is retained. No scalar-child, diagonal, Jensen, or finite-summary
replacement occurs.

At `(B,L)=(2,4)`, exact decomposition by the last-root height is

```text
T1_reset =6628367198857337/21450464220937500,
T1_h1    =0,
T1_h2    =22259/1575000,
T1_h3    =6974311/300000000,
T1_h4    =1735419680239/29524500000000.            (4.3)
```

In particular,

```text
T1_reset+T1_h4-Delta_(2,4)
 =480024264873449410111/8339940489100500000000
 ~=0.05755727699745519>0.                           (4.4)
```

Equation (4.4) is the promised exact obstruction. There is no nonzero
`h>4` sector at `L=4`, so it also refutes the weaker request that reset plus
the whole `h>=4` tail fit below (2.5).

## 5. Why this is not a contraction counterexample

Summing all actual terms in (4.3) gives

```text
T_1(6,2,1,2)
 =422384074903914714287/1042492561137562500000
 ~=0.4051674713563533.                              (5.1)
```

The true parent budget is

```text
1-q=13057/16807~=0.7768786815017552,               (5.2)
```

and its exact unused slack is

```text
(1-q)-T_1
 =387506171468022785713/1042492561137562500000
 ~=0.3717112101454019>0.                            (5.3)
```

The failure in (4.4) is caused by loose lower-sector reservations, not by the
actual history. For example, actual `h=1` vanishes and actual `h=2,h=3` are
far below their accepted upper bounds. Their unused slack more than pays for
the reset and `h=4` branch.

## 6. Surviving standalone lemma

Let `T_h(B,L)` denote the exact actual-history height-`h` charge and let
`U_h(B,L)` be (2.2)--(2.4). The first remaining positive statement is:

> **Joint all-height actual-history slack/amortization lemma.** For every
> fresh right-heavy parent, prove directly from the vector history that
>
> ```text
> T_reset+sum_(h>=4)T_h-Delta_(B,L)
> <=sum_(h=1)^3 [U_h(B,L)-T_h(B,L)].                (6.1)
> ```
>
> Equivalently, prove the full fresh-parent inequality after coupling unused
> lower-height slack with reset and the high tail, without bounding either
> side independently.

Every bracket on the right is nonnegative by the accepted sector theorems.
M201 proves that their joint use is necessary: the left side of (6.1) can be
strictly positive. A successful proof must preserve the observation-dependent
Hilbert/Jacobi history and killed atoms across all heights.

This is a strict reduction. It neither proves nor refutes (6.1).

## 7. Reproducibility and dependencies

Run from this directory:

```text
python3 -B exact_obstruction.py --output exact_results.json
```

The script uses standard-library `Fraction`, `seed=null`, imports no
predecessor, and evaluates only the named minimal state `B=2,L=4`. It
constructs compositions and history blocks from definitions; it does not
enumerate a range of `L`.

Accepted immutable inputs are M173/M177, M179/M184, and M193/M197. Their
complete ledgers passed before use.
