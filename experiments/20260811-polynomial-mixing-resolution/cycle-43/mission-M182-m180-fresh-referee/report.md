# M182 report: fresh referee of immutable M180

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
VERDICT: ACCEPT M180.
MATERIAL OBJECTIONS: 0.
NONMATERIAL EXPOSITION QUALIFICATIONS: 2.
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` for odd
`k>=3`, and sources

```text
A=(0,k,2k),                    B=(0,1)(k,2k).
```

The target is the uniform minimal-factorization law of the long cycle and
the operator is M73's nonlazy cyclic rank-two coordinate kernel. This audit
does not concern the global identity-word law or its local heat-bath chain.
It accepts only M180's strict reductions. `(SCBR)`, `(BIR)`, `(BR)`,
PCS-bound, every gap/mixing claim, and both Terminals remain unresolved.

## 2. Immutable-input verification

M180 was not edited. Before any conclusion, its checksum manifest passed for
all eight artifacts. Recomputed top-level hashes exactly matched the supplied
values:

```text
report       9054e112dbecc7151560f5f52aebf7d4556140805193a1757c152e6c13ef50ad
proof        99e55f6a5484cf3b4a6e1c6831d0f869f8a441d74de43d9c35abcea56933d5d0
manifest     3355c8c5a9bd1fb2518c20de31a711c2f8ea14d4bdb4d13d0a443f035f7f4a03
SHA256SUMS   b362d629eaae627432efb3d6de97a825ed1bb17c0ca17ffb39c342db5c9d76d6
```

The source-of-truth project files, complete project skill, sampling and
experiment references, and relevant accepted predecessor definitions were
read before the audit.

## 3. Ratio coefficient and sharp centers

Writing `x=1/d`, clean-room expansion gives

```text
log(e^2 tau(d-2)/tau(d))=3x+(17/6)x^2+O(x^3).
```

Therefore the quadratic coefficient after exponentiation is

```text
17/6+3^2/2=22/3,
```

not a truncated alternative. The corresponding exact centers are

```text
u_1(d)=  7/(24d)+O(d^-2),
u_2(d)=-29/(24d)+O(d^-2),
v_1(d)=-5/3+O(d^-1),
v_2(a,b)=1/3-2(1[a=1]+1[b=1])+O(d^-1).
```

The logarithmic-series remainder is uniform for `d>=3`; the finitely many
zero-shift cases are bounded directly. This proves the uniform estimates
needed below for every positive two-run split.

## 4. Exact decomposition and uniform remainder

Starting from M174's exact response with the already accepted pointwise
constants `L_T=0,L_D=-2`, independent expansion yields

```text
B_k(s)=2nQ(s)-7/2-2I_D(s)+R(s),
Q(s)=sum_i u_i,

R=sum_i w_i-2sum_i d_i u_i
  +2sum_(i<j)(epsilon_i u_j+epsilon_j u_i+u_i u_j),
```

where `w_1=v_1+5/3` and `w_2=v_2-1/3+2I_D`. The triangle and double
constant calculations both give the common `-7/2`, with the double retaining
`-2I_D` exactly.

The sharp centers imply `u_i=O(1/d_i)` and `w_i=O(1/d_i)`. Hence every
`d_i u_i`, epsilon cross term, product, and small-size term in `R` is
uniformly bounded. Because `eta=P_B-P_A` has zero mass and bounded signed
variation while `0<=I_D<=2`, this proves both directions of

```text
eta(B_k)=O(1)  iff  n eta(Q)=O(1).
```

## 5. Raw signed coefficient, moments, and tail

The raw first-row identity is

```text
eta(s)=a(s)delta_k(s)/R_n,
R_n=(n-3)(n-4).
```

Thus M180's

```text
M_r(d)=R_n^-1 sum_s a(s)delta_k(s)N_r(d;s)
```

is exactly the signed component-count pushforward, after the full source
contrast has been formed. Fubini gives

```text
eta(Q)=sum_d[M_1(d)u_1(d)+M_2(d)u_2(d)].
```

If `t_k=eta(T)`, triangle component counts `(3,0)`, double counts `(2,1)`,
zero signed mass, and total residual size `n` give exactly

```text
sum_d M_1(d)=t_k,
sum_d M_2(d)=-t_k,
sum_d d[M_1(d)+M_2(d)]=0.
```

There are three components per state and `sum_s|eta(s)|<=2`, so
`sum_(r,d)|M_r(d)|<=6`. Therefore, for `d>n/2`,

```text
sum |M_1u_1+M_2u_2| <= (2C/n)sum_(r,d)|M_r(d)|=O(1/n).
```

This verifies only the large-component tail. No attempt was made to prove
the remaining small-component lemma `(SCBR)`.

## 6. Boundary incidence and exact BIR equivalence

For M180's ordered-lift boundary statistic `0<=W<=2`, a generic boundary
edge in a residual size-`d` component has completion ratio

```text
1/(n-3) * tau(d-1)/tau(d).
```

The one- and two-run components have respectively `d-1` and `d-2` such
edges. Thus the first factor's boundary probability is `H/(n-3)`, where
`H=sum_i U_i`. The second position has the same marginal because the sum of
all transpositions is central. Hence, exactly on cyclic orbits,

```text
(bar K W)(O_s)=2H(s)/(n-3).
```

Also

```text
eta(Q)=e eta(H)-t_k,
eta(H)=(n-3)/2[(bar K^2W)(O_B)-(bar K^2W)(O_A)].
```

Since the accepted exact formula makes `t_k=O(n^-2)`, the already proved
`BR iff n eta(Q)=O(1)` is equivalent in both directions to

```text
|(bar K^2W)(O_B)-(bar K^2W)(O_A)|=O(n^-2).
```

This verifies the reduction to BIR, not BIR itself.

## 7. Independent falsification and exact calibration

`cleanroom_boundary_audit.py` was written from the definitions and imports
no M180 code or data. It uses literal permutations, exact `Fraction`
completion counts, and formal degree-two polynomials in `E`; it is hard-capped
at `k=3,5`. All assertions passed.

It checked raw source normalization and delta normalization, residual run
classification, the full response/decomposition, component moments, and the
literal ordered-lift `KW` identity on 64 and 810 source-accessible states.
Post-check displays were:

| `k` | `n eta(H)` | `n eta(Q)` | `n^2 Delta_W` | `eta(B)` |
|---:|---:|---:|---:|---:|
| 3 | 2.0725360 | 4.6737370 | 6.2176081 | 5.3716368 |
| 5 | 1.4820926 | 3.5438970 | 3.7052316 | 5.5840961 |

These agree with M180 but are only finite exact calibration. No sign,
monotonicity, limit, or uniform asymptotic bound is inferred.

## 8. Numbered objections, dependencies, and first open step

1. **Material objections: none.** All five assigned proof-critical claims
   survive clean-room derivation and exact falsification.
2. **Nonmaterial notation qualification.** M180 sometimes supplies a raw
   representative as the argument of `bar K`; formally the argument is its
   cyclic orbit. Because `W` and `H` are invariant, the expressions are
   unambiguous and no identity changes.
3. **Nonmaterial small-size qualification.** The zero convention for invalid
   shifted `tau` indices is invoked after the decoration displays. Repeating
   it beside those displays would improve self-containment; the finite cases
   are correct and uniformly harmless.

Proved dependencies used are M73's exact rank-two kernel, M91's complete
two-channel signed row/common-channel cancellation, M94/M100's raw Borel
normalization, and M174/M178's exact response and kind transfer. No external
theorem is added. The first open step remains exactly `(SCBR)`, equivalently
`(BIR)` and `(BR)` under the accepted identities.

## 9. Artifacts, command, hygiene, and final action

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`cleanroom_boundary_audit.py`, `cleanroom_results.json`, `results.json`, this
report, and the freeze files.

Retained deterministic command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-43/mission-M182-m180-fresh-referee/cleanroom_boundary_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-43/mission-M182-m180-fresh-referee/cleanroom_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`. No
network, package installation, broad matrix computation, `k=7`, SCBR attempt,
or finite-sign inference was used. Final action: **accept and freeze M180's
strict reduction, with the two qualifications above; keep every named open
bound unresolved.**
