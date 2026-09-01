# M91 halfway checkpoint: posterior score and two-channel Borel--Abel identity

Date: 2026-08-12.  Status labels below are controlling.

## Scope and target

The target remains the strict-`Lambda_n` estimate

```text
TV(bar K_n^2(alpha,.),bar K_n^2(beta,.)) <= C/n^2
```

for M73's cyclic quotient kernel of the uniform minimal long-cycle bridge.
The focused source edge is `n=3k`, odd `k>=3`,

```text
A_k=(0,k,2k),       B_k=(0,1)(k,2k),
eta_k=bar K(B_k,.)-bar K(A_k,.).
```

No H0 gap, fixed-endpoint bridge gap, identity heat-bath gap, or Terminal
conclusion is in scope.

## Proved posterior cancellation

Put `f_k=eta_k/bar pi`.  Reversibility gives, exactly,

```text
f_k(s)=bar K(s,B_k)/bar pi(B_k)-bar K(s,A_k)/bar pi(A_k),
eta_k bar K(t)=bar pi(t)(bar K f_k)(t),
TV(eta_k bar K)=1/2 E_barpi |bar K f_k|.
```

Writing `A_g=F_(n-3)(g^-1h)` and
`C(g,s)=F_(n-5)((gs)^-1h)`, the score has the explicit phase formula

```text
f_k([s]) = n^(n-3)/A_s * sum_(r=0)^(n-1)
  { C(s,theta^r B_k)/A_(B_k) - C(s,theta^r A_k)/A_(A_k) }.
```

This formula is valid even though the balanced `A_k` orbit has size `k`
rather than `n`: the all-`n` phase sum repeats each short-orbit state exactly
`n/k=3` times, and the quotient orbit size cancels that repetition.  The
ordered pair-product lift multiplicities `a(s),a(A),a(B)` cancel only after
literal quotient masses are used.

## Proved common-component cancellation

The residual components are

```text
A_k: C_- of size k, M of size k, C_+ of size k;
B_k: {0}, L of size 2k-1, M of size k.
```

The middle component `M=(k,...,2k-1)` is identical.  Put `m=k-1`,
`D=3m(3m-1)`, and let `J` be the number of the first two **ordered**
completion factors drawn from the exterior rank `2m`.  The `alpha_j` below
are conditional-color probabilities (not unnormalized schema weights), and
their law is the same under both sources:

```text
alpha_0=m(m-1)/D,
alpha_1=4m^2/D,
alpha_2=2m(2m-1)/D.
```

Conditional on `J=0`, both product laws are exactly `mu_M`, so they cancel
before applying the second kernel.  If `H_{j,B},H_{j,A}` are the conditional
product laws for `J=j`, then the full quotient signed row is exactly

```text
eta_k = alpha_1(H_{1,B}-H_{1,A})
      + alpha_2(H_{2,B}-H_{2,A}).
```

Here `H_1` is the one-exterior/one-middle cross law and `H_2` is the full
first-pair law in, respectively, the merged exterior cycle `L` or the two
separate exterior cycles.  Thus every `I3,IS,IN,X` first-step term is retained,
but the common schema block is removed exactly rather than triangle-bounded.

## Proved Borel--Abel identity

Let

```text
p_s=(2k-1)w_(2k-1)(s),  1<=s<=k-1,
q_s=k w_k(s),           1<=s<=(k-1)/2,
q_s=0 otherwise,
D_u=sum_(s<=u)(p_s-q_s).
```

These are the conditioned-Borel smaller-split laws of the merged and
separate exterior first edges.  For `j=1,2`, let `Phi_{j,s}` be the conditional
`H_{j,B}` product law given merged split `s`, and `Psi_{j,s}` the conditional
`H_{j,A}` law given separate split `s`.  Every `Phi` and `Psi` is a normalized
probability measure on quotient product states, with all raw ordered lifts
summed before quotient pushforward.  Then, as an exact signed quotient measure,

```text
H_{j,B}-H_{j,A}
 = sum_(u=1)^(k-2) D_u(Phi_{j,u}-Phi_{j,u+1})
   +sum_(s=1)^((k-1)/2) q_s(Phi_{j,s}-Psi_{j,s}).
```

The first sum is literal Abel summation; the second is the cyclic embedding /
conditional-second-factor defect.  Applying `bar K` occurs only after the
two `j` channels and all these signed terms are combined.

## Exact falsification checks

`posterior_score_audit.py` checks the score, phase, detailed-balance, and
stationary-L1 identities.  They pass over exact rationals at `k=3,n=9` and
over floating arithmetic at `k=5,7` (`n=15,21`).

`balanced_abel_audit.py` independently reconstructs both full quotient rows
from ordered completion factors at `k=3`, verifies the common `J=0`
cancellation, both measure-valued Abel identities, every conditioned-Borel
weight, and equality after the second kernel.  It reproduces

```text
TV(eta_3)=3196/5625,
TV(eta_3 bar K)=27708771860129/306307575000000.
```

These are exact finite formula checks, not evidence proving an asymptotic
rate.

## Remaining named inequality

For a target orbit `t`, put

```text
G_t(s)=bar K(s,t)/bar pi(t)
```

and evaluate the two Abel brackets above on `G_t`, calling the results
`A_{1,k}(t),A_{2,k}(t)`.  The balanced family is reduced to the single
positive summation inequality

```text
sum_t bar pi(t)
  [alpha_1 A_{1,k}(t)+alpha_2 A_{2,k}(t)]^2 <= C/k^4.   (BA2)
```

Indeed the bracket is exactly `(bar K f_k)(t)`, so Cauchy--Schwarz turns
`(BA2)` into `TV(eta_k bar K)<=sqrt(C)/(2k^2)`.  The square and the eventual
absolute value remain outside both channels and all four second-step schemas.

`(BA2)` is unresolved.  Finite values of `k^4 E[(bar K f_k)^2]` at
`k=3,5,7` are `5.23023,3.57733,4.29699`; they merely fail to falsify it.
The corresponding termwise weighted-Fisher upper bounds, after multiplication
by `k^4`, are `7.91878,13.9029,37.4078`.  This finite inflation warns against
splitting the Abel gradients before their remaining signed cancellation.  The
general strict-edge inequality also remains unresolved.
