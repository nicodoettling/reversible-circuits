# M106 fresh referee report on frozen M103

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, accepted claim, convention, and exact scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

The accepted claim is narrow and negative. For the full **nonlazy
stationary-flow parking-degree projection** in the minimal long-cycle
factorization sector, the universal pointwise certificate

```text
(I+Q)r_U(x)>=0
```

is **refuted** at the reachable fresh context

```text
x=(s,K,R,B)=(30,1,0,10).
```

The complete weighted and stronger unweighted reset resolvents are both
strictly below their budgets at this witness. Thus M103 correctly does
**not** refute either universal full-resolvent inequality. It proves no slow
mode, conductance bound, spectral-gap upper bound, auxiliary `Pbar` gap,
ROOT-MEAN LIFT, result for the original lazy exact same-product `{3,4,5}`
heat-bath chain, Terminal A, or Terminal B.

The global target remains the uniform fixed-length law on
`Omega(N,m)`. Permutations compose as `(pq)(x)=p(q(x))`; displayed factors
multiply left-to-right.

## 2. Frozen provenance and package integrity

The required M103 hashes independently match:

| frozen artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `354c854abccedb0160a3d452a361dd6a453daad82723101b9d913e29513076d1` | match |
| `SHA256SUMS` | `01281ce9a5d70eb3a013c4304859428f373e65ae049eff957484b06eab6ab4d1` | match |

Running `sha256sum -c SHA256SUMS` inside the frozen M103 directory returned
`OK` for all eight entries. M90, M96, M98, M99, and M103 were read as frozen
predecessors. The fresh implementation imports no predecessor module and did
not read M103 output until after its own exact run had completed.

The fresh principal artifact hashes before final report freeze are:

```text
522ff3e01c66265dec5c9213a32aab80adc281241b704b8b473b6fbc2bcc66e3  independent_exact_audit.py
a011e9be0c6820f9b7d567bd8c01cce21b69c9369e3a0884658ca1289444fd47  independent_exact_audit.json
```

## 3. Independent all-rank recurrence and two-layer identity

For an active context `x=(s,K,R,B)`, the audit independently reconstructs

```text
q_x = w_(s+1-B)w_B/w_(s+1),
U(x)=q_x(1-q_x)K/(R+1),
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)),
r_U=U-A-QU.
```

The full attachment law is

```text
nu(j)=binom(R+j,j)
      binom(K-R-1+k-j,k-j)/binom(K+k,k),   0<=j<=k.
```

Its total is one. `j=0` is the killed branch; **every** live rank
`j=1,...,k` is retained. At the witness there are 191 deep-eligible root
groups and 1,521 live `(k,t,j)` edges. Every expected live `j` is present in
each group; the observed live ranks are `1,...,20`. The exact live row mass
is

```text
6973912757528008932573989084161387090439400
------------------------------------------------
17761887753093897979823770061456102763834271.
```

No stochasticity claim requires that this substochastic live mass equal one.
The missing mass comprises killed and terminal branches.

Direct linearity gives, without any sign assumption,

```text
(I+Q)r_U
 = U-A-QU + QU-QA-Q^2U
 = U-A-QA-Q^2U.                                  (3.1)
```

The program evaluates both sides of (3.1) separately and requires exact
`Fraction` equality. The check passes.

## 4. Reachability, activity, and finite descent

The witness is active because `s=30>=2` and `1<=B=10<=s`. It is reachable
at depth zero: `(K,R)=(1,0)` is precisely a fresh seed in the accepted
reachable closure

```text
{(1,0)} union {K>R>=1}.
```

For a live child

```text
y=(t-1,K+k,R+j,B),
P(x)=s+K-R,
```

and positivity of the root group means that the `k-1` parts preceding `t`
sum to at least `k-1`. Therefore

```text
P(x)-P(y)=s-t-k+j+1>=j>=1.                       (4.1)
```

The minimum observed first-layer drop is one. Equation (4.1) proves strict
descent for every live edge, so all local expressions and both complete
resolvents are finite DAG sums; no analytic convergence assumption is used.

## 5. Exact rational countercertificate

Independent exact arithmetic gives

```text
r_U(x)       = -0.003687096818561213...,
(Qr_U)(x)    =  0.003535610344928366...,
(I+Q)r_U(x) = -0.00015148647363284748... .       (5.1)
```

The last quantity in (5.1) is exactly `n/d`, where

```text
n = -18352263982326106830589550281101477193130227917057131016459597314934705386984965970310345077527236691379433999653803737538576355105542511063202998224136419162340209867319700105707335828265917920775435513871091034338447833540406902941644889245715528957755207307267520522637521016938528636523322673200578811646654846284057509787092225718714994180390881815125800234778265110087053668447131837758392966255055394801794851625164015696739313835574382357275317418303147977263836446773985499067916634583206196842721911944566578339743712720348480302337193688128651658576803693198792193557840403796327795211186332890546884705014062429289268701043284827405192616421691963349551760810678343597065658537

d = 121147872428569776664438450031164669948189107230846336111969296145099826108566356485453086725286073894909004772486222236977588817981891892151833609456261714224168106571974995669210545695938578572101181466252133187454986158435380666166125584991971874397435394657775695487378525469907578046253849401207766164545700279881988008585167928228127247820386178813706504374261912419694627236287868799228802701318757740974415452620678355045025010822910964158608147019445840516464174932156403354596082063769256395301865506681992834059531683644224678507457736997629386919374747194393807243028584411612450838563789809346569725343392260843110400000000000000000000000000000000000000000000000000000000000000000.
```

Thus `n<0<d` is a complete exact sign certificate. Normalizing by the
positive budget gives

```text
(I+Q)r_U/U=-0.006914605163495121... .             (5.2)
```

The independent numerator and denominator of `U`, `r_U`, `Qr_U`, (5.1), and
(5.2) all agree bit-for-bit with the corresponding frozen M103 records.

## 6. Exact full weighted and unweighted resolvent audit

The independent paired recursion visited 1,522 contexts and computed

```text
G=[(I-Q)^(-1)A](x),
H=[(I-Q)^(-1)A_0](x),
A_0=sum_e theta_e^2/Q_G(e).
```

At this fresh witness, `K/(R+1)=1`, so both comparison budgets are
`U=q(1-q)`. Exact results are:

| quantity | exact sign and decimal |
|---|---:|
| `G/U` | `0.7372496452184509... < 1` |
| `U-G` | `0.005756384312696922... > 0` |
| `H/[q(1-q)]` | `0.8267268839096050... < 1` |
| `q(1-q)-H` | `0.003796100097007001... > 0` |

All four values, both ratios, and both margins were produced as reduced
exact numerator/denominator pairs. They are recorded under
`full_resolvents` in `independent_exact_audit.json`; every pair agrees
bit-for-bit with frozen `two_layer_exact.json`. In particular the exact
positive margin numerators are

```text
weighted:
697373712364427030662666484201660860215636058960924697731180525636853965073667902597815789590193951696153746110889938533039045637201572761583662126820932092636506359767226671631927088865450805028541037642178603641146364477262117313553998586914272718041705899518465160939930509913394863637783630969003689250311101816699809055344779239908207903724044562827125122884190708148350436303983041965625784192027254270884622698783568271500635170215919225013544171816476368238260931110402322401492071601451134494096900727263495740920717377934011973462424961640282734895345426815304102169188046356793599702582537887199224115592529593484194218028866406268541106191945711714524111915377972593727298341463

unweighted:
183772008103211005450231312771227070797491395970071479056848869315051294535880673578519279543756772364006266562283134970914004966535812944589090929866845750909767136747673155719608268497646598312589426277877612453718559605292414731912931066062655521527423055360483683238073318017777462918408474906149498739780813964674822873582573180185602643501076186404814677447169181991880554171433874226665261381338913848021909701430617040306022800554665764518397329320188178052115706192829050290943345271105070802620130587289986602041685719727561231775859430915427410049837701508467011063307488925437395607367289865104200541661852477794854252445582226383764801656258189409861397861126097210167250697.
```

Their positive denominators are stored completely in the raw JSON. These
are exact finite survival diagnostics, not universal sign proofs.

## 7. Direct grouped checks and predecessor calibration

The independent implementation also performs checks that do not use M103
logic or output:

- literal ordered compositions agree with the grouped Cayley root law in all
  63 nonzero `(s,k,t)` cells through `s=7`;
- 70 attachment laws over `1<=K<=4`, `0<=R<K`, `1<=k<=7` sum exactly to one
  and have every `j=0,...,k` positive;
- the contextual root mean equals `q_(s,B)` exactly at
  `(6,1,0,3)`, `(8,2,1,3)`, and `(11,1,0,4)`;
- literal endpoint-composition sums agree exactly with independently grouped
  weighted and unweighted canonical energies at `(6,1,0,3)` and
  `(8,1,0,4)`; and
- the predecessor boundary calibration `(11,1,0,4)` is reproduced exactly:

```text
r_U       = -0.000962793358473315...,
Qr_U      =  0.017385168676277662...,
r_U+Qr_U  =  0.016422375317804348... > 0.
```

The last three reduced fractions match M96's independently frozen records.
These checks directly attack missing factorials, grouping multiplicities,
split-mass factors, omitted attachment ranks, and stale `j=k`-only logic.

## 8. Strongest self-attack, boundaries, artifacts, and hygiene

The strongest self-attack is decisive for interpretation: the local negative
pair is more than compensated later in both complete excursions. Hence the
counterexample kills only one sufficient pointwise proof template. It is not
a slow eigenfunction, bottleneck, stationary-mass cut, conductance estimate,
comparison-congestion lower bound, or spectral-gap upper bound.

The result lives at auxiliary rank `s=30`. It does not address the original
chain's exceptional cases `m` odd, `m=0`, `m=2`, or `N=2`. No new literature
theorem is invoked. M103's secondary binary64 right-heavy scan was not rerun;
it was explicitly empirical and is unnecessary for the exact accepted claim.

Owned artifacts are `plan.md`, `checkpoint.md`,
`independent_exact_audit.py`, `independent_exact_audit.json`, this report,
and `SHA256SUMS`. The principal command was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M106-m103-fresh-referee/independent_exact_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-22/mission-M106-m103-fresh-referee/independent_exact_audit.json
```

It completed in `60.16` seconds under Python `3.12.3`, deterministically
with `seed=null`, using only the standard library. Before freeze, JSON
parsing, source execution, manifest verification, whitespace checks, cache
hygiene, and owned-directory status are checked. No predecessor, coordinator
note, manuscript, project skill, or shared source is edited.

## 9. Final verdict, numbered objections, and next obligation

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M103 correctly refutes the universal global two-layer condition by an exact,
active, reachable, all-`j` rational witness. It also correctly limits the
scope because both complete resolvents survive exactly at that witness.

The first surviving standalone obligation remains:

> **FULL RESET EXCURSION.** Prove
> ```text
> [(I-Q)^(-1)A](x)<=U(x)
> ```
> for every reachable active context, or prove the stronger universal
> unweighted resolvent bound.

Until then, the full reset frontiers, marked occupation, the auxiliary
`Pbar` gap, ROOT-MEAN LIFT, the original heat-bath gap, and both terminals
remain **unresolved**.
