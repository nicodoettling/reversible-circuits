# M261 immutable dependency audit

Date: 2026-08-14 UTC.

Before mathematical use, `sha256sum -c SHA256SUMS` was run independently in
each required source and referee directory. Every declared payload passed.
The observed checksum-ledger and freeze-manifest digests are:

| mission | `SHA256SUMS` SHA-256 | `freeze_manifest.md` SHA-256 |
|---|---|---|
| M161 | `17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8` | `b6b366bab63493245abbf47c89cb6cfb14d40af56e9812a3227a6086f3af926d` |
| M166 | `344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3` | `a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498` |
| M168 | `3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd` | `32e62aba79103a298eb19050f916dc1a359c671cdeaa1c1744c156dcec7b92f0` |
| M171 | `c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d` | `40c18be04a8a782a4110b933adcf5b3d92b7f98dc53c877ab4b96e763fd4ad35` |
| M174 | `fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba` | `f346d050476912f02728a130fb97b1ee21e1717bd099ce8930c06397860e3de8` |
| M178 | `6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba` | `15c7d7b462625c36d21d609560d0cac6a5c963643d80d8adba428b88924b961d` |
| M256 | `f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261` | `b4a9c90767d34da2e91db0f447376a204e4f96df61a6c8f8f24996cf02219f3d` |
| M259 | `c91571dbca9e1b7ebd8e014448530459bfade658168a76bac24b5a0ec4217aa2` | `dbe54a4582bbeb9b9ace4f5c10a0b83723bc99fac3aefbd43f3c249ec645fc30` |

M161 and M166 are historical inventories that omit their own freeze
manifests; those two manifest hashes were therefore checked separately. The
M166 value above agrees with M259. M256's `dependency_audit.md` instead
contains the already-refereed nonmaterial transcription error

```text
a78b5ebb...bb897bb59d63b40705aa9a
```

which splices the correct freeze-hash prefix with the suffix of M166's report
hash. No payload mismatch results, and no predecessor was edited.

Interfaces used below:

- M161/M166: exact constant-mass fixed-cell convolution and reflection;
- M168/M171: exact phase law, `FD-bound`, and minority-sign alternative;
- M174/M178: accepted PCS reduction, used only to identify the independent
  stopping point;
- M256/M259: accepted conditional chain through PCS and the mandatory stop at
  independent FD/minority sign.

No full-DV statement is used in M261.

