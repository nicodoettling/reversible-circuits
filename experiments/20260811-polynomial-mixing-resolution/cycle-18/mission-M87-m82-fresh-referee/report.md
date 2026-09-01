# M87 fresh referee report on frozen M82

Date: 2026-08-12. Repository commit recorded by the source and independent
audit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, and frozen source audited

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors are displayed
left-to-right. The background target is uniform on

```text
Omega(N,m)={w in T_N^m: eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` block heat-bath kernel.
M82 does **not** analyze that kernel directly. Its exact scope is the full
nonlazy stationary-flow parking-degree projection `Pbar_r` in the minimal
long-cycle factorization sector, and specifically the contextual canonical
reset operator

```text
K_reset=(I-D)^(-1)J_can.
```

The two assigned source digests match exactly:

| frozen artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `0df7639c4460ebb428ab44d8e039dffa48f56fcc7c4706adf716254dc2a1ba53` | match |
| `SHA256SUMS` | `20ed2e03ebf964f78a7e1e13c7c86c48009ff8b44c9836ed05a0c34a6be327cc` | match |

Running `sha256sum -c SHA256SUMS` in M82's directory returned `OK` for all
ten entries. No frozen or shared file was edited.

M82's result is correctly scoped as follows: the universal split-mass bound
and four raw/eliminated counterexamples are proved; several bounded exact
inequalities survive finite falsification; and one deep-eliminated weighted
reset lemma remains unresolved. M82 claims no `Pbar` gap, ROOT-MEAN LIFT,
original heat-bath gap, Terminal A, or Terminal B.

## 2. Full independent proof and computation audit

### 2.1 Operator normalization — accepted

Put

```text
w_a=a^(a-1)/a!,
rho_s(c_1,...,c_k)=product_i w_(c_i)/[k!w_(s+1)],
q_x=w_(s+1-B)w_B/w_(s+1),
x=(s,K,R,B).
```

The independent implementation imports no M82, M79, or predecessor code.
It reconstructs every ordered composition and verifies exactly that
`sum_C rho_s(C)=1`. For M65's displayed contextual observable `H_x(C)`, it
also verifies on every direct operator call that

```text
sum_C rho_s(C)H_x(C)=q_x.                          (2.1)
```

For a composition with `k` parts and last part `t>B`, the reconstructed deep
coefficient is exactly

```text
D(x,y)=rho_s(k,t) q_y nu_(K,R,k)(j)/q_x,
y=(t-1,K+k,R+j,B),

nu_(K,R,k)(j)
 =binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

Here `rho_s(k,t)` is the aggregate of `rho_s(C)` over compositions with the
specified `k,t`. For a canonical endpoint `e`, direct basin-current
enumeration gives

```text
J_can(x,y_e)=theta_e^2/[Q_G(e)q_x],
Q_G(e)=rho_s(e)*degree(e).                          (2.2)
```

Thus both `D` and `J_can` contain the parent `q_x` divisor. The fresh direct
calculation agrees with every corresponding grouped coefficient; no raw,
transformed, or eliminated kernel is interchanged.

### 2.2 Strict phase descent, right-heaviness, and reachability — accepted

For `P=s+K-R`, a deep child satisfies

```text
P(x)-P(y)=s-t-k+j+1.
```

The `k-1` positive parts preceding `t` have total `s-t>=k-1`, so the
difference is at least `j>=1`. A reset child has

```text
y=(A+c_2-1,k-1,k-2,c_2),
P(y)=A+c_2<=s<P(x).
```

Hence `(I-D)^(-1)J_can` is a finite DAG sum. Every reset target has
`K-R=1`.

The stated reachable closure is exact, including the contextual rather than
merely mark-pair quantifier:

```text
{(K,R)=(1,0)} union {K>R>=1}.                      (2.3)
```

Deep steps from this set preserve `K>R` and have new `R>=1`; resets return
to `K-R=1`. Conversely, for any desired `(s,K,R,B)` with `K>R>=1`, start
from the fresh seed

```text
(s+K-1,1,0,B),
```

choose the positive composition `(1^(K-2),s+1)`, whose part count is
`k=K-1`, and choose inherited rank `j=R`. Its positive deep coefficient
lands exactly at `(s,K,R,B)`. The case `(1,0)` is already a fresh seed.
Thus M82's all-context counterexample is genuinely reachable, while its
failure to be right-heavy is also genuine.

### 2.3 Universal split-mass bound — accepted

For `a,b>=1`, `n=a+b`, define

```text
p=binom(n,a)(a/n)^a(b/n)^b.
```

Direct algebra gives

```text
q(a,b)=w_aw_b/w_n=p*n/(ab).                        (2.4)
```

If `a=1`, then `q=(1-1/n)^(n-2)`, which decreases for `n>=3` from
`2/3`; the case `b=1` is symmetric. If `a,b>=2`, the binomial masses
adjacent to the mass `p` have ratios `b/(b+1)` and `a/(a+1)` to `p`.
Their sum with the central mass is at most one, so

```text
p<=[1+b/(b+1)+a/(a+1)]^(-1)<=3/7,
n/(ab)=1/a+1/b<=1.
```

Therefore `q(a,b)<=2/3` whenever `a+b>=3`. The excluded pair `(1,1)` has
`q=1`, but for a reset target its two parts are `A,c_2` and it gives local
rank `A+c_2-1=1`; that target is discarded. The quantifier used in M82 is
therefore exact.

### 2.4 Eliminated-kernel finite claims and counterexample — accepted

The independent full scan covers exactly the same 1,015 reachable contexts
with `2<=s<=8`, `K<=8`, every `B`, and `R=0` only for `(K,R)=(1,0)`.
All exact maxima and failure counts match M82:

| quantity | maximizing context | exact/decimal maximum | failures |
|---|---:|---:|---:|
| `K_reset 1` | `(8,8,1,3)` | `1.2921324746861385...` | `17` |
| right-heavy `K_reset 1` | `(8,1,0,4)` | `.538434439350936...` | `0` |
| `K_reset1/[(K-R)(1-q)]` | `(8,1,0,3)` | `.621004266940768...` | `0` |
| `(K_reset W)/W` | `(8,1,0,4)` | `.437150354002130...` | `0` |

The lexicographically first unweighted eliminated failure in that scan is
exactly

```text
x=(6,8,1,2),
K_reset 1
 =1205648301042298686456011/
  1135274399078805562500000
 >1.                                             (2.5)
```

Here `K-R=7`, so (2.5) refutes the all-reachable-context unweighted row
bound but not the right-heavy statement. Every output of `K_reset` is
right-heavy, so a non-right-heavy context can occur only within the deep
excursion already absorbed into the resolvent.

A separate independent scan of the 65 fresh seeds through `s=11` gives
the same exact maxima as M82: unweighted `.632621701887196...` at
`(11,1,0,4)`, weighted ratio `.539149961500758...` at `(11,1,0,5)`, and
multitype ratio `.694743790562165...` at `(11,1,0,4)`. All of these are
finite falsification data only.

### 2.5 Raw Bellman refutations and downward floors — accepted

The independent audit reproduces all four certificates.

1. At the reachable right-heavy context `(3,13,12,2)`,
   ```text
   D1=13/14,
   J_can1=953/12544,
   (D+J_can)1=12601/12544>1.
   ```
2. For `U_0=W` at `(11,1,0,4)`, the exact raw ratio is
   `1.011824758998902...>1`.
3. For `U_1=PW` at `(44,1,0,30)`, the exact raw ratio is
   `1.001733271840305...>1`.
4. For `U_2=P^2W` at `(120,1,0,102)`, the independent enumeration gives
   exactly
   ```text
   deep terms:       1,123
   reset terms:      8,214,806
   deep floor:       9035810685106442828848365141114545
   reset floor:      5572770673503574703458209485091641
   scale:            10^30
   total lower bound:14608.581358610018...
   parent:           14550.287347995294...
   lower-parent:     58.29401061472363...>0.
   ```

Every deep summand is a product of nonnegative masses, conditional
probabilities, and `U_2`; every reset summand contains a squared current and
is also nonnegative. Consequently

```text
floor(10^30 term)/10^30 <= term
```

for each summand, and the displayed summed floor is a rigorous rational lower
bound. The full numerator of the exact positive lower-minus-parent value in
`independent_audit.json` matches M82's certificate. This refutes exponents
`0,1,2`, not all fixed exponents, and it does not refute the eliminated
weighted inequality.

### 2.6 Grouped Cayley identity — accepted

Lagrange inversion gives the product-weight sum over positive `p`-part
compositions of `A`:

```text
C(A,p)=[z^A]T(z)^p=p A^(A-p-1)/(A-p)!.
```

For an endpoint `e=(A,b,c_3,...,c_(l+1))`, let

```text
v_e=product_(i=2)^(l+1)w_(c_i),
S_e=sum_(p=1)^A C(A,p)[H_x(p+l,c_(l+1))-q_x]/(p+l)!.
```

Directly summing the basin gives

```text
theta_e=v_eS_e/w_(s+1),
Q_G(e)=w_Av_e/[l!w_(s+1)],
theta_e^2/Q_G(e)=v_el!S_e^2/[w_Aw_(s+1)].          (2.6)
```

Division by `q_x` then gives the reset coefficient. Grouping the tail by its
last part uses the same Cayley coefficient; the child depends only on
`A,b,l`, so no endpoint or child multiplicity is lost. Similarly,

```text
rho_s(k,t)=w_t C(s-t,k-1)/[k!w_(s+1)].             (2.7)
```

The fresh implementation compares (2.6)--(2.7) against literal direct
composition/basin enumeration for all

```text
2<=s<=7, 1<=K<=4, 0<=R<K, every B, d in {0,1,2}.
```

There are 810 contexts and 1,620 separate `D`/`J` exact equalities, with
zero failures.

### 2.7 Conditional reset-occupation implication — accepted

Let

```text
W(x)=(1-q_x)K/(R+1).
```

Every reset target `y` is right-heavy, so `W(y)=1-q_y`. Section 2.3 gives

```text
1/3<=W(y)<=1.                                      (2.8)
```

Assume, without claiming, M82's proposed inequality `K_reset W<=W` on every
active right-heavy seed. For

```text
mu_n=delta_x K_reset^n
```

with right-heavy `x`, positivity and iteration give

```text
mu_n W<=W(x)=1-q_x<=1,
mu_n 1<=3mu_n W<=3.                                (2.9)
```

Every reset epoch strictly lowers the positive integer `P`, so
`mu_n=0` for `n>=P(x)`. The accepted predecessor base-excursion estimate is

```text
b(z)<=eP(z)^2[1+log P(z)].
```

Since `P(z)<=P(x)` along the descent, (2.9) yields exactly

```text
sum_(n<P)mu_n b
 <=P*3*eP^2(1+log P)
 =3eP^3(1+log P).                                  (2.10)
```

Thus M82's implication and constant are correct. It remains conditional on
the unproved weighted inequality; M71's one-shot `O(r^9)` unmarking estimate
does not remove that antecedent.

### 2.8 Scope and terminal status — accepted

M82 labels the proposed eliminated weighted inequality as its “first
unproved lemma,” calls every surviving scan finite evidence only, and states
that marked occupation, ROOT-MEAN LIFT, the auxiliary `Pbar` gap, and every
conclusion for the original chain remain unresolved. The failures concern
proof templates or an auxiliary row inequality, not a stationary-mass cut or
spectral-gap upper bound for the literal heat-bath chain. Terminal A and
Terminal B both remain unresolved.

## 3. Probability, normalization, runtime, and accounting

- All independent promoted values use Python `fractions.Fraction`; binary64
  decimals are presentation only.
- Python was `3.12.3`; seed `null`; nonstandard dependencies `{}`.
- The independent main audit ran for `371.13` seconds, dominated by the
  rank-120 floor enumeration. The full rank-eight scan ran for `1.30`
  seconds; the fresh-seed rank-eleven scan ran for about five seconds.
- Root composition masses, contextual means, every parent `q_x` divisor,
  every reset capacity, strict phase descent, and right-heavy reset output
  are asserted in the fresh code.
- The rank-120 term counts and both floor integers agree exactly, not merely
  numerically, with M82.
- The finite scans prove only their displayed finite statements. The
  universal split bound and floor sign use separate analytic/exact rational
  arguments.

## 4. Dependencies and claim status

| input or claim | status in this audit | basis |
|---|---|---|
| root-composition/canonical-basin formulas | frozen accepted dependency plus independently reconstructed normalization | M50 and fresh direct enumeration |
| contextual observable and rank inheritance | frozen accepted dependency plus independently reconstructed formulas | M56/M65/M69 and fresh exact means |
| pure-deep base bound and one-shot unmarking | frozen accepted dependency | M71 |
| strict phase descent/reachable closure/resolvent | proved and independently rechecked | M76/M79 and Section 2.2 |
| `q(a,b)<=2/3` on active ranks | proved | Section 2.3 |
| grouped Cayley formula | proved and independently checked | Section 2.6 |
| all-context unweighted row bound | refuted | exact witness (2.5) |
| raw constant and `d=0,1,2` Bellman inequalities | refuted at stated exponents | exact certificates in Section 2.5 |
| right-heavy unweighted, multitype, and weighted eliminated inequalities | exact finite evidence only | rank-eight/rank-eleven scans |
| universal weighted eliminated lemma | unresolved | no proof or counterexample |
| marked occupation / ROOT-MEAN LIFT / `Pbar` gap / original `K` gap | unresolved | conditional chain stops at the preceding row |

## 5. First unproved standalone step

The first unresolved statement is exactly:

> **DEEP-ELIMINATED BETA-BINOMIAL RESET SUPERSOLUTION.** For every active
> reachable right-heavy seed `x=(s,K,K-1,B)`, with the normalization in
> Section 2.1,
> ```text
> sum_y [(I-D)^(-1)J_can](x,y)W(y)<=W(x),
> W(x)=(1-q_x)K/(R+1).                             (5.1)
> ```

Because reset targets are right-heavy, (5.1) is equivalently

```text
sum_y K_reset(x,y)(1-q_y)<=1-q_x.
```

No accepted argument presently controls the cancellation across the complete
pure-deep excursion. The attachment harmonicity motivates the weight but is
not itself a proof.

## 6. Strongest self-attack and documentation note

The strongest mathematical self-attacks all survive scrutiny:

- the all-context eliminated unweighted row already exceeds one at (2.5);
- every tested raw power `P^dW` for `d=0,1,2` eventually fails;
- the raw constant row fails even at local rank three;
- the finite margins for (5.1) could still shrink and reverse at larger rank.

None of these refutes (5.1), because raw deep continuation is precisely what
the resolvent aggregates and repeated reset outputs are right-heavy.

Nonmaterial archival note: M82's bundle states its bounded grouped-versus-
direct validation but does not freeze a separate direct-comparison output.
M87 supplies an independent reproducible direct harness and machine-readable
result covering 1,620 exact equalities. This does not affect any mathematical
claim or the verdict.

## 7. Calibration and exceptional cases

- Active contextual local rank is `s>=2`, with `1<=B<=s`.
- `(K,R)=(1,0)` is the only reachable case with `R=0`; otherwise
  `K>R>=1`.
- The split pair `(1,1)` is excluded only because it yields discarded local
  rank one; it must not be silently included in the `q<=2/3` theorem.
- The right-heavy set is exactly `K-R=1`, including fresh seeds `(1,0)`.
- This auxiliary result introduces no new statement for odd `m`, `m=0,2`,
  or `N=2`. For the background chain, odd `m` is empty and the main target
  remains `N>=3`, even `m>=4`.
- Polynomial control in the auxiliary rank would still require all accepted
  comparison steps before implying a polynomial in `N,m`; no wire-count
  efficiency claim follows.

## 8. Artifacts, hashes, and reproduction

Owned artifacts before adding this report have these SHA-256 digests:

```text
471a1569c325ddb48e0be7ded202fab58b9eed4daf79e67660006335ca5b97fa  plan.md
bb099390620faa859d44a119536a4630a2d9ad568d0ea4ebbfe095369bf21c3b  checkpoint.md
47aa22af82bc0c23965fd4ddd6ed15e98e8da3f3a3ce4df351d6a7e9f62e7f93  independent_audit.py
dc9f7030023ceef48da0c27b53ac678267545572efe811430319c01f4901f29d  independent_audit.json
a9b61fe0d1776f73a634d6d60a5fcb2b8895a8f34724c4596bc2bdf515cb60e0  independent_audit_prelim.json
4a6e82a45f0c3ce559c211c51a61608e860baa65298a7ba568b126cc1ad1fcad  finite_s8_audit.py
fdbc8a803a858445a6de6057d2c348098fcb250f41ad3c86dfb19544b792a03d  finite_s8_audit.json
```

Primary reproduction commands, run from the M87 directory, are

```text
python3 -B independent_audit.py --include-d2 \
  --output independent_audit.json

python3 -B finite_s8_audit.py
```

The first command imports no predecessor code. The second imports only the
owned independent core. A final read-only cross-bundle comparison checked the
rank-eight context/failure data, exact `d=0,d=1` ratios, both `d=2` floor
integers and term counts, and the full positive rational margin; every
comparison returned exact equality.

## 9. Verdict and numbered objections

```text
REFEREE VERDICT: ACCEPT M82.
MATERIAL OBJECTIONS: NONE.
NUMBERED OBJECTIONS: EMPTY.
```

The accepted scoped conclusion is:

```text
PROVED: q<=2/3 ON EVERY ACTIVE SPLIT AND THE CONDITIONAL
        <=3 RESET-EPOCH-MASS / <=3eP^3(1+log P) IMPLICATION.
REFUTED: THE ALL-CONTEXT UNWEIGHTED ELIMINATED ROW BOUND AND
         THE RAW CONSTANT/d=0/d=1/d=2 BELLMAN TEMPLATES.
UNRESOLVED: THE RIGHT-HEAVY DEEP-ELIMINATED WEIGHTED LEMMA,
            MARKED OCCUPATION, Pbar GAP, AND ORIGINAL K GAP.
NO TERMINAL-A OR TERMINAL-B CLAIM.
```
