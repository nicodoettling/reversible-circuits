# M329 run manifest

Date: 2026-08-14 UTC

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Random seeds: none; deterministic checksum audit only.
- Nonstandard dependencies: none.
- Writable scope: this M329 directory only.
- Immutable inputs: M323 and M326.

Commands, run from the indicated frozen package directory as applicable:

```text
ls -1A
sha256sum plan.md checkpoint.md halfway_checkpoint.md dependency_audit.md proof_audit.md salvage_obligation.md report.md run_manifest.md final_checkpoint.md freeze_manifest.md
awk '{print NR, length($1), $0}' SHA256SUMS
sha256sum SHA256SUMS
sha256sum -c SHA256SUMS
git rev-parse HEAD
```

The unavailable `rg` executable was not needed; `ls -1A` supplied the exact
eleven-file M326 inventory. No code, guard, search, or stochastic computation
was run.

