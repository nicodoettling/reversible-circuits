# M116 independent proof audit of frozen M115

## 1. Audited claim, target, and convention

The project target remains the uniform law on fixed-length identity words in
`Omega(N,m)`, with `(pq)(x)=p(q(x))` and factors displayed left-to-right.  The
claim audited here is much narrower: for the auxiliary full nonlazy
stationary-flow parking-degree projection in the minimal-long-cycle sector,

```text
H(s,K,K-1,s-3) <= q(1-q),  s>=4, K>=1.
```

This is an unweighted right-heavy reset-excursion contraction at suffix excess
`L=3`.  The positive-history comparison then gives `G<=H` and, because the
seed is right-heavy, `U=q(1-q)`.  No auxiliary gap, ROOT-MEAN LIFT, original
lazy `{3,4,5}` heat-bath gap, polynomial mixing theorem, Terminal A, or
Terminal B is part of the claim.

## 2. Frozen provenance gate

Before the mathematical audit, `sha256sum -c SHA256SUMS` succeeded for every
M115-owned artifact.  The observed frozen hashes are

```text
e40b17baeee3f410ffa65b3f43b339772dc23b86ebf85b43ddedf957fb310ecc  checkpoint.md
c78456397be02642800a45295a261e4c0f36d49c8c95a9e763a268d4e46412fb  independent_l3_audit.json
79a4259923fbe6dd0018bca3eea5ca0cae5c96150c68dbe333351cad881ec39e  independent_l3_audit.py
444d424b20d0b4f7122c3a6ed6084142b5ce701eececa654ad1fd914eb56406d  l3_exact.json
ff3d2d286c898e1c5d8da074f5d4b797c33ff31b43bd9377440c361a11a6edac  l3_exact.py
ac17baddbdb88d876460580b1f576424cef9d4011632f31d0dddd97183ba98c0  plan.md
30a72149e1213eee3a8eb287db1f6f7f5d649f2cf9aa46b3c0f99b92d46441d5  report.md
b12ee541ceee4e195d9741fe3956fa668c22d8c8fe0859ea99232b00ba3c1835  suffix_excess_three.md
56512f2f7808395047a020e280acd7d6a2c45deaa5058957b2a831eb7cd7af81  symbolic_discovery.py
199499d29ffbe7937bf18d0786380c4623b856603e11c3a99c2032ff114bfb2f  SHA256SUMS
```

No M115 artifact was edited.

## 3. Exact all-rank recurrence and root support

The accepted recurrence from M109/M114 is

```text
H(x)=A_0(x)+sum_y Q(x,y)H(y),
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),  j=1,...,k,
y=(t-1,K+k,R+j,B).
```

Only `j=0` and children with auxiliary rank `t-1<2` are killed.  For every
retained child,

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,
L(x)-L(y)=s-t+1>=1,
```

so the recursion is a finite DAG.  The fresh reconstruction enumerates each
ordered composition separately and retains each individual `j`; it does not
use M115's grouped helper functions.

For `B=s-3`, positivity of the contextual mean leaves four possibilities for
the last part.  If `t=B`, the prefix is an ordered composition of three; if
`t=s-2`, it is a composition of two; if `t=s-1`, it is the singleton prefix;
and if `t=s`, it is empty.  Thus the support is exactly

```text
(3,B), (1,2,B), (2,1,B), (1,1,1,B),
(2,s-2), (1,1,s-2), (1,s-1), (s).
```

With

```text
q=(8/3)ruvy, z=1/(K+1),
d=2z^2/(1+z), e=6z^3/[(1+z)(1+2z)],
```

direct substitution independently gives M115's eight masses and means:

```text
composition       mass             mean
(3,B)             9q/32            2z
(1,2,B)           q/16             3d
(2,1,B)           q/16             3d
(1,1,1,B)         q/64             4e
(2,s-2)           3q/(16y)         y(1-d)
(1,1,s-2)         q/(16y)          y(1-e)
(1,s-1)           3q/(16vy)        vy(1-d)
(s)               r                (3/2)uvy(1-z).
```

Their mass-weighted mean is exactly `q`.  Literal checks at `(s,K)=(4,1)`,
`(5,2)`, and `(7,5)` reproduce all eight rows and the seven positive `(k,t)`
groups.

## 4. Seven canonical basins and ordinary-height subtraction

For endpoint `E=(A,c_2,...,c_k)`, its canonical basin consists of
`(alpha,c_2,...,c_k)` for every ordered composition `alpha` of `A`.  Intersecting
these basins with the eight supported sources gives exactly

```text
(1,1,1,B): {(1,1,1,B)}
(2,1,B):   {(2,1,B),(1,1,1,B)}
(1,2,B):   {(1,2,B)}
(3,B):     {(3,B),(1,2,B),(2,1,B),(1,1,1,B)}
(1,1,s-2): {(1,1,s-2)}
(2,s-2):   {(2,s-2),(1,1,s-2)}
(1,s-1):   {(1,s-1)}.
```

There is no eighth exceptional basin.  Counting supported source mass with
its canonical-path multiplicity gives

```text
q[37/64+5/(16y)+3/(16vy)].
```

Writing `theta_E=sum_{C in B_E}rho(C)(f(C)-q)` and
`cap_E=k rho(E)`, literal current and capacity evaluation gives

```text
endpoint          theta_E/q                              cap_E/q
(1,1,1,B)         (4e-q)/64                              1/16
(2,1,B)           (12d+4e-5q)/64                         3/16
(1,2,B)           (3d-q)/16                              3/16
(3,B)             (36z+24d+4e-27q)/64                    9/16
(1,1,s-2)         [y(1-e)-q]/(16y)                       3/(16y)
(2,s-2)           [4y-3yd-ye-4q]/(16y)                   3/(8y)
(1,s-1)           3[vy(1-d)-q]/(16vy)                    3/(8vy).
```

Squaring and dividing by the displayed capacities yields all seven terms in
M115 equation (3.2), including denominators `256,768,48,2304,48y,96y`, and
`32vy/3` respectively.

The ordinary-basin subtraction is valid in the required direction.  The
total canonical path mass is

```text
sum_C rho(C)(degree(C)-1)=(s-1)/(s+1)=hbar.
```

If `Exc` is the set of seven exceptional basins, then

```text
sum_(ordinary E) rho(B_E)
 =hbar-sum_(E in Exc)rho(B_E)
 <=hbar-sum_(E in Exc)sum_(supported C in B_E)rho(C).
```

Thus subtracting only the displayed supported occurrences enlarges the
ordinary contribution and is a legitimate upper bound after
`beta_E<=degree(E)`.  The endpoints beginning in `(1,1)` are inactive reset
targets, but adding their nonnegative square energies and including inactive
ordinary edges can only enlarge `A_0`.

## 5. Arbitrary-deficit `L=1` child lemma

For `X=(S,K_0,R_0,S-1)`, put

```text
D=K_0-R_0, p=D/(K_0+1),
y_0=w_(S-1)/w_S, b_0=w_(S-1)/w_(S+1), h_0=(S-1)/(S+1).
```

The only supported compositions are `(1,S-1)` and `(S)`, with masses
`b_0/2,b_0/y_0` and means `2p,y_0(1-p)`.  Their weighted mean is `b_0`.
The former is the sole exceptional singleton basin, so

```text
A_0<=b_0^2(h_0-b_0/2)+(b_0/4)(2p-b_0)^2.
```

For the unary group, the killed mass is

```text
nu(0)=(K_0-R_0)/(K_0+1)=p,
```

and the retained mass is `nu(1)=1-p`.  Its child is
`(S-1,K_0+1,R_0+1,S-1)`: the deficit remains exactly `D`, and the child is
suffix-terminal with split `y_0`.  M109/M114's accepted `L=0` theorem applies
to every reachable deficit, so the deep charge is

```text
(b_0/y_0)(1-p)y_0(1-y_0)=b_0(1-p)(1-y_0).
```

Consequently the claimed bound is exactly

```text
H(X)/b_0 <= b_0(h_0-b_0/2)+(2p-b_0)^2/4+(1-p)(1-y_0).
```

The normalization is `H/b_0`, not `H/[b_0(1-b_0)]`.  At `S=2`, both actual
targets have rank one and are inactive; `y_0=1`, so the added deep charge is
zero and the upper bound remains valid.  The fresh literal recurrence checks
all 168 contexts `2<=S<=7`, `2<=K_0<=8`, `1<=R_0<K_0`, including every
deficit allowed by those ranges, with zero failures.

## 6. Parent normalization and all descendants

The four possible live groups are

```text
(2,s-2), (3,s-2), (2,s-1), (1,s).
```

For `(2,s-1)`, the parent attachment masses are

```text
nu_1=2z(1-z)/(1+z), nu_2=(1-z)/(1+z),
```

and the children have deficits two and one.  Since their new `K_0+1` is
`K+3`, their attachment parameters are exactly

```text
p_1=2/(K+3)=2z/(1+2z),
p_2=1/(K+3)=z/(1+2z).
```

Both child splits are `b=vy`.  Multiplying `H(child_j)<=bF(p_j)` by the
parent mass `3q/(16b)`, summing the two ranks, and dividing by `q` gives
precisely

```text
(3/16)[nu_1F(p_1)+nu_2F(p_2)].
```

There is no missing factor of `b`, `1-b`, or `q`.  The two terminal groups
give `[3(1-d)+(1-e)](1-y)/16`.  The unary group has a right-heavy `L=2`
child of split `c=(3/2)uvy`, and `(r/q)c=9/16`, giving
`(9/16)(1-z)(1-c)`.  These are exactly M115 equation (5.2).

At `s=4`, the nominal `(2,s-2)` and `(3,s-2)` children have rank one and are
inactive.  Here `y=w_1/w_2=1`, so both displayed upper-bound charges vanish.
At `K=1`, `z=1/2`; the attachment laws are finite and, for the `k=2` and
`k=3` groups, reduce to the expected fresh uniform laws.

## 7. Independent Bernstein certificates

The exact envelope has only denominators from `(1+z)` and `(1+2z)`.  Every
apparent `1/y` or `1/(vy)` cancels because `q` contains the factor `ruvy` and
the corresponding square numerators contain `y` or `vy`.  Therefore

```text
T=1728(1+z)^2(1+2z)^2[1-q-E]
```

is polynomial, of degree at most two in each of `r,u,v,y` and at most six in
`z`.  M116 reconstructs coefficients by forward differences, Newton
polynomials, and power-to-Bernstein conversion, independently of M115's
Lagrange matrix.

For every `s=4,...,20`, the seventh forward difference vanishes exactly and
all seven degree-six Bernstein coefficients on `z in [0,1/2]` are positive.
All 119 fresh coefficients equal M115's frozen coefficients as exact
numerator/denominator pairs.

For the tail, let `b_n=(n/(n+1))^(n-1)`.  The function
`(x-1)log(1+1/x)` is increasing because

```text
log(1+1/x)>1/(x+1)>(x-1)/[x(x+1)],
```

so `b_n` decreases.  Also `b_n>1/3`, while the exact inequality
`b_18=(18/19)^17<2/5` holds.  Hence all four actual consecutive ratios for
`s>=21` lie in `[1/3,2/5]`.  Replacing `hbar,h1` by one enlarges the envelope
because both enter with nonnegative coefficients.

On `[1/3,2/5]^4 x [0,1/2]`, M116 verifies the asserted multidegree through
837 exact full-grid forward-difference slices and independently derives all
567 tensor Bernstein coefficients.  Every coefficient is positive.  The
exact minimum is

```text
682328/28125 at (2,2,2,0,0),
```

and all 567 exact fractions equal M115's frozen output.  Positivity of the
Bernstein basis therefore proves the scalar sign on the full box, not merely
at sampled points.

## 8. Fresh exact finite-DAG reconstruction

The primary owned command is

```text
python3 -B independent_m115_referee.py \
  --output independent_m115_referee.json \
  --reference-json ../../cycle-23/mission-M115-suffix-excess-three/l3_exact.json
```

The program computes every fresh quantity before reading the reference JSON.
A separate fresh-only run, with no predecessor file read at all, produced
zero failures and SHA-256
`242a1e76892b8e33f255b901b1a565b2d602549cbcf5d3414bede6cd95be7a40`
for its `/tmp` output.  The durable output includes the post-hoc equality
gate and has SHA-256
`04d0af726caa88a964f9bd7c605fff7da0b641b61e783cc793b4d2da22115c4f`.

The literal reconstruction checks 15 complete `L=3` DAGs for
`4<=s<=8`, `K in {1,2,5}`.  All satisfy

```text
exact reset <= reset envelope,
exact resolvent <= full envelope <= q(1-q).
```

The largest exact resolvent ratio in these rows is `.5742599506...`, and the
largest envelope ratio is `.8707861320...`, both at `(s,K,R,B)=(8,1,0,5)`.
For the requested corner `(4,1,0,1)`, the retained ranks are exactly

```text
(k,t,j)=(1,4,1),(2,3,1),(2,3,2),
```

and

```text
H/[q(1-q)] = 44975303/224870400 = .2000054386...,
envelope/[q(1-q)] = 1326997/2928000 = .4532093579....
```

Finally, rerunning M115's literal source from `/tmp` reproduced its frozen
JSON hash `c7845639...` exactly.  Rerunning `l3_exact.py` reproduced its
entire mathematical payload exactly after removing only the recorded elapsed
time field.

## 9. Conclusion

No omitted support composition, exceptional basin, live rank, descendant
normalization, or certificate coefficient was found.  The proof correctly
uses the accepted M109/M114 recurrence, canonical-basin estimate, universal
all-deficit terminal theorem, and right-heavy `L<=2` theorem.  Its scope ends
at auxiliary right-heavy suffix excess `L=3`; `L=4` and every gap/mixing
obligation remain unresolved.

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

