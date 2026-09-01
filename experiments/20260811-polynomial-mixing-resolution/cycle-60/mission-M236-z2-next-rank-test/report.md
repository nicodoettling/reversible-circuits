# M236 final report: the frozen Z2 formula survives the complete next rank

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
PROMOTE ONLY AN EXACT FINITE d=7 -> 8 NEXT-RANK THEOREM.
```

Outcome (a) occurs: there is no formula failure or same-Z2 behavior collision
on the complete primary template. This is not an all-rank theorem.

## Field 2 — immutable provenance

Every payload in M214/M218, M220/M223, M225/M228, and M231/M234 passes its
frozen checksum inventory. Their top `SHA256SUMS` digests are recorded in
`immutable_gate.md`, and their coordinator dispositions were reconciled at
L-0278, L-0281, L-0283, and L-0286. No predecessor was edited or imported.

## Field 3 — target and convention

There is no probability distribution or Markov kernel in M236. The target is
exact DPS endpoint correction

```text
N_(T,i)=F_7(T,s_i pi_7)(07)^2,
A_(T,i)=F_8(T+{{1,8}},s_i pi_8)
```

under chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

Every constructed endpoint evaluates to identity before comparison.

## Field 4 — predeclared formula and scopes

Before any next-rank endpoint was constructed, `immutable_gate.md` fixed
exactly M231's formula

```text
Z2=("closed",) if late OR ascent,
   ("open",v,epsilon) otherwise,

W=identity if closed,
  Q(v,epsilon) B_7 Q(v,epsilon)^-1 otherwise.
```

Only `d` changed from 6 to 7. The primary universe is ordinary odd edits
`{1,3,5,7,9}`. Internal even and the two boundary families are separately
reconciled and are not treated as Z2 rows. No endpoint-derived adaptation or
post-result exception exists.

## Field 5 — complete exact universe and formal checks

Direct seven-vertex Prüfer generation agrees with adjoining the fixed root
leaf to every six-vertex tree, giving exactly `6^4=1,296` trees. The checker
also verifies the carrier on all `8P4=1,680` ordered distinct-symbol choices
and 28 initial-run sign cases.

The primary table contains 6,480 rows; the secondary table contains 7,776;
the complete eleven-edit table contains 14,256.

## Field 6 — exact result

All rows pass:

```text
edit                 1      3      5      7      9
primary passes    1,296  1,296  1,296  1,296  1,296
primary failures      0      0      0      0      0
Z2 classes            9      6      4      3      2
```

There are 20 global Z2 classes and 20 primary words. The closed class has
2,974 rows; the 19 open classes have 3,506. Maximum finite route length is 21.

The fixed edits `{2,4,6,8,10,11}` pass 7,776/7,776. The full table passes
14,256/14,256 and uses 22 words. Both first-failure fields and the first
same-Z2 behavior-collision field are null.

## Field 7 — normalized digests and determinism

```text
tree universe   4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary rows    f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2 classes      30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
secondary rows  f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full rows       114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
results file    34e7a7a76b7993595b71a588d43afe85a443d851e722bb60b6e3d5f2bc3e1585
```

Two consecutive runs reproduce the result file byte-for-byte.

## Field 8 — reproduction and anti-lookup audit

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B z2_next_rank_check.py
```

The checker reads no inputs, imports no predecessor, assigns the descriptor
and route before endpoints, and performs no route search, endpoint lookup,
quotient-state enumeration, or group-element enumeration. Its only quotient
operation is a post-replay class census.

## Field 9 — strict reduction boundary and next step

```text
PROMOTE: the complete finite d=7 -> 8 route-normal endpoint theorem, with
6,480/6,480 primary and 14,256/14,256 full-table replays.

DO NOT INFER: all-rank DPS closure, every-color routing, polynomial route
length, comparison congestion, spectral gap, mixing, or Terminal.
```

The next mathematical obligation is an all-rank symbolic DPS closure proof;
another finite pass cannot substitute for induction. Freeze M236 and request
a fresh no-import audit of source order, completeness, formula fidelity,
endpoint replay, counts, and normalized digests.

