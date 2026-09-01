# M174 proof: exact PC response and boundary-coefficient reduction

Date: 2026-08-13 UTC.

Status: Propositions 1--4 are **proved**. The final scalar bound `(BR)` is
**unresolved**. Accordingly `(PCS-bound)` remains unresolved. This note is
only about the first fixed boundary cell for the accepted M73 nonlazy cyclic
rank-two quotient kernel.

## 1. Target, convention, and exact event form

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Let `n=3k`, with odd `k>=3`,

```text
h=(0 1 ... n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

Let `P_g` be the law of the product `s` of the first two factors in a uniform
minimal factorization of `g^-1 h`. In M168 notation,

```text
P_g(s)=a(s) C_g(s)/A_g,
f_k(s)=S(s)/A_s,
```

where `a(s)=3` for an oriented triangle, `a(s)=2` for a double,
`A_s=F_(n-3)(s^-1h)`, and `S(s)` is the exact all-phase PC moment.

### Proposition 1 (proved: scalar expectation and covariance)

For the physical first-cell event `C_k`,

```text
Delta_k(C_k)=E_(P_B) f_k-E_(P_A) f_k,                (1.1)
sum_y z_k(y)=2 Delta_k(C_k)/pi_y,                    (1.2)
pi_y=2/(n-2) (1-2/n)^(n-3).                         (1.3)
```

Let `P_(g,j)` be the subprobability law in M91's source channel `J=j`, so
its mass is `alpha_j`. The `J=0` submeasures agree. For `j=1,2`, define

```text
mu_j=(P_(B,j)+P_(A,j))/(2 alpha_j),
sigma_j(s)=
 (P_(B,j)(s)-P_(A,j)(s))/(P_(B,j)(s)+P_(A,j)(s))
```

on a positive denominator and zero otherwise. Then

```text
Delta_k(C_k)=2 sum_(j=1)^2 alpha_j
                  Cov_(mu_j)(f_k,sigma_j).           (1.4)
```

In particular `(PCS-bound)` is equivalent to

```text
n^2 |Delta_k(C_k)|=O(1).                             (1.5)
```

#### Proof

Substitute `P_g(s)=a(s)C_g(s)/A_g` into M168 `(PCS)` and then use its event
identity `(CE)`. This gives (1.1)--(1.2). The completion formula
`F_(n-3)(1,1,n-2)=(n-3)! tau(n-2)` gives (1.3). By construction
`E_(mu_j)sigma_j=0`, while

```text
P_(B,j)-P_(A,j)=2 alpha_j sigma_j mu_j.
```

The common `J=0` measure cancels, proving (1.4). Finally (1.2)--(1.3),
`n=3k`, and `(1-2/n)^(n-3)` bounded above and below by positive absolute
constants prove the equivalence (1.5). QED.

This is a signed covariance identity, not a Poincare estimate; no spectral
gap is invoked.

## 2. Exact PC/cycle-index response

Put `tau(d)=d^(d-1)/d!` and `R_n=(n-3)(n-4)`. A residual component of
`q=s^-1h` is a union of either one or two positive ambient `h`-runs. For a
one-run component of size `d`, set (invalid subscripts give zero)

```text
U_1(d)=(d-1) tau(d-1)/tau(d),
V_1(d)=(d-2)(d-3) tau(d-2)/tau(d).                   (2.1)
```

For a two-run component with run sizes `a,b>=1`, `d=a+b`, set

```text
U_2(a,b)=(d-2) tau(d-1)/tau(d),
V_2(a,b)=((d-2)(d-3)-2[(a-2)_+ +(b-2)_+])
             tau(d-2)/tau(d).                       (2.2)
```

### Proposition 2 (proved: exact decorated component moment)

If the three residual components have decorations `(U_i,V_i)` from
(2.1)--(2.2), then

```text
f_k(s)=1/R_n [sum_i V_i+2 sum_(i<j)U_iU_j].          (2.3)
```

For a triangle all three components use `(U_1,V_1)`. A separated double with
positive support gaps `(x,y,z,w)` uses one-run sizes `x,z` and two-run
decoration `(y,w)`; a nested double uses one-run sizes `y,w` and two-run
decoration `(x,z)`.

#### Proof

In M168 `(PC)`, a one-run size-`d` component has `g=d-1` generic boundary
edges and `a=(d-2)_+` adjacent generic pairs. Hence its ordered same-component
coefficient is `(d-2)(d-3)` (with the invalid small-size completion set to
zero), while a cross-component use supplies `d-1`. Dividing the corresponding
completion products by `A_s=(n-3)! product tau(d_i)` and using
`(n-5)!/(n-3)!=1/R_n` gives (2.1).

A two-run component has `g=d-2` and
`a=(a-2)_+ +(b-2)_+`, giving (2.2). Cross-component products factor into
the two `U` decorations, which proves (2.3). The positive-gap residual-cycle
descriptions of triangle/separated/nested double give the last sentence.
QED.

Let

```text
T(z)=sum_(d>=1)tau(d)z^d= z exp(T(z)).               (2.4)
```

Then the exact one-run cycle-index decorations are

```text
sum_(d>=1) tau(d)U_1(d)z^d=z^2 T'(z),
sum_(d>=1) tau(d)V_1(d)z^d=z^4 T''(z).               (2.5)
```

Indeed these are coefficient shifts. Thus every triangle contribution to a
Borel-weighted expectation of (2.3) is a coefficient of a polynomial in
`T,zT',z^2T''`. The two-run contribution is the analogous bivariate positive
composition convolution, with the explicit boundary correction in (2.2).

## 3. Exact affine cancellation and the sharper boundary lemma

Define bounded residual functions, exactly (not asymptotically), by

```text
u_1(d)=e U_1(d)-d-1/2,
v_1(d)=e^2 V_1(d)-d^2+2d,

u_2(a,b)=e U_2(a,b)-d+1/2,
v_2(a,b)=e^2 V_2(a,b)-d^2+4d,       d=a+b.           (3.1)
```

Standard elementary estimates for `(1-c/d)^d` (or Taylor expansion with a
uniform remainder, treating finitely many small `d` separately) show that
all four functions in (3.1) are uniformly bounded for positive valid sizes.

### Proposition 3 (proved: leading affine response)

Let `kind(s)` be triangle `T` or double `D`, and put `L_T=0`, `L_D=-2`.
There is an explicit boundary response `B_k(s)`, obtained by substituting
(3.1) into (2.3), such that

```text
e^2 R_n f_k(s)=n^2+L_(kind(s)) n+B_k(s).             (3.2)
```

More explicitly, if `epsilon_i=+1/2` for a one-run component and `-1/2`
for a two-run component, and `u_i,v_i` denote (3.1), then

```text
B_k(s)=-sum_i c_i d_i-L_(kind(s))n+sum_i v_i
 +2 sum_(i<j)[d_i(epsilon_j+u_j)+d_j(epsilon_i+u_i)
              +(epsilon_i+u_i)(epsilon_j+u_j)],      (3.3)
```

where `c_i=2` for a one-run component and `c_i=4` for a two-run component.
Formula (3.3) is a single scalar
positive-composition coefficient, including every small-component boundary
term. The identities `sum d_i=n`, `sum epsilon_i=3/2` for triangles and
`1/2` for doubles give `L_T=0`, `L_D=-2`.

#### Proof

Write `eU_i=d_i+epsilon_i+u_i` and
`e^2V_i=d_i^2-2d_i` for a one-run component, or
`d_i^2-4d_i` for a two-run component, plus `v_i`. Expand (2.3). Its quadratic
part is `(sum_i d_i)^2=n^2`. The deterministic linear part is

For a triangle, `-2n` from the `V` terms and `+2n` from the epsilon cross
terms cancel. For a double, the two one-run components contribute
`-2(n-d_two)`, the two-run component contributes `-4d_two`, and the epsilon
cross term contributes `+2d_two`, totaling `-2n`. Thus
`L_T=0,L_D=-2`; the remaining literal terms are exactly (3.3). QED.

The important point is that `B_k` need not be uniformly bounded pointwise:
bounded `u_i` multiplied by a macroscopic `d_j` can be `O(n)`. Its *signed
source coefficient* is the narrower object.

### Proposition 4 (proved: kind transfer is explicit and small)

For the signed source measure `eta=P_B-P_A`,

```text
eta(T)=alpha_2 [3/(2k-1)-3(k-2)/(k(2k-3))]
      =12(k-1)/[3k(3k-4)(2k-1)],                    (3.4)
eta(D)=-eta(T),                                      (3.5)
```

and the `J=0` and `J=1` kind masses cancel separately. Hence

```text
Delta_k(C_k)=e^-2/R_n [2n eta(T)+eta(B_k)].          (3.6)
```

#### Proof

The `J=0` measures are identical. In `J=1`, one exterior factor and one
middle factor always have disjoint supports and hence form a double under
both sources, so their kind masses agree. In `J=2`, two exterior factors
form a triangle exactly when the second edge shares one endpoint with the
first. The exact local triangle probability from M73 (4.1), specialized to
one residual `d`-cycle, is `3/d`. Thus the long `(2k-1)` cycle gives
`3/(2k-1)`. For two
separate `k`-cycles, the two factors must first choose the same component,
which has probability `(k-2)/(2k-3)`, and then give a triangle with
probability `3/k`. This proves the bracket in (3.4). Multiplication by M91's
`alpha_2` and simplification give the last expression. Total signed mass is
zero, proving (3.5). Substitute (3.2) in `eta(f)`; the constant `n^2` drops
out and the `0-(-2n)` difference gives (3.6). QED.

Equation (3.4) is `O(k^-2)`, so `2n eta(T)=O(1)`. Therefore the original
PCS statement is now equivalent to one strictly sharper scalar coefficient
lemma:

> **Boundary-response coefficient lemma `(BR)` (unresolved).** Uniformly for
> odd `k>=3`, with both M91 channels summed with their signs,
>
> ```text
> |eta(B_k)|
> =|2 sum_(j=1)^2 alpha_j Cov_(mu_j)(B_k,sigma_j)|=O(1).   (BR)
> ```

This is sharper than asking directly for an `O(k^-2)` event contrast: all
constant and deterministic affine terms have been evaluated and cancelled,
leaving one explicit bounded-decoration, positive-composition coefficient.
Via (2.4)--(2.5), `(BR)` is a finite coefficient estimate in the rooted-tree
function `T` plus the two-run boundary correction in (2.2). It retains both
source channels and triangle/double transfer until (3.6).

The present mission does not prove `(BR)`. In particular, taking absolute
values over split `u`, over channels, or over triangle/double components
loses the required cancellation and is not a proof.

## 4. Falsification and scope

`pcs_channel_calibration.py` independently enumerates only the two ordered
source factors and evaluates (2.3). Exact `Fraction` checks at the allowed
`k=3,5,7` reproduce the frozen M168 signed cell sums. They also verify the
common `J=0` cancellation, the zero `J=1` kind transfer, (3.4), and the
opposite `J=2` triangle/double kind masses. The finite values

```text
k             3          5          7
n^2 Delta   2.66440    1.51186    1.19283
eta(B_k)    5.37164    5.58410    5.46418
```

are calibration only. They neither prove `(BR)` nor a universal sign.

This proof does not concern FD-bound, direct L1, H0, a spectral gap, the
identity heat-bath chain, mixing, or either Terminal.
