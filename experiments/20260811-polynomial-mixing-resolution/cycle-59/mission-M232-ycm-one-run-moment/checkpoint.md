# M232 checkpoint

## Start

- Plan and checkpoint initialized before substantive work.
- Target is exactly YCM; all excluded statements remain open.
- M226/M229 are immutable, and `G_k` will be used only on the corrected domain `1<=x<=(3k-3)/2`.
- The complete M226 inventory passed `sha256sum -c`; its checksum-file digest is
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`.
- The complete M229 inventory passed `sha256sum -c`; its checksum-file digest is
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.

## Analytic theorem skeleton (recorded before finite diagnostics)

Put `D=2k-1`, `R=2k-3`, `j=(k-1)/2`, `L=(3k-1)/2`, and

    b_n=e^(-n)n^(n-1)/n!,
    q_s=[k/(k-1)]b_s b_(k-s)/b_k.

The proof route derives the following uniform coefficient envelope from the
closed M226/M229 formulas:

    |c^Y_(k,y)| <= C_*/(k sqrt(y)),          2<=y<=j,
    |c^Y_(k,y)| <= C_*/(k sqrt(k-y)),        j<y<k,
    |c^Y_(k,k)| <= C_* k^(-3/2),
    |c^Y_(k,k+z)| <= C_*/(k sqrt(z)),        1<=z<=j.       (CP)

A deliberately nonoptimized quantified choice targeted below is
`C_*=2^16`, sufficient for all odd `k>=9`; the finite boundary ranks
`k=3,5,7` are handled directly by the trivial raw-observable bound. Summing
(CP) gives YCM with the explicit universal choice `C_Y=2^20`.

### Foundational scalar bounds

Elementary Stirling and the Borel recurrence give, for `n>=1`,

    e^(-1)n^(-3/2) <= b_n <= (2 pi)^(-1/2)n^(-3/2),
    rho_n:=b_(n-1)/b_n=e(1-1/n)^(n-2),
    0<=log rho_n<=2/n.

Consequently, for `1<=r<=n/2`, `b_(n-r)/b_n` is uniformly bounded and
differs from one by `O(r/n)`. The exact Borel convolution and its weighted
form are

    sum_(t=1)^(m-1)b_t b_(m-t)=2(m-1)b_m/m,
    sum_(t=1)^(m-1)t b_t b_(m-t)=(m-1)b_m.          (BC)

### Small-argument cancellation in G

For `1<=x<=k/4`, the exact three-source coefficient satisfies

    |G_k(x)-2b_x| <= C_0 (x+1)b_x/k.                (SG)

Divide by `b_x` and split the survivor from the two fragmentation sources.
The survivor is `[q_x/b_x]h(D-x)=1+O((x+1)/k)`. For fragmentation define

    a_r(x)=((r-x-1)/R)[b_(r-x)/b_r].

Its no-shift comparison has the exact q-average

    sum_s q_s[(D-s)/R+1{s>x}s/R]
      =1+2/R-(1/R)sum_(s<=x)sq_s.                  (G0)

Long parents and short parents `s>=2x` differ from (G0) by
`O((x+1)/k)`. On the only non-smooth strip `x<s<2x`, use (BC),
`q_s<=Cb_s`, and cancellation in `q_s a_s(x)` to bound both comparison
mass and actual mass by

    (C/R)sum_(t<=x)t b_t <= C sqrt(x)/R <= Cx/k.

This proves (SG) without sign inference.

### Global G envelopes

The same decomposition with crude ratios gives

    G_k(x)<=C b_x,                                  1<=x<=j. (GG1)

For `j<=x<=L-1`, set `M=D-x`. Substitution `a=M-s`, kernel-denominator
cancellation, and (BC) give

    G_k(x) <= (C/R)sum_s b_s(M-s)b_(M-s)
           <= (C/R)(M-1)b_M
           <= C/[k sqrt(M)].                        (GG2)

At `x=j`, the survivor is separately `O(k^(-3/2))`, absorbed by (GG2).
The corrected G domain is essential here and is never exceeded.

### Coefficient regions and seams

For `2<=y<=k/4`, both exact sides have the same leading term:

    |B^Y_(k,y)-2b_y|+|A^Y_(k,y)-2b_y|
       <= C(y+1)b_y/k.                              (C1)

For B use (SG). For A, with `m=k-y`, use

    A^Y_(k,y)/(2b_y)
      =[b_m/b_k]{m+(m-1)(m-2)/(k-1)}/R

and the Borel ratio bound. Thus `|c^Y_(k,y)|<=C/(k sqrt(y))`.
For `k/4<y<=j`, each of A and B is `O(k^(-3/2))` by (GG1), yielding
the same envelope.

For `j<y<k`, put `m=k-y`. The A formula gives

    A^Y_(k,y)<=C m b_m/k<=C/[k sqrt(m)],

while (GG2) gives `B^Y_(k,y)<=Ck^(-3/2)`. At the seam,

    c^Y_(k,k)=B^Y_(k,k)=((k-1)/D)G_k(k-1)=O(k^(-3/2)).

Above the seam, for `y=k+z`, `1<=z<=j`,

    c^Y_(k,k+z)=((k-z)/D)G_k(k+z-1)+(z/D)G_k(z),

so (GG2), (GG1), and `zb_z<=C/sqrt(z)` prove the fourth line of (CP).

### Prefix summation and boundary ranks

Use `sum_(r<=n)r^(-1/2)<=2sqrt(n)`. If `ell<=j`, the first line of (CP)
gives `O(sqrt(ell)/k)`. If `j<ell<k`, the two endpoint sums are
`O(k^(-1/2))=O(sqrt(ell)/k)`. If `ell>=k`, add the seam and post-seam
sum, again obtaining `O(sqrt(ell)/k)`.

For `k=3,5,7`, each raw normalized one-run observable is bounded by three,
so the signed raw numerator is bounded by six; this is smaller than
`2^20 sqrt(ell)/k` for every `ell>=2`. This closes every odd boundary rank.

## Scope and next step

This skeleton proves only YCM once its displayed constants are audited. It
does not state or imply TCM, WBE, DE, J2, or any downstream claim. Next:
write the fully quantified proof, then and only then run compact exact
`k<=21` formula checks for falsification/calibration, freeze, and request a
fresh immutable audit.
