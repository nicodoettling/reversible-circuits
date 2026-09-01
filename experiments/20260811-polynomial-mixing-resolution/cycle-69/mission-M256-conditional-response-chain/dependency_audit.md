# M256 immutable dependency audit

Date: 2026-08-14 UTC.

## Audit method

Before using any claim, M256 ran `sha256sum -c SHA256SUMS` in every source
and referee directory in the table below. Every declared entry passed. A
directory listing was also compared with each inventory; for the principal
M168--M253 chain, every regular payload file other than `SHA256SUMS` itself
is inventoried. M189 has an untracked generated `__pycache__` directory but
no extra regular payload. No dependency was edited.

The supplementary M161/M166 pair is used only for the exact
`A_k(1,1)`--`FCL1` equivalence. Its historical checksum lists omit the
freeze manifest itself, so M256 independently recomputed the two freeze
manifest hashes and matched the values frozen in the accepted referee and
coordinator ledger.

## Frozen checksum-file digests and interfaces

| mission | SHA-256 of `SHA256SUMS` | interface used here |
|---|---|---|
| M161 | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` | `A_k(1,1)=k(n-3)^-1 sum_y|Z_k(y)|` |
| M166 | `344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3` | accepts the preceding equivalence |
| M168 | `3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd` | `(PCS-bound)+(FD-bound)=>FCL1` with exact `TV-close` |
| M171 | `c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d` | accepts M168's scalar closure |
| M174 | `fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba` | `BR iff PCS-bound`, including affine kind transfer |
| M178 | `6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba` | accepts M174 and supplies explicit remainder audit |
| M180 | `b362d629eaae627432efb3d6de97a825ed1bb17c0ca17ffb39c342db5c9d76d6` | `SCBR => n eta(Q)=O(1) iff BR iff BIR` |
| M182 | `4b5f96b5269f6174102086ce30ed0858537122bdec39b551e2248d843439c9ad` | accepts M180's tail, remainder, and BIR normalization |
| M186 | `9d5aa5ff628f8bf15051c09fd1537ffa240fba72ad2a9945356c8adfe8ebd7bd` | singleton bound, exact SBP, and `WPCR=>SCBR` |
| M189 | `893275dc8e31ffbd2a801415a5c26f3cd0221795d7c22260ec5866781494ce66` | accepts M186's exact endpoint-bearing implication |
| M192 | `4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60` | J2 shared/disjoint Abel law, scalar bound, unequal-mass endpoint |
| M195 | `1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a` | accepts M192's conditional J2 implication |
| M217 | `7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557` | exact signed `DE=S+K+N` reduction |
| M222 | `d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd` | accepts M217 and the normalizer bound |
| M235 | `7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527` | TCM, used transitively by DE |
| M238 | `eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8` | accepts TCM |
| M239 | `66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542` | YCM, used transitively by DE |
| M246 | `df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97` | accepts YCM |
| M248 | `c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8` | proved DE for `X_D,Y_D`, common constant `7164` |
| M249 | `9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7` | accepts WBE and DE |
| M252 | `896c8a7169ba73a8ae500a350de1d9106cd3a6f81dd4934b078fbdfd2e137556` | full WPCR conditional on full DV |
| M253 | `73cdc9d1345985b92430b76df7142a4a8bf3b3f8b7b42f68735b6e03be79fdc2` | accepts M252 with zero objection |

The independently recomputed supplementary freeze-manifest hashes are

```text
M161 b6b366bab63493245abbf47c89cb6cfb14d40af56e9812a3227a6086f3af926d
M166 a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897bb59d63b40705aa9a
```

## Dependency status

All interfaces actually used in the conditional proof below are **proved
and freshly accepted** in their own frozen pairs, except full `(DV)`, which
is the explicit hypothesis of M256. M235/M238 and M239/M246 are transitive
dependencies of the already accepted M248/M249 DE theorem; M256 does not
reassemble their coefficient proofs.

This audit found no manifest disagreement in the principal chain. It makes
no assertion that the auxiliary fixed-cell kernel is the project identity
heat-bath kernel; every cited source explicitly says it is not.
