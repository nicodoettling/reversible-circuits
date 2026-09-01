# Exact Borel convolution and the central-double obstruction to `(BA2)`

Status: Propositions 1--5 are **proved**.  The scalar lower bound `(BD)` is
**unresolved**.  Finite values testing `(BD)` are empirical/exact-finite only.
Nothing here proves a balanced L1 bound, an H0 estimate, or a sampler gap.

## 1. Setup

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Put `n=3k`, with odd `k>=3`, and

```text
h=(0 1 ... n-1),
A=A_k=(0,k,2k),
B=B_k=(0,1)(k,2k).
```

Let `X_n` be M73's raw admissible rank-two products.  For `x in X_n`, let
`a(x)=3` for an oriented triangle and `a(x)=2` for a double.  Write

```text
b_d=e^(-d) d^(d-1)/d!,
beta_3(x)=product_(C cycle of x^-1 h) b_|C|,
beta_5(x,y)=1[ell_T((xy)^-1 h)=n-5]
              product_(C cycle of (xy)^-1 h) b_|C|.
```

Singleton cycles are included; `b_1=e^-1`, so the exponential factors still
cancel because all cycle sizes sum to `n`.  Set

```text
R_n=(n-3)(n-4),
c_n=(n-3)! e^n/n^(n-2).
```

The raw stationary law and kernel are

```text
pi(x)=a(x)c_n beta_3(x),
K(x,y)=a(y)/R_n * beta_5(x,y)/beta_3(x).              (1.1)
```

These are exactly M73's completion-count formulas, rewritten with Borel
weights; no asymptotic approximation enters `(1.1)`.

## 2. Exact signed target-residual convolution

Define the complete first-row Borel difference

```text
d_k(s)=beta_5(B,s)/beta_3(B)-beta_5(A,s)/beta_3(A).   (2.1)
```

It already includes the difference of the fully combined `J=1,2` channels;
no channelwise absolute value is taken.

Let `theta(x)=h^-1 x h`, let `O_t` be the distinct cyclic orbit of `t`, and
put

```text
Q_t(s)=|O_t|^-1 sum_(t' in O_t) beta_5(s,t').         (2.2)
```

### Proposition 1 (proved: exact orbit-aware convolution)

If

```text
z_k(O_t)=
 [bar K^2(O_B,O_t)-bar K^2(O_A,O_t)]/bar pi(O_t),     (2.3)
```

then

```text
z_k(O_t)=1/[c_n R_n^2 beta_3(t)]
 sum_(s in X_n) a(s)d_k(s)Q_t(s)/beta_3(s).           (2.4)
```

Consequently

```text
(BA2)_k=E_pi[z_k^2],
2 TV(bar K^2(O_A,.),bar K^2(O_B,.))=E_pi|z_k|.        (2.5)
```

Here the expectations in `(2.5)` may be taken on raw states: `z_k` is
constant on cyclic orbits, so aggregation gives the literal quotient norms.

#### Proof

For a source representative `g`, `(1.1)` gives

```text
bar K(O_g,O_s)=a(s)/R_n sum_(s' in O_s)
 beta_5(g,s')/beta_3(g).                              (2.6)
```

For fixed target orbit `O_t`, the quantity

```text
beta_3(s)^-1 sum_(t' in O_t)beta_5(s,t')
```

is constant as `s` runs through its orbit.  Expand the intermediate-orbit
sum in the difference of the two squared rows, then replace it by the sum
over all raw `s`.  This gives

```text
bar K^2(O_B,O_t)-bar K^2(O_A,O_t)
 =a(t)/R_n^2 sum_s a(s)d_k(s)/beta_3(s)
                 sum_(t' in O_t)beta_5(s,t').         (2.7)
```

The stationary orbit mass is

```text
bar pi(O_t)=|O_t|a(t)c_n beta_3(t).
```

Dividing `(2.7)` proves `(2.4)`.  This division retains the short size-`k`
orbit when `t=A`; it is precisely the `|O_t|` in `(2.2)`.  Summing the
square or absolute value against stationary orbit masses proves `(2.5)`.
QED.

For any cyclic-invariant raw target event `E`, orbit averaging is unnecessary:

```text
Delta_k(E):=bar K^2(O_B,E)-bar K^2(O_A,E)
 =1/R_n^2 sum_(s in X_n) a(s)d_k(s)/beta_3(s)
       sum_(t in E) a(t)beta_5(s,t).                  (2.8)
```

Equation `(2.8)` is the promised target-residual/Borel convolution.  Its only
sign is the complete difference `d_k`; the target sum and outer stationary
inequality below are positive.

## 3. Sharp bulk and boundary scales of the M91 Abel coefficients

Retain M91's split laws

```text
p_s=b_s b_(2k-1-s)/[(1-1/(2k-1))b_(2k-1)],
q_s=b_s b_(k-s)/[(1-1/k)b_k]       (s<k/2),
q_s=0                              (s>k/2),
D_u=sum_(s<=u)(p_s-q_s).                               (3.1)
```

Put `c=(2 pi)^(-1/2)` and, away from the single cutoff point `x=1/2`,

```text
P(x)=c x^(-3/2)(1-x/2)^(-3/2),
Q(x)=c x^(-3/2)(1-x)^(-3/2) 1[x<1/2],
mathcal D(x)=integral_0^x [P(y)-Q(y)]dy.              (3.2)
```

The integrand difference in `(3.2)` is integrable at zero because its
`y^-3/2` terms cancel, leaving `O(y^-1/2)`.

### Proposition 2 (proved: Borel coefficient scaling)

For every fixed `0<x<1`, `x != 1/2`,

```text
sqrt(k) D_floor(kx) -> mathcal D(x).                  (3.3)
```

Moreover, if `u=u(k)` satisfies `u->infinity` and `u=o(k)`, then

```text
D_u ~ -3/[2 sqrt(2 pi)] * sqrt(u)/k.                  (3.4)
```

#### Proof

Stirling with a uniform remainder gives

```text
b_j=c j^-3/2(1+O(j^-1)).                              (3.5)
```

For `s=floor(kx)` in a compact subinterval of `(0,1)`, `(3.5)` gives

```text
k^(3/2)p_s -> P(x),
k^(3/2)q_s -> Q(x).                                   (3.6)
```

Near zero, the ratio form in `(3.1)` and `(3.5)` gives the uniform bound

```text
|p_s-q_s| <= C b_s(s+1)/k             (s<=epsilon k), (3.7)
```

so `sqrt(k)` times the omitted initial sum is `O(sqrt(epsilon))`.
Apply ordinary Riemann convergence to `[epsilon,x]` and then let
`epsilon` decrease to zero.  This proves `(3.3)`.

For `s<=u=o(k)`, expanding the same ratios one order further gives uniformly

```text
p_s-q_s
 =-b_s(1+3s/2)/(2k)+O(b_s(1+s^2)/k^2).               (3.8)
```

Now `(3.5)` implies

```text
sum_(s<=u)s b_s ~ 2c sqrt(u),
sum_(s<=u)b_s=O(1),
sum_(s<=u)s^2b_s=O(u^(3/2)).                          (3.9)
```

Summing `(3.8)` and using `u=o(k)` proves `(3.4)`.  QED.

Thus the Abel coefficients have a genuine `k^-1/2` bulk profile.  They do
not supply the extra half-power demanded by `(BA2)`.

## 4. A positive-mass central double event

Let `r_k=(k+1)/2`.  Define `E_k` to consist of quotient double-transposition
states whose four positive cyclic support gaps `(x,y,z,w)` all satisfy

```text
x,y,z,w >= r_k.                                      (4.1)
```

Condition `(4.1)` is invariant under the four colored-composition encodings
of the same double orbit.

### Proposition 3 (proved: exact mass and `Theta(k^-1)` asymptotic)

The exact stationary mass is

```text
bar pi(E_k)=n(n-3)!/n^(n-2)
 sum_[x+y+z+w=n; x,y,z,w>=r_k]
       tau(x)tau(z)tau(y+w),                          (4.2)
```

where `tau(d)=d^(d-1)/d!`.  If `rho=1/6`, then

```text
k bar pi(E_k) -> I_rho/(6 pi),                        (4.3)

I_rho=integral_[x,y,z,w>=rho; x+y+z+w=1]
          [x z (y+w)]^(-3/2) dx dy dz,
```

and `0<I_rho<infinity`.  In particular there are absolute constants
`0<c_E<C_E<infinity` such that

```text
c_E/k <= bar pi(E_k) <= C_E/k                         (4.4)
```

for every sufficiently large odd `k`.

#### Proof

A colored positive four-composition has residual sizes

```text
S: (x,z,y+w),       N: (x+z,y,w).
```

Every odd-`n` double orbit has size `n` and exactly four colored-composition
encodings.  The `S` and `N` sums over the invariant domain `(4.1)` agree by
a cyclic change of variables.  Substituting M73's orbit mass

```text
n*2*(n-3)! tau(lambda_1)tau(lambda_2)tau(lambda_3)/n^(n-2)
```

and dividing the two-color encoding sum by four proves `(4.2)`.

Write the product in `(4.2)` as `e^n b_xb_zb_(y+w)`.  Stirling gives

```text
n(n-3)!e^n/n^(n-2) ~ sqrt(2 pi)n^(1/2).               (4.5)
```

The three Borel factors contribute
`(2 pi)^(-3/2)n^(-9/2)` uniformly on `(4.1)`, and the three-dimensional
lattice Riemann sum contributes `n^3`.  Since `r_k/n->1/6`, the product of
these factors is exactly `(2 pi n)^(-1) I_rho(1+o(1))`.  Replacing
`n=3k` proves `(4.3)`.  The integration domain is compact, has positive
volume, and stays away from every singular face, proving positivity,
finiteness, and `(4.4)`.  QED.

Equivalently, integrating first over `y` gives the explicit two-dimensional
form

```text
I_rho=integral_[x,z>=rho; x+z<=1-2rho]
 (1-x-z-2rho)[x z (1-x-z)]^(-3/2) dz dx.              (4.6)
```

## 5. A one-scalar route to refuting `(BA2)`

### Proposition 4 (proved: event lower bound and separation from L1)

For every odd `k>=3`,

```text
(BA2)_k >= Delta_k(E_k)^2/bar pi(E_k).                (5.1)
```

Consequently:

1. `(BA2)_k=O(k^-4)` implies
   `Delta_k(E_k)=O(k^-5/2)`;
2. if `liminf k^2 |Delta_k(E_k)|>0`, then
   `(BA2)_k=Omega(k^-3)`, so `(BA2)` is false;
3. the same lower bound on `Delta_k(E_k)` merely gives
   `TV>=|Delta_k(E_k)|=Omega(k^-2)` (up to the convention for signed TV),
   and therefore does **not** refute a matching direct `O(k^-2)` L1 bound.

#### Proof

Apply Cauchy--Schwarz on `E_k` to the signed density `z_k`:

```text
Delta_k(E_k)^2
 =[sum_(O_t in E_k)bar pi(O_t)z_k(O_t)]^2
 <=bar pi(E_k) sum_(O_t in E_k)bar pi(O_t)z_k(O_t)^2.
```

The last sum is at most `(BA2)_k`, proving `(5.1)`.  Combine it with
Proposition 3.  Total variation dominates the absolute signed mass of any
event, proving the final statement.  QED.

The remaining scalar statement is therefore:

> **CENTRAL DOUBLE BULK DEFECT `(BD)` (unresolved).**  There is an absolute
> `c>0` such that for all sufficiently large odd `k`,
>
> ```text
> |bar K^2(O_B,E_k)-bar K^2(O_A,E_k)| >= c/k^2.       (BD)
> ```

Unlike `(BA2)`, `(BD)` has no targetwise square, no rare stationary
denominator, and only one invariant event.  Equation `(2.8)` is its exact
signed Borel-convolution formula.  Proving `(BD)` would rigorously refute
`(BA2)` while leaving the desired direct signed-L1 estimate open.

## 6. Finite falsification evidence, not an asymptotic proof

The exact checker verifies `(4.2)` and `(5.1)` over `Fraction` at `k=3,5`.
The all-target floating diagnostic extends the scalar check to `k=7,9`.
The finite values are recorded in the report and JSON artifacts.  They show
stable positive `k^2 Delta_k(E_k)` near `0.04` and stable
`k bar pi(E_k)` near `0.07` from `k=5` onward, but they cannot prove `(BD)`.

The strongest self-attack is that the signed convolution `(2.8)` still has
large cancellation across intermediate residual shells.  At the central
`k=7` targets, the minimum-one double-intermediate shell is negative while
the minimum-two through minimum-six shells are positive.  No termwise
positivity or monotonicity needed for `(BD)` has yet been proved.

## 7. A direct-L1 shell envelope that may survive `(BA2)`

Let

```text
S_d={O_t: min cycle size of t^-1 h equals d},          1<=d<=k,
M_(k,d)=bar pi(S_d),
Z_(k,d)=sup_(O_t in S_d)|z_k(O_t)|.                  (7.1)
```

### Proposition 5 (proved: sufficient shell criterion)

The direct signed target follows from the single summability condition

```text
sum_(d=1)^k M_(k,d) Z_(k,d) <= C/k^2.                (L1-shell)
```

More generally, it is enough to replace the supremum by the conditional
mean absolute score on each shell.  In contrast, `(BA2)` asks for

```text
sum_d M_(k,d) E[z_k^2 | S_d] <= C/k^4.                (7.2)
```

#### Proof

The shells partition the target space, so `(2.5)` gives

```text
2 TV=sum_d M_(k,d)E[|z_k| | S_d]
    <=sum_d M_(k,d)Z_(k,d).
```

The analogous decomposition of the square gives `(7.2)`.  QED.

This is elementary but cleanly displays the exponent separation.  The
stationary minimum-residual law has the uniform conditioned-Borel boundary
envelope

```text
M_(k,d) <= C d^(-3/2),                1<=d<=k.        (7.3)
```

Put `Gamma_n=n(n-3)!e^n/n^(n-2)<=C sqrt(n)`, uniformly for `n>=9`, by
Stirling.  M73's support-gap encoding shows that, up to fixed multiplicities,
fixing a triangle residual component at `d` leaves

```text
Gamma_n b_d sum_(i+j=n-d)b_i b_j.                    (7.4)
```

For a double, according to whether the component fixed at `d` is split or
unsplit, the corresponding upper bound is one of

```text
Gamma_n(d-1)b_d sum_(i+j=n-d)b_i b_j,
Gamma_n b_d sum_(i+j=n-d)(j-1)b_i b_j.               (7.5)
```

These cover both colors; a union over the three residual components costs
only an absolute factor.  The exact Borel convolution identities are

```text
sum_(i+j=N)b_i b_j=2(1-1/N)b_N,
sum_(i+j=N)(j-1)b_i b_j=(N-3+2/N)b_N.                (7.6)
```

On `S_d`, `d<=n/3`, so `N=n-d>=2n/3`.  Combining `(7.4)--(7.6)` with
`b_N<=C N^(-3/2)` bounds each expression by `C b_d`; since
`b_d<=C d^(-3/2)`, this proves `(7.3)`.  The finite score shells suggest the
complementary envelope

```text
Z_(k,d) <= C d/k,                                    (7.7)
```

but `(7.3)` and `(7.7)` alone sum only to `O(k^-1/2)`, far too weak.  The target
scale requires substantial signed posterior cancellation inside each shell,
not just a pointwise likelihood bound.  The boundary and positive-volume
bulk have different natural scales.  A falsifiable sufficient form retaining
both is

```text
M_(k,d) E[|z_k| | S_d]
 <= C/k^2 * [d^(-3/2)+(kd)^(-1/2)]                  (L1-envelope)
```

uniformly for `1<=d<=k`.  Indeed `sum_d d^(-3/2)=O(1)` and
`sum_(d<=k)(kd)^(-1/2)=O(1)`, so it proves `(L1-shell)`.  The first term is
the small-component boundary envelope; for `d=Theta(k)`, the second is
`Theta(k^-1)` after the outside `k^-2`, matching a positive-volume bulk
distributed across `Theta(k)` shells.  Exact values at `k=7,9` satisfy this
shape with small finite constants, but they only calibrate it.
`(L1-envelope)` is **unresolved**, and no direct L1 upper bound is claimed.

The central event from Proposition 3 has mass `Theta(k^-1)` and average
score empirically `Theta(k^-1)`, so it naturally contributes
`Theta(k^-2)` to L1 but `Theta(k^-3)` to L2.  This makes the scalar bulk
obstruction compatible with `(L1-envelope)` only at its summability edge,
exactly as required.
