# Mission M248 checkpoint

## Initial checkpoint

- Status: active; no mathematical inference made yet.
- The mission directory, plan, and checkpoint were initialized before substantive dependency work.
- The project skill has been read in full.
- Next action: read the repository source-of-truth files and then line-audit the four immutable dependency pairs.

## Dependency and formula checkpoint

- All frozen inventories in M217/M222, M226/M229, M235/M238, and M239/M246 pass `sha256sum -c SHA256SUMS`.
- Their checksum-file digests are, in the same order:

      M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
      M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
      M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
      M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688
      M235 7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527
      M238 eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8
      M239 66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542
      M246 df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97

- Exact alignment found:
  - M226/M229 identifies `S_Y+K_Y` with the YCM prefix.
  - It identifies `(S_X+K_X)-(S_Y+K_Y)` with the TCM prefix, preserving all literal kinds, seams, and collision multiplicities.
  - Accepted YCM (`7000`) therefore gives Y-WBE; YCM plus accepted TCM (`160`) gives X-WBE with `7160` by one triangle inequality.
  - M217/M222 gives `DE_Z=S_Z+K_Z+N_Z` and the explicit ratio bound `a_F/a_L-1 <= 16/(3k^2)`. Since `B_s^Z<=3` and `sum_s q_s=1`, `|N_Z|<=16/k^2`.
  - On `k>=3`, `ell>=2`, the integer inequality `k^2 ell>=18>16` implies `16/k^2<=4 sqrt(ell)/k`. Thus DE constants `7004` for Y and `7164` for X are available.
- No disagreement among the frozen claims was found. M229's domain qualification `1<=x<=(3k-3)/2` is already enforced by M239/M246 and does not affect this assembly.
- No downstream claim has been inferred.

## Final checkpoint

- Status: theorem, proof, report, checker, result record, manifest, and fresh-audit request complete.
- The compact no-import checker passes through every odd `k<=1001`, every admissible split, and every admissible cutoff; `git diff --check` on the mission path passes.
- Frozen verdict: WBE constants `7000` (Y) and `7160` (X); normalizer remainder `16/k^2`; signed averaged DE constants `7004` (Y) and `7164` (X), subject to fresh immutable audit.
- DV and every stated downstream claim remain open.
