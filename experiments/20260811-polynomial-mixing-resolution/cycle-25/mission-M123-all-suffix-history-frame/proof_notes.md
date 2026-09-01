# M123 proof notes: complete histories and the basin-frame obstruction

Date: 2026-08-13.  This note concerns only the auxiliary unweighted reset
excursion

```text
H=(I-Q)^(-1)A_0
```

in the minimal-long-cycle parking projection.  It is not a statement about
the original identity-word heat-bath chain.  Permutations compose as
`(pq)(x)=p(q(x))`, and factors are displayed left-to-right.

## 1. Exact recurrence and normalization

For `x=(s,K,R,B)`, put

```text
q_x=w_(s+1-B)w_B/w_(s+1),
rho_s(C)=product_i w_(c_i)/[len(C)! w_(s+1)].
```

If `C` has `k` parts and last part `t`, M65's accepted contextual mean is
`h_x(C)=0` for `t<B`, is its terminal binomial value for `t=B`, and for
`t>B` is

```text
h_x(C)=q_y sum_(j=1)^k nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B),
```

where the displayed `q_y` is independent of `j`.  Every `j=1,...,k` is
retained.  The `j=0` class is a failure class, not a child.  The accepted
closed-mean identity is

```text
sum_C rho_s(C) h_x(C)=q_x.                         (1.1)
```

The deep kernel used here is

```text
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),                   (1.2)
```

with no child/parent `alpha` ratio.  The phase `s+K-R` strictly descends.

## 2. Complete-success-history mass

Define `S(x)` by expanding all terminal and deep marked choices, including
every attachment rank:

```text
S(x)=sum_(k,t=B) rho_s(k,t) h_x(k,t)
    +sum_(k,t>B) rho_s(k,t) sum_(j=1)^k nu_j S(y_j).   (2.1)
```

**Lemma 2.1 (proved).**  For every admissible finite-DAG context,

```text
S(x)=q_x.                                          (2.2)
```

**Proof.**  Induct on the strictly descending phase.  At every child use
`S(y_j)=q_(y_j)`.  The deep summand in (2.1) then equals the deep line of
`h_x(k,t)`.  Adding the terminal line and the zero below-threshold line turns
(2.1) into (1.1).  This proves (2.2).  The induction is finite and inserts
no `alpha` factor.  QED.

This is a mass identity for the normalized successful histories.  By itself
it does not construct their failure complement or prove that the contextual
statistic is a literal Bernoulli indicator.

At `x=(3,1,0,1)`, inserting `alpha_child/alpha_parent` changes `q=9/16` to
`15/16`; inserting its inverse changes it to `7/16`.  These exact witnesses
falsify both extra-alpha normalizations.

## 3. Exact signed two-copy frame equality

For every active canonical endpoint `e`, let `B_e` be the set of source
compositions refining its first part and put

```text
theta_e(x)=sum_(C in B_e) rho_s(C)[h_x(C)-q_x],
c_e=len(e)rho_s(e),
A_0(x)=sum_e theta_e(x)^2/c_e.                     (3.1)
```

Expanding each square gives the algebraic identity

```text
theta_e^2/c_e
 =sum_(C,C' in B_e)
   {rho_s(C)[h_x(C)-q_x]}
   {rho_s(C')[h_x(C')-q_x]}/c_e.                  (3.2)
```

Because `Q` is nilpotent,

```text
H(x)=sum_(a: deep history from x) p(a)A_0(x_a).    (3.3)
```

Substituting (3.2) into (3.3) is the complete signed two-copy expansion of
`H`.  Thus the signed-frame equality is proved universally from the accepted
recurrence; it is not a positivity or orthogonality statement.  The exact
checker independently finds zero equality failures in its bounded all-`j`
audit.

## 4. Canonical reset basins are not categories

At the fresh right-heavy state

```text
x=(s,K,R,B)=(4,1,0,1),
C=(1,1,1,1),
```

the contextual mean is one and `rho_4(C)=1/125`.  Its canonical first-merge
path is

```text
(1,1,1,1) -> (2,1,1) -> (3,1) -> (4).
```

The first displayed endpoint after the source and the next endpoint are both
active.  Hence every successful hidden atom above `C` lies in both basins
`B_(2,1,1)` and `B_(3,1)`.  A first-active-edge assignment changes the
second current from `1647/15625` to `1098/15625`; its resulting energy is
`748477/28125000`, rather than

```text
A_0(x)=1351279/28125000.                           (4.1)
```

The literal ambient `n=6,r=5` checker enumerates the five relevant factor
words, every scan and actual two/three-state pair fibre.  It finds two
favourable word/scan/outcome atoms, total raw rate
`alpha_5=1/30`, normalized contextual value one, and both basin memberships.
Thus finer word, scan, outcome, shuffle, or insertion marks cannot turn the
natural canonical basins into a partition.

## 5. Exact composition-frame obstruction at rank five

On `L2(rho_s)`, define

```text
v_e(C)=1[C in B_e]/sqrt(c_e),
O_(e,f)=rho_s(B_e intersect B_f),
C_(e,f)=c_e 1[e=f].                                (5.1)
```

The Gram matrix is `G=C^(-1/2)OC^(-1/2)`.  The analysis operator is at most
the identity iff `C-O` is positive semidefinite.

At `s=5`, select

```text
e_1=(1,3,1), e_2=(2,2,1), e_3=(3,1,1), e_4=(4,1).
```

The corresponding principal matrix is exactly

```text
C-O = [ 5/108       0        0       -5/216   ]
      [    0     35/1296     0      -25/1296  ]
      [    0        0      49/1296  -41/1296  ]
      [ -5/216  -25/1296  -41/1296    4/81    ].   (5.2)
```

Its determinant is

```text
-27125/235092492288 < 0.                           (5.3)
```

More directly, for

```text
a=(1/2,5/7,41/49,1),
```

one has

```text
a^T(C-O)a = -155/63504,
a^TCa     = 2094265/6223392,
a^TOa     = 2109455/6223392,
(a^TOa)/(a^TCa)=421891/418853 > 1.                (5.4)
```

Therefore `G` has an eigenvalue strictly greater than one.  Exact exhaustive
principal-minor checks prove `C-O` positive semidefinite at `s=2,3,4`; at
`s=5` all 231 principal minors of size at most three are nonnegative and
(5.2) is the first found four-coordinate obstruction.  Floating power
iteration gives `lambda_max approximately 1.039533091512` only as a
calibration; (5.3)--(5.4) certify the sign.

This refutes the universal canonical-basin Bessel/frame inequality.  It does
not refute the inequality for the particular contextual functions generated
by the excursion recurrence.

## 6. What marked pullback does and does not preserve

**Lemma 6.1 (isometric full-space pullback, proved).**  Let `(Omega,mu)` be
a finite marked probability space and `kappa:Omega->Comp(s)` satisfy
`kappa_*mu=rho_s`.  Then `Uf=f composed with kappa` is an isometry from
`L2(rho_s)` into `L2(mu)`.  In particular the pulled vectors `Uv_e` have
exactly the Gram matrix in (5.1), hence the same nonzero Gram spectrum.

**Proof.**  For every `e,f`,

```text
<Uv_e,Uv_f>_mu
 =sum_C mu[kappa=C]1[C in B_e intersect B_f]/sqrt(c_ec_f)
 =O_(e,f)/sqrt(c_ec_f).                            (6.1)
```

QED.

Consequently the natural full marked ambient space (stationary local macro,
then conditional factor word, scan, outcome, and auxiliary marks) inherits
the rank-five obstruction whenever its forgetful marginal is the accepted
`rho_s` and the capacities remain `c_e`.  Any all-history positive frame
which contains these root coordinates also fails: adding descendant
coordinates cannot decrease a positive frame operator.

There is nevertheless an important qualification.  `history_frame_search.py`
constructs only the aggregate successful-history submeasure of total `q`.
If its root pushforward is written

```text
eta_x(C)=rho_s(C)h_x(C),
```

then constant basin vectors have the different overlap matrix

```text
O^succ_x(e,f)
 =sum_C rho_s(C)h_x(C)1[C in B_e intersect B_f].   (6.2)
```

The coarse matrix `O` does not decide (6.2).  Moreover
`theta_e=eta_x(B_e)-q_x rho_s(B_e)` is a difference of two measures, not an
analysis coordinate in `L2(eta_x)` without a new identity.

For a genuinely constructed all-prefix probability space, the exact missing
operator would have coordinates

```text
V_(a,e)(omega)
 =1[omega reaches prefix a]1[kappa_a(omega) in B_e]
  /sqrt(p_a c_e),                                  (6.3)
```

where the prefix has mass `p_a` and conditional local composition law
`rho_(s_a)`.  Its cross-prefix Gram entries are

```text
G^hist_((a,e),(b,f))
 =mu(R_a intersect R_b intersect kappa_a^-1(B_e)
                    intersect kappa_b^-1(B_f))
  /sqrt(p_a p_b c_e c_f).                          (6.4)
```

The current aggregate recursion computes neither the failure atoms nor
(6.4).  If (6.3) is the intended normalized frame, its root block is (5.1)
and is already refuted.  If a success-weighted or otherwise renormalized
frame is intended, its measure, vectors, Gram matrix, and equality to `H`
must first be stated and proved; measure-preserving pullback cannot simply be
asserted for it.

## 7. Consequence and remaining frontier

The complete mass identity, signed two-copy equality, nested-basin collision,
and exact rank-five frame obstruction are all auxiliary structural results.
They close the proposed category/Bessel route negatively.  They leave open

```text
H(x)<=q_x(1-q_x)
```

for arbitrary right-heavy suffix excess.  The accepted theorem remains only
through `L<=4`; `L=5`, all `L`, ROOT-MEAN LIFT, every auxiliary or original
chain gap, and both terminal project outcomes remain unresolved.
