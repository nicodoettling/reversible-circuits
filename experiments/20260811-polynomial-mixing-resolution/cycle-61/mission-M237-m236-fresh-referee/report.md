# M237 final report: fresh referee of frozen M236

Date: 2026-08-13 UTC.

## Verdict

```text
ACCEPT M236 AS FROZEN.
```

Accepted scope is exactly the complete finite `d=7 -> 8` one-leaf endpoint
table.  This is not an all-rank theorem.

## Target and convention

There is no probability distribution or Markov kernel in this mission.  The
target is deterministic endpoint correction

```text
N_(T,i)=F_7(T,s_i pi_7)(07)^2,
A_(T,i)=F_8(T+{{1,8}},s_i pi_8)
```

under chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

Every independently constructed endpoint evaluates to identity.

## Immutable source audit

All ten frozen M236 payload checksums pass, its directory inventory is exact,
and its top `SHA256SUMS` digest is

```text
0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a.
```

Static inspection confirms a no-input checker and the decisive ordering
`descriptor -> formula -> endpoints -> replay`.  There is no route search,
target lookup, endpoint-derived descriptor, quotient/group enumeration, or
formula adaptation.  The immutable-gate/source/result modification times are
ordered consistently with predeclaration; they are not an external
cryptographic timestamp.

## Clean-room reconstruction

`independent_referee.py` reads no inputs and imports no M236 code, data, or
project module.  It constructs the root-leaf universe both by filtering every
seven-vertex Prüfer code and by adjoining `{1,7}` to every six-vertex tree;
the two 1,296-tree sets agree exactly.  It independently implements the DPS
boundary closure, assigns M231's `Z2` and literal formula before endpoints,
and performs exact chronological replay.

The formal audits pass all `8P4=1,680` carrier substitutions and all 28
initial-run sign cases.  The unedited source-extension identity passes on all
1,296 trees.

## Exact result

All declared rows pass:

```text
edit                 1      3      5      7      9
primary passes    1,296  1,296  1,296  1,296  1,296
primary failures      0      0      0      0      0
Z2 classes            9      6      4      3      2
closed rows          864    756    624    463    267
open rows            432    540    672    833  1,029
```

There are 6,480 primary passes, 20 global `Z2` classes, 2,974 closed rows,
3,506 open rows, 20 primary formula words, and maximum finite length 21.  The
primary length histogram is
`{0:2974,5:1029,9:833,13:672,17:540,21:432}`.

The fixed edits `{2,4,6,8,10,11}` pass 7,776/7,776.  Thus the complete table
passes 14,256/14,256, uses 22 words, and has histogram
`{0:8158,1:1296,2:1296,5:1029,9:833,13:672,17:540,21:432}`.  Both first
failure fields and the first same-`Z2` behavior-collision field are null.

## Normalized certificate replay

The independently fixed native table was later encoded in M236's published
normalization, without any runtime read of M236.  Every digest agrees:

```text
tree universe   4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary rows    f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2 classes      30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
primary words   3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608
secondary rows  f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full rows       114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
full words      d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c
```

Two consecutive final runs reproduce `referee_results.json` byte-for-byte at
SHA-256
`f2f36b7ba75d9bdf978dd07d0b132183f914551df832a3fd528bd5d7342da037`.
Environment: Python 3.12.3, dependencies `{}`, seed `null`; command
`python3 -B independent_referee.py`.

## Numbered objections

Material objections:

1. None.

Nonmaterial qualifications:

1. M236's predeclaration chronology is supported by its written assertion,
   frozen checksums, and modification-time ordering, but not by an external
   cryptographic timestamp.  This does not affect the independently replayed
   finite equalities.

## Accepted boundary

Accepted as **proved by exact finite exhaustive replay**: M231's predeclared
route-normal formula closes every primary endpoint and the fixed formulas
close every secondary endpoint in the complete `d=7 -> 8` one-leaf template.

Not inferred: an all-rank DPS closure lemma, every-color or
arbitrary-representative routing, a polynomial route-length theorem,
comparison congestion, spectral gap, polynomial mixing, or Terminal.

