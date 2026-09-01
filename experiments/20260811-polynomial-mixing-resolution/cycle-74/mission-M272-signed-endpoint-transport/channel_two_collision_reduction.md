# Exact channel-two collision coefficient

Date: 2026-08-14 UTC.

Status: Propositions 1--2 are **proved exact**.  Proposition 3 proves the
complete shared-endpoint part is at the target scale.  The two signed
disjoint coefficients in Section 5, the decorated owner-ratio coefficient,
`SET`, `PBV`, and `FD-bound` remain **unresolved**.

## 1. Literal ordered-pair law

Put `n=3k`, odd `k>=3`, and use `(pq)(x)=p(q(x))`.  The exterior
residuals are

```text
F=(0,...,k-1)(2k,...,3k-1),
L=(1,...,k-1,2k,...,3k-1).
```

For `G in {F,L}`, let `Lambda_G(e,f)` be the normalized law of the
first two **ordered** factors in a uniform minimal factorization of `G`:

```text
Lambda_G(e,f)
 =F_(r(G)-2)((ef)^-1 G)/F_(r(G))(G),                 (1.1)
```

on literal admissible pairs.  Thus three oriented lifts of a triangle, two
ordered lifts of a double, both exterior colors of `F`, and every cyclic
phase remain in the law.

For a product `a=ef`, define the collision derivative vector

```text
mathcal I(a)
 =(I_(ell+1)(a)-I_ell(a))_(ell=2,...,n-3).           (1.2)
```

The conditional channel-two coefficient is exactly

```text
eta_2(Delta I)=E_(Lambda_L) mathcal I(ef)
               -E_(Lambda_F) mathcal I(ef).         (1.3)
```

No product kind or phase is removed in (1.3).

## 2. Split and shared-endpoint masses

Let `s` be the smaller split of the first factor in its source cycle.
Its marginal is M91's normalized `p_s` for `L`,
`1<=s<=k-1`, and `q_s` for `F`, `1<=s<k/2`, with `q_s=0`
outside that range.

Conditioned on `s`, let `gamma_L(s)` and `gamma_F(s)` be the
probabilities that the second factor shares an endpoint with the first.
Cutting the active cycle marks one vertex in each new component.  For a
marked size-`r` component, the critical-Cayley convolution

```text
sum_(c=1)^(r-1) tau(c)tau(r-c)=2(r-1)tau(r)/r        (2.1)
```

shows that all second chords incident to the mark have total normalized
weight `2(r-1)/[r(2k-3)]`.  Summing the two marked components gives

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                 (2.2)
```

Summing (2.2) against the first-split laws, or equivalently counting the
first two edges incident in the Cayley tree, gives

```text
sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].              (2.3)
```

These identities are rederived here from (2.1); no channel-two profile
claim from an earlier mission is assumed.

## 3. Triangle/double disintegration

Define the unnormalized disjoint split masses

```text
p_hat_s=p_s[1-gamma_L(s)],
q_hat_s=q_s[1-gamma_F(s)].                          (3.1)
```

Let `Theta_(B,s),Theta_(A,s)` be the unnormalized vectors (1.2) on
shared-endpoint pairs at split `s`.  Let `Phi_s^D,Psi_s^D` be the
normalized vectors on disjoint ordered pairs at split `s` for `L,F`.
They are expectations of the complete vector `mathcal I(ef)`; in
particular they are not size/run summaries.

Then, before every lag absolute value,

```text
eta_2(Delta I)=Theta+R_D,                            (3.2)

Theta=sum_s[Theta_(B,s)-Theta_(A,s)],
R_D=sum_s p_hat_s Phi_s^D-sum_s q_hat_s Psi_s^D.    (3.3)
```

## 4. Exact vector-valued signed Abel identity

Put

```text
E_u=sum_(s<=u)(p_hat_s-q_hat_s),       1<=u<=k-1.   (4.1)
```

### Proposition 1 (proved)

The endpoint is nonzero and equals

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].                   (4.2)
```

As an exact vector indexed by `ell=2,...,n-3`,

```text
R_D
 =E_(k-1)Phi_(k-1)^D
  +sum_(u=1)^(k-2)E_u[Phi_u^D-Phi_(u+1)^D]
  +sum_(s<k/2)q_hat_s[Phi_s^D-Psi_s^D].             (4.3)
```

#### Proof

Equation (2.3) gives

```text
E_(k-1)=[1-3/(2k-1)]
        -[1-3(k-2)/(k(2k-3))],
```

which is (4.2).  Add and subtract
`sum_s q_hat_s Phi_s^D` in (3.3), write
`p_hat_s-q_hat_s=E_s-E_(s-1)`, and summation-by-parts using
`E_0=0`.  This proves (4.3) coordinatewise and hence as a vector.  QED.

The nonzero endpoint in (4.2) cannot be discarded by pretending that the
disjoint sublaws are probability measures of equal mass.

### Proposition 2 (proved scalar cumulative input)

Uniformly in `u`,

```text
|E_u|<=C sqrt(u)/k.                                  (4.4)
```

#### Proof

For `D_u=sum_(s<=u)(p_s-q_s)`, the exact critical-Borel likelihood
ratios give

```text
|D_u|<=C sqrt(u)/k.
```

Indeed, below `k/2`,
`|p_s-q_s|<=C(s/k)b_s` and `b_s<=Cs^-3/2`; above `k/2`, use
normalization and the long-cycle bulk tail.  From (2.2),
`gamma_L,gamma_F<=C/k`, so

```text
E_u=D_u-sum_(s<=u)[p_s gamma_L(s)-q_s gamma_F(s)].
```

The last sum is `O(1/k)`, proving (4.4).  QED.

## 5. Proved triangle scale and first open signed coefficients

### Proposition 3 (proved)

```text
||Theta||_1=O(1/k).                                  (5.1)
```

#### Proof

A triangle moves three vertices, so its nonzero circular collision profile
has total mass six.  The total variation of that profile is at most twice
its mass, hence the restricted derivative vector (1.2) has l1 norm at most
`12`.  Equations (2.3) and the triangle inequality only between the two
positive triangle submeasures give

```text
||Theta||_1
 <=12[3/(2k-1)+3(k-2)/(k(2k-3))]=O(1/k).
```

This triangle bound retains every triangle phase; it does not split a
signed double coefficient.  QED.

The mission-level channel-combined collision lemma is

```text
(CIBV)
sum_ell|alpha_1 eta_1(Delta I_ell)
             +alpha_2 eta_2(Delta I_ell)|=O(1/k).
```

The complete channel-one term and the channel-two triangles are proved.
Thus CIBV is reduced exactly to the following two signed channel-two vector
estimates:

```text
(CSBV)
||E_(k-1)Phi_(k-1)^D
  +sum_(u=1)^(k-2)E_u[Phi_u^D-Phi_(u+1)^D]||_1
 =O(1/k),

(CEBV)
||sum_(s<k/2)q_hat_s[Phi_s^D-Psi_s^D]||_1=O(1/k).   (5.2)
```

Both norms are taken only after the signed sums.  Proving (CSBV) and (CEBV)
would combine with (5.1) to prove
`sum_ell|eta_2(Delta I_ell)|=O(1/k)`, and with the independently proved
channel-one result in `phase_incidence_lemma.md` would prove CIBV.
Neither estimate in (5.2) is proved here.

## 6. Why adjacent-profile triangle bounds do not close

Inserting (4.4) term by term in (4.3) would demand the much stronger norm

```text
CDV=sum_(u=1)^(k-2)sqrt(u)
          ||Phi_u^D-Phi_(u+1)^D||_1=O(1).           (6.1)
```

The legal uniform statewise bound only makes each adjacent norm `O(1)`;
substitution then loses a polynomial factor and cannot prove (CSBV).
This **refutes that statewise-triangle inference as a target-scale proof
route**, not (CSBV), channel-two collision, or SET.

The exact checker further makes the obstruction concrete:

| `k` | `CDV` | `k||CSBV vector||_1` | `k||CEBV vector||_1` | `k||eta_2(Delta I)||_1` |
|---:|---:|---:|---:|---:|
| 3 | 0.0000 | 0.9600 | 3.2889 | 5.3369 |
| 5 | 6.0563 | 0.8543 | 5.1017 | 5.0161 |
| 7 | 25.4890 | 0.9642 | 4.5937 | 4.6274 |

Thus the norm created by adjacent triangle bounds grows sharply over the
tested family while the two signed vectors remain at the target finite
scale.  These values are exact-finite falsification/calibration only; they
do not prove a uniform bound, divergence of (6.1), or any asymptotic sign.

Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-74/mission-M272-signed-endpoint-transport/channel_two_collision_probe.py --k 3 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-74/mission-M272-signed-endpoint-transport/channel_two_collision_results.json
```

Python `3.12.3`; standard library only; `seed=null`.

## 7. Separate decorated obstruction

M261's exact affine identity is

```text
e^2 eta(E_ell)=eta(Delta I_ell)+eta(Delta Q_ell).
```

Even if (5.2) closes the collision term, SET still needs the signed
decorated estimate

```text
(DOR)
sum_(ell=2)^(n-3)|eta(Delta Q_ell)|=O(1/k),          (7.1)
```

or a joint collision/decorated estimate before their absolute value.
The plausible seam probability times owner-ratio defect mechanism has not
been proved.  No channel, kind, or path edge is triangle-bounded to assert
(7.1).
