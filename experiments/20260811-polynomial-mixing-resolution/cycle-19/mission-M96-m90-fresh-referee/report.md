# M96 fresh referee report on frozen M90

Date: 2026-08-12. Audited repository commit recorded by M90:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, exact accepted claim, and scope

```text
ACCEPT M90's exact recurrence, excursion-defect reduction, and refutations.
Material numbered objections: none.
```

The accepted positive result is a **reduction only** for the full nonlazy
stationary-flow parking-degree projection `Pbar_r` in the minimal long-cycle
factorization sector. For every active reachable right-heavy context
`x=(s,K,K-1,B)`, M90 correctly reduces

```text
K_reset W(x)<=W(x),
K_reset=(I-D)^(-1)J_can,
W(x)=(1-q_x)K/(R+1),
```

to two explicit defect inequalities, or alternatively to a stronger
unweighted inequality. Neither inequality is proved. The accepted negative
results refute several raw variance, Bessel, and scalar-compensator proof
routes.

This audit accepts no auxiliary `Pbar` gap, ROOT-MEAN LIFT, result for the
original lazy exact same-product `{3,4,5}` heat-bath kernel, Terminal A, or
Terminal B. Those conclusions remain unresolved.

## 2. Frozen provenance and package integrity

The assigned source digests independently match:

| frozen M90 artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `36230c7e509eff638eb5888b2e61703957dcc32f2f06fae582739d7f1414d458` | match |
| `SHA256SUMS` | `3d63f177659abae99b6c3a4247aee67b6dfc087cd1270df40e806f5a9f99b5b8` | match |

Running `sha256sum -c SHA256SUMS` inside M90's directory returned `OK` for
all 37 entries. The report's bounded-range counts and extrema agree with the
corresponding frozen JSON. No M90, predecessor, coordinator, manuscript,
skill, or shared project file was edited.

Permutations compose as `(pq)(x)=p(q(x))`, and displayed factors multiply
left-to-right. M90 invokes no new external literature result.

## 3. All-rank recurrence, normalization, and strict descent audit

Put

```text
q_x=w_(s+1-B)w_B/w_(s+1),
g(x)=q_x[(I-D)^(-1)J_can W](x),
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),
U(x)=q_x(1-q_x)K/(R+1).
```

For a deep child `y=(t-1,K+k,R+j,B)`, M90 retains every
`j=1,...,k`. Direct substitution into

```text
D(x,y)=rho_s(k,t)q_y nu(j)/q_x
```

gives `q_x D(x,y)F(y)=rho_s(k,t)nu(j)g(y)`. For a canonical reset endpoint
`e`, every reset target is right-heavy, so `W(y_e)=1-q_(y_e)` and

```text
q_x J_can(x,y_e)W(y_e)
  =[theta_e^2/Q_G(e)](1-q_(y_e)).
```

Therefore the grouped recurrence is exactly

```text
g=A+Qg,
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)).          (3.1)
```

No split-mass divisor is missing or duplicated. The fresh implementation
checked exactly:

- 204 direct ordered-composition masses against the grouped Cayley formula,
  with `sum_C rho_s(C)=1` through `s=8`;
- 288 complete attachment laws `sum_(j=0)^k nu(j)=1`;
- 378 literal canonical-basin reset rewards against M90's grouped endpoint
  identity; and
- four exact M82 calibration fractions, including weighted ranks eight and
  eleven and unweighted ranks eight and eleven.

For a deep child,

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,
```

because the `k-1` parts preceding `t` sum to at least `k-1`. A reset target
from `e=(A,b,...)` has `P(y_e)=A+b<=s<P(x)`. Hence all resolvents are finite
DAG sums. M90's normalization and nilpotence claims are accepted.

## 4. Excursion identity, reachability, and boundary-layer reduction

Define

```text
r_U=U-A-QU.
```

Since `(I-Q)g=A` and `Q` is nilpotent,

```text
U-g=(I-Q)^(-1)r_U=sum_(d>=0)Q^d r_U.               (4.1)
```

This is an algebraic identity, not a pointwise Bellman inequality. The fresh
exact audit verifies (4.1), including at `(11,1,0,4)`, where

```text
r_U=-.000962793358473315...,
Qr_U=.017385168676277662...,
r_U+Qr_U=.01642237531780435...>0.
```

The reachable contextual closure is exactly

```text
{(K,R)=(1,0)} union {K>R>=1}.                      (4.2)
```

Indeed, deep steps send a fresh context to `R+j>=1`, preserve `K>R` on a
nonfresh context, and reset steps return `(K,R)=(ell,ell-1)`. Conversely,
any desired nonfresh `(s,K,R,B)` is reached from
`(s+K-1,1,0,B)` using the positive composition
`(1^(K-2),s+1)` and attachment rank `j=R`.

Every positive-depth descendant of a fresh context is nonfresh. Therefore
the following pair is genuinely sufficient for `U>=g`:

```text
r_U(z)>=0                         for every reachable nonfresh z,
r_U(x)+(Qr_U)(x)>=0               for every fresh x.              (4.3)
```

For a nonfresh seed, every term in (4.1) is then nonnegative. For a fresh
seed, the first two terms are nonnegative together and every later term is a
positive average of nonfresh defects. The signs in (4.3) remain universal
conjectures. A fresh independent finite closure through all 65 seeds with
`2<=s<=11` visited 725 contexts and found no nonfresh defect or fresh
two-level failure; this is finite falsification only.

## 5. Variance, Bessel, and compensator refutations

M90's mixed-second-moment recurrence is correct. Conditional on a root
composition with `t>B`, each contextual statistic is the deterministic
mixture `sum_(j>=1)nu_j Phi_j` on the same child macro; multiplying two such
mixtures gives the displayed double sum. Including the killed `j=0` branch
as the zero statistic makes variance convexity applicable. Thus

```text
r_V:=V-A-QV
   =Var(E[Phi|C])-A-L_attach,
L_attach>=0,                                           (5.1)
```

is exact.

The independent literal-composition implementation reproduces every
decisive frozen obstruction as the identical rational number:

| rejected route | exact witness | independent sign/value |
|---|---:|---:|
| raw variance supersolution | `(6,2,1,2)` | `r_V=-21394206021215/36917038301316768` |
| full-context `g<=V` | `(11,6,1,4)` | `g-V=.000075015352569408...>0` |
| direct `h<=V` Bessel bound | `(8,1,0,3)` | `h-V=.001444112277648932...>0` |
| direct `A_0<=Var(E[Phi|C])` | `(11,1,0,4)` | excess `.002689971516500665...>0` |
| literal probability interpretation off right-heavy | `(12,32,5,4)` | `H(6,4)=16182/6919>1` |
| raw `U` local supersolution | `(11,1,0,4)` | `r_U<0` as above |

At the single fresh context `(11,1,0,4)`, the fresh audit also reproduces a
strictly negative defect for all eight named interpolants

```text
M=V+a(U-V),
a in {s/(s+c),P/(P+c):c=1,2,4}
     union {1-1/s^2,1-1/P^2}.
```

These exact witnesses reject only the named local proof templates. They do
not refute `U>=g`, the boundary-layer conditions (4.3), or the original
mixing conjecture.

## 6. Stronger unweighted frontier and conditional occupation audit

For

```text
h(x)=q_x[(I-D)^(-1)J_can 1](x),
A_0(x)=sum_e theta_e^2/Q_G(e),
```

the same cancellation gives exactly

```text
h=A_0+Qh.                                           (6.1)
```

On a right-heavy seed, `h<=q_x(1-q_x)` is equivalent to
`K_reset1<=1-q_x`. Since every reset target is right-heavy and
`0<=W(y)=1-q_y<=1`, positivity gives

```text
K_reset W(x)<=K_reset1(x)<=1-q_x=W(x).             (6.2)
```

So the stronger unweighted frontier logically implies the weighted target.
The independent audit reproduces the exact M82 ratios `.6210042669...` at
`(8,1,0,3)` and `.6947437906...` at `(11,1,0,4)`. It also confirms
termwise `K_reset W<=K_reset1` in the tested calibrations.

The right side of (6.2) is only Bernoulli-shaped. The failures in Section 5
show that the existing contextual statistic supplies neither the required
orthogonal increments nor a global probability-valued representation. M90
correctly labels such a representation as missing.

Finally, assume without claiming the weighted inequality on every active
right-heavy seed. Accepted split-mass bounds give `1/3<=W(y)<=1` on every
active reset target. For `mu_n=delta_x K_reset^n`, positivity and iteration
give `mu_n1<=3mu_nW<=3`; strict reset-phase descent gives `mu_n=0` for
`n>=P(x)`. Combining this with the accepted base-excursion bound
`b<=eP^2(1+log P)` yields exactly

```text
sum_(n<P)mu_n b<=3eP^3(1+log P).                  (6.3)
```

If the stronger (6.2) were proved, row substochasticity replaces `3` by
`1`. Equations (6.2)--(6.3) concern separated marked occupation for the
auxiliary `Pbar` route only; they are not an auxiliary gap or an original
chain statement.

## 7. Fresh certificates, stale-output exclusion, and finite ranges

`independent_audit.py` is a standard-library implementation written from
scratch. It imports no M90 or predecessor module. Literal ordered
compositions and canonical basins reproduce these predecessor maxima exactly:

| quantity | context | exact ratio |
|---|---:|---:|
| weighted reset | `(8,1,0,4)` | `.43715035400213015...` |
| weighted reset | `(11,1,0,5)` | `.5391499615007582...` |
| unweighted frontier | `(8,1,0,3)` | `.6210042669407680...` |
| unweighted frontier | `(11,1,0,4)` | `.6947437905621655...` |

At `(11,1,0,5)`, a deliberately reconstructed stale `j=k`-only recurrence
gives `.4725194121119847...`, not `.5391499615007582...`. All nine frozen
M90 source files that perform deep recursion contain the full
`range(1,k+1)` loop and no literal singleton-`k` loop. Each retained discovery
JSON explicitly records “every `j>=1`”; its rank-eleven binary64 value agrees
with the corrected exact recurrence. The stale result is not retained.

The frozen manifest and JSON also support M90's stated finite scopes: 38,269
reachable contexts in the broad `s<=12,K<=32` defect scan, seven negative
defects all fresh, 7,334 contexts in the rank-20 fresh closures, no nonfresh
or fresh-two-level failure there, no weighted failure in the rank-20 or
fresh rank-24 files, and no unweighted failure in the rank-20 file. These
larger-range statements are verified frozen computations, not asymptotic
evidence or universal proofs.

## 8. Strongest self-attack, boundaries, artifacts, and hygiene

The strongest remaining attack is substantive. The local budget itself is
not superharmonic, variance and all tested scalar repairs fail, the stronger
unweighted energy exceeds both natural variance budgets, and the exact
finite margins shrink with rank. No asymptotic sign for the weighted or
unweighted resolvent has been proved. Therefore neither the finite scans nor
the Bernoulli shape should be promoted beyond the reductions stated here.

The audit is confined to active ranks of the auxiliary minimal long-cycle
sector. The original chain's exceptional cases `m` odd, `m=0`, `m=2`, and
`N=2` are outside this lemma and no conclusion about them is inferred.

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_audit.py`,
`independent_audit.json`, this report, and `SHA256SUMS`. The principal command
was

```text
python3 -B independent_audit.py
```

run from this mission directory. It completed in 2.28 seconds under Python
`3.12.3`, deterministically with `seed=null`, using no network or
nonstandard dependency. JSON parsing, source compilation, manifest
verification, and cache hygiene are checked before freeze. The final
manifest freezes every owned artifact other than itself.

## 9. Final verdict, numbered objections, and first unproved obligation

**ACCEPT, with zero material numbered objections.**

M90 correctly promotes the exact transformed recurrences, finite-DAG
excursion identity, fresh/nonfresh sufficient reduction, stronger
unweighted implication, and named exact refutations. It correctly leaves all
surviving inequalities conditional.

The first unproved obligation is still to prove either

```text
r_U>=0 on every reachable nonfresh context,
r_U+Qr_U>=0 on every fresh context,
```

or the stronger `K_reset1<=1-q` on every active reachable right-heavy seed.
Until then, marked occupation, an auxiliary `Pbar` gap, ROOT-MEAN LIFT, the
local heat-bath gap, and both Terminals remain **unresolved**.
