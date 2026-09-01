# M156 checkpoint

Date: 2026-08-13 UTC.

## Source reconciliation

Read `HANDOFF.md`, `GOAL_SPEC.md`, the complete project skill, its sampling
problem and experiment references, and the relevant manuscript theoretical
status.  `AGENTS.md` names repository-level `references/experiments.md`, which
is absent; the skill-owned
`.codex/skills/reversible-circuit-sampler/references/experiments.md` was read
and this mismatch is retained explicitly.

The accepted M147 recurrence and M151 normalization audit were also inspected
to fix the exact meaning of `H/q`, the killed `j=0` branch, and the child
coordinates.  The M145/M149 result is used only for scope: right-heavy suffix
excess six is already accepted and is not being reproved here.

## Immutable gate

All supplied hashes match the frozen files byte-for-byte:

```text
f1dafebd7f6722a16abedbf5382ad433e729f5294295f06b23fb6d82eb97bd70  report.md
dfebb6c250f6c4fcf0eaf44da961d0887613ad28012689b52b6a40c441023b6d  beta_jensen_obstruction.md
5c9cd1a4693859147d0f356f30e997e2d3e8c1c04f6ead4c8d4ff4740edf4388  beta_potential.py
b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa  beta_potential.json
0c444c254bd49c008cd4836f14d16ecc43aa8aace628e5177278e2457304db51  freeze_manifest.md
141a6d131e4d1c36e6d5d2716d249ee157544084269e28ac78c279ba02fc94c6  SHA256SUMS
```

A deterministic rerun of the frozen checker to `/tmp` reproduced the JSON
digest exactly and reported zero failures.

## Audit target frozen

The candidate conclusion is deliberately narrow: M152 may prove a global
majorant and refute the associated pointwise canonical-basin Jensen
supersolution family, but it may not be read as refuting arbitrary
deficit-aware potentials or the accepted true `L=6` contraction.

