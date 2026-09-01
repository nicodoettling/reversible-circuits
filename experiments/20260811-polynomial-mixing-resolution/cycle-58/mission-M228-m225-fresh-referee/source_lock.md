# M228 immutable source lock

Date: 2026-08-13 UTC.

## Inventory gate

All 12 payloads named by frozen M225's `SHA256SUMS` returned `OK`.  The top
inventory digest is exactly

```text
e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
```

M225 is immutable.  No file in its directory was edited.

## Source-order evidence

The frozen text explicitly labels `candidate_descriptors.md` as written before
any M225 endpoint replay and fixes exactly Candidate A and nested Candidate B,
with no third refinement.  Filesystem metadata is consistent with that claim:

```text
plan.md                    2026-08-13 21:55:38 UTC
candidate_descriptors.md   2026-08-13 21:58:28 UTC
symbolic_transport.md      2026-08-13 21:58:28 UTC
child_contour_audit.py     2026-08-13 22:04:17 UTC
child_contour_results.json 2026-08-13 22:04:40 UTC
```

The inventory cryptographically freezes the current contents, but it was
created after all payloads.  Therefore the asserted chronology is supported
by consistent text and filesystem metadata, not by a cryptographic timestamp
or earlier commit.  This is a procedural caveat to record in the verdict.

## Clean-room closure

Only M225's frozen textual candidate definitions, symbolic note, theorem, and
report were read after the inventory gate.  M225's checker and machine result
data are excluded from the decisive reconstruction: the M228 checker will
import neither and will read no M225 path.  Candidate formulae are now closed
for transcription.

## Repository source-path discrepancy

`AGENTS.md` names `references/experiments.md`, which is absent.  The skill's
actual relative file
`.codex/skills/reversible-circuit-sampler/references/experiments.md` exists and
was read.  No source file was altered to resolve this mismatch.
