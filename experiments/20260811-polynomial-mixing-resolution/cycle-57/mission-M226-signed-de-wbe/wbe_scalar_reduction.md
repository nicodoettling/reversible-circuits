# M226 exact scalar reduction of WBE

Date: 2026-08-13 UTC.

Status: the coefficient identities and reduction below are **proved**. The
two named scalar moment lemmas, hence WBE and DE, remain **unresolved**.

## 1. Immutable interface

Use M217/M222 with odd `k>=3`, `D=2k-1`, `R=2k-3`,
`j=(k-1)/2`, and

    b_r=e^(-r)r^(r-1)/r!,
    K_R(r,d)=b_d b_(r-d)/(R b_r),
    h(r)=(r-1)(r-2)/(rR),
    q_s=[k/(k-1)]b_s b_(k-s)/b_k,  1<=s<=j.

The exact target is

    |S_Z+K_Z|<=C sqrt(ell)/k,       Z=X_ell,Y_ell.    (WBE)

All terms below are raw disjoint numerators with the `q_s` weight. No
conditional normalizer or pointwise absolute profile difference is inserted.

## 2. Coefficient-level cancellation for Y

For `x>=1`, define the complete q-averaged B coefficient multiplying the
two-seam incidence `F_ell(x)`:

    G_k(x)=1{x<=j}q_x h(D-x)
      +sum_(s=x+1)^j q_s(s-x-1)K_R(s,x)
      +sum_(s=1)^j q_s(D-s-x-1)K_R(D-s,x).          (2.1)

The first term is a surviving face; the next two are fragmentation terms.
Thus (2.1) combines them before any estimate.

Let `B^Y_{k,y}` and `A^Y_{k,y}` be the coefficients of
`1{2<=y<=ell}` in the full q-averaged B and A raw one-run numerators.
The exact two-seam law gives, for `2<=y<k`,

    B^Y_{k,y}=((D-2y)/D)G_k(y)+((y-1)/D)G_k(y-1),   (2.2)

and at and above the seam,

    B^Y_{k,k}=((k-1)/D)G_k(k-1),

    B^Y_{k,y}=((2k-y)/D)G_k(y-1)
              +((y-k)/D)G_k(y-k),                  (2.3)

for `k<y<=(3k-1)/2`.

On the A side, surviving marked/untouched faces and every fragmentation
source combine exactly to

    A^Y_{k,y}=
      [2 b_y b_(k-y)/(R b_k)]
      [(k-y)+(k-y-1)(k-y-2)/(k-1)]                 (2.4)

for `2<=y<k`, and `A^Y_{k,y}=0` for `y>=k`.

### Proof of (2.1)--(2.4)

In M217 (3.2), a term `F_ell(x)` occurs in `h(D-s)F_ell(s)` when
`s=x`, in `W_s(F_ell)` when `s>x+1`, and in every
`W_(D-s)(F_ell)`. Collecting their exact coefficients gives (2.1).
Substituting the three atoms of M199's seam laws gives (2.2)--(2.3).

For (2.4), the coefficient of `J_ell(y)` in the A numerator has four
sources: the marked surviving term at `s=y`, the untouched surviving term
at `s=y`, marked fragmentation with `s>y`, and untouched fragmentation.
Use

    q_y=k b_y b_(k-y)/[(k-1)b_k],

the convolution identity

    sum_(r=1)^(m-1)b_r b_(m-r)=2(m-1)b_m/m,

and direct cancellation of `K_R` denominators. Their sum simplifies to
(2.4). This is an algebraic equality, not an asymptotic approximation.

Consequently, with

    c^Y_{k,y}=B^Y_{k,y}-A^Y_{k,y},                  (2.5)

the exact WBE quantity for `Y` is the scalar prefix

    S_Y+K_Y=sum_(y=2)^ell c^Y_{k,y}.                (2.6)

This is the required cancellation between surviving and fragmentation
coefficients before taking an absolute value.

## 3. Exact X-minus-Y two-run reduction

Let `T^B_{k,y}` and `T^A_{k,y}` be the exact q-averaged raw masses of the
literal complementary two-run face of size `y` in M199's B-X and A-full
tuple laws. They count every same/cross kind, seam, and repeated-size
collision with multiplicity. Since `X_ell-Y_ell` is exactly the number of
two-run faces in the cutoff,

    S_X+K_X-(S_Y+K_Y)
      =sum_(y=2)^ell c^T_{k,y},
    c^T_{k,y}:=T^B_{k,y}-T^A_{k,y}.                 (3.1)

Equation (3.1) is a signed difference. Bounding the two positive laws
separately discards the only available cancellation and is not the stated
remaining lemma.

## 4. First two standalone moment lemmas

> **ONE-RUN COEFFICIENT MOMENT (YCM), unresolved.** Uniformly in odd
> `k>=3` and `2<=ell<=(3k-1)/2`, the explicit coefficients
> (2.1)--(2.5) satisfy
>
>     |sum_(y=2)^ell c^Y_{k,y}|<=C sqrt(ell)/k.      (YCM)

> **SIGNED TWO-RUN COEFFICIENT MOMENT (TCM), unresolved.** On the same
> range, the literal signed coefficients in (3.1) satisfy
>
>     |sum_(y=2)^ell c^T_{k,y}|<=C sqrt(ell)/k.      (TCM)

YCM is a one-dimensional Borel-convolution estimate with no topology left.
TCM is the remaining signed boundary-placement estimate for the unique
two-run face. Equations (2.6) and (3.1), followed by one triangle inequality,
show that YCM+TCM imply WBE for both observables. M217/M222 then show WBE
would imply DE, but neither YCM nor TCM is proved here.

## 5. Small versus macroscopic ell

For `ell` comparable with `k`, M217's accepted macroscopic split-tail lemma
controls the bulk `s` region at the target `k^-1/2` scale. The remaining
small-s region is still encoded exactly by YCM/TCM. For fixed or small
`ell`, the target is `O(sqrt(ell)/k)` and the `O(k^-1/2)` bulk estimate is
too weak; coefficient cancellation in YCM and TCM is indispensable. Thus
the regime split narrows where work is needed but does not prove either
moment lemma.

## 6. Refuted shortcut

A proposed unsigned shortcut was: for a fixed first edge, parent, and
unordered child size `a`, at most `4 min(ell,a)` placements give a two-run
face of size at most `ell`. Exact `k=5` B-side data refute it. With first
split `s=2`, parent size `7`, child size `a=1`, and `ell=7`, there are
exactly five such placements, while `4 min(ell,a)=4`. At `k=7`, the same
ratio reaches eight. Hence TCM cannot be replaced by that placement-count
bound.

## 7. Scope

The coefficient identities are exact and universal. The finite diagnostics
only verify/falsify algebra at small ranks. WBE, DE, DV, conditional J2,
PCR, every downstream gap claim, and both Terminals remain open.

