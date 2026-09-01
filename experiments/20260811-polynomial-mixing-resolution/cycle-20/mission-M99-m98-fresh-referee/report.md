# M99 fresh referee report on frozen M98

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, exact accepted claim, convention, and scope

```text
ACCEPT M98 WITH ZERO MATERIAL NUMBERED OBJECTIONS.
```

The accepted theorem is the following narrow negative result. For the full
**nonlazy stationary-flow parking-degree projection** in the minimal
long-cycle factorization sector, M90's transformed one-step defect satisfies

```text
r_U(16,K,K-1,4)<0                 for every integer K>=710.       (1.1)
```

Every context in (1.1) is reachable from a fresh context. Consequently the
proposed universal nonfresh premise `r_U>=0` is **refuted** by an explicit
infinite family.

This is not a slow mode, a gap upper bound, or a result for the original lazy
exact same-product `{3,4,5}` heat-bath chain on identity words. The fresh
two-level condition, the proposed global two-layer condition, both universal
full-resolvent inequalities, the auxiliary `Pbar` gap, ROOT-MEAN LIFT, the
original heat-bath gap, and Terminals A and B all remain **unresolved**.

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. No external literature theorem is invoked by the accepted
claim.

## 2. Frozen provenance and package integrity

The assigned frozen digests match exactly:

| M98 artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `fcf92cf8222aec8f4675b56fc86fda0cb676a37aac79320571eb7a8856e34476` | match |
| `SHA256SUMS` | `2a8772686dfcfdc4d16103c4ff2b32ff5a0f610da5988184eb7410e69f81521e` | match |

All eight entries in M98's manifest independently return `OK`. The fresh
audit imports no M98 or predecessor Python module. It reads M98's frozen JSON
only after independently computing each decisive value, then requires exact
numerator-and-denominator equality.

No M98, predecessor, coordinator note, manuscript, project skill, or shared
source was edited.

## 3. All-rank normalization and contextual/right-heavy formulas

For a root group with part count `k` and last part `t`, the independently
reconstructed mass is

```text
rho_s(k,t)=w_t c(s-t,k-1)/[k! w_(s+1)],
w_a=a^(a-1)/a!,
c(n,p)=p n^(n-p-1)/(n-p)! .                       (3.1)
```

Literal ordered compositions reproduce (3.1) and total mass one through
rank eight. The fresh audit checks 92 nonzero literal root groups.

The attachment law is

```text
nu_(K,R,k)(j)
 =binom(R+j,j) binom(K-R-1+k-j,k-j)/binom(K+k,k),
                                                    0<=j<=k.     (3.2)
```

Chu--Vandermonde gives `sum_(j=0)^k nu(j)=1`. The transformed live operator
retains **every** `j=1,...,k`; `j=0` is the killed branch. This distinction is
implemented correctly by M98. Exact normalization was checked for every
`1<=K<=8`, `0<=R<K`, `1<=k<=8`, and for right-heavy `K=709,710`,
`1<=k<=16`, totaling 320 laws.

For right-heavy `R=K-1`, (3.2) becomes

```text
nu(j)=binom(K-1+j,j)/binom(K+k,k),                 (3.3)
```

so `nu(k)=K/(K+k)->1`, while each fixed `j<k` tends to zero. This justifies
retaining only `j=k` in the limit and nowhere at finite `K`.

Direct substitution in the accepted contextual formula gives

```text
H_K(k,t)=0,                                        t<B,
H_K(k,B)=k!/product_(i=1)^(k-1)(K+i),
H_K(k,t)=q_(t-1,B)
           [1-k!/product_(i=1)^k(K+i)],            t>B.           (3.4)
```

The general and specialized formulas agree in 484 exact checks. Their root
average is exactly `q_(s,B)` at each tested finite `K`, including `709` and
`710`. Letting `K` tend to infinity in (3.4) yields exactly M98's

```text
H_infty(k,t)=0                 (t<B),
              1                 (t=B,k=1),
              0                 (t=B,k>=2),
              q_(t-1,B)         (t>B).             (3.5)
```

No all-rank normalization or finite contextual factor is missing.

## 4. Cayley/basin coefficient and limiting decomposition

The canonical-basin coefficient is

```text
L_(A,ell)=sum_(p=1)^A c(A,p)/(p+ell)!.             (4.1)
```

Using the beta identity for `1/(p+ell)!` and
`[z^A]exp(uT)=u(u+A)^(A-1)/A!`, the fresh derivation gives

```text
L_(A,ell)
 =1/(ell-1)! integral_0^1 (1-u)^(ell-1)
    u(u+A)^(A-1)/A! du.                            (4.2)
```

Equation (4.2) was evaluated as an exact finite beta sum and matched (4.1)
in 136 pairs with `A+ell<=17`, covering every pair used at rank 16. For
`A<=8`, a third, literal sum over every ordered refinement of `A` also agrees. Literal
endpoint/basin currents reproduce six grouped weighted or unweighted reset
energies, and literal limiting energy coefficients reproduce every grouped
coefficient through ranks two to eight.

At `(s,B)=(16,4)`, let `m_(s,t)` be the stationary last-part mass and
`e_(s,t)` the canonical reset-energy coefficient. Exact stationary averaging
gives `E_rho H_infty=q`, and hence

```text
q(1-q)-Q_infty U=Var_rho(H_infty).                 (4.3)
```

The basin calculation gives

```text
A_infty=sum_t e_(s,t)[H_infty(t)-q]^2.             (4.4)
```

Combining (4.3)--(4.4) gives

```text
r_infty(16,4)
 =sum_t [m_(16,t)-e_(16,t)][H_infty(t)-q]^2

=-9227444489897033899069928546555383705889289522405715688049247702588321735512746884149350887011428507035652533537
 /206939781608101554317882579170416040081179045783441942415142310077467888193085115142449958815210345070592000000000000
<0.                                                     (4.5)
```

Every mass, energy coefficient, square, and contribution in the 16
last-part fibres matches M98 exactly. The negative coefficients are precisely
`t=3,4,5,6,7,8`. Thus (4.5) is a signed exact decomposition, not a decimal
extrapolation.

## 5. Direct denominator clearing, finite signs, and Newton tail

The most important fresh check avoids fitting a polynomial from 34 values.
Put

```text
D(K)=product_(i=1)^16(K+i),
P(K)=D(K)^2 r_U(16,K,K-1,4).                       (5.1)
```

The audit constructs every coefficient of `P` directly in `Q[K]`. From
(3.4), each contextual denominator divides `D`, so the squared canonical
current has denominator dividing `D^2`. For a deep rank `j`,

```text
nu(j)(K+k)/(K+j)
 =(k!/j!)
   [K(K+1)...(K+j-1)(K+k)]
   /[(K+1)...(K+k)(K+j)].                          (5.2)
```

The denominator in (5.2) divides `D^2`; after clearing, its degree is
`32+j-k<=32`. The cleared `U` and reset terms also have degree at most 32.
Componentwise evaluations of cleared `U`, `A`, `QU`, every contextual
numerator, and every deep multiplier give 520 additional exact checks.

The directly constructed `P` has actual degree exactly `32`. Its leading
coefficient equals the exact negative limit (4.5), as it must because `D` is
monic. Polynomial evaluation and a separate rational recurrence agree and
reproduce M98's exact signs:

```text
r_U(16,709,708,4)= 1.983359607144234...e-8 >0,
r_U(16,710,709,4)=-4.279501288526443...e-8 <0.      (5.3)
```

At `K=710`, the negative numerator is exactly

```text
-661615179812287703733401538288146672176656056694303980320445480238015535840763927227096436539021950529551118381660089830702424942161641416917615391141563,
```

over the positive denominator frozen in both exact JSON files.

Fresh forward differences of the directly constructed polynomial satisfy

```text
Delta^d P(710)<0       for every 0<=d<=32,
Delta^33 P(710)=0.                                      (5.4)
```

All 33 nonzero coefficients match M98 as exact fractions. Newton's identity

```text
P(710+n)=sum_(d=0)^32 Delta^dP(710) binom(n,d)          (5.5)
```

therefore proves `P(710+n)<0` for every integer `n>=0`. Since `D(K)^2>0`
there, (1.1) follows rigorously.

## 6. Reachability, finite DAG, and full-resolvent survival

For every integer `K>=710`, start from the fresh context

```text
(K+15,1,0,4).
```

The positive root composition `(1^(K-2),17)` has part count `K-1`. Taking
attachment rank `j=K-1` has exact conditional probability `1/K` and produces

```text
(17-1,1+(K-1),0+(K-1),4)=(16,K,K-1,4).             (6.1)
```

Thus every member of the counterfamily is genuinely in the reachable
closure, not merely a formal context.

For a deep child `y=(t-1,K+k,R+j,B)`, the phase `P=s+K-R` decreases by

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,                          (6.2)
```

because the `k-1` parts before `t` have total at least `k-1`. Hence the
resolvent computations are finite DAG sums.

At the first witness, the independent exact recursion reproduces

```text
weighted full-resolvent ratio   =.4080533675130647...<1,
unweighted full-resolvent ratio =.5988444277550840...<1.          (6.3)
```

It also reproduces

```text
r_U+Qr_U=.006513975507625593...>0.                  (6.4)
```

Equations (6.3)--(6.4) are exact **finite calibrations only**. They confirm
M98's strongest self-attack: later positive compensation is substantial, so
the local counterfamily neither violates either full resolvent nor supplies
a conductance bottleneck.

## 7. Dependencies, boundaries, and strongest self-attack

The audit treats the accepted M50/M56/M65/M69 and
M71/M76/M79/M82/M87/M90/M96 formulas as inherited definitions and inputs,
then independently checks every new algebraic step used by M98. In
particular:

- **proved and independently accepted:** all-rank finite formulas,
  right-heavy limit, variance/energy decomposition, Cayley/beta coefficient,
  exact negative limit, degree-32 clearing, Newton tail, and reachability;
- **refuted:** universal nonfresh one-step defect positivity;
- **exact finite only:** the `K=710` two-layer and full-resolvent survival
  values;
- **unresolved:** every global two-layer or full-resolvent inequality and all
  gap/mixing consequences.

The strongest attack on (1.1) was that `Delta^33P=0` at sampled integers
might be an interpolation artifact. The direct coefficient construction
eliminates that concern and separately checks `U`, `A`, and `QU`; the degree
bound is structural, not inferred from the samples. A second possible attack
was a missing finite attachment rank. Exact normalization and the live
`j=1,...,k` loops eliminate that concern.

The result lives at active auxiliary rank `s=16`, `B=4`, `K>R>=1`. Odd
identity length, `m=0`, `m=2`, and `N=2` are exceptional cases of the
original chain and are outside this lemma. No claim about them is made.

## 8. Artifacts, reproduction, runtime, and hygiene

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-20/mission-M99-m98-fresh-referee/
```

The exact audit is reproduced from repository root with

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-20/mission-M99-m98-fresh-referee/independent_audit.py
```

The final exact run took about `4.1` seconds and at most about `22` MiB RSS
under Python `3.12.3`. It is deterministic (`seed=null`), uses only the
standard library, and writes `independent_audit.json`. The raw file records
the direct polynomial coefficients, all Newton coefficients, every limiting
fibre, finite signs, reachability, exact resolvents, and frozen provenance.

Owned source compilation by execution, JSON parsing, M98 manifest
verification, `git diff --check`, and owned-directory cache hygiene are
checked before freeze. No cache was created in M99. A pre-existing cache in
M90's directory lies outside this worker's ownership; it was reported to the
coordinator and not modified.

## 9. Final verdict, numbered objections, and handoff

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M98 correctly refutes the old universal nonfresh one-layer sign by the exact
reachable family (1.1), while preserving the much narrower logical scope of
that refutation. The first surviving falsifiable target is the global
two-layer defect

```text
r_U+Qr_U>=0
```

on every reachable active context, or directly either full weighted or
unweighted resolvent inequality. None is established by M98 or this audit.
