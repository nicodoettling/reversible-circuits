# M267 report: literal phase-endpoint transport reduction

Date: 2026-08-14 UTC.

## 1. Verdict, target, and scope

```text
VERDICT: STRICT EXACT ENDPOINT-PROFILE REDUCTION.
NEW UNIFORM STATEWISE ENDPOINT-L1 ENVELOPE: PROVED.
SET / PBV / FD-BOUND: UNRESOLVED.
MINORITY-SIGN SUBSTITUTE: UNRESOLVED.
```

For odd `k>=3`, `n=3k`, this mission concerns only the balanced first fixed
cell of the uniform minimal length-`n-1` factorization law of the long cycle
under M73's nonlazy cyclic rank-two quotient kernel.  Permutations compose as
`(pq)(x)=p(q(x))`; displayed factors multiply left-to-right.

This is not the uniform identity-word law and not the lazy exact
same-product `{3,4,5}` heat-bath chain.  No FCL1, gap, mixing, or Terminal
conclusion is inferred.

## 2. Immutable dependency verification

Every payload named in each required `SHA256SUMS` passes for M91/M94,
M161/M166, M168/M171, M256/M259, and M261/M264.  Their checksum-ledger
digests are respectively

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M161  17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166  344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168  3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171  c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M256  f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261
M259  c91571dbca9e1b7ebd8e014448530459bfade658168a76bac24b5a0ec4217aa2
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
```

The M166 freeze-manifest digest is the accepted corrected value
`a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498`.
No predecessor was edited.

The audited logical chain is: M91 supplies the normalized two-channel
measure-valued Abel identity; M161/M166 supplies the literal fixed-cell
score; M168/M171 isolates FD or minority sign; M256/M259 proves the
conditional chain stops at the independent FD/sign obligation; and
M261/M264 proves FD is exactly PBV and that accepted size/run cutoff profiles
do not determine its endpoint observable.  M94's signed-convolution warning
is respected: no channelwise or schemawise absolute value is used.

## 3. Strongest exact endpoint law

For a supported product `s`, let `o_s(r)` be the residual-cycle owner of the
generic edge `(r,r+1)`, with null owner at a support head.  Extend the exact
rooted-tree coefficient by `kappa(C,empty)=0`.  Then

```text
E_ell(s)=sum_(x mod n)
 [kappa_s(o_s(x-ell),o_s(x+1))
  -kappa_s(o_s(x-ell),o_s(x))].                     (3.1)
```

Only literal owner jumps contribute.  Equation `(3.1)` retains every
positive/negative one-run/two-run endpoint and the owner-pair coefficient;
it does not average away the lag.

Choose `x` uniformly and record the endpoint signature at
`x-ell,x,x+1`, including `T/D` kind, the full residual sizes, owner sizes,
null status, and equality pattern.  Let `Gamma_(nu,K,ell)` be this
phase-averaged signature law under a quotient law `nu`, and let `w` be the
charge in `(3.1)`.  Its exact normalization is

```text
nu(E_ell)=n sum_K <w,Gamma_(nu,K,ell)>.              (3.2)
```

Applying this linear profile map to all normalized M91 conditional laws
gives the adjacent-split and embedding differences

```text
A_(j,u,K,ell)=Gamma_(Phi_(j,u),K,ell)
              -Gamma_(Phi_(j,u+1),K,ell),
B_(j,u,K,ell)=Gamma_(Phi_(j,u),K,ell)
              -Gamma_(Psi_(j,u),K,ell),
```

and the signed endpoint transport tensor

```text
T_(K,ell)=sum_(j=1)^2 alpha_j {
 sum_u D_u A_(j,u,K,ell)+sum_(u<k/2)q_u B_(j,u,K,ell)}.
```

The literal M91 chord/completion formulas and all normalizers are displayed
in `endpoint_profile_representation.md`.  Both channels and both kinds are
summed before the scalar absolute value.  Exactly,

```text
alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)
 =eta(E_ell)=n sum_K <w,T_(K,ell)>.                  (3.3)
```

Thus PBV is reduced, with no hidden normalization, to the half-profile
signed transport lemma

> **`(SET)` (unresolved).**
>
> ```text
> sum_(ell=2)^((n-3)/2)
> |sum_K <w,T_(K,ell)>|=O(n^-2).
> ```

This is an exact transport/coupling interface: any couplings of adjacent
`Phi` laws and same-split `Phi/Psi` laws represent their profile difference
as the expected difference of literal endpoint signatures.  Proving `(SET)`
still requires summing the signed `D_u/q_u`, channel, kind, and endpoint
coefficients before absolute value.

## 4. New proved structural bounds

Symmetry of the owner-pair matrix gives pointwise

```text
E_ell(s)=-E_(n-ell-1)(s),
E_((n-1)/2)(s)=0.                                   (4.1)
```

This halves the PBV domain, including at the level of every product rather
than only after source averaging.

The owner sets are unions of at most two circular intervals.  For two such
sets, the lag correlation has total variation at most four times the smaller
set size.  Combining this with

```text
|e^2 kappa_ii-1|<=20/d_i,
|e^2 kappa_ij-1|<=20(1/d_i+1/d_j)
```

and M261's affine derivative proves uniformly for every supported product

```text
sum_(ell=2)^(n-3)|E_ell(s)|<=1232/e^2.              (4.2)
```

This is stronger than M261's pointwise `|E_ell|<=8` in the lag-summed
direction and rules out a hidden factor `n` in local endpoint coupling
errors.  It does not supply the required signed factor `1/n`: applying
`(4.2)` after total variation or separate Abel absolute values remains too
lossy.

## 5. Firewall and conditional sign route

M264's exact products

```text
s_1=(0,2)(6,7),       s_2=(1,8)(6,7)
```

have the same residual size/run profile `((1,1),(2,1),(6,2))` but

```text
E_2(s_1)=-625/1296,   E_2(s_2)=-20/81.
```

Their endpoint signatures differ, so the accepted `X_D,Y_D` cutoff
theorems cannot replace the tensor.

The tensor also isolates a possible but unresolved one-threshold statement:

```text
eta(E_ell)<=0 for 2<=ell<=k-2,
eta(E_ell)>=0 for k-1<=ell<=(n-3)/2.                (SR)
```

Conditional on `(SR)`, reflection and telescoping reduce PBV exactly to

```text
eta(R_2)+eta(R_((n-1)/2))-2eta(R_(k-1))=O(n^-3),   (TPR)
```

or equivalently the corresponding three fixed scores at scale `O(n^-2)`.
Neither `(SR)` nor `(TPR)` is proved.  No total-positivity/PF shortcut is
invoked.

## 6. Exact finite falsification

Only after the analytic profile and `(SET)` target were fixed,
`endpoint_profile_probe.py` was run.  It imports the checksum-validated M261
enumerator for the source law but implements `(3.1)` independently.

At `k=3,5`, it checks every supported rank-two product (336 and 3,185
products): the owner-jump vector equals M261's endpoint vector exactly,
reflection and central zero hold pointwise, and the maximum statewise `l1`
values are respectively `16/3` and
`20014594024/2357947691`, both below `(4.2)`.

For the complete signed source law:

| `k` | `n sum_ell|eta(E_ell)|` | first-half signs | sign changes |
|---:|---:|---|---:|
| 3 | 2.01300014 | `++` | 0 |
| 5 | 2.41867390 | `--+++` | 1 |
| 7 | 1.97841277 | `----++++` | 1 |
| 9 | 1.73708446 | `------+++++` | 1 |

The threshold in `(SR)` survives these exact finite ranks, but this is never
a sign proof.  More importantly, at `k=9` the separated first-half signs are

```text
J1-D: +++---+-+++
J2-T: ------++---
J2-D: ------++-++
```

while their required combination is `------+++++`.  Thus even this finite
candidate depends on the channel/kind cancellation that `(3.3)` preserves.

Retained deterministic command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-73/mission-M267-phase-endpoint-pbv/endpoint_profile_probe.py --output experiments/20260811-polynomial-mixing-resolution/cycle-73/mission-M267-phase-endpoint-pbv/endpoint_profile_results.json
```

Python `3.12.3`; standard library only; `seed=null`; no nonstandard
dependency.  The finite data can falsify formulas or sign candidates but
cannot prove PBV, `(SR)`, or asymptotic positivity.

## 7. Status ledger and strongest self-attack

```text
dependency inventories                                      verified
literal owner-jump law and phase-profile normalization      proved
two-channel/T-D signed endpoint transport tensor             proved
pointwise reflection and central zero                        proved
uniform statewise endpoint-vector l1 envelope                proved
M264 cutoff-profile firewall                                 proved scope obstruction
k=3,5,7,9 threshold pattern                                  exact finite only
SET / PBV / FD-bound                                         unresolved
SR, TPR, minority sign, FCL1                                 unresolved
```

The representation is not itself an estimate.  The statewise bound is only
`O(1)`; applying it after absolute source mass or the `Theta(sqrt(k))` Abel
coefficient mass misses the target.  No literal coupling has yet proved the
extra signed `1/n` gain.  The one-threshold pattern occurs only after
irregular channel/kind pieces cancel, so generic variation-diminishing
claims would be unjustified.

## 8. Final action and hygiene

**KEEP AND FREEZE THE EXACT ENDPOINT-PROFILE/REFLECTION/STATEWISE-VARIATION
REDUCTION; REQUEST A FRESH IMMUTABLE AUDIT.**  The referee should check the
outside factor `n` in `(3.2)--(3.3)`, the short-orbit phase normalization,
the T/D conditional-law formulas, the reflection indices, the constants in
`(4.2)`, and the conditional `(SR)=>(TPR)` telescoping.

M267 changed only its owned mission directory.  It installed no package,
used no network, and made no commit or push.

