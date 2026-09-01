# M261 report: exact fixed-cell phase-boundary reduction

Date: 2026-08-14 UTC.

## 1. Verdict, target, and scope

```text
VERDICT: STRICT EXACT REDUCTION.
FD-BOUND: UNRESOLVED.
MINORITY-SIGN SUBSTITUTE: UNRESOLVED.
```

For odd `k>=3`, `n=3k`, this mission concerns only M161/M168's balanced
first fixed cell under the uniform minimal length-`n-1` factorization law of
the long cycle and M73's nonlazy cyclic rank-two kernel. Permutations compose
as `(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.

This is not the uniform identity-word law or the lazy exact same-product
`{3,4,5}` heat-bath chain. No full DV, FCL1, gap, mixing, or Terminal
conclusion is used or inferred.

## 2. Immutable dependency result

Every declared payload in M161/M166, M168/M171, M174/M178, and M256/M259
passes `sha256sum -c SHA256SUMS`. Exact checksum-ledger and freeze-manifest
digests are recorded in `dependency_audit.md`.

The sole discrepancy is the already-refereed nonmaterial transcription of
M166's historical freeze-manifest hash in M256. The actual value

```text
a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498
```

agrees with M259. No predecessor was edited.

## 3. Strongest proved result

For a supported first-pair product `s`, let `q_s=s^-1h`, and let
`chi_i^s(r)` indicate that the polygon edge `E_r=(r,r+1)` is a generic
directed edge of residual component `i`. With the exact rooted-tree ratios

```text
kappa_ii=tau(d_i-2)/tau(d_i),
kappa_ij=tau(d_i-1)tau(d_j-1)/[tau(d_i)tau(d_j)]  (i!=j),
```

the literal target response at lag `ell` is exactly the circular coefficient

```text
R_ell(s)=1/[(n-3)(n-4)]
 sum_(i,j) kappa_ij sum_r chi_i(r)chi_j(r+ell).
```

This includes all `IS/IN/X` second-row topologies. The signed source law is

```text
eta=P_B-P_A
   =alpha_1(H_(1,B)-H_(1,A))
    +alpha_2(H_(2,B)-H_(2,A)),
```

where the normalized ordered-factor laws retain their triangle/double
mixtures. Therefore both channels and both kinds are summed before every
absolute value.

Taking one literal phase difference converts the length-`Theta(n)`
correlation into the endpoint observable

```text
E_ell(s)=sum_(i,j)kappa_ij
 sum_x chi_i(x-ell)[chi_j(x+1)-chi_j(x)],
|E_ell(s)|<=8.
```

Writing M91's exact Abel law evaluated on this observable as `Xi_(j,ell)`,

```text
z_k(y+1)-z_k(y)=Lambda_n/[(n-3)(n-4)]
 [alpha_1 Xi_(1,y+1)+alpha_2 Xi_(2,y+1)],

Lambda_n=(n-2)(1-2/n)^(-(n-3)).
```

Since `k^2 Lambda_n/[(n-3)(n-4)]=Theta(n)`, FD-bound is exactly equivalent
to the standalone coefficient lemma

> **Phase-boundary variation `(PBV)` (unresolved).**
>
> ```text
> sum_(ell=2)^(n-3)
> |alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)|=O(1/n).
> ```

This is the strictest reduction: it is an `l1` estimate for a uniformly
bounded jump-endpoint observable, with the exact phase, both channels, and
both kinds retained.

## 4. DV/DE observable-class obstruction

The accepted DE theorem and the proved Y clause of DV apply only to the
literal cumulative component-count observables

```text
X_D=sum_(2<=d<=D)[N_1(d)+N_2(d)],
Y_D=sum_(2<=d<=D)N_1(d).
```

The remaining X clause of full DV is itself still conditional. Even granting
full DV, these theorems do not act on `E_ell`: `X_D,Y_D` depend only on
component size and whether its support has one or two ambient runs, whereas
`E_ell` retains the literal displacement between individual jump endpoints
and the owner-pair weight `kappa_ij`.

In particular, `N_2(d)` records only the total size `d=a+b` of a two-run
component. It forgets the separate run lengths and seam positions that occur
in

```text
chi_i(x-ell)[chi_j(x+1)-chi_j(x)].
```

Thus `E_ell` is not measurable with respect to the accepted
`(N_1(d),N_2(d))` profile, and there is no licensed substitution into the
existing DV/DE estimates. A new observable theorem is required: either
direct PBV control for the endpoint coefficient or an exact representation
of every `E_ell` by an enlarged run-endpoint profile with a summable
coefficient norm. This is an obstruction to reusing the accepted theorem,
not a refutation of PBV.

## 5. Pointwise affine and collision refinement

Let `b_s(r)=1[r+1 in supp(s)]` and
`I_ell(s)=sum_r b_s(r)b_s(r+ell)`. Thus `I_ell` is the sparse ordered
moved-vertex collision profile. With

```text
rho_ij=e^2 kappa_ij-1,
Q_ell=sum_(i,j)rho_ij C_ij(ell),
```

the response has the exact pointwise affine form

```text
e^2(n-3)(n-4)R_ell(s)
 =n-8+2 1[kind(s)=T]+I_ell(s)+Q_ell(s).
```

Applying the complete centered source law gives

```text
z_k(ell-1)=Lambda_n e^-2/[(n-3)(n-4)]
 [2eta(T)+eta(I_ell)+eta(Q_ell)],

eta(T)=12(k-1)/[3k(3k-4)(2k-1)]>0.
```

This simultaneously exposes the exact positive kind baseline relevant to
the minority-sign route and the exact FD coefficient

```text
eta(Delta I_ell+Delta Q_ell).
```

Neither collision nor the decorated remainder may be dropped or
triangle-bounded at the target conclusion without a new proof.

## 6. Exact finite falsification

`pbv_exact.py` independently enumerates the first two ordered source
factors, classifies `J=0,1,2` and triangle/double before subtraction,
constructs `E_ell` from literal generic-edge jumps, and only afterward reads
frozen M161 scores. It verifies every adjacent score exactly.

| `k` | accessible products A/B | `n sum|eta(E_ell)|` | `k^2 V(z_k)` | `k min(P_k,N_k)` |
|---:|---:|---:|---:|---:|
| 3 | 30 / 51 | 2.01300 | 2.12172 | 0 |
| 5 | 360 / 716 | 2.41867 | 2.21091 | 0 |
| 7 | 1638 / 3459 | 1.97841 | 1.73663 | 0 |

The collision/decorated-remainder separate values of `n` times their
variation are respectively

```text
k=3:  6.02880, 10.40803
k=5:  6.62897, 12.12517
k=7:  6.72848,  9.15365.
```

Their inflation relative to the combined column is finite evidence that the
exact signed combination matters. The three zero minority masses say only
that frozen scores are positive at these ranks. Neither table proves a
uniform bound or sign theorem.

Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-71/mission-M261-fixed-cell-fd/pbv_exact.py --k 3 5 7 --frozen-m161 experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M161-fixed-boundary-cell-score/fixed_cell_results.json --output experiments/20260811-polynomial-mixing-resolution/cycle-71/mission-M261-fixed-cell-fd/pbv_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`; no
nonstandard dependency.

## 7. Status ledger and first unproved lemma

```text
literal circular phase coefficient and normalization       proved
generic interval endpoint derivative, |E_ell|<=8           proved
two-channel Abel evaluation and FD <=> PBV                 proved
pointwise kind/collision/decorated separation              proved
existing DV/DE does not cover the endpoint observable     proved scope obstruction
k=3,5,7 reconstruction and positivity                      exact finite only
PBV / FD-bound                                             unresolved
minority-sign bound                                        unresolved
FCL1 and A_k(1,1)=O(1)                                    unresolved
```

The first standalone lemma is exactly `(PBV)`. A viable proof must control
the combined signed coefficient at `O(1/n)`; the uniform pointwise bound
`|E_ell|<=8` alone loses the required source cancellation.

## 8. Final action and hygiene

**KEEP AND FREEZE THE STRICT PHASE-BOUNDARY/COLLISION REDUCTION; REQUEST A
FRESH IMMUTABLE AUDIT.** The referee should check the completion-ratio
normalization, endpoint sign/index shift, the factor
`k^2 Lambda_n/R_n=Theta(n)`, and retention of both channels/kinds.

M261 changed only its owned mission directory. It installed no package, used
no network, and made no commit or push.
