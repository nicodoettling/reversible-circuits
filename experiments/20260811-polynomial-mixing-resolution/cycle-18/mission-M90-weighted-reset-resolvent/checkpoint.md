# M90 halfway checkpoint: exact grouped resolvent and contextual variance lead

Date: 2026-08-12. Frozen predecessor base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and normalization

This checkpoint concerns only the full nonlazy stationary-flow parking-degree
projection `Pbar_r` in the minimal long-cycle sector. It makes no statement
about the original lazy identity-word heat-bath kernel `K`.

For `x=(s,K,R,B)`, retain M82's exact normalization

```text
q_x=w_(s+1-B)w_B/w_(s+1),
J_can(x,y_e)=theta_e^2/[Q_G(e)q_x],
D(x,y)=rho_s(k,t)q_y nu_(K,R,k)(j)/q_x.
```

Every retained child strictly lowers `P=s+K-R`. Define

```text
F(x)=[(I-D)^(-1)J_can W](x),
W(x)=(1-q_x)K/(R+1),
g(x)=q_xF(x).
```

Because every reset target is right-heavy, exact cancellation of the parent
and child split masses gives the grouped whole-excursion recurrence

```text
g(x)=A(x)+sum_(k,t,j>=1) rho_s(k,t)nu_(K,R,k)(j)g(y),
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)),
y=(t-1,K+k,R+j,B).                                (C.1)
```

All `j=1,...,k` are retained. A preliminary discovery implementation which
incorrectly retained only `j=k` on right-heavy parents was caught because it
gave `.4725...` instead of M82's exact rank-eleven `.539149...`; it was fixed
before any result below was recorded, and all owned discovery JSON was
overwritten from the corrected recurrence.

## Independent exact recurrence and finite falsification

`exact_weighted_resolvent.py` implements (C.1) with exact Cayley grouping and
`fractions.Fraction`, without importing predecessor code. It reproduces
M82's exact ratios at both frozen calibration maxima:

```text
(8,1,0,4):  .43715035400213015...
(11,1,0,5): .5391499615007582...
```

The second numerator and denominator agree exactly with M82's frozen JSON.
An exact scan over

```text
s in {12,14,16,18,20},
K in {1,2,4,8,16,32}, R=K-1, every 1<=B<=s
```

finds no violation. Its worst row is

```text
x=(20,1,0,7),
g/[q(1-q)]=.6781776227304538...<1,
q(1-q)-g=.012069769767893484...>0
```

with the sign stored as an exact rational. Exact fresh-seed scans at ranks
22 and 24 also find no violation; rank 24 peaks at `(24,1,0,9)` with ratio
`.7076960352612462...` and exact positive margin `.008104059498624878...`.
These are bounded falsifiers only and prove no universal inequality.

## Stronger whole-excursion variance route

Let `Phi_x` be M56/M65's pointwise contextual suffix statistic on a local
parking macro with stationary mean `q_x`, and put

```text
V(x)=Var_(pi_s)(Phi_x).
```

The natural stronger statement is

```text
g(x)<=V(x)                                          (C.2)
```

on every reachable context. For a right-heavy seed, the constrained-shuffle
interpretation makes `0<=Phi_x<=1`; hence

```text
V(x)<=q_x(1-q_x),
```

and (C.2) would prove the assigned lemma.

An exact microstate audit of every realizable context through ambient rank
seven finds no violation of (C.2). More sharply, it finds no violation of
the one-step variance remainder

```text
A(x)+sum_(k,t,j)rho_s(k,t)nu_j V(y)<=V(x).          (C.3)
```

The tightest tested ratio is

```text
61153941593/64041192000=.954915...,
x=(5,2,1,2) in ambient rank 7.
```

The same exact audit verifies the beta-binomial variance envelope
`V(x)<=q_x(1-q_x)K/(R+1)` on every tested context, with equality at the
minimal fresh context `(2,1,0,2)`.

Equation (C.3), if proved, telescopes by strict `P` descent and gives (C.2)
without using any refuted raw `P^dW` Bellman inequality. Its root-level
content is precise: `Var(H_x)` must pay both the weighted canonical reset
energy and the conditional-variance loss incurred when the hidden
negative-hypergeometric attachment rank `J` is separated into distinct deep
children. This is the current Bessel/Doob filtration target.

## Status and next step

- **Proved here:** exact grouped recurrence (C.1), strict-phase validation in
  the implementation, and exact agreement with the frozen M82 values.
- **Exact finite:** no assigned-lemma failure through the displayed rank-24
  scans; no contextual-variance or one-step-remainder failure through ambient
  rank seven.
- **Unresolved:** the universal inequalities (C.2)--(C.3), the assigned
  right-heavy lemma, marked occupation, the auxiliary `Pbar` gap, and every
  claim for the original chain.
- **Next:** express the reset scores and separated `J`-children as orthogonal
  increments of the augmented contextual-event filtration, or extract the
  first exact cross-term obstruction if that Bessel system is not contractive.

## Post-checkpoint corrections and boundary-layer finding

The exact mixed-second-moment recursion later refuted both variance claims
that were still open at the halfway point. The raw supersolution (C.3) first
fails at the right-heavy context `(6,2,1,2)`:

```text
V-A-QV=-21394206021215/36917038301316768<0.
```

The whole-excursion strengthening `g<=V` fails on non-right-heavy reachable
contexts by rank twelve; at `(12,32,5,4)` its exact ratio is
`1.0802089991127168...`. This does not refute the assigned right-heavy
`g<=U` inequality because the same context has a much larger beta-binomial
budget `U`. All eight tested scalar interpolants
`M=V+a(U-V)` are also refuted exactly by rank twelve, including failures at
the fresh seed `(12,1,0,4)`. Thus the tentative variance route above is
withdrawn, not promoted.

The exact identity behind its failure is nevertheless useful. If `C` is the
root composition and the deep child observables are mixed with M65's full
attachment law, then

```text
r_V=V-A-QV
   =Var(E[Phi|C])-A-L_attach,                       (C.4)
```

where `L_attach>=0` is exactly the Jensen loss between the average of child
variances and the variance of their correlated mixture. The positive term
`Var(E[Phi|C])` does not always pay both `A` and `L_attach` locally.

For the actual budget `U=q(1-q)K/(R+1)`, put `r_U=U-A-QU`. Nilpotence gives
the exact entire-excursion identity

```text
U-g=sum_(d>=0) Q^d r_U.                             (C.5)
```

On the full deep closure of every fresh seed through rank twenty, all
nonfresh defects are positive and every fresh two-level block
`r_U+Qr_U` is positive. Hence every positive-depth contribution in (C.5)
is positive in that bounded audit, even where the depth-zero defect is
negative. These signs are exact finite evidence only. They isolate the
new standalone proof target: prove `r_U>=0` on all reachable nonfresh
contexts and `r_U+Qr_U>=0` on all fresh contexts.

Finally, the stronger sufficient inequality

```text
K_reset 1(x)<=1-q_x
```

also survives an independent exact all-`j` scan through rank twenty, with
largest ratio `.7893855076290114...` at `(20,1,0,6)`. It would imply the
assigned weighted inequality because every reset target has
`W(y)=1-q_y<=1`. A direct Bessel proof is not available: already at
`(8,1,0,3)`, `q K_reset1/Var(Phi)=1.020118...`, and at `(11,1,0,4)` the
raw reset energy exceeds `Var(E[Phi|C])` by a factor `1.077622...`.
