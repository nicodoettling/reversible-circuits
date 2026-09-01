# Phase incidence after full split transport

Date: 2026-08-14 UTC.

Status: Propositions 1--2 are **proved exact identities**.  Proposition 3 is
a **proved asymptotic bound for the complete channel-one collision
derivative**.  The seam-only cancellation claim is **refuted exactly at
finite rank**.  `channel_two_collision_reduction.md` proves the complete
triangle contribution and an exact vector-valued disjoint Abel reduction;
its two signed disjoint bounds, the decorated owner-ratio bound, `SET`,
`PBV`, and `FD-bound` remain **unresolved**.

## 1. Raw laws and the exact bad-phase indicator

Use the notation and conventions of `adjacent_transport.md`.  Put

```text
F=C_- C_+,
L=(1,...,k-1,2k,...,3k-1),
M=(k,...,2k-1).
```

Let `lambda_F,lambda_L,lambda_M` be the exact first-factor laws in these
residual permutations, and let `Lambda_F,Lambda_L` be the exact ordered
first-two-factor laws.  For `g in {A,B}`, write `R_A=F,R_B=L` and define,
for each first exterior factor `e`, product kind `K`, and lag `ell`,

```text
V_(g,K,ell)(e)
 =alpha_1 lambda_(R_g)(e) sum_f lambda_M(f)
       1[K(ef)=K] E_ell(ef)
  +alpha_2 sum_f Lambda_(R_g)(e,f)
       1[K(ef)=K] E_ell(ef).                         (1.1)
```

Every sum is over literal ambient transpositions.  Thus the two channels
are combined inside `V`, while the `T/D` kind is still explicit.

Let `U_-={1,...,k-1}` and `U_+={2k,...,3k-1}`.  The literal splice/deletion
indicators are

```text
b_B(e)=1[e has one endpoint in U_- and one in U_+],
b_A(e)=1[0 is an endpoint of e].                    (1.2)
```

Define

```text
eta_bad(E_ell)
 =sum_K {sum_e b_B(e)V_(B,K,ell)(e)
        -sum_e b_A(e)V_(A,K,ell)(e)},

eta_good(E_ell)
 =sum_K {sum_e (1-b_B(e))V_(B,K,ell)(e)
        -sum_e (1-b_A(e))V_(A,K,ell)(e)}.            (1.3)
```

### Proposition 1 (proved: exact phase-incidence partition)

For every `2<=ell<=n-3`,

```text
eta(E_ell)=eta_good(E_ell)+eta_bad(E_ell),           (1.4)

sum_K <w,T_(K,ell)>
 ={eta_good(E_ell)+eta_bad(E_ell)}/n.                (1.5)
```

#### Proof

The `J=0` law is common and absent.  Equation `(1.1)` is exactly the
remaining M91 `J=1,2` raw law, with its normalized channel masses and all
ordered lifts.  The two indicators in `(1.2)` partition their respective
first-exterior-edge spaces, proving `(1.4)`.  The independently rederived
owner-charge phase normalization proves `(1.5)`.  QED.

No absolute value has occurred in `(1.1)--(1.5)`.  In particular, this is a
legal place to ask whether only seam/deletion incidences survive; it does
not assume that claim.

## 2. Exact channel-one collision coefficient

Let `I_ell(s)=sum_r b_s(r)b_s(r+ell)` be M261's moved-head collision
profile.  Consider the conditional channel-one contrast

```text
eta_1=H_(1,B)-H_(1,A),                              (2.1)
```

before multiplication by `alpha_1`.  Its product is `s=ef`, where the
exterior edge `e` and middle edge `f` are disjoint and independent.

For a chord in the exterior source, let `a` be the positive ambient face
not containing the middle block.  Direct chord classification gives the
two normalized face laws

```text
rho_A(a)=(k-a)nu_k(a),                    1<=a<k,

rho_B(a)=S_k(a)nu_(2k-1)(a)
        +C_k(a)nu_(2k-1)(a-1),           1<=a<=2k-1, (2.2)

S_k(a)=(k-1-a)_+ +(k-a)_+,

C_k(a)=a-1             for 2<=a<=k,
       =2k-a            for k<a<=2k-1,
       =0               otherwise.
```

Invalid `nu` indices are zero.  Put `delta rho=rho_B-rho_A`, with both
sequences extended by zero.

Let `a_B(v),a_A(v)` be the endpoint intensities of the exterior chord and
let `m(v)` be the middle-chord endpoint intensity.  Cyclic symmetry gives
exactly

```text
a_B(v)=2/(2k-1)  on U_- union U_+,       0 otherwise,
a_A(v)=1/k       on {0} union U_- union U_+, 0 otherwise,
m(v)=2/k         on M,                   0 otherwise. (2.3)
```

Consequently

```text
||a_B-a_A||_1=2/k,             ||Delta m||_1=4/k.   (2.4)
```

### Proposition 2 (proved: exact channel-one collision law)

For every circular lag `ell`,

```text
eta_1(I_ell)
 =delta rho(ell)+delta rho(n-ell)
  +sum_v (a_B-a_A)(v)m(v+ell)
  +sum_v m(v)(a_B-a_A)(v+ell).                      (2.5)
```

#### Proof

Since `e,f` are disjoint,

```text
I_ell(ef)=I_ell(e)+I_ell(f)
 +sum_(v in e,w in f){1[w-v=ell]+1[v-w=ell]}.
```

The middle-only term cancels.  A chord with exterior face `a` contributes
one ordered endpoint pair at `a` and one at `n-a`, giving the first line of
`(2.5)`.  Independence and the endpoint intensities give the second line.
QED.

## 3. A Borel face bounded-variation lemma

Write `b_j=e^-j j^(j-1)/j!`.  The exact per-chord law is

```text
nu_d(a)=b_a b_(d-a)/[(d-1)b_d].                     (3.1)
```

### Lemma (proved)

There is an absolute `C` such that, for every odd `k>=3`,

```text
sum_a |delta rho(a+1)-delta rho(a)| <=C/k.           (3.2)
```

#### Proof

Put

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2),
R_m(a)=b_(m-a)/b_m.
```

The logarithmic series for `r_j` gives, uniformly for `j>=2`,

```text
r_j asymp 1,
|r_j-1|<=C/j,
|r_(j+1)-r_j|<=C/j^2.                               (3.3)
```

It also gives `|b_(a+1)-b_a|<=C b_a/a` and
`sum_a b_a<infinity`.

For `1<=a<=k/2`, substitution of `(3.1)` in `(2.2)` gives

```text
delta rho(a)=b_a H_k(a),

H_k(a)= (2k-1-2a)/(2k-2) R_(2k-1)(a)
       +(a-1)/(2k-2) r_a R_(2k-1)(a-1)
       -(k-a)/(k-1) R_k(a).                         (3.4)
```

Using the product identity

```text
R_m(a)=product_(i=0)^(a-1) r_(m-i)
```

and `(3.3)`, compare the three terms in `(3.4)` before taking absolute
values.  Their constant parts cancel, and telescoping the ratio products
gives

```text
|H_k(a)|<=Ca/k,             |H_k(a+1)-H_k(a)|<=C/k. (3.5)
```

Therefore

```text
|delta rho(a+1)-delta rho(a)|<=C b_a/k              (3.6)
```

through the half range, and these terms sum to `O(1/k)`.

On `k/2<a<=k`, all Borel indices in `(2.2)` are comparable to `k`.
The same exact ratio bounds give each summand size `O(k^-3/2)` and adjacent
difference `O(k^-5/2)`; their total variation is `O(k^-3/2)`.

Finally, for `k<a<=2k-1`, put `c=2k-a`.  Equation `(2.2)` reduces exactly
to

```text
rho_A(a)=0,                 rho_B(a)=c nu_(2k-1)(c).
```

From `(3.1)--(3.3)`,

```text
c nu_(2k-1)(c)<=C/(k sqrt(c)),
|Delta[c nu_(2k-1)(c)]|
 <=C/(k c^(3/2))+C/(k^2 sqrt(c)).                   (3.7)
```

Summing `(3.7)` proves an `O(1/k)` far-tail variation.  The two junction
terms obey the neighboring displayed bounds.  This proves `(3.2)`.  QED.

### Proposition 3 (proved: channel-one collision derivative)

There is an absolute `C` such that

```text
sum_(ell=2)^(n-3)
 |eta_1(I_(ell+1)-I_ell)| <=C/k.                    (3.8)
```

#### Proof

The first two terms of `(2.5)` have circular variation at most twice
`(3.2)`.  For circular convolution,

```text
||Delta(f*g)||_1<=||f||_1 ||Delta g||_1.
```

Thus `(2.4)` bounds the two cross terms together by `16/k^2`.  Restricting
the circular variation to the displayed lag range can only decrease it.
QED.

This is a real part of the target scale.  A channelwise triangle inequality
would be legal only after proving the analogous complete `O(1/k)`
channel-two bound; that bound is not assumed here.

## 4. Falsification of the seam-only shortcut

Only after `(1.3)` was fixed, `phase_incidence_probe.py` evaluated it over
exact rational source laws.  The relevant values are

| `k` | `n sum|eta_good(E)|` | `n sum|eta_bad(E)|` | `n sum|eta(E)|` |
|---:|---:|---:|---:|
| 3 | 0.96614 | 1.04686 | 2.01300 |
| 5 | 1.38220 | 1.03648 | 2.41867 |
| 7 | 1.28696 | 0.77395 | 1.97841 |

At `k=3,5` the good and bad vectors even have the same coordinatewise sign
where nonzero, since the first two columns' `l1` sums add exactly to the
third.  At `k=7` their separate sum is `2.06091`, only slightly above the
combined `1.97841`.  Therefore the exact universal assertion

```text
eta_good(E_ell)=0 for every ell
```

is refuted already at the first family member.  A proof cannot charge all
of the response solely to crossing/deleted-vertex first-edge phases.

The same check finds nonzero cancellations between channels and kinds.  For
example, `n` times the separately absolute channel sums versus the combined
sum are

```text
k=3: 0.25116+2.10361 >2.01300,
k=5: 0.49837+2.16036 >2.41867,
k=7: 0.38640+1.76763 >1.97841.
```

These are exact-finite facts, not an asymptotic proof that channel
cancellation is quantitatively essential.  They do rule out replacing the
required combined scalar by an asserted exact channel or phase
orthogonality.

Retained deterministic command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-74/mission-M272-signed-endpoint-transport/phase_incidence_probe.py --k 3 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-74/mission-M272-signed-endpoint-transport/phase_incidence_results.json
```

Python `3.12.3`; standard library only; `seed=null`.

## 5. Exact channel-two reduction and first unresolved coefficients

Writing M261's exact affine split as

```text
e^2 eta(E_ell)=eta(Delta I_ell)+eta(Delta Q_ell),    (5.1)
```

the complete collision task is

```text
sum_ell |alpha_1 eta_1(Delta I_ell)
             +alpha_2 eta_2(Delta I_ell)|=O(1/k),   (CIBV)
```

Proposition 3 supplies the complete first summand.  Independently,
`channel_two_collision_reduction.md` proves that the channel-two
shared-endpoint triangles contribute `O(1/k)` and reduces the disjoint
part, before lag absolute values, to the exact signed vectors `(CSBV)`
and `(CEBV)`.  Those two estimates remain open.

Even after `(CIBV)`, the owner-ratio task is separate: pair each splice
incidence probability of order `s/k` with its literal
`rho_ij=O(1/s+1/(k-s))` defect before summing the signed split law.  The
resulting decorated obligation `(DOR)` is not proved.
