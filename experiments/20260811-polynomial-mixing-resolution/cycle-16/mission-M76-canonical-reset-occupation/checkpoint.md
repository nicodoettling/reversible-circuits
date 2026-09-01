# M76 halfway checkpoint: strict phase descent, renewal frontier

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Scope and status

This checkpoint concerns only the nonlazy stationary-flow parking projection
`Pbar_r` in the minimal long-cycle sector. It is not a result for the identity
bridge chain `K`. The marked recurrence uses `G_s=R_s/alpha_s`,
`alpha_s=2/[3s(s-1)]`, so each canonical reset coefficient is
`theta_e^2/[Q_G(e)q_x]` and each deep coefficient is M65's exact stationary
negative-hypergeometric weight.

The reset-to-reset occupation theorem is still unresolved. The useful proved
structure and the eliminated false potentials are recorded below.

## H-001: strict descending coordinate (proved)

Put `u=K-R` and

```text
P(x)=s+u.
```

For a deep child `(t-1,K+k,R+j,B)`, write `n=s-t` for the prefix mass.
Then

```text
P(x)-P(y)=s-t+1-k+j=n-k+j+1>=j>=1,
```

because a prefix with `k-1` positive parts has `n>=k-1`. A canonical
first-boundary reset child is `(A+c_2-1,k-1,k-2,c_2)`, hence has
`P(y)=A+c_2<=s<P(x)`. Thus every child strictly lowers `P`, including
history-colliding children.

Reachability from canonical resets is also exact. Every reset has `u=1`.
Starting from `(K,R)=(1,0)`, a deep step with `k=K'-1,j=R'` reaches any
`K'>R'>=1`; conversely every deep step has `j>=1`, so no context with
`R=0,K>1` is reachable. The closure is therefore

```text
{(1,0)} union {(K,R): K>R>=1}.                     (H.1)
```

## H-002: one-step polynomial phase potentials are false (proved)

Fix any exponent `d`. Take

```text
x_(s,K)=(s,K,K-1,s-1),       K->infinity.
```

The unary composition gives a deep child with exact coefficient `K/(K+1)`,
`P_child=s`, and suffix excess plus one `ell_child=1`. The canonical
degree-two edge `(s-1,1)->(s)` has basin `Z={last part=1}` and reset child
`(s-1,1,0,1)`. On `Z`, the parent contextual mean is zero, so its normalized
reset coefficient is exactly

```text
p_s^2,        p_s=rho_s(last part=1).
```

Moreover

```text
p_s>=rho_s((s-1,1))=w_(s-1)/(2w_(s+1))->e^(-2)/2.
```

Both children have `P=s`. Hence for `V=P^d u`, their combined ratio tends
to at least `1+e^(-4)/4>1`. For
`V=P^d u[1+log(s-B+1)]`, the same two children give

```text
(s/(s+1))^d [K/(K+1)+p_s^2(1+log(s-1))]/(1+log 2),
```

which diverges. Thus every fixed one-step power, with or without this
suffix logarithm, is refuted. This does not refute reset-to-reset renewal:
the reset child has `B=1`, and its later deep excursion can compensate.

## H-003: exact reset renewal (finite falsifier)

Split the canonical recurrence as `D+J_can` and eliminate pure-deep
excursions:

```text
b=(I-D)^(-1)a_can,       K_reset=(I-D)^(-1)J_can.  (H.2)
```

`reset_renewal_probe.py` computes (H.2) exactly on the rank DAG. For every
right-heavy seed scanned through rank 14 and
`K=1,...,16,64,128,256,1024,4096`, the largest reset row sums are

```text
s       3      4      5      6      7      8      9     10
max   .160   .279   .356   .444   .497   .538   .578   .609

s      11     12     13     14
max   .633   .656   .675   .691.
```

Every maximum occurs at `(K,R)=(1,0)`. This strongly suggests, but does not
prove, the substochastic renewal statement

```text
sum_y K_reset(x,y)<=1                              (H.3)
```

for every right-heavy seed. If (H.3) holds, strict reset-rank descent gives
at most `r` reset generations; M71's canonical base bound and exact pure-D
suffix contraction then give polynomial separated marked occupation.

## H-004: one-dimensional seed reset formula (proved and normalized)

For the degree-two reset edge from local rank `s` with seed `(K,R)=(1,0)`,
let

```text
A_a=[z^a](e^T-1)/T,
C_a=[z^a]int_0^1 u e^(uT)du
   =[z^a]((T-1)e^T+1)/T^2.
```

Equivalently, `A_a=sum_comp prod w/(p+1)!` and
`C_a=sum_comp (p+1)prod w/(p+2)!`. Then

```text
p_t=P(last=t)=w_t A_(s-t)/w_(s+1),
q_B=w_(s+1-B)w_B/w_(s+1),

M_B(t)=0,                                           t<B,
       =w_B A_(s-B)/w_(s+1),                       t=B,
       =w_(t-B)w_B C_(s-t)/w_(s+1),               t>B.
```

The exact reset entry is

```text
J_s(B,t)=[M_B(t)-q_B p_t]^2
          /{[w_(s-t)w_t/w_(s+1)]q_B}.              (H.4)
```

Formula (H.4) was checked against every directly enumerated entry through
`s=10` at error below `2e-12`. It is a proved basin-current identity; the
finite check is only a normalization audit. The child has local rank `s-1`,
so (H.4) is rank lowering, not a same-rank kernel.

## Remaining standalone proposition

> **CANONICAL RESET SUBSTOCHASTICITY.** Prove (H.3), preferably by a
> chi-square/martingale conservation identity for canonical basin currents
> along the pure-deep descendant law. A bound `1+O(s^-1)` would also suffice
> with a polynomial rank potential. Then combine at most `r` reset
> generations with M71's one-shot `O(r^9)` actual-edge unmarking.

Until this proposition is proved, the result is only a separated marked
reduction for auxiliary `Pbar`; it is neither an actual-edge comparison nor
a theorem for `K`.
