# M186 exact component Borel--Abel reduction

Date: 2026-08-13 UTC.

Status: Propositions 1--4 are **proved**. The full prefix response `(PCR)`
and hence `(SCBR)`, `(BIR)`, `(BR)`, and PCS-bound remain **unresolved**.

## 1. Setting and accepted input

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Put `n=3k`, odd `k>=3`,

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

This concerns M73's nonlazy cyclic rank-two coordinate kernel under the
uniform law on minimal length-`n-1` factorizations of `h`. It is not the
global identity bridge or the lazy `{3,4,5}` heat-bath chain.

M180/M182 define the complete signed first-row law `eta=P_B-P_A`, already
combining the two noncommon M91 channels, and the component coefficients

```text
M_r(d)=sum_s eta(s)N_r(d;s),             r in {1,2}, (1.1)
```

where `N_r(d;s)` counts size-`d` residual components of ambient run type
`r`. They prove

```text
eta(Q)=sum_d[M_1(d)u_1(d)+M_2(d)u_2(d)],             (1.2)
```

and reduce `(BR)` to `(SCBR)`, the same sum restricted to `d<=n/2` being
`O(1/n)`. All predecessor checksum manifests named in the M186 plan passed
before this proof was written.

## 2. Closed critical-Borel chord formula

Let

```text
M=(k,k+1,...,2k-1),
C_-=(0,1,...,k-1),
C_+=(2k,2k+1,...,3k-1),
F=C_- C_+,
L=(1,...,k-1,2k,...,3k-1).
```

Thus `F` is A's exterior two-cycle permutation, `L` is B's exterior
`(2k-1)`-cycle, and `M` is common. For a minimal residual permutation `R`
of transposition rank `r(R)`, define on its internal transpositions

```text
lambda_R(e)=F_(r(R)-1)(eR)/F_(r(R))(R),
Lambda_R(e,f)=F_(r(R)-2)(feR)/F_(r(R))(R).           (2.1)
```

The second law is on ordered admissible pairs: after the displayed factors
`e,f`, the remaining residual is `(ef)^-1R=feR`. Both laws normalize to one.

They are closed critical-Borel products. Write `b_j=e^-j tau(j)`. If an
edge of `L` cuts it into sizes `a,D-a`, `D=2k-1`, then

```text
lambda_L(e)=b_a b_(D-a)/[(D-1)b_D].                 (2.2)
```

If an edge of `F` cuts one `k`-cycle into `a,k-a`, then

```text
lambda_F(e)=b_a b_(k-a)/[2(k-1)b_k].                (2.3)
```

For the common cycle,

```text
lambda_M(e)=b_a b_(k-a)/[(k-1)b_k].                 (2.4)
```

If the positive source-residual sizes after an admissible ordered pair are
`x_1,...,x_l`, factorial cancellation gives

```text
Lambda_L(e,f)=product_i b_(x_i)/[(D-1)(D-2)b_D],
Lambda_F(e,f)=product_i b_(x_i)/[(2k-2)(2k-3)b_k^2]. (2.5)
```

Every shared-endpoint triangle, same-run or cross-run double, and
small-component collision is present literally in (2.5).

For an ordered pair put

```text
chi_(r,d)(e,f)=N_r(d;ef),                            (2.6)
```

where the components are those of `(ef)^-1h`, not those of the source
residual in (2.5).

### Proposition 1 (proved: complete component coefficient)

With M91's exact channel masses `alpha_1,alpha_2`, one has

```text
M_r(d)=alpha_1 {
  sum_(e in L,f in M)lambda_L(e)lambda_M(f)chi_(r,d)(e,f)
 -sum_(e in F,f in M)lambda_F(e)lambda_M(f)chi_(r,d)(e,f)}

 +alpha_2 {
  sum_(e,f)Lambda_L(e,f)chi_(r,d)(e,f)
 -sum_(e,f)Lambda_F(e,f)chi_(r,d)(e,f)}.             (CB)
```

No absolute value occurs in `(CB)`.

#### Proof

M91's channel `J=1` has one exterior and one middle factor. Their source
supports are disjoint, so the product is independent of their color order;
conditional component factorizations give the product measures in the first
braces. Channel `J=2` is precisely the first two ordered factors of `L` for
B and of `F` for A, giving the second braces. The common `J=0` law is the
same first-two-factor law of `M` and cancels. Applying the component-count
test (2.6) proves `(CB)`. Equations (2.2)--(2.5) follow by substituting
`F_r=r! product tau(d_i)` into (2.1); all exponentials cancel because source
component sizes have the same total. QED.

This is already a finite critical-Borel formula for every `M_r(d)`. It has
only `O(n^4)` displayed chord terms conceptually, but no quotient matrix,
target shell, continuum replacement, or deleted collision face.

## 3. Exact component-valued Abel form

For a first exterior edge, let `s` be its smaller split in its source cycle.
Its marginal under `lambda_L` is M91's `p_s`, `1<=s<=k-1`; its marginal
under `lambda_F` is `q_s`, `1<=s<k/2`, extended by zero. Put

```text
D_u=sum_(s<=u)(p_s-q_s),              D_(k-1)=0.     (3.1)
```

For `j=1,2`, `r=1,2`, define the normalized finite profiles

```text
phi_(j,s;r,d)=E_B[N_r(d;ef) | J=j, first exterior split=s],
psi_(j,s;r,d)=E_A[N_r(d;ef) | J=j, first exterior split=s]. (3.2)
```

The expectations in (3.2) are exactly the chord sums in `(CB)` restricted
to the displayed first split. They retain the complete ordered pair before
applying `N_r`.

### Proposition 2 (proved: closed Borel--Abel coefficient)

For every `r,d`,

```text
M_r(d)=sum_(j=1)^2 alpha_j {
  sum_(u=1)^(k-2)D_u[
       phi_(j,u;r,d)-phi_(j,u+1;r,d)]
 +sum_(s<k/2)q_s[
       phi_(j,s;r,d)-psi_(j,s;r,d)]}.                (BA-C)
```

#### Proof

Disintegrating `(CB)` by the first smaller split gives

```text
H_(j,B)(N_r(d))=sum_s p_s phi_(j,s;r,d),
H_(j,A)(N_r(d))=sum_s q_s psi_(j,s;r,d).
```

Add and subtract `sum_s q_s phi_(j,s;r,d)`. Apply ordinary discrete
summation by parts to `p_s-q_s=D_s-D_(s-1)`, using `D_0=D_(k-1)=0`, then
sum the two channels with their signs. This gives `(BA-C)`. QED.

Equation `(BA-C)` is the requested exact one-dimensional coefficient law:
both channels are outside neither the Abel sum nor the embedding defect;
they meet in `M_r(d)` before any later estimate.

## 4. The complete `J=1` face collapse

For a chord in a directed `d`-cycle whose two source arcs have sizes
`a,d-a`, write its per-chord probability as

```text
nu_d(a)=(d-2)! tau(a)tau(d-a)/d^(d-2)
       =b_a b_(d-a)/[(d-1)b_d].                     (4.1)
```

For a chord within a contiguous ambient `k`-block, let `a` be the ordinary
linear separation of its endpoints. There are `k-a` such chords, so the
middle and A-exterior face law is

```text
rho_A(a)=(k-a)nu_k(a),                 1<=a<k.       (4.2)
```

For B's two-run cycle `L`, let `a` be the ambient face cut off away from
the middle block `M`. A same-run chord of linear separation `a` has source
split `a`; a cross-run chord has source split `a-1`. The exact counts are

```text
S_k(a)=(k-1-a)_+ +(k-a)_+,

C_k(a)=a-1,             2<=a<=k,
       =2k-a,            k<a<=2k-1,
       =0                otherwise.                 (4.3)
```

Consequently

```text
rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1),  (4.4)
```

with invalid indices zero. Literal chord classification, or summing (2.2),
shows `sum rho_A=sum rho_B=1`.

Every `J=1` product is a double. If the exterior chord is same-run it is a
separated double; if it is cross-run it is nested around the middle chord.
In both cases the residual component data are

```text
(one run,a), (one run,b), (two runs,n-a-b),          (4.5)
```

where `a~rho_B` or `rho_A` and independently `b~rho_A`.

### Proposition 3 (proved: exact `J=1` coefficients and scale)

Before multiplication by `alpha_1`, the conditional signed coefficients are

```text
M_1^(1)(d)=rho_B(d)-rho_A(d),

M_2^(1)(d)=sum_(a+b=n-d)
             [rho_B(a)-rho_A(a)]rho_A(b).            (4.6)
```

Moreover,

```text
sum_a |rho_B(a)-rho_A(a)|/a=O(1/k),                 (4.7)

sum_(a,b) |rho_B(a)-rho_A(a)|rho_A(b)/(n-a-b)
 =O(1/k).                                            (4.8)
```

Thus the conditional channel-1 charge itself is `O(1/k)`.

#### Proof

Equation (4.6) is (4.5), with the common `b`-component canceling from the
one-run coefficient. For the bounds, standard Stirling inequalities with a
uniform remainder imply, for `1<=a<=m/2`,

```text
nu_m(a)<=C b_a/m,
|m nu_m(a)-b_a|<=C(a/m)b_a.                         (4.9)
```

Indeed `m nu_m(a)=m/(m-1)b_a b_(m-a)/b_m`, and uniform Stirling gives
`b_(m-a)/b_m=1+O(a/m)` in this range. Also
`b_(a-1)<=C b_a` for `a>=2`.

For `a<=k/2`, insert (4.2)--(4.4) and use (4.9). Since

```text
S_k(a)=2k-1-2a,
```

the leading multipliers `1-a/k` and `1-2a/(2k-1)` agree up to
`O(a/k^2)`. Hence

```text
|rho_B(a)-rho_A(a)|
 <=C a[b_a+b_(a-1)]/k.                              (4.10)
```

After division by `a`, (4.10) sums to `O(1/k)`. On `a>k/2`, use
`1/a<=2/k` and the total variation bound `sum|rho_B-rho_A|<=2`. This proves
(4.7).

For (4.8), first take `a<=k`. Since `b<=k-1`, the denominator is at least
`k+1`, so this part is `O(1/k)`. For `a>k`, put `c=2k-a`. Equations
(4.3)--(4.4) give the exact tail identity

```text
rho_B(2k-c)=c nu_(2k-1)(c),          1<=c<=k-1.      (4.11)
```

Put `r=k-b`. Then `rho_A(k-r)=r nu_k(r)` and these values sum to one.
Therefore

```text
sum_b rho_A(b)/(n-(2k-c)-b)
 =sum_r r nu_k(r)/(c+r)<=1/c.
```

The tail in (4.8) is at most `sum_(c<k)nu_(2k-1)(c)=O(1/k)` by (4.9).
Finally M180's sharp centers give `|u_r(d)|<=C/d`; combining (4.6)--(4.8)
proves the charge statement. QED.

This proposition is a genuine asymptotic step, but it is **not** used to
take an absolute value across the two channels. The final obligation below
always uses their fully combined coefficients from `(CB)` or `(BA-C)`.

## 5. Exact signed summation by parts

Let

```text
m=floor(n/2)=(n-1)/2,
P_d=M_1(d),                    N_d=M_1(d)+M_2(d).     (5.1)
```

A two-run component has size at least two. For `d>=2`, put

```text
r_d=u_1(d)-u_2(d)=e tau(d-1)/tau(d)-1.               (5.2)
```

Then the full, channel-combined small charge is exactly

```text
S_k=M_1(1)u_1(1)
    +sum_(d=2)^m[N_d u_2(d)+P_d r_d].                (5.3)
```

Define the fully combined prefixes

```text
A_D=sum_(d=2)^D N_d,
C_D=sum_(d=2)^D P_d.                                 (5.4)
```

### Proposition 4 (proved: prefix reduction and first boundary)

One has the exact identity

```text
S_k=M_1(1)u_1(1)+A_m u_2(m)+C_m r_m
 +sum_(d=2)^(m-1){
    A_d[u_2(d)-u_2(d+1)]
   +C_d[r_d-r_(d+1)]}.                               (SBP)
```

Furthermore

```text
M_1(1)=O(1/n).                                       (5.5)
```

Consequently `(SCBR)` follows from the strictly coefficient-level lemma

> **PREFIX COMPONENT RESPONSE `(PCR)` (unresolved).** There is an absolute
> `C` such that, for every odd `k>=3` and `2<=D<=m`,
>
> ```text
> |A_D|+|C_D|<=C sqrt(D)/n.                           (PCR)
> ```

The weaker weighted-prefix condition

```text
n[(|A_m|+|C_m|)/m
  +sum_(d=2)^(m-1)(|A_d|+|C_d|)/d^2]=O(1)           (WPCR)
```

also suffices.

#### Proof

Equation (5.3) uses `u_1=u_2+r` for `d>=2`; ordinary Abel summation gives
`(SBP)`.

For (5.5), let `W(s)` be M180's ordered-lift boundary incidence. On a double,
each one-run singleton is exactly a boundary factor, so `N_1(1;s)=W(s)`.
On a triangle, every support edge occurs in two of its three ordered lifts,
so `W(s)=2N_1(1;s)/3`. Therefore

```text
M_1(1)=eta(W)+(1/2)eta(W 1_T).                       (5.6)
```

M180's exact row identity gives

```text
eta(W)=2/(n-3)[H(B)-H(A)]
       =2/(n-3)[U_2(2k-1)-2U_1(k)].                 (5.7)
```

The sharp centers make the bracket in (5.7) uniformly bounded. Also
`0<=W<=2`, and the triangle probability under either source is `O(1/k)`:
in the common `J=0` channel it is `3/k`, in `J=1` it is zero, and in `J=2`
it is `3/(2k-1)` for B and at most `3/k` for A. Hence the second term in
(5.6) is `O(1/k)`, proving (5.5).

Finally the same ratio expansions used by M180 give, uniformly for `d>=2`,

```text
|u_2(d)|+|r_d|<=C/d,
|u_2(d)-u_2(d+1)|+|r_d-r_(d+1)|<=C/d^2.             (5.8)
```

Substituting `(PCR)` in `(SBP)` and using
`sum d^(-3/2)<infinity` proves `S_k=O(1/n)`. Substitution of `(WPCR)` and
(5.8) does the same. QED.

`(PCR)` is a signed Kolmogorov-type bound on two already channel-, kind-,
and collision-combined component measures. It contains no Cayley-ratio
weights and no target observable. It is strictly more explicit and directly
falsifiable through `(CB)`/`(BA-C)`, but it is not proved here.

## 6. Exact finite calibration and limitations

`component_abel_check.py` constructs the literal source rows and separately
constructs the critical-Borel chord laws, then checks `(CB)`, `(BA-C)`, (4.6), and
`(SBP)` coefficientwise over `Fraction`. It is capped at `k=3,5`.

The channel masses are

```text
k=3: (alpha_0,alpha_1,alpha_2)=(1/15,8/15,2/5),
k=5: (alpha_0,alpha_1,alpha_2)=(1/11,16/33,14/33).
```

The diagnostic maxima

```text
max_(2<=D<=n/2) n/sqrt(D) max(|A_D|,|C_D|)
```

are `2.78720` and `1.64136`. These two values merely fail to falsify the
scale in `(PCR)`; they imply no uniform constant, sign, or asymptotic law.
The corresponding `k` times the two channel-1 weighted face sums in
(4.7)--(4.8) are `1.93872` and `1.46711`, also calibration only.

This mission proves no `(PCR)`, `(SCBR)`, `(BIR)`, `(BR)`, PCS-bound,
FD-bound, FCL1, direct-L1, H0/gap, mixing, or Terminal claim. It neither
uses nor launches a broad quotient computation and makes no inference from
finite signs.
