# M129 freeze manifest

Frozen: 2026-08-13 UTC.

Mission: fresh referee of M125's exact defect-mass recurrence.

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Verdict: **ACCEPT** with zero objections.  Relative to the already accepted
M113/M118 exact cell formula, the rooted partition recurrences, connected-
unicycle extraction, cycle-type coefficient formula, multiset aggregation,
and `c=1` repair are proved.  The `d=4` ULC claim is refuted exactly.  Ordinary
log-concavity and unimodality through `d=22` are exact finite facts only.
Universal ordinary log-concavity, DEFECT NO-VALLEY, all downstream gaps, and
the original lazy `{3,4,5}` heat-bath gap remain unresolved.  No terminal
result follows.

## Frozen M129 payload

| file | SHA-256 |
|---|---|
| `plan.md` | `22663a062a5f20a6cf893127d55a711370ab3c9ac5577ca6c1710cc0ec6d8497` |
| `checkpoint.md` | `dfe91ecf53d85ae1a00b42b60cf010c8f086ea12355c6f6c076f262df2d7724a` |
| `independent_referee.py` | `c9e473ec62b78a0e37fc59211877d8a017327fc625ebdfdf2b8899f7714839b4` |
| `independent_results.json` | `96a880122c2a745fe7032d90442ddfcb2ed762d0723345e47630f76cc7604fee` |
| `report.md` | `eb7cdcd179a704deed4a8b7cb03a7a69c912bc0b57677a7fb2d886d17056b2d4` |

## Frozen source and reference integrity

The complete M125 `SHA256SUMS` set passed before audit.  The supplied source
hashes matched:

| M125 artifact | SHA-256 |
|---|---|
| `report.md` | `dc8f8cb0ab9c6c06f9b49cd56a30b29cc258698dcdfccceb887b265ff67c5879` |
| `freeze_manifest.md` | `a6bb1090f1a6f88c38ddd253ec35069e062f9a00563096ae1d0617370b7befdd` |
| `audit_recurrence.py` | `0061794c17ae1e2ea3e374adf03dc923fc7d2283f0ba59b80617b9299ec0bb62` |
| `audit_results.json` | `b33f8c39961d2080ff01c71b882c5df229766f94ae7f1daac78fc7747f63bfb6` |
| `defect_recurrence.md` | `068a42ed4c9141cbabd81ffe35d352c833b634a295a9a6a6f44dabbeb09ffde1` |
| `exact_results.json` | `01938aab9d001597991d13efb3dd0583d61b629c776cfcd2f4ccfde023588131` |
| `SHA256SUMS` | `f58c059ae432fd04fc33ed25da26e25ca54e5036739963810ef07670e7371d09` |

M124's complete checksum set also passed.  Its independently frozen exact-key
`results.json` hash is
`36b898a0f987d7df114a0c9ef4cb433441f114f1fe3d03495b9cc88152163553`.

## Reproduction and validation

From the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-27/mission-M129-m125-fresh-referee/independent_referee.py \
  --max-d 22 --direct-max-d 6 --recurrence-compare-max-d 8 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-27/mission-M129-m125-fresh-referee/independent_results.json
```

Environment: Python `3.12.3`, standard library only, exact deterministic
arithmetic, `seed=null`.

Validation at freeze:

- zero failures in the fresh checker;
- 23 direct cycle-type cases and 47,728 literal partition-pair tests through
  `d=6`;
- 58 indexed-versus-multiset recurrence cases through `d=8`;
- exact agreement with M124 rows `d=2,...,5` and M125 rows `d=2,...,22`;
- exact primitive `d=4` row `(627,1520,1113)`, ordinary margin `1612549`,
  and ULC margin `-481004`;
- all rows through `d=22` unimodal and ordinarily log-concave; every tested
  row `d>=4` non-ULC;
- Python source compiles in memory, JSON parses, owned-directory whitespace
  and checksum checks pass;
- no Python cache remains, no package was installed, and no file outside the
  owned M129 directory was edited.

`SHA256SUMS` hashes all payload files above and this manifest.  It
intentionally does not hash itself.
