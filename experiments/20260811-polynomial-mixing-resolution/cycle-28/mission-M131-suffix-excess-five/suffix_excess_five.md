# M131 suffix-excess-five conditional reduction

Date: 2026-08-13 UTC.

## 1. Scope, target, and accepted recurrence

This note concerns only the auxiliary full **nonlazy stationary-flow
parking-degree projection** in the minimal-long-cycle sector. It is not a
mixing theorem for the original lazy `{3,4,5}` identity-word heat-bath chain.
Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.

Use the accepted all-rank finite-DAG recurrence

```text
H=A_0+QH,  Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),  j=1,...,k.
```

Only `j=0` and targets of auxiliary rank below two are killed. M109/M114,
M115/M116, and M117/M121 prove right-heavy contraction for suffix excess
`L<=4`, the universal all-deficit `L=0` theorem, and the arbitrary-deficit
`L=1,2` envelopes used below.

The target here is

```text
H(s,K,K-1,s-5)<=q(1-q),  s>=6, K>=1,
q=w_6 w_(s-5)/w_(s+1).
```

The conclusion obtained is conditional on one standalone scalar lemma about
canonical-basin density. No auxiliary gap, ROOT-MEAN LIFT, original-chain
gap, polynomial mixing, or project terminal is inferred.

## 2. Root support, basins, and all live groups

Write `b_n=w_n/w_(n+1)`, and put

```text
(r,u,v,y,x,g)=(b_s,b_(s-1),...,b_(s-5)),
z=1/(K+1), q=w_6 ruvyxg.
```

For `h=0,...,5`, the supported roots whose last part is `B+h` are

```text
(P,B+h), where P ranges over every ordered composition of 5-h.
```

There are therefore

```text
sum_(h=0)^4 2^(4-h)+1=32
```

supported ordered compositions. Their contextual means, in the notation

```text
delta_k(z)=k!z^k/prod_(a=1)^(k-1)(1+az),
c_h=w_h prod_(bottom h Cayley ratios),
```

are

```text
len(P)+1 times delta_len(P)(z),        h=0,
c_h[1-delta_(len(P)+1)(z)],            h>=1.
```

The exact stationary mass divided by `q` is

```text
prod_(a in P)w_a /
[(len(P)+1)! w_6 prod_(bottom h ratios)].
```

The mass-times-mean sum is one after division by `q`. Every nonempty prefix
has one canonical endpoint for each first-merge cut, giving exactly

```text
31
```

nominal exceptional canonical basins. Of these, 23 are active and eight begin
with `(1,1)` and are inactive. The envelope deliberately retains the latter
only in conservative upper-bound bookkeeping. Currents and capacities are
generated literally from the displayed mass/mean rows in `l5_exact.py`;
selected full tables are in `l5_exact.json`.

There are 16 positive `(k,t)` groups. Exactly 11 have `t>B` and send retained
deep mass:

```text
h=1: k=2,3,4,5
h=2: k=2,3,4
h=3: k=2,3
h=4: k=2
h=5: k=1.
```

For every group, every `j=1,...,k` is retained before aggregation. The child
has suffix excess `h-1` and deficit

```text
D'=k+1-j.
```

Thus right-heavy `j=k` children use the accepted `L<=4` theorem. Non-right-
heavy children have excess at most three and use the new recursive envelope
in Section 4.

At `s=6`, `B=1`. The nominal `h=1` children have local rank one and are
inactive. Their displayed terminal charge vanishes because the bottom Cayley
ratio is `b_1=1`. The literal recurrence retains exactly every other listed
rank, so this boundary needs no limiting convention.

## 3. Exact canonical-basin density and the standalone lemma

For a canonical endpoint `E=(A,c_2,...,c_k)`, let `B_E` be its first-prefix
refinement basin and put

```text
beta(A,k)=rho(B_E)/rho(E),
lambda(A,k)=beta(A,k)/k.
```

The accepted Cayley coefficient gives the exact identity

```text
lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!] (A)_p/A^p.       (3.1)
```

In particular, exact telescoping yields

```text
lambda(A,2)=A/(A+1).                               (3.2)
```

Comparing the coefficient of each `p` in (3.1) with its coefficient at
`k=2` gives, for `k>=2` and `p>=1`,

```text
(k-1)!(p+1)!/(p+k-1)! <=2/k.
```

Summing term by term and using (3.2) gives the universal sharpening

```text
lambda(A,k)<=2A/[k(A+1)]<=2/k.                    (3.3)
```

The exact all-basin coefficient at local rank `s` is

```text
C_s=sum_(all canonical endpoints E) degree(E)rho(E)lambda(E)^2

   =sum_(k=2)^s sum_(A=1)^(s-k+1)
      [w_A c(s-A,k-1)/(k!w_(s+1))]
      k lambda(A,k)^2.                             (3.4)
```

Inactive endpoints are included deliberately in (3.4). They contribute
nonnegative terms and therefore only enlarge the envelope; this convention
also makes the closed endpoint-degree marginal exact.

Here `c(n,p)=p n^(n-p-1)/(n-p)!`. The endpoint-degree marginal in (3.4) is
exactly

```text
sum_A w_A c(s-A,k-1)/(k!w_(s+1))
 =binom(s-1,k-1)s^(s-k)/(s+1)^(s-1).              (3.5)
```

Thus (3.4) is a one-dimensional Cayley-coefficient obligation, separate from
the `L=5` contextual recurrence.

> **Standalone scalar lemma C (unresolved).** For every `s>=100`,
> ```text
> C_s<=3/4.                                        (3.6)
> ```

The exact evaluation of (3.4) is `.7145417887...` at `s=100`. This is
falsification data only. No monotonicity or uniform tail proof of (3.6) is
claimed. For clarity, the tempting shortcut `2(3-e)<9/16` is false: the
factorial-tail estimate

```text
e<sum_(n=0)^6 1/n! + (1/7!)sum_(r>=0)8^(-r)
 =1957/720+1/4410 <87/32
```

instead gives `2(3-e)>9/16`. The weaker bound

```text
2(3-e)<17/30
```

is true because `e>sum_(n=0)^5 1/n!=163/60`; it is not by itself a proof of
Lemma C. Any future refinement of (3.3) must be inserted with its exact
parameter threshold and a complete aggregate argument.

## 4. New arbitrary-deficit suffix-excess-three envelope

Let an arbitrary reachable context have suffix excess `ell<=3`, Cayley-ratio
tuple `(b_S,...,b_B)`, `K+1=(1+az)/z`, and deficit `D=K-R`. Its exact
attachment law is

```text
nu_(a,D,k)(0)
 =(D)_k z^k/prod_(r=0)^(k-1)[1+(a+r)z],

nu_(a,D,k)(j)
 =binom(k,j)(D)_(k-j) z^(k-j)
  prod_(r=0)^(j-1)[1+(a-D+r)z]
  /prod_(r=0)^(k-1)[1+(a+r)z].                    (4.1)
```

The root support and canonical-basin recurrence are the same formulas as
Section 2 with `ell` in place of five and (4.1) in place of the fresh law.
Every child has parameters

```text
(a',D')=(a+k,D+k-j)
```

and suffix excess `h-1`. Recursing to the accepted universal terminal theorem
therefore defines an exact reset-plus-descendant envelope `F_ell`; no child
with `ell>2` is needed below the new `ell=3` case.

The generic code reproduces M115/M116's accepted arbitrary-deficit `L=1`
formula and M117/M121's accepted arbitrary-deficit `L=2` formula exactly.
It then defines the new `L=3` envelope from 8 supported rows, 7 exceptional
basins, and all 4 live groups. On all checked reachable contexts

```text
ell=1,2,3; ell+1<=S<=8; 2<=K<=8; 1<=R<K,
```

the exact full resolvent is at most `qF_ell`, with zero failures. The proof of
the envelope is structural: exact reset currents plus the already accepted
lower-excess envelopes, not finite extrapolation. The finite rows audit the
implementation and every normalization.

## 5. Refined `L=5` reset and descendant envelope

For an ordinary basin, its current is `-q rho(B_E)`, so its exact density
upper contribution after division by `q` is

```text
q degree(E)rho(E)lambda(E)^2.
```

Summing over all basins and replacing each exceptional ordinary term by its
exact current gives the refined root reset envelope

```text
R_5=q[C_s-q sum_(31 exceptional E)
             rho_supported(B_E)lambda(E)^2]
    +sum_(31 exceptional E) (theta_E/q)^2/(cap_E/q).   (5.1)
```

This is sharper than the inherited `beta<=degree` expression and retains
every exceptional nesting. The descendant term `D_5` sums all 11 live groups
and every attachment rank. Right-heavy children use accepted contraction;
the remaining children use Section 4. Thus

```text
H/q <= E_5:=R_5+D_5.                              (5.2)
```

The original inherited envelope is exactly refuted as a proof template:
at `(s,K)=(7,4096)` its normalized value is about `1.019485`, whereas the
exact `H/[q(1-q)]` is about `.402510`. This refutes only that loose envelope,
not the contraction target.

## 6. Exact scalar certificates and conditional theorem

Let

```text
Delta(z)=prod_(a=1)^5(1+az),
T_s(z)=Delta(z)^2[1-q-E_5(z)].                    (6.1)
```

With actual `C_s`, `T_s` has degree 12 in `z`. For every `s=6,...,99`, all
13 exact degree-12 Bernstein coefficients on `[0,1/2]` are positive. Across
all 1222 coefficients, the exact minimum is

```text
5307578203959502651/4736091661711441920000
```

at `s=7`.

For `s>=100`, all six Cayley ratios lie in

```text
[4/11,187/500].                                   (6.2)
```

For completeness, write `b_n=(n/(n+1))^(n-1)`. The function
`(x-1)log(1+1/x)` is increasing because
`log(1+1/x)>1/(x+1)>(x-1)/(x(x+1))`; hence the `b_n` decrease. Also
`log(1+1/n)<1/n`, so `b_n>1/e`. The elementary series estimate

```text
e=5/2+sum_(n>=3)1/n! <5/2+(1/6)sum_(r>=0)3^(-r)=11/4
```

gives `1/e>4/11`. The smallest ratio index is at least 95, and the exact
integer comparison

```text
500*95^94 < 187*96^94
```

gives `b_95=(95/96)^94<187/500`, proving the upper bound. Replacing every
path height by one enlarges the envelope. Replacing `C_s` by `3/4` does
likewise under Lemma C.

After these replacements, (6.1) has multidegree

```text
(1,1,2,2,2,2,12)
```

in the six ratios and `z`. All

```text
2*2*3^4*13=4212
```

exact tensor Bernstein coefficients on (6.2) times `[0,1/2]` are positive.
The exact minimum is

```text
4360847276079323/50118750000000000000
```

at tensor index `(1,1,2,2,2,0,0)`. An exact off-grid tensor identity passes.

Consequently:

> **Conditional `L=5` theorem.** If standalone Lemma C holds, then for every
> `s>=6,K>=1`,
> ```text
> H(s,K,K-1,s-5)<=q(1-q).
> ```

The proof is unconditional for `6<=s<=99`. The universal `s>=100` inference
is conditional only on (3.6).

## 7. Literal checks and limitations

The standalone exact implementation checks:

- all 32 support rows and the mean identity;
- all 31 nominal exceptional basins (23 active) and 11 live groups;
- every retained rank and resulting child deficit;
- exact full resolvents and refined envelopes for
  `6<=s<=12`, `K in {1,2,5,64,4096}`;
- arbitrary-deficit `L=1,2,3` recursive envelopes;
- all 1222 finite and 4212 conditional-tail Bernstein coefficients; and
- the `s=6` inactive-child boundary.

There are zero failures. The largest tested exact resolvent ratio is about
`.67196`; the largest refined envelope ratio is about `.99862`. These finite
values audit formulas only. Lemma C remains the first unproved step.

No generic basin-frame/Bessel argument is used. The M123/M128 unrestricted,
centered, and bounded-event frame obstructions therefore do not enter this
reduction. No one-step or two-layer defect sign is assumed.
