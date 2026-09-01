# M308 Dependency Audit

Date: 2026-08-14 UTC

The assigned frozen M307 checksum-file digest is exactly

```text
41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e.
```

Every payload named by M307 and by each direct or transitive source lock was
checked from its own mission directory with `sha256sum -c SHA256SUMS`; every
row passed.  Independently measured checksum-file digests and inventory row
counts are:

```text
M274  c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e  10
M277  c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890  11
M280  60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9  10
M283  156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf  10
M285  54eed4258da59ee1b8491815f182f05ac7c57c809e0f002bc2a2a79666098ac8  10
M287  0298ecf0d0f3ca2970f4a817469a01e247b125b4b0211eb748b752146e73fc35  10
M295  42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5  10
M298  d56bd6de3307284a8c5a135f5282ed1f1a3a793125ca056bb72f675e64f38cf8  13
M300  24964f0c5c8e8588715a98fc22a80d7b268b8e6abe683bd95772f51acecbebc8  15
M303  a3a708c95c72be4d665a47bcfe14196c1bc11bb281c9e26ee3b625b843cf1e72   9
M307  41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e  10
```

M307 directly locks M300 and its fresh referee M303.  The eight earlier
inventories above are the source locks cited by that accepted pair, so the
recursive provenance used here is complete.

## Metadata correction

M300's checksum file contains **15** rows.  M303's frozen dependency prose
says fourteen, although all rows and the top digest pass.  M307 explicitly
identifies and correctly repairs this metadata statement without editing
M303.  It is a nonmathematical, nonmaterial typo.  This inventory count is
logically separate from the independently verified fact that the `k=9`
quantile transport also has 15 supported cells.

No predecessor file was modified.
