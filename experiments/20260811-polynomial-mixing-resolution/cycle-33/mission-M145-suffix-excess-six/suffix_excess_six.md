# M145 suffix-excess-six refined-reset theorem

## 1. Scope, convention, and theorem

The surrounding project target is uniform on fixed-length identity
transposition words in `Omega(N,m)`, with `(pq)(x)=p(q(x))` and factors
displayed left-to-right.  This note concerns only the auxiliary full
**nonlazy stationary-flow parking-degree projection** in the minimal-long-cycle
sector.

Use the accepted finite-DAG recurrence

```text
H=A_0+QH,
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B), j=1,...,k.
```

Only `j=0` and auxiliary rank-one children are killed.  M109/M114 prove the
recurrence, nilpotence, the all-deficit suffix-terminal bound, and `G<=H` by
positive histories.  M140/M144 prove the scalar estimate `C_S<3/4` for every
`S>=100`.

> **Theorem (refined suffix-excess-six contraction).**  For every `s>=7`,
> `K>=1`, and right-heavy seed
> ```text
> x=(s,K,K-1,s-6),
> q=w_7 w_(s-6)/w_(s+1),
> ```
> the complete auxiliary excursion obeys
> ```text
> H(x)<q(1-q),  G(x)<=H(x)<U(x)=q(1-q).
> ```

The strict inequality is stronger than needed.  This is not an auxiliary gap,
ROOT-MEAN LIFT, original `{3,4,5}` heat-bath gap, polynomial mixing theorem,
Terminal A, or Terminal B.

## 2. General context coordinates and all-rank structure

Fix the bottom rank `B`.  Write a descendant as

```text
X_(ell,a,D)=(B+ell,K_0+a,K_0+a-D,B),
z=1/(K_0+1),
K_0+a+1=(1+az)/z.
```

Here `ell` is suffix excess and `D` is the attachment deficit.  Put

```text
b_n=w_n/w_(n+1),
r_(ell:0)=(b_(B+ell),...,b_B),
q_ell=w_(ell+1) product_(i=0)^ell b_(B+i).
```

For a group of degree `k`, the exact attachment law is

```text
nu_(a,D,k)(0)
 =(D)_k z^k / product_(r=0)^(k-1)(1+(a+r)z),

nu_(a,D,k)(j)
 =binom(k,j)(D)_(k-j)z^(k-j)
   product_(r=0)^(j-1)(1+(a-D+r)z)
   /product_(r=0)^(k-1)(1+(a+r)z),       j=1,...,k.       (2.1)
```

Every positive rank is retained.  Its child coordinates are exactly

```text
(ell',a',D')=(h-1,a+k,D+k-j),                         (2.2)
```

where `h=t-B` is the root group's height.

For excess `ell`, the contextual support consists of

```text
(P,B+h),  h=0,...,ell,
P an ordered composition of ell-h.                    (2.3)
```

The empty prefix at `h=ell` is the unary composition.  If `P` has length
`k-1`, its root mass divided by `q_ell` and contextual mean are

```text
mu_(h,P)
 = product_(p in P)w_p
   /[k! w_(ell+1) product_(i=0)^(h-1)b_(B+i)],

f_(h,P)
 = k nu_(a,D,k-1)(0),                              h=0,
 = w_h product_(i=0)^(h-1)b_(B+i)
      [1-nu_(a,D,k)(0)],                            h>0.       (2.4)
```

Empty products have value one.  Direct substitution gives the exact mean
identity

```text
sum_(h,P) mu_(h,P) f_(h,P)=1.                       (2.5)
```

At `ell=6`, (2.3) has

```text
32+16+8+4+2+1+1=64
```

supported rows.  The positive groups have degree ranges

```text
h=0: k=2,...,7
h=1: k=2,...,6
h=2: k=2,...,5
h=3: k=2,...,4
h=4: k=2,3
h=5: k=2
h=6: k=1,
```

giving 22 groups, of which the last 16 are live.  Their 51 nominal positive
attachment ranks are distributed as

```text
20+14+9+5+2+1=51.                                  (2.6)
```

When `s=7`, `B=1`; all 20 ranks at `h=1` have rank-one targets and are
inactive, leaving exactly 31.  Their displayed terminal charge is zero because
the corresponding split equals one.

## 3. Universal full-basin refined-reset identity

For a canonical endpoint

```text
E=(A,c_2,...,c_k),
```

let `B_E` be the basin obtained by refining `A`, and put

```text
c_E=k rho(E),
b_E=rho(B_E),
lambda_E=b_E/c_E
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!](A)_p/A^p.          (3.1)
```

The scalar root coefficient is

```text
C_S=sum_E c_E lambda_E^2=sum_E b_E lambda_E.         (3.2)
```

Let `S_X` be the contextual support at `X`, and call `E` exceptional when
`B_E intersect S_X` is nonempty.  Write

```text
theta_E=sum_(C in B_E)rho(C)(f_X(C)-q_X).
```

For every ordinary endpoint, `f_X` vanishes throughout its basin, so
`theta_E=-q_X b_E`.  Therefore, after harmlessly adding inactive canonical
edges, the nominal reset energy has the exact decomposition

```text
A_0(X)
 <=q_X^2[C_S-sum_(exceptional E)c_E lambda_E^2]
   +sum_(exceptional E)theta_E^2/c_E

 =q_X^2[C_S-sum_(exceptional E)b_E lambda_E]
   +sum_(exceptional E)theta_E^2/c_E.               (3.3)
```

This is the corrected **one-power** subtraction on full basin mass `b_E`.
It must not be confused with M131's rejected `a_E lambda_E^2`, where
`a_E=rho(B_E intersect S_X)`.  Formula (3.3) is also sharper than M140's safe
`a_E lambda_E` subtraction: it removes the complete ordinary baseline before
putting back the exact exceptional square.

For `ell=6`, the exceptional endpoint counts by height are

```text
32+16+8+4+2+1=63.                                  (3.4)
```

Thus (2.3)--(3.3) specify every support row and every exceptional basin without
an omitted table entry.

## 4. A recursive refined envelope valid at every deficit

Define `F_(ell,a,D)` to bound `H(X_(ell,a,D))/q_ell`.  At the terminal boundary
use the accepted all-deficit theorem

```text
F_(0,a,D)=1-q_0.                                    (4.1)
```

For `ell>=1`, divide (3.3) by `q_ell` and denote the result by
`R_(ell,a,D)`.  Then set

```text
F_(ell,a,D)=R_(ell,a,D)
 +sum_(h=1)^ell sum_(P models ell-h) sum_(j=1)^k
    mu_(h,P) nu_(a,D,k)(j) q_(h-1)
    F_(h-1,a+k,D+k-j),                              (4.2)
```

omitting only actual rank-one targets.  Here `k=length(P)+1`; coincident
children may be grouped only after every `j` has appeared.

Induction on `ell` in the accepted finite DAG proves

```text
H(X_(ell,a,D))/q_ell <=F_(ell,a,D).                  (4.3)
```

The key point is that (4.2) is propagated through **right-heavy children as
well as non-right-heavy children**.  Replacing every right-heavy child by its
coarser Bernoulli budget is insufficient at `ell=6`.  Exact arithmetic at
`s=7,K=128` gives

```text
coarse child-budget envelope / target =1.0003190402... >1,
exact H / target                       =0.6265122819... <1.     (4.4)
```

At the polynomial endpoint `z=0`, the same coarse envelope has strictly
negative cleared slack.  Equation (4.4) is therefore a rigorous obstruction
to that induction template, not a counterexample to the desired `H` bound.

## 5. Uniform-in-excess multiaffinity invariant

The refined recurrence exposes an invariant absent from the earlier
exceptional-basin tables.

> **Lemma (multiaffine refined envelope).**  For fixed `ell,a,D,z` and scalar
> coefficients `C_S`, the envelope `F_(ell,a,D)` is multiaffine in the
> consecutive Cayley ratios `(b_(B+ell),...,b_B)`.

**Proof.**  For a basin at height `h`, write

```text
P_h=product_(i=0)^(h-1)b_(B+i),
P_top=product_(i=h)^ell b_(B+i).
```

The normalized source mass in (2.4) is a constant times `1/P_h`, while its
positive contextual contribution is ratio-independent: at `h>0`, the factor
`P_h` in the mean cancels the mass denominator, and at `h=0` neither is
present.  Consequently the normalized exceptional current has the form

```text
Theta_E=alpha_E-gamma_E P_top,
```

and its normalized capacity is `c_E/q_ell=eta_E/P_h`.  In the refined reset,
the quadratic term

```text
Theta_E^2/(c_E/q_ell)
```

is paired with the full ordinary-baseline subtraction

```text
-q_ell^2(c_E/q_ell)lambda_E^2.
```

Because `b_E=c_E lambda_E`, their `P_h P_top^2` terms cancel exactly.  The
remainder is a linear combination of `P_h` and
`q_ell=w_(ell+1)P_hP_top`, both squarefree in all ratios.  The baseline
`q_ell C_S` is also squarefree.  Hence the reset is multiaffine.

For a descendant at height `h`, the product of normalized parent group mass
and child split is

```text
mu_(h,P) q_(h-1),
```

in which `P_h` cancels.  What remains is a ratio-independent coefficient
times the child envelope, which is multiaffine in its bottom `h` ratios by
induction.  Summing proves the lemma. QED.

This lemma applies structurally at every suffix excess.  It does not by itself
prove contraction for `ell>=7`; a sign certificate or analytic inequality is
still required there.

## 6. Denominator and degree bound at excess six

Put

```text
Delta_6(z)=product_(a=1)^6(1+az).
```

Along a history, the attachment offset changes from `a` to `a+k`.  Thus the
denominator segments in (2.1) occupy consecutive subintervals of
`{1,...,6}`.  Squared reset currents require at most two copies of each
factor; descendant products use the remaining consecutive segments.
Induction in (4.2) therefore shows that every denominator divides
`Delta_6(z)^2`.  Tracking numerator degrees in the same induction gives

```text
T_s(z)=Delta_6(z)^2[1-q_6-F_(6,0,1)]               (6.1)
```

as a polynomial of degree at most 14 in `z`.  The generic fourteenth finite
difference is nonzero, so degree 14 is sharp.  Combined with Section 5, the
tail multidegree is

```text
(1,1,1,1,1,1,1,14).                                (6.2)
```

`l6_exact.py` derives (6.2), verifies independent off-grid identities, and
uses exact rational Bernstein transforms.  The analytic denominator and
multiaffinity arguments, rather than an off-grid sample, justify the finite
degree used by interpolation.

## 7. Exact finite certificate, `7<=s<=104`

For every `s=7,...,104`, the checker substitutes the exact consecutive
Cayley ratios and exact scalar values `C_S` at every nonterminal descendant.
It converts (6.1) to degree-14 Bernstein form on `z in [0,1/2]`.

All

```text
98*15=1470
```

coefficients are strictly positive.  The minimum occurs at `s=104`, index
zero, and is approximately

```text
0.08438881398289777.
```

Its full exact fraction is stored in `l6_exact.json`; the digest of all 1470
ordered exact fractions is

```text
12bcb36c2409ede2ae36d8157a10671246c498043e0f6c6a8dc9f081018edde0.
```

Bernstein positivity proves `F_(6,0,1)<1-q_6` on the whole interval, not only
at the discrete values `z=1/(K+1)`.

## 8. Universal tail certificate, `s>=105`

The Cayley ratios `b_n=(n/(n+1))^(n-1)` decrease and satisfy `b_n>1/e>4/11`.
At `s>=105`, the smallest of the seven indices is 99, and exact arithmetic
gives

```text
b_99<187/500.                                       (8.1)
```

Every nonterminal descendant has total rank at least

```text
B+1=s-5>=100.
```

Hence accepted M140/M144 gives `C_S<3/4` at every reset that occurs in
(4.2).  The refined recurrence is increasing in each `C_S`: it appears with
positive coefficient in a reset, and all descendant weights are nonnegative.
Replacing every `C_S` by `3/4` therefore enlarges the envelope.

On

```text
[4/11,187/500]^7 x [0,1/2],
```

the tensor Bernstein expansion at multidegree (6.2) has

```text
2^7*15=1920
```

coefficients.  Every coefficient is positive.  The exact minimum is

```text
11435975715855226131133337
/149750370000000000000000000                       (8.2)
```

at index `(1,1,1,1,1,1,0,0)`, approximately `0.07636692794719123`.  The
ordered coefficient digest is

```text
b2aafe3c93fc583b7ae7dc32fadaf3a46de97dac0fe8ba46f8ace2a6815dec1d.
```

Thus `F_(6,0,1)<1-q_6` for every `s>=105`.  Section 7 covers all smaller
allowed ranks.  Equations (4.3) and (6.1) prove the theorem.

## 9. Independent exact checks and limitations

The checker has two separate finite-DAG paths.  One literally enumerates all
ordered compositions and every active canonical basin.  The other uses the
Cayley forest formula before summing currents.  They agree exactly on resets
and complete resolvents for the six roots

```text
s in {7,8}, K in {1,2,5}.
```

Every root satisfies

```text
exact H <= q F_(6,0,1) < q(1-q).
```

An additional 270 arbitrary-deficit contexts cover

```text
ell=1,...,4; ell+1<=S<=7; 2<=K<=6; 1<=R<K.
```

All exact resolvents lie below the recursive refined envelope.  The largest
exact/envelope ratio is `761/763` at `(S,K,R,B)=(3,4,2,1)`.

The theorem settles only the first open boundary `L=6`.  The multiaffinity
recurrence is reusable, but no sign certificate is supplied for `L>=7` and no
asymptotic all-`L` contraction, auxiliary spectral gap, or original-chain
mixing statement follows.

