# M192 exact shared-endpoint and disjoint-prefix reduction

Date: 2026-08-13 UTC.

Status: Propositions 1--3 below are **proved**. The profile estimates `(DV)`
and `(DE)`, hence the `J=2` prefix estimate, full `(PCR)/(WPCR)`, `(SCBR)`,
and every downstream statement remain **unresolved**.

## 1. Setting and accepted interface

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Put `n=3k`, odd `k>=3`,

```text
h=(0,1,...,n-1),
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform law on minimal length-`n-1` transposition
factorizations of `h`, and the operator is the fixed-cell nonlazy cyclic
rank-two coordinate kernel. This is not the global identity bridge or the
lazy `{3,4,5}` heat-bath chain.

M186/M189's immutable exact `J=2` coefficient is the component pushforward
of

```text
Lambda_L-Lambda_F,
```

where `L` is B's exterior `(2k-1)`-cycle and `F=C_-C_+` is A's two exterior
`k`-cycles. Let `p_s,q_s` be the normalized laws of the first smaller split,
with supports

```text
p_s: 1<=s<=k-1,               q_s: 1<=s<k/2,
```

and extend `q_s=0`. Every ordered second edge, shared endpoint, same/cross-run
double, unit gap, and repeated component size is retained before projection.

The prefix observables relevant to M186 are

```text
X_l=sum_(2<=d<=l)[N_1(d)+N_2(d)],
Y_l=sum_(2<=d<=l)N_1(d),        2<=l<=(n-1)/2.       (1.1)
```

They take values in `[0,3]`.

## 2. Exact shared-endpoint coefficient

Put `tau(d)=d^(d-1)/d!`. Lagrange inversion for
`T(z)=sum_(d>=1)tau(d)z^d=ze^T` gives

```text
[z^r]T(z)^2=2(r-1)tau(r)/r,
```

or equivalently

```text
sum_(c=1)^(r-1)tau(c)tau(r-c)=2(r-1)tau(r)/r.        (2.1)
```

After the first chord cuts an active cycle into sizes `a,b`, its endpoints
are marked, one in each new component. The second factor produces a triangle
exactly when it is an internal chord incident to either marked endpoint. For
a marked size-`r` component, summing the completion-count ratio over its
`r-1` possible partners and using (2.1) contributes

```text
2(r-1)/[r(R-1)],                                    (2.2)
```

where `R-1=2k-3` is the exterior rank remaining after the first factor.

### Proposition 1 (proved: complete shared-endpoint law)

Conditioned on first smaller split `s`, the exact shared-endpoint
probabilities are

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),

gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                 (G)
```

Their total masses are

```text
sum_s p_s gamma_L(s)=3/(2k-1),

sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].              (2.3)
```

Consequently, for `Z=X_l` or `Y_l`,

```text
|E_B[Z 1_T]-E_A[Z 1_T]|=O(1/k).                     (2.4)
```

#### Proof

For `L`, use (2.2) on component sizes `s,2k-1-s`. For `F`, use it on
`s,k-s`; the untouched `k`-cycle contributes rank but contains neither
marked endpoint. This gives `(G)`.

The first identity in (2.3) is the standard first-two-factor triangle mass
`3/(2k-1)` for one cycle. On the A side, after the first exterior factor,
the second chooses the same original `k`-cycle with probability
`(k-2)/(2k-3)`; conditional there, the triangle probability is `3/k`. This
gives the second identity. Since `0<=Z<=3`, (2.4) follows. Every repeated
small face remains inside `Z`; no collision stratum was deleted. QED.

Thus shared-endpoint triangles already have the desired
`O(sqrt(l)/k)` scale for every `l>=2`. The rest of the proof works only with
disjoint second edges, whose products are doubles.

## 3. Exact disjoint-pair Abel identity

Define the unnormalized disjoint split weights

```text
p_hat_s=p_s[1-gamma_L(s)],
q_hat_s=q_s[1-gamma_F(s)].                           (3.1)
```

Let `Phi_s^D` and `Psi_s^D` be the B/A product laws conditioned jointly on
the first split `s` and a disjoint second edge. They are normalized literal
ordered-pair laws. In particular, they retain both double colors, every
same-run/cross-run choice in `L`, the unique two-run ambient component,
and all component-size multiplicities.

For `1<=u<=k-1`, put

```text
E_u=sum_(s<=u)(p_hat_s-q_hat_s).                     (3.2)
```

### Proposition 2 (proved: disjoint-prefix response)

For any test function `Z` on double products,

```text
R_D(Z):=sum_s p_hat_s Phi_s^D(Z)-sum_s q_hat_s Psi_s^D(Z)

=E_(k-1)Phi_(k-1)^D(Z)
 +sum_(u=1)^(k-2)E_u[Phi_u^D(Z)-Phi_(u+1)^D(Z)]
 +sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)].         (DA)
```

The endpoint is exactly

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].                   (EP)
```

#### Proof

Add and subtract `sum_s q_hat_s Phi_s^D(Z)`. For the scalar difference,
write `p_hat_s-q_hat_s=E_s-E_(s-1)` and use `E_0=0`. Unlike M186's original
probability-law Abel transform, the disjoint submeasures have unequal total
mass, so the endpoint in `(DA)` must remain. By (2.3),

```text
E_(k-1)=[1-3/(2k-1)]
        -[1-3(k-2)/(k(2k-3))],
```

which simplifies to `(EP)`. QED.

The endpoint is `O(k^-2)`, and `|Phi_(k-1)^D(Z)|<=3` for either prefix
observable, so it is harmless at the desired scale.

## 4. Scalar cumulative bound

Let

```text
D_u=sum_(s<=u)(p_s-q_s).                             (4.1)
```

Uniform Stirling bounds give `b_s=e^-s tau(s)<=Cs^-3/2`. For
`s<=k/2`, the exact Borel likelihood ratios imply

```text
p_s+q_s<=C b_s,
|p_s-q_s|<=C(s/k)b_s.                               (4.2)
```

Hence, for `u<=k/2`,

```text
|D_u|<=C/k sum_(s<=u)s b_s<=C sqrt(u)/k.            (4.3)
```

For `u>k/2`, normalization gives `D_u=-sum_(s>u)p_s`. The uniform bulk
form

```text
p_s<=C k^(3/2)/[s^(3/2)(2k-1-s)^(3/2)]
```

implies `|D_u|<=C/sqrt(k)<=C sqrt(u)/k`. Thus (4.3) holds for every
`1<=u<=k-1`.

### Proposition 3 (proved: disjoint scalar response)

Uniformly in odd `k>=3` and `1<=u<=k-1`,

```text
|E_u|<=C sqrt(u)/k.                                  (EW)
```

#### Proof

By (3.1)--(4.1),

```text
E_u=D_u-sum_(s<=u)[p_s gamma_L(s)-q_s gamma_F(s)].  (4.4)
```

Formula `(G)` gives `0<=gamma_L,gamma_F<=C/k`. Since `p,q` are probability
laws, the second term in (4.4) is `O(1/k)`. Combine with (4.3), noting
`sqrt(u)>=1`. QED.

This proves the exact signed scalar cancellation that is lost by separating
the B and A disjoint laws in absolute value.

## 5. Strict remaining profile lemmas

For `Z=X_l,Y_l`, define:

> **DISJOINT SPLIT VARIATION `(DV)` (unresolved).** Uniformly in odd `k`
> and `2<=l<=(3k-1)/2`,
>
> ```text
> sum_(u=1)^(k-2)sqrt(u)
>   |Phi_u^D(Z)-Phi_(u+1)^D(Z)| <=C sqrt(l).         (DV)
> ```

> **DISJOINT EMBEDDING RESPONSE `(DE)` (unresolved).** In the same range,
>
> ```text
> |sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)]|
> <=C sqrt(l)/k.                                    (DE)
> ```

Substituting `(EW)`, `(DV)`, and `(DE)` in `(DA)` gives

```text
|R_D(Z)|<=C sqrt(l)/k.                               (5.1)
```

Together with Proposition 1, this is the desired **conditional `J=2` prefix
estimate**. Neither `(DV)` nor `(DE)` is proved here. They are strictly more
explicit than the original `J=2` prefix obligation:

- `(DV)` is only weighted variation as the first B split changes by one;
- `(DE)` is one signed deletion/merge embedding response under the A
  disjoint weight;
- shared endpoints, the unequal double mass, the scalar Borel mismatch, and
  the nonzero endpoint have already been handled exactly; and
- same/cross-run double types and size collisions remain literally inside
  the two profiles rather than being bounded as separate channels.

This mission does not combine a separate absolute `J=1` estimate with (5.1)
to claim full `(PCR)`, `(WPCR)`, or `(SCBR)`.

## 6. Exact finite calibration and scope

`j2_prefix_check.py` is deterministic, standard-library only, and capped at
exact `k=3,5,7`. It constructs only exterior first-factor and ordered-pair
completion laws and verifies `(G)`, (2.3), `(DA)`, and `(EP)` exactly. It
retains 14, 132, and 470 ordered collision events at those ranks.

The finite maxima are:

| `k` | `max_u k|E_u|/sqrt(u)` | max `(DV)` LHS / `sqrt(l)` | max `k|(DE)|/sqrt(l)` | max `k|R_D|/sqrt(l)` |
|---:|---:|---:|---:|---:|
| 3 | 1.0400 | 0.3464 | 0.6333 | 0.6034 |
| 5 | 0.8393 | 1.0483 | 0.4680 | 0.4956 |
| 7 | 0.8301 | 1.2453 | 0.4359 | 0.4908 |

Each maximum is over both `X_l,Y_l`, except the displayed variation column,
which reports their larger maximum. These values only fail to falsify the
two proposed lemmas at three ranks. They imply no sign, monotonicity,
uniform constant, asymptotic limit, or proof.

No broad quotient/shell computation, final channelwise absolute split,
PCS/FCL1/direct-L1, H0/gap, mixing, or Terminal inference occurs here.
