# Exact finite `d=7 -> 8` route-normal correction theorem

Date: 2026-08-13 UTC. Status: **proved for the complete declared finite
template only**.

## Statement

Let `T` range over all trees on `[7]` in which root 7 is a leaf adjacent to
vertex 1. There are exactly

```text
6^(6-2)=6^4=1,296
```

such trees, by deleting the fixed leaf. For the canonical rooted order

```text
pi_d=(2d-3,2d-2,1,...,2d-4)
```

and each ordinary odd inherited edit

```text
i in {1,3,5,7,9},       i=2v-3,
```

define

```text
N_(T,i)=F_7(T,s_i pi_7)(07)^2,
A_(T,i)=F_8(T+{{1,8}},s_i pi_8).
```

The chronological signed right-Hurwitz convention is

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

Root `T` at 7. Let `P(v)=(v,p(v),...,1)`, let `lambda` record whether an
internal vertex of `P(v)` is greater than `v`, and let `alpha` record whether
two consecutive internal path entries ascend. Put `L=7-v-1`; for `0<=t<L`,
define

```text
c_t=1 iff p(v+t+1)=v,
epsilon_0=-1 if c_0=1, else +1,
epsilon_t=-1 if c_t=1, else -epsilon_(t-1).
```

Use exactly the M231 route-normal descriptor and word

```text
Z2(T,v)=("closed",)                    if lambda OR alpha,
         ("open",v,epsilon)            otherwise,

W(T,v)=identity                        if lambda OR alpha,
       Q(v,epsilon) B_7 Q(v,epsilon)^-1 otherwise,

Q(v,epsilon)=product_(t=0)^(L-1)
  R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t,

B_7=R_10^- R_11 R_12^- R_11^- R_10^-.
```

Then for every one of the `1,296*5=6,480` pairs `(T,i)`, literal action by
`W(T,v)` sends `N_(T,i)` exactly to `A_(T,i)`.

This produces exactly 20 occurring `Z2` classes and 20 literal formula words.
The class counts by edit are

```text
edit                 1      3      5      7      9      global
Z2 classes           9      6      4      3      2          20
closed rows        864    756    624    463    267       2,974
open rows          432    540    672    833  1,029       3,506
passes           1,296  1,296  1,296  1,296  1,296       6,480
failures             0      0      0      0      0           0
```

The primary route-length histogram is

```text
length       0      5     9    13    17    21
rows     2,974  1,029   833   672   540   432.
```

Thus the maximum correction length in this finite table is 21.

## Fixed-family reconciliation

The six non-Z2 families use the already declared fixed words

```text
edits {2,4,6,8} -> identity,
edit 10          -> (R_9^-)^2,
edit 11          -> R_12^-.
```

They pass all `1,296*6=7,776` rows. Consequently the complete eleven-edit
finite table passes all 14,256 rows, uses 22 distinct words, and has route
length histogram

```text
length       0      1      2      5     9    13    17    21
rows     8,158  1,296  1,296  1,029   833   672   540   432.
```

These six families are not Z2 rows and do not affect the primary quotient
claim.

## Literal-word kernel

At fixed `d=7`, `Z2` is exactly the kernel of the displayed literal word map
on occurring descriptor values. The closed class uniquely has length zero.
An open word has length `4L+5`, which determines `v`, and the first differing
entry of `epsilon` changes the first signed transport pair where the words can
differ. This syntax lemma is independent of endpoint correctness.

## Exact proof certificate

`z2_next_rank_check.py` reads no input file and imports no predecessor. It:

1. constructs the tree universe both by direct seven-vertex Prüfer codes and
   by adjoining `{1,7}` to every six-vertex tree, and asserts equality and the
   exact count 1,296;
2. verifies the five-move carrier on all `8P4=1,680` ordered choices of four
   distinct symbols;
3. assigns `Z2` and the literal formula word before constructing either
   endpoint for each primary row;
4. reconstructs both DPS endpoints, verifies both products are identity, and
   replays every signed Hurwitz generator exactly;
5. performs no route search, endpoint lookup, quotient-state enumeration, or
   group-element enumeration;
6. repeats all checks for the six fixed non-Z2 families.

The normalized digests are

```text
tree universe     4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary rows      f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2 classes        30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
primary words     3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608
secondary rows    f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full rows         114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
full words        d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c
```

Two consecutive executions produce the identical result-file SHA-256
`34e7a7a76b7993595b71a588d43afe85a443d851e722bb60b6e3d5f2bc3e1585`.

## Dependencies, first unproved step, and strict boundary

The proof uses only Prüfer completeness, the explicitly implemented DPS
boundary construction, and exact transposition/Hurwitz algebra. M214/M218,
M220/M223, M225/M228, and M231/M234 were checksum-verified and source-locked;
their finite results provide provenance, not an inductive premise.

The first unproved step is still an all-rank DPS closure lemma proving the two
implications

```text
lambda OR alpha  => N=A,
not(lambda OR alpha) => Q B_d Q^-1 N=A
```

for every rank, together with the later every-color and total-length steps.
Survival at two consecutive finite ranks does not prove that lemma.

This theorem proves no all-`d` route, every-color or arbitrary-representative
routing, polynomial or voltage-corrected total length, comparison congestion,
spectral gap, mixing bound, or Terminal conclusion.

