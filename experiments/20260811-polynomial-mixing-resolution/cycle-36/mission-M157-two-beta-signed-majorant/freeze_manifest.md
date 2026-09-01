# M157 freeze manifest

Frozen: 2026-08-13 UTC.

## Environment and scope

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
dependencies: standard library only
seed: null
owned directory: experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M157-two-beta-signed-majorant/
```

The frozen claim is limited to the auxiliary normalized full unweighted
reset excursion.  It contains no auxiliary gap, original-chain gap,
polynomial mixing theorem, or project terminal.

## Durable command

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M157-two-beta-signed-majorant/two_beta_exact.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M157-two-beta-signed-majorant/two_beta_exact.json \
  --max-B 3 --max-excess 6 --max-kappa 16
```

Fresh payload comparison used the identical command with output
`/tmp/m157_two_beta_exact.json`.  Both JSON payloads have SHA-256
`ad7714307a2c66afe6a3f8a375001a794fd8b1d935a4b0ee81cb612eea1d1832`.

## Frozen pre-manifest hashes

```text
2b26b2041ce84d4ccc737316873c3022c2e7a5e852cbff0bb71bb2eeafb580a3  plan.md
f10489f356cf5b5ce1d3d793d44bc11913f315f478dba20a0db80edac219c694  checkpoint.md
e3dcd4d5c3c01d4c146fab67def1c025342f89185a3ba5dc957bbfd10df1eae3  two_beta_theorem.md
a86672353beefa2b048dc45f57fd70cd3756dacaae0fd1b7b587f0d07a507741  two_beta_exact.py
ad7714307a2c66afe6a3f8a375001a794fd8b1d935a4b0ee81cb612eea1d1832  two_beta_exact.json
c9f3317574fafa9daf1d1c08be625132a879716cb876914065d783b28cfe22c2  report.md
```

## Validation gate

- checker output: `failure_count=0`;
- 51,840 shared-X transfer monomial rows;
- 720 retained/killed transfer-mass rows;
- 2,520 reset two-copy equalities;
- seven full signed-kernel equality rows;
- exact M152 witness and both new obstruction fractions reproduced;
- fresh `/tmp` JSON payload byte-identical by SHA-256;
- JSON parsed successfully;
- no `__pycache__` or `.pyc` remains in the owned directory;
- no predecessor, coordinator, manuscript, project skill, package,
  configuration, commit, or remote state was changed.

The authoritative final digests, including this manifest, are in
`SHA256SUMS`.
