# M246 clean-room proof audit of immutable M239

Date: 2026-08-14 UTC.

Verdict: **ACCEPT**. Frozen M239 proves the one-run coefficient moment
`(YCM)` with universal constant `7000`. This audit is limited to YCM and
makes no TCM, WBE, DE, DV, J2, comparison, gap, mixing, or Terminal claim.

## 1. Immutable gate and exact dependencies

Every file listed in M239's frozen inventory passed `sha256sum -c` before
substantive use. Its checksum-file digest is exactly

    66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542.

The complete M226, M229, M241, and M243 inventories also pass. Their
checksum-file digests are respectively

    a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a,
    6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688,
    07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936,
    99e30270a3852d53ecbdf70222f5a6490b6d12d01a4720e18745e3e30351d59b.

Thus the exact coefficient interface accepted in M226/M229 and the
`SG=128`, `GG2=70` package proved and freshly accepted in M241/M243 are
immutable inputs. In particular, M229's corrected domain
`1<=x<=L-1` is enforced.

For odd `k>=3`, set

    D=2k-1, R=2k-3, j=(k-1)/2, L=(3k-1)/2,
    b_n=e^(-n)n^(n-1)/n!,
    q_s=[k/(k-1)]b_s b_(k-s)/b_k.

The audit uses the exact normalization `sum_(s=1)^j q_s=1`, the Borel
convolution identities

    sum_(r=1)^(n-1)b_r b_(n-r)=2(n-1)b_n/n,
    sum_(r=1)^(n-1)(n-r)b_r b_(n-r)=(n-1)b_n,

and the elementary bounds

    e^(-1)n^(-3/2)<=b_n<n^(-3/2),
    b_(n-1)/b_n<3,
    b_a/b_n<e(n/a)^(3/2).

## 2. Independent GG1 derivation

For `1<=x<=j`, all three sources in M226's `G_k(x)` are nonnegative.

The survivor divided by `b_x` is

    [k/(k-1)] [b_(k-x)/b_k]
      [(D-x-1)(D-x-2)/((D-x)R)].

Here `k-x>=j+1`, so the Borel-ratio bound gives
`b_(k-x)/b_k<e 2^(3/2)<9`. Also `k/(k-1)<=3/2` and the final factor is
at most `D/R<=5/3`. The survivor is therefore `<23b_x`.

For the short-parent source put `t=s-x` and `m=k-x`. Exact cancellation of
`b_s` against its kernel denominator gives

    b_x k/[(k-1)R b_k]
      sum_(t=1)^(j-x)(t-1)b_t b_(m-t).

The original range is positive and lies inside `1<=t<=m-1`. The exact full
weighted convolution is

    sum_(t=1)^(m-1)(t-1)b_t b_(m-t)
      =[(m-1)(m-2)/m]b_m <=m b_m.

Since `m>=j+1`, `b_m/b_k<9`; moreover `m/R<=1`. This gives the short
source `<14b_x`.

For the long-parent source put `M=D-x`. Exact cancellation gives

    b_x k/[(k-1)R b_k] sum_(s=1)^j
      b_s(M-s-1)b_(M-s)[b_(k-s)/b_(D-s)].

For `s<=j`, `(D-s)/(k-s)<3`, hence the bracket is
`<e 3^(3/2)<18`. Positivity permits enlargement to the full weighted
convolution. Since `b_M/b_k<e(k/M)^(3/2)<3` and
`M/R<=D/R<=5/3`, the long source is strictly below

    18 (3/2) (3) (5/3)b_x=135b_x.

All original ranges are contained in the enlarged nonnegative ranges,
including at `k=3`. Therefore

    G_k(x)<(23+14+135)b_x=172b_x,  1<=x<=j.       (GG1)

This rederivation checks the survivor, short, and long constants and both
exact cancellations without importing M239's checker.

## 3. Small coefficients and the repaired A triangle

The small range `2<=y<=k/4` is nonempty only for odd `k>=9`. Write

    alpha=(D-2y)/D, beta=(y-1)/D.

Substitute `G_k(r)=2b_r+delta_r` in the exact below-seam formula. SG and
`b_(y-1)<3b_y` give three contributions to `|B_(k,y)-2b_y|`:

    128(y+1)b_y/k,
    384y^2 b_y/k^2 <=96y b_y/k,
    [4y b_y+2(y-1)b_(y-1)]/D <=10y b_y/k.

Hence

    |B_(k,y)-2b_y|<=234(y+1)b_y/k.                (3.1)

For the A coefficient put `m=k-y` and

    Q=b_m/b_k,
    P=[m+(m-1)(m-2)/(k-1)]/R.

The exact expansion

    R-[m+(m-1)(m-2)/(k-1)]
      =[3ky-y^2-4y-k+1]/(k-1)

shows `0<=1-P<=4y/k`. M241's indexed ratio estimate gives
`1<=Q<=1+16y/k<=5`. This referee uses the safe triangle

    |QP-1|<=Q|P-1|+|Q-1|
             <=5(4y/k)+16y/k=36y/k.

Since `A/(2b_y)=QP`, it follows that

    |A_(k,y)-2b_y|<=72y b_y/k.                    (3.2)

Thus the proof does not depend on the optional sharper `40` aside in M239.
Combining (3.1)--(3.2), using `(y+1)/y<=3/2` and
`b_y<y^(-3/2)`, in fact gives `423/[k sqrt(y)]`; M239's displayed
`500/[k sqrt(y)]` is safe.

## 4. Middle range and every seam domain

For `k/4<y<=j`, both `y` and `y-1` lie in GG1. The two nonnegative seam
weights are at most one, so `B<172(b_y+b_(y-1))<688b_y`. With
`m=k-y>=j+1`, the ratio `b_m/b_k<9`, and the A bracket divided by `R`
is at most two. Hence `A<36b_y`. Since `y>k/4`,

    |c_(k,y)|<724y^(-3/2)<2896/[k sqrt(y)].

Together with the small range this proves the safe envelope

    |c_(k,y)|<=3000/[k sqrt(y)],  2<=y<=j.        (E1)

For `j<y<k`, put `m=k-y`, so `1<=m<=j`. Both G arguments `y,y-1`
lie in the GG2 range and have `D-x>=m`, yielding
`B<=140/[k sqrt(m)]`. Also `b_y/b_k<9`; the A bracket is at most `2m`,
so `A<=36m b_m/k<=36/[k sqrt(m)]`. Therefore

    |c_(k,k-m)|<=176/[k sqrt(m)],  1<=m<=j.       (E2)

At `y=k`, GG2 is invoked at `x=k-1`, where `D-x=k`, and gives

    |c_(k,k)|<=70k^(-3/2).                         (E3)

For `y=k+z`, `1<=z<=j`, the exact formula invokes GG2 at
`x=k+z-1` and GG1 at `x=z`. Since `k-z>=z`, `D>=k`, and
`zb_z<=z^(-1/2)`,

    c_(k,k+z)
      <=70/[k sqrt(k-z)]+172z b_z/D
      <=242/[k sqrt(z)].                           (E4)

These four cases are disjoint and exhaustive for `2<=y<=L`. Their G
arguments have minimum one and maximum `L-1`, exactly M229's accepted
domain. At the shared endpoint `x=j`, both GG1 and GG2 apply; no seam gap
or overlap is hidden.

## 5. Exact prefix constant and small ranks

Using `sum_(r=1)^n r^(-1/2)<=2sqrt(n)`, E1 contributes at most
`6000sqrt(j)/k` after its range is complete. E2 contributes at most
`352sqrt(j)/k`. Thus before the seam the total is at most
`6352sqrt(ell)/k`. E3 may be enlarged to `70sqrt(ell)/k`, and the E4
prefix contributes at most `484sqrt(ell-k)/k<=484sqrt(ell)/k`.
Consequently

    |sum_(y=2)^ell c_(k,y)|
      <=(6352+70+484)sqrt(ell)/k
      =6906sqrt(ell)/k
      <7000sqrt(ell)/k.

At `k=3,5,7`, the SG/small-coefficient subrange `2<=y<=k/4` is empty.
GG1 covers E1, GG2 covers E2--E4 as above, and all definitions remain in
range. Thus these ranks are part of the analytic proof, not finite
exceptions.

## 6. Independent falsification check

`ycm_boundary_check.py` imports no M239 or predecessor module/data. It
reconstructs `q`, the kernel, the three G sources, B, A, every coefficient,
and every prefix from the closed definitions. Exponential factors cancel in
those formulas, so their values are exact `Fraction` objects. Auxiliary
ratios involving `b_n` use a rigorous rational Taylor enclosure of `e`;
square-root inequalities are checked by exact squaring of nonnegative
rationals.

The deterministic command

    python3 experiments/20260811-polynomial-mixing-resolution/cycle-65/mission-M246-m239-fresh-referee/ycm_boundary_check.py --max-k 101

passes for every odd `3<=k<=101`. It checks exact q normalization, every
corrected G-domain call, the separate GG1 constants, SG/GG2, the safe
small-A constant `72`, E1--E4, the sharper prefix constant `6906`, and
explicit exact coefficient/prefix rows for `k=3,5,7`. This finite result is
only falsification evidence; Sections 2--5 prove the universal statement.

## 7. Numbered objections and verdict

1. **Material objections:** none.
2. **Nonmaterial clarity note:** M239 mentions an optional sharper small-A
   estimate `40`. It is unnecessary. This referee accepts the theorem using
   only the explicitly rederived safe constant `72`; removing that aside
   would make the dependency clearer.
3. **Scope guard:** accepting YCM does not by itself prove or re-audit TCM,
   WBE, DE, DV, J2, any comparison theorem, any spectral gap, mixing, or a
   Terminal.

Final verdict: **ACCEPT YCM WITH UNIVERSAL CONSTANT 7000** on exactly the
stated domain `k>=3` odd and `2<=ell<=(3k-1)/2`.
