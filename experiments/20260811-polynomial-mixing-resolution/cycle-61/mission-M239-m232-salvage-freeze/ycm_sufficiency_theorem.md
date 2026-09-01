# M239 quantified YCM sufficiency theorem

Date: 2026-08-14 UTC.

Status: **proved from the frozen M226/M229 coefficient identities and the
frozen M241 SG/GG2 lemmas**. M243's frozen fresh audit accepts M241 with no
material objection. No TCM or downstream claim is made.

## 1. Statement and immutable interface

For odd `k>=3`, put

    D=2k-1, R=2k-3, j=(k-1)/2, L=(3k-1)/2,
    b_n=e^(-n)n^(n-1)/n!.

Use exactly M226/M229's coefficients on the corrected domain
`1<=x<=L-1`:

    B_(k,y)=((D-2y)/D)G_k(y)+((y-1)/D)G_k(y-1),  2<=y<k,
    B_(k,k)=((k-1)/D)G_k(k-1),
    B_(k,k+z)=((k-z)/D)G_k(k+z-1)+(z/D)G_k(z),  1<=z<=j,

and, for `m=k-y`,

    A_(k,y)=2b_y b_m/(R b_k)
      [m+(m-1)(m-2)/(k-1)],                       2<=y<k,
    A_(k,y)=0,                                     y>=k,
    c_(k,y)=B_(k,y)-A_(k,y).

Then, uniformly in odd `k>=3` and `2<=ell<=L`,

    |sum_(y=2)^ell c_(k,y)| <= 7000 sqrt(ell)/k.  (YCM)

The proof uses the following frozen M241 estimates, whose checksum inventory
was independently verified by M239:

    |G_k(x)-2b_x| <=128(x+1)b_x/k,  1<=x<=k/4,   (SG)
    G_k(x) <=70/[k sqrt(D-x)],       j<=x<=L-1.   (GG2)

M241 proves these from R1--R3 with the exact GG2 range
`1<=s<=min(j,D-x-2)`. M239 checked the definitions, range endpoints,
positive enlargements, convolution identities, and constants in that proof;
M243 then independently accepted them.

We also use the elementary bounds, proved in M241,

    e^(-1)n^(-3/2)<=b_n< n^(-3/2),
    b_(n-1)/b_n<3,
    b_a/b_n < e(n/a)^(3/2)                         (a,n>=1). (1.1)

The last inequality follows directly by applying the upper Stirling envelope
to the numerator and the lower envelope to the denominator; no ordering of
`a,n` is needed.

## 2. A quantified global bound for `G_k`

> **Lemma GG1.** For odd `k>=3` and `1<=x<=j`,
>
>     G_k(x)<172 b_x.                              (GG1)

### Proof

All three sources in `G_k(x)` are nonnegative. The survivor divided by `b_x`
is

    [k/(k-1)] [b_(k-x)/b_k]
      [(D-x-1)(D-x-2)/((D-x)R)].

Here `k/(k-1)<=3/2`, `k-x>=j+1`, (1.1) gives
`b_(k-x)/b_k<e 2^(3/2)<9`, and the last factor is at most
`D/R<=5/3`. Thus the survivor is `<23b_x`.

For the short-parent sum put `t=s-x` and `m=k-x`. Exact cancellation of
`b_s` gives

    b_x k/[(k-1)R b_k]
      sum_(t=1)^(j-x)(t-1)b_t b_(m-t).

Positivity and the weighted Borel convolution enlarge this to

    b_x [k/(k-1)] [m/R] [b_m/b_k].

Since `m>=j+1`, (1.1) gives `b_m/b_k<9`; also `m/R<=1` and
`k/(k-1)<=3/2`. Hence this source is `<14b_x`.

For the long-parent sum set `M=D-x`. After exact cancellation it is

    b_x [k/((k-1)R b_k)] sum_(s=1)^j
      b_s(M-s-1)b_(M-s) [b_(k-s)/b_(D-s)].

Because `k-s>=j+1`, (1.1) gives

    b_(k-s)/b_(D-s)
      <e[(D-s)/(k-s)]^(3/2)<e 3^(3/2)<18.

Enlarge the positive sum and use
`sum_(s=1)^(M-1)(M-s)b_s b_(M-s)=(M-1)b_M`. Also
the two-sided Stirling envelope directly gives
`b_M/b_k<e(k/M)^(3/2)<3`; also `M/R<=D/R<=5/3` and
`k/(k-1)<=3/2`. The long-parent source is therefore `<135b_x`.
Adding the three bounds proves `23+14+135=172`. All original summation
ranges are contained in the enlarged positive ranges, including `k=3`. ∎

## 3. Four coefficient regions

We prove the following uniform envelope:

    |c_(k,y)| <=3000/[k sqrt(y)],       2<=y<=j,   (E1)
    |c_(k,k-m)| <=176/[k sqrt(m)],      1<=m<=j,   (E2)
    |c_(k,k)| <=70 k^(-3/2),                         (E3)
    |c_(k,k+z)| <=242/[k sqrt(z)],      1<=z<=j.   (E4)

### 3.1 Small coefficients, `2<=y<=k/4`

This range is nonempty only for `k>=9`. Put
`alpha=(D-2y)/D` and `beta=(y-1)/D`. Applying SG at `y` and `y-1`, and
using `b_(y-1)<3b_y`, gives

    |B_(k,y)-2b_y|
      <=128(y+1)b_y/k
        +(y/k)128y(3b_y)/k
        +(4y b_y+2(y-1)b_(y-1))/D
      <=234(y+1)b_y/k.                             (3.1)

For A put `m=k-y`,

    Q=b_m/b_k,
    P=[m+(m-1)(m-2)/(k-1)]/R,
    A_(k,y)/(2b_y)=QP.

M241's ratio estimate gives `1<=Q<=1+16y/k`. Direct expansion gives

    R-[m+(m-1)(m-2)/(k-1)]
      =[3ky-y^2-4y-k+1]/(k-1).

On `2<=y<=k/4`, the numerator is positive and at most `3ky`; since
`k>=9`, this proves `0<=1-P<=4y/k`. Therefore

    |A_(k,y)-2b_y|<=72y b_y/k.                    (3.2)

Indeed the sharper decomposition
`QP-1=P(Q-1)+(P-1)` gives `40`, since `P<=1`; the displayed `72` also
follows without using this sign by `Q<=5`. Equations (3.1)--(3.2),
`b_y<y^(-3/2)`, and
`(y+1)/y<=3/2` yield

    |c_(k,y)|<500/[k sqrt(y)].                    (3.3)

### 3.2 Middle coefficients, `k/4<y<=j`

Both arguments `y,y-1` lie in GG1. Since the two nonnegative B weights are
at most one and `b_(y-1)<3b_y`,

    B_(k,y)<688b_y.

Here `m=k-y>=j+1`, so (1.1) gives `b_m/b_k<9`. The bracket defining A is
at most `2m`, hence its quotient by `R` is at most two. Thus
`A_(k,y)<36b_y`. Because `y>k/4`,

    |c_(k,y)|<724y^(-3/2)<2896/[k sqrt(y)].       (3.4)

Together (3.3)--(3.4) prove (E1), including the small ranks where the first
subrange is empty.

### 3.3 Below, at, and above the seam

For `j<y<k`, put `m=k-y`, so `1<=m<=j`. Both G arguments lie in GG2 and
their `D-x` values are at least `m`. Hence

    B_(k,y)<=140/[k sqrt(m)].

Also `y>=j+1`, so `b_y/b_k<9`; the A bracket is at most `2m`. Therefore

    A_(k,y)<=36m b_m/k<=36/[k sqrt(m)],

which proves (E2).

At `y=k`, GG2 at `x=k-1`, for which `D-x=k`, proves (E3).

Finally let `y=k+z`, `1<=z<=j`. GG2 at `x=k+z-1` and GG1 at `x=z` give

    c_(k,k+z)
      <=70/[k sqrt(k-z)]+172z b_z/D
      <=242/[k sqrt(z)],

because `k-z>=z`, `D>=k`, and `zb_z<=z^(-1/2)`. This proves (E4). Every
G argument used here lies in the corrected interval `1<=x<=L-1`.

## 4. Prefix summation

Use `sum_(r=1)^n r^(-1/2)<=2sqrt(n)`. If `ell<=j`, (E1) gives
`6000sqrt(ell)/k`. If `j<ell<k`, (E1)--(E2) give at most

    (6000+352)sqrt(j)/k <=6352sqrt(ell)/k.

At `ell=k`, (E3) adds at most `70sqrt(ell)/k`. For `ell>k`, (E4) adds at
most `484sqrt(ell-k)/k<=484sqrt(ell)/k`. Thus every allowed prefix is at
most

    (6352+70+484)sqrt(ell)/k
      =6906sqrt(ell)/k
      <7000sqrt(ell)/k.

This proof covers `k=3,5,7` analytically: their small-coefficient subrange
`2<=y<=k/4` is empty, while GG1, GG2, and the other three regions include all
their coefficients. Odd `m`, `m=0`, `m=2`, and `N=2` are Markov-chain
exceptions but are irrelevant to this scalar coefficient theorem.

## 5. Dependency and scope

- **Proved/frozen inputs:** M226/M229 exact coefficient identities and domain;
  M241 R1--R3, SG, and GG2; elementary Borel/Stirling bounds.
- **New proved step:** GG1 with constant 172, four envelopes (E1)--(E4), and
  their prefix assembly, yielding `C_Y=7000`.
- **Independent check of the dependency:** frozen M243 accepts M241 with no
  material objection; its checksum-file digest is
  `99e30270a3852d53ecbdf70222f5a6490b6d12d01a4720e18745e3e30351d59b`.
- **Outside this mission:** TCM is neither used nor re-proved here; its external
  status is left to its own frozen missions. This mission makes no WBE, DE,
  J2, downstream comparison/gap/mixing, or Terminal inference.
