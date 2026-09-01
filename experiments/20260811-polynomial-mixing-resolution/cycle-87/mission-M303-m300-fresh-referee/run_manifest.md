# M303 run manifest

Date: 2026-08-14 UTC.

```text
repository commit: 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
Python: 3.12.3
nonstandard dependencies: none
deterministic: yes
random seed: null
target: frozen M300 designated channel-one all-middle coefficient reduction
permutation convention: (pq)(x)=p(q(x)); displayed factors left-to-right
new finite ranks: exactly k=7, n=21
```

Single independent reconstruction command, run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-87/mission-M303-m300-fresh-referee/independent_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-87/mission-M303-m300-fresh-referee/independent_results.json
```

The script uses only the Python standard library, imports no project,
predecessor, or M300 code/data, and contains `k=7` as a fixed constant.  No
second rank was evaluated.  The computation is an exact finite audit only.

The M300 and eight predecessor inventories were checked with
`sha256sum -c SHA256SUMS` from inside each frozen mission directory.  Proof
and referee passages were then inspected, followed by the independent
analytic reconstruction in `independent_reconstruction.md`.
