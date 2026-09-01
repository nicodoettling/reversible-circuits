# M266 unconditional auxiliary fixed-cell response theorem

Date: 2026-08-14 UTC.

Status: **proved by exact assembly of frozen, independently accepted
inputs**, subject only to a fresh audit of this assembly.  “Unconditional”
here means that the former full-DV hypothesis has now been discharged.  The
theorem is confined to the first auxiliary minimal-long-cycle fixed cell; it
is not a theorem about the global identity-word law or the lazy exact
same-product `{3,4,5}` heat-bath chain.

## 1. Exact setting and notation

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors
multiplying left-to-right.  Fix an odd integer `k>=3` and put

```text
n=3k,        m=(n-1)/2=floor(n/2),
L=2k-1,      R=2k-3.
```

Here `n` is the size of the ambient long cycle and `m` is the component-size
cutoff endpoint.  They are not the ambient symmetric-group parameter and
circuit-word length in the project-level identity heat-bath problem.  The
target is the uniform law on minimal length-`n-1` transposition
factorizations of that long cycle, under the nonlazy cyclic rank-two
coordinate kernel.

After the two exterior transpositions, let `N_r(d)` count with multiplicity
the residual component cycles of size `d` whose supports have exactly `r`
ambient cyclic runs.  For every integer `2<=ell<=m`, define the literal
cutoff observables

```text
X_ell=sum_(2<=d<=ell)[N_1(d)+N_2(d)],
Y_ell=sum_(2<=d<=ell)N_1(d).                         (1.1)
```

Equal-size faces, same/cross kinds, both seams, unit gaps, and collision
multiplicities remain included.  Write `Phi_s^disj` for the source papers'
normalized disjoint-B profile `Phi_s^D`; the superscript is renamed only to
avoid confusing it with a cutoff index.  The adjacent ranks are exactly
`1<=s<=k-2`, joining the first-split profiles at `s` and `s+1`.

## 2. Full DV with explicit constant

M251/M255 proves, on precisely this domain and for precisely `Y_ell`,

```text
sum_(s=1)^(k-2)sqrt(s)
 |Phi_(s+1)^disj(Y_ell)-Phi_s^disj(Y_ell)|
 <=18400sqrt(ell).                                  (2.1)
```

M258/M263 proves the exact pointwise decomposition

```text
Phi_s^disj(X_ell)-Phi_s^disj(Y_ell)=Theta_s(ell)    (2.2)
```

and, on the same odd-`k`, cutoff, and rank domain,

```text
sum_(s=1)^(k-2)sqrt(s)
 |Theta_(s+1)(ell)-Theta_s(ell)|
 <=500sqrt(ell).                                    (2.3)
```

Apply the triangle inequality to (2.2) only after taking the exact adjacent
difference and short/long pairing used by the two accepted component
theorems.  Equations (2.1)--(2.3) give

```text
sum_(s=1)^(k-2)sqrt(s)
 |Phi_(s+1)^disj(X_ell)-Phi_s^disj(X_ell)|
 <=(18400+500)sqrt(ell)=18900sqrt(ell).             (2.4)
```

The `Y` bound is also at most `18900sqrt(ell)`.  Thus full `(DV)` holds for
both exact observables with the common absolute constant

```text
K_V=18900.                                          (2.5)
```

There is no `q` or `qhat` average in (2.1)--(2.4): `(DV)` concerns the
normalized B profile at each split.  This is exactly the interface required
by the disjoint Abel term in M192/M195.

## 3. DE and the full weighted prefix response

M217/M222 establishes the literal signed deletion/embedding identity, and
M248/M249 proves for the same `X_ell,Y_ell` and the same cutoff range

```text
|DE_Z|=|sum_(s<k/2)qhat_s[Phi_s^disj(Z)-Psi_s^disj(Z)]|
      <=7164sqrt(ell)/k,             Z=X_ell,Y_ell.   (3.1)
```

Here `qhat` remains the original unnormalized disjoint submeasure.  M192's
nonzero unequal-disjoint-mass Abel endpoint is separate from `(DE)` and is
retained downstream.

Let `K_E` be the accepted absolute constant in M192/M195's signed scalar
cumulative estimate `|E_u|<=K_E sqrt(u)/k`.  That proof did not freeze a
numerical value for `K_E`, so it cannot be replaced honestly by a number.
Substituting (2.5) into M252/M253 gives, for each channel-two prefix,

```text
K_J=K_E K_V+7164+15+6
   =18900K_E+7185.                                  (3.2)
```

The `15` is the complete shared-endpoint contribution and the `6` is the
retained unequal-disjoint-mass endpoint.  With

```text
den=(3k-3)(3k-4),
alpha_0=(k-1)(k-2)/den,
alpha_1=2(k-1)(2k-2)/den,
alpha_2=(2k-2)(2k-3)/den,
```

the exact source-independent channel masses are nonnegative and sum to one.
The `J=0` law cancels, while the full prefixes are exactly
`alpha_1` times the channel-one prefixes plus `alpha_2` times the
channel-two prefixes.  Thus the conditional profiles in (3.1) use no
missing renormalization.

Let `K_1,K_2` be the accepted absolute constants in the channel-one
weighted coefficient estimates.  M252/M253's exact Hardy--Abel transfer and
nonnegative channel mixture now prove unconditionally

```text
n[(|A_m|+|C_m|)/m
  +sum_(ell=2)^(m-1)(|A_ell|+|C_ell|)/ell^2]
 <=C_W,                                             (WPCR*)

C_W=18K_1+9K_2+18(18900K_E+7185)
   =18K_1+9K_2+340200K_E+129330.                    (3.3)
```

This is full `WPCR`, not pointwise `PCR`.  The unresolved `J1-PCR` estimate
is unused.

## 4. Response chain through PCS

M256/M259 proves that `(WPCR*)` is sufficient for the small-component
boundary response.  The exact finite Abel identity retains

```text
M_1(1)u_1(1),       A_m u_2(m),       C_m r_m,
```

as well as every interior first difference.  The accepted singleton bound
`M_1(1)=O(1/n)`, endpoint bounds `O(1/d)`, and first-difference bounds
`O(1/d^2)` therefore give

```text
|S_k|=O(1/n).                                        (SCBR)
```

Because `k` and hence `n=3k` are odd, `m=(n-1)/2` is exactly the last small
component size; no half-size cell is omitted.  Combining SCBR with the
accepted large-component tail and the exact boundary identities yields the
uniform proved chain

```text
SCBR
 => BR: eta(B_k)=O(1)
 <=> BIR: |(bar K^2W)(O_B)-(bar K^2W)(O_A)|=O(n^-2)
 => Delta_k(C_k)=O(n^-2)
 <=> k |sum_(y=1)^(n-3) z_k(y)|=O(1).              (PCS-bound)
```

The affine constant, collision indicator, bounded response remainder, and
the `2n eta(T)` kind term all remain in these exact identities.

## 5. Minimal rank and endpoint audit

The accepted component theorems explicitly include `k=3`.  Then
`n=9`, `m=4`, the adjacent-rank sum has the single edge `s=1`, and the
cutoffs are `ell=2,3,4`.  M251/M255 checks the relevant denominator values
`H_1=1/2,H_2=2/9`; M258/M263 treats the special `ell=4>L-2` term by the
empty-sum convention.  No asymptotic rank threshold is used.

The cycle-count observables begin at component size two, but the size-one
term is not discarded: it reappears separately as `M_1(1)u_1(1)` in the
SCBR Abel identity.  Likewise the cutoff endpoint `ell=m`, the shared
endpoint triangles, and the unequal-disjoint-mass endpoint are all retained.

## 6. Exact stop

The proved PCS bound controls only the absolute value of a signed total.  It
does not control the absolute phase sum.  M168's deterministic closure has
the independent term

```text
(n-3)k sum_(y=1)^(n-4)|z_k(y+1)-z_k(y)|.
```

The separately unresolved condition

```text
k^2 sum_(y=1)^(n-4)|z_k(y+1)-z_k(y)|=O(1)          (FD-bound)
```

would control it because `(n-3)/k<=3`.  Alternatively one may prove the
unresolved minority-sign estimate `k min(P_k,N_k)=O(1)`.  Without one of
these inputs there is no `FCL1` and no bound on the first-cell scalar
`A_k(1,1)`.

Even either closure would address only the first auxiliary fixed cell.
This theorem proves no direct L1/all-edge bound, H0, bridge-chain spectral
gap, polynomial mixing of the local heat-bath chain, or Terminal.  Full
pointwise `PCR` is neither proved nor needed for the result above.
