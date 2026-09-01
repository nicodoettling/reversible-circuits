# M82 final report: reset occupation and beta-binomial phase weights

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, exact scope, and conventions

**VERDICT: OPEN AT ONE DEEP-ELIMINATED WEIGHTED RESET LEMMA; RAW
POWER-BELLMAN ROUTES REFUTED.**

Permutations compose as `(pq)(x)=p(q(x))`; factors are displayed
left-to-right. This mission concerns only the full **nonlazy
stationary-flow parking-degree projection** `Pbar_r` in the minimal
factorization sector of `(0 1 ... r)`, with stationary law

```text
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!].
```

It is not a theorem for the original lazy `{3,4,5}` same-product heat-bath
chain on the uniform fixed-length identity-word target `Omega(N,m)`.

The assigned right-heavy statement

```text
[(I-D)^(-1)J_can]1(s,K,K-1,B)<=1                  (1.1)
```

remains **unresolved**. It has no exact finite counterexample in the tested
range. The broader all-reachable-context version is **refuted** exactly,
but its counterexample is not right-heavy and therefore does not refute
(1.1). A more structured weighted statement survives every exact test and
is sufficient for polynomial reset occupation; it is isolated in Field 8.

No `Pbar` gap, ROOT-MEAN LIFT, or conclusion for the original chain `K` is
claimed.

## 2. Exact operator, normalization, and strict phase descent

For a contextual mark `x=(s,K,R,B)`, put

```text
rho_s(C)=product_i w_(c_i)/[k! w_(s+1)],
w_a=a^(a-1)/a!,
q_x=w_(s+1-B)w_B/w_(s+1),
P(x)=s+K-R.
```

M65's closed contextual root mean is `H_x(C)`. For a root composition with
`k` parts and last part `t>B`, attachment rank `1<=j<=k`, and child

```text
y=(t-1,K+k,R+j,B),
```

the exact deep coefficient is

```text
D(x,y)=rho_s(k,t) q_y nu_(K,R,k)(j)/q_x,

nu_(K,R,k)(j)
 =binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

For the first-boundary canonical edge with refined endpoint
`e=(A,c_2,...,c_k)`, basin current `theta_e`, and
`Q_G(e)=rho_s(e)k`, the reset coefficient is

```text
J_can(x,y_e)=theta_e^2/[Q_G(e)q_x],
y_e=(A+c_2-1,k-1,k-2,c_2).                         (2.1)
```

Thus every reset target is right-heavy: `K_y-R_y=1`. Frozen M76/M79 prove
that every `D` and `J_can` child strictly lowers the positive integer `P`.
Consequently

```text
K_reset=(I-D)^(-1)J_can                            (2.2)
```

is a finite DAG sum, not an analytic convergence assumption. The exact
reachable mark closure is

```text
{(K,R)=(1,0)} union {K>R>=1}.                      (2.3)
```

All computations here retain (2.1), including division by parent `q_x`;
no raw or eliminated kernel is silently interchanged.

## 3. A proved split-mass bound and conditional occupation closure

The following elementary bound is new and universal in the active ranks:

> **Split-mass bound.** If `a,b>=1` and `a+b>=3`, then
> ```text
> q(a,b)=w_aw_b/w_(a+b)<=2/3.                       (3.1)
> ```

Proof. Put `n=a+b` and

```text
p=binom(n,a)(a/n)^a(b/n)^b.
```

Then `q=p n/(ab)`. If `a=1`,
`q=((n-1)/n)^(n-2)`, which decreases for `n>=3` and equals `2/3` at
`n=3`: the derivative of `(x-2)log(1-1/x)` is at most
`-1/x+(x-2)/[x(x-1)]<0`, using
`log(1+1/(x-1))>=1/x`. The case `b=1` is symmetric. If `a,b>=2`, the two probabilities
adjacent to the binomial mode `a` have ratios `b/(b+1)` and `a/(a+1)` to
`p`. Hence

```text
p<=[1+b/(b+1)+a/(a+1)]^(-1)<=3/7,
```

while `n/(ab)=1/a+1/b<=1`. This proves (3.1). The excluded pair
`a=b=1` is local rank one, where no active reset child is retained.

Define the beta-binomial phase weight

```text
W(x)=(1-q_x) K/(R+1).                              (3.2)
```

Every reset target is right-heavy, so `W(y)=1-q_y`. By (3.1), every
active reset target satisfies

```text
1/3<=W(y)<=1.                                      (3.3)
```

Suppose the weighted eliminated lemma in Field 8 holds on right-heavy
seeds. If `mu_n=delta_x K_reset^n`, then

```text
mu_n W<=W(x)<=1,
mu_n 1<=3 mu_n W<=3.
```

Strict `P` descent makes `mu_n=0` for `n>=P(x)`. Frozen M71/M76 give the
pure-deep base-excursion bound

```text
b(z)<=e P(z)^2[1+log P(z)].
```

Therefore the weighted lemma would imply the separated marked occupation
bound

```text
sum_(n<P) mu_n b
 <=3e P^3(1+log P).                                (3.4)
```

M71's one-shot `O(r^9)` actual-edge label Cauchy estimate could then be
applied. Equation (3.4) is a **conditional implication**, not a proved
ROOT-MEAN LIFT or `Pbar` gap.

## 4. Exact eliminated-kernel audit and the scope of substochasticity

`reset_substochasticity_audit.py` uses M79's frozen independent
`fractions.Fraction` kernel. Over all 1,015 reachable contexts with

```text
2<=s<=8, 1<=K<=8, 0<=R<K, 1<=B<=s,
R=0 only when (K,R)=(1,0),
```

it finds:

- **Exact finite:** no violation of right-heavy (1.1); its largest row is
  `.538434439350936...` at `(8,1,0,4)`.
- **Exact finite:** no violation of
  `K_reset1<=(K-R)(1-q_x)`; its largest normalized ratio is
  `.621004266940768...` at `(8,1,0,3)`.
- **Exact finite:** no violation of `K_reset W<=W`; its largest normalized
  ratio is `.437150354002130...` at `(8,1,0,4)`.
- **Refuted universally on the full reachable closure:** the unweighted
  row can exceed one away from the right-heavy set. The first stored
  witness is
  ```text
  x=(6,8,1,2),
  K_reset1
   =1205648301042298686456011/1135274399078805562500000
   >1.                                             (4.1)
  ```

The witness (4.1) does not refute repeated reset occupation: every output
of `K_reset` is right-heavy, so non-right-heavy contexts occur only inside
the already eliminated deep excursion. It does show that an all-context
unweighted induction is false.

A separate exact fresh-seed scan through rank eleven gives

```text
max K_reset1=.632621701887196...,
max (K_reset W/W)=.539149961500758... .             (4.2)
```

These are bounded falsifiers only. They do not prove either universal
inequality.

## 5. Raw Bellman inequalities fail, even with phase powers

Full deep elimination is indispensable. Four exact certificates separate
the false one-step templates from the surviving resolvent statement.

1. **Raw constant row, refuted at rank three.** The reachable right-heavy
   context
   ```text
   x=(3,13,12,2)
   ```
   has
   ```text
   D1=13/14,
   J_can1=953/12544,
   (D+J_can)1=12601/12544>1.                       (5.1)
   ```

2. **Raw beta-binomial weight, refuted.** For `U_0=W`, the fresh seed
   `x=(11,1,0,4)` has the exact ratio
   ```text
   (D+J_can)U_0/U_0=1.011824758998902...>1.         (5.2)
   ```

3. **One phase power, refuted.** For
   `U_1=P(1-q)K/(R+1)`, the fresh seed `x=(44,1,0,30)` has the exact ratio
   ```text
   (D+J_can)U_1/U_1=1.001733271840305...>1.         (5.3)
   ```

4. **Two phase powers, refuted rigorously.** For
   `U_2=P^2(1-q)K/(R+1)`, the fresh seed `x=(120,1,0,102)` has parent
   potential
   ```text
   U_2(x)=14550.287347995294... .
   ```
   Summing 1,123 exact deep terms and 8,214,806 exact reset terms after
   rounding **each nonnegative rational term downward** to `10^-30` gives
   the rigorous lower bound
   ```text
   (D+J_can)U_2 >=14608.581358610018...,
   lower bound - U_2(x) >=58.29401061472363...>0.   (5.4)
   ```

The per-term floors make (5.4) an exact rational sign certificate, not a
floating comparison. These results refute only exponents `0,1,2`; no claim
is made for every fixed exponent. More importantly, none refutes
`K_reset W<=W`, because the bad raw deep continuation is precisely what
the resolvent aggregates before the next reset.

## 6. Exact grouped formula and certificate audit

Let a canonical refined endpoint be

```text
e=(A,b,c_3,...,c_(l+1)),
v_e=product_(i=2)^(l+1) w_(c_i),
t=c_(l+1).
```

The basin consists of arbitrary positive `p`-part refinements of `A`.
With

```text
C(A,p)=[z^A]T(z)^p=p A^(A-p-1)/(A-p)!,
S_e=sum_(p=1)^A C(A,p)[H_x(p+l,t)-q_x]/(p+l)!,
```

direct substitution gives

```text
theta_e=v_e S_e/w_(s+1),
Q_G(e)=w_Av_e/[l!w_(s+1)],
theta_e^2/Q_G(e)=v_e l! S_e^2/[w_Aw_(s+1)].        (6.1)
```

Thus the reset coefficient is (6.1) divided by `q_x`. Grouping the tail by
its last part uses the same Cayley coefficient and loses no multiplicity.
The deep group mass is exactly

```text
rho_s(k,t)=w_t C(s-t,k-1)/[k!w_(s+1)].             (6.2)
```

`weighted_bellman_exact.py` implements (6.1)--(6.2) using only rational
arithmetic. It was compared term-for-term with direct composition
enumeration for every `s<=7`, `K<=4`, `0<=R<K`, every `B`, and exponents
`0,1,2`; all comparisons were exact equalities. For the large certificate
(5.4), replacing one enormous common Fraction by individual downward
floors avoids denominator explosion while preserving a rigorous lower
bound.

## 7. Dependencies, probability, and runtime accounting

- **Frozen/accepted M50:** root-composition law, first-boundary canonical
  basins, and exact capacities.
- **Frozen M56 and frozen/refereed M65/M69:** contextual locality, closed
  mean, and exact negative-hypergeometric marked inheritance.
- **Frozen M71:** right-heavy reset geometry, deep contraction, canonical
  base bound, and one-shot `O(r^9)` label multiplicity.
- **Frozen/refereed M76/M79:** strict `P` descent, reachable closure, exact
  resolvent normalization, and the refutation of inverse-split-mass
  superharmonicity.
- **Proved here:** split-mass bound (3.1), exact grouped identity (6.1),
  exact counterexamples (4.1), (5.1)--(5.3), and rigorous lower certificate
  (5.4).
- **Exact finite only:** survival of (1.1), the multitype
  `(K-R)(1-q)` bound, and weighted eliminated superharmonicity in the
  displayed bounded scans.
- **Unresolved:** universal right-heavy (1.1), universal weighted eliminated
  superharmonicity, marked occupation, actual unmarked ROOT-MEAN LIFT, the
  auxiliary `Pbar` gap, and every conclusion for `K`.

All runs are deterministic with seed `null`, Python `3.12.3`, and no
nonstandard dependency. The exact rank-eight and rank-eleven audits each
completed in seconds; the exact rank-44
certificate about 6.6 seconds; and the rigorous rank-120 lower certificate
361.4 seconds. Binary64 discovery scans selected candidates only and support
no promoted claim.

## 8. First unproved lemma and strongest self-attack

The surviving standalone statement is:

> **DEEP-ELIMINATED BETA-BINOMIAL RESET SUPERSOLUTION.** For every active
> reachable right-heavy seed `x=(s,K,K-1,B)`, let `D,J_can` have the exact
> normalization in Field 2 and define `W` by (3.2). Then
> ```text
> sum_y [(I-D)^(-1)J_can](x,y) W(y) <=W(x).         (8.1)
> ```

Because every reset target is right-heavy, (8.1) is equivalently

```text
sum_y K_reset(x,y)(1-q_y)<=1-q_x.                  (8.2)
```

The factor `K/(R+1)` is the positional beta-binomial correction. Under the
full negative-hypergeometric attachment law,

```text
E[(R+J+1)/(K+k+1)]=(R+1)/(K+1),
```

and the reset operation returns the factor in (3.2) exactly to one. This
explains the alignment but is not a proof: reciprocal harmonicity is false,
and the raw Bellman form of (8.1) is refuted by (5.2). Any proof must expose
the cancellation over the complete pure-deep excursion, for example by an
augmented-event filtration or a direct generating-function resolvent
identity.

The strongest self-attack is that every tested raw polynomial repair up to
degree two eventually fails, while the all-context unweighted eliminated
row already fails at (4.1). The finite margins for (8.1) may likewise shrink
or reverse. A valid counterexample must evaluate the fully eliminated
weighted row on a right-heavy seed; none is known.

The alternative stronger statement

```text
K_reset1(x)<=(K-R)(1-q_x)                          (8.3)
```

also survives the exact rank-eight scan. It would imply (1.1) immediately
on right-heavy seeds. It has less direct attachment-harmonic structure than
(8.1), so (8.1) is the recommended next target.

## 9. Artifacts, reproduction, and handoff

Primary artifacts are `plan.md`, `checkpoint.md`, this report, and:

```text
reset_substochasticity_audit.py
exact_reset_audit_s3_k13.json
exact_reset_audit_s8.json
exact_reset_seed_s11.json
weighted_bellman_exact.py
weighted_bellman_d0_s11.json
weighted_bellman_d1_s44.json
weighted_bellman_d2_s120.json
```

Representative commands:

```text
python3 -B reset_substochasticity_audit.py --s-max 8 --k-max 8 \
  --output exact_reset_audit_s8.json

python3 -B weighted_bellman_exact.py \
  --s 44 --K 1 --R 0 --B 30 --exponent 1 \
  --output weighted_bellman_d1_s44.json

python3 -B weighted_bellman_exact.py \
  --s 120 --K 1 --R 0 --B 102 --exponent 2 \
  --lower-bound-digits 30 --output weighted_bellman_d2_s120.json
```

Exact raw-output hashes before final freezing are recorded by the bundle
manifest. The rank-120 certificate records its term counts, scale, exact
parent, exact lower bound, and positive exact lower-minus-parent value.

**Handoff:** do not pursue another raw fixed-power Bellman scan. Prove or
refute the fully deep-eliminated inequality (8.1) using its exact contextual
event interpretation. If (8.1) holds, (3.4) supplies polynomial separated
marked occupation and unlocks M71's one-shot unmarking step. Until then,
the auxiliary comparison and the original heat-bath mixing question remain
open.
