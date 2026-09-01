# M277 independent reconstruction of the M274 interface

Date: 2026-08-14 UTC.

Status: Sections 1--6 are independent exact derivations from the
checksum-verified predecessor definitions.  They were fixed before M274's
checker implementation was opened.  No universal sign or minority-mass
estimate is asserted.

## 1. Scope, target, and immutable source gate

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`,
and `n=3k`.  Put

```text
h=(0,1,...,n-1),
A=(0,k,2k),                    B=(0,1)(k,2k),
E_r=(r,r+1),
t_(r,y)=E_r E_(r+y+1),         1<=y<=n-3.
```

This is only the first separated fixed cell of the auxiliary uniform
minimal length-`n-1` factorization law of `h`, under the nonlazy cyclic
rank-two quotient kernel.

M274's supplied checksum-ledger digest is

```text
c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e,
```

and all ten named payloads pass.  The cited dependency-ledger digests are

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M100  bc5a915fc10aef4b546542938e9289e516e97a13553d4888d7b0395acd8965a2
M161  17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166  344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168  3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171  c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M174  fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba
M178  6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M266  6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268  62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270  6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
```

Every payload in all fifteen dependency inventories passes.

## 2. Raw per-lag law, lifts, kinds, and topologies

For a supported rank-two product `s`, put

```text
q_s=s^-1h,
A_s=F_(n-3)(q_s),
C_g(s)=F_(n-5)((gs)^-1h),
omega(s)=a(s)[C_B(s)/A_B-C_A(s)/A_A],               (2.1)
```

where `a(s)=3` for an oriented triangle and `a(s)=2` for a double.
Thus `omega=P_B-P_A` is already the complete signed first-pair product
law.

Let

```text
W_(k,y)(s)=sum_(r mod n)
 F_(n-5)(t_(r,y)s^-1h),
R_(y+1)(s)=W_(k,y)(s)/A_s,
F_T=F_(n-3)(t_(0,1)^-1h).
```

The target orbit has raw double lift two, free phase orbit size `n`, and
constant mass

```text
pi_y=2nF_T/n^(n-2).
```

The target lift two cancels the same factor in `pi_y`; the intermediate
lift `a(s)` remains.  Therefore

```text
Lambda_n=n^(n-2)/(nF_T)
        =(n-2)(1-2/n)^(-(n-3)),

z_k(y)=Lambda_n sum_s omega(s)R_(y+1)(s)

      =n^(n-2)/(nF_T) [
          sum_(s in X_T)3 d_k(s)W_(k,y)(s)/A_s
         +sum_(s in X_D)2 d_k(s)W_(k,y)(s)/A_s],

d_k(s)=C_B(s)/A_B-C_A(s)/A_A.                       (2.2)
```

For an explicit topology check, let the three residual cycles of `q_s`
have sizes `d_i`, ranks `r_i=d_i-1`, and let a chord in a directed
cycle `C` have exact first-factor law `nu_C`.  Let
`mu_C^S,mu_C^N` be the exact ordered-double completion laws for separated
and nested chords, including their double lift two.  With
`R_n=(n-3)(n-4)`, the target response partitions literally as

```text
bar K(O_s,O_y)=P_y^S(s)+P_y^N(s)+P_y^X(s),           (2.3)

P_y^c(s)=sum_(r mod n)sum_i r_i(r_i-1)/R_n
  1[{E_r,E_(r+y+1)} subset C_i]
  mu_(C_i)^c(E_r,E_(r+y+1)),             c in {S,N},

P_y^X(s)=sum_(r mod n)sum_(i<j)2r_i r_j/R_n [
  1[E_r subset C_i,E_(r+y+1) subset C_j]
     nu_(C_i)(E_r)nu_(C_j)(E_(r+y+1))
 +1[E_r subset C_j,E_(r+y+1) subset C_i]
     nu_(C_j)(E_r)nu_(C_i)(E_(r+y+1))].             (2.4)
```

Equations (2.2)--(2.4) retain triangle/double intermediate kinds and all
`IS/IN/X` target topologies.  Inadmissible phases contribute zero.

## 3. Reflection and endpoints

The displayed lag is

```text
ell=y+1 in {2,...,n-2}.
```

Thus both disjoint-edge endpoints `ell=2,n-2` are present.  Reversing the
unordered target-edge pair gives

```text
z_k(y)=z_k(n-2-y).                                  (3.1)
```

The involution has no fixed integer because `n-2` is odd.  Hence the
`n-3` colored appearances form pairs, and every physical target orbit
appears exactly twice.  This is an intentional colored duplication, not a
missing factor.

## 4. Exact channel formulas and the CP hierarchy

Let `H_(j,g)` be M91's normalized conditional source law in exterior
channel `j=1,2`.  The common `j=0` laws cancel.  The exact source
difference is

```text
eta=alpha_1(H_(1,B)-H_(1,A))
    +alpha_2(H_(2,B)-H_(2,A)),                      (4.1)

alpha_1=4(k-1)^2/[3(k-1)(3k-4)],
alpha_2=2(k-1)(2k-3)/[3(k-1)(3k-4)].
```

Define the normalized scalar response

```text
g_(k,y)(s)=2W_(k,y)(s)/(A_s pi_y)
          =Lambda_n R_(y+1)(s).                     (4.2)
```

Then

```text
CP_j(k,y)=(H_(j,B)-H_(j,A))(g_(k,y)),
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y).         (4.3)
```

Let `L=(1,...,k-1,2k,...,3k-1)`,
`M=(k,...,2k-1)`, and
`F=C_-C_+` with `C_-=(0,...,k-1)`,
`C_+=(2k,...,3k-1)`.  Direct substitution of the literal conditional
factor laws gives

```text
CP_1=
 sum_(e in T(L))nu_L(e)sum_(f in T(M))nu_M(f)g(ef)
 -1/2 sum_(C in {C_-,C_+})sum_(e in T(C))nu_C(e)
       sum_(f in T(M))nu_M(f)g(ef),                 (4.4)

CP_2=
 sum_(e in T(L))sum_(f in T(eL))N_L(e,f)g(ef)
 -sum_(C in {C_-,C_+})sum_(e in T(C))
       sum_(f in T(eF))N_F(e,f)g(ef).               (4.5)
```

The fair first exterior-component choice in channel two is already encoded
by the normalized full-`F` law `N_F`; adding another `1/2` would be
wrong.

Consequently

```text
CP_1,CP_2 >=0 pointwise  =>  OS+: z_k(y)>=0.         (4.6)
```

Channel positivity is sufficient but stronger than a direct
channel-combined score inequality.

## 5. PCS plus minority mass

Define

```text
P_k=sum_y(z_k(y))_+,
N_k=sum_y(-z_k(y))_+.
```

For any finite real sequence,

```text
sum_y|kz_k(y)|
 =k(P_k+N_k)
 =k|P_k-N_k|+2k min(P_k,N_k)
 =k|sum_y z_k(y)|+2k min(P_k,N_k).                  (5.1)
```

M266/M268 proves uniformly over odd `k>=3`

```text
(PCS)   k|sum_y z_k(y)|=O(1).
```

Therefore the first-cell absolute estimate
```text
(FCL1)  sum_y|kz_k(y)|=O(1)
```
holds if and only if
```text
(MS)    k min(P_k,N_k)=O(1).                        (5.2)
```

The reverse implication `FCL1=>MS` is immediate from (5.1); the forward
implication uses proved PCS.  Thus “equivalent given PCS” is the correct
logical strength.  OS+ makes `N_k=0` and is strictly stronger.

## 6. Positive kind transfer is not atomwise positivity

The exact channel-two kind transfer is

```text
eta(T)=12(k-1)/[3k(3k-4)(2k-1)]>0,
eta(D)=-eta(T).                                      (6.1)
```

At each lag `2<=ell<=n-2`, M261's affine separation is

```text
z_k(ell-1)=Lambda_n e^-2/[(n-3)(n-4)]
 [2eta(T)+eta(I_ell)+eta(Q_ell)].                   (6.2)
```

The phase-total event contrast is separately

```text
Delta_k(C_k)=e^-2/[(n-3)(n-4)]
 [2n eta(T)+eta(B_k)].                              (6.3)
```

The first displayed term is positive in (6.2) and (6.3), but the signed
collision/decorated or boundary remainder has no proved lower bound.
Neither positivity of `2eta(T)` nor positivity of its phase sum
`2n eta(T)` implies a per-lag score sign, raw-atom sign, OS+, or MS.

## 7. Analytic raw-atom firewall

The direct formulas (4.4)--(4.5) have both signs at every odd rank.
Let

```text
e_+=(1,2k),       e_-=(0,1),       f_M=(k,k+1).
```

`e_+` is internal to `L` and to neither separate cycle, while `e_-`
is internal to `C_-` and absent from `L`.  Hence the raw channel-one
atoms `(e_+,f_M)` and `(e_-,f_M)` have respectively positive and
negative signed coefficients.

For channel two choose `f=(1,2)`.  Cutting `L` by `e_+` leaves a
`(k-1)`-cycle containing `1,2`; cutting `C_-` by `e_-` does the
same.  Thus both ordered atoms are admissible and have respectively
positive and negative signed coefficients.  This is an exact counterfamily
for all odd `k>=3`.  It refutes only raw atomwise positivity; cancellation
after grouping by the response value remains possible.

## 8. Independent finite reproduction

The no-import checker reconstructs the exact cyclic quotient, normalized
conditional laws, and target response directly from permutation products and
minimal-completion counts.  It obtains:

```text
k=3: MON failures 4  = 0 adjacent + 4 embedding,
     FOSD upper-tail failures 36;

k=5: MON failures 46 = 32 adjacent + 14 embedding,
     FOSD upper-tail failures 250.
```

The first `k=3` embedding defect is exactly

```text
-876877452441/14123762450000,
```

and the first FOSD defect is exactly `-32/375` at threshold
`343359/268912`.  Every one of the 18 full scores, all four signed blocks in
each row, and both violation counts agree with frozen M274.  Both `CP_j` are
strictly positive in all 36 finite channel-lag tests, with exactly the four
weighted minima printed by M274.  This is finite calibration only.

The retained `k=9` artifact has 24 strictly positive exact scores, exact
reflection, endpoint equality, and exact reconstruction from all six
triangle/double topology parts.  Its minimum is attained at the reflected
pair

```text
y=7 and y=18,
score=580831276471610051279788142378387803852964672689057077515748629008943685931026032121674360006369721985955610452803703256981901005784819675050597717251521554590305783769134227638567918655290612160179411748230201358677365324745050547697
      /96807272859689495189672079251168298025546443676394441647201213168174231747479264458170679967406261603978098549357976716692473316773152304490425456683731079101562500000000000000000000000000000000000000000000000000000000000000000000000000.
```

There the triangle sum is positive (`0.010948178900420163`) and the double
sum is negative (`-0.004948306583869576`), so kindwise signing is already
invalid.  A fresh M161 evaluation reproduces every mathematical field.

The raw-atom construction was also instantiated for every odd
`k=3,5,...,21`.  This is only a checker sanity test; the proof for all odd
`k>=3` is the explicit component-membership and post-cut argument in Section
7.

## 9. Audited logical endpoint

The exact hierarchy is

```text
CP_1>=0 and CP_2>=0 pointwise
       => OS+: z_k(y)>=0 pointwise
       => MS: k min(P_k,N_k)=O(1)
       <=> FCL1, conditional on proved PCS.
```

Here CP is fully recombined *within each channel*; the genuinely
cross-channel score is `alpha_1 CP_1+alpha_2 CP_2`.  MON, FOSD, and literal
raw ordered-atom positivity are refuted.  CP, OS+, MS, and FCL1 remain open.
No finite outcome licenses a later-cell, direct-L1, gap, mixing, or Terminal
claim.
