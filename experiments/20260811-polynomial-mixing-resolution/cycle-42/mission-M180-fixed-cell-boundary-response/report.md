# M180 report: fixed-cell boundary charge

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: STRICT ONE-DIMENSIONAL BOUNDARY-CHARGE REDUCTION.
(BR) AND PCS-BOUND: UNRESOLVED.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. For `n=3k`, odd `k>=3`, this mission concerns only M73's
nonlazy cyclic rank-two coordinate kernel under the uniform law on minimal
length-`n-1` factorizations of the long cycle, at

```text
A_k=(0,k,2k),                  B_k=(0,1)(k,2k).
```

It is not the global identity-word target or the lazy `{3,4,5}` heat-bath
chain. No FD-bound, direct-L1, H0, gap, mixing, or Terminal statement is
proved or inferred.

## 2. Strongest proved theorem

Let `eta=P_B-P_A` be the complete signed first-row law, with M91's `J=1,2`
channels already combined. For an intermediate `s`, let its three residual
components have sizes `d_i` and ambient run types one or two. Define

```text
Q(s)=sum_i u_type(i)(d_i),
```

where `u_1,u_2` are M174's exact centered `U` decorations. If `I_D(s)` is
the number of unit runs in the unique two-run component of a double (zero
for a triangle), then this mission proves exactly

```text
B_k(s)=2nQ(s)-7/2-2I_D(s)+R(s),
sup_(n,s)|R(s)|<infinity.                            (2.1)
```

The bounded kind/collision terms are harmless under the signed probability
measure. Therefore

```text
eta(B_k)=O(1)  iff  n eta(Q)=O(1).                   (2.2)
```

This removes every quadratic response, affine kind term, collision
indicator, and uniformly bounded small-size correction from the open step.
The only remaining object is an additive first-boundary component charge.

## 3. Correct sharp centers and response constants

The exact Cayley ratios satisfy, uniformly over positive valid sizes,

```text
u_1(d)=  7/(24d)+O(d^-2),
u_2(d)=-29/(24d)+O(d^-2),

v_1(d)=-5/3+O(d^-1),
v_2(a,b)=1/3-2(1[a=1]+1[b=1])+O(d^-1).              (3.1)
```

The material intermediate expansion is

```text
e^2 tau(d-2)/tau(d)=1+3/d+22/(3d^2)+O(d^-3).
```

Its `22/3` coefficient comes from retaining the cubic logarithm term before
multiplication by `d-3`. It yields the common type constant `-7/2` in
(2.1). The previously rejected transient affine value `7/5` is unrelated
and remains invalid; the exact kind coefficients are still

```text
L_T=0,                         L_D=-2.
```

All `(a-2)_+,(b-2)_+` terms survive through the exact indicator in (3.1).

## 4. Exact one-dimensional coefficient and proved tail

With M94's exact Borel contrast

```text
delta_k(s)=beta_5(B,s)/beta_3(B)-beta_5(A,s)/beta_3(A),
```

let `N_r(d;s)` count residual components of size `d` and run type
`r in {1,2}`. Define

```text
M_(r,k)(d)=1/((n-3)(n-4))
 sum_(s in X_n)a(s)delta_k(s)N_r(d;s).               (4.1)
```

This sums both source channels and both intermediate kinds before projecting
to size. The exact response is

```text
eta(Q)=sum_d[M_(1,k)(d)u_1(d)+M_(2,k)(d)u_2(d)].     (4.2)
```

Writing

```text
t_k=12(k-1)/[3k(3k-4)(2k-1)],
```

the coefficients obey

```text
sum_d M_1(d)=t_k,          sum_d M_2(d)=-t_k,
sum_d d[M_1(d)+M_2(d)]=0.                            (4.3)
```

Their total variation is at most six because each source residual has three
components. Since `u_r(d)=O(1/d)`, every term with `d>n/2` contributes only
`O(1/n)` even after absolute values. Thus `(BR)` is equivalent to the
strictly one-dimensional lemma

> **SMALL-COMPONENT BOUNDARY RESPONSE `(SCBR)` (unresolved).**
>
> ```text
> |sum_(d<=n/2)[M_1(d)u_1(d)+M_2(d)u_2(d)]|=O(1/n).
> ```

The stronger projected-L1 form, putting an absolute value around each
already channel- and type-combined size coefficient, is a convenient
falsifiable sufficient condition. No channelwise absolute value is used.

## 5. Equivalent bounded boundary-incidence observable

Let `E_n` be the `n` polygon boundary transpositions. For a supported
rank-two product `t`, average over its literal ordered lifts:

```text
W(t)=1/a(t) sum_(ab=t)[1[a in E_n]+1[b in E_n]].     (5.1)
```

Then `0<=W<=2`. If

```text
H(s)=sum_i U_i,
```

the exact row identity is

```text
(bar K W)(s)=2H(s)/(n-3).                            (5.2)
```

It follows from `Q=eH-n-sum epsilon_i` and the exact kind transfer that

```text
eta(Q)=e eta(H)-t_k,

eta(H)=(n-3)/2[(bar K^2W)(B)-(bar K^2W)(A)].         (5.3)
```

Since `t_k=O(n^-2)`, `(BR)` is also equivalent to the single bounded-
observable estimate

```text
|(bar K^2W)(B)-(bar K^2W)(A)|=O(n^-2).               (BIR)
```

This is much narrower than two-step total variation: it asks only for the
predictive response of one explicit boundary-incidence statistic. It remains
unproved.

## 6. Dependencies and status labels

- **Accepted proved inputs:** M91's common-component cancellation and exact
  two-channel source law; M94/M100's raw Borel convolution; M102/M105's
  collision warning and topology scope correction; M155/M159's boundary
  condensation; M161/M166's literal fixed-cell convolution; M168/M171's
  phase collapse; M174/M178's exact affine response and PCS/BR equivalence.
- **Proved here:** sharp centers (3.1); decomposition (2.1); equivalence
  (2.2); exact coefficient formula (4.1)--(4.3); the `d>n/2` tail bound;
  and the boundary-incidence identities (5.1)--(5.3).
- **Exact finite only:** deterministic `k=3,5` coefficient checks.
- **Unresolved:** `(SCBR)`, `(BIR)`, `(BR)`, PCS-bound, FD-bound, FCL1,
  direct L1, every all-edge/H0/gap theorem, and both Terminals.

No external theorem or new dependency is used.

## 7. Exact falsification and calibration

`boundary_charge_check.py` reconstructs the two source laws from literal
ordered factors. It checks the full response and decomposition as
polynomials in a formal variable `E`, then evaluates at `E=e`. It also
checks (4.3), the small/large component split, (5.3), and frozen M174's
`eta(B_k)` values. Exact work is capped at `k=3,5`.

| `k` | `n eta(H)` | `n eta(Q)` | `n^2 Delta_W` | projected charge L1 times `n` |
|---:|---:|---:|---:|---:|
| 3 | 2.0725360 | 4.6737370 | 6.2176081 | 7.4808092 |
| 5 | 1.4820926 | 3.5438970 | 3.7052316 | 5.2546970 |

Here `Delta_W=(bar K^2W)(B)-(bar K^2W)(A)`. The large-component signed
charge times `n` is `.82607,.38102`, while the corresponding absolute value
is `.82607,.45338`; this only checks the proved tail decomposition at two
ranks. The reconstructed `eta(B_k)` values are exactly the frozen displays
`5.3716368,5.5840961` after formal computation.

No finite sign, decrease, boundedness, or limit is promoted.

## 8. First unproved step and strongest self-attack

The one-dimensional projection is an identity, not a bound. Neither the
moment cancellations (4.3) nor the `1/d` response alone forces `(SCBR)`:
a signed component measure with zero total size can still pair at constant
order with `1/d`. The finite projected-L1 values do not prove uniform
summability.

In particular, this mission does **not** prove that each fixed-small-size
coefficient is `O(1/n)`, or that such pointwise bounds have a summable
envelope. Those are exactly the remaining analytic tasks. A useful stronger
next target is

```text
sum_(d<=n/2)|M_1(d)u_1(d)+M_2(d)u_2(d)|<=C/n,        (8.1)
```

where both channels and run types have already been combined. This is
compatible with the collision warning because all lower-support strata are
inside `M_r(d)` before the absolute value.

## 9. Artifacts, command, hygiene, and final action

Owned artifacts are `plan.md`, `checkpoint.md`,
`boundary_charge_reduction.md`, `boundary_charge_check.py`,
`boundary_charge_results.json`, `results.json`, this report, and the freeze
files.

The retained deterministic command is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-42/mission-M180-fixed-cell-boundary-response/boundary_charge_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-42/mission-M180-fixed-cell-boundary-response/boundary_charge_results.json \
  --frozen-m174 experiments/20260811-polynomial-mixing-resolution/cycle-40/mission-M174-fixed-cell-pcs-bound/pcs_channel_exact.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`. No
network, package install, random input, broad quotient matrix, or computation
beyond exact `k=3,5` was used. No predecessor, coordinator, manuscript,
skill, goal, or shared project file was edited.

**Final action: keep and freeze the strict boundary-charge/one-dimensional
coefficient reduction; send it for fresh independent audit. Keep `(SCBR)`,
`(BIR)`, `(BR)`, and every downstream bound open.**
