# M156 freeze manifest

Date: 2026-08-13 UTC.

## Verdict and exact scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

Frozen M152 proves a global beta-Jensen majorant with the killed `j=0` atom
charged exactly.  Its right-heavy witness at
`(s,kappa,D,B)=(9,2,1,3)`, `L=6`, refutes the entire pointwise
canonical-basin Jensen supersolution family as a uniform contraction
certificate.  It does not refute sharper deficit potentials or the true
right-heavy inequality.  The independent exact true-excursion slack is
approximately `0.3065643253`, so accepted M145/M149 remains intact.

No all-suffix contraction, auxiliary gap, `ROOT-MEAN LIFT`, original-chain
gap, polynomial mixing theorem, Terminal A, or Terminal B follows.

## Frozen predecessor hashes verified

```text
f1dafebd7f6722a16abedbf5382ad433e729f5294295f06b23fb6d82eb97bd70  M152 report.md
dfebb6c250f6c4fcf0eaf44da961d0887613ad28012689b52b6a40c441023b6d  M152 beta_jensen_obstruction.md
5c9cd1a4693859147d0f356f30e997e2d3e8c1c04f6ead4c8d4ff4740edf4388  M152 beta_potential.py
b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa  M152 beta_potential.json
0c444c254bd49c008cd4836f14d16ecc43aa8aace628e5177278e2457304db51  M152 freeze_manifest.md
141a6d131e4d1c36e6d5d2716d249ee157544084269e28ac78c279ba02fc94c6  M152 SHA256SUMS
```

## Independent computation

```text
repository base commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
dependencies: Python standard library only
seed: null
predecessor imports: none
broad scan: none
command: python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M156-m152-fresh-referee/fresh_referee.py --output experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M156-m152-fresh-referee/fresh_referee.json
```

The clean-room checker enumerates literal roots, not the frozen grouped-root
implementation.  It reports zero failures, 21 full/retained/killed Doob
checks, 280 literal-source context checks, exact equality of polynomial and
discrete-posterior majorants, and exact agreement with every witness/reset/
descendant/true-excursion fraction.  A second run to `/tmp` reproduced

```text
b9fe0bde90e70c083a825cf61579be6ec8473808ccd48dce0059f0ef8419359f  fresh_referee.json
```

## Frozen owned inventory

```text
4a98450c166475e3f03a6cc38210047103772c90c0c159a1bb28b4483f0087f1  plan.md
444e6aae2aa088e5f960ee3218198d5a81e49cf0245ba806f9448388bffed14f  checkpoint.md
af10a0ea7b1956dbd1ab675a9aedfa704ea1878713305d8df288c58f3a954df7  fresh_referee.py
b9fe0bde90e70c083a825cf61579be6ec8473808ccd48dce0059f0ef8419359f  fresh_referee.json
2dcd6b06f96bf9915b946e3c0b0e907cf01f6541ed14c85a78f5876d38ea7790  proof_audit.md
752641647ef1b5631264f8e304403db0d44c55af9e587d383d07720cd03eb1f4  report.md
```

Only this assigned M156 directory was edited.  No predecessor, coordinator,
manuscript, skill, package, machine configuration, commit, or remote state was
changed.  The repository-level `references/experiments.md` named by
`AGENTS.md` is absent; the skill-owned experiment reference was used and the
discrepancy was recorded.

