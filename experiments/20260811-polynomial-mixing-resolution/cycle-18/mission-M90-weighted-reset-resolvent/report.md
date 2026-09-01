# M90 final report: weighted reset resolvent and excursion defect

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, exact scope, and conventions

**VERDICT: UNRESOLVED. NO RIGHT-HEAVY COUNTEREXAMPLE FOUND; RAW VARIANCE
AND SIMPLE COMPENSATOR ROUTES REFUTED; PROMOTE THE EXACT EXCURSION-DEFECT
REDUCTION, NOT THE INEQUALITY.**

This mission concerns only the full **nonlazy stationary-flow
parking-degree projection** `Pbar_r` in the minimal long-cycle
factorization sector. It does not prove a gap, ROOT-MEAN LIFT, or any result
for the original lazy `{3,4,5}` same-product heat-bath chain `K` on
identity words.

Permutations compose as `(pq)(x)=p(q(x))`, and factors are displayed
left-to-right. For every active reachable right-heavy seed
`x=(s,K,K-1,B)`, the assigned statement is

```text
K_reset W(x)<=W(x),
K_reset=(I-D)^(-1)J_can,
W(x)=(1-q_x)K/(R+1).                               (1.1)
```

M82's normalization is preserved exactly:

```text
w_a=a^(a-1)/a!,
rho_s(C)=product_i w_(c_i)/[k!w_(s+1)],
q_x=w_(s+1-B)w_B/w_(s+1),
J_can(x,y_e)=theta_e^2/[Q_G(e)q_x],
D(x,y)=rho_s(k,t)q_y nu_(K,R,k)(j)/q_x.            (1.2)
```

Every retained deep rank `j=1,...,k` is included. Every deep and reset
child strictly lowers `P=s+K-R`, so every resolvent below is a finite DAG
sum, not an analytic convergence assertion.

## 2. Exact grouped recurrence and asymptotic diagnostics

Put

```text
F(x)=[(I-D)^(-1)J_can W](x),
g(x)=q_xF(x),
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),
U(x)=q_x(1-q_x)K/(R+1).
```

Every reset target is right-heavy, hence `W(y_e)=1-q_(y_e)`. Multiplying
`F=J_can W+DF` by the parent `q_x` cancels both split-mass divisors and
proves the exact grouped recurrence

```text
g(x)=A(x)+sum_(k,t>B,j>=1) Q(x,y)g(y),              (2.1)
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)),
y=(t-1,K+k,R+j,B).
```

For a refined endpoint `e=(A,b,c_3,...,c_(ell+1))`, with
`v_e=product_(i>=2)w_(c_i)` and last part `t`, M82's Cayley grouping gives

```text
C(A,p)=p A^(A-p-1)/(A-p)!,
S_e=sum_(p=1)^A C(A,p)[H_x(p+ell,t)-q_x]/(p+ell)!,
theta_e^2/Q_G(e)=v_e ell! S_e^2/[w_Aw_(s+1)].      (2.2)
```

The deep group mass is

```text
rho_s(k,t)=w_t C(s-t,k-1)/[k!w_(s+1)].             (2.3)
```

Equations (2.1)--(2.3), implemented independently with exact rational
arithmetic, reproduce M82's frozen rank-eight and rank-eleven values.

Two elementary asymptotic checks explain the sensitive regimes but do not
settle (1.1). Write `n=s+1`. Stirling's formula gives

```text
q_s(b) -> e^(-b)w_b                         (fixed b),
q_s(B) ~1/[sqrt(2pi){beta(1-beta)n}^(3/2)]  (B/n->beta in (0,1)).
```

On a right-heavy context,

```text
nu_j=binom(K-1+j,j)/binom(K+k,k).                    (2.4)
```

For a fresh seed `K=1`, every `j=0,...,k` has mass `1/(k+1)`. For fixed
`k` and `K->infinity`, `nu_k=K/(K+k)`,
`nu_(k-1)=kK/[(K+k)(K+k-1)]`, and lower ranks are successively smaller.
Thus the `j=k` branch is asymptotically dominant only in a large-`K`
regime; deleting `j<k` is never an exact recurrence and is maximally wrong
at the fresh seeds that dominate the scans.

## 3. Exact countersearch beyond the predecessor ranks

`exact_weighted_resolvent.py` is a standard-library `Fraction`
implementation independent of predecessor code. It reproduces

```text
(8,1,0,4):  g/U=.43715035400213015...,
(11,1,0,5): g/U=.5391499615007582...,
```

including the exact frozen M82 numerator and denominator at rank eleven.
It then finds zero failures over

```text
s in {12,14,16,18,20},
K in {1,2,4,8,16,32}, R=K-1, every B.
```

The largest ratio in that scan is at `(20,1,0,7)`:

```text
g/U=.6781776227304538...,
U-g=.012069769767893484...>0                       (exact sign).
```

A separate exact fresh-seed scan at `s=22,24` also has zero failures. Its
largest row is `(24,1,0,9)`:

```text
g/U=.7076960352612462...,
U-g=.008104059498624878...>0                       (exact sign).
```

A corrected binary64 discovery scan, used only to select possible
counterexamples, reaches `s=30` for `K in {1,2,4,16}`. Its largest ratio is
`.7372496452184516...` at `(30,1,0,10)`. This trend, the apparent maximizing
scale `B` near `s/3`, and every other bounded survival value are finite
diagnostics only.

An early discovery version mistakenly kept only `j=k` on right-heavy deep
steps and produced `.4725...` rather than M82's rank-eleven `.539149...`.
That recurrence is invalid because every `j<k` child is non-right-heavy and
may later reset. The bug was caught before retained results, the executable
and all discovery JSON now state and use every `j>=1`, and the stale warning
is preserved in `checkpoint.md`.

## 4. Whole-excursion slack and a boundary-layer reduction

Define the exact local defect

```text
r_U(x)=U(x)-A(x)-sum_y Q(x,y)U(y).                  (4.1)
```

Since `Q` is nilpotent under strict `P` descent, (2.1) gives the exact
entire-excursion identity

```text
U(x)-g(x)=[(I-Q)^(-1)r_U](x)
          =sum_(d>=0)[Q^d r_U](x).                 (4.2)
```

This is not the refuted raw Bellman inequality: `r_U` can be negative. For
example, at `(12,1,0,4)`,

```text
r_U=-.002546678913981043...,
Qr_U=.016015335272696666...,
Q^2r_U=.010074279760915785...,
U-g=.034039264472470600... .
```

Every later depth contribution in this exact profile is positive.

The accepted reachable mark closure is

```text
{(K,R)=(1,0)} union {K>R>=1}.                      (4.3)
```

Call `(1,0)` fresh and the second class nonfresh. Every deep child of a
fresh context is nonfresh, and deep steps preserve nonfreshness. Therefore
the following two statements are a proved sufficient reduction for (1.1):

```text
r_U(z)>=0                  for every reachable nonfresh z,       (4.4)
r_U(x)+(Qr_U)(x)>=0        for every fresh x.                    (4.5)
```

Indeed a right-heavy nonfresh seed is handled by (4.4), while for a fresh
seed the first two terms in (4.2) are nonnegative by (4.5) and every term
of depth at least two is a nonnegative average of nonfresh defects by
(4.4).

The signs in (4.4)--(4.5) remain unproved universally, but two independent
exact audits make this a concrete next target:

- Among all 38,269 reachable contexts with `2<=s<=12` and `K<=32`, exactly
  seven have `r_U<0`; all seven are fresh: `(11,1,0,B)` for `B=3,4,5` and
  `(12,1,0,B)` for `B=3,4,5,6`. There is no nonfresh failure.
- On the complete pure-deep closures of all 209 fresh contexts with
  `2<=s<=20`, comprising 7,334 distinct contexts, there is no nonfresh
  defect failure and no fresh two-level failure. The smallest normalized
  nonfresh defect is `.0379056303649582...` at `(19,2,1,6)`; the smallest
  normalized fresh two-level block is `.0525169898121164...` at
  `(20,1,0,6)`. All signs are exact.

These finite passes do not prove (4.4) or (4.5). They show exactly where a
telescoping proof would have to act: the negative boundary defect occurs at
fresh seeds and is paid by the first nonfresh layer, rather than by a raw
current-state potential.

## 5. Contextual variance identity and exact obstructions

Let `Phi_(K,R;B)` be M56/M65's contextual split **rate divided by
`alpha_r`**, and let `V(x)=Var_(pi_s)(Phi_x)`. It is not a literal
`{0,1}` event indicator. It is already an average over hidden factor words,
the scan site, and the favourable heat-bath outcome. On right-heavy
contexts the closed root-composition mean `H_x(C)` is in `[0,1]` by the
displayed binomial formulas; pointwise `Phi_x in [0,1]` passed the exact
macro audit through ambient rank seven. No new universal pointwise or
Bernoulli-event representation is claimed here.

M65's pointwise inheritance proves a useful exact mixed-second-moment
recurrence. For two contexts `a,b` with the same `(s,B)`, condition on a
root composition with part count `k` and last part `t`:

```text
M_s(a,b)=E[Phi_a Phi_b],
t<B:  contribution 0,
t=B:  contribution H_a(k,B)H_b(k,B),
t>B:  contribution sum_(j,l>=1)nu_a(j)nu_b(l)
                     M_(t-1)(a_j,b_l).             (5.1)
```

The base `s=B=1` is the singleton statistic one. This follows by multiplying
the two pointwise inheritance identities on the same last-branch macro and
then using the accepted product restriction. It exactly matches two direct
macro variances:

```text
V(5,2,1,2)=10981/131220,
V(6,1,0,3)=24731355/282475249.
```

Write the deep conditional statistic as the correlated mixture
`sum_j nu_j Phi_(y_j)`. The law of total variance and convexity give the
proved defect identity

```text
r_V:=V-A-QV
   =Var(H_x(C))-A-L_attach,                         (5.2)
L_attach=sum_(deep C)rho(C)
 [sum_j nu_j V(y_j)-Var(sum_j nu_j Phi_(y_j))]>=0.
```

Thus root-mean variance must pay both canonical reset energy and the Jensen
loss caused by charging the attachment ranks separately. It need not do so:

```text
x=(6,2,1,2),
r_V=-21394206021215/36917038301316768<0.            (5.3)
```

This is a right-heavy exact counterexample to the raw variance
supersolution. The full-excursion proposal `g<=V` also fails on reachable
non-right-heavy contexts, first in the stored scan at `(11,6,1,4)` and with
largest tested ratio

```text
x=(12,32,5,4),       g/V=1.0802089991127168... .    (5.4)
```

The same exact scan finds no violation of `V<=U` through `s=12,K<=32`, but
that is finite evidence only. At the witness (5.4), `U` is much larger than
both `V` and `g`, so (5.4) does not refute (1.1).

Finally, all eight tested scalar interpolants

```text
M=V+a(U-V),
a in {s/(s+c),P/(P+c):c=1,2,4}
     union {1-1/s^2,1-1/P^2}
```

fail the raw supersolution `M>=A+QM` exactly by rank twelve, with fresh
failures at `(12,1,0,4)`. This rejects these named current-state
compensators, not every possible compensation.

## 6. Stronger unweighted frontier and why it is only Bernoulli-shaped

There is a simpler sufficient inequality. Define

```text
h(x)=q_x[(I-D)^(-1)J_can 1](x),
A_0(x)=sum_e theta_e^2/Q_G(e).
```

The same exact cancellation gives

```text
h=A_0+Qh.                                           (6.1)
```

On a right-heavy seed, the stronger frontier is exactly

```text
q_x K_reset 1(x)<=q_x(1-q_x),                      (6.2)
```

or `K_reset1<=1-q_x`. Because every reset target is right-heavy and
`W(y)=1-q_y<=1`, (6.2) implies

```text
K_reset W(x)<=K_reset1(x)<=1-q_x=W(x).
```

An independent exact all-`j` scan over

```text
s in {8,11,12,14,16,18,20},
K in {1,2,4,8,16,32}, R=K-1, every B
```

finds no (6.2) failure. It reproduces M82's ratios `.621004266940768...`
at `(8,1,0,3)` and `.694743790562165...` at `(11,1,0,4)`. Its largest
ratio is

```text
.7893855076290114... at (20,1,0,6),
q(1-q)-h=.008912118034790353...>0                  (exact sign).
```

The scalar right side of (6.2) has the form of a Bernoulli variance, but
this report does **not** identify a Bernoulli random variable whose Doob
increments have energy `h`. Such a representation is the missing theorem,
not an interpretation that may be assumed. Two exact witnesses rule out the
most direct Bessel arguments:

```text
(8,1,0,3):  h/Var(Phi)=1.0201181953869307...>1,
(11,1,0,4): A_0/Var(H(C))=1.0776222300606009...>1. (6.3)
```

Canonical basin indicators are nested rather than orthogonal, so their
positive cross terms matter. Moreover the deep excursion leaves the
right-heavy class: at the reachable non-right-heavy context `(12,32,5,4)`,
the closed contextual value is `16182/6919>1` on the root group `(k,t)=(6,4)`.
There is therefore no literal global Bernoulli event furnished by the
existing contextual statistic.

## 7. Dependencies, probability, runtime, and claim status

- **Frozen accepted inputs:** M50's root-composition law, canonical basins,
  and capacities; M56/M65/M69's contextual locality, closed mean, pointwise
  negative-hypergeometric inheritance, and product restriction; M71's
  pure-deep base bound and one-shot label accounting; M76/M79's reachable
  closure, reset geometry, exact resolvent, and strict `P` descent;
  M82/M87's weighted target, split-mass bound, and normalization.
- **Proved here:** transformed recurrences (2.1) and (6.1); mixed-moment
  recurrence (5.1); variance-defect identity (5.2); entire-excursion
  telescoping identity (4.2); and the logical sufficient reduction
  (4.4)--(4.5).
- **Refuted here:** the raw variance supersolution; full-context `g<=V`;
  direct `h<=V`; direct `A_0<=Var(H)`; and the eight named scalar
  compensators.
- **Exact finite only:** survival of (1.1), (4.4)--(4.5), (6.2), and
  `V<=U` in their explicitly stated ranges.
- **Unresolved:** (1.1), (4.4), (4.5), (6.2), a global excursion
  martingale/Doob representation, marked occupation, actual unmarked
  ROOT-MEAN LIFT, an auxiliary `Pbar` gap, and every result for `K`.

All retained computations are deterministic with seed `null`, Python
`3.12.3`, and standard-library exact rational arithmetic. Representative
exact runtimes were 170.69 seconds for the weighted rank-20 slice, 160.39
seconds for fresh ranks 22/24, 161.98 seconds for mixed moments through
`s=12,K=32`, 262.46 seconds for the compensator scan, 171.26 seconds for
the unweighted rank-20 slice, 43.55 seconds for the full fresh-closure
boundary audit, and 115.70 seconds for the 38,269-context defect scan.
The binary64 rank-30 discovery pass took 345.38 seconds and supports no
promoted sign.

## 8. First unproved steps, strongest self-attack, and conditional implication

The assigned standalone lemma remains exactly:

> **DEEP-ELIMINATED BETA-BINOMIAL RESET SUPERSOLUTION.** For every active
> reachable right-heavy seed `x=(s,K,K-1,B)`, with (1.2),
> ```text
> sum_y[(I-D)^(-1)J_can](x,y)W(y)<=W(x).            (8.1)
> ```

The recommended scalar proof target is now the pair of explicit grouped
inequalities (4.4)--(4.5). They use the complete pure-deep excursion and
would prove (8.1) algebraically. The alternative stronger target is (6.2),
preferably through a genuinely constructed augmented-event filtration.
Neither target is claimed.

The strongest self-attack is cumulative:

- raw constant and `P^dW`, `d=0,1,2`, were already refuted by M82/M87;
- raw `U` itself fails at fresh rank eleven;
- raw contextual variance fails at right-heavy rank six;
- full-context variance domination and every tested scalar interpolation
  fail;
- the stronger unweighted energy exceeds both natural local variance
  budgets in (6.3);
- exact margins shrink with rank, and no asymptotic limit of either
  resolvent ratio has been proved.

If, and only if, (8.1) is later proved, M82's accepted argument gives for
right-heavy reset epochs `mu_n=delta_x K_reset^n`

```text
mu_n1<=3,
sum_(n<P)mu_n b<=3eP^3(1+log P).                   (8.2)
```

This is only a separated marked-occupation bound for auxiliary `Pbar`.
If the stronger (6.2) were proved, the factor `3` in (8.2) could be replaced
by `1`. Neither implication is a `Pbar` gap, an unmarked lift, or an
original-`K` statement.

## 9. Artifacts, reproduction, hashes, and hygiene

Primary proof artifacts are `plan.md`, `checkpoint.md`, this report, and:

```text
exact_weighted_resolvent.py       exact weighted recurrence and scans
boundary_layer_scan.py            full fresh-closure two-level audit
reachable_defect_scan.py          broad reachable-context defect audit
exact_unweighted_resolvent.py     stronger unweighted recurrence
contextual_second_moment.py       exact mixed moments and variance attacks
defect_filtration_scan.py         law-of-total-variance/tail audit
resolvent_slack_profile.py        exact depth and reset-rank profiles
compensator_probe.py              eight scalar compensator falsifiers
structural_witnesses.py           compact Bessel/Bernoulli obstructions
discovery_scan.py                 corrected all-j binary64 discovery only
```

Representative commands are:

```text
python3 -B exact_weighted_resolvent.py \
  --s-values 12 14 16 18 20 --K-values 1 2 4 8 16 32 \
  --output exact_s20_k32.json

python3 -B boundary_layer_scan.py \
  --s-values 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 \
  --output boundary_layer_s20.json

python3 -B reachable_defect_scan.py \
  --s-max 12 --k-max 32 --output reachable_defect_s12_k32.json

python3 -B exact_unweighted_resolvent.py \
  --s-values 14 16 18 20 --K-values 1 2 4 8 16 32 \
  --output exact_unweighted_s20.json

python3 -B contextual_second_moment.py \
  --s-max 12 --k-max 32 --output contextual_second_moment_s12_k32.json

python3 -B compensator_probe.py \
  --s-max 12 --k-max 32 --output compensator_s12_k32.json
```

All exact JSON stores exact numerators and denominators; decimals are
presentation only. `SHA256SUMS` contains every owned artifact digest. JSON parsing,
source compilation without bytecode writes, the manifest, and cache hygiene
were checked before freeze. No predecessor, coordinator note, manuscript,
project skill, or shared source was edited.
