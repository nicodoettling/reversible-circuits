# M40 halfway checkpoint: cut multiplicity removes the logarithmic loss

## Scoped theorem now proved modulo the frozen M37 bookkeeping

Use `(pq)(x)=p(q(x))`, let `m=4N^3+4`, and let `V^(a)` be the literal
original-`K` graph neighborhood of the disconnected identity words.  The new
core lemma below closes the only M37 step that used
`a<=N^2/[100 log(N+1)]`.  Rechecking the remaining displayed inequalities
gives, for `N>=10^6` and every `1<=a<=floor(N^2/100)`,

```text
pi(V^(a))<=exp(-4N^2),
Phi_pm^K(V^(a))>=N^(-25).                              (C.1)
```

This is a genuine quadratic-radius anti-bottleneck theorem.  It is not a
global gap proof and does not control larger shell radii.

The omitted radius `a=0` satisfies the same displayed bounds: its mass is at
most that of `V^(1)`, and the frozen M25 theorem gives
`Phi_pm^K(U)>=1/(32N^3)>=N^-25`.

## 1. Deterministic repair-code condition

Put `d=N-1`, `E=binom(d,2)`, and fix the isolate subgroup
`H=Stab(N)=S_d`.  For an internal transposition word `u` and a nontrivial
cut `S|([d]\S)`, let `X_S(u)` count occurrences of factors crossing the cut.
Call `u` *`a`-cut-robust* when

```text
X_S(u)>5a for every nontrivial S subset [d].           (C.2)
```

Deleting any union of at most `a` update windows removes at most `5a`
coordinates of `u`.  Hence every cut retains a crossing factor, so the
support graph of the undeleted word is connected.  This implication is
deterministic and does not union-bound deletion patterns.

## 2. Arbitrary-endpoint abundance

Let

```text
t>=4N^3-5a,                   1<=a<=N^2/100.           (C.3)
```

For every parity-compatible `h in S_d`, at least

```text
(1/2)E^t/d!                                             (C.4)
```

length-`t` factorizations of `h` are `a`-cut-robust.

The inherited arbitrary-endpoint Fourier estimate gives at least `E^t/d!`
total factorizations.  For a fixed cut with smaller side `s`, a uniformly
chosen internal word has

```text
X_S ~ Bin(t,p_S),        p_S=s(d-s)/E>=2/d,
mu_S>=2t/d.                                             (C.5)
```

Now `5a<=mu_S/2`, so the elementary lower-tail Chernoff inequality gives

```text
Pr[X_S<=5a]<=exp(-mu_S/8)<=exp[-t/(4d)].               (C.6)
```

There are fewer than `2^d` cuts.  Therefore all bad words, without an
endpoint restriction, number at most

```text
2^d E^t exp[-t/(4d)].                                  (C.7)
```

After division by the endpoint lower bound, the lost fraction is at most

```text
d! 2^d exp[-t/(4d)]
 <=exp{N log N+N-0.9975N^2}
 <=exp(-0.98N^2)<1/2,                                 (C.8)
```

where `t>=4N^3-N^2/20>=3.99N^3`.  Subtraction proves (C.4).  This explicitly
pays the `d!` endpoint-conditioning loss.

## 3. Substitution into the primitive-source proof

For fixed primitive blocks and the four reserved internal factors used by
the final `H_5` surgery, the remaining core length is

```text
t_0=m-L-4>=4N^3-5a.                                   (C.9)
```

Its requested endpoint is parity-compatible because `m` is even and every
fixed factor is a transposition.  Thus (C.4) replaces M37's former
window-choice union bound and gives the same source factor
`(1/2)E^(m-L)/d!`.

In a hypothetical path of at most `a` updates to the surgery target, the
union of all windows removes at most `5a` core coordinates.  Condition (C.2)
forces the remaining `[d]` support to be connected.  Consequently the only
possible initial disconnection cut is `{N}|[d]`.  Primitive-block rigidity
then shows that the extended rightmost block needs one extra update, exactly
as in M37.

## 4. Quadratic-scale constant audit

All other M37 losses remain constant or polynomial:

```text
[M/(M-1)]^(4a) <= exp(4a/(M-1)) < exp(0.081)<2,
C=ceil(20sqrt(a))<=2N+1,
16aC/m<0.081,
theta_->60,                 theta<=80,
4a log(5/2)<0.037N^2.                                (C.10)
```

The isolate source/outer comparison therefore still gives
`|V^(a)|<=N^5 B_a`; every non-isolate cut retains exponential suppression.
The direct outer count remains below `exp(-4N^2)|Omega|`.  A specified
same-product `H_5` surgery has probability at least
`1/[6(m-4)M^4]`, yielding (C.1) after retaining only these nonnegative
`Q_5` contributions.

## 5. Current frontier

The first remaining shell proposition is now:

> **POST-QUADRATIC SHELL ACTION.**  Determine whether some universal
> `kappa'>1/100` controls every proper `V^(a)` beyond `a=N^2/100`, or find the
> first radius where the primitive-isolate boundary construction loses its
> entropy/action advantage.

The present proof has ample cut-connectivity margin; its chosen `1/100`
constant is instead a conservative simultaneous choice for the primitive
entropy and coefficient comparisons.  No conductance monotonicity is used.
