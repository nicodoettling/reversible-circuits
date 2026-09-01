# M109 final report: full reset excursion and suffix-boundary theorem

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, scope, and conventions

**VERDICT: PROMOTE THE COMPLETE SUFFIX-BOUNDARY CONTRACTION FOR
`L=s-B<=2`; KEEP THE UNIVERSAL FULL-EXCURSION CONTRACTION UNRESOLVED.**

The proved result is an analytic all-`s`, all-right-heavy theorem for the
first three suffix-excess sectors, not a finite extrapolation. No exact
counterexample to the global full-excursion inequality was found.

This mission concerns only the full **nonlazy stationary-flow parking-degree
projection** `Pbar_r` in the minimal long-cycle sector. “Suffix-terminal”
below means `L=0` in its reset DAG; it is unrelated to project Terminal A or
Terminal B. Nothing here proves an auxiliary `Pbar` gap, ROOT-MEAN LIFT,
marked occupation beyond accepted conditional implications, a slow mode, or
a gap/mixing result for the original lazy `{3,4,5}` identity-word heat-bath
chain.

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are displayed
left-to-right. The project target law remains uniform on fixed-length
identity words, but the present operator is only an auxiliary projection.

```text
candidate              | full reset excursion of auxiliary Pbar
claimed target         | right-heavy unweighted/weighted contraction
identity ok            | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics      | four frozen calibrations; exact L<=2 certificates
verdict                | proved for L<=2; universal claim unresolved
```

## 2. Exact recurrence, reachability, and finite DAG

An active reachable context is

```text
x=(s,K,R,B),  s>=2, 1<=B<=s,
{(K,R)=(1,0)} union {K>R>=1}.
```

Put

```text
w_a=a^(a-1)/a!,
q_x=w_(s+1-B)w_B/w_(s+1),
U(x)=q_x(1-q_x)K/(R+1),
c(n,p)=p n^(n-p-1)/(n-p)!, c(0,0)=1,
rho_s(k,t)=w_t c(s-t,k-1)/(k!w_(s+1)),
nu_(K,R,k)(j)=binom(R+j,j)
 binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

Every live deep child is

```text
y=(t-1,K+k,R+j,B),  t>B, t-1>=2, j=1,...,k,
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j).
```

Every `j=1,...,k` is retained; `j=0` and inactive children are killed. The
accepted progress and the new suffix excess both strictly descend:

```text
P=s+K-R,   P(x)-P(y)=s-t-k+j+1>=j>=1,
L=s-B,     L(x)-L(y)=s-t+1>=1.
```

Thus `Q` is nilpotent and every resolvent is an exact finite sum. If `A_0`
is unweighted canonical reset energy and `A` weights each reset leaf by
`1-q_leaf`, exact Schur elimination gives

```text
H=A_0+QH=(I-Q)^(-1)A_0=q_x K_reset 1,
G=A+QG=(I-Q)^(-1)A=q_x K_reset W,
K_reset=(I-D)^(-1)J_can,
W(x)=(1-q_x)K/(R+1).
```

Fresh attachment is exactly uniform,
`nu_(1,0,k)(j)=1/(k+1)` for `j=0,...,k`. At `B=s`, `Q=0`.

## 3. Selected global lemma and implication

The falsifiable mission target was the genuinely whole-excursion statement

> For every active reachable right-heavy `x=(s,K,K-1,B)`,
> `H(x)<=q_x(1-q_x)`.

Every reset target is right-heavy, hence its leaf weight is
`W(y)=1-q_y<=1`. Therefore this unweighted lemma implies term by term

```text
G(x)<=H(x)<=q_x(1-q_x)=U(x).
```

The target compares only after all depths have been aggregated. It assumes
neither M98/M99's refuted nonfresh one-step defect sign nor M103/M106's
refuted two-layer sign `(I+Q)r_U>=0`. The global lemma remains unresolved,
but it is proved here on every sector `L<=2`.

## 4. Proved analytic results

### 4.1 Canonical-basin sharpening

For a canonical edge with refined endpoint
`e=(A,c_2,...,c_k)`, `k=ell+1`, and source basin `B_e`, the accepted exact
formula and Cayley coefficient give

```text
rho(B_e)/rho(e)
 =k!/w_A sum_p c(A,p)/(p+ell)! <=k.                 (4.1)
```

Indeed `c(A,p)/w_A<=p` and
`sum_p p ell!/(p+ell)!<=sum_p p/(p+1)!=1`. This improves the
constant-`e` density estimate in precisely the capacity normalization needed
here.

### 4.2 Suffix-terminal and one-layer sectors

At `L=0`, only the unary root composition has nonzero contextual mean and
`Q=0`. Bound (4.1) and the exact binomial root-degree mean give

```text
H=A_0<=q^2(s-1)/(s+1)<=q(1-q),
q=(s/(s+1))^(s-1).                                 (4.2)
```

The last inequality is equivalent to
`2(s/(s+1))^s<=1`.

At `L=1`, only `(1,s-1)` and `(s)` have nonzero contextual mean, and only
the unary group has a live deep child; that child is suffix-terminal. With
`r=w_s/w_(s+1)`, `u=w_(s-1)/w_s`, `q=ru`, and `z=1/(K+1)`, the complete
excursion reduces to the convex quadratic

```text
f(z)=z^2-z(q+1-u)+q[1+(s-1)/(s+1)]-u-q^2/4.
```

Both endpoints `z=0,1/2` are nonpositive. The exceptional case `s=2` has
no active reset or deep target, so `H=0`. This proves contraction for every
right-heavy `L=1` context.

### 4.3 Suffix excess two

For `B=s-2`, exactly four root compositions have nonzero contextual mean:

```text
composition   mass       contextual mean
(2,B)         q/3        2z
(1,1,B)       q/9        3d
(1,s-1)       q/(3v)     v(1-d)
(s)           r          a(1-z),
```

where

```text
r=w_s/w_(s+1), u=w_(s-1)/w_s, v=w_B/w_(s-1),
a=uv, q=(3/2)ruv, z=1/(K+1), d=2z^2/(1+z).
```

Only deep groups `(k,t)=(2,s-1)` and `(1,s)` survive. The former retains
both `j=1,2` children, which are suffix-terminal; the latter retains its
`j=1` child, which has `L=1`. Charging these children by (4.2) and the
one-layer theorem yields an explicit rational envelope
`H/q<=E_s(z)`. Its derivative satisfies

```text
9(1+z)^3 E_s'(z)=N_s(z),
N_s(z)=(12v+72)z^4+(6a-14q+24v+156)z^3
 +(18a-42q+36)z^2+(18a-36q-18)z+(6a-8q-6).
```

The accepted split bound `a,q<=2/3` gives `N_s''>0` and `N_s(0)<0`, so
`E_s` has no interior maximum. Its endpoint slacks reduce to two explicit
polynomials. For `s>=10`, their lower bounds are the positive polynomials

```text
p(u)=12u^5+9u^4-60u^2+16u+4,
m(u)=108u^6+81u^5-360u^3+72u^2+32u+24
```

on `u in [1/3,7/16]`; the derivative needed to obtain the second lower
bound is also positive there. Exact Bernstein coefficients prove all three
signs. The remaining `3<=s<=9` are closed by exact degree-four Bernstein
certificates in `boundary_exact.json`. Therefore

```text
H(x)<=q_x(1-q_x),  G(x)<=U(x)                      (4.3)
```

for every active right-heavy context with `L<=2`. The complete formulas and
all coefficients are in `excursion_reduction.md`.

## 5. Exact audits and bounded diagnostics

`boundary_exact.py` is a standalone standard-library `Fraction`
implementation; it imports no predecessor experiment and retains every live
attachment rank. It exactly reproduces four frozen complete-resolvent ratios:

```text
weighted   (8,1,0,4): .43715035400213015...
weighted  (11,1,0,5): .5391499615007582...
unweighted (8,1,0,3): .6210042669407680...
unweighted(11,1,0,4): .6947437905621655...
```

It then checks with exact signs:

- 60 `L=0/1` rows, `2<=s<=16`, `K in {1,2,5,64}`;
- 56 `L=2` rows, `3<=s<=16`, the same `K`, verifying
  `actual resolvent <= analytic envelope <= target`;
- the envelope polynomial identity for every one of those `L=2` rows;
- all five Bernstein coefficients for each finite `s=3,...,9` certificate;
- every coefficient of the three asymptotic Bernstein certificates.

There are zero failures. The largest actual `L=2` ratio in this targeted
audit is `.5171121551284000...` at `(16,1,0,14)`; the largest envelope ratio
is `.9558812610337982...` at `(16,64,63,14)`. These rows audit formulas;
analytic completeness comes from Section 4.

A fresh referee should audit the `L=2` theorem in this exact order:

1. the four-support table, including all four stationary masses and means;
2. exceptional-basin occurrence accounting `5q/9+q/(3v)` and every factor
   in reset envelope (6.1) of `excursion_reduction.md`;
3. the two live groups and all retained `j=1,2` and `j=1` masses leading to
   the descendant charge (6.2);
4. the cleared derivative polynomial `N_s`, its `N_s''>0` shape argument,
   and the conclusion that only endpoints can maximize `E_s`;
5. the monotonic reductions of the two endpoint numerators to `p,j,m`;
6. both the seven finite Bernstein identities and the three interval
   Bernstein coefficient lists.

A separate interrupted binary64 discovery check completed only the fresh
rows `s=35,B=9` and `s=40,B=11`. The unweighted ratios were
`.8395444045...` and `.8474765622...`; the weighted ratios were
`.7502804485...` and `.7649862014...`. They are retained only as discovery
data and prove no sign.

## 6. Dependencies and claim status

- **Accepted inputs:** M50's root-composition law, canonical basins,
  capacities, and binomial root-degree law; M56/M65/M69's contextual mean
  and attachment formulas; M76/M79's reset geometry and reachability; M82/M87's
  split bound `q<=2/3` on active targets and weighted normalization;
  M90/M96's all-`j` transformed recurrence; M98/M99 and M103/M106's exact
  local-route refutations.
- **Proved here:** strict `L` descent; fresh uniform attachment; the exact
  Schur recurrences; basin estimate (4.1); universal unweighted and weighted
  full-excursion contraction for `L=0,1,2`.
- **Exact finite only:** four predecessor calibrations and the displayed
  diagnostic rows. They are not used to extrapolate beyond their role in the
  explicit finite `s=3,...,9` algebraic certificate.
- **Refuted accepted context:** universal one-step/nonfresh defect positivity
  and universal two-layer defect positivity. This report does not retry them.
- **Unresolved:** the selected contraction for arbitrary `L`, beginning at
  `L=3`; any full reset-excursion counterexample; auxiliary `Pbar` gap;
  ROOT-MEAN LIFT; and all original-chain gap/mixing conclusions.

The finite `s=3,...,9` certificate is a complete exact check of seven fixed
polynomials, joined to the analytic `s>=10` proof; it is not a bounded scan
offered as asymptotic evidence.

## 7. First unproved step and strongest self-attack

The exact all-depth expansion is

```text
H(x)=sum_(d=0)^L sum_(x=x_0->...->x_d)
 [product_(i<d)Q(x_i,x_(i+1))]A_0(x_d).             (7.1)
```

The first unproved case is `L=3`. A proof must bound the aggregate marked
reset-leaf measure in (7.1) by the initial `q_x(1-q_x)` budget. The `L=2`
argument works because contextual support has four compositions and every
descendant lies in an already settled boundary sector. At `L=3`, more
exceptional basins and non-right-heavy descendants appear; no uniform
filtration or induction inequality controlling their cross-terms was proved.

The strongest self-attack is therefore structural:

- the basin bound `rho(B_e)/rho(e)<=degree(e)` can be loose;
- the `L=2` envelope approaches the target more closely than the actual
  resolvent in the audit, leaving limited slack for a naive induction;
- M98/M99 prove that nonfresh local defects can be negative infinitely often;
- M103/M106 give the exact fresh witness `(30,1,0,10)` where even the global
  two-layer defect block is negative, although both full resolvents survive;
- fresh full-resolvent discovery ratios increase over the tested ranks.

Accordingly, the boundary theorem supplies no legitimate inference for
arbitrary `L`. A future proof needs a new complete-history measure inequality;
a future refutation needs one exact full-resolvent witness.

## 8. Reproduction, probability, and boundary cases

The retained exact command is

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-22/\
mission-M109-full-reset-excursion/boundary_exact.py \
  --s-max 16 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-22/\
mission-M109-full-reset-excursion/boundary_exact.json
```

The final run used Python `3.12.3`, standard-library exact rational
arithmetic, seed `null`, and took `1.49` seconds. `s=2` is handled explicitly
in the `L=1` proof; `s=3` is the first `L=2` case. The auxiliary state has
`s>=2`; original-chain cases `m` odd, `m=0`, `m=2`, and `N=2` do not enter
this separated lemma and receive no new conclusion here.

## 9. Artifacts, freeze, hashes, and hygiene

Owned artifacts are

```text
plan.md                    objective and failure modes
checkpoint.md              durable halfway and final checkpoint
excursion_reduction.md     complete formulas and analytic proofs
boundary_exact.py          standalone all-j exact checker
boundary_exact.json        exact raw output and Bernstein certificates
targeted_discovery.json    two interrupted binary64 discovery rows
report.md                  this nine-field final report
SHA256SUMS                 frozen manifest
```

The M106 frozen report and manifest remained unchanged at startup and freeze:

```text
66deb693559cc2da5b4d5d67113a56776c5204bcdbd2e7cb0777e6f2c09bf129  report.md
57afd0e41cef8c128489f9d12ce35336a076f40f9023839457f91af7a93d5f16  SHA256SUMS
```

JSON parsing, source compilation without bytecode writes, exact rerun,
manifest verification, and cache hygiene are checked at freeze. No
predecessor, coordinator note, manuscript, project skill, or shared source
was edited. Repository status shows the shared experiment tree and `notes/`
as untracked at the base commit; M109's owned directory contains only the
files listed above.
