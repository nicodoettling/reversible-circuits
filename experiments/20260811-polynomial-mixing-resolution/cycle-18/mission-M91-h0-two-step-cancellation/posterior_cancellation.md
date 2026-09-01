# Posterior cancellation and Borel--Abel reduction for the balanced edge

Status: Propositions 1--3 and Lemma 4 are **proved**.  Inequality `(BA2)` is
**unresolved**.  Nothing here is a gap or Terminal theorem.

## 1. Setup and exact quotient formulas

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  Fix `n=3k`, with odd `k>=3`, and

```text
h=(0 1 ... n-1),
A=(0,k,2k),             B=(0,1)(k,2k).
```

M83/M88 proved that `[A],[B]` are strict endpoint-sharing neighbors.  The
underlying target is uniform on minimal length-`n-1` transposition
factorizations of `h`; `bar K` is M73's pair-product kernel after quotienting
by `theta(g)=h^-1 g h`.

For an admissible raw rank-two product `g`, put

```text
A_g=F_(n-3)(g^-1h),
C(g,s)=F_(n-5)((gs)^-1h),
Z=n^(n-2).
```

If `O_g` is the `theta` orbit of `g`, `o_g=|O_g|`, and `a(g)` is the number
of ordered transposition-pair lifts (`3` for an oriented triangle and `2` for
a double), the accepted exact formulas are

```text
bar pi(O_g)=o_g a(g) A_g/Z,
bar K(O_g,O_s)=a(s)/A_g * sum_(s' in O_s) C(g,s').       (1.1)
```

For this family,

```text
A_A=(3k-3)! tau(k)^3,
A_B=(3k-3)! tau(2k-1)tau(k),
o_A=k, a(A)=3,         o_B=n, a(B)=2.                  (1.2)
```

The short balanced orbit in `(1.2)` is retained throughout.

## 2. Posterior-score identity

Define the signed one-step row and its stationary score by

```text
eta=bar K(O_B,.)-bar K(O_A,.),
f(O_s)=eta(O_s)/bar pi(O_s).                            (2.1)
```

### Proposition 1 (proved: exact posterior cancellation)

For every quotient state `O_s`,

```text
f(O_s)
 =bar K(O_s,O_B)/bar pi(O_B)-bar K(O_s,O_A)/bar pi(O_A) (2.2)

 =n^(n-3)/A_s * sum_(r=0)^(n-1)
    {C(s,theta^r B)/A_B-C(s,theta^r A)/A_A}.            (2.3)
```

Moreover, for every target orbit `O_t`,

```text
(eta bar K)(O_t)=bar pi(O_t)(bar K f)(O_t),             (2.4)
TV(eta bar K)=1/2 E_barpi |bar K f|.                    (2.5)
```

#### Proof

Equation `(2.2)` is detailed balance for `bar K`, divided by the literal
stationary orbit masses.

For a general source orbit `O_g`, `(1.1)` gives

```text
bar K(O_s,O_g)/bar pi(O_g)
 =Z/[o_g A_s A_g] * sum_(g' in O_g) C(s,g').            (2.6)
```

The all-`n` phase sum visits each member of `O_g` exactly `n/o_g` times.
Thus

```text
(1/o_g)sum_(g' in O_g)C(s,g')
  =(1/n)sum_(r=0)^(n-1)C(s,theta^r g).                  (2.7)
```

Substituting `Z/n=n^(n-3)` in `(2.6)` proves `(2.3)`.  In particular, the
factor three caused by the stabilizer of `A` is neither lost nor inserted by
hand: it is exactly the repetition in `(2.7)`.  The lift multiplicities
`a(s),a(g)` cancel between `(1.1)` and the stationary masses only after the
orbit sums have been retained.

Finally, detailed balance gives

```text
sum_s eta(s)bar K(s,t)
 =bar pi(t)sum_s bar K(t,s)eta(s)/bar pi(s),
```

which is `(2.4)`; summing its absolute value proves `(2.5)`.  QED.

This absorbs the entire first-step signed schema sum into one centered
posterior score.  The second application of `bar K` is a conditional
expectation, not a separate triangle bound on sixteen ordered schemas.

## 3. Exact cancellation of the common residual component

The accepted residual cycles are

```text
A^-1h:
  C_-=(0,1,...,k-1),
  M=(k,k+1,...,2k-1),
  C_+=(2k,2k+1,...,3k-1);

B^-1h:
  {0},
  L=(1,...,k-1,2k,...,3k-1),
  M=(k,k+1,...,2k-1).                                  (3.1)
```

Let `nu_C` be the first-transposition law in a uniform minimal factorization
of a cycle `C`.  Let `mu_Q` be the pushforward of the first two ordered
factors to their product in a uniform minimal factorization of a residual
permutation `Q`.  Thus `mu_Q` includes all ordered-product multiplicities:
three lifts for oriented triangles and two for doubles.  Every law below is
pushed to cyclic product orbits only after these raw multiplicities are
included.

Put `m=k-1`, `R=3m`, `D=R(R-1)`.  Call `C_-` and `C_+` exterior for source
`A`, call `L` exterior for source `B`, and let `J` be the number of exterior
colors among the first two completion factors.  The exterior rank is `2m`
and the common `M` rank is `m` for both sources, so

```text
alpha_0=Pr(J=0)=m(m-1)/D,
alpha_1=Pr(J=1)=4m^2/D,
alpha_2=Pr(J=2)=2m(2m-1)/D.                            (3.2)
```

Define conditional pair-product laws

```text
H_(0,A)=H_(0,B)=mu_M;

H_(1,B)=Law(E_L E_M),
  E_L~nu_L, E_M~nu_M independently;

H_(1,A)=1/2 Law(E_- E_M)+1/2 Law(E_+ E_M),
  E_~nu_(C_-/C_+), E_M~nu_M independently;

H_(2,B)=mu_L,
H_(2,A)=mu_(C_- C_+),                                  (3.3)
```

where the last law uses the uniform interleaving of the two independent
component factorizations.  Products in `H_1` are unaffected by the two color
orders because their supports are disjoint; the factor two for those orders
is already in `alpha_1`.

### Proposition 2 (proved: two-channel merge defect)

The complete quotient rows satisfy

```text
bar K(O_A,.)=sum_(j=0)^2 alpha_j H_(j,A),
bar K(O_B,.)=sum_(j=0)^2 alpha_j H_(j,B),               (3.4)
```

and hence

```text
eta=alpha_1(H_(1,B)-H_(1,A))
    +alpha_2(H_(2,B)-H_(2,A)).                          (3.5)
```

#### Proof

Uniform residual-component interleaving samples the first two colors without
replacement from ranks `(m,m,m)` for `A` and `(2m,m,0)` for `B`.  Counting
the events `J=0,1,2` gives `(3.2)`.  Conditional component factorizations are
independent and uniform, giving precisely `(3.3)` and `(3.4)`.  The `J=0`
law is literally the same `mu_M`; subtracting proves `(3.5)`.  QED.

In M73's schema language, `H_(2,B)` contains `I3,IS,IN`, while
`H_(2,A)` contains those same-cycle schemas and the exterior `X` schema;
`H_1` contains the remaining cross schemas.  Thus `(3.5)` deletes only an
identical block.  It does not discard a color, embedding, or lift
multiplicity.

## 4. A common conditioned-Borel split and exact Abel summation

For an odd `d`-cycle, a specified chord with smaller split `s<d/2` has

```text
w_d(s)=(d-2)! tau(s)tau(d-s)/d^(d-2).                  (4.1)
```

There are exactly `d` such chords, so define probability laws, extending
`q_s` by zero outside its displayed support,

```text
p_s=(2k-1)w_(2k-1)(s),       1<=s<=k-1,
q_s=k w_k(s),                1<=s<=(k-1)/2,
q_s=0,                       (k+1)/2<=s<=k-1.          (4.2)
```

Equivalently, with critical Borel mass `b_j=e^-j tau(j)`,

```text
p_s=b_s b_(2k-1-s)/[(1-1/(2k-1))b_(2k-1)],
q_s=b_s b_(k-s)/[(1-1/k)b_k].                          (4.3)
```

For `j=1`, let `Phi_(1,s)` be `H_(1,B)` conditioned on the smaller split of
`E_L` being `s`; let `Psi_(1,s)` be `H_(1,A)` conditioned on the smaller
split of its exterior edge being `s`.  For `j=2`, condition on the smaller
split of the first ordered factor in the laws `mu_L` and `mu_(C_-C_+)`,
respectively, and call the resulting product laws `Phi_(2,s)` and
`Psi_(2,s)`.  Equal component ranks make the `C_-`/`C_+` choice exactly fair.
Then

```text
H_(j,B)=sum_(s=1)^(k-1) p_s Phi_(j,s),
H_(j,A)=sum_(s=1)^((k-1)/2) q_s Psi_(j,s).             (4.4)
```

Each `Phi_(j,s),Psi_(j,s)` is a normalized probability measure, not a
signed schema fragment.  They also have completely explicit completion-count
forms.  If `E_C(s)` is the set of chords internal to the oriented cycle `C`
with smaller split `s`, and `T(Q)` is the set of transpositions internal to
the cycles of a residual permutation `Q`, write

```text
N_Q(e,f)=F_(r(Q)-2)((ef)^-1 Q)/F_(r(Q))(Q).            (4.4a)
```

For every test function `g` on quotient product states,

```text
Phi_(1,s)(g)
 =p_s^-1 sum_(e in E_L(s)) nu_L(e)
          sum_(f in T(M)) nu_M(f) g([ef]),

Psi_(1,s)(g)
 =q_s^-1 (1/2)sum_(C in {C_-,C_+})
          sum_(e in E_C(s))nu_C(e)
          sum_(f in T(M))nu_M(f) g([ef]),

Phi_(2,s)(g)
 =p_s^-1 sum_(e in E_L(s))
          sum_(f in T(eL)) N_L(e,f) g([ef]),

Psi_(2,s)(g)
 =q_s^-1 sum_(C in {C_-,C_+})sum_(e in E_C(s))
          sum_(f in T(e C_-C_+))
             N_(C_-C_+)(e,f)g([ef]).                  (4.4b)
```

In the last line the fair choice of `C_-` or `C_+` is already contained in
`N_(C_-C_+)`: under the uniform two-component factorization, the first
factor chooses either equal-rank component with probability `1/2`.
Equations `(4.4a)--(4.4b)` sum ordered first and second factors before sending
`ef` to its cyclic orbit.  They therefore retain the three triangle lifts,
the two double lifts, and every orbit multiplicity literally.

Put

```text
D_u=sum_(s=1)^u(p_s-q_s),       1<=u<=k-1.             (4.5)
```

Both laws in `(4.2)` normalize, so `D_(k-1)=0`.

### Proposition 3 (proved: measure-valued Borel--Abel identity)

For `j=1,2`, as an exact signed measure on cyclic product orbits,

```text
H_(j,B)-H_(j,A)
 =sum_(u=1)^(k-2) D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_(s=1)^((k-1)/2) q_s(Phi_(j,s)-Psi_(j,s)).       (4.6)
```

#### Proof

Add and subtract `sum_s q_s Phi_(j,s)` in `(4.4)`.  The embedding/conditional
defect is the second sum in `(4.6)`.  For the remaining scalar signed weights,
write `p_s-q_s=D_s-D_(s-1)`, with `D_0=D_(k-1)=0`; ordinary summation by
parts gives

```text
sum_(s=1)^(k-1)(p_s-q_s)Phi_(j,s)
 =sum_(u=1)^(k-2)D_u(Phi_(j,u)-Phi_(j,u+1)).
```

This is an equality of measures, proving `(4.6)`.  QED.

### Lemma 4 (proved: sign and size of the Borel coefficients)

For every common-support index `1<=s<=(k-1)/2`, one has `p_s<q_s`.
Consequently

```text
D_u<0 for 1<=u<=k-2,
max_u |D_u|=-D_((k-1)/2)
             =sum_(s>(k-1)/2)p_s=Theta(k^-1/2),
W_k:=sum_(u=1)^(k-2)|D_u|
   ~[(2-sqrt(2))/sqrt(pi)]sqrt(k).                     (4.7)
```

#### Proof

Let `r_j=b_(j-1)/b_j=e(1-1/j)^(j-2)`.  The sequence `r_j` is strictly
decreasing for `j>=2`: for `x>2`, putting `y=1/x` gives

```text
d/dx [(x-2)log(1-1/x)]
 =log(1-y)+y(1-2y)/(1-y)
 <-y+y-y^2/(1-y)<0.                                  (4.8)
```

From `(4.3)`,

```text
p_s/q_s
 ={(1-1/k)/(1-1/(2k-1))}
   product_(i=0)^(s-1) r_(2k-1-i)/r_(k-i) <1.         (4.9)
```

Thus the cumulative deficit grows throughout the support of `q`; after that
only positive `p_s` terms remain, returning it monotonically to zero.  This
proves the equality in `(4.7)`.  Uniform two-sided Stirling bounds in the
range `(k-1)/2<s<=k-1` give

```text
p_s asymp k^(3/2)/[s^(3/2)(2k-1-s)^(3/2)] asymp k^-3/2.
```

There are `Theta(k)` such indices, proving the maximum estimate in `(4.7)`.

Since `p` stochastically dominates `q`, the discrete tail-sum identity gives

```text
W_k=E_p[S]-E_q[S].                                   (4.10)
```

M83's accepted dominated-Riemann calculation for the conditioned-Borel
smaller fragment says, for odd `d`,

```text
E[S_d]=d sum_(s<d/2)s w_d(s)
       ~sqrt(2d/pi).                                  (4.11)
```

Apply `(4.11)` at `d=2k-1` and `d=k` in `(4.10)` to obtain the stated
constant for `W_k`.  QED.

Lemma 4 explains the scale that a triangle estimate loses: the Abel
coefficients themselves retain the accepted `Theta(k^-1/2)` Borel boundary.
The extra `k^-3/2` must come from the signed conditional differences after
the second kernel, not from a smaller first-step tail.

## 5. One standalone remaining inequality

For a target orbit `O_t`, define its full one-step posterior likelihood

```text
G_t(O_s)=bar K(O_s,O_t)/bar pi(O_t)
 =n^(n-3)/A_s sum_(r=0)^(n-1)C(s,theta^r t)/A_t.       (5.1)
```

For `j=1,2`, evaluate the right side of `(4.6)` on `G_t`:

```text
cal A_(j,k)(t)
 =sum_(u=1)^(k-2)D_u[
      Phi_(j,u)(G_t)-Phi_(j,u+1)(G_t)]
  +sum_(s=1)^((k-1)/2)q_s[
      Phi_(j,s)(G_t)-Psi_(j,s)(G_t)].                 (5.2)
```

Every `G_t` is the sum of the full four-schema second row.  Therefore no
absolute value has been taken inside any of the `I3,IS,IN,X` terms.

Detailed balance and Propositions 2--3 give the exact pointwise identity

```text
(bar K f)(O_t)
 =alpha_1 cal A_(1,k)(t)+alpha_2 cal A_(2,k)(t).       (5.3)
```

Indeed, `bar K(t,s)/bar pi(s)=G_t(s)`, so the left side is `eta(G_t)`.

The balanced family is now reduced to one explicit positive summation
inequality:

> **BALANCED ABEL COLLISION `(BA2)` (unresolved).**  There is an absolute
> constant `C` such that, for every odd `k>=3`,
>
> ```text
> sum_(O_t) bar pi(O_t)
>   [alpha_1 cal A_(1,k)(t)+alpha_2 cal A_(2,k)(t)]^2
> <= C/k^4.                                            (BA2)
> ```

By `(2.5)`, `(5.3)`, and Cauchy--Schwarz, `(BA2)` implies

```text
TV(bar K^2(O_A,.),bar K^2(O_B,.))<=sqrt(C)/(2k^2).     (5.4)
```

The single square in `(BA2)` is essential: it is outside both merge-defect
channels, both Abel sums, every cyclic embedding, and all four second-step
schemas.

There is a compact equivalent collision form.  Put
`q_g(s)=1[s=g]/bar pi(g)`.  Then `f=bar K(q_B-q_A)` and

```text
left side of (BA2)=||bar K f||_(2,bar pi)^2
 =<q_B-q_A,bar K^4(q_B-q_A)>_(bar pi)                 (5.5)

 =bar K^4(B,B)/bar pi(B)+bar K^4(A,A)/bar pi(A)
  -bar K^4(A,B)/bar pi(B)-bar K^4(B,A)/bar pi(A).      (5.6)
```

Equation `(5.6)` is a localized signed contrast, not a global trace or a
fixed-moment heuristic.  Finite evaluation may falsify `(BA2)` but cannot
prove it.

### A proved weighted-Fisher sufficient route

The sign information in Lemma 4 makes the loss of an entrywise gradient
bound explicit.  Define the already channel-combined likelihood differences

```text
X_u(t)=alpha_1[Phi_(1,u)-Phi_(1,u+1)](G_t)
      +alpha_2[Phi_(2,u)-Phi_(2,u+1)](G_t),

Y_s(t)=alpha_1[Phi_(1,s)-Psi_(1,s)](G_t)
      +alpha_2[Phi_(2,s)-Psi_(2,s)](G_t).              (5.7)
```

Weighted Cauchy--Schwarz, followed only once by `(x+y)^2<=2x^2+2y^2`,
proves

```text
E_barpi[(bar K f)^2]
 <=2W_k sum_u |D_u| E_barpi[X_u^2]
   +2 sum_s q_s E_barpi[Y_s^2].                       (5.8)
```

Thus a sufficient (not necessary) Fisher target is

```text
sum_u |D_u| E_barpi[X_u^2]=O(k^-9/2),
sum_s q_s E_barpi[Y_s^2]=O(k^-4).                     (5.9)
```

The powers in `(5.9)` use `W_k=Theta(sqrt(k))`.  Crucially, the two
first-step channels are already combined inside `X_u,Y_s`, and each
likelihood `G_t` still contains the full four-schema second row.  Finite
values through `k=7` show that `(5.8)` is substantially looser than `(BA2)`;
therefore `(BA2)`, or the direct signed L1 analogue, remains the primary
target rather than termwise Fisher control.

## 6. Scope and strongest self-attack

1. `(BA2)` is unproved and is stronger than the desired balanced-family L1
   estimate.  The latter could hold even if rare target orbits invalidate
   `(BA2)`.
2. The exact Abel transform does not bound the embedding defects
   `Phi-Psi`.  Lemma 4 shows that separate triangle bounds begin with a
   `Theta(k^-1/2)` coefficient, so a genuine posterior smoothing estimate is
   still required.
3. The two channels in `(5.3)` must remain paired.  Bounding their images
   separately is not justified at the target scale.
4. The general strict-`Lambda_n` edge lemma is not proved.  Propositions 2--3
   exploit the special balanced geometry: one common `k`-cycle and a merge of
   the other two components after removing vertex `0`.
5. The family exists only for `n=3k` with odd `k`; `k=3,n=9` is the first
   member.  `k=1,n=3`, even `k`, identity endpoints, `m=0,2`, and `N=2` are
   outside the statement.
