# M292 fresh immutable proof audit of frozen M289

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
VERDICT: ACCEPT M289 AS FROZEN.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL OBJECTIONS: NONE.
```

M289 proves, for every odd `k>=3`, only the auxiliary channel-two embedding
bounded-variation statement

```text
||sum_(1<=s<k/2) qhat_s(Phi_s^D-Psi_s^D)||_1=O(1/k),
qhat_s=q_s a_F(s).
```

The setting is the balanced first fixed cell of the auxiliary uniform
minimal-factorization law, with `(pq)(x)=p(q(x))` and displayed factors
multiplied left-to-right.  This is not the global fixed-length identity-word
law and not the lazy exact same-product `{3,4,5}` heat-bath chain.

This audit does not promote or infer `CIBV`, `DOR`, `SET`, `PBV`, `FD`,
`FCL1`, a bridge/local spectral gap, polynomial mixing, or Terminal A/B.
M276/M279 record a separate exact implication `CSBV+CEBV => CIBV`; applying
that implication is a coordinator synthesis step, not a claim of this
CEBV-only referee package.

## 2. Immutable gate and provenance

The independently computed SHA-256 digest of M289's checksum file is exactly

```text
327176968d69eb447ff862354eb566ed00cfd2c56b2e77079231bcc077f93680.
```

The directory contains exactly the following nine frozen payloads and
`SHA256SUMS`, with no unmanifested payload:

```text
plan.md
checkpoint.md
cebv_coefficient_reduction.md
cleanroom_cebv_check.py
cleanroom_results.json
report.md
run_manifest.md
audit_request.md
freeze_manifest.md
SHA256SUMS
```

Every payload passes `sha256sum -c SHA256SUMS`.  The key frozen hashes are

```text
proof       a1b8cdd5e4b2ba572a67ba05db6cccf1ac72afda597d63847fd9778d15b2fe72
checker     ea339c11ec6e4ba1640ccfef6be970e2285f2ff678c7d80a24e6e782df320545
results     38c6f6deecd5beb83c8a5703253736fb728bdf3cf23b38902af945a92577e04b
report      493ee080fc93731947b319a08f5b46ca3bb9638582eabe4a93de5f78b5bd0817
freeze      c0b0e5ceb8d32224269d6c4c4a0d9d7d6a12dff1205b0df18b8dd4756722797e
```

Every payload in every cited predecessor ledger also passes.  The checksum
file digests independently obtained are

```text
M192 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
M195 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a
M199 1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed
M207 817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688
M276 882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M279 3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66
M282 cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7
M286 3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a
```

M226/M229 are background only and are not imported into M289's argument.
The mathematical dependency actually used here is the accepted M276/M279
CEBV interface plus elementary minimal-completion and Borel identities; the
M282/M286 one-component proof is independently generalized below.

## 3. Independent raw-law reconstruction

Put

```text
n=3k,  D=2k-1,  R=2k-3,  j=(k-1)/2,
b_r=e^(-r)r^(r-1)/r!,
K_R(r,x)=b_x b_(r-x)/(R b_r).
```

For a residual permutation `Q` of rank `r`, exact minimal-completion
counting gives

```text
F_r(Q)=r! product_i tau(d_i),
N_Q(e,f)=F_(r-2)((ef)^(-1)Q)/F_r(Q),
tau(d)=d^(d-2)/(d-1)!.
```

After a first chord, a residual component of size `r` is selected with rank
weight `(r-1)/R`; a specified internal chord of split `x` has raw weight
`K_R(r,x)`.  Avoiding the marked endpoint has mass

```text
h(r)=(r-1)(r-2)/(rR).
```

At directed ordinary separation `x`, the ordered second-edge endpoints and
the four directed first/second pairs in one orientation have respective raw
coefficients

```text
1[x<=r-2](r-x-1)K_R(r,x),
4(r-1)/(rR)-2K_R(r,x).
```

Their sum is M289's `U_r(x)`.  Adding `U_r(M-x)` retains the reverse
orientations.  Each disjoint outcome then contributes two ordered first-edge
pairs and ten other ordered pairs, so the B law for a fixed split has exactly

```text
beta_s(d)=a_L(s)1[min(d,D-d)=s]
          +Z_(D,s)(min(d,D-d))+Z_(D,D-s)(min(d,D-d)),
sum_d beta_s(d)=12a_L(s).
```

No factor two is missing: the two `Z` rows correspond to the two residual
components, while each `Z` already contains both directed orientations.

On the A side, the marked components give `Z_(k,s)+Z_(k,k-s)`.  Selecting
the untouched `k`-cycle has mass `u=(k-1)/R`; its ordered second-edge
coefficient is

```text
T_k(d)=kK_R(k,d),       sum_d T_k(d)=2u.
```

For fixed `x` in the active block and `y` in the untouched block, the
endpoint intensities are `2/k` and `2u/k`.  The fair active-block choice
halves each orientation and the reversed active-block choice restores it.
Thus, with

```text
N_l=#{(x,y) in C_0 x C_2:y-x=l mod n},
M_l=N_l+N_(n-l),
```

the exact cross coefficient is

```text
X_k(l)=4uM_l/k^2,             sum_l X_k(l)=8u.
```

Consequently

```text
mass(mathcal B_s)=12a_L(s),
mass(mathcal A_s)
 =2a_F(s)+10[h(s)+h(k-s)]+2u+8u
 =12a_F(s).
```

This independently establishes M289 `(2.3)--(2.9)`, including ordered
factors, product kind, and support-pair multiplicity.

## 4. Subprobability normalizer and exact collapse

The accepted shared-endpoint mass identity gives

```text
sum_s qhat_s=sum_s q_s a_F(s)
 =1-3(k-2)/(kR)<1.
```

Thus `qhat` is genuinely a subprobability and is never normalized again.
Since `Phi_s^D=mathcal B_s/a_L(s)` and
`Psi_s^D=mathcal A_s/a_F(s)`, direct substitution gives

```text
H=sum_s q_s[(a_F/a_L)mathcal B_s-mathcal A_s]
 =sum_s q_s(mathcal B_s-mathcal A_s)
  +sum_s q_s delta_s mathcal B_s,
```

where elementary cancellation in `h` gives exactly

```text
delta_s a_L(s)=a_F(s)-a_L(s)
 =2(k-1)/[R(k-s)(D-s)].
```

For `1<=s<=j` this is `O(k^-2)`.  A nonnegative profile of mass
`12a_L(s)` has circular variation at most `24a_L(s)`, hence

```text
TV(H_N)<=24sum_s q_s delta_s a_L(s)=O(k^-2).
```

This verifies the exact collapse and its remainder without conditioning or
renormalizing `qhat`.

## 5. Independent phase maps and Lemma 1

For the B exterior word

```text
V=(1,...,k-1,2k,...,3k-1),
```

counting the `D` possible starting phases of an oriented abstract interval
gives the two-seam map

```text
(E_D f)_l=[(D-2l)f_l+(l-1)f_(l-1)]/D,  1<=l<=k,
(E_D f)_(k+r)=[r f_r+(k-r)f_(k-r)]/D,  1<=r<k,
(E_D f)_(n-l)=(E_D f)_l.
```

For either contiguous A block, the `k` phases give

```text
(E_k g)_l=(k-l)g_l/k, 1<=l<k,
(E_k g)_l=0,          k<=l<=2k,
(E_k g)_(n-l)=(E_k g)_l.
```

An independent coordinate enumerator agrees with both formulas for arbitrary
symmetric rational profiles, not only the CEBV coefficients.

For Lemma 1 put `a_s=sw_s`, `a_0=0`, truncate the D half-profile after
`j`, and reflect the k profile.  Direct subtraction gives

```text
v_l=a_(l-1)/D-a_l/(kD),            1<=l<=j,
v_(j+1)=a_j(1/D-1/k),
v_l=-a_(k-l)/k,                    j+1<l<k,
v_k=0,
v_(k+r)=a_r/D,                     1<=r<=j,
v_(k+r)=a_(k-r)/D,                 j<r<k.
```

Thus `l=1`, `l=j`, the `j/j+1` seam, `l=k-1`, `l=k`, both middle-seam
ends, the duplicated midpoint values at `r=j,j+1`, and reflection are all
controlled by `TV(a_0,...,a_j)/k`.  Because `a_0=0`, the same hypothesis
also bounds every `|a_s|`; no missing terminal `a_j-to-0` assumption is
needed.  The `k=3` coincidence `j+1=k-1` uses the displayed seam value and
is directly included.

For the first-edge application,

```text
q_s=[k/(k-1)]b_s[b_(k-s)/b_k],
a_L(s)=[D-6+2/s+2/(D-s)]/R.
```

The Borel ratio bounds imply, for `w_s=q_sa_L(s)`,

```text
w_s<=Cb_s,
|Delta(sw_s)|<=Cs^(-3/2)+C/[k sqrt(s)].
```

Both series give a uniform bound on `TV(0,sw_s)`.  For `w_s=b_s`,
`|Delta(sb_s)|=O(s^-3/2)`, so the same hypothesis holds.

The two extensions stated after Lemma 1 are also complete consequences of
the already proved phase bound `(4.2)`:

- the omitted Borel tail `j<d<k` has endpoint-inclusive half-variation
  `O(k^-3/2)` and `l1=O(k^-1/2)`, hence embedding cost
  `O(k^-3/2)+D^-1O(k^-1/2)=O(k^-3/2)`;
- a constant tail of height `c=O(1/k)` has half-variation `2c=O(1/k)`
  and `l1=O(kc)=O(1)`, hence embedding cost `O(1/k)`.

Therefore neither the Borel tail nor the constant reference hides an
unproved seam term.

## 6. Generalized stabilization, including `r=1,2`

For odd `M in {k,D}`, `1<=r<M`, and `1<=d<M/2`, subtract

```text
B_r(d)=(r/R)b_d+4/R
```

from `Z_(M,r)(d)=U_r(d)+U_r(M-d)`.

For `r=1`, `U_1` is empty.  For `r=2`, the only possible value satisfies

```text
U_2(1)=R^-1[2-2b_1^2/b_2]=0.
```

In both cases `Z=0`, while the endpoint-inclusive variation of `B_r` is
`O(1/R)` because `b_d` is decreasing and summable and the constant part has
only two jumps.

For `r>=3`, on `d<r` the direct-row error is

```text
R^-1{b_d[(r-d-3)Q_r(d)-r]-4/r},
Q_r(d)=b_(r-d)/b_r.
```

On `d<=r/2`, the bracket has size `O(d+1)` and adjacent difference `O(1)`;
after multiplication by `b_d`, its total variation is `O(1)`.  On the
other half, with `a=r-d<r/2`, it becomes

```text
(a-3)b_a Q_r(a)-r b_(r-a).
```

The first term has variation
`O(1)+r^-1 sum_(a<=r/2)O(a^-1/2)=O(1)`, and the monotone second term has
variation `O(r b_(ceil(r/2)))=O(r^-1/2)`.  At the active/inactive
`r-1/r` cutoff both brackets are `O(1)`.  The inactive row
`-[rb_d+4]/R` has variation `O(1/R)`.  These bounds also make the value at
either zero-padded half endpoint `O(1/R)`, including the earlier endpoint
created when `M=k`.

The reflected row is active only for `d>M-r`.  With

```text
a=r-(M-d),
```

the inequalities `d< M/2` and `r<M` imply `a<r/2`, including `r=M-1`.
Its bracket

```text
4(r-1)/r+(a-3)b_a b_(r-a)/b_r
```

has total variation and both support-endpoint values `O(1)`.  Division by
`R` controls its internal variation, support cutoff, midpoint, and zero
endpoint uniformly.  Hence

```text
TV[Z_(M,r)-((r/R)b+4/R)]<=C/R
```

is valid for all stated `M,r`, including `r=1,2`.

Pairing `r=s,M-s` gives the B and A marked references.  Their error
profiles have `l1=O(1)` because both raw nonnegative profiles and their
references have uniformly bounded mass.  This supplies the `l1` guards
needed in `(4.2)--(4.4)`.

For the untouched row,

```text
T_k(d)-(k/R)b_d=(k/R)b_d[Q_k(d)-1].
```

On `d<=j`, `|Q_k(d)-1|<=Cd/k` and `|Delta Q_k(d)|<=C/k`.  Combining
these with `|Delta b_d|<=Cb_d/d`, the `d=1` zero endpoint, and the
`d=j` endpoint gives variation `O(1/k)` and `l1=O(1)`.  This proves the
untouched estimate independently.

## 7. Final assembly and CEBV

The first-edge difference is Lemma 1 applied to `w_s=q_sa_L(s)`, plus an
A remainder of mass

```text
2sum_s q_s[a_F(s)-a_L(s)]=O(k^-2).
```

The marked and untouched stabilization errors pass through the phase maps
at cost `O(1/k)` by their half-variation and `l1` guards.  The two reference
slopes differ only by

```text
2k/R-D/R=1/R,
```

while Lemma 1 and its explicitly checked Borel and constant tails compare
the common reference profiles at cost `O(1/k)`.

Finally `N_(2k+t)=k-|t|` for `|t|<=k-1`, and zero otherwise.  Therefore
`TV(M)<=2TV(N)=O(k)` and

```text
TV(X_k)<=4u TV(M)/k^2=O(1/k).
```

Together with the `O(k^-2)` normalizer remainder this proves full circular
`TV(H)=O(1/k)`.  The CEBV vector is exactly the restriction of
`(H_(l+1)-H_l)` to `l=2,...,n-3`; restriction cannot increase `l1`.
M289's theorem follows.

## 8. Independent computation and boundary falsification

`independent_cebv_audit.py` was written after the formulas above were fixed.
It imports no M289, predecessor, or project code/data.  It constructs
minimal completions directly and checks every raw ambient coefficient at
`k=3,5`.  The exact results are

```text
k=3: CEBV l1=148/135,
k=5: CEBV l1=1411115143/1382976000.
```

For every required split, the direct B/A collision masses equal
`12a_L(s)` and `12a_F(s)`, and the cross mass equals `8u`.  An arbitrary
rational-profile coordinate test independently verifies both phase maps.
Formula/boundary scans through `k=63` include every `r` for both `M=k,D`,
with explicit `r=1,2,M-1` rows, both cutoffs, reflection, midpoint, both
zero endpoints, the untouched term, triangular term, actual Lemma 1
weights, and its Borel/constant tails.  These scans are finite falsifiers
only; Sections 3--7 are the proof.

After the independent checker was fixed and run, M289's frozen checker was
replayed into this mission directory.  The replay and frozen result are
byte-identical, both with SHA-256

```text
38c6f6deecd5beb83c8a5703253736fb728bdf3cf23b38902af945a92577e04b.
```

## 9. Numbered objections and exact stop

1. **Material objections to M289:** none.
2. **Nonmaterial objections to M289:** none.
3. **Scope guard:** ACCEPT promotes only CEBV.  This referee makes no CIBV,
   DOR, SET, PBV, FD, FCL1, gap, mixing, or Terminal inference.

Final verdict: **ACCEPT M289 AS FROZEN AT CEBV-ONLY SCOPE.**
