# M45 final report: M43 accepted and later literal shells rejected as a bottleneck

## Referee decision on the frozen M43 bundle

**ACCEPT.**  There are no numbered objections and no corrections to the
frozen statement.  The acceptance is for the scoped theorem

```text
N>=10^12, m=4N^3+4, 0<=a<=floor(m/10^8)
  => pi(V^(a))<=exp(-4N^2), Phi_pm^K(V^(a))>=N^(-25),
```

subject only to M43's explicitly listed inherited M25/M31/M37/M40/M42
dependencies at their frozen scopes.  It is not acceptance of Terminal A or
Terminal B.

The numbered referee checks are:

1. The overlap hulls must be processed from the globally first uncovered
   crossing.  In that order, the incoming inverse-prefix state is `z`, the
   trimmed hull has product in `Stab(z)`, and its last crossing is a return.
   The untouched factors between hulls are internal, so induction restarts
   from `z`.  This proves that the hulls group consecutive whole primitive
   excursions; M43 does not make the invalid out-of-order inference.
2. If `q(L)=ceil((L-1)/4)`, then an overlap component of `u` windows has
   span at most `4u+1`, and
   `q(L_1+g+L_2)>=q(L_1)+q(L_2)-1_{g<=2}`.  Thus the exact lower witness is
   `p=Q-h<=a`.
3. Once all primitive words and gap lengths are fixed, every primitive
   product lies in `H=Stab(z)`.  Centrality of the internal transposition
   class sum combines all interspersed gaps into one parity-compatible
   coefficient of `C^G`; only one endpoint factorial is paid.
4. The primitive count is `d(M-1)^(l-2)`.  Relative to `E^l`, a budget-`q`
   primitive has weight `y A^(4(q-1))D_A`.  The exact binomial product is
   `binom(p-1,k-1)(p)^(over h)/h!`, so short returns sum to
   `(1-3yD_A)^(-p)`.  Extending the upper sum to infeasible `h` is in the
   safe direction.
5. The two hard-rod layout coefficients are correct: after subtracting
   three from each of the `k-1` long gaps, the outer layout count is
   `binom(m-L-R-2k+3,k)`; reserving four trailing factors gives clean-source
   count `binom(m-L-2k-1,k)`.
6. Prefix return times uniquely recover every clean primitive interval.
   Its length recovers its budget and residue; the complement recovers all
   gap and core positions.  Thus the source encoding is injective.
7. M42's robust-core subtraction is uniform in all deterministic kicks and
   every compatible endpoint.  It does not condition each gap separately.
8. With `h=b_1b_2b_3b_4`, the surgery preserves ordered product because
   `t h=h(h^-1 t h)`.  In inverse-prefix coordinates the four internal
   factors cannot return the state to `z`, and the conjugated last
   transposition returns it exactly; the final primitive budget rises by one.
9. The specified outcome has probability at least
   `1/[6(m-4)M^4]`: one half for the nonlazy part, one third for `r=5`, one
   over `m-4` for the scan, and at least `M^-4` in the conditional fiber.
   Every omitted `Q_3,Q_4,Q_5` contribution is nonnegative.  M25 handles
   `a=0`, M42 overlaps the direct positive-radius range, and floors only
   shrink the asserted interval.

## 1. Exact red-team claim, quantifiers, conventions, and kernel

Use `(pq)(x)=p(q(x))`, evaluate an ordered word as `t_1...t_m`, and put

```text
N>=10^12,                  M=binom(N,2),
d=N-1,                     E=binom(d,2),
m=4N^3+4,                  a_**=floor(m/10^4),
U={w in Omega(N,m): the support graph of w is disconnected},
V^(0)=U,
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.
```

The target is uniform on `Omega(N,m)`, and the exact chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)]
       sum_{i=1}^{m-r+1} H_{i,r},
```

where `H_{i,r}` is uniform on the length-`r` transposition words with the
same ordered product as the current block.

**Later-shell anti-bottleneck theorem (proved).**  Simultaneously for every
integer `0<=a<=a_**`,

```text
pi_{N,m}(V^(a))<=exp(-4N^2)<1/2,
Phi_pm^K(V^(a))>=N^(-25).                             (1.1)
```

This disproves the candidate that a literal disconnected-macro shell at a
radius between `m/10^8` and `m/10^4` supplies Terminal B.  It remains a
scoped anti-bottleneck theorem, not a global gap theorem.

## 2. Full argument

The exact decomposition, path lower witness, primitive enumeration, and
hard-rod formulas are the accepted M43 equations (2.1)--(2.19).  Only their
constant range changes.  The checks below verify every inequality needed for
the larger range rather than extrapolating from M43's stated constant.

### 2.1 Canonical segmentation and one endpoint coefficient

Fix an isolate `z` and `H=Stab(z)`.  For
`X_j=(t_1...t_j)^(-1)(z)`, decompose the crossings into unique primitive
excursions of lengths `l_j>=2`.  Define

```text
q_j=ceil((l_j-1)/4), Q=sum_j q_j,
h=#{short inter-excursion gaps of length at most two},
k=c-h, p=Q-h.
```

The accepted ordered-hull argument gives `p<=a` for every word at graph
distance at most `a` from the `H`-internal macro.  A primitive length `l`
has exactly `d(M-1)^(l-2)` factor words.  After primitive words and gap
lengths are fixed, centrality of the `H`-transposition class sum turns all
internal positions into one arbitrary-endpoint coefficient.  Since
`G>=m-5a`, the inherited dense trace bounds apply throughout the new range:

```text
G>=m(1-5/10^4)-4>3.997N^3.                            (2.1)
```

Parity compatibility is automatic because `m` is even and `G=m-L`.

### 2.2 Close returns remain a constant correction

Retain

```text
A=(N+1)/(N-1), D_A=1+A+A^2+A^3,
y=d/E^2=4/[(N-1)(N-2)^2].
```

For `N>=10^12`, elementary expansion gives

```text
D_A<5, y<5/N^3, 3yD_A<75/N^3,
m<4.001N^3.
```

Thus, for every `p<=a<=m/10^4`,

```text
(3yD_A)p<0.031,
(1-3yD_A)^(-p)
 <=exp(2(3yD_A)p)<exp(0.062)<2.                       (2.2)
```

The exact negative-binomial resummation therefore incurs the same factor
two used in the frozen proof.

### 2.3 Hard-rod comparison and cluster tail

Let `C=ceil(20sqrt(a))`.  For `k<=C` and
`n=m-4a-3k-1`, the new range and threshold imply

```text
k<0.401N^(3/2),             n-k>3.99N^3,
4k/(n-k)<1/N,
k(3k+4)/(n-k)<1.                                      (2.3)
```

For `p=a-r`, the exact source and outer coefficients

```text
W_(a,k)=binom(a-1,k-1)y^k A^(4(a-k))D_A^k
          binom(m-4a-3k-1,k),
U_(p,k)=binom(p-1,k-1)y^k A^(4(p-k))D_A^k
          binom(m-4p+3,k)
```

therefore satisfy, exactly as in M43,

```text
U_(a-r,k)/W_(a,k)<=e exp(-3r/N),
sum_{p=k}^a U_(p,k)<=2N W_(a,k).                      (2.4)
```

Here `log A>=1/N`; the `4r` part of the layout ratio costs at most
`r/N`, while `A^(-4r)` supplies at least `exp(-4r/N)`.

The exact quantity controlling the large-`k` ratio has ample slack.  For
`N>=10^12`,

```text
m y<16.000000001, D_A<4.000000001,
m yD_A/A^4<65<80.
```

Consequently

```text
U_(p,k+1)/U_(p,k)
 <=80a/[k(k+1)]<=1/5                 for k>C.         (2.5)
```

The tail costs at most `5/4`.  The no-crossing term is absorbed by the
`k=1` source term (indeed its non-`A` factor is already greater than one).
Including the endpoint upper/lower constants and the close-return factor,
the accepted comparison remains

```text
O_z(a)<=41N B_a,                                      (2.6)
```

where

```text
B_a=(1/2)(E^m/d!) sum_{k=1}^C W_(a,k).
```

### 2.4 Endpoint-uniform robust sources

After deleting the primitive positions and four reserved factors, the
internal core length satisfies (2.1), while its allowed away fraction is

```text
epsilon=10a/(m-5a-4)<0.001002.                        (2.7)
```

Its binary entropy is below `0.008`, stronger than the `0.06` bound in
M42.  The kicked Johnson-walk calculation therefore still gives
unconditioned failure at most `exp(-0.78N^2)` and, after the one endpoint
factor, all subset cuts, and residue classes, endpoint-uniform failure below
`exp(-0.75N^2)<1/2`.  Thus `B_a` remains an injective lower count of sources
robust against every alternative disconnection cut.

### 2.5 Non-isolate cuts

Use the inherited exact shrunken-cluster inequality for a cut with smaller
side `2<=s<=N/2`.  For `s<=N/4`, its logarithm relative to the isolate
baseline is at most

```text
2s log N-5.6(s-1)N^2+20as/N
 +2sqrt(800sa).                                       (2.8)
```

In the new range,

```text
20as/N<0.0081sN^2.
```

The square-root term is maximized relative to `(s-1)N^2` at `s=2` and is
less than `1.7N^(3/2)`.  At `N>=10^12`, (2.8) is below `-5.5N^2` for
`s=2` and decreases on the needed exponential scale for larger `s`.

For `s>=N/4`, the inherited internal trace suppression is `0.8N^3`.
The active term is below `0.0041N^3`, the Bessel term is below `0.81N^2`,
and cut entropy is lower order.  Hence the summed non-isolate contribution
is still less than `B_a`.  After union over isolates and cuts,

```text
|V^(a)|<=N^3 B_a.                                     (2.9)
```

### 2.6 Global mass orientation

An explicit upper bound on the source coefficient follows from
`theta=m yD_A/A^4<80`:

```text
sum_k W_(a,k)
 <=A^(4a) 80 exp(2sqrt(80a)).                         (2.10)
```

Using `|Omega(N,m)|>=2M^m/N!`, `N!/d!=N`, and
`E/M=(N-2)/N`, equations (2.9)--(2.10) give

```text
log pi(V^(a))
 <=4log N +m log(1-2/N)+4a log A
    +log 80+2sqrt(80a).
```

Here

```text
m log(1-2/N)<=-8N^2,
4a log A<0.0033N^2,
2sqrt(80a)<0.36N^(3/2)<4x10^(-7)N^2.
```

Therefore `pi(V^(a))<=exp(-4N^2)<1/2` with enormous slack.

### 2.7 Full original-kernel boundary flow

Every robust clean source has an exact length-`a` zipper path from the
isolate macro.  Moving its final return crossing through the four reserved
internal factors is one genuine same-product `H_5` outcome.  Canonical
segmentation raises the isolate cost to `a+1`, and the endpoint-uniform
prefix certificate rules out every other cut at distance at most `a`.

The outcome probability is at least

```text
p_exit=1/[6(m-4)M^4].                                 (2.11)
```

All other terms in `Q_3+Q_4+Q_5` are nonnegative.  From (2.9), the source
fraction is at least `N^-3`; hence

```text
Phi_pm^K(V^(a))
 >=N^(-3)/[6(m-4)M^4]>=N^(-25).                      (2.12)
```

For `a=0` use the inherited M25 theorem.  Equivalently one may splice M42
through `floor(N^2 log log N/100)`; at `N>=10^12` this interval overlaps the
direct range and lies strictly below `a_**`.  Every displayed binomial top
is positive in the new range, and taking floors only strengthens the bounds.

## 3. Probability, runtime, path length, and congestion accounting

- Close-return overhead is below two.
- Cumulative depth costs at most `2N`; the large-cluster tail costs at most
  `5/4`.
- Endpoint-conditioned robust-core loss is below `exp(-0.75N^2)` uniformly
  in the skeleton, layout, deterministic kicks, subset cut, and compatible
  endpoint.
- The robust source fraction of the full shell is at least `N^-3`.
- Each source has a constructive length-`a` path of genuine local zipper
  updates and one specified `H_5` exit of probability at least
  `1/[6(m-4)M^4]`.
- There is no comparison-flow congestion.  Canonical returns and source
  decoding take `O(m)` permutation-state updates; the maintained-product
  zipper takes the inherited `O(aN)` time.  Exact block sampling for fixed
  `r<=5` is polynomial in `N,m`.

## 4. Dependencies and status labels

1. **Independently accepted here:** the complete frozen M43 new-core proof
   and its exact use of the inherited dependencies.
2. **Proved here:** every revised constant needed to extend the shell radius
   from `m/10^8` to `m/10^4`.
3. **Proved in frozen M43:** canonical primitive segmentation, close-return
   resummation, exact hard-rod coefficients, and source/shell comparison.
4. **Proved in inherited M37/M40:** primitive zipper, clean rigidity,
   shrunken-cluster cut encoding, and final `H_5` surgery.
5. **Proved in inherited M42:** prefix-hull witness and endpoint-uniform
   kicked-core robustness.
6. **Proved in inherited M12/M25/M31:** dense endpoint bounds, parity return
   lower bound, and radius-zero mass/flow.
7. **Cited or empirical dependencies:** none.

## 5. First unproved standalone proposition

> **NEAR-QUARTER LITERAL-SHELL ACTION.**  For `m=4N^3+4`, determine the
> stationary orientation and full-`K` boundary flow of `V^(a)` uniformly in
> a regime with `a/m` tending to `1/4` from below (or first locate the exact
> quartile radius if lower-order coefficient entropy shifts that scale).
> Either prove inverse-polynomial conductance for every
> smaller-side shell in that interval or exhibit an explicit infinite
> sequence with superpolynomial conductance decay.

The accepted renewal factor stays constant for every fixed `a/m<1/4`, and
the hard-rod depth comparison stays polynomial.  The named obstruction is
that the internal core and the isolate large-deviation exponent both vanish
near `m/4`; the current endpoint-uniform alternative-cut certificate then no
longer has a dense core.  This is a narrower issue than the old intermediate-
return loss.

## 6. Strongest self-attack

This result only rejects one larger family of literal Terminal-B candidates.
Conductance is not monotone in shell radius.  The proof gives no information
at the near-`m/4` mass transition, for unrelated dense full-support cuts, or
for the global spectral gap.  Its larger constant is obtained from slack in
the accepted M43 mechanism, so it is not a new paradigm.

The most likely way the extension could fail would be if an inherited
non-isolate or endpoint-uniform inequality had an unstated dependence on
`a<=N^2 log log N/100`.  The frozen formulas used here expose their entire
dependence through `G=m-5a`, `epsilon=10a/G`, `20as/N`, and
`2sqrt(800sa)`; substituting `a<=m/10^4` leaves the explicit slack shown
above.  No other radius hypothesis is used.

## 7. Calibration

- Odd `m`: `Omega(N,m)` is empty; no claim.
- `m=0` and `N=2` with even `m`: singleton regimes, outside the theorem.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`: the theorem's threshold does not
  include them; the exact counts `27`, `120`, and `3936` and the whole-word
  `H_4` update at `m=4` remain intact.  No finite extrapolation is used.
- Near-minimal doubled-tree words need not have a dense core; this theorem is
  only for `m=4N^3+4`.
- The proof uses ordered products and inverse-prefix returns, not a graph-only
  edge-shift model or degree/multiplicity parity.
- The exit is a real length-five heat-bath outcome.  No length-two local
  simulation or canonical-hub routing is asserted.

## 8. Artifacts and reproduction commands

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation or stochastic experiment was used.  Reproduce by checking
the frozen M43 equations (2.1)--(2.32), then substitute
`a<=floor(m/10^4)` in this report's (2.1)--(2.12).  Read-only commands used:

```text
sed -n '1,519p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M43-superquadratic-shell/report.md
sed -n '39,260p' \
  experiments/20260811-polynomial-mixing-resolution/cycle-09/mission-M42-linear-shell-mechanism/report.md
```

Repository base commit recorded by the run: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

This verdict is for the scoped later-shell anti-bottleneck theorem and the
ACCEPT decision on frozen M43.  It is not Terminal A or Terminal B.
