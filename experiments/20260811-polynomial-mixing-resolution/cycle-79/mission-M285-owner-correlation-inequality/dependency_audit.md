# M285 immutable dependency audit

Date: 2026-08-14 UTC.

The mission plan and initial checkpoint were created before any substantive
dependency file was opened.  Each source directory was then treated as
immutable.  Its `SHA256SUMS` digest, exact listed-payload count, and
`sha256sum -c SHA256SUMS` result are:

| mission | checksum-file SHA-256 | listed payloads | result |
|---|---|---:|---|
| M280 | `60afef642d945847db0427f388d1219497416a09c4a955818607f71df87ae0a9` | 10 | all pass |
| M283 | `156fa5207e088f38ae71b69e48332a8a708bae8f03f1447c77e9710128572cdf` | 10 | all pass |
| M91 | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | 13 | all pass |
| M94 | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` | 15 | all pass |
| M261 | `b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b` | 9 | all pass |
| M264 | `b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f` | 6 | all pass |

The inventories match their frozen mission payloads exactly: no listed file
is missing, no digest fails, and the checksum files themselves are excluded
from their own listed payload counts.

Controlling use in M285:

- M280/M283: accepted exact `CP-OCI` identity and its normalization only;
  neither source proves OCI.
- M91/M94: exact normalized `J=1,2` channel/Abel laws and their limitations;
  `BA2`, the central-double defect, and every downstream estimate remain
  unresolved.
- M261/M264: accepted owner-correlation and collision/decorated affine
  identities; `PBV`, minority sign, and FCL1 remain unresolved.

No dependency file was edited.
