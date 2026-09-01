# Exact phase-boundary reduction for the fixed-cell FD obligation

Date: 2026-08-14 UTC.

Status: Propositions 1--4 below are **proved** exact identities. The final
phase-boundary variation estimate `(PBV)` is **unresolved**. No finite
diagnostic was used in deriving these identities.

## 1. Scope and accepted phase law

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Put `n=3k`, with odd `k>=3`,

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k),
E_r=(r,r+1)                    (indices modulo n).
```

The target is only the uniform law on minimal length-`n-1` transposition
factorizations of `h` under M73's nonlazy cyclic rank-two kernel. For a
supported rank-two product `s`, put

```text
q_s=s^-1 h,
A_s=F_(n-3)(q_s),
C_g(s)=F_(n-5)((gs)^-1 h),
a(s)=3 for a triangle and 2 for a double,
omega(s)=a(s)[C_B(s)/A_B-C_A(s)/A_A].                (1.1)
```

Thus `omega=P_B-P_A` is the complete signed first-pair product law, with both
triangle and double kinds. For `2<=ell<=n-2`, define the literal fixed-phase
response

```text
R_ell(s)=A_s^-1 sum_(r mod n)
             F_(n-5)(E_r E_(r+ell) q_s).             (1.2)
```

Let `F_T=F_(n-3)(E_0E_2 h)` in the accepted M161 notation and

```text
Lambda_n=n^(n-2)/(n F_T)
        =(n-2)(1-2/n)^(-(n-3)).                      (1.3)
```

M161/M166's exact raw convolution specializes pointwise to

```text
z_k(y)=Lambda_n sum_s omega(s) R_(y+1)(s),
                                      1<=y<=n-3.     (1.4)
```

The sum in (1.4) is signed before any absolute value.

## 2. Exact circular coefficient formula

Let `C_1,C_2,C_3` be the residual cycles of `q_s`, with sizes `d_i`. Define
the generic-edge indicator

```text
chi_i^s(r)=1[s(r+1)=r+1 and r belongs to C_i].        (2.1)
```

The identity `q_s(r)=s^-1(r+1)=r+1` shows that these, and only these,
boundary edges are directed adjacent edges of a residual cycle. Put, with an
invalid shifted size interpreted as zero,

```text
kappa_ii(s)=tau(d_i-2)/tau(d_i),
kappa_ij(s)=tau(d_i-1)tau(d_j-1)/[tau(d_i)tau(d_j)]
                                                   (i!=j),
C_ij^s(ell)=sum_(r mod n) chi_i^s(r)chi_j^s(r+ell),
R_n=(n-3)(n-4).                                      (2.2)
```

### Proposition 1 (proved: exact all-kind phase coefficient)

For every supported triangle or double `s` and every `2<=ell<=n-2`,

```text
R_ell(s)=R_n^-1 sum_(i,j=1)^3 kappa_ij(s) C_ij^s(ell). (2.3)
```

#### Proof

The two polygon edges are disjoint in the displayed lag range. A nonzero
completion requires both to be generic. If their residual owners agree, the
two directed cycle edges isolate two singleton tails and replace size `d_i`
by `(1,1,d_i-2)`. If their owners are `i!=j`, they replace `(d_i,d_j)` by
`(1,d_i-1,1,d_j-1)`. Dividing the corresponding completion product by
`A_s=(n-3)! product_i tau(d_i)` gives respectively the two coefficients in
(2.2), together with `(n-5)!/(n-3)!=R_n^-1`. Ordered `(i,j)` retains both
cross-component orientations. This partitions every nonzero `IS`, `IN`, and
`X` term, while the outer `s`-sum in (1.4) retains both intermediate kinds.
QED.

For a residual component made from one ambient `h`-run, `chi_i` is one
interval of boundary tails. For the unique two-run component of a double it
is a union of two intervals. This statement includes empty intervals when a
run has size one.

## 3. Exact endpoint derivative and channel law

Define the discrete jump

```text
partial chi_j^s(x)=chi_j^s(x+1)-chi_j^s(x)           (3.1)
```

and, for `2<=ell<=n-3`, the bounded endpoint observable

```text
E_ell(s)=sum_(i,j) kappa_ij(s)
          sum_(x mod n) chi_i^s(x-ell) partial chi_j^s(x).  (3.2)
```

### Proposition 2 (proved: endpoint derivative)

One has exactly

```text
R_(ell+1)(s)-R_ell(s)=E_ell(s)/R_n,                  (3.3)
|E_ell(s)|<=8.                                       (3.4)
```

#### Proof

Subtract adjacent circular correlations in (2.3):

```text
C_ij(ell+1)-C_ij(ell)
 =sum_r chi_i(r)[chi_j(r+ell+1)-chi_j(r+ell)]
 =sum_x chi_i(x-ell) partial chi_j(x).
```

This is (3.3). Each rooted-tree ratio `kappa_ij` lies in `[0,1]`. At a fixed
jump position, at most one `chi_i(x-ell)` is nonzero. A triangle has three
one-run components and hence at most six jumps in total. A double has two
one-run components and one two-run component and hence at most eight. Taking
absolute values only for this pointwise deterministic bound proves (3.4).
QED.

M91's exact source decomposition is

```text
omega=alpha_1(H_(1,B)-H_(1,A))
     +alpha_2(H_(2,B)-H_(2,A)),                      (3.5)
```

where each `H` is a normalized ordered-factor law and includes its literal
triangle/double mixture. Applying (3.5) to (3.2), then the accepted
measure-valued Abel law, gives

```text
z_k(y+1)-z_k(y)=Lambda_n/R_n
 [alpha_1 Xi_(1,y+1)+alpha_2 Xi_(2,y+1)],             (3.6)

Xi_(j,ell)
 =sum_(u=1)^(k-2) D_u[
      Phi_(j,u)(E_ell)-Phi_(j,u+1)(E_ell)]
  +sum_(u<k/2) q_u[
      Phi_(j,u)(E_ell)-Psi_(j,u)(E_ell)].             (3.7)
```

The two channels and both kinds are combined inside the absolute value in
the next proposition. No phase is averaged away: `ell` remains the literal
cyclic displacement, and (3.2) retains both the positive and negative jump
endpoints of every one-run/two-run component.

### Proposition 3 (proved: exact FD equivalence)

Since

```text
k^2 Lambda_n/R_n = Theta(n)                          (3.8)
```

uniformly for odd `k>=3`, M168's independent fixed-difference obligation is
equivalent to the following standalone endpoint coefficient estimate:

> **Phase-boundary variation `(PBV)` (unresolved).** There is an absolute
> constant `C` such that, for every odd `k>=3`,
>
> ```text
> sum_(ell=2)^(n-3)
>  |alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)| <= C/n.    (PBV)
> ```

#### Proof

Sum the absolute value of (3.6) over `y=1,...,n-4` and multiply by `k^2`.
Equation (1.3), `n=3k`, and `R_n=(n-3)(n-4)` show that the positive scalar
in (3.8) is bounded above and below by absolute multiples of `n`. Thus
`FD-bound` and `(PBV)` imply each other. QED.

`(PBV)` is the first unresolved step. It is a signed `l1` estimate for a
uniformly bounded endpoint-incidence observable, not for the original
length-`Theta(n)` circular correlations. Proving it still requires the full
two-channel coefficient cancellation: the pointwise bound (3.4) and the
known `Theta(sqrt(k))` Abel coefficient mass do not suffice separately.

## 4. Pointwise affine/collision separation

Let

```text
b_s(r)=1- sum_i chi_i^s(r)
      =1[r+1 belongs to supp(s)],
I_ell(s)=sum_(r mod n)b_s(r)b_s(r+ell),               (4.1)
rho_ij(s)=e^2 kappa_ij(s)-1,
Q_ell(s)=sum_(i,j)rho_ij(s)C_ij^s(ell).               (4.2)
```

Thus `I_ell` counts ordered pairs of moved vertices at literal cyclic
displacement `ell`. It is a sparse collision profile: its complete support
over `ell` has size at most `12` for a triangle and `24` for a double
(the crude ordered-pair bounds suffice here).

### Proposition 4 (proved: exact pointwise affine separation)

For `2<=ell<=n-2`,

```text
e^2 R_n R_ell(s)
 =n-8+2 1[kind(s)=T]+I_ell(s)+Q_ell(s),               (4.3)

z_k(ell-1)=Lambda_n e^-2/R_n [
  2 eta(T)+eta(I_ell)+eta(Q_ell)],                    (4.4)
```

where `eta=P_B-P_A` is still the complete two-channel signed law. Moreover,
for `2<=ell<=n-3`,

```text
e^2 E_ell(s)
 =[I_(ell+1)(s)-I_ell(s)]
  +[Q_(ell+1)(s)-Q_ell(s)].                           (4.5)
```

#### Proof

Summing `C_ij` over the residual owners removes the owner labels:

```text
sum_(i,j)C_ij(ell)
 =sum_r (1-b_s(r))(1-b_s(r+ell))
 =n-2|supp(s)|+I_ell(s).
```

A triangle moves three vertices and a double moves four, giving
`n-8+2 1_T+I_ell`. Now write `e^2 kappa_ij=1+rho_ij` in (2.3), proving
(4.3). Apply the centered signed law `eta`, for which `eta(1)=0`, and use
(1.4) to obtain (4.4). Finally subtract (4.3) at adjacent lags and compare
with (3.3), proving (4.5). QED.

The accepted kind transfer is

```text
eta(T)=12(k-1)/[3k(3k-4)(2k-1)]>0.                   (4.6)
```

Thus a minority-sign proof could equivalently show that the collision plus
decorated remainder in (4.4) has only uniformly bounded negative mass after
the exact positive baseline (4.6) is included. The FD route is independent:
its exact remaining coefficient is

```text
sum_(ell=2)^(n-3)|eta(Delta I_ell+Delta Q_ell)|=O(1/n). (4.7)
```

No triangle inequality between `Delta I` and `Delta Q`, between channels,
or between kinds is asserted; (4.7) retains all cancellations.

## 5. Scope firewall

No full DV, PCS-to-FCL1 inference, sign theorem, FD estimate, FCL1, other
fixed cell, direct L1, H0, gap, mixing, or Terminal result is asserted here.
