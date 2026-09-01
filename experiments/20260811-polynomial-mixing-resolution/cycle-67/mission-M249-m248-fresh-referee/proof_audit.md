# M249 fresh immutable proof audit of M248

Date: 2026-08-14 UTC.

Verdict: **ACCEPT**. Frozen M248 correctly assembles the accepted one-run
and two-run coefficient moments into WBE, and then uses the exact normalizer
identity to prove signed averaged DE. The constants are `7000,7160` for WBE
and `7004,7164` for DE on the complete stated domain. This audit makes no
claim about DV or anything downstream of DE.

## 1. Immutable provenance gate

All eight files named in frozen M248 pass `sha256sum -c SHA256SUMS`. The
SHA-256 of that checksum file is exactly

```text
c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8.
```

Every file in each cited frozen dependency inventory also passes. The
recomputed checksum-file digests are

```text
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688
M235 7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527
M238 eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8
M239 66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542
M246 df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97
```

These are exactly the digests recorded by M248. No M248 or predecessor
file was edited by this mission.

## 2. Exact domain and accepted interfaces

Fix odd `k>=3` and

```text
D=2k-1, R=2k-3, j=(k-1)/2, L=(3k-1)/2,
2<=ell<=L.
```

M217/M222 accepts the literal raw-numerator partitions and the signed identity

```text
DE_Z=S_Z+K_Z+N_Z,                    Z=X_ell,Y_ell,
N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z.
```

Here `q_s` is a probability law on `1<=s<=j`, `B_s^Z=a_L Phi_s^D(Z)`,
and no absolute value or conditional renormalization has been inserted.
M226/M229 accepts the complete coefficient identities on the same cutoff
domain, with every actual `G_k` argument in the corrected range
`1<=x<=L-1`. M235/M238 accepts TCM with constant `160`; M239/M246 accepts
YCM with constant `7000`. Both moment theorems include `k=3` and use the
same integer cutoff range as M248.

## 3. Independent audit of the two WBE identities

For either observable, the definitions of the surviving and fragmentation
blocks give, by finite linearity,

```text
S_Z+K_Z=sum_s q_s(B_s^Z-A_s^Z).                    (3.1)
```

For `Y_ell`, M226/M229 extracts from the complete raw B/A one-run numerators
the coefficient `c^Y_(k,y)` of the cutoff atom of size `y`. Summing cutoff
atoms in (3.1) therefore gives exactly

```text
S_(Y_ell)+K_(Y_ell)=sum_(y=2)^ell c^Y_(k,y).       (3.2)
```

This is the YCM prefix, so accepted M239/M246 proves

```text
|S_(Y_ell)+K_(Y_ell)|<=7000 sqrt(ell)/k.           (3.3)
```

For every literal ordered tuple, `Y_ell` counts its one-run faces in the
cutoff and `X_ell` counts its one-run faces plus its unique complementary
two-run face. Thus `X_ell-Y_ell` is exactly that two-run cutoff count.
Subtracting (3.1) for X and Y before taking an absolute value yields

```text
[S_(X_ell)+K_(X_ell)]-[S_(Y_ell)+K_(Y_ell)]
  =sum_(y=2)^ell c^T_(k,y).                        (3.4)
```

This subtraction is over the complete raw laws. Hence the original ordered
tuple, same/cross kind, both B seam incidences, and each equal-size collision
remain counted with their original multiplicity; nothing is deduplicated or
dropped by the surviving/fragmentation partition. Accepted M235/M238 gives

```text
|sum_(y=2)^ell c^T_(k,y)|<=160 sqrt(ell)/k.        (3.5)
```

One triangle inequality applied to (3.3)--(3.5) proves

```text
|S_(X_ell)+K_(X_ell)|<=(7000+160)sqrt(ell)/k
                       =7160sqrt(ell)/k.           (3.6)
```

Thus both WBE constants and their exact domains are correct.

## 4. Independent normalizer derivation

Using M217/M222's exact definitions,

```text
gamma_L=2[2-1/s-1/(D-s)]/R,
gamma_F=2[2-1/s-1/(k-s)]/R,
a_L=1-gamma_L, a_F=1-gamma_F.
```

Direct subtraction, with `D-k=k-1`, gives

```text
a_F/a_L-1
 =2(k-1)/[R(k-s)(D-s)a_L].                        (4.1)
```

Write `k=2j+1`. Since `s<=j`,

```text
R>=k,
k-s>=(k+1)/2,
D-s>=(3k-1)/2.
```

Moreover `a_L=h(s)+h(D-s)>=h(D-s)`, where
`h(r)=(r-1)(r-2)/(rR)`. The function `r-3+2/r` is increasing for
integers `r>=2`; hence its minimum here is at `r=3j+1`. The inequality
`h(3j+1)>=1/2` is equivalent to

```text
(6j-1)(j-1)>=0,
```

including equality at `k=3,s=1`. Thus `a_L>=1/2`. Substitution in (4.1)
gives

```text
a_F/a_L-1
 <=16(k-1)/[k(k+1)(3k-1)]
 <=16/(3k^2),                                      (4.2)
```

because the second cross-multiplied right-minus-left margin is `5k-1>0`.

The literal observables lie in `[0,3]`, and `0<a_L<=1`, so
`0<=B_s^Z=a_L Phi_s^D(Z)<=3`. Since `q_s>=0` and `sum_s q_s=1`, (4.2)
implies the explicit universal bound

```text
|N_Z|<=16/k^2.                                     (4.3)
```

Finally `k>=3` and `ell>=2` give `k^2 ell>=18>16`. Both sides are
nonnegative, so this is exactly

```text
16/k^2<=4sqrt(ell)/k.                              (4.4)
```

Combining the exact signed identity with (3.3), (3.6), and (4.3)--(4.4)
proves

```text
|DE_(Y_ell)|<=7004sqrt(ell)/k,
|DE_(X_ell)|<=7164sqrt(ell)/k.                     (4.5)
```

The separate Abel endpoint in M192 is outside the definition of DE, so it
is neither needed nor silently discarded in this assembly.

## 5. Independent compact check

`independent_check.py` contains no imports and reads no M248 or predecessor
code or data. It checks exact integer forms of `a_L,a_F`, (4.1), (4.2), the
`h(D-s)>=1/2` inequality, the absorption inequality, all constant additions,
and every corrected `G_k` call generated by the three coefficient cases for
all odd `3<=k<=2001`. It passes 500,500 split rows, 1,501,500 cutoffs, and
3,002,000 G-domain calls. The smallest absorption margin is the boundary
value `3^2*2-16=2`. These finite checks are exact falsification evidence;
Sections 2--4 are the all-rank proof.

## 6. Numbered objections and scope

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
3. **Scope guard:** ACCEPT proves only the M248 WBE and signed averaged DE
   statements. DV remains open. This audit makes no conditional J2,
   PCR/WPCR/SCBR, comparison, spectral-gap, mixing-time, or Terminal
   inference.

Final verdict: **ACCEPT M248 AS FROZEN.**
