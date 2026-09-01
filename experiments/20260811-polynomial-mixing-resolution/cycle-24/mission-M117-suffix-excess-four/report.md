# M117 final report: suffix-excess-four excursion contraction

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: PROMOTE WITH FRESH REFEREE AUDIT.
PROVED CLAIM: complete right-heavy reset-excursion contraction for L<=4.
FIRST UNRESOLVED BOUNDARY: L=5.
```

The project target remains uniform on fixed-length identity words in
`Omega(N,m)`. Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are
displayed left-to-right. This mission concerns only the auxiliary full
**nonlazy stationary-flow parking-degree projection** in the
minimal-long-cycle sector.

Nothing here proves an auxiliary gap, ROOT-MEAN LIFT, the original lazy
`{3,4,5}` heat-bath gap, polynomial mixing, Terminal A, or Terminal B.

```text
candidate                  | full auxiliary reset excursion at L=4
claimed target             | right-heavy unweighted/weighted contraction
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | literal recurrence, child audit, full certificates
verdict                    | prove L=4; universal all-L claim unresolved
```

## 2. Precise theorem and status

For every `s>=5`, `K>=1`, and

```text
x=(s,K,K-1,s-4),
q_x=w_5 w_(s-4)/w_(s+1),
```

the accepted all-`j` finite-DAG recurrence satisfies

```text
H(x)=(I-Q)^(-1)A_0(x)<=q_x(1-q_x).
```

Each weighted reset leaf is its unweighted leaf multiplied by a number in
`[0,1]`, so the accepted positive-history comparison gives `G<=H`.
Right-heaviness gives `U=q(1-q)K/(R+1)=q(1-q)`, hence `G<=U`.

**Status: proved relative to M109/M114's accepted recurrence, basin estimate,
and `L<=2` theorems, and M115/M116's accepted arbitrary-deficit `L=1`
envelope and right-heavy `L=3` theorem.** The proof is universal algebra, not
a finite-rank extrapolation. All four predecessor manifests verified before
freeze.

## 3. Exact support, basins, and reset envelope

Put

```text
r=b_s, u=b_(s-1), v=b_(s-2), y=b_(s-3), x=b_(s-4),
z=1/(K+1),
d=2z^2/(1+z),
e=6z^3/[(1+z)(1+2z)],
f=24z^4/[(1+z)(1+2z)(1+3z)],
q=(125/24)ruvyx.
```

Exactly 16 ordered compositions have nonzero contextual mean:

```text
prefix total 4, last B=s-4:       8 compositions
prefix total 3, last s-3:         4 compositions
prefix total 2, last s-2:         2 compositions
(1,s-1), (s):                     2 compositions.
```

Their exact masses and means are listed in `suffix_excess_four.md`; their
mass-weighted mean is `q`. They occupy 11 positive `(k,t)` groups.

The exceptional canonical basins are exactly all refinements in the four
nonunary prefix families:

```text
8 + 4 + 2 + 1 = 15 basins.
```

The proof note lists, for every basin, its complete supported-source nesting,
`theta_E/q`, and `cap_E/q`. Four endpoints beginning with `(1,1)` are
inactive; adding their nonnegative energy and inactive ordinary edges only
enlarges the bound. The exact supported exceptional path mass is

```text
q[369/625 + 37/(125x) + 4/(25xy) + 12/(125xyv)].
```

Using the accepted `rho(basin)/rho(endpoint)<=degree(endpoint)` bound on all
ordinary basins yields the closed reset envelope

```text
A_0/q <= q[h_0-qS_4] + sum_(15 E)(theta_E/q)^2/(cap_E/q).
```

A separate literal implementation enumerates every ordered composition and
every active canonical basin, with no grouped current formula. On ten rows
`5<=s<=9`, `K in {1,5}`, it exactly equals the grouped reset recurrence and
matches all 11 active exceptional currents and capacities. The number of
literal active basins grows from 11 at `s=5` to 191 at `s=9`.

## 4. New arbitrary-deficit `L=2` proposition

For

```text
X=(S,K_0,R_0,S-2), D=K_0-R_0,
p=D/(K_0+1),
d_0=D(D+1)/[(K_0+1)(K_0+2)],
p'=D/(K_0+2),
R=w_S/w_(S+1), U=w_(S-1)/w_S, Y=w_(S-2)/w_(S-1),
a=UY, q_0=(3/2)RUY,
H_0=(S-1)/(S+1), H_1=(S-2)/S,
```

define

```text
F_1(b,y,h;p)=b(h-b/2)+(2p-b)^2/4+(1-p)(1-y).
```

The new proposition proves

```text
H(X)/q_0 <= R_2+D_2,

R_2=q_0[H_0-5q_0/9-q_0/(3Y)]
    +(3d_0-q_0)^2/27
    +(3d_0+6p-4q_0)^2/54
    +[Y(1-d_0)-q_0]^2/(6Y),

D_2=(1-d_0)(1-Y)/3
    +(2/3)(1-p)F_1(a,Y,H_1;p').
```

The four supported rows are `(2,S-2)`, `(1,1,S-2)`, `(1,S-1)`, and
`(S)`. The first three generate exactly three exceptional basins and every
square in `R_2`. The group `(2,S-1)` sends retained mass to all-deficit
terminal children; the unary group sends mass to an arbitrary-deficit `L=1`
child, preserving `D`. This gives `D_2` with no missing normalization.

The proposition bounds `H/q_0`; it does not claim arbitrary-deficit
contraction. The owned exact audit checks all 252 reachable contexts

```text
3<=S<=9, 2<=K_0<=9, 1<=R_0<K_0.
```

Every support mass, mean, mean identity, reset bound, and full bound passes.
The largest reset-to-envelope and resolvent-to-envelope ratios are about
`.9994582` and `.9973788`, respectively, making this a deliberately tight
audit rather than a superficial scan.

## 5. Full all-rank descendant envelope

Exactly seven root groups send live mass:

```text
(2,3,4;s-3) -> all-deficit L=0,
(2,3;s-2)   -> arbitrary-deficit L=1,
(2;s-1)     -> j=1 deficit-two L=2; j=2 right-heavy L=2,
(1;s)       -> right-heavy L=3.
```

Every `j=1,...,k` is retained before aggregation. Let `nu_k(j)` be the exact
right-heavy attachment law and
`p_(k,j)=(k+1-j)z/(1+kz)`. With
`c_2=(3/2)vyx`, `c_3=(8/3)uvyx`, and `F_2^(2)` the new deficit-two
child envelope, the normalized descendant charge is

```text
D_4=
 (1-x)/125 [18(1-d)+8(1-e)+(1-f)]
 +(12/125) sum_(j=1)^2 nu_2(j)F_1(xy,x,h_1;p_(2,j))
 +( 4/125) sum_(j=1)^3 nu_3(j)F_1(xy,x,h_1;p_(3,j))
 +(18/125)[nu_2(1)F_2^(2)+nu_2(2)(1-c_2)]
 +(64/125)(1-z)(1-c_3).
```

The coefficients are exact cancellations of each parent group mass against
its child split. The `j=2` child at `t=s-1` uses the accepted right-heavy
`L=2` theorem; the unary child uses accepted right-heavy `L=3`. At `s=5`,
the nominal terminal children have rank one and are inactive, while `x=1`
makes their displayed charge zero.

Together with the reset envelope this gives `H/q<=E_4=R_4+D_4`.

## 6. Universal scalar certificate

Set

```text
Delta(z)=prod_(a=1)^4(1+az),
T=Delta(z)^2[1-q-E_4].
```

All apparent inverse Cayley-ratio factors cancel. The result is a polynomial
of multidegree at most

```text
(2,2,2,2,2,10) in (r,u,v,y,x,z).
```

The degree-ten bound is sharp and is independently detected by exact finite
differences.

- For `s=5,...,21`, all `17*11=187` coefficients in the exact degree-ten
  Bernstein basis on `z in [0,1/2]` are positive. The exact minimum is
  `71734022477173585947/9023189417984000000000` at `s=7`, index zero.
- For `s>=22`, all five ratios lie in `[1/3,2/5]`: their smallest index is
  `s-4>=18`, the ratios decrease, exceed `1/3`, and
  `(18/19)^17<2/5`. The three path heights are below one and enter the
  envelope with nonnegative coefficients, so setting all of them to one is
  pessimistic.
- On `[1/3,2/5]^5 x [0,1/2]`, every one of the
  `3^5*11=2673` tensor Bernstein coefficients is positive. The exact minimum
  is `742081/227812500` at index `(2,2,2,2,0,0)`.

The script verifies the finite interpolants and tensor interpolant at
independent off-grid rational points. Positivity proves `E_4<1-q` on every
actual parameter tuple and completes the theorem.

## 7. Exact implementation and reproducibility

`l4_exact.py` is a standalone standard-library `Fraction` implementation. It
imports no predecessor source or output. It reconstructs:

- root groups and contextual means;
- literal supported compositions and canonical basins;
- grouped and literal exact reset energies;
- every individual attachment rank and the finite-DAG resolvent;
- the arbitrary-deficit `L=2` envelope;
- the closed `L=4` envelope;
- finite and tensor Bernstein transforms and off-grid identities.

The durable command is

```text
python3 -B l4_exact.py --s-max 20 --certify --output l4_exact.json
```

run from this directory. It records 80 full L=4 rows for
`K in {1,2,5,64,4096}`, ten literal-reset rows, 252 arbitrary-deficit child
rows, 187 finite coefficients, all 2673 tensor coefficients, and zero
failures. The largest observed exact-resolvent ratio is `.6536992`; the
largest closed-envelope ratio is `.9904517`. These finite extrema audit the
formulas; the polynomial certificate proves universality.

The run used Python 3.12.3, standard-library exact arithmetic, no nonstandard
dependency, and `seed=null`.

## 8. Dependencies, statuses, and strongest self-attack

- **Accepted inputs:** M109/M114's exact all-`j` recurrence, finite descent,
  `beta_E<=degree(E)`, positive-history `G<=H`, all-deficit `L=0`, and
  right-heavy `L<=2`; M115/M116's arbitrary-deficit `L=1` envelope and
  right-heavy `L=3` contraction.
- **Proved here:** the 16-support and 15-basin structure; every reset current
  and capacity; the arbitrary-deficit `L=2` proposition; every descendant
  normalization; the complete universal sign certificate; right-heavy `L=4`
  unweighted and weighted contraction.
- **Exact finite audit only:** the 80 full-DAG rows, ten literal-reset rows,
  and 252 child rows. They validate formulas but do not supply the universal
  inference.
- **Unresolved:** right-heavy contraction beginning at `L=5`, the all-`L`
  excursion, every auxiliary gap and ROOT-MEAN obligation, the original
  heat-bath gap, polynomial mixing, and both project terminals.

The strongest self-attack is the narrow slack in the deliberately loose
envelope: the finite high-`K` envelope ratio reaches `.9904517`, and the tail
tensor minimum is positive but small. Four inactive reset terms are added,
and the exceptional-basin count has doubled. A fresh referee should therefore
rederive all 15 currents, audit the deficit-two child normalization, verify
the height monotonicity and tail threshold, and independently regenerate the
2673 coefficients before acceptance. No pointwise defect induction may be
inserted; the accepted one- and two-layer defect signs remain refuted.

Original-chain cases `m` odd, `m=0`, `m=2`, and `N=2` do not enter this
separated auxiliary lemma and receive no new conclusion.

## 9. Artifacts, verdict, and hygiene

Owned artifacts are

```text
plan.md
checkpoint.md
suffix_excess_four.md
l4_exact.py
l4_exact.json
report.md
SHA256SUMS
```

The final freeze validates source execution, JSON parsing, a fresh `/tmp`
rerun with mathematical-payload equality, whitespace, manifest integrity,
and owned cache hygiene. No predecessor, coordinator note, manuscript,
project skill, or shared source is edited.

```text
FINAL VERDICT: PROMOTE WITH FRESH REFEREE AUDIT.
```
