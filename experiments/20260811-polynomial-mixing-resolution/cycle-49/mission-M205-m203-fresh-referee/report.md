# M205 final report: fresh immutable referee of M203

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — exact verdict

```text
ACCEPT M203 AS FROZEN.
```

The exact finite obstruction and its narrow scope are correct: the naive
proof that embeds independent d=5 target routes while fixing an added filler
does not apply automatically at d=6. This verdict does not accept any d=6
nonreachability or all-d routing conclusion, because M203 makes none.

## Field 2 — immutable provenance and exact payload hashes

Before substantive comparison, `sha256sum -c SHA256SUMS` returned `OK` for all
twelve M203 payloads. The verified inventory was

```text
3117fda431e14bc7ef05e05b1f51804dbb2e05a21adda2af12f40d088264b918  plan.md
2fb9f851291776d5f2e5f8917e047d8e90caf700034e457c472da82216ac8a78  checkpoint.md
20c7dfadf209e429926644b1602146e3eb237a9066f0f76d7b53fa859afe94b0  immutable_gate.md
b0e327599b4efefb1df56a0a42f70a72af59ca6803b10c90cf519ba374f0cc6c  halfway_checkpoint.md
2f1b8f6122e870486b178a1350e25d56339430386ac42973b4411edbf0ffc5cf  locality_probe.py
eb6c19276c511dc51900ec7848fd6059d557e7c4d58ad0cad4f53475ce6b3b45  run_locality_d56.py
f49bd2b327e8867c49ff27e81e6b01efc82c67b0d8d23b9f3f33ddcbfda6379a  locality_results.json
1a13a66ce16543f91fc200c1b54f83f758b66d78bc04b0debd14384987b1fafa  leaf_stabilization_probe.py
5779eac90d13c32279c26276e98f35db35c0898d415d83fff9ab7573ea89aeba  leaf_stabilization_results.json
ef9735b7d1a36b7aed14259d46b92b14825ed2fba7b09928f90f394be400fc68  obstruction.md
ade8960f2648f1881d2e3b92a83163d8befe221fea435e32bd3cfd8d6f0adcc5  report.md
b622b691ae327bab80c46968ba6578cd7f7c07c2fe8942f722f3338275a60f5c  freeze_manifest.md
```

The digest of M203's `SHA256SUMS` is
`584d5110354693e3d5979fc6c1e83193e24754fcba4f51f035c9415cba3816e6`.
M203 was never edited.

## Field 3 — audited claim and declared scope

The audit covers only M181's two explicit `r=1` source patterns at d=5 and
d=6, all root relabelings, all adjacent DPS-value edits, literal nominal
six-factor locality, d=6 active/filler cross-coupling, and fourteen named
d5-to-d6 leaf-stabilization comparisons.

There is no target probability distribution or Markov kernel in this finite
combinatorial mission. No quotient graph `Q_6` was enumerated.

## Field 4 — independent method

`fresh_locality_referee.py` imports no M203 code. It independently generates
Cayley trees by Prüfer codes, reconstructs rooted DPS descriptors from the
hairy-tree boundary closure, applies the adjacent-value edits, and completes
its d=5,6 row table before reading either frozen JSON artifact.

For the fourteen quotient comparisons it computes the exact lexicographically
minimal representative over every global label permutation. Equality is first
decided on those representatives; SHA-256 is only a compact archival digest.

## Field 5 — factor-locality and cross-coupling replay

The reconstruction produced exactly 70 d=5 rows and 108 d=6 rows. Its complete
normalized row-table digest is
`3144898428d5ec658c5fcda682c445b79c92123703bb53b700af237a741fb3ac`,
identical to the separately normalized frozen table, with zero mismatched
rows.

Exact reproduced totals are:

```text
all rows                                      178
adjacent-factor locality failures            110
six-factor-region locality failures          106
  d=5 / d=6 split                         43 / 63
d=6 active edit (i<=5) changes filler          29
d=6 filler edit (i>=7) changes active block    22
```

The distinguished pattern-0/root-5/edit-1 descriptor is recovered after 37
trials. It changes positions `[2,5,6,9]`; position 9 is in the added `(05)^2`
filler. The exact source and target in `proof_audit.md` and
`referee_results.json` match M203.

## Field 6 — fourteen quotient comparisons and first witness

The clean comparison table has digest
`90a3781b721fd01ad22ce0c77dd2e30df6a32957c61e74fac8356589494ab857`,
identical to frozen M203, with no mismatched comparison. Exact classification:

```text
equal:   (0,2) (0,4) (0,6) (1,2) (1,4)
unequal: (0,1) (0,3) (0,5) (0,7) (1,1) (1,3) (1,5) (1,6) (1,7)
```

Thus the reproduced count is 5 equal and 9 unequal. The first exact unequal
canonical representatives have the recorded digests

```text
naive d5 target plus (05)^2:
bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f

actual d6 matched target:
bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b
```

## Field 7 — proof logic and numbered objections

The independent-block argument needs the actual enlarged matched target to be
globally relabeling-equivalent to the old target with fixed complement. The
pattern-0/edit-1 representative inequality falsifies that necessary premise,
so M203's stated no-go follows.

Numbered objections:

1. None. The data, exact representative test, logical implication, and scope
   language all survived the clean replay.

## Field 8 — reproducibility and hygiene

Environment: Python 3.12.3; nonstandard dependencies `{}`; seed `null`.
Command:

```text
timeout 120s python3 -B fresh_locality_referee.py
```

The clean replay completed in 0.778 seconds. All writes were confined to M205;
there was no M203 modification, quotient enumeration, cache creation, or
external dependency. `referee_results.json` archives the row/comparison
digests, counts, first witnesses, exact mismatch lists, and scope conclusion.

## Field 9 — accepted boundary and disposition

```text
ACCEPT: M203 refutes only the naive independent d5-block plus fixed-filler
proof route.

DO NOT INFER: d6 target nonreachability, failure or success of another all-d
route theorem, quotient/corrected route length, polynomial mixing, spectral
gap, or Terminal.
```

M181's all-d source-voltage result and the finite d=5 route results remain
outside the claim being refuted. Freeze M205 and return its hashes for
coordinator synthesis.

