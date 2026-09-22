# Freeze manifest and timestamp correction

Observed with clock tool: 2026-09-22 05:53:22 UTC.
The frozen `proof_v1.md` has SHA256
`43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0`.
Its filesystem modification time, observed by `stat` at the same check, is
2026-09-22 05:52:41.907381352 +0000. This is the actual artifact creation/freeze time available from filesystem evidence.

The internal header's manually estimated `05:55 UTC` is erroneous and must not be used as provenance. It is retained solely to preserve the frozen hash. The initial checkpoint's manually estimated `05:49 UTC` likewise preceded an exact clock check and is only approximate; use the filesystem/settings timestamps for that artifact. All later checkpoints use an observed UTC timestamp.

No R2 candidate proof had been received or read before this freeze. Root informed this worker that root and R2 separately found related majorants, and sent an alternative constants calculation only after v1 was frozen; these are not claimed statistically independent reviewers.
