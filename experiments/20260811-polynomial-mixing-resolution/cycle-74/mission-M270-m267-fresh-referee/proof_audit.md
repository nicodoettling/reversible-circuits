# M270 proof audit of M267's endpoint-profile reduction

Date: 2026-08-14 UTC.

## 1. Audited statement and exact scope

Fix odd `k>=3`, put `n=3k`, and use `(pq)(x)=p(q(x))`.  The audit concerns
only the balanced first fixed cell of the auxiliary uniform minimal
length-`n-1` factorization law of the long cycle under the nonlazy cyclic
rank-two quotient kernel.  It is not the global identity-word law and not
the lazy exact same-product `{3,4,5}` heat-bath chain.

The accepted M261 endpoint observable for a supported rank-two product `s`
is

```text
E_ell(s)=sum_(i,j) kappa_ij sum_x
 chi_i(x-ell)[chi_j(x+1)-chi_j(x)],   2<=ell<=n-3.   (1.1)
```

The audit asks whether M267 exactly represents `(1.1)`, reduces PBV to its
named half-profile `(SET)`, and proves the uniform statewise lag-variation
bound.  It does not assume or attempt `(SET)`, `(SR)`, or `(TPR)`.

## 2. Null-owner jump identity

Let `o(r)=i` when `chi_i(r)=1` and let `o(r)=empty` otherwise.  M261's
generic-edge iff makes the null positions exactly the support heads of `s`.
Extend `kappa` by zero whenever either argument is null.  At a fixed `x`,
the `i` sum in `(1.1)` selects `o(x-ell)` when nonnull, while the two `j`
sums select `o(x+1)` and `o(x)`.  Therefore

```text
E_ell(s)=sum_x [kappa(o(x-ell),o(x+1))
                 -kappa(o(x-ell),o(x))].             (2.1)
```

This also proves that a position contributes only when
`o(x)!=o(x+1)`.  Null/non-null transitions are included because their
coefficient is exactly zero on the null side.  M267's sign, displacement,
and endpoint indices are correct.

## 3. Phase, kind, and two-channel normalization

For a quotient law `nu`, M267's `Gamma_(nu,K,ell)` chooses a product orbit,
averages all `n` literal phases, and records the endpoint signature.  A
cyclic change of representative only permutes those `n` phases.  If an orbit
is short, the all-`n` list repeats each member by its stabilizer, so the
average remains a probability profile; no orbit-size correction appears.
Summing over signatures gives mass `nu(K)`, and `T,D` partition every
supported rank-two product.

The signature records the three owner sizes, their equality pattern and null
status, so it determines

```text
w=kappa(o(x-ell),o(x+1))-kappa(o(x-ell),o(x)).
```

Consequently, directly from `(2.1)`,

```text
sum_K <w,Gamma_(nu,K,ell)>=nu(E_ell)/n.              (3.1)
```

This independently confirms the outside factor `n` in M267.

For M91's channel one, the raw first exterior-edge mass at split `u` is
`p_u` on the merged cycle and `q_u` on either equal-rank separate exterior
cycle; the independent middle-edge law has mass one.  Hence division by
`p_u` or `q_u`, including the explicit fair `1/2` in the latter law, gives
normalized `Phi_(1,u),Psi_(1,u)` profiles.

For channel two, `N_Q(e,f)` is the raw ordered-pair completion probability.
Summing it over first edges of split `u` and all admissible second factors
gives `p_u` for the merged cycle and `q_u` for the two equal-rank exterior
cycles.  In the latter expression the fair first-component choice is already
inside `N_(C_-C_+)`, so an additional `1/2` would be wrong.  Raw ordered
factors are summed before quotienting; triangle multiplicity three, double
multiplicity two, seams, collisions, and the short orbit are retained.

The source-independent color probabilities are

```text
alpha_0=m(m-1)/D, alpha_1=4m^2/D,
alpha_2=2m(2m-1)/D,  m=k-1, D=3m(3m-1),
```

and sum to one.  The identical `J=0` law cancels.  Applying the linear
profile map to M91's exact Abel identity, and only then combining channels
and kinds, gives exactly

```text
eta(E_ell)=alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)
          =n sum_(K in {T,D}) <w,T_(K,ell)>.         (3.2)
```

No channel, kind, or phase normalizer is missing.

## 4. Reflection, central zero, and exact PBV/SET equivalence

Put

```text
F_ell=sum_(i,j)kappa_ij sum_r chi_i(r)chi_j(r+ell).
```

Symmetry of `kappa`, followed by exchanging owners and shifting `r`, gives
`F_ell=F_(n-ell)`.  Since `E_ell=F_(ell+1)-F_ell`,

```text
E_ell=-E_(n-ell-1).                                  (4.1)
```

The target domain `2,...,n-3` is invariant under this involution.  Because
`n` is odd, its unique fixed point is `(n-1)/2`, where `(4.1)` gives zero.
The lower representatives are exactly
`2,...,(n-3)/2`.

Writing `c_ell=sum_K<w,T_(K,ell)>`, equation `(3.2)` shows

```text
PBV: sum_(ell=2)^(n-3)|eta(E_ell)|=O(n^-1)
iff  sum_(ell=2)^(n-3)|c_ell|=O(n^-2).
```

Reflection and the central zero make the full sum exactly twice the sum over
`2<=ell<=(n-3)/2`.  Thus M267's half-profile `(SET)` is precisely equivalent
to PBV, with only this harmless factor two.

## 5. Uniform statewise `1232/e^2` bound

Each owner set is one circular interval for a one-run residual component and
at most two circular intervals for the unique two-run component of a double.
For two circular binary sets `A,B`, each with at most four boundary jumps,

```text
C_AB(ell)=sum_r 1_A(r)1_B(r+ell)
```

satisfies

```text
sum_ell |C_AB(ell+1)-C_AB(ell)|<=4|A|.
```

The symmetric calculation gives the same bound with `|B|`, hence the exact
upper bound `4 min(|A|,|B|)` used by M267.

With `tau(d)=d^(d-1)/d!`, put

```text
a_d=tau(d-1)/tau(d)=(1-1/d)^(d-2),
b_d=tau(d-2)/tau(d)=(1-1/d)(1-2/d)^(d-3).
```

For `d>=2`, the elementary bounds
`-x/(1-x)<=log(1-x)<=-x` give

```text
1/(d-1)<=1+(d-2)log(1-1/d)<=2/d.
```

Thus `0<=e a_d-1<=4/d`.  For `d>=4`, applying the same log bounds separately
at `1/d` and `2/d` gives

```text
0<=2+log(1-1/d)+(d-3)log(1-2/d)<=5/d,
```

and hence `0<=e^2 b_d-1<=20/d`.  The invalid shifts at `d=1,2` give
`rho_ii=-1`, and `d=3` is an immediate direct check (using `e^2<8`), so the
same diagonal bound holds for every positive `d`.

For distinct owners of sizes at least two, write
`e a_d=1+x_d`, where `0<=x_d<=4/d`.  Then

```text
|e^2 a_d a_e-1|=x_d+x_e+x_dx_e
 <=8(1/d+1/e)<=20(1/d+1/e).
```

If either size is one, the coefficient is zero and the claimed bound is
immediate.  Therefore all of M267's Cayley-ratio inequalities hold, including
invalid shifts and minimal component sizes.

Let owner `i` have size `d_i` and `g_i<=d_i` generic positions.  For the
three diagonal ordered pairs, interval variation and the ratio bound give at
most `3*4*20=240`.  Each of the six off-diagonal ordered pairs contributes
at most

```text
4 min(d_i,d_j) 20(1/d_i+1/d_j)<=160,
```

giving `960`.  Finally the support-head histogram `I_ell` has support size
`h<=4`; since `sum_ell I_ell=h^2`, its circular variation is at most
`2h^2<=32`.  M261's exact affine derivative on the target lags is

```text
e^2 E_ell=Delta I_ell+Delta Q_ell.
```

Restricting the full circular variation bounds to `2,...,n-3` proves

```text
sum_(ell=2)^(n-3)|E_ell(s)|<=(240+960+32)/e^2=1232/e^2
```

for every supported triangle or double, uniformly in rank.  This is a valid
statewise `O(1)` envelope, not the signed `O(1/n)` PBV estimate.

## 6. Conditional sign route

Let `G_ell=eta(R_ell)`, `R_n=(n-3)(n-4)`, and
`m_0=(n-3)/2`.  Under the unresolved `(SR)` signs,

```text
sum_(ell=2)^(k-2)|eta(E_ell)|
 =R_n[G_2-G_(k-1)],
sum_(ell=k-1)^m_0|eta(E_ell)|
 =R_n[G_((n-1)/2)-G_(k-1)].
```

The first sum is empty when `k=3`.  Reflection duplicates these two lower
half contributions and the center is zero, so

```text
sum_(ell=2)^(n-3)|eta(E_ell)|
 =2R_n[G_2+G_((n-1)/2)-2G_(k-1)].                  (6.1)
```

The bracket is nonnegative under `(SR)`.  Since `R_n=Theta(n^2)`, PBV is
then equivalent to `(TPR)`, namely that bracket being `O(n^-3)`.  From
`z_k(y)=Lambda_n G_(y+1)` and `Lambda_n=Theta(n)`, the equivalent score
indices are exactly `1,(n-3)/2,k-2` at scale `O(n^-2)`.  This verifies only
the conditional implication; neither `(SR)` nor `(TPR)` is promoted.

## 7. Firewall and finite falsification

The clean-room checker reads no predecessor and contains no import statement.
It exhausts all 336 and 3,185 supported products at `k=3,5`, respectively,
checking the jump/correlation derivative, all cyclic reflection indices,
central zero, phase factor `n`, null-owner positions, owner interval
variation, and target-lag statewise bound.  It also checks normalized `p,q`
and `alpha` masses and synthetic `(SR)=>(TPR)` endpoint ranges at five odd
ranks, plus finite Cayley-ratio guards.

Independently, the checker reconstructs M264's two products.  Both have
residual size/run profile `((1,1),(2,1),(6,2))`, but their exact endpoint
values are `-625/1296` and `-20/81`.  Therefore `E_ell` is not determined by
the accepted `X_D,Y_D` size/run cutoff profiles.  Those theorems cannot
replace M267's literal endpoint tensor without additional positional data.

All computations are exact except the explicitly finite numerical ratio
guard.  They are falsification only; the universal conclusions above rest on
the symbolic audit.

## 8. Exact stop

The audit finds no material or nonmaterial objection.  It accepts only the
endpoint representation, reflection/half-profile reduction, and statewise
variation envelope.  `(SET)`, `(SR)`, `(TPR)`, PBV, FD-bound, minority sign,
FCL1, any spectral gap, polynomial mixing, and Terminal all remain open.

