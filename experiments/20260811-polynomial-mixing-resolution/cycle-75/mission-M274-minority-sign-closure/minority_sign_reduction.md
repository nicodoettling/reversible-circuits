# M274 exact minority-sign reconstruction

Date: 2026-08-14 UTC.

Status: Sections 1--3 are exact consequences of frozen M161/M166,
M168/M171, and M266/M268.  The minority-sign estimate in Section 4 and the
directional positive-sign statement in Section 5 are **unresolved**.

## 1. Scope and conventions

Permutations compose as `(pq)(x)=p(q(x))`, and displayed factors multiply
left-to-right.  Fix odd `k>=3`, put `n=3k`, and set

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k),
E_r=(r,r+1)                    (indices modulo n),
t_(r,y)=E_r E_(r+y+1),         1<=y<=n-3.
```

This is the first separated fixed cell of the auxiliary uniform
minimal-length factorization law of `h` and M73's nonlazy cyclic rank-two
coordinate kernel.  It is not the global identity-word law and not the lazy
exact `{3,4,5}` heat-bath chain.

Write `O_y` for the cyclic orbit of `t_(0,y)` and

```text
z_k(y)=
 [bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/pi_y,
pi_y=2n F_T/n^(n-2),
F_T=F_(n-3)(t_(0,1)^(-1)h).
```

The lags are exactly `ell=y+1 in {2,...,n-2}`.  Reflection reverses the
unordered target pair and gives

```text
z_k(y)=z_k(n-2-y).                                  (1.1)
```

Because `n` is odd, the involution has no fixed `y`; every physical target
orbit appears exactly twice in the displayed colored list.  Both endpoints
`ell=2,n-2` are included.

## 2. Literal per-lag response, kinds, and channels

Let `X_n=X_T disjoint_union X_D` be the supported rank-two products.  For
`s in X_n`, let `a(s)=3` on oriented triangles and `a(s)=2` on doubles, and
put

```text
A_s=F_(n-3)(s^(-1)h),
C_g(s)=F_(n-5)((gs)^(-1)h),
d_k(s)=C_B(s)/A_B-C_A(s)/A_A,
W_(k,y)(s)=sum_(r mod n)F_(n-5)(t_(r,y)s^(-1)h).
```

The complete exact raw formula is

```text
z_k(y)=n^(n-2)/(n F_T)
       [ sum_(s in X_T) 3 d_k(s) W_(k,y)(s)/A_s
        +sum_(s in X_D) 2 d_k(s) W_(k,y)(s)/A_s ].   (2.1)
```

Here `W_(k,y)(s)` is the sum of all `IS`, `IN`, and `X` target topologies.
It is nonnegative, but `d_k(s)` has no asserted sign.  Formula (2.1) sums
triangle/double kinds and every topology before an absolute value.  Thus a
positive `W` is not a positivity proof for `z`.

For the exact two-channel form, put

```text
p_s=b_s b_(2k-1-s)/[(1-1/(2k-1))b_(2k-1)],
q_s=b_s b_(k-s)/[(1-1/k)b_k]      (s<k/2),
q_s=0                              (s>k/2),
D_u=sum_(s<=u)(p_s-q_s),

alpha_1=4(k-1)^2/[3(k-1)(3k-4)],
alpha_2=2(k-1)(2k-3)/[3(k-1)(3k-4)].
```

The endpoints are `D_0=D_(k-1)=0`; the Abel gradient runs over
`1<=u<=k-2`, while the embedding term runs over
`1<=u<k/2`, equivalently `1<=u<=(k-1)/2`.  If

```text
R_(k,y)(rho)=E_(s~rho)[2W_(k,y)(s)/(A_s pi_y)],
```

where the factor `2` is the literal target-double lift, then

```text
z_k(y)=sum_(j=1)^2 alpha_j {
  sum_(u=1)^(k-2)D_u[
    R_(k,y)(Phi_(j,u))-R_(k,y)(Phi_(j,u+1))]
 +sum_(u<k/2)q_u[
    R_(k,y)(Phi_(j,u))-R_(k,y)(Psi_(j,u))] }.        (2.2)
```

Every `Phi` and `Psi` is a normalized law containing its literal
triangle/double outcomes.  Channel `j=1` is one exterior factor and one
independent middle factor; channel `j=2` contains the full ordered second
exterior-factor conditional.  The common `j=0` law cancels as a measure.
The two displayed channels, the `T/D` outcomes inside each, both Abel terms,
all cyclic phases, and `IS/IN/X` are combined before any sign or absolute
value is taken.

## 3. Exact phase total and every retained boundary term

M168's all-lag collapse is obtained by summing (2.1) over
`y=1,...,n-3`, equivalently over all ordered disjoint boundary-edge pairs.
For the three residual cycles of `s^(-1)h`, let `d_i` be their sizes,
`g_i` their numbers of generic boundary edges, and `a_i` their numbers of
ambient-adjacent generic edge pairs.  Then

```text
S(s)=sum_i [g_i(g_i-1)-2a_i]
          F_(n-5)(sort(d_1,...,1,1,d_i-2,...,d_3))
    +sum_(i<j)2g_i g_j
          F_(n-5)(sort(d_other,1,d_i-1,1,d_j-1)),    (3.1)

sum_y z_k(y)=n^(n-2)/(nF_T)
 sum_(s in X_n) a(s) S(s)/A_s
       [C_B(s)/A_B-C_A(s)/A_A].                     (3.2)
```

The subtraction `-2a_i` is the adjacent-pair boundary correction; invalid
small sizes are zero.  Same-component `IS/IN` and cross-component `X`, both
source channels, and both intermediate kinds remain in (3.2).

The now-proved PCS estimate is

```text
k |sum_y z_k(y)|=O(1).                              (PCS)
```

Its proof does not discard endpoint terms.  In the accepted final
summation-by-parts interface it retains the singleton and both cutoff
endpoints

```text
M_1(1)u_1(1),          A_m u_2(m),          C_m r_m,
m=(n-1)/2,
```

all interior first differences, the channel-two shared endpoint, and the
unequal-disjoint-mass endpoint.  Odd `n` has no omitted half-size cell.

M174's phase-summed affine identity is, separately,

```text
Delta_k(C_k)=e^(-2)/[(n-3)(n-4)]
             [2n eta(T)+eta(B_k)],                  (3.3)

eta(T)=12(k-1)/[3k(3k-4)(2k-1)]>0,
eta(D)=-eta(T).
```

The first term in (3.3) is a positive **phase-total kind-transfer** term.
The collision/bounded-remainder coefficient `eta(B_k)` is separate and has
no proved sign.

M261/M264, whose checksum-ledger digests are
`b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b`
and `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f`,
give the finer exact per-lag separation.  With

```text
I_ell(s)=sum_r 1[r+1 in supp(s)]1[r+ell+1 in supp(s)],
Q_ell(s)=sum_(i,j)(e^2 kappa_ij(s)-1)C_ij^s(ell),
Lambda_n=(n-2)(1-2/n)^(-(n-3)),
R_n=(n-3)(n-4),
```

one has

```text
z_k(ell-1)=Lambda_n e^(-2)/R_n
 [2eta(T)+eta(I_ell)+eta(Q_ell)].                    (3.4)
```

Thus `2eta(T)>0` is the exact per-lag baseline.  It must remain separate
from the signed collision/decorated remainder
`eta(I_ell)+eta(Q_ell)`, which has no proved lower bound and may not be
triangle-bounded by its two pieces.  The existence of the positive baseline
does not by itself prove a score sign.

## 4. Exact minority-mass equivalence after PCS

Define

```text
P_k=sum_(y=1)^(n-3)(z_k(y))_+,
N_k=sum_(y=1)^(n-3)(-z_k(y))_+.
```

For every real finite sequence, and hence exactly here,

```text
sum_y |kz_k(y)|
 =k|P_k-N_k|+2k min(P_k,N_k)
 =k|sum_y z_k(y)|+2k min(P_k,N_k).                  (4.1)
```

Consequently, in the presence of proved PCS, FCL1 is equivalent to the
single symmetric one-sided-mass estimate

```text
(MS)       k min(P_k,N_k)=O(1)                      (4.2)
```

uniformly over odd `k>=3`.  A directional estimate `kN_k=O(1)` is
sufficient but not necessary.  The one-sign statement

```text
(OS)       P_k N_k=0                                (4.3)
```

is stronger still.  The finite observations suggest the directional form
`z_k(y)>=0`, but no sign of either (2.1) or (2.2) has been proved.

## 5. Fixed universal sign candidate and analytic obstruction

The natural universal candidate to falsify is

```text
(OS+)      z_k(y)>=0
           for every odd k>=3 and every 1<=y<=3k-3. (5.1)
```

Neither representation gives termwise positivity:

1. In (2.1), `W_(k,y)(s)>=0`, but the complete source coefficient `d_k(s)`
   is signed.
2. In (2.2), `D_u<0` throughout `1<=u<=k-2`; the response differences
   have no established common orientation.  The embedding differences have
   no established common orientation either.
3. Triangle and double aggregate contributions already have opposite signs
   in frozen exact finite rows.  They cannot be bounded or signed
   independently without losing the required cancellation.
4. The exact positive per-lag term `2eta(T)` in (3.4) is smaller than the
   unsigned collision/decorated coefficient unless a new combined lower
   bound is proved.  The phase-total `2n eta(T)` in (3.3) must likewise stay
   separate from `eta(B_k)`.

Thus a proof of (5.1), or even (4.2), must be a literal combined-channel,
combined-kind coefficient inequality.  The present first unproved
directional coefficient statement is

```text
(CCP)  sum_(j=1)^2 alpha_j {
         sum_u D_u Delta_u R_(j,y)
        +sum_(u<k/2)q_u Emb_u R_(j,y)} >=0           (5.2)
```

for every allowed `(k,y)`, with the terms exactly as in (2.2).  This is
merely (OS+) written at the critical-Borel/phase interface, not yet a proof
or a strict reduction.  A valid weaker repair would bound the negative part
of the left side in aggregate over `y` by `O(1/k)`, which is exactly the
directional form of (MS).

### A stronger monotonicity route to falsify

Because `D_u<0` and `q_u>0`, the following termwise statement would imply
`(CCP)`:

```text
(MON)
R_(k,y)(Phi_(j,u+1)) >= R_(k,y)(Phi_(j,u)),
R_(k,y)(Phi_(j,u))   >= R_(k,y)(Psi_(j,u))           (5.3)
```

for both `j=1,2`, every legal split, and every target lag.  This is a
genuine universal critical-Borel monotonicity claim, much stronger than the
needed combined coefficient inequality.  A capped exact `k=3,5` checker
will test (5.3), and will also record the four aggregate signed blocks
`J1-gradient`, `J1-embedding`, `J2-gradient`, and `J2-embedding`.  A finite
failure refutes only this termwise proof route, not `(OS+)` or `(MS)`.

### Minimally repaired channel statement

Return from the Abel expansion to the fully recombined conditional laws.
For `j=1,2`, define with the exact target normalization from Section 2

```text
CP_j(k,y):=(H_(j,B)-H_(j,A))(s ->
             2W_(k,y)(s)/(A_s pi_y)).                (5.4)
```

Equivalently, by M91's exact equality of measures,

```text
CP_j(k,y)=
 sum_u D_u[R_(k,y)(Phi_(j,u))-R_(k,y)(Phi_(j,u+1))]
 +sum_(u<k/2)q_u[R_(k,y)(Phi_(j,u))-R_(k,y)(Psi_(j,u))]. (5.5)
```

The definition is (5.4), not a license to sign the two pieces in (5.5).
The exact full score is

```text
z_k(y)=alpha_1 CP_1(k,y)+alpha_2 CP_2(k,y).          (5.6)
```

Hence the repaired sufficient statement is

```text
(CP)       CP_j(k,y)>=0
           for j=1,2, odd k>=3, 1<=y<=3k-3.         (5.7)
```

`(CP)` would prove `(OS+)`, hence `(MS)` and, with PCS, FCL1.  It is
strictly weaker than `(MON)` because it permits all gradient/embedding and
split cancellations within a channel, but it remains stronger than the
needed cross-channel inequality `(CCP)`.  It is now the first repaired
unproved sign lemma.

A direct monotone-coupling route would follow from the stronger scalar
stochastic order

```text
(FOSD)  H_(j,B)[R_(k,y)>=a] >= H_(j,A)[R_(k,y)>=a]   (5.8)
```

for every real threshold `a`, both channels, and every allowed `(k,y)`.
On a finite response space this is equivalent to the existence of a
coupling with `R_(k,y)(S_B)>=R_(k,y)(S_A)` almost surely, and hence implies
`CP_j>=0`.  This exact universal order is now fixed for a capped `k=3,5`
falsifier.  Its failure would rule out response-monotone coupling while
leaving the mean inequality `(CP)` open.

## 6. Fully recombined coefficient check and exact firewalls

Put

```text
g_(k,y)(s)=2W_(k,y)(s)/(A_s pi_y).
```

Let `nu_C` be the first-transposition law in a uniform minimal
factorization of a directed cycle `C`, and let `N_Q(e,f)` be M91's exact
ordered first-two-factor probability in a residual permutation `Q`.  Direct
substitution of the normalized channel laws, with no Abel expansion, gives

```text
CP_1(k,y)=
 sum_(e in T(L))nu_L(e) sum_(f in T(M))nu_M(f)g_(k,y)(ef)
 -1/2 sum_(C in {C_-,C_+}) sum_(e in T(C))nu_C(e)
       sum_(f in T(M))nu_M(f)g_(k,y)(ef),            (6.1)

CP_2(k,y)=
 sum_(e in T(L))sum_(f in T(eL))N_L(e,f)g_(k,y)(ef)
 -sum_(C in {C_-,C_+})sum_(e in T(C))
       sum_(f in T(e C_- C_+))N_(C_-C_+)(e,f)g_(k,y)(ef). (6.2)
```

In the last line, the fair choice of the first exterior component is already
inside `N_(C_-C_+)`, exactly as in M91; no extra factor `1/2` is allowed.
Equations (6.1)--(6.2) are the requested direct fully recombined coefficient
formulas.  They include all phases, kinds, collisions, and completion
weights.

There is no atomwise-positive factorization.  For every odd `k>=3`, take

```text
e_+=(1,2k),       e_-=(0,1),       f_M=(k,k+1).
```

The chord `e_+` is internal to the merged exterior cycle `L` and to neither
separate exterior cycle, whereas `e_-` is internal to `C_-` and absent from
`L`.  Thus the channel-one signed atom coefficients of `(e_+,f_M)` and
`(e_-,f_M)` are respectively strictly positive and strictly negative at
every rank.  For channel two, after `e_+` cuts `L`, and after `e_-` cuts
`C_-`, the edge `f=(1,2)` is internal to a remaining `(k-1)`-cycle.
Therefore the ordered atoms `(e_+,f)` and `(e_-,f)` likewise have strictly
positive and strictly negative coefficients in (6.2).  This is an exact
arbitrary-rank obstruction to proving `(CP)` by signing raw atoms.

The response-monotone coupling route is also false.  At `k=3`, channel one,
`y=1`, the exact upper-tail threshold

```text
a=343359/268912
```

has

```text
H_(1,B)[g_(k,y)>=a]-H_(1,A)[g_(k,y)>=a]=-32/375<0.  (6.3)
```

Thus `(FOSD)` fails, so no coupling of these two scalar response laws can
have the B response above the A response almost surely.  This does not
refute their mean inequality `(CP_1)`.

The earlier termwise route `(MON)` fails too.  The exact capped checker finds
4 violations at `k=3` and 46 at `k=5`; the latter split into 32 adjacent and
14 embedding violations.  The first `k=3` embedding failure is

```text
R_(3,2)(Phi_(1,1))-R_(3,2)(Psi_(1,1))
 =-876877452441/14123762450000.                      (6.4)
```

Nevertheless, all 18 capped lags have both channel-combined values `CP_j`
positive (36 channel values total).  The smallest **weighted** values
`alpha_j CP_j` are

```text
k=3, j=1: 29326617178443/882735153125000,
k=3, j=2: 288372901815351/3530940612500000,

k=5, j=1:
469380953030255528575240193615921483304253622141733093283
/62593163860600167157006651607817304625660070187459136716800,

k=5, j=2:
12355546254704689070281046180638277338919762446656677440681
/751117966327202005884079819293807655507920842249509640601600.
```

These are exact finite facts only.  M272's full monotone-split path coupling
also gives only the expectation identity: the target response is not
monotone under a single adjacent chord extension, and the channel-two
second-factor coupling may change `T/D` kind.  Thus neither monotone split,
atom signs, nor scalar stochastic order proves `(CP)`.

## 7. Exact stop and hierarchy

The analytic attempt closes no universal sign estimate.  The surviving
hierarchy, from strongest to weakest, is

```text
(CP_1 and CP_2 nonnegative pointwise)
        => (OS+: every z_k(y)>=0)
        => (MS: k min(P_k,N_k)=O(1))
        <=> FCL1, given proved PCS.                  (7.1)
```

`(MON)` and `(FOSD)` are refuted.  Raw atomwise positivity is refuted at
every odd rank.  The first open analytic lemma is `(CP)` in its direct
coefficient form (6.1)--(6.2); if channel positivity itself fails later,
the minimally repaired statement is the cross-channel negative-mass bound
`(MS)`, not a return to separately absolute Abel pieces.

No FCL1, other cell, direct L1, H0, bridge gap, local identity-heat-bath
mixing, or Terminal conclusion is proved here.
