# M266 immutable dependency manifest

Every entry in every named predecessor `SHA256SUMS` inventory passed
`sha256sum -c` on 2026-08-14 UTC.  The independently observed digest of each
checksum file is:

| mission | SHA-256 of `SHA256SUMS` |
|---|---|
| M192 | `4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60` |
| M195 | `1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a` |
| M217 | `7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557` |
| M222 | `d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd` |
| M248 | `c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8` |
| M249 | `9246377285741ba7af0b2eb713f94e32e9aa25a0c00a7278c0cd9e8240b2d3f7` |
| M251 | `c4cee2dc9596bb54503f85a7b32b91b360fe22d1aa981eb0dce7e3d7657c04fd` |
| M255 | `d9a4e48e25b829bd06b098719b239587b8be5553a6f965b315e9d5efc55875a8` |
| M252 | `896c8a7169ba73a8ae500a350de1d9106cd3a6f81dd4934b078fbdfd2e137556` |
| M253 | `73cdc9d1345985b92430b76df7142a4a8bf3b3f8b7b42f68735b6e03be79fdc2` |
| M256 | `f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261` |
| M259 | `c91571dbca9e1b7ebd8e014448530459bfade658168a76bac24b5a0ec4217aa2` |
| M258 | `753ef6932c3e5e5d69df7f429e8740710d77269357749d505dca0cf31e109ef8` |
| M263 | `28e4d4f8f913b725b0a5793e67aecc57bfac021e4258754001c314094ac8f87b` |

M259 identified one nonmaterial transcription error in M256's dependency
audit.  The correct SHA-256 of M166's historical `freeze_manifest.md` is

```text
a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498
```

not M256's printed
`a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897bb59d63b40705aa9a`.
The M166 payload inventory and checksum-file digest pass; the error is
provenance-only and is not propagated here.

