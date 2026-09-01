# Exact fixed-cell posterior convolution

Date: 2026-08-13.

Status: the identities in Sections 1--3 are exact specializations of the
accepted M73/M91/M94 formulas.  No asymptotic bound is claimed yet.

## 1. Target cell and normalization

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
Put `n=3k`, with odd `k>=3`, and `h=(0 1 ... n-1)`.  For
`1<=y<=n-3`, put `w=n-2-y` and

```text
t_y=(0,1)(1+y,2+y).
```

This is the separated colored composition `(1,y,1,w;S)`.  Its complement
`t_y^-1 h` has cycle sizes `(1,1,n-2)`, independently of `y`.  If `O_y` is
its orbit under `theta(g)=h^-1 g h`, then `|O_y|=n` and

```text
pi_y:=bar pi(O_y)
 =2n(n-3)! tau(n-2)/n^(n-2)
 =2n c_n b_1^2 b_(n-2),                              (1.1)
```

where `tau(d)=d^(d-1)/d!`, `b_d=e^-d tau(d)`, and
`c_n=(n-3)!e^n/n^(n-2)`.  The equality `O_y=O_w` explains the intentional
double appearance of an orbit when `y` runs through the full cell.

Let

```text
eta_k=bar K(O_B,.)-bar K(O_A,.),
z_k(y)=[bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/pi_y.
```

Then, exactly,

```text
z_k(y)=sum_(O_s) eta_k(O_s) L_y(O_s),
L_y(O_s)=bar K(O_s,O_y)/pi_y,                         (1.2)

A_k(1,1)=1/(n-3) sum_(y=1)^(n-3) k^2 |z_k(y)|.       (1.3)
```

Thus the only absolute values occur after the complete signed intermediate
sum.

## 2. Literal target-response convolution

For an intermediate raw state `s`, let `q_s=s^-1h` have three cycles
`C_1,C_2,C_3`, sizes `d_i`, and ranks `r_i=d_i-1`; put
`R_n=(n-3)(n-4)`.  For a directed cycle `C` and a chord `e` whose endpoints
lie in `C`, let `cut_C(e)=(u,d-u)` be the two cycle sizes after left
multiplication by `e`, and define

```text
nu_C(e)=(d-2)! tau(u)tau(d-u)/d^(d-2).                (2.1)
```

For two disjoint chords `e,f` in `C`, let `cut_C(e,f)` be the three cycle
sizes after left multiplication by `ef`; set

```text
mu_C(e,f)=2(d-3)! product_(v in cut_C(e,f))tau(v)/d^(d-2)   (2.2)
```

when the transposition rank falls by two, and zero otherwise.  The factor
two is the literal ordered-pair lift multiplicity of a double.  Split (2.2)
as `mu_C^S+mu_C^N` according to whether the chord endpoints are separated or
nested in the cyclic order of `C`.

For a phase `r in Z/nZ`, write

```text
e_r=(r,r+1),             f_(r,y)=(r+y+1,r+y+2).
```

M73's four-schema row identity gives the exact scalar response

```text
bar K(O_s,O_y)=P_y^S(s)+P_y^N(s)+P_y^X(s),            (2.3)
```

where

```text
P_y^c(s)=sum_(r mod n) sum_i
  r_i(r_i-1)/R_n * 1[{e_r,f_(r,y)} subset C_i]
  * mu_(C_i)^c(e_r,f_(r,y)),                 c in {S,N},

P_y^X(s)=sum_(r mod n) sum_(i<j) 2r_i r_j/R_n * [
  1[e_r subset C_i, f_(r,y) subset C_j] nu_(C_i)(e_r)nu_(C_j)(f_(r,y))
 +1[e_r subset C_j, f_(r,y) subset C_i] nu_(C_j)(e_r)nu_(C_i)(f_(r,y))].
                                                               (2.4)
```

Here `e subset C` means both endpoints lie in the cycle.  Formula (2.4)
already sums the complete target orbit, and (2.1)--(2.2) are finite Borel
convolutions in the cut sizes.  It includes both same-component double
schemas `IS,IN` and the cross-component schema `X`; inadmissible crossings
are zeros rather than discarded error terms.  The intermediate `s` itself
may be a triangle or either double color, so all collision and lower-support
strata remain present in (1.2).

Put `E_r=(r,r+1)` and
`N_i(r)=1[E_r subset C_i]nu_(C_i)(E_r)`.  Then the cross-component term is
the literal circular correlation

```text
P_y^X(s)=sum_(i!=j) 2r_i r_j/R_n
                    sum_(r mod n)N_i(r)N_j(r+y+1).    (2.5)
```

For `c in {S,N}`, put
`M_i^c(r,l)=1[{E_r,E_(r+l)} subset C_i]
mu_(C_i)^c(E_r,E_(r+l))`.  The same-component terms are the lag slices

```text
P_y^c(s)=sum_i r_i(r_i-1)/R_n
               sum_(r mod n)M_i^c(r,y+1).             (2.6)
```

Equations (2.5)--(2.6) are the reduced exact convolution in `y`.  Reversing
the unordered target-edge pair proves

```text
z_k(y)=z_k(n-2-y).                                   (2.7)
```

No quotient matrix is needed to evaluate these correlations.

## 3. Two-channel Borel--Abel specialization

Retain M91's normalized split laws

```text
p_u=b_u b_(2k-1-u)/[(1-1/(2k-1))b_(2k-1)],
q_u=b_u b_(k-u)/[(1-1/k)b_k]             (u<k/2),
q_u=0                                     (u>k/2),
D_u=sum_(v<=u)(p_v-q_v),

alpha_1=4(k-1)^2/[3(k-1)(3k-4)],
alpha_2=2(k-1)(2k-3)/[3(k-1)(3k-4)].                 (3.1)
```

Let `Phi_(j,u),Psi_(j,u)` be M91's literal normalized conditional
intermediate laws for channels `j=1,2`.  For any such law `rho`, define the
complete fixed-cell response

```text
R_(k,y)(rho)=E_(s~rho)[(P_y^S(s)+P_y^N(s)+P_y^X(s))/pi_y].    (3.2)
```

Substitution in M91's measure-valued Abel identity yields the reduced exact
convolution

```text
z_k(y)=sum_(j=1)^2 alpha_j {
  sum_(u=1)^(k-2) D_u[
    R_(k,y)(Phi_(j,u))-R_(k,y)(Phi_(j,u+1))]
 +sum_(u<k/2) q_u[
    R_(k,y)(Phi_(j,u))-R_(k,y)(Psi_(j,u))] }.         (3.3)
```

The two channels are added before the absolute value in (1.3).  Equations
(2.1)--(2.4) give every scalar response in (3.3) as an explicit finite
convolution of conditioned-Borel cut weights and the phase displacement
`y`.  In particular, no generic bulk limit, triangle bound, or deletion of a
small-component layer occurs.

## 4. First unresolved scalar bound

Let `Z_k(y)=kz_k(y)`.  By (1.3), boundedness of the first cell is exactly
the scalar convolution estimate

```text
sum_(y=1)^(n-3)|Z_k(y)|=O(1).                         (FCL1)
```

This is unresolved.  Exact checks at `k=3,5,7` find every score positive,
verify (2.7), and give respectively

```text
A_k(1,1)=1.560166409446641,
           1.013460499098716,
           0.847617928778357.
```

These are exact finite rational values, not an asymptotic theorem.
