# M259 immutable hash audit

M256's complete nine-file inventory passes. Its checksum-file digest is the
assigned value

~~~text
f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261.
~~~

Every entry in each cited predecessor inventory passes. The independently
observed checksum-file digests are:

| mission | observed SHA-256 of SHA256SUMS |
|---|---|
| M161 | 17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8 |
| M166 | 344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3 |
| M168 | 3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd |
| M171 | c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d |
| M174 | fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba |
| M178 | 6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba |
| M180 | b362d629eaae627432efb3d6de97a825ed1bb17c0ca17ffb39c342db5c9d76d6 |
| M182 | 4b5f96b5269f6174102086ce30ed0858537122bdec39b551e2248d843439c9ad |
| M186 | 9d5aa5ff628f8bf15051c09fd1537ffa240fba72ad2a9945356c8adfe8ebd7bd |
| M189 | 893275dc8e31ffbd2a801415a5c26f3cd0221795d7c22260ec5866781494ce66 |
| M192 | 4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60 |
| M195 | 1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a |
| M217 | 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557 |
| M222 | d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd |
| M235 | 7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527 |
| M238 | eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8 |
| M239 | 66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542 |
| M246 | df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97 |
| M248 | c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8 |
| M249 | 9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7 |
| M252 | 896c8a7169ba73a8ae500a350de1d9106cd3a6f81dd4934b078fbdfd2e137556 |
| M253 | 73cdc9d1345985b92430b76df7142a4a8bf3b3f8b7b42f68735b6e03be79fdc2 |

The historical M161 checksum list omits its freeze manifest; its independently
observed freeze-manifest hash is the M256 value
'b6b366bab63493245abbf47c89cb6cfb14d40af56e9812a3227a6086f3af926d'.

The historical M166 list also omits its freeze manifest. Its actual hash is

~~~text
a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498.
~~~

M256 instead prints
'a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897bb59d63b40705aa9a'.
That value is incorrect and appears to splice the actual hash prefix with
the suffix of M166's inventoried report hash
'2263f740da7e278e73690e4e99f171378077d87d779b897bb59d63b40705aa9a'.
The coordinator ledger already contains the actual freeze-manifest value.
This is a nonmaterial provenance transcription error, not a payload mismatch.

