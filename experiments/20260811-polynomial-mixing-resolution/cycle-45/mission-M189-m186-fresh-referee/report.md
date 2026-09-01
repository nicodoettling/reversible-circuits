# M189 report: fresh referee of immutable M186

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, objections, and scope

```text
VERDICT: ACCEPT M186'S STRICT EXACT REDUCTION.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL NUMBERED QUALIFICATIONS: TWO.
```

Accepted: the exact combined critical-Borel/component formulas, complete
`J=1` `O(1/n)` conditional charge, singleton boundary estimate, and signed
prefix reduction. Not accepted or proved: `(PCR)`, `(WPCR)`, `(SCBR)`,
`(BIR)`, `(BR)`, PCS-bound, FD/FCL1/direct-L1, H0/gap, mixing, or either
Terminal.

## 2. Immutable provenance and dependency gate

M186's complete eight-entry `SHA256SUMS` passed before conclusions. Fresh
top-level hashes are

```text
report      dd8d46b3d05f20dd3e3616bd3709f877b3e997bfbb465171179a7188ac7737f7
proof       59116384a8dd2b9dc280b5774022eae62e0e23bb98473d76270525d445edd02a
manifest    9bd47230cc9c6ab6af7030559f886bae045dea8901e24ff9ba5af2f40d67d248
checksums   9d5aa5ff628f8bf15051c09fd1537ffa240fba72ad2a9945356c8adfe8ebd7bd
```

M186 was never edited. The audit uses its accepted M91 and M180 interfaces
only after checking consistency with the literal completion-count rows.

## 3. Target, convention, and exact normalization

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` for odd
`k>=3`, `h=(0,1,...,n-1)`, `A=(0,k,2k)`, and
`B=(0,1)(k,2k)`. The target is the uniform minimal-factorization law of the
long cycle under the fixed-cell nonlazy rank-two coordinate kernel.

From `F_r(R)=r! product tau(d_i)`, direct factorial cancellation gives
first-prefix denominator `r` and ordered-pair denominator `r(r-1)`. This
independently recovers

```text
lambda_L: (D-1)b_D,             lambda_F: 2(k-1)b_k,
lambda_M: (k-1)b_k,             D=2k-1,
Lambda_L: (D-1)(D-2)b_D,
Lambda_F: (2k-2)(2k-3)b_k^2.
```

All numerator exponentials cancel because post-split total size is unchanged.
The laws normalize by the unique first factor/ordered prefix of every minimal
factorization; no lift or component-choice factor is missing.

## 4. Fully combined `(CB)` and `(BA-C)` signs

Since `eta=P_B-P_A`, both surviving channel braces have sign `+L-F`. The
common `J=0` middle law cancels exactly. `J=1` exterior and middle factors
commute and their two color orders already lie in `alpha_1`; `J=2` retains
the ordered `Lambda` law. Thus `(CB)` keeps both channels, kinds, double
colors, shared endpoints, and collision multiplicities before estimation.

Disintegration gives

```text
sum_s p_s phi_s-sum_s q_s psi_s
=sum_s(p_s-q_s)phi_s+sum_s q_s(phi_s-psi_s).
```

With `D_s=sum_(t<=s)(p_t-q_t)` and `D_0=D_(k-1)=0`, summation by parts gives
`sum_(u<k-1)D_u(phi_u-phi_(u+1))`. Hence every sign and endpoint in
`(BA-C)` is correct.

## 5. Exact `J=1` face law and weighted response

For a contiguous block, `rho_A(a)=(k-a)nu_k(a)`. The B exterior runs have
lengths `k-1,k`, so same-run chords number

```text
S_k(a)=(k-1-a)_+ +(k-a)_+.
```

Writing a cross chord as `(i,2k+t)` makes its face avoiding the middle
`a=k+i-t` and its source split `a-1`. Solving the endpoint constraints gives
`C_k(a)=a-1` through `k` and `C_k(a)=2k-a` above `k`. Therefore

```text
rho_B(a)=S_k(a)nu_(2k-1)(a)+C_k(a)nu_(2k-1)(a-1),
rho_B(2k-c)=c nu_(2k-1)(c).
```

Every separated or nested `J=1` double has component data
`(1,a),(1,b),(2,n-a-b)`, yielding M186's exact coefficient formulas.
Uniform Stirling ratios prove the first weighted sum is `O(1/k)`. For the
second, the `a<=k` part has denominator at least `k+1`; the tail reduces to

```text
sum_(c<k)nu_(2k-1)(c)=1/(2k-1).
```

Thus the conditional `J=1` charge is rigorously `O(1/k)=O(1/n)`.

## 6. Singleton, signed summation, and prefix implication

Pointwise on accessible products,

```text
N_1(1)=W+(1/2)W 1_T.
```

M180's exact boundary identity gives

```text
eta(W)=2[U_2(2k-1)-2U_1(k)]/(n-3)=O(1/n).
```

The exact triangle probabilities are `3/k,0` in `J=0,1`, and in `J=2`
are `3/(2k-1)` at B and `3(k-2)/[k(2k-3)]` at A. Since `W<=2`, this proves
`M_1(1)=O(1/n)`.

Writing `P_d=M_1(d)`, `N_d=M_1(d)+M_2(d)` and their prefixes `C_D,A_D`,
ordinary finite Abel summation gives M186's `(SBP)` exactly. The uniform
bounds `u_2,r=O(1/d)` and first differences `O(1/d^2)` show:

- `(PCR)`, `|A_D|+|C_D|=O(sqrt(D)/n)`, implies `(SCBR)`; and
- the displayed weighted-prefix `(WPCR)` condition also implies `(SCBR)`.

Neither prefix condition is proved or attempted here.

## 7. Clean-room exact check

`cleanroom_component_audit.py` is self-contained, standard-library only,
imports no M186 code or data, and runs only exact `k=3,5`. It reconstructs
literal source rows and separately derived component-prefix laws. All
normalization, `(CB)`, `(BA-C)`, face/tail, singleton, triangle, and formal
`(SBP)` assertions pass on 64 and 810 source-accessible states.

| `k` | channel masses `(alpha_0,alpha_1,alpha_2)` | `k` times both `J=1` weighted sums |
|---:|---:|---:|
| 3 | `(1/15,8/15,2/5)` | 1.93871746 |
| 5 | `(1/11,16/33,14/33)` | 1.46710702 |

These are exact calibration only; no sign, limit, or uniform bound is
inferred from two ranks.

## 8. Numbered qualifications and first open step

1. **Nonmaterial:** M186 (4.10) displays `b_(a-1)` while the stated range
   includes `a=1`, but `b_0` is undefined. Handle `a=1` separately (or set
   the invalid term to zero); the bound is unchanged.
2. **Nonmaterial:** the low-face summation should explicitly cite
   `sum_a b_a<infinity`—indeed critical Borel gives `sum_a b_a=1`. This is
   standard and does not leave a mathematical gap.

There are no material objections. The first unproved step remains the fully
channel-, kind-, and collision-combined `J=2` prefix estimate `(PCR)` or the
weaker `(WPCR)`. Global moment cancellations and the proved `J=1` bound do
not supply it.

## 9. Artifacts, hygiene, and action

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`cleanroom_component_audit.py`, `cleanroom_results.json`, `results.json`,
this report, and the freeze files. Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-45/mission-M189-m186-fresh-referee/cleanroom_component_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-45/mission-M189-m186-fresh-referee/cleanroom_results.json
```

Python `3.12.3`; standard library only; `seed=null`. No M186 import/edit,
`k=7`, PCR attempt, broad shell computation, channelwise final absolute
split, finite-sign inference, or downstream claim occurred. Final action:
**accept and freeze only M186's strict reduction, retain both qualifications,
keep `(PCR)` and everything downstream open, and request a fresh immutable
audit before promotion.**
