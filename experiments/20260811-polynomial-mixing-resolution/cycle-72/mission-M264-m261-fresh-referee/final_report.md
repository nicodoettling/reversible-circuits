# M264 fresh immutable referee report on M261

Date: 2026-08-14 UTC.

Verdict: **ACCEPT**.

M261 proves an exact strict reduction of the balanced first fixed-cell
`FD-bound` to the phase-boundary variation lemma `(PBV)`. It does not prove
`(PBV)`, `FD-bound`, a minority-sign substitute, `FCL1`, a comparison gap,
polynomial mixing, or either Terminal. No material objection was found.

## 1. Immutable provenance gate

The SHA-256 digest of M261's `SHA256SUMS` is exactly

```text
b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b.
```

All nine files named there pass `sha256sum -c SHA256SUMS`. M261 was treated
as immutable. The predecessor provenance correction concerning M256's
transcription of M166's historical freeze-manifest hash is accurately
reported by M261 and is nonmaterial to this reduction.

## 2. Exact setting and completion coefficient

The audited target is the uniform law on minimal length-`n-1`
transposition factorizations of the ambient cycle, with `n=3k`, odd `k>=3`,
under the nonlazy cyclic rank-two quotient kernel. Permutations compose as
`(pq)(x)=p(q(x))`. This is not the uniform identity-word target and not the
lazy exact `{3,4,5}` heat-bath chain.

For a supported rank-two product `s`, put `q_s=s^{-1}h`. Its three residual
cycles have sizes `d_i`. A boundary edge `E_r=(r,r+1)` is generic precisely
when `s(r+1)=r+1`; then `q_s(r)=r+1`, so the edge is a directed adjacent edge
of one residual cycle. Let `chi_i(r)` record its owner and define

```text
C_ij(ell)=sum_(r mod n) chi_i(r)chi_j(r+ell).
```

The lag range `2<=ell<=n-2` makes the two polygon edges disjoint. Two generic
edges with the same owner replace `d_i` by `(1,1,d_i-2)`; two with distinct
owners replace `(d_i,d_j)` by `(1,d_i-1,1,d_j-1)`. Therefore, with invalid
sizes assigned zero,

```text
kappa_ii=tau(d_i-2)/tau(d_i),
kappa_ij=tau(d_i-1)tau(d_j-1)/[tau(d_i)tau(d_j)]  (i!=j).
```

Dividing `(n-5)! product tau(new size)` by
`A_s=(n-3)! product tau(d_i)` gives exactly

```text
R_ell(s)=1/[(n-3)(n-4)] sum_(i,j)kappa_ij C_ij(ell).
```

The ordered sum retains both cross-owner orientations. It covers all
same-cycle `IS/IN` and cross-cycle `X` completions for every supported
triangle and both double kinds. The triangle/double lift factor belongs to
the outer product law, not this conditional response, so M261 has no missing
factor two or three.

## 3. Endpoint derivative, sign, and bound

Direct subtraction gives

```text
C_ij(ell+1)-C_ij(ell)
 =sum_x chi_i(x-ell)[chi_j(x+1)-chi_j(x)].
```

Thus M261's sign and index are correct:

```text
E_ell(s)=sum_(i,j)kappa_ij sum_x
          chi_i(x-ell)[chi_j(x+1)-chi_j(x)],
R_(ell+1)-R_ell=E_ell/[(n-3)(n-4)].
```

At a fixed jump, at most one source owner `i` is active, and the weighted
change is the difference of two numbers in `[0,1]`. A triangle owner string
has at most six interval endpoints; a double has at most eight because its
three residual components consist of two one-run components and one two-run
component. Hence `|E_ell|<=8`. This uses only monotonicity of
`tau(d)`: `tau(d)/tau(d-1)=(d/(d-1))^(d-2)>=1`.

## 4. M91 two-channel Abel normalization

M91's complete source difference is

```text
eta=alpha_1(H_(1,B)-H_(1,A))
   +alpha_2(H_(2,B)-H_(2,A)).
```

Each `H` is a normalized ordered-pair product law. The `J=0` channel is
absent only because its two laws are literally the same. Conditioning the
designated exterior factor on its smaller split yields normalized measures
`Phi_(j,u),Psi_(j,u)` and the exact long/short chord laws `p_u,q_u`. With
`D_u=sum_(v<=u)(p_v-q_v)` and `D_(k-1)=0`, summation by parts gives

```text
H_(j,B)-H_(j,A)
 =sum_(u=1)^(k-2)D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_(u<k/2)q_u(Phi_(j,u)-Psi_(j,u)).
```

M91's all-`n` phase sum already accounts for the short orbit's repetitions,
so evaluating this identity on `R_ell` requires no extra stabilizer factor.
The exact fixed-target likelihood scale is

```text
Lambda_n=n^(n-3)/F_T
        =n^(n-3)/(n-2)^(n-4)
        =(n-2)(1-2/n)^(-(n-3)).
```

Consequently

```text
z_k(y)=Lambda_n[alpha_1 Xi_1(R_(y+1))
                   +alpha_2 Xi_2(R_(y+1))],
```

with both channels and triangle/double kinds inside the final absolute value.

## 5. Exact FD/PBV equivalence

Because `n=3k`, `Lambda_n=Theta(n)`, and
`(n-3)(n-4)=Theta(n^2)`, one has uniformly for odd `k>=3`

```text
k^2 Lambda_n/[(n-3)(n-4)]=Theta(n).
```

The lag correspondence is `ell=y+1`: summing adjacent differences over
`y=1,...,n-4` is exactly summing `ell=2,...,n-3`. Therefore M168's
`FD-bound`

```text
k^2 sum_y |z_k(y+1)-z_k(y)|=O(1)
```

is equivalent, with universal constants, to M261's unresolved statement

```text
sum_(ell=2)^(n-3)
 |alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)|=O(1/n).   (PBV)
```

The pointwise estimate `|E_ell|<=8` alone does not establish this signed
source cancellation.

## 6. Pointwise affine split

Let `b_s(r)=1[r+1 in supp(s)]`. Summing over owners gives

```text
sum_(i,j)C_ij(ell)
 =sum_r(1-b_s(r))(1-b_s(r+ell))
 =n-2|supp(s)|+I_ell(s),
```

where `I_ell=sum_r b_s(r)b_s(r+ell)`. Since support size is three for a
triangle and four for a double,

```text
sum_(i,j)C_ij(ell)=n-8+2 1_T(s)+I_ell(s).
```

Putting `rho_ij=e^2 kappa_ij-1` and
`Q_ell=sum_(i,j)rho_ij C_ij(ell)` proves the exact pointwise identity

```text
e^2(n-3)(n-4)R_ell
 =n-8+2 1_T+I_ell+Q_ell.
```

Only after applying the centered source law `eta(1)=0` may the constant be
removed. Adjacent subtraction also gives
`e^2E_ell=Delta I_ell+Delta Q_ell`. M261 correctly keeps collision and
decorated terms together.

## 7. Why accepted X_D/Y_D DV/DE does not cover E_ell

The accepted disjoint-profile theorems control cutoff counts of residual
components by size and by whether their support has one or two ambient runs:

```text
X_D=sum_(2<=d<=D)[N_1(d)+N_2(d)],
Y_D=sum_(2<=d<=D)N_1(d).
```

They vary the conditioned exterior split. By contrast, `E_ell` varies the
literal target phase and depends on individual jump positions, their cyclic
displacement, and the owner-pair coefficient `kappa_ij`. The cutoff profile
does not retain those data.

The clean-room check gives an exact witness inside the relevant `J=2`
support at `k=3`. The two products

```text
s_1=(0,2)(6,7),       s_2=(1,8)(6,7)
```

have the same complete residual component size/run profile
`((1,1),(2,1),(6,2))`, hence the same entire `X_D,Y_D` cutoff profile, but

```text
E_2(s_1)=-625/1296,   E_2(s_2)=-20/81.
```

Thus `E_ell` is not a function of the accepted profile even on the disjoint
channel. Reuse would require a new endpoint-profile representation and a
summable coefficient theorem. This is a scope obstruction, not a refutation
of PBV.

## 8. Independent exact checker

`check_pbv_reduction.py` imports and reads no M261 code or data. It rebuilds
the two source laws directly from minimal-factorization counts and checks
exactly at `k=3,5`:

- source-law normalization and accessible-product counts `30/51` and
  `360/716`;
- `alpha_0,alpha_1,alpha_2`, common-`J=0` cancellation, both live channel
  decompositions, split laws, and the measure-valued Abel identity;
- 10,104 raw circular-completion identities and 9,230 endpoint identities;
- the six/eight jump bounds and every affine incidence identity;
- direct-source, channel, and Abel evaluation agreement; and
- `V(z)=Lambda_n[(n-3)(n-4)]^-1 sum_ell|eta(E_ell)|`.

The retained deterministic command is

```text
python3 -B check_pbv_reduction.py
```

under Python `3.12.3`, standard library only, `seed=null`. `results.txt`
contains the output. These finite checks can falsify the displayed exact
formulas but cannot prove PBV or eventual positivity.

## 9. Numbered objections and scope

1. **Material objections:** none.
2. **Nonmaterial objections to M261:** none.
3. **Repository documentation note:** `AGENTS.md` names
   `references/experiments.md`, which is absent; the existing skill-owned
   `.codex/skills/reversible-circuit-sampler/references/experiments.md` was
   used. This does not affect M261.
4. **Scope guard:** ACCEPT covers only M261's exact strict PBV reduction and
   its observable-class obstruction. `(PBV)`, `FD-bound`, minority sign,
   `FCL1`, `A_k(1,1)=O(1)`, a spectral gap, polynomial mixing, and Terminal
   remain unresolved.

Final verdict: **ACCEPT M261 AS FROZEN.**
