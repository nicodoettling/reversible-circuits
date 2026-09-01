# M289 exact CEBV support-pair coefficient theorem

Date: 2026-08-14 UTC.

Status: **CEBV proved for every odd `k>=3`, subject to a fresh immutable
audit.**  The proof uses a raw B/A support-pair collapse and signed phase
aggregation before every lag norm.  It does not use the refuted pointwise
`IKBE-b` route or adjacent-profile triangle bounds.  No downstream claim is
made.

## 1. Frozen interface and exact target

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`, and

```text
n=3k,       D=2k-1,       R=2k-3,       j=(k-1)/2.
```

The B exterior cycle has abstract word

```text
V=(1,...,k-1,2k,...,3k-1),
```

while the A exterior source consists of the two contiguous `k`-cycles
`C_0=(0,...,k-1)` and `C_2=(2k,...,3k-1)`.  Let `q_s`,
`1<=s<=j`, be the accepted A first-split probability law and put

```text
a_L(s)=1-gamma_L(s)=h(s)+h(D-s),
a_F(s)=1-gamma_F(s)=h(s)+h(k-s)+u,

h(r)=(r-1)(r-2)/(rR),       u=(k-1)/R,
qhat_s=q_s a_F(s).                                  (1.1)
```

For a disjoint product, let `I_l` be the complete ordered support-pair
collision profile and `Delta I_l=I_(l+1)-I_l`.  M276/M279 reduce the open
embedding vector exactly to

```text
(CEBV)
|| sum_(s=1)^j qhat_s(Phi_s^D-Psi_s^D) ||_1=O(1/k), (1.2)
```

where the vector coordinates are `Delta I_l`, `l=2,...,n-3`.  The
subprobability `qhat` is not renormalized.

## 2. Raw support-pair kernels

Write

```text
b_r=e^(-r)r^(r-1)/r!,
K_R(r,x)=b_x b_(r-x)/(R b_r),       1<=x<r,

U_r(x)=1[x<=r-2](r-x-1)K_R(r,x)
       +4(r-1)/(rR)-2K_R(r,x),                     (2.1)
```

and extend `U_r` by zero outside `1<=x<r`.  The first term is the ordered
second-edge endpoint pair.  The second term is the four first/second cross
pairs after deleting both marked-endpoint incidences.  Thus every ordered
factor and every support-collision multiplicity remains literal.

For an odd abstract cycle of size `M`, define

```text
Z_(M,r)(d)=U_r(d)+U_r(M-d),       1<=d<=(M-1)/2.   (2.2)
```

The B raw profile at fixed first split `s`, before conditioning on
disjointness, is the two-seam phase embedding of the symmetric abstract
coefficient

```text
beta_s(d)=a_L(s) 1[min(d,D-d)=s]
          +Z_(D,s)(min(d,D-d))
          +Z_(D,D-s)(min(d,D-d)).                  (2.3)
```

Equivalently the first term is the ordered first-edge pair and the last two
terms are all remaining ten ordered pairs.  Hence its total mass is
`12a_L(s)`, and its ambient embedding, denoted `mathcal B_s`, satisfies

```text
mathcal B_s=a_L(s)Phi_s^D(I).                      (2.4)
```

On the A side, marked second edges give

```text
V_s^A(d)=Z_(k,s)(d)+Z_(k,k-s)(d),       1<=d<=j.  (2.5)
```

An edge in the untouched `k`-cycle contributes the ordered second-edge
coefficient

```text
T_k(d)=k K_R(k,d),                    1<=d<k.      (2.6)
```

The remaining eight cross pairs have an `s`-independent ambient profile.
Let

```text
N_l=#{(x,y) in C_0 x C_2 : y-x=l mod n},
M_l=N_l+N_(n-l),
X_k(l)=4u M_l/k^2.                                  (2.7)
```

Indeed a fixed active vertex is a first-edge endpoint with probability
`2/k`, and a fixed untouched vertex has raw second-edge endpoint intensity
`2u/k`; the two factors are independent.  The triangular law is

```text
N_(2k+t)=k-|t|,       -(k-1)<=t<=k-1,
```

and zero otherwise.  Thus `sum_l X_k(l)=8u`.

Let `mathcal E_D` denote phase embedding along `V`, and let `mathcal E_k`
denote phase embedding in either contiguous A block.  The complete A raw
profile is exactly

```text
mathcal A_s
 =mathcal E_k[a_F(s)1[min(d,k-d)=s]+V_s^A(d)+T_k(d)]
  +X_k.                                             (2.8)
```

Its mass is

```text
2a_F(s)+10[h(s)+h(k-s)]+2u+8u=12a_F(s),
```

and therefore

```text
mathcal A_s=a_F(s)Psi_s^D(I).                      (2.9)
```

Equations (2.3)--(2.9) are coefficient identities, not estimates.

## 3. Exact cancellation of conditional normalizers

Put

```text
delta_s=a_F(s)/a_L(s)-1
 =2(k-1)/[R(k-s)(D-s)a_L(s)].                     (3.1)
```

The CEBV collision profile before its final lag difference is exactly

```text
H=sum_s q_s[(a_F(s)/a_L(s))mathcal B_s-mathcal A_s]
  =H_0+H_N,                                        (3.2)

H_0=sum_s q_s(mathcal B_s-mathcal A_s),
H_N=sum_s q_s delta_s mathcal B_s.
```

No conditional law has been renormalized.  Since `mathcal B_s` is
nonnegative with mass `12a_L(s)`, its full circular variation is at most
`24a_L(s)`.  Also

```text
delta_s a_L(s)
 =2(k-1)/[R(k-s)(D-s)]<=C/k^2.                    (3.3)
```

Using `sum q_s=1` gives

```text
TV(H_N)<=C/k^2.                                    (3.4)
```

It remains to prove `TV(H_0)=O(1/k)`.

## 4. Phase-embedding BV operators

For a symmetric coefficient on the abstract D-cycle, let its half-profile
be `f_1,...,f_(k-1)`, with `f_0=f_k=0`.  Direct two-seam phase counting gives

```text
(mathcal E_D f)_l
 =[(D-2l)f_l+(l-1)f_(l-1)]/D,          1<=l<=k,

(mathcal E_D f)_(k+r)
 =[r f_r+(k-r)f_(k-r)]/D,              1<=r<=k-1,

(mathcal E_D f)_(n-l)=(mathcal E_D f)_l.           (4.1)
```

Adjacent subtraction implies

```text
TV(mathcal E_D f)
 <=C TV(0,f_1,...,f_(k-1),0)
   +(C/D)sum_d|f_d|.                                (4.2)
```

For a symmetric coefficient on a contiguous abstract `k`-cycle, write its
half-profile `g_1,...,g_j`, with `g_0=g_(j+1)=0` and
`g_d=g_(k-d)`.  The one-wrap-seam law is

```text
(mathcal E_k g)_l=(k-l)g_l/k,       1<=l<k,
(mathcal E_k g)_l=0,                k<=l<=2k,
(mathcal E_k g)_(n-l)=(mathcal E_k g)_l.           (4.3)
```

The same adjacent subtraction gives

```text
TV(mathcal E_k g)
 <=C TV(0,g_1,...,g_j,0)
   +(C/k)sum_(d=1)^j|g_d|.                          (4.4)
```

These inequalities apply to signed coefficients and retain both seams.

## 5. Seam-comparison lemma

### Lemma 1 (proved: two-seam versus one-seam comparison)

Let `w_s`, `1<=s<=j`, be nonnegative and put `a_s=s w_s`, `a_0=0`.
If

```text
TV(a_0,a_1,...,a_j)<=C_0,                          (5.1)
```

let `f^D_s=w_s` for `s<=j`, `f^D_s=0` for `j<s<k`, and let
`f^k_d=w_min(d,k-d)`.  Then

```text
TV(mathcal E_D f^D-mathcal E_k f^k)<=C C_0/k.     (5.2)
```

#### Proof

For `1<=l<=j`, subtraction of (4.1) and (4.3) gives exactly

```text
(mathcal E_D f^D-mathcal E_k f^k)_l
 =a_(l-1)/D-a_l/(kD).                              (5.3)
```

At `l=j+1`, the value is `a_j(1/D-1/k)`.  For `j+1<l<k`, putting
`t=k-l` gives `-a_t/k`.  Hence the entire low-range variation is
`O(C_0/k)`.  On the middle range `l=k+r`, (4.1) is exactly

```text
a_r/D,           1<=r<=j,
a_(k-r)/D,       j<r<k,
```

while (4.3) is zero.  Its endpoint-inclusive variation is again
`O(C_0/k)`.  Reflection only doubles the bound.  QED.

The lemma also admits a tail of half-profile variation `O(k^-3/2)` and
`l1=O(k^-1/2)` on `j<s<k`, by (4.2), and admits a constant tail of height
`O(1/k)` with cost `O(1/k)`.

Two instances will be used.  First,

```text
w_s=q_s a_L(s).                                    (5.4)
```

The exact Borel product law, `a_L>=1/2` on this range, and adjacent-ratio
bounds give

```text
w_s<=Cb_s,
|(s+1)w_(s+1)-s w_s|
 <=C s^(-3/2)+C/[k sqrt(s)].                       (5.5)
```

Thus (5.1) holds uniformly.  Second, `w_s=b_s` satisfies (5.1) directly.
The Borel tail `b_s`, `j<s<k`, has variation `O(k^-3/2)` and l1
`O(k^-1/2)`.  Therefore

```text
TV(mathcal E_D[b_d]-mathcal E_k[b_min(d,k-d)])
 =O(1/k).                                          (5.6)
```

Here the left profile uses `b_d`, `1<=d<k`, on the D half-cycle and the
right profile uses the symmetric k-cycle coefficient.

## 6. B and A component-kernel stabilization

### Lemma 2 (proved: general one-component stabilization)

For odd abstract cycle size `M`, `1<=r<M`, and half range
`1<=d< M/2`, define `Z_(M,r)` by (2.2), with zero padding at both half
endpoints.  Uniformly for the present `M in {D,k}`,

```text
TV[Z_(M,r)(d)-((r/R)b_d+4/R)]<=C/R.               (6.1)
```

#### Proof

The direct row `U_r(d)` is identical to M282/M286's accepted stabilized
row.  On `d<r`, subtracting the reference gives

```text
R^-1{b_d[(r-d-3)b_(r-d)/b_r-r]-4/r}.
```

The Borel product-ratio estimates give bracket variation `O(1)` on both
halves of the active range.  On `d>=r`, the error is
`-[r b_d+4]/R`; its internal variation, the `r-1/r` cutoff, and both
zero endpoints cost `O(1/R)`.  The reflected row is active only when
`d>M-r`.  With `a=r-(M-d)`, the half-range condition and `r<M` give
`a<r/2`; its bracket

```text
4(r-1)/r+(a-3)b_a b_(r-a)/b_r
```

has variation and endpoint values `O(1)`.  Division by `R` proves (6.1),
including `r=1,2`, the midpoint, and support cutoff.  QED.

For B, pairing `r=s,D-s` and averaging `q_s` gives the half-profile

```text
B_2(d):=sum_s q_s[Z_(D,s)(d)+Z_(D,D-s)(d)],

TV[B_2-((D/R)b_d+8/R)]<=C/R.                      (6.2)
```

For A marked components, pairing `r=s,k-s` gives

```text
A_mark(d):=sum_s q_s[Z_(k,s)(d)+Z_(k,k-s)(d)],

TV[A_mark-((k/R)b_d+8/R)]<=C/R.                   (6.3)
```

All errors in (6.2)--(6.3) also have l1 `O(1)`, since each raw profile and
each reference has uniformly bounded mass.

For the untouched second-edge coefficient (2.6), put

```text
Q_k(d)=b_(k-d)/b_k.
```

On `d<=j`, `Q_k(d)` is bounded,
`|Q_k(d)-1|<=Cd/k`, and `|Delta Q_k(d)|<=C/k`.
Consequently

```text
TV[T_k(d)-(k/R)b_d]
 <=C/k sum_d b_d +O(k^-3/2)
 =O(1/k),                                          (6.4)
```

with zero endpoints included.  The error has l1 `O(1)`.  Combining
(6.3)--(6.4),

```text
TV[A_mark+T_k-((2k/R)b_d+8/R)]=O(1/k).             (6.5)
```

## 7. Proof of the raw embedding BV

Split `H_0` into first-edge, remaining within-block, and untouched cross
terms.

For first edges, put `w_s=q_s a_L(s)`.  Equations (2.3), (2.8), and (5.4)
give

```text
H_first
 =mathcal E_D[f_w^D]-mathcal E_k[f_w^k]+R_first,
```

where `R_first` is the A first-edge profile with total mass
`2sum_s q_s[a_F(s)-a_L(s)]=O(k^-2)`.  Its variation is at most twice its
mass.  Lemma 1 therefore yields

```text
TV(H_first)=O(1/k).                                (7.1)
```

For the remaining within-block terms, (4.2), (4.4), and the l1 guards in
Section 6 allow the stabilization errors to pass through phase embedding
at cost `O(1/k)`.  Since `2k=D+1`, the coefficient difference between the
two Borel references is itself `1/R=O(1/k)`.  The constant reference
`8/R` has height `O(1/k)`.  Lemma 1 with `w_s=b_s`, its permitted Borel
tail, and its constant-tail clause now give

```text
TV(mathcal E_D[B_2]-mathcal E_k[A_mark+T_k])
 =O(1/k).                                          (7.2)
```

Finally, the triangular count in (2.7) has total variation `O(k)`.
Therefore

```text
TV(X_k)<=4u O(k)/k^2=O(1/k).                       (7.3)
```

Equations (7.1)--(7.3) prove

```text
TV(H_0)=O(1/k).                                    (7.4)
```

Together with (3.4), this proves `TV(H)=O(1/k)`.

## 8. CEBV theorem and boundary cases

The CEBV vector is the restriction of the adjacent differences of `H` to
`l=2,...,n-3`.  Restriction cannot increase l1, so (3.4) and (7.4) prove:

### Theorem (proved, subject to fresh audit)

There is an absolute constant `C` such that for every odd `k>=3`, retaining
literal collision support, all cyclic phases, both B seams, ordered factors,
product kind, support collisions, and the original subprobability
normalization,

```text
|| sum_(s<k/2) qhat_s(Phi_s^D-Psi_s^D) ||_1
 <=C/k.                                             (8.1)
```

Every displayed estimate is uniform for `k>=5`.  At `k=3`, the same exact
finite formulas have only `s=1` and components of sizes `1,2,3,4`; the
`r=1,2`, midpoint, seam, reflection, and zero-endpoint cases are already
included in Lemmas 1--2, so enlarging the absolute constant covers the
minimal rank without an asymptotic threshold.

## 9. Exact stop

This theorem closes only `CEBV`, subject to a fresh immutable audit.  Even
together with accepted CSBV, no mission here infers `CIBV`; that assembly is
reserved for the coordinator after audit.  `DOR`, `SET`, `PBV`, `FD`,
`FCL1`, every bridge/local gap, polynomial mixing, and Terminal A/B remain
unresolved.

## 10. First open obligation

There is no remaining mathematical sublemma inside the claimed CEBV proof.
The first open obligation is the following standalone certification gate:

### Fresh immutable reconstruction obligation (open)

Starting only from the accepted M276/M279 interface and the frozen
predecessor ledgers, independently reconstruct the raw identities
(2.3)--(2.9), the normalizer cancellation (3.2), both phase operators, and
Lemmas 1--2, including `k=3`, `r=1,2`, midpoint, reflection, active/inactive
cutoffs, both seams, ordered factors, and zero endpoints.  Accept (8.1) only
if that reconstruction has no numbered objection.  This audit obligation is
not a hypothesis used in the proof and licenses no downstream inference.
