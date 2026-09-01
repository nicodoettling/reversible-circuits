# M276 fresh immutable referee report on M272

Date: 2026-08-14 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict

```text
REJECT M272 AS A FROZEN SELF-CONTAINED PACKAGE.

MATERIAL OBJECTION: ITS CHANNEL-ONE BOUNDED-VARIATION PROOF OMITS THE
SHORT-CYCLE A-TAIL AND USES A FALSE BULK-COMPARABILITY CLAIM.

APPEND-ONLY SALVAGE: M276 PROVES THE MISSING TAIL BOUND AND THEREFORE THE
CHANNEL-ONE O(1/k) THEOREM, SUBJECT TO FRESH AUDIT OF THIS NEW PROOF.
```

M272's raw laws, full signed endpoint coupling, phase normalization,
phase partition/refutation, and channel-two triangle/vector Abel reduction
survive the audit.  `CSBV`, `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, and `FD`
remain open.  No downstream inference is licensed.

The scope is odd `k>=3`, `n=3k`, the balanced first fixed cell of the
auxiliary uniform minimal-long-cycle factorization law under the nonlazy
cyclic rank-two quotient kernel, with `(pq)(x)=p(q(x))`.  It is not the
global identity-word target or its lazy `{3,4,5}` heat-bath chain.

## 2. Provenance

M272's advertised checksum-file digest matches exactly:

```text
af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3.
```

Every M272 payload and every declared M91/M94/M261/M264/M267 dependency
payload passes.  The transitive M270 inventory and its acceptance of M267's
exact representation also pass.  Exact ledger digests are in
`checkpoint.md`.

## 3. Accepted exact M272 content

The clean-room derivation confirms:

- the first-factor law `nu_Q` and ordered-first-two law `N_Q`, including
  `sum_f N_Q(e,f)=nu_Q(e)`;
- normalized `H_(j,A/B)`, `p,q,Phi,Psi`, with channel two's fair exterior
  choice already inside `N_(C_-C_+)`;
- the monotone quantile coupling `S<=T` and exact crossing mass
  `Pr(S<=u<T)=-D_u`;
- the full path telescoping identity

  ```text
  eta(g)=sum_j alpha_j E_j[g(X_T)-g(Y_S)];
  ```

- the literal owner-charge normalization

  ```text
  sum_K<w,T_(K,ell)>
   =1/n sum_j alpha_j E_j[E_ell(X_T)-E_ell(Y_S)];
  ```

- the combined-channel good/bad first-edge partition and the exact
  refutation of seam-only cancellation;
- the channel-one collision identity before its BV estimate;
- channel two's `gamma_L,gamma_F`, total shared masses, triangle
  `O(1/k)` bound, nonzero disjoint endpoint, and vector Abel identity.

The coupling identity is an equality of expectations.  It provides no
pathwise order of the endpoint response.

## 4. Material frozen-proof objection

In `phase_incidence_lemma.md` Section 3, M272 claims that on
`k/2<a<=k` every Borel index in the face formula is comparable to `k` and
every summand is `O(k^-3/2)`.  The short-cycle term contradicts this:

```text
rho_A(k-1)=nu_k(1)
 =(k-1)^(k-3)/k^(k-2)=Theta(1/k).
```

M272's following displayed tail estimate applies only after `a>k`, where
`rho_A=0`; it does not literally cover the missing `A` tail.  Thus the
frozen proof does not establish its claimed channel-one BV proposition.
Under a strict immutable-package standard this objection is material even
though the theorem is repairable.

## 5. Append-only corrected channel-one theorem

The detailed proof in `proof_audit.md` sets `c=k-a` and treats

```text
rho_A(k-c)=g_k(c)=c nu_k(c)=c b_c R_k(c)/(k-1).
```

The same Borel ratio bounds used elsewhere give

```text
g_k(c)<=C/[k sqrt(c)],
|g_k(c+1)-g_k(c)|
 <=C/[k c^(3/2)]+C/[k^2 sqrt(c)].
```

Their sum, including the boundary at `c=0`, is `O(1/k)`.  Separating the
long-cycle `B` bulk from both small-complement tails then proves

```text
sum_a |Delta(rho_B-rho_A)(a)|=O(1/k).
```

The exact collision convolution and endpoint-intensity bounds consequently
give the corrected theorem

```text
sum_(ell=2)^(n-3)|eta_1(I_(ell+1)-I_ell)|=O(1/k).
```

This is an append-only M276 proof, not a retroactive repair of the frozen
M272 text.  It needs fresh audit before promotion.

## 6. Independent exact check

`independent_check.py` is self-contained, has no project imports, and reads
no predecessor or M272 artifact.  At the predeclared ranks `k=3,5` it
rebuilds minimal-factorization laws from cycle decompositions and verifies
all six groups of exact identities named in `checkpoint.md`.

At `k=3,ell=2`, it independently finds

```text
eta_good(E_2)=8042647144727/367569090000000 !=0.
```

Its phase good/bad norms and channel-two CSBV/CEBV/total norms make ten exact
matches to the frozen M272 values.  Separately rerunning both M272 checkers
at `k=3,5,7` to `/tmp` reproduces their frozen result arrays exactly.  These
are finite falsification/reproducibility facts only.

Retained clean-room command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-76/mission-M276-m272-fresh-referee/independent_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-76/mission-M276-m272-fresh-referee/independent_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`; no
network or nonstandard dependency.

## 7. Status ledger and exact stop

| Claim | Referee status |
|---|---|
| M272 inventory and dependency gate | verified |
| Raw laws and all channel normalizations | proved exact |
| `q`-to-`p`, `-D` crossing, full path telescoping | proved exact |
| Owner charge and outside `1/n` | proved exact |
| Phase partition; seam-only equality | proved / refuted exact |
| M272's written J1 BV proof | rejected: material gap |
| Corrected J1 collision derivative `O(1/k)` | proved in M276; fresh audit required |
| J2 shared triangles `O(1/k)` | proved |
| J2 endpoint and vector Abel identity | proved exact |
| `CSBV`, `CEBV`, `CIBV`, `DOR` | unresolved |
| `SET`, `PBV`, `FD`, `FCL1` | unresolved |
| gap, mixing, Terminal | unresolved |

Final action: **reject a plain immutable acceptance of M272; retain its exact
coupling/phase/J2 reductions; submit M276's corrected channel-one theorem for
fresh audit; make no downstream inference.**

