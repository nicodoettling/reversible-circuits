# M115 final report: suffix-excess-three excursion contraction

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: PROMOTE WITH FRESH REFEREE AUDIT.
PROVED CLAIM: complete right-heavy reset-excursion contraction for L<=3.
FIRST UNRESOLVED BOUNDARY: L=4.
```

The project target remains uniform on fixed-length identity words in
`Omega(N,m)`.  Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are
displayed left-to-right.  This mission concerns only the auxiliary full
**nonlazy stationary-flow parking-degree projection** in the minimal-long-cycle
sector.

Nothing here proves an auxiliary gap, ROOT-MEAN LIFT, the original lazy
`{3,4,5}` heat-bath gap, polynomial mixing, Terminal A, or Terminal B.

```text
candidate                 | full auxiliary reset excursion at L=3
claimed target            | right-heavy unweighted/weighted contraction
identity ok               | not a sampler-generation claim
crosses Hurwitz components| not applicable to this quotient operator
exact diagnostics         | two exact implementations; complete certificates
verdict                    | prove L=3; universal all-L claim unresolved
```

## 2. Precise theorem and status

For every `s>=4`, `K>=1`, and

```text
x=(s,K,K-1,s-3),
q_x=w_4 w_(s-3)/w_(s+1),
```

the accepted all-`j` recurrence satisfies

```text
H(x)=(I-Q)^(-1)A_0(x)<=q_x(1-q_x).
```

Since each weighted reset leaf is its unweighted leaf times a number in
`[0,1]`, `G<=H` term by term.  Right-heaviness gives
`U=q(1-q)K/(R+1)=q(1-q)`, hence `G<=U` as well.

**Status: proved relative to the accepted M109/M114 recurrence, basin estimate,
and `L<=2` theorems.**  The proof is analytic with finite exact algebraic
certificates; it is not a finite-rank extrapolation.

## 3. Exact support and exceptional basins

Writing

```text
r=w_s/w_(s+1), u=w_(s-1)/w_s,
v=w_(s-2)/w_(s-1), y=w_(s-3)/w_(s-2),
a=uvy, b=vy, c=(3/2)a, q=(8/3)ruvy,
z=1/(K+1), d=2z^2/(1+z),
e=6z^3/[(1+z)(1+2z)],
```

there are exactly eight supported root compositions:

```text
(3,B), (1,2,B), (2,1,B), (1,1,1,B),
(2,s-2), (1,1,s-2), (1,s-1), (s),   B=s-3.
```

Their exact masses and means are displayed in `suffix_excess_three.md`; their
mean is `q`.  They occupy exactly seven nested exceptional canonical basins:

```text
(1,1,1,B) subset (2,1,B) subset (3,B),
(1,2,B)   subset (3,B),
(1,1,s-2) subset (2,s-2),
(1,s-1).
```

The exceptional supported path mass, with nesting multiplicity, is

```text
q[37/64+5/(16y)+3/(16vy)].
```

Exact current/capacity evaluation gives seven square terms.  All remaining
basins use the accepted `beta_E<=degree(E)` estimate.  This produces the
closed reset envelope `A_0/q<=R_s(z)` in equation (3.2) of the proof note.
The two rank-one exceptional reset targets, and inactive ordinary targets,
are added only as nonnegative upper-bound terms.

## 4. New non-right-heavy one-layer proposition

The proof-critical new point is that the live group `(2,s-1)` has one child
of deficit two, outside M109's right-heavy `L=1` theorem.  A direct proposition
handles any reachable `L=1` context

```text
X=(S,K_0,R_0,S-1), D=K_0-R_0,
p=D/(K_0+1), y_0=w_(S-1)/w_S,
b_0=w_(S-1)/w_(S+1), h_0=(S-1)/(S+1):

H(X)/b_0 <= b_0(h_0-b_0/2)+(2p-b_0)^2/4
             +(1-p)(1-y_0).                       (4.1)
```

Exactly two root compositions are supported: `(1,S-1)` has mass `b_0/2`
and mean `2p`; `(S)` has mass `b_0/y_0` and mean `y_0(1-p)`.  The former is
the sole exceptional basin.  The unary group is the sole deep group, of live
mass `1-p`; its child is suffix-terminal with the same deficit `D`.  It is
right-heavy iff `D=1`, but the accepted terminal theorem applies to every
reachable deficit.  This proves (4.1).

The normalization is `H/b_0`, not `H/[b_0(1-b_0)]`.  In the parent group,
whose mass is `3q/(16b)`, the child factor `b` cancels and gives exactly

```text
(3/16)[nu_1 F(p_1)+nu_2 F(p_2)],
nu_1=2z(1-z)/(1+z), nu_2=(1-z)/(1+z),
p_1=2z/(1+2z),      p_2=z/(1+2z).
```

## 5. Full all-j descendant envelope

Exactly four root groups send live mass:

```text
(2,s-2): j=1,2 -> L=0,
(3,s-2): j=1,2,3 -> L=0,
(2,s-1): j=1,2 -> general-attachment L=1,
(1,s):   j=1 -> right-heavy L=2.
```

Every rank is retained before aggregation.  The first two use the accepted
all-deficit terminal theorem; the last uses M109/M114's right-heavy `L=2`
theorem.  Together with (4.1), their normalized charge is the closed
`D_s(z)` in equation (5.2).  Consequently

```text
H(x)/q<=E_s(z):=R_s(z)+D_s(z).
```

At `s=4`, the nominal first two groups have rank-one inactive children; their
envelope charge is exactly zero because `y=1`.

## 6. Universal scalar certificate

The cleared slack

```text
T_s(z)=1728(1+z)^2(1+2z)^2[1-q-E_s(z)]
```

is a polynomial of degree at most six.

- For `4<=s<=20`, every coefficient in its exact degree-six Bernstein basis
  on `[0,1/2]` is positive: 119 coefficients total.
- For `s>=21`, the four consecutive Cayley ratios lie in `[1/3,2/5]` because
  they are decreasing, exceed `1/3`, and `(18/19)^17<2/5`.  Replacing both
  path-height factors by one enlarges `E_s`.  The enlarged cleared slack has
  multidegree `(2,2,2,2,6)` in `(r,u,v,y,z)`.  All 567 exact tensor-Bernstein
  coefficients on `[1/3,2/5]^4 x [0,1/2]` are positive; the minimum is
  `682328/28125` at index `(2,2,2,0,0)`.

Therefore `E_s(z)<1-q` for every `s>=4`, `0<=z<=1/2`, which proves the
theorem.  All coefficients, not merely their minima, are stored in
`l3_exact.json`.

## 7. Exact implementations and reproducibility

`l3_exact.py` is a standalone standard-library `Fraction` implementation of
the grouped root law, scalar reset energy, all-`j` recurrence, envelope, and
both complete certificate families.  Command:

```text
python3 -B l3_exact.py --s-max 20 --output l3_exact.json
```

It records 68 bounded rows (`4<=s<=20`, `K in {1,2,5,64}`), 17 finite
certificates, all 567 asymptotic coefficients, and zero failures.  The largest
actual full-resolvent ratio is `.6066269000...`; the largest envelope ratio is
`.9582756891...`.

`independent_l3_audit.py` is a second implementation path.  It enumerates
ordered compositions literally, constructs each canonical basin from every
refinement of its first part, computes current/capacity energy directly, and
recursively retains every individual `j`.  Command:

```text
python3 -B independent_l3_audit.py
```

It covers all 56 right-heavy contexts `4<=s<=10`, `1<=K<=8`, with exact

```text
reset <= reset envelope,
resolvent <= complete envelope <= target
```

and zero failures.  On the 21 rows shared by both scripts, exact
numerator/denominator comparisons match for both resolvent and envelope
ratios.

Both proof scripts use Python 3.12.3, no nonstandard dependency, and
`seed=null`.  `symbolic_discovery.py` is an optional derivational aid using
SymPy 1.12; no theorem or certificate relies on floating point or on that
script.

## 8. Dependencies, statuses, and strongest self-attack

- **Accepted inputs:** M109/M114's exact all-`j` finite-DAG recurrence,
  positive-history `G<=H`, root-composition/contextual/attachment formulas,
  canonical-basin estimate, universal all-deficit `L=0` theorem, and
  right-heavy `L<=2` theorem.
- **Proved here:** the exact `L=3` support, seven-basin nesting and currents,
  general-attachment `L=1` proposition, four-group all-`j` descendant
  envelope, exact universal scalar sign, and right-heavy contraction for
  `L=3`.
- **Exact computational audit:** bounded resolvent comparisons and all finite
  and tensor-Bernstein coefficients.
- **Unresolved:** all-`L` full-excursion contraction beginning at `L=4`, every
  auxiliary gap/ROOT-MEAN obligation, the original heat-bath gap, and both
  terminals.

The strongest self-attack is the exceptional-basin combinatorics: the number
and nesting grow with `L`, and the present eight-support calculation offers no
uniform organization.  The second literal implementation reduces the risk of
an omitted basin or rank at `L=3`, but a fresh referee should independently
rederive all seven currents and the non-right-heavy normalization before the
claim is accepted.

## 9. Artifacts, verdict, and hygiene

Owned artifacts are:

```text
plan.md
checkpoint.md
suffix_excess_three.md
l3_exact.py
l3_exact.json
independent_l3_audit.py
independent_l3_audit.json
symbolic_discovery.py
report.md
SHA256SUMS
```

The final freeze validates source compilation, JSON parsing, exact reruns,
cross-implementation equality, whitespace, manifest verification, and owned
cache hygiene.  No predecessor, coordinator note, manuscript, project skill,
or shared source is edited.

```text
FINAL VERDICT: PROMOTE WITH FRESH REFEREE AUDIT.
```
