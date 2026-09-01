# M152 freeze manifest

Date: 2026-08-13 UTC.

## Scope and disposition

M152 proves the exact killed-atom beta-posterior identity and constructs a
global nonnegative beta-mixture/Jensen majorant for the normalized auxiliary
full-reset excursion.  It then refutes the entire associated pointwise
canonical-basin Jensen supersolution family as a uniform right-heavy
contraction certificate.

The exact obstruction is the fresh right-heavy state

```text
(s,kappa,D,B)=(9,2,1,3), L=6,
q=3176523/25000000,

V-(1-q)
 =5714491495302498676679596453643417785239504603683
  /223395363274892426079078092636160000000000000000000
 >0.
```

The true normalized excursion at the same state is approximately
`0.5663747547` and has positive budget slack approximately `0.3065643253`.
Thus M152 leaves the accepted M145/M149 right-heavy `L=6` theorem untouched.
It proves no all-suffix contraction, auxiliary gap, `ROOT-MEAN LIFT`,
original-chain gap, mixing result, or project terminal.

## Environment and deterministic command

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
dependencies: Python standard library only
seed: null
command: python3 -B beta_potential.py --output beta_potential.json --max-excess 6 --max-kappa 128
```

The final result payload SHA-256 is

```text
b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa  beta_potential.json
```

A second run to `/tmp/m152-beta-potential-rerun.json` reproduced that digest
and compared byte-for-byte equal.  The final run reports zero failures,
2,142 exact posterior/killed-atom monomial rows, five Jensen audits, 21 capped
boundary diagnostics, the explicit obstruction, a discrete-posterior
cross-check, and a separate exact reset/resolvent cross-check.

The capped passed rows are not universal claims.  An obsolete broader
boundary diagnostic was terminated after the exact witness was obtained; it
wrote no retained artifact and contributes no evidence.

## Accepted dependency hashes observed before freeze

```text
4b724f49eb6c47b7697ccb39f16b1a17fed693d17e259569898593898c0946f3  M140 report
7670f7f4717a81d427df68c24b4bd90a5e38e57ea7d8ae21caa437e79c86b6d2  M144 report
e760b6b7620e0278c8a21969112cb5675e268217d64d2319230f9642baecee11  M147 report
f98bd88222ad137d5402ab7dac730f02e04e12fc8372cf832ade85a759441b8c  M151 report
46bc88095f2223874341d820daa60ffe90f59815ab29aecc5156b0f645b815f4  M145 report
8db35d46cf6c3d3882ac5ff9d0f9f34cfab3b05f6fc94f202873ae86d88e76de  M149 report
05a65a8f6111029a93a1c06e1dc014579ae013ff3d0ccaa356050189437afb9c  M123 report
4a9e29d3bfa13940c06e4bc2d547c79f413e100e7437d97b6b58670ab07f97db  M128 report
```

M147/M151 supplies the exact attachment recurrence.  M140/M144 supplies
corrected-reset context but is not used in the Jensen inequality itself.
M145/M149 and M123/M128 are scope/route comparisons, not positive inputs to
the obstruction calculation.

## Owned inventory

```text
plan.md
checkpoint.md
beta_jensen_obstruction.md
beta_potential.py
beta_potential.json
report.md
freeze_manifest.md
SHA256SUMS
```

`AGENTS.md` names `references/experiments.md`, which is absent; the existing
skill-owned `.codex/skills/reversible-circuit-sampler/references/experiments.md`
was read and the mismatch was recorded rather than silently ignored.  The
default sandbox intermittently failed at `bwrap` loopback setup, so only
scoped approved repository reads, owned writes, and exact runs were used.
No package, network access, configuration change, predecessor edit, commit,
or push was attempted.  The generated Python bytecode cache was removed
before freeze.

