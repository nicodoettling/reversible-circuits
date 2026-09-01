# Exact marked-history density recurrence

Date: 2026-08-11.  Write `P=Pbar_r`,
`alpha=2/[3r(r-1)]`, and let `L_k={d in J_r:d_0=k}`.  Let `pi_k` be
`pi_r` conditioned on `L_k`.  The exact root-degree law is

```text
p_k=pi_r(L_k)
   =binom(r-1,k-1) r^(r-k)/(r+1)^(r-1), 1<=k<=r.    (1.1)
```

## 1. Canonical and random-boundary kernels

For `x in L_k`, let `M_k(x,y)` retain only moves that merge the first two
root branches.  M50 gives total rate `alpha k` for that boundary, so

```text
M_k(x,y)=P(x,y)/(alpha k)                            (1.2)
```

on its support.  This is a stochastic kernel from `L_k` to `L_(k-1)`.
The uniform-boundary variant retains every root-decreasing move and has

```text
Mtilde_k(x,y)=P(x,y)/[alpha k(k-1)].                 (1.3)
```

Iterating either kernel until `L_1` is the marked coalescence map.

## 2. Exact reverse-history recurrence

Let `eta_k` be the unnormalized distribution in layer `k` after all original
states with root degree at least `k` have been coalesced down to that layer.
Thus

```text
eta_r=p_r pi_r,
eta_(k-1)=p_(k-1)pi_(k-1)+eta_k M_k.                (2.1)
```

Put `h_k=d eta_k/d pi_k`.  Reversibility gives the exact pointwise
recurrence

```text
h_r=p_r,
h_(k-1)(y)=p_(k-1)
 +[p_(k-1)/(p_k alpha k)]
   sum_(x in L_k:first-merge(x)=y) P(y,x)h_k(x).     (2.2)
```

For the uniform-boundary schedule, replace `alpha k` by
`alpha k(k-1)` and sum over every `x in L_k` adjacent to `y`.

At `k=1`, `eta_1` has total mass one, so `g_r=h_1` is exactly the
Radon--Nikodym density of the endpoint law with respect to `pi_1`.  Equivalently,
for the canonical schedule,

```text
g_r(y)=p_1 sum_(reverse first-split histories from y)
             product_(layer k step) P(x_(k-1),x_k)/(alpha k).  (2.3)
```

The zero-step history gives the universal pointwise lower bound

```text
g_r(y)>=p_1=(r/(r+1))^(r-1)>=e^(-1).                (2.4)
```

Formula (2.3) is the requested valid ordered-cut-history partition
function.  Its nonzero terms are shape-dependent.

## 3. Exact failure of stationary normalization

At the smallest nontrivial case `r=3`, start in root composition `(1,2)`
with its stationary conditional law and merge its only boundary.  The
output and stationary target laws on the unary-root macros are

```text
macro                 output       pi(. | root composition (3))
(0,1,1)                  0                       1/3
(0,1,2)                  1                       2/3.
```

The density is therefore `0,3/2`.  The star-under-the-root target has no
valid right-spine cut of the required ordered sizes.  Marking the cut makes
the bijection exact, but forgetting the mark does not give the stationary
coarse-fiber law.

Mixing over every initial root degree softens but does not remove the bias.
At `r=3`, canonical coalescence has endpoint densities `15/16,33/32` and
total variation `1/48`; uniform-boundary coalescence has densities
`57/64,135/128`.

## 4. Exact finite L2 diagnostics

The bounded audit gives the following endpoint chi-square divergences from
`pi_1`:

```text
r       2          3          4          5          6          7
canonical
        0       .001953    .007494    .013191    .018295    .022713
uniform boundary
        0       .005981    .013141    .019619    .025157    .029839
```

The exact rational values and extremizers are in `marked_history_n8.json`.
Canonical pointwise density through `r=7` lies between approximately
`.6994` and `1.3262`; the extreme low state is the unary root above a star.
These finite values are compatible with small aggregate distortion but do
not prove any asymptotic bound.

## 5. Surviving proposition

> **MARKED-HISTORY L2 CONTROL.**  Prove an exact bound on the recurrence
> (2.2) strong enough that its endpoint and prefix occupation densities
> incur only a multiplicative `1+O(1/r)` loss in the recursive all-pairs
> flow (an `O(1/r)` chi-square bound is a candidate), and prove that the
> resulting edge loads are additive/polynomial rather than a constant loss
> multiplied once per depth.

A constant pointwise bound at one recursion level is not sufficient:
raising a fixed constant through depth `Theta(r)` is exponential.  The
recurrence (2.2), rather than the product of the crude one-step Radon bounds,
is the smallest exact object that must be controlled.

## 6. Factorially weighted nested-split partition

There is a useful cancellation which is not visible in (2.2).  Let
`y_1 in L_1`, and let

```text
y_1 <- y_2 <- ... <- y_k
```

be a reverse canonical history: `y_l in L_l`, and `y_l -> y_(l-1)` is
the forward merge of the first two root branches.  Put

```text
a_l(y_(l-1),y_l)=P(y_(l-1),y_l)/alpha.              (6.1)
```

If the reverse split removes a degree unit from a vertex whose degree in
`y_(l-1)` is `q_l`, then

```text
pi(y_l)/pi(y_(l-1))=q_l/l.                          (6.2)
```

Detailed balance and the forward normalization `alpha l` give

```text
[pi(y_l)/pi(y_(l-1))]
 [P(y_l,y_(l-1))/(alpha l)]
 =P(y_(l-1),y_l)/(alpha l)=a_l/l.                   (6.3)
```

Therefore, if `H_s(y)` is the total product of the `a_l` weights over all
length-`s` nested reverse histories from `y`, with `H_0=1`, then the exact
endpoint density is

```text
g_r(y)=p_1 sum_(s=0)^(r-1) H_s(y)/(s+1)!.           (6.4)
```

Every reverse step cuts a last-child suffix subtree from the current first
root branch; all previously cut branches remain an ordered root suffix.
Thus (6.4) is literally a nested right-spine suffix-cut partition function,
not merely an algebraic path sum.

Its first moments are explicit.  The mass supplied by initial layer
`L_(s+1)` is `p_(s+1)`, so

```text
E_(pi_1) H_s=(s+1)! p_(s+1)/p_1
 = (s+1)! binom(r-1,s)/r^s <=s+1.                   (6.5)
```

Equations (6.4)--(6.5) are universal consequences of reversibility and the
accepted M50 boundary normalization.  The exact probe checks both identities
without a failure through `r=7`.

## 7. Two tempting bounds and the corrected sufficient condition

The individual canonical reverse first-split bound

```text
P(y,x)<=alpha                                         (7.1)
```

has no exact counterexample through `r=7`, but remains unproved.  More
importantly, the literal harmonic bound on the total first-split propensity
is false.  At global `r=5`,

```text
y=(0,0,1,2,3),  root composition (4,1),
sum_(canonical first refinements x) P(y,x)/alpha=13/6>H_4=25/12.  (7.2)
```

Even in the unary layer it first fails at tested `r=7`:

```text
y=(0,1,1,3,4,5,6),
sum_x P(y,x)/alpha=157/60=H_7+1/42.                 (7.3)
```

Thus neither `H_(first branch size)` nor `H_r` may be cited as proved.
The following robust replacement would still yield polynomial endpoint
density:

> **LOGARITHMIC NESTED-SPLIT PROPENSITY.**  There is a universal `C` such
> that, in every layer and every suffix context,
> `sum_x P(y,x)/alpha <= C log(r+1)` over canonical first refinements.

Indeed the recursive definition of `H_s` would give

```text
H_s(y)<=[C log(r+1)]^s,
g_r(y)<=p_1 exp(C log(r+1))<=(r+1)^C.               (7.4)
```

This proves only polynomial endpoint `L-infinity`, hence polynomial `L2`;
it does not by itself make recursive edge loads additive.  Exact values
through `r=7` are compatible with the logarithmic replacement, but finite
agreement is not evidence for the universal inequality.

## 8. Alignment with the stronger H-minus frontier

M54 gives the sharper sufficient functional **SPINE-BIAS H-minus-one
BOUND**.  Endpoint control in (6.4) is one possible way to build its
effective-resistance flow, but the literal task is now to prove

```text
sum_(a refining b) ||ell_(b,a)||_(-1,b)^2/q_(b,a)
 <= A r^C.                                           (8.1)
```

The exact nested identity does not prove (8.1): first moments (6.5) do not
control pairs of histories or their internal edge occupation.  A valid next
step must bound the two-history intersection/effective-resistance term, not
multiply one-step Radon maxima.
