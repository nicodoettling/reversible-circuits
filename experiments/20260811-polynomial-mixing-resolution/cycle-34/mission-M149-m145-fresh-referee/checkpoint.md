# M149 checkpoint

Date: 2026-08-13 UTC.

## Provenance and reconciliation

All six supplied M145 SHA-256 values matched exactly before inspection:

```text
plan        eef285e14c41ba475dac8c16bfeb9500188935807f766f98ddbacb4d45385231
checkpoint  4b7519915ee8ca97c4483c818a99b020fa0a589196ac05d5a49ab602eaa70182
proof       6e0af764322dcde3108f6b35102f9a7f334c427077ae5ae5de95ce0bbe84e65d
checker     9ec575eea344e9ea57e9561b29fdfa3dc3c7c982fe5f0052fbf61b853423e314
JSON        a3583b387a6553fcdbf156fdb3f37bf71f077c729a400983f79ebfa81513c6fc
report      46bc88095f2223874341d820daa60ffe90f59815ab29aecc5156b0f645b815f4
```

Exactly those six files are immutable for this audit.  The predecessor
`__pycache__` was observed and left untouched as instructed.  M140's scalar
lemma and M144's fresh ACCEPT report were read and reconciled as M145's only
new scalar dependency; the accepted M109/M114 recurrence and M117/M121
arbitrary-deficit lower-excess boundary were also inspected.

## Halfway mathematical status

- The literal ordered-composition support formula gives `2^6=64` rows.
- Nonempty first-prefix cuts give `2^6-1=63` exceptional endpoints.
- Group degree ranges yield 22 positive groups, 16 deep live groups, and
  `20+14+9+5+2+1=51` nominal positive attachment ranks.
- At `s=7`, all 20 ranks at height one lead to auxiliary rank-one targets;
  their terminal split is one, so 31 ranks remain with nonzero structural
  charge.
- The proof's full-basin reset normalization is internally consistent:
  removing ordinary energy `q^2 c_E lambda_E^2=q^2 b_E lambda_E` and restoring
  the exact exceptional square uses one power of `lambda_E` on full basin
  mass `b_E`.  It is distinct from rejected `a_E lambda_E^2`.
- M145's code retains every `j=1,...,k` before applying the rank-one boundary
  and sends a child to excess `h-1` and deficit `D+k-j`.

## Remaining audit

Implement the clean-room recurrence and a Bernstein conversion that does not
reuse M145's source.  Regenerate finite/tail coefficient families, verify the
`761/763` arbitrary-deficit extremum and literal/grouped equality, prove the
degree/multiaffinity assumptions used by interpolation, then issue the final
dependency-scoped verdict and freeze owned artifacts.

## Environment

The default workspace sandbox fails during `bwrap` loopback setup with
`RTM_NEWADDR: Operation not permitted`; scoped approved escalated commands are
being used only inside the assigned repository paths.  No package,
configuration, commit, or push action is planned.

