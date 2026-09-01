# M83 report: endpoint-sharing influence and the balanced Borel tail

Date: 2026-08-12.

## 1. Exact claim, scope, and status

Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply from
left to right.  Fix odd `n=2l+1>=7` and

```text
h=(0 1 ... n-1).
```

The target law is the uniform minimal transposition-factorization bridge of
length `n-1` to `h`.  This report concerns M73's rank-two product-coordinate
kernel `bar K_n`, quotiented by simultaneous conjugation by `h`.  It is not
the identity bridge and does not itself prove a fixed-endpoint or global
mixing bound.

The assigned claim was

> for every edge `alpha~beta` of M80's strict endpoint-sharing graph
> `Lambda_n`,
> `TV(bar K_n^2(alpha,.),bar K_n^2(beta,.))<=C/n^2`.

Its status remains **unresolved**.  The principal new result is a rigorous
negative theorem about the tempting one-step shortcut:

> **Proved.**  Along `n=3k` with odd `k>=3`, there are strict
> endpoint-sharing neighbors `A_k,B_k` for which
> 
> ```text
> TV(bar K_n(A_k,.),bar K_n(B_k,.))
>     >= (4/(9e sqrt(pi))+o(1))/sqrt(k)
>     = (4sqrt(3)/(9e sqrt(pi))+o(1))/sqrt(n).
> ```

In particular the proposed premise

```text
max_(alpha~beta) TV(bar K_n(alpha,.),bar K_n(beta,.))=O(1/n)
```

is **refuted**.  This result does not refute the two-step claim: finite
calculations continue to show the required `n^-2` scale after applying the
second kernel, through cancellation between much larger signed pieces.

## 2. Exact kernel and accepted inputs

For an admissible rank-two product `g`, let

```text
A_g=F_(n-3)(g^(-1)h),
B_(g,s)=F_(n-5)((gs)^(-1)h),
a(g)=3 for an oriented 3-cycle and 2 for a noncrossing double.
```

M73 proved

```text
pi(g)=a(g)A_g/n^(n-2),
K(g,s)=a(s)B_(g,s)/A_g,
```

and proved that the cyclic quotient `bar K` is self-adjoint.  If the three
cycles of `g^(-1)h` have sizes `d_i` and ranks `r_i=d_i-1`, with
`r=n-3`, its exact row is

```text
K_g = sum_i r_i(r_i-1)/[r(r-1)] Emb_i mu_(d_i)
      +sum_(i<j) 2r_i r_j/[r(r-1)]
                    Emb_(ij)(nu_(d_i) tensor nu_(d_j)).       (2.1)
```

This is the four-schema decomposition `{I3,IS,IN,X}`.  The local first-edge
weight for a specified chord splitting a `d`-cycle into sizes `s,d-s` is

```text
tau(d)=d^(d-1)/d!,
w_d(s)=nu_d(e)=(d-2)! tau(s)tau(d-s)/d^(d-2).          (2.2)
```

M80 proved that the stricter graph `Lambda_n` has diameter at most four.
Consequently, if

```text
alpha_n=max_(O~O') TV(bar K(O,.),bar K(O',.)),
```

then Dobrushin submultiplicativity gives the exact implication

```text
delta(bar K^2)<=delta(bar K)^2<=16 alpha_n^2.          (2.3)
```

The theorem below proves that the `alpha_n=O(1/n)` premise needed by this
shortcut is false.

## 3. Proved balanced-tail proposition

Let `n=3k`, where `k>=3` is odd, and define the raw representatives

```text
A_k=(0,k,2k),
B_k=(0,1)(k,2k).
```

They are `Lambda_n` adjacent.  Indeed they have ordered lifts

```text
A_k=((k,2k),(2k,0)),
B_k=((k,2k),(0,1)),
```

and the differing chords `(2k,0)` and `(0,1)` share endpoint `0`.

Let `F_k` be the cyclic-invariant set of double-transposition target orbits
whose residual cycle sizes are

```text
(1,u,3k-1-u),       k<=u<=floor((3k-1)/2).             (3.1)
```

Equivalently, the target has a singleton residual cycle and both remaining
residual cycles have size at least `k`.

**Proposition 3.1 (proved).**  One has

```text
bar K(A_k,F_k)=0,
bar K(B_k,F_k)>=p_k,                                  (3.2)
```

where

```text
p_k = 2(2k-2)(k-1)/[(3k-3)(3k-4)]
      * (k-1)w_k(1)
      * {sum_(s=1)^(k-2) s w_(2k-1)(s)
         +2(k-1)w_(2k-1)(k-1)}.                      (3.3)
```

Moreover

```text
p_k ~ 4/[9e sqrt(pi k)]                               (3.4)
```

and, for every odd `k>=3`, the explicit weaker bound

```text
p_k >= 2/[27e^2 sqrt(k)]                              (3.5)
```

holds.  Therefore

```text
TV(bar K(A_k,.),bar K(B_k,.))>=p_k=Omega(n^(-1/2)).   (3.6)
```

## 4. Proof of Proposition 3.1

### 4.1 Residual components and the zero side

The residual cycles of `A_k^(-1)h` are the three contiguous blocks

```text
[0,...,k-1], [k,...,2k-1], [2k,...,3k-1],             (4.1)
```

all of size `k`.  In a minimal factorization of this residual permutation,
every transposition factor has both endpoints in one of these blocks.

A noncrossing double target with a singleton residual cycle contains a
polygon boundary edge.  This follows directly from M73's two double-gap
schemas: in the separated schema the residual sizes are `(x,z,y+w)`, and in
the nested schema they are `(x+z,y,w)`.  A size-one entry is exactly a
matched boundary gap.  If the other target edge lies inside one of the
contiguous blocks (4.1), one of the two nonsingleton residual sizes is at
most `k-1`.  Hence no target in `F_k` can occur in a minimal continuation
from `A_k`.  Because `F_k` is invariant under cyclic conjugation, this proves
the quotient identity `bar K(A_k,F_k)=0`.

The residual cycles of `B_k^(-1)h` are

```text
{0},
L=(1,2,...,k-1,2k,2k+1,...,3k-1),   |L|=2k-1,
M=(k,k+1,...,2k-1),                  |M|=k.            (4.2)
```

### 4.2 A B-only cross-schema subset

Choose one edge in each nontrivial component of (4.2):

```text
e=(i,j),  1<=i<=k-1, 2k<=j<=3k-1, k+1<=j-i<=2k,
f=(m,m+1), k<=m<=2k-2.                                (4.3)
```

The endpoints have cyclic order `i<m<m+1<j`.  Thus the target `t=ef` is a
noncrossing nested double and

```text
cycle sizes of t^(-1)h = (1,j-i-1,3k-(j-i)).          (4.4)
```

Both nonsingleton entries in (4.4) are at least `k`, so every target in
(4.3) belongs to `F_k`.

The probability that the first two residual-factor colors are `L,M` in
either order is

```text
c_k=2(2k-2)(k-1)/[(3k-3)(3k-4)].                     (4.5)
```

Conditional on this cross-color event, the two chords are independent with
laws `nu_(2k-1)` and `nu_k`.  There are `k-1` allowed boundary chords `f`,
each of weight `w_k(1)`.  In the cyclic order of `L`, put

```text
r=j-i-k.
```

For `r=1,...,k-1`, the smaller local split is `r` and there are `r` choices;
for `r=k`, the smaller split is `k-1` and there are `k-1` choices.  Thus the
allowed long-chord probability is

```text
L_k=sum_(s=1)^(k-2)s w_(2k-1)(s)
    +2(k-1)w_(2k-1)(k-1).                             (4.6)
```

Multiplying (4.5), `(k-1)w_k(1)`, and (4.6) gives exactly (3.3).  This proves
the second inequality in (3.2).

### 4.3 Conditioned-Borel asymptotics

Put

```text
b_s=e^(-s)tau(s).
```

This is the critical Borel law.  For odd `d` and
`1<=s<d/2`, the Borel--Tanner convolution identity gives

```text
d w_d(s)=b_s b_(d-s)/[(1-1/d)b_d].                    (4.7)
```

The left side is the probability that the smaller fragment of a `nu_d`
chord has size `s`: there are exactly `d` such chords.

Stirling's formula gives

```text
b_s~(2pi)^(-1/2)s^(-3/2).                             (4.8)
```

Taking `d=2k-1`, (4.7)--(4.8) and a standard dominated Riemann-sum argument
give

```text
sqrt(d) sum_(s=1)^(k-2) s w_d(s)
 -> (2pi)^(-1/2) integral_0^(1/2)
       x^(-1/2)(1-x)^(-3/2) dx
  =sqrt(2/pi).                                        (4.9)
```

The omitted central term in (4.6) is `O(k^(-3/2))`.  Since `d/k->2`,

```text
sqrt(k)L_k -> 1/sqrt(pi).                             (4.10)
```

Similarly, `(k-1)w_k(1)->b_1=e^(-1)`, while `c_k->4/9`.
Equations (4.5), (4.6), and (4.10) prove (3.4).

For a fully explicit bound, the smaller-fragment distribution in (4.7)
dominates `b_s`, and the elementary Stirling upper bound

```text
s!<=e sqrt(s)(s/e)^s
```

implies `b_s>=e^(-1)s^(-3/2)`.  Therefore

```text
L_k >= (2k-1)^(-1) sum_(s=1)^(k-2) s b_s
    >=1/[4e sqrt(k)].                                 (4.11)
```

Also `(k-1)w_k(1)>=2/(3e)` and `c_k>=4/9`.  Their product is (3.5).
Finally, total variation dominates the difference on the invariant event
`F_k`; (3.2) proves (3.6).  QED.

## 5. Exact remaining two-step lemma

Write, on quotient states,

```text
eta_k=bar K(B_k,.)-bar K(A_k,.).
```

Then the requested family difference is exactly

```text
bar K^2(B_k,.)-bar K^2(A_k,.)=eta_k bar K.             (5.1)
```

Let `rho_k=1_(F_k)eta_k`; it is a positive measure of mass at least `p_k`,
and put `xi_k=eta_k-rho_k`.  The balanced-family instance of the first
unproved step is the signed estimate

```text
(1/2)||rho_k bar K+xi_k bar K||_1 <= C/k^2.           (5.2)
```

The two summands in (5.2) cannot be bounded separately at the target scale:
`rho_k` already has mass `Omega(k^-1/2)`.  Equation (5.2) must pair its image
with the complementary `I3,IS,IN,X` terms before taking absolute values.
For a general `Lambda_n` edge, the exact unresolved lemma remains

```text
TV(bar K_n^2(alpha,.),bar K_n^2(beta,.))<=C/n^2.      (5.3)
```

Equivalently, after expanding (2.1) twice, the absolute value must remain
outside the signed sum over all sixteen ordered schema pairs.

A stronger sufficient target suggested by finite data is the coordinatewise
bound

```text
|bar K^2(alpha,T)-bar K^2(beta,T)|<=C/n^5             (5.4)
```

for every quotient target `T`: there are `O(n^3)` quotient states, so (5.4)
implies (5.3).  This is only a proposed analytic target, not a theorem.

## 6. Dependency and claim ledger

- **Proved input (M73):** the exact kernel, quotient reversibility, the four
  residual-forest schemas, and the conditioned-Borel first-edge identity.
- **Proved input (M80):** `diam(Lambda_n)<=4`.  It is used only to explain
  the now-refuted one-step Dobrushin shortcut.
- **Proved here:** adjacency of `A_k,B_k`; the invariant event obstruction;
  the exact mass (3.3); its asymptotic (3.4); and the explicit lower bound
  (3.5).
- **Refuted here:** a uniform `O(1/n)` bound on one-step influence along
  strict endpoint-sharing edges.
- **Finite only:** all displayed kernel TV values, transport solutions, and
  per-target discrepancy scaling.
- **Unresolved:** the two-step bound (5.3), a signed Abel/cancellation formula
  proving (5.2), and the sharp H0 consequence that depends on them.

The coordinator's correction is controlling: neither a polynomial two-step
minorization nor a weaker `O(log n/n^2)` trace-two estimate closes the frozen
M16 accumulation.  No such fallback is claimed here.

## 7. Strongest self-attack and exceptional cases

1. Proposition 3.1 is a one-step lower bound, not an asymptotic refutation of
   the assigned two-step inequality.  The main verdict therefore remains
   inconclusive.
2. The family exists only for the infinite subsequence `n=3k` with odd `k`.
   That is sufficient to refute a universal one-step `A/n` bound, but says
   nothing adverse about other odd ranks or the two-step claim.
3. The smallest family member is `n=9`.  The assigned `n=7` case is not part
   of the asymptotic construction and remains an exact finite case.
4. The quotient issue is essential.  The proof uses the cyclic-invariant
   residual-size event `F_k`; a phase-specific raw event would not by itself
   lower-bound quotient TV.
5. The Riemann-sum limit proves only the selected cross-schema mass.  It does
   not assert an asymptotic formula for the full one-step TV, whose finite
   constant is larger.
6. The earlier polynomial-minorization exploration is auxiliary and is not
   used in any conclusion.  Even if fully audited, it would not imply
   `kappa_+=O(1/n)`.

Boundary checks relevant here are: `k=1` would give `n=3` and is excluded;
`k` must be odd because `n` is odd; and `k=3` satisfies the exact formula and
the explicit bound.  The identity-bridge cases `m=0,2` and `N=2` are outside
this long-cycle product-coordinate model.

## 8. Finite certificates, reproduction, and artifacts

All computation in this section is **finite**.  The proof of (3.4)--(3.6) is
separate and analytic.

The exact rational certificate was run as

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-17/\
mission-M83-endpoint-sharing-influence/balanced_tail_certificate.py \
  --k 3 5 7 9 11 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-17/\
mission-M83-endpoint-sharing-influence/balanced_tail_exact_n33.json
```

At `n=9,15,21,27,33`, direct completion enumeration agrees exactly with
(3.3), assigns zero selected mass to `A_k`, and verifies that every selected
target is in `F_k`.  The first three exact values are

```text
k=3:  832/5625,
k=5:  1333643264/19729747125,
k=7:  24175662657910272/512054275623857603.
```

The focused floating family diagnostic through `n=51` gives

```text
n                 9       15       21       33       51
one-step TV   .56818   .37029   .29387   .22286   .17503
sqrt(n) TV    1.7045   1.4341   1.3467   1.2802   1.2500
```

The corresponding two-step family values at `n=9,15,21` are approximately
`.090461,.025045,.012698`, with `n^2` multiples `7.327,5.635,5.600`.
These values support but do not prove (5.2).

Primary artifacts are:

- `balanced_tail_certificate.py` and `balanced_tail_exact_n33.json`: exact
  formula certificate;
- `balanced_one_step_family.py` and its JSON outputs: focused finite family;
- `balanced_two_step_layers.py` and `balanced_two_step_layers_n21.json`:
  signed boundary/complement cancellation;
- `influence_diagnostic.py`: exhaustive strict-edge checks at small ranks;
- `transport_diagnostic.py` and `optimal_transport_diagnostic.py`: finite
  signed-transport tests;
- `plan.md` and `checkpoint.md`: scope and halfway/final checkpoints.

Environment: repository base commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, NumPy
`1.26.4` where used, deterministic calculations, and no random seed.

## 9. Verdict

**Overall verdict: inconclusive on the assigned two-step lemma; promote the
balanced one-step lower bound and reject the one-step Dobrushin shortcut.**

The durable advance is an exact asymptotic obstruction, not another finite
warning: strict endpoint-sharing one-step influence can be
`Omega(n^-1/2)`.  Any proof of the desired `O(n^-2)` two-step influence must
therefore exploit signed cancellation after the second kernel, across the
full sixteen posterior schemas.  The first unproved standalone statement is
exactly (5.3), with (5.2) its sharply exposed balanced-tail subproblem.
