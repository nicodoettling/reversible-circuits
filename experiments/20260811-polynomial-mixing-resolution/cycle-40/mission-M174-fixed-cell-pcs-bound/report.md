# M174 report: fixed-cell PCS boundary coefficient

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, and verdict

For `n=3k`, odd `k>=3`, this mission attacked only

```text
(PCS-bound)    k |sum_(y=1)^(n-3) z_k(y)|=O(1).
```

**Verdict: strict reduction; PCS-bound remains unresolved.** The report proves
an exact signed covariance/cycle-index representation, evaluates every
constant and affine response term, and reduces PCS-bound to the boundedness
of one explicit boundary-response coefficient `(BR)`. No finite sign is
promoted.

## 2. Target distribution, convention, and kernel

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The target is the uniform law on minimal length-`n-1` transposition
factorizations of the long cycle `h=(0 1 ... n-1)`. The sources are

```text
A=(0,k,2k),                   B=(0,1)(k,2k).
```

The kernel is M73's exact nonlazy cyclic rank-two quotient kernel. It is not
the global identity-word law and not the `{3,4,5}` heat-bath chain.

## 3. Exact scalar/covariance theorem

With M168's phase-collapsed response `f_k(s)=S(s)/A_s` and the exact first
pair-product laws `P_A,P_B`,

```text
Delta_k(C_k)=E_(P_B)f_k-E_(P_A)f_k,
sum_y z_k(y)=2 Delta_k(C_k)/pi_y,
pi_y=2/(n-2)(1-2/n)^(n-3).
```

Hence PCS-bound is equivalent to `n^2|Delta_k(C_k)|=O(1)`. Splitting the
source pair laws into the accepted M91 channels, their common `J=0` measure
cancels exactly. With the symmetric channel law `mu_j` and signed likelihood
score `sigma_j`,

```text
Delta_k(C_k)=2 sum_(j=1)^2 alpha_j
                  Cov_(mu_j)(f_k,sigma_j).
```

Both channels are summed before an absolute value. This identity is not a
Poincare or spectral statement.

## 4. Exact PC/cycle-index response

For a one-run residual component of size `d`, define

```text
U_1=(d-1)tau(d-1)/tau(d),
V_1=(d-2)(d-3)tau(d-2)/tau(d).
```

For a two-run component with positive runs `a,b`, `d=a+b`, define

```text
U_2=(d-2)tau(d-1)/tau(d),
V_2=((d-2)(d-3)-2[(a-2)_+ +(b-2)_+])tau(d-2)/tau(d).
```

Then, exactly, retaining triangle/double and all PC target topologies,

```text
f_k(s)=1/((n-3)(n-4))
       [sum_i V_i+2 sum_(i<j)U_iU_j].
```

For the rooted-tree function
`T(z)=sum tau(d)z^d=z exp(T(z))`, the one-run decorations satisfy

```text
sum tau(d)U_1(d)z^d=z^2T'(z),
sum tau(d)V_1(d)z^d=z^4T''(z).
```

The two-run term is the corresponding explicit bivariate positive-composition
coefficient with its displayed boundary correction.

## 5. Signed affine cancellation and exact kind transfer

Writing exact bounded residuals around the one-run asymptotics
`eU_1=d+1/2+O(1/d)`, `e^2V_1=d^2-2d+O(1)` and two-run asymptotics
`eU_2=d-1/2+O(1/d)`, `e^2V_2=d^2-4d+O(1)` gives an explicit scalar `B_k(s)`
such that

```text
e^2(n-3)(n-4)f_k(s)=
  n^2+B_k(s)                 for a triangle,
  n^2-2n+B_k(s)              for a double.
```

The source kind transfer occurs only in `J=2` and is exactly

```text
eta(T)=12(k-1)/[3k(3k-4)(2k-1)],    eta(D)=-eta(T).
```

Therefore

```text
Delta_k(C_k)=e^-2/((n-3)(n-4))
                  [2n eta(T)+eta(B_k)].
```

The explicit kind term is already `O(n^-2)` after normalization.

## 6. Dependencies, multiplicity, and status labels

- **Accepted proved inputs:** M73's raw/quotient kernel and gap schemas;
  M91's source residual split, channel weights, and common `J=0`
  cancellation; M94/M100's Borel convention; M161/M166's exact first-cell
  score; M168/M171's PC/PCS and physical event identities.
- **Proved here:** scalar expectation and covariance identities; exact
  `U,V` component response; rooted-tree coefficient shifts; affine response
  cancellation; exact source kind transfer; equivalence to `(BR)`.
- **Exact finite only:** ordered-lift calibration at `k=3,5,7`.
- **Unresolved:** `(BR)` and therefore PCS-bound.

Triangle lift `3`, double lift `2`, ordered source factors, target's twofold
colored representation, and both signed source channels are retained. No
new literature theorem is used.

## 7. Falsification and boundary cases

`pcs_channel_calibration.py` enumerates only the first two ordered source
factors and evaluates the phase-collapsed first-cell response; it constructs
no quotient matrix. Exact `Fraction` runs at the mandated cap `k=3,5,7`
match every frozen M161 score sum and verify:

- common `J=0` cancellation;
- zero `J=1` kind transfer;
- the closed `J=2` triangle/double transfer formula;
- reconstruction of the full PCS event contrast.

The values of `n^2 Delta` are `2.66440,1.51186,1.19283`, and the residual
boundary coefficients are `5.37164,5.58410,5.46418`. These do not prove
boundedness or positivity. The family starts at odd `k=3`; `k=1`, even `k`,
`m=0,2`, and `N=2` are outside this fixed-cell parameterization.

## 8. First unproved standalone lemma and self-attack

The sole remaining scalar is:

> **Boundary-response coefficient `(BR)` (unresolved).** Uniformly for odd
> `k>=3`,
>
> ```text
> |eta(B_k)|
> =|2 sum_(j=1)^2 alpha_j Cov_(mu_j)(B_k,sigma_j)|=O(1).
> ```

This is strictly sharper than PCS-bound because the constant part, affine
component response, and exact kind-mass transfer are already removed.
Pointwise `B_k(s)` can be `O(n)`: a bounded residual decoration multiplies a
macroscopic component size. Thus a triangle inequality over split sizes,
channels, or kinds does not close `(BR)`; its signed Borel coefficient must
be controlled. That is the exact obstruction, not a computational gap.

## 9. Artifacts, commands, hygiene, and scope firewall

Owned artifacts are `plan.md`, `checkpoint.md`, `proof.md`,
`pcs_channel_calibration.py`, `pcs_channel_exact.json`, `results.json`, this
report, `freeze_manifest.md`, and `SHA256SUMS`.

The decisive command is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-40/mission-M174-fixed-cell-pcs-bound/pcs_channel_calibration.py --k 3 5 7 --frozen-m168 experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-40/mission-M174-fixed-cell-pcs-bound/pcs_channel_exact.json
```

It is deterministic, uses Python 3 standard library only, and has
`seed=null`. No dependency, network, random input, package install, broad
matrix, or shell scan was used. No predecessor, coordinator, manuscript,
skill, or shared project file was edited.

FD-bound was not attacked. This result gives no direct-L1, H0, spectral-gap,
identity-chain, mixing-time, or Terminal inference. A fresh referee should
audit the exact affine constants, the kind-transfer simplification, and the
claim that `(BR)` is equivalent to PCS-bound before any promotion.
