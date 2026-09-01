# M264 checkpoint 0 — pre-inspection

Status: `in progress`.

The mission directory and audit plan were initialized before inspecting M261.
No claim from the target artifact has yet been used beyond the assignment's
explicit checklist and advertised top digest.

## Provenance gate

The assigned M261 directory is
`cycle-71/mission-M261-fixed-cell-fd`. Its `SHA256SUMS` validates all nine
named files, and the SHA-256 digest of that checksum file is exactly

```text
b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b.
```

The repository-level path `references/experiments.md` named by `AGENTS.md`
does not exist. The existing skill-owned file
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was read
instead; this path mismatch will be reported as nonmaterial repository
documentation drift.

## Clean derivation before opening M261

Use the accepted fixed-cell convention: `n=3k`, odd `k>=3`,
`h=(0 1 ... n-1)`, `E_r=(r,r+1)` modulo `n`, and target lag
`ell=y+1 in {2,...,n-2}`. For a supported rank-two intermediate product
`s`, let `q=s^{-1}h` have three cycles `C_1,C_2,C_3` of sizes `d_i`.
Write

```text
chi_i(r)=1{E_r is generic for s and belongs to C_i},
C_ij(ell)=sum_(r mod n) chi_i(r)chi_j(r+ell),
R=(n-3)(n-4).
```

A generic boundary edge cuts one singleton from its owner cycle. Thus two
disjoint generic edges in different owners `i!=j` give the normalized
completion ratio

```text
kappa_ij=tau(d_i-1)tau(d_j-1)/[tau(d_i)tau(d_j)],
```

whereas two in the same owner give

```text
kappa_ii=tau(d_i-2)/tau(d_i).
```

Invalid sizes have coefficient zero. This applies to every supported
oriented-triangle intermediate and both supported double kinds. Since
`F_(n-3)(q)=(n-3)! product_i tau(d_i)`, the corresponding completion has
`(n-5)!` in place of `(n-3)!`; hence the exact all-phase normalized response
must be

```text
R_ell(s)=R^-1 sum_(i,j) kappa_ij(s) C_ij^s(ell).       (A)
```

No lift factor enters `(A)`: the triangle/double lift multiplicity belongs
to the law of the intermediate product, while `(A)` is the conditional
target response at a fixed product.

For the endpoint derivative, put

```text
E_ell(s)=sum_(x mod n) sum_(i,j)
          chi_i(x-ell) kappa_ij(s)[chi_j(x+1)-chi_j(x)].   (B)
```

Changing variables `x=r+ell` gives, with the sign and index visible,

```text
C_ij(ell+1)-C_ij(ell)
 =sum_x chi_i(x-ell)[chi_j(x+1)-chi_j(x)],
R_(ell+1)-R_ell=E_ell/R.                              (C)
```

At a fixed `x`, the bracket in `(B)` changes from no owner to one owner,
one owner to none, or one owner to another, so its `kappa`-weighted
contribution has absolute value at most one. Owner can change only next to
a non-generic boundary edge. A triangle has three non-generic heads and a
double has four, so the circular owner string has at most respectively six
or eight jump positions. Consequently

```text
|E_ell(s)|<=8.                                        (D)
```

Here `0<=kappa_ij<=1`: with
`tau(d)=d^(d-2)/(d-1)!`, `tau(d)/tau(d-1)=(d/(d-1))^(d-2)>=1`.

M91's already accepted two-channel identity says

```text
eta=alpha_1(H_(1,B)-H_(1,A))+alpha_2(H_(2,B)-H_(2,A)),
H_(j,B)-H_(j,A)
 =sum_u D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_v q_v(Phi_(j,v)-Psi_(j,v)).                    (E)
```

Every measure in `(E)` is normalized, and the `J=0` channel is absent only
because its two conditional laws are literally equal. For any observable
`F`, denote the two bracketed evaluations by `Xi_j(F)`. Detailed balance
and M91's phase repetition give

```text
z_k(y)=Lambda[alpha_1 Xi_1(R_(y+1))
                 +alpha_2 Xi_2(R_(y+1))],
Lambda=n^(n-3)/F_T.                                  (F)
```

For the fixed target residual `(1,1,n-2)`,
`F_T=(n-2)^(n-4)`, so

```text
Lambda=n[n/(n-2)]^(n-4)=Theta(n),
k^2 Lambda/R=Theta(n).                               (G)
```

Combining `(C)` and `(F)` shows that the unresolved FD bound is equivalent,
up to universal constants, to

```text
sum_(ell=2)^(n-3)
 |alpha_1 Xi_1(E_ell)+alpha_2 Xi_2(E_ell)|=O(1/n).    (PBV)
```

Finally, let `T(s)` indicate triangle kind and let `H(s)` be the set of
non-generic heads. Because `|H|=3` for triangles and `4` for doubles,

```text
sum_(i,j)C_ij(ell)
 =|H^c intersect (H^c-ell)|
 =n-8+2 1_T(s)+I_ell(s),
I_ell=|H intersect (H-ell)|.
```

Putting `rho_ij=e^2 kappa_ij-1` and
`Q_ell=sum_(i,j)rho_ij C_ij(ell)` into `(A)` gives the exact pointwise affine
split

```text
e^2 R R_ell=n-8+2 1_T+I_ell+Q_ell.                  (H)
```

The accepted `X_D,Y_D` DV/DE theorems cannot simply be substituted into
`(PBV)`: they control expectations of cutoff counts of final residual
components classified only by size and by one/two ambient runs while varying
the conditioned split size. In contrast, `E_ell` is a phase derivative at
a fixed intermediate product and retains the literal positions of individual
owner jumps, the displacement `ell`, and the owner-pair weights `kappa_ij`.
Those data are not measurable from the `X_D,Y_D` cutoff profiles. A new
representation theorem would be needed; the existing bounds alone do not
provide one.

## Comparison with frozen M261

Only after the derivation above was fixed, M261's
`phase_difference_reduction.md`, `report.md`, dependency audit, and freeze
manifest were opened. Equations `(2.2)--(2.3)`, `(3.2)--(3.8)`, and
`(4.1)--(4.5)` agree with `(A)--(H)` above, including:

- same-owner `tau(d_i-2)/tau(d_i)` versus cross-owner
  `tau(d_i-1)tau(d_j-1)/(tau(d_i)tau(d_j))`;
- the ordered cross-owner sum and retention of every `IS/IN/X` response;
- the positive endpoint difference
  `chi_i(x-ell)[chi_j(x+1)-chi_j(x)]`, not its negative or a shifted
  `x+ell` version;
- the lag ranges `2<=ell<=n-2` for responses and
  `2<=ell<=n-3` for differences;
- normalized M91 channel measures, source-independent `alpha_j`, and the
  absence of `J=0` only through literal cancellation;
- `Lambda_n=n^(n-3)/(n-2)^(n-4)` and the consequent
  `k^2 Lambda_n/[(n-3)(n-4)]=Theta(n)`; and
- the centered-law deletion of the constant `n-8` only after the pointwise
  affine identity has been established.

No hidden target lift, orbit-size, or factor-three correction is missing.
M91's all-`n` phase repetition has already put the short triangle orbit on
the same raw normalization as the full orbit before the fixed target factor
`F_T` is divided out.

## Independent exact falsification

`check_pbv_reduction.py` reads and imports no M261 artifact. It enumerates
the first two ordered residual factors from minimal-factorization counts,
retaining triangle lift three and double lift two automatically. At `k=3,5`
it verifies exactly:

- both complete source laws normalize;
- the three `J` masses equal the M91 `alpha_j` and the `J=0` laws agree;
- conditioning on the first exterior split yields the exact long-cycle
  `p_u` and short-cycle `q_u` laws in both live channels;
- the measure-valued two-channel Abel identity holds product by product;
- every raw circular completion equals `(A)`;
- every adjacent raw response equals `(B)/R` with the asserted sign/index;
- triangle/double jump counts are at most six/eight and `|E_ell|<=8`;
- the exact affine incidence identity underlying `(H)` holds pointwise;
- direct source evaluation, channel evaluation, and Abel evaluation agree;
  and
- `V(z)=Lambda R^-1 sum_ell|eta(E_ell)|` exactly.

The retained command was

```text
python3 -B check_pbv_reduction.py
```

under Python `3.12.3`, standard library only, deterministic, `seed=null`.
The raw output is `results.txt`. The finite values reproduce the advertised
`k=3,5` calibration, but they prove neither PBV nor a sign theorem.

Current audit verdict: no material mathematical objection found. Final
freeze remains pending a last provenance check and repository hygiene pass.
