# M237 source, immutability, and anti-lookup audit

Date: 2026-08-13 UTC.

## Frozen inventory

Running `sha256sum -c SHA256SUMS` in frozen M236 returned `OK` for every
listed payload:

```text
plan.md
checkpoint.md
immutable_gate.md
halfway_checkpoint.md
z2_next_rank_check.py
z2_next_rank_results.json
finite_next_rank_theorem.md
report.md
audit_request.md
freeze_manifest.md
```

The directory has exactly these ten payloads plus `SHA256SUMS`.  The top
inventory digest is

```text
0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a  SHA256SUMS
```

M237 did not modify or execute M236 or any predecessor.

## Source ordering

Filesystem chronology is consistent with M236's predeclaration assertion:

```text
2026-08-13 22:46:49 UTC  plan.md
2026-08-13 22:50:33 UTC  immutable_gate.md
2026-08-13 22:54:12 UTC  z2_next_rank_check.py
2026-08-13 22:55:59 UTC  z2_next_rank_results.json
2026-08-13 23:00:19 UTC  SHA256SUMS
```

The assertion and modification times are not an external cryptographic
commitment.  This is retained as a nonmaterial provenance qualification.

## Static no-input and anti-lookup audit

Static inspection occurred only after M237 had fixed its independent table,
counts, and native hashes in `checkpoint.md`.  M236 was not imported or run,
and its result data were not read into the M237 checker.

The frozen M236 checker imports only Python standard-library modules.  Its
only filesystem operation is the final `OUTPUT.write_text`; it has no input
open/read, subprocess, dynamic import, `exec`, `eval`, or deserialization
path.  Tree generation, descriptors, words, endpoints, replay, and summaries
are all constructed internally.

The decisive call ordering is literal in the source:

```text
primary row:   descriptor_data -> formula_route -> endpoint_pair -> act
secondary row: fixed_non_z2_route             -> endpoint_pair -> act
```

`formula_route` depends only on rank and the tree-side descriptor.  The class
census and failure classification occur after every replay and never feed
back into the formula.  There is no route search, target table, endpoint
field in `Z2`, quotient/group enumeration, or post-failure exception rule.

## Independent reconstruction and compatibility separation

M237's decisive checker independently implements Prüfer decoding, the rooted
plus-mirror DPS boundary closure, transposition algebra, chronological signed
right-Hurwitz replay, `Z2`, the M231 word formula, and the six fixed-family
words.  It reads no input file and imports no project module.

After the independent results were fixed, an isolated serialization-only
function was transcribed to compare normalized certificates.  It performs no
M236 runtime reads and changes no tree, descriptor, word, endpoint, or replay
result.  It reproduces all seven published M236 normalized digests exactly.

