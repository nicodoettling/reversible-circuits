# M329 integrity audit

Date: 2026-08-14 UTC

## Immutable inputs

- M323 top `SHA256SUMS` digest:
  `0aa6cfccd9d5feaf16ded0c4c5b5bf42d552c1f36ff4f4ce58998c927cbac39c`.
- Frozen M326 top `SHA256SUMS` digest:
  `a1ea699e4086cb967875c9408f586afc0854c85096a278e32eed9697b5ba2a2a`.

M326 contains exactly ten payloads plus its non-self-listed `SHA256SUMS`.
M323 and M326 were read only and remain immutable.

## Independent M326 payload rehash

| payload | independently recomputed SHA-256 | frozen-row status |
|---|---|---|
| `plan.md` | `341b0ca8a40412039e803cc6cc631b0bb92d3070d8f0e96fb1113bf2e2d2254e` | exact match |
| `checkpoint.md` | `e6de14130dfe99b4eb46ea739b7ff387e3fe8e0a64909771d35fd06883a80b76` | exact match |
| `halfway_checkpoint.md` | `cc52da32f177b02273054b04ece272aeb660c59db109984bc8bbb65fcfdffe00` | exact match |
| `dependency_audit.md` | `0a5d6799a4fda5e8ef0d5c37196d0b2e625a68edadf516d1ea70da8faf210df4` | exact match |
| `proof_audit.md` | `e54e1c8aa58a48dc819f862cf7ea839221170397a1c1c1203d23fe06907350c0` | exact match |
| `salvage_obligation.md` | `d884393edfa9fcfe95684623b5fcb13823cda0ee3f19c55f6427af4ef9d9f260` | exact match |
| `report.md` | `94bc16902da4bec770f95b6b7a1fc378f4095441ecc3dba739b5805bd64a862d` | exact match |
| `run_manifest.md` | `a27542054b7af7ed7bff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4` | frozen row malformed |
| `final_checkpoint.md` | `b3f2e171ccc8d70c931a4c652d748a8a565eb29918ec87b7438861ccaa8810c1` | exact match |
| `freeze_manifest.md` | `254098a86ed46a49181676695fccf1203abef7e737191c345c76dad48b07f73e` | exact match |

Nine frozen rows are well formed and exact. The eighth frozen row contains
only 63 hexadecimal characters:

```text
a27542054b7af7edbff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4  run_manifest.md
```

It omits the character `7` immediately after `...f7ed`. The corrected full
64-character row is:

```text
a27542054b7af7ed7bff75261df5fb64dcc01b3afc9868ac99954c6bd5f76df4  run_manifest.md
```

This is a checksum-manifest transcription defect only. The payload itself is
present and independently hashes to the corrected value.

## M323 dependency gate

The M323 top digest equals the assigned value above, and
`sha256sum -c SHA256SUMS` verifies all fifteen M323 payload rows. No dependency
gate changed.

## Scope conclusion

This audit repairs only freeze provenance. It performs no mathematical
reanalysis, witness search, rank computation, guard, or source surgery.

