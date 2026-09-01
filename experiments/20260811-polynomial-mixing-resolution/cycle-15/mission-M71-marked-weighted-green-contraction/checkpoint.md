# M71 halfway checkpoint: the exact marked DAG survives, rank-only weights do not

Date: 2026-08-12.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and normalization

This mission concerns only the full nonlazy stationary-flow
parking-degree projection `Pbar_s` in the minimal long-cycle sector.  It
does not concern the identity bridge chain `K`.  Permutations compose as
`(pq)(x)=p(q(x))`; factors multiply left-to-right.

Write

```text
G_s=R_s/alpha_s,                 alpha_s=2/[3s(s-1)],
rho_s(C)=Z_s^(-1) [1/k!] product_i w_(c_i),
w_t=t^(t-1)/t!,                 C=(c_1,...,c_k).
```

For a contextual mark `x=(s,K,R,B)`, let `Phi_x` be M65's normalized
suffix statistic, `H_x(C)=E[Phi_x|C]`, and

```text
q_x=E H_x=w_(s+1-B)w_B/w_(s+1).
```

## H-001: exact child-mark-resolved Green DAG (proved accounting identity)

Let `theta_x` be the electrical root-quotient flow for
`rho_s(H_x-q_x)`.  For an undirected quotient edge `e`, orient its
refined endpoint as

```text
a=(...,A,B,...),        b=(...,A+B,...).
```

If `a` has `k` parts and the split boundary is `p` (zero based), the
residual contextual child has the exact mark

```text
y_e=(A+B-1, k-1, k-p-2, B).                         (H.1)
```

Its coefficient is

```text
[theta_x(e)^2/Q_G(e)]/q_x.                          (H.2)
```

On a deep root-composition group with `k` parts and last part `t>B`,
M65 marked inheritance gives children

```text
y_(k,t,j)=(t-1,K+k,R+j,B),        1<=j<=k,          (H.3)
```

with coefficients

```text
[rho_s(k,t) q_(t-1,B)/q_x]
  nu_(K,R,k)(j),                                    (H.4)

nu_(K,R,k)(j)
 =binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

Here `rho_s(k,t)` is the stationary mass of all compositions with
`k` parts and last part `t`, and
`q_(t-1,B)=w_(t-B)w_B/w_t`.  All children in (H.1) and (H.3) have
strictly smaller local rank than `s`.

Consequently, in M56's marked separated-capacity network, the exact
rank-resolved recurrence is

```text
T_x <= a_x
 +sum_(k,t>B,j) Wdeep(x,y_(k,t,j)) T_y
 +sum_e Wquot(x,y_e) T_y,                           (H.5)

a_x=||H_x-q_x||_(-1,G_s)^2/q_x.
```

The deep coefficients sum exactly to M56's `delta(x)`; the quotient
coefficients sum exactly to `a_x`.  Thus replacing all child values by
`max_(u<s)T_u` recovers M56's refuted scalar recurrence, while (H.5)
retains precisely the information lost there.  Equations (H.1)--(H.5)
follow by combining M56's exact electrical disintegration and
`alpha/gamma` cancellation with M65's pointwise marked inheritance.
No asymptotic or numerical input is used in this accounting identity.

## H-002: every rank-only polynomial Lyapunov weight fails (proved)

Fix an exponent `p>=0`.  A tempting repair assumes
`T_y<=C(rank(y))^p` in (H.5).  This cannot contract universally.

Take

```text
x_(s,K)=(s,K,K-1,s-1),       s>=2.
```

Only `C_0=(s)` is deep and only `C_1=(1,s-1)` is terminal.  Put

```text
h_s=w_(s-1)/w_s,
rho_0=rho_s((s))=w_s/w_(s+1),
lambda_s=sum_(A=1)^(s-1)w_Aw_(s-A)/w_s=2(s-1)/s.
```

The closed mean formula gives

```text
H(C_0)=h_s K/(K+1),       H(C_1)=2/(K+1),
q_x=rho_0 h_s,
deep mass/q_x=K/(K+1).                              (H.6)
```

Every quotient edge incident to `C_0` has residual child rank `s-1`.
The electrical demand at `C_0` is

```text
q_x[K/(K+1)-rho_0].
```

Its total incident conductance is `rho_0 lambda_s`.  Cauchy--Schwarz
for the incident electrical currents therefore forces rank-weighted
quotient energy at least

```text
q_x (s-1)^p
 h_s[K/(K+1)-rho_0]^2/lambda_s.                    (H.7)
```

Combining (H.6)--(H.7), the proposed weighted recursive coefficient is at
least

```text
(1-1/s)^p [
 K/(K+1)
 +h_s[K/(K+1)-rho_0]^2/lambda_s].                  (H.8)
```

Choose, for example, `K=s^2`.  Stirling gives

```text
h_s -> e^-1,       rho_0 -> e^-1,       lambda_s ->2,
```

so the lower limit of (H.8) is

```text
1 + e^-1(1-e^-1)^2/2 > 1.                          (H.9)
```

Hence every fixed rank power eventually amplifies.  This is an infinite
obstruction to a **rank-only proof template**, not a gap upper bound:
the child mark has suffix size `B=s-1` and becomes terminal after the
descent.  Forgetting `B` is exactly the false step.

## H-003: exact finite marked resolvent (empirical falsifier)

`marked_resolvent_probe.py` evaluates (H.5) recursively with every
`(K,R,B)` mark retained.  The rank DAG is finite because every child has
smaller rank.  Through `s=10`, scanning every `1<=K<=32`, every
`0<=R<K`, every `B`, and additional
`K=64,128,256,1024,4096` slices, the largest separated-capacity
resolvent values are

```text
s          2      3      4      5      6      7      8      9     10
max T   .444   .580   .671   .744   .790   .828   .857   .879   .898
```

The worst tested contexts have `K=4096,R=0` and moderate `B`.
The maximum deep-mass identity error is at floating linear-solve scale,
and the CG residuals are recorded in
`marked_resolvent_s10_k32.json`.  These values are compatible with

```text
T_x <=1-c/s
```

for a universal `c>0`, but are finite falsification evidence only.

`weighted_green_probe.py` separately confirms why coarse substitutes
are misleading.  Rank-only weights are headed toward the proved failure
(H.9).  A suffix-excess-only potential fails first on terminal hub
contexts, whose quotient disintegration creates nonterminal child marks.

## H-004: Schur complement and actual-edge collision

Let `A=I-Pbar_s` and split the Hilbert space into root-composition means
`M` and within-fibre fluctuations `Z`.  The exact root-mean energy
after harmonic relaxation is

```text
S=A_MM-A_MZ A_ZZ^dagger A_ZM.                       (H.10)
```

Positivity gives the qualitative contraction
`A_MZ A_ZZ^dagger A_ZM<=A_MM`.  The useful target is the quantitative
form

```text
A_MZ A_ZZ^dagger A_ZM
 <=(1-s^(-C))A_MM.                                  (H.11)
```

The finite marked values suggest an `s^-1` slack.  However (H.5) lives
in a network with history-separated capacity copies.  Different synthetic
histories can reach the same unmarked macro and actual edge.  Neither
(H.5) nor the finite `T_x<1` checks prove (H.11), because projecting
marked currents can create uncontrolled cross terms.

M70's full-twist theorem controls every nonzero cyclic character sector.
For a `U`-invariant test function, averaging (H.10) over all cyclic root
choices is therefore a plausible place for the history collisions to
cancel.  The parking macro is not deterministically conjugation-lumpable
(accepted M46), so this must be done on factorization microstates or the
exact averaged stationary-flow kernel, not by cyclically rotating a
degree vector.

## Remaining standalone proposition

> **MARKED DAG SLACK AND UNMARKING.**  Prove a universal
> `T_x<=1-s^-C` bound for the exact child-mark DAG (H.5), and construct
> its currents on actual unmarked `Pbar` edges with only polynomial
> additive load.  Equivalently, prove (H.11).  In the `U`-invariant
> long-cycle sector it is enough to prove the cyclic-root-averaged version,
> since M70 already controls every nonzero character.

The first half is now a completely explicit weighted-composition/electrical
DAG.  The second half is the surviving history-collision problem.  No claim
here is Terminal A or Terminal B for the original chain.
