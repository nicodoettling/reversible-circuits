# M160 freeze manifest

Frozen: 2026-08-13 UTC.

## Environment and scope

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
python: 3.12.3
dependencies: standard library only
seed: null
owned directory: experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M160-m157-fresh-referee/
verdict: ACCEPT; no material or nonmaterial objections
```

The accepted claim is limited to M157's auxiliary normalized full unweighted
reset excursion.  There is no contraction, gap, polynomial-mixing theorem,
or project terminal.

## Durable command

```text
python3 -B independent_referee.py --output independent_results.json
```

A fresh run to `/tmp/m160_independent_results.json` reproduced the result
payload byte-for-byte with SHA-256
`845c6a4780631be4f037a1b2815c7e42bf4eff5fa392979fb8b968af1b40281c`.

## Frozen pre-manifest hashes

```text
ca1ac42e336142bbafe8fb14f6abeae1f8273e5405d7d58f299ea5a02f634c12  plan.md
8d49d92bb638673bf54d741ee0b817f9c85e3412aa9435859c0c84dd4e507d82  checkpoint.md
5acb1bd47038d1eecc4f8f504720ed2265ba6f7cb5f1c3b8b29b4b36065236a3  proof_audit.md
7f445fdcbf1da85315f556f94c9f730cccc8f4f48bb3ea749e8fc55f5ecf67ad  independent_referee.py
845c6a4780631be4f037a1b2815c7e42bf4eff5fa392979fb8b968af1b40281c  independent_results.json
dab3c237df698f4c03911a1baf62e2a6c37e2b69860a4a63360df608b085819c  report.md
```

## Validation and hygiene

- all seven M157 frozen hashes verified before inspection;
- clean-room checker `failure_count=0`;
- 504 shared-X posterior monomial identities and 16 mass rows checked;
- three selected exact reset/full-kernel equalities checked;
- exact `-165/512`, diagonal-trace fraction, and M152 polarization fraction
  reproduced;
- fresh `/tmp` JSON payload byte-identical;
- no predecessor code or data imported;
- no broad scan, package install, cache file, commit, or remote mutation;
- no predecessor, coordinator, manuscript, or skill file edited.

The authoritative final hashes, including this manifest, are in
`SHA256SUMS`.
