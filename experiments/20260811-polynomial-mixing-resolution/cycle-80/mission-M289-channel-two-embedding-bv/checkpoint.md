# M289 checkpoint

## Initial checkpoint (pre-inspection)

- Mission directory initialized before inspecting any substantive frozen
  predecessor artifact.
- Target fixed to the exact channel-two embedding vector `CEBV`; no
  downstream inference is in scope.
- The project skill has been reread.  No predecessor code or data has been
  imported, and no frozen predecessor has been modified.
- Next: finish the required repository-source reading, verify all ten frozen
  checksum ledgers, and reconstruct the literal coefficient from completion
  counts.

## Substantive checkpoint

- Every payload named by the frozen ledgers for M192/M195, M199/M207,
  M217/M222, M276/M279, and M282/M286 verifies `OK`; their checksum-file
  SHA-256 digests are recorded in `run_manifest.md`.
- The literal B and A raw support-pair profiles have been reconstructed.  The
  exact normalizer collapse is

  ```text
  H=sum_s q_s[(a_F(s)/a_L(s)) B_s-A_s]
   =sum_s q_s(B_s-A_s)+sum_s q_s(a_F(s)/a_L(s)-1)B_s.
  ```

  The second term has full circular variation `O(k^-2)`.
- A two-seam/one-seam comparison lemma controls the signed first-edge term.
  Generalized support-pair stabilization controls the B marked components,
  the A marked components, and the untouched A component before phase
  embedding.  The cross-block term is a single triangular coefficient with
  variation `O(k^-1)`.
- One clean-room checker, fixed only after the formulas, compares direct
  minimal-completion enumeration with every raw formula at `k=3,5`; all
  exact assertions pass.  The formula scan at `k=3,5,7,9,15,31` is only a
  convention/boundary falsification and is not used for the theorem.
- Current verdict: **CEBV proved for every odd `k>=3`, subject to a fresh
  immutable audit.**  No downstream inference is made.
