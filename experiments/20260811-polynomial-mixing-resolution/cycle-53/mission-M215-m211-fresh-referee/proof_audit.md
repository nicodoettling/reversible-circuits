# M215 clean-room proof audit of immutable M211

Date: 2026-08-13 UTC.

Verdict: **ACCEPT** M211's refutation of pointwise IKBE-b and therefore of
the two-clause conjunction called IKBE. Material objections: none.
IKBE-a/DV and signed averaged DE remain unresolved.

## 1. Immutable gate

All eight files named by frozen M211 passed sha256sum -c SHA256SUMS before
the proof was read. Fresh hashes agree; M211's checksum-file digest is

    79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225.

M211 was not edited.

## 2. Exact witness geometry

For q>=1 set

    k=12q-1, D=2k-1=24q-3, n=3k=36q-3,
    s=3q, l=4q.

Then k is odd, 1<=s<k/2, and 2<=l<=(3k-1)/2.

For a source step x=s<k, the two-seam law has gaps

    s, s+1, s+k

with multiplicities D-2s,s,s. The cutoff l=4q contains s=3q and
s+1=3q+1 but not s+k=15q-1. Therefore

    F_l(s)=(D-s)/D=1-s/D.                              (2.1)

For x=D-s, the complementary length is s. Its gaps are

    n-s=33q-3, n-s-1=33q-4, n-s-k=21q-2.

All exceed l=4q, including q=1, so

    F_l(D-s)=0.                                       (2.2)

The contiguous A incidence is

    J_l(x)=(k-x)/k 1{2<=x<=l}.

Thus

    J_l(s)=1-s/k,   J_l(k-s)=0,                       (2.3)

because k-s=9q-1>4q.

## 3. Independent Borel normalization

Let

    b_d=e^(-d)d^(d-1)/d!.

The rooted-tree series

    T(z)=sum_(d>=1)d^(d-1)z^d/d!

satisfies T=ze^T on 0<=z<=e^-1. At z=e^-1 its minimal nonnegative solution
is T=1. Hence

    sum_(d>=1)b_d=1,  b_1=e^-1,
    beta:=sum_(d>=2)b_d=1-e^-1.                       (3.1)

This independently supplies the beta used by M211.

## 4. Uniform critical-Borel tail

Put R=2k-3 and

    K_R(r,d)=b_d b_(r-d)/(R b_r),
    W_r(f)=sum_(d<r)(r-d-1)K_R(r,d)f(d).

Suppose r/k->rho in (0,2], 0<=f_k<=1, and for fixed d,
f_k(d)->1{d>=2}. Uniform Stirling bounds give

    c m^(-3/2)<=b_m<=C m^(-3/2).                      (4.1)

For fixed M and M<d<=r/2,

    b_(r-d)/b_r<=C,

so, using (r-d-1)/R<=C,

    sum_(M<d<=r/2)(r-d-1)K_R(r,d)f_k(d)
      <=C sum_(d>M)b_d
      <=C M^(-1/2).                                   (4.2)

For d>r/2 write c=r-d. The summand becomes

    (c-1)b_(r-c)b_c f_k(r-c)/(R b_r).

Since b_(r-c)/b_r<=C and sum_(c<=r/2)c b_c<=C sqrt(r),

    sum_(d>r/2)... <= C sqrt(r)/R=O(k^-1/2).           (4.3)

For fixed d,

    (r-d-1)/R ->rho/2,
    b_(r-d)/b_r->1.

Taking k to infinity, then M to infinity, gives

    W_r(f_k)->(rho/2)beta.                             (4.4)

For the untouched term

    C_l=sum_(d<k)(k-d)K_R(k,d)1{2<=d<=l},

with l=4q<k/2, the same fixed-d limit and (4.2) bound give

    C_l->beta/2.                                      (4.5)

This verifies both child-size ranges and leaves no uncontrolled bulk.

## 5. Exact profile decomposition

With

    h(r)=(r-1)(r-2)/(rR),  u=(k-1)/R,

the audited literal formulas regroup as

    Phi=[h(s)F(D-s)+h(D-s)F(s)
         +W_s(F)+W_(D-s)(F)]
        /[h(s)+h(D-s)],                               (5.1)

    Psi=[h(s)J(k-s)+h(k-s)J(s)
         +W_s(J)+W_(k-s)(J)
         +u(J(s)+J(k-s))+C_l]
        /[h(s)+h(k-s)+u].                             (5.2)

These denominators are exactly 1-gamma_L(s) and 1-gamma_F(s), respectively.

## 6. Kernel cancellation

The macroscopic parent ratios are

    s/k->1/4, (D-s)/k->7/4, (k-s)/k->3/4.

By (4.4)--(4.5),

    W_s(F)+W_(D-s)(F)->beta/8+7beta/8=beta,

    W_s(J)+W_(k-s)(J)+C_l
      ->beta/8+3beta/8+beta/2=beta.                   (6.1)

Thus every fragmentation term cancels in the B-minus-A limit.

## 7. Surviving faces and normalizers

Directly,

    h(s)->1/8, h(D-s)->7/8,
    h(k-s)->3/8, u->1/2.

Both denominators in (5.1)--(5.2) tend to one. Using (2.1)--(2.3),
the B surviving term tends to

    (7/8)(1-1/8)=49/64,

while A's marked plus untouched term tends to

    (3/8+1/2)(1-1/4)=42/64.

Together with (6.1),

    Phi_(3q)^D(Y_(4q))-Psi_(3q)^D(Y_(4q))->7/64.      (7.1)

Finally,

    sqrt(l)/k=2sqrt(q)/(12q-1)->0.

The positive constant (7.1) contradicts every proposed universal
pointwise IKBE-b bound C sqrt(l)/k.

## 8. Calibration and scope

The clean-room checker imports no M211 code/data and uses only the exact
closed formulas at q=1. It obtains

    (k,s,l)=(11,3,4),
    F_l(s)=6/7, J_l(s)=8/11,
    Phi-Psi approximately 0.09224121091748724,

matching M211's rational exactly. This is calibration only; (7.1) supplies
the universal refutation.

The counterexample refutes pointwise IKBE-b and hence the conjunction called
IKBE. It does not refute IKBE-a/DV. It also does not refute signed averaged
DE: the q_hat weighting and signed summation across s are absent from the
pointwise witness and may still yield cancellation.

## 9. Objections and verdict

Material objections: none.

Numbered nonmaterial qualifications:

1. In M211's second-range estimate, the displayed phrase
   b_(r-c)/b_r<=C relies on c<r/2 after the substitution; recording this
   condition explicitly makes the uniformity transparent.
2. The Borel normalization can be made self-contained by mentioning the
   rooted-tree equation T=ze^T at z=e^-1, as above.

Neither changes the theorem. Verdict: ACCEPT, with scope restricted exactly
to pointwise IKBE-b/the two-clause IKBE conjunction. Keep IKBE-a/DV, signed
averaged DE, conditional J=2, and all downstream claims open.
