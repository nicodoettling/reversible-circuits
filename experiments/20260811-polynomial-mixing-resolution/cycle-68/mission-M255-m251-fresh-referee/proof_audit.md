# M255 clean-room proof audit of immutable M251

Date: 2026-08-14 UTC.

Status: **ACCEPT** M251's exact paired-domain identities and its `Y-DV`
theorem with constant `18400`. The literal two-run `TAV`, hence `X-DV`,
remains **unresolved**. No downstream inference is made.

## 1. Immutable gate and scope

All 11 files named by M251's `SHA256SUMS` pass `sha256sum -c`. The digest
of that checksum file is

```text
c4cee2dc9596bb54503f85a7b32b91b360fe22d1aa981eb0dce7e3d7657c04fd.
```

M251 was not edited. The accepted M199/M207 literal B-side ordered-disjoint
double law is the only substantive dependency. The audited domain is odd
`k>=3`, `D=2k-1`, `R=2k-3`, and
`2<=ell<=(3k-1)/2`.

## 2. Paired-domain identity and endpoints

For a parent of size `r`, the old triangular domain is
`1<=d<=r-2`, `1<=a<=r-d-1`. Its intersection with the size-`r+1`
domain is exactly the same triangle; the new strip is
`1<=d<=r-1`, `a=r-d`. Adding and subtracting the new kernel times the
old observable gives M251 (2.1), including the `X` seam edit. The survivor
term is split exactly by adding and subtracting
`h(r+1)F_ell(D-r)`.

With `q=D-s`,

```text
N_(s+1)-N_s = [U_(s+1)-U_s] - [U_q-U_(q-1)],
```

so every long-parent increment has the stated minus sign. At `s=1`, the
long increment is indexed by `q-1=D-2`; at `s=k-2`, it is indexed by `k`.
Both lie in the one-parent range, and all empty short domains are harmless.

Writing `h(r)=(r-3+2/r)/R` independently gives

```text
H_(s+1)-H_s
 = (2/R){1/[(q-1)q]-1/[s(s+1)]}.
```

The ordinary quotient identity then gives M251 (3.3). Splitting the long
strip at `d=s-1` and distributing the add-subtract term reconstructs (4.1)
exactly. For `Y`, its placement average is `F_ell(d)` for either parent, so
the middle observable edit is identically zero.

## 3. Lemma 1: Borel cumulative increments

Put `c=r-d` and
`A_r(d)=(c-1)b_c/b_r`. Direct division verifies

```text
A_(r+1)(d)-A_r(d)
 = (b_c/b_r){1-c[1-rho_(r+1)/rho_(c+1)]}.
```

For `L(x)=log rho_x`, its logarithmic series gives
`0<=-L'(x)<=3/x^2` and `0<=L(x)<=2/x`. Hence
`q=rho_(r+1)/rho_(c+1)` satisfies `0<=c(1-q)<2`, so the factor in braces
has absolute value at most one. The convolution identity

```text
sum_(d=1)^(r-1)b_d b_(r-d)=2(r-1)b_r/r
```

also follows directly by counting a labeled tree with an oriented
distinguished edge. It bounds the full common contribution by `2/R`.
When admitted by the cutoff, the only new atom is `d=r-1`, whose coefficient
before division by `R` is
`b_2 rho_r rho_(r+1)<=e^-2 e^2=1`. Thus the global `3/R` bound includes the
boundary atom and the empty `r=1` case.

In the far regime `d<=t` and `r>=2t+2`, `c>=r/2`. Integration of the same
derivative bounds gives

```text
log(b_c/b_r)<=4d/r<=2,
0<=L(c+1)-L(r+1)<=12d/r^2.
```

Consequently `|b_c/b_r-1|<=4e^2d/r` and
`1-rho_(r+1)/rho_(c+1)<=12d/r^2`. Substitution yields
`|Delta A_r(d)-1|<=16e^2d/r<120d/r`. Finally
`b_d<=1/(2d^(3/2))` and `sum_(d<=t)d b_d<=sqrt(t)`, proving
the claimed `120sqrt(t)/(Rr)`. No monotonicity of individual coefficient
increments is used.

## 4. Lemma 2: head response and the true denominator bound

For `s<2t+2`, the paired fragmentation increment is at most `6/R`; direct
summation gives M251's safe `16sqrt(t)` near bound. If the far range is
nonempty, then `s>=2t+2` and `q-1>=k>=2t+4`, so Lemma 1 applies to both
parents. Their common `B_t/R` terms cancel before absolute values, leaving
at most `240sqrt(t)/(Rs)`, whose weighted sum is at most `480sqrt(t)`.
Thus `496sqrt(t)` is valid for fragmentation.

Each of the two survivor summands has at most one cutoff jump. Its remaining
increments have size at most `1/R`; splitting at its cutoff bounds their
combined weighted variation by `4sqrt(t)`. Also `0<=P_s(t)<=2` and direct
summation of the normalization formula gives
`sum_s sqrt(s)|Delta H_s|<=8/3`, hence a quotient-normalization contribution
at most `16/3` before division by the next denominator.

The actual uniform denominator identity is

```text
H_s=[D-6+2/s+2/(D-s)]/R.
```

For `k=3`, the needed values are `H_1=1/2` and `H_2=2/9`. For `k>=5`,
`H_s>=(D-6)/(D-2)>=3/7`. Therefore `H_s>=2/9` universally, and

```text
(9/2)[496sqrt(t)+4sqrt(t)+16/3] <=2300sqrt(t).
```

Lemma 2 and its constant are valid, including the minimal case.

## 5. Seam profiles, constant annihilation, and `Y-DV`

The accepted three-gap seam incidence law independently yields M251
(4.1)--(4.3). For `x<k`, the gaps are `x,x+1,x+k` with multiplicities
`D-2x,x,x`; for `x>=k`, only the gap `x+1` can meet the allowed cutoff,
with multiplicity `D-x`. This gives exactly the three displayed regimes and
all their empty-range conventions.

In each regime the nonzero adjacent changes are confined to the initial
jump, a slope-`1/D` interval, and at most two cutoff jumps, all at indices
at most `ell`. Direct accounting gives total unweighted variation below
`3`; hence the weighted variation is already below `3sqrt(ell)`, and in
particular below the claimed `8sqrt(ell)`.

The Borel convolution also gives `W_r(1)=h(r)`, so `L_s(1)=2` and adjacent
responses annihilate constants. The finite identity

```text
f(d)=f(1)+sum_t [f(t+1)-f(t)] 1{d>t}
```

has the stated Abel minus sign because `1{d>t}=1-e_t(d)`. Applying Lemma 2
after this exact expansion and then the seam bound proves
`2300*8=18400`, exactly M251's `Y-DV` theorem.

## 6. Exact remaining obligation

Subtracting the literal `Y` tuple law from the literal `X` tuple law cancels
both one-run faces and leaves exactly M251 (5.1), including both parent
orientations, every seam incidence, and repeated-size multiplicity. Thus

```text
Theta_s(ell)=Phi_s^D(X_ell)-Phi_s^D(Y_ell)
```

is precisely the normalized complementary two-run atom. Its weighted
adjacent variation bound `(TAV)` is sufficient, by the triangle inequality
with `Y-DV`, and is the sole remaining scalar obligation for `X-DV`.
`TAV` is not proved by M251 or this audit.

## 7. Bounded falsification certificate

`cleanroom_check.py` contains no imports and shares no M251 code. Its custom
rational arithmetic checks `k=3,5,7`, every allowed `ell`, all bounded
parent/split endpoints, the exact seam cases, common/strip identities,
quotient identity, boundary atom/global and far bounds, `H_s`, constant
annihilation, Lemma 2, `Y-DV`, and the literal `Theta` identity. A rational
Taylor enclosure of `e` makes the bounded far checks rigorous. It passes
952 assertions. This is finite falsification only.

## 8. Objections and verdict

Material objections: none.

Numbered nonmaterial qualifications:

1. M251 states the `k=3` denominator check tersely; the exact values above
   should accompany any later reuse. No correction is required.
2. M251's seam-variation sentence omits the short case accounting supplied
   above. The claimed constant is safe by a large margin.

Verdict: **ACCEPT** the paired identities and `Y-DV` with constant `18400`.
Keep `TAV`, `X-DV`, full `DV`, conditional `J2`, PCR/WPCR, SCBR, gap,
mixing, and every Terminal open unless separately discharged and audited.

