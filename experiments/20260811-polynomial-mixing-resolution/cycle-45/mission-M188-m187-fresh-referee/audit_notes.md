# M188 audit notes and numbered objections

Date: 2026-08-13 UTC.

## Decision

```text
REJECT M187 AS A CITABLE FROZEN PACKAGE.
SALVAGE ITS APPEND-ONLY CONTROLLING FINITE RESULT.
```

The controlling `final_scope.md` and `audit_correction.md` are unambiguous to
a reader who knows to privilege them. They correctly reduce the theorem to a
formal endpoint criterion and retain only the exact finite fourteen-route
result. But the package's ordinarily cited `proof.md` and nine-field
`report.md` still assert a superseded all-`d` geometric DPS locality theorem,
and `report.md` closes by requesting a referee of that invalid broader claim.
Because ordinary project citation points to `report.md`/`proof.md`, the
correction-by-separate-file does not make the frozen package safely citable.

## Numbered objections

1. **Material stale theorem in `proof.md`.** Section 3 labels the geometric
   pair/boundary-aligned DPS locality lemma and its all-`d` synchronized
   corollary as proved. `audit_correction.md` explicitly says that language is
   motivational only and is not an independently proved all-`d` theorem.
   These statements cannot coexist in one citable proof artifact without an
   inline retraction.

2. **Material stale theorem and verdict in `report.md`.** Fields 1, 4, 6, and
   9 promote the same superseded geometric theorem, including “This theorem
   is all-`d`” and a fresh-audit request to verify its rooted hypotheses. A
   standard citation of the nine-field report would therefore overclaim even
   though a later controlling file narrows it.

3. **Stale manifests/checkpoints and inconsistent inventory prose.** The
   original `freeze_manifest.md` declares the geometric theorem proved and
   describes a ten-file payload while omitting the later correction/control
   files. `checkpoint_final.md` and `halfway_checkpoint.md` retain the same
   stale scope. The controlling manifest correctly says every regular file is
   hashed, and the actual `SHA256SUMS` does hash all thirteen payload files, so
   integrity is not compromised; citation hygiene is.

4. **Route sequences not archived by M187.** `report.md` says “The other
   positive paths are stored by the checker,” but `targeted_results.json`
   stores only their count and length multiset. The deterministic checker
   recomputes them, so the numerical claim remains reproducible. M188 now
   archives and directly verifies all fourteen sequences; this is a
   reproducibility defect, not a refutation of the finite result.

## Salvaged statements

The following append-only corrected statements are independently accepted:

1. For the exact named `d=5`, width-two source pair, the ten rooted DPS
   reconstructions and seventy coordinate/root/edit targets yield 54 distinct
   eligible quotient target tuples.
2. Exactly fourteen of those targets occur in the signed-Hurwitz radius-five
   ball from the source tuple. Explicit paths have lengths
   `0,1,1,1,1,1,1,2,2,3,3,3,3,5` and every path directly replays.
3. Targets absent from that bounded ball are unresolved, not unreachable.
4. The exact endpoint criterion is formally true: all-zero-aligned selected
   endpoints use the empty word; all-one-step-aligned endpoints use `R_i`.
5. M135 matching perfectness does not imply either alignment condition; the
   every-color route remains unresolved.

No all-`d` geometric selection rule, route-length asymptotic, gap, mixing, or
Terminal conclusion is accepted.
