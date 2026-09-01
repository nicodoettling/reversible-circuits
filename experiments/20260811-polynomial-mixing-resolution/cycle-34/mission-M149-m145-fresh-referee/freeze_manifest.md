# M149 freeze manifest

Frozen: 2026-08-13 UTC.

## Verdict and scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

Accepted only: the auxiliary full nonlazy stationary-flow parking-degree
right-heavy suffix-excess-six inequality for every `s>=7,K>=1`, relative to
the accepted recurrence/lower-excess inputs and accepted M140/M144 scalar
bound. No all-`L`, weighted gap, ROOT-MEAN LIFT, original-chain gap, mixing,
Terminal A, or Terminal B claim is included.

## Immutable M145 gate

Exactly six predecessor files were assigned and verified:

```text
eef285e14c41ba475dac8c16bfeb9500188935807f766f98ddbacb4d45385231  plan.md
4b7519915ee8ca97c4483c818a99b020fa0a589196ac05d5a49ab602eaa70182  checkpoint.md
6e0af764322dcde3108f6b35102f9a7f334c427077ae5ae5de95ce0bbe84e65d  suffix_excess_six.md
9ec575eea344e9ea57e9561b29fdfa3dc3c7c982fe5f0052fbf61b853423e314  l6_exact.py
a3583b387a6553fcdbf156fdb3f37bf71f077c729a400983f79ebfa81513c6fc  l6_exact.json
46bc88095f2223874341d820daa60ffe90f59815ab29aecc5156b0f645b815f4  report.md
```

The clean-room checker verifies this gate before computation. No predecessor
file or cache was edited or deleted.

## Accepted dependencies inspected

- M109/M114: all-rank finite-DAG recurrence, nilpotence/descent, suffix
  terminal theorem, and positive-history `G<=H`.
- M117/M121: accepted arbitrary-deficit lower-excess envelope used by the
  recursive audit boundary.
- M140/M144: universal scalar `C_S<3/4` for all `S>=100` and corrected L5
  dependency. Observed proof/report hashes:

```text
d8e49d7e06eb82f45621febb3107e75d0ab35eea440402db083797675e994bb6  M140 proof
7670f7f4717a81d427df68c24b4bd90a5e38e57ea7d8ae21caa437e79c86b6d2  M144 report
```

M131's rejected two-power display is negative provenance only.

## Reproduction

From this directory:

```text
python3 -B cleanroom_referee.py --output cleanroom_referee.json
```

Python 3.12.3; standard library only; exact `Fraction` arithmetic;
deterministic `seed=null`. Final result: `status=ACCEPT`, zero failures,
finite/tail digests exactly matching M145.

## Owned pre-freeze hashes

```text
5f24d911368fcbaff1b65690f7fb432280c37a77c1a507c057fd2a3c60375bb3  plan.md
ca556f97d3e651eaeb7c0ddb17718d7448678d8248b81aa0a9a6f8772a831df8  checkpoint.md
a9e924f2dd77ee7b0c0d360ae54ca963a2e15221bf6ec212fcca966cc072a500  cleanroom_referee.py
7cacc0f0bb5a44d107bab1851034837115c7ee6f3916068223d3962ee27c8787  cleanroom_referee.json
8db35d46cf6c3d3882ac5ff9d0f9f34cfab3b05f6fc94f202873ae86d88e76de  report.md
```

`SHA256SUMS` is the final inventory and includes this manifest. No cache is
retained. No package, machine configuration, commit, or push action occurred.

