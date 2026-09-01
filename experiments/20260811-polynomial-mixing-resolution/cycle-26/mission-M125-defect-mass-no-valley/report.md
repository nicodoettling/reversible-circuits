# M125 final report: exact defect coefficients, no-valley still open

Date: 2026-08-13 UTC.

## Field 1 — decision and claim status

Verdict: **PROMOTE** the exact cycle-type/incidence-species coefficient
reduction and its multiset aggregation; **REFUTE** ultra-log-concavity;
**KEEP OPEN** ordinary log-concavity and DEFECT NO-VALLEY.

**PROVED:** M113/M118's defect mass `M[d,r]` is given exactly by the rooted
partition recurrences and cycle-type coefficient formula in
`defect_recurrence.md`, with no permutation, key, or word enumeration left.
Equal-size cycle atoms can be aggregated by exact binomial multiplicities.

**REFUTED:** the natural ultra-log-concavity strengthening fails exactly at
`d=4`.

**EXACT FINITE:** every row for `2<=d<=22` is unimodal and ordinarily
log-concave; ULC fails for every tested `d>=4`.  These are finite statements,
not a universal theorem.

**UNRESOLVED:** universal ordinary log-concavity, DEFECT NO-VALLEY, the defect-
projection gap, fixed-defect two-step gaps, `gap(A_d)`, the M113 handle
projection, and the original lazy `{3,4,5}` heat-bath gap.  Neither Terminal A
nor Terminal B follows.

## Field 2 — target, convention, and accepted input

The target is the auxiliary M113/M118 law

```text
rho(kappa)=|C_kappa|/Z_inc
```

on realizable connected-unicyclic incidence keys, not the uniform identity-
word law and not the lifted law `bar_pi`.  For `R(kappa)=d-c(p)`, define

```text
M[d,r]=sum_{R(kappa)=r}|C_kappa|,     0<=r<=d-2.
```

Permutations compose as `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right.  The sole imported enumerative input is M113's exact cell
formula, accepted with no material objection by M118:

```text
|C_kappa|=j!(2d-j)!
 product_{B in Q_L union Q_R}|B|^(c_B-3)
 product_{a cycle of p}[a^a/(a-1)!]^2.
```

M120's defect directional-rate theorems and M124's acceptance motivate the
no-valley target but are not used to derive the coefficient formula.

## Field 3 — exact partition and connected-component recurrences

Fix indexed permutation-cycle lengths `a=(a_1,...,a_c)`.  For nonempty
`S subseteq [c]`, put

```text
w(S)=(sum_{i in S}a_i)^(|S|-3),
P_S(y)=sum_{pi partition of S}y^|pi| product_{B in pi}w(B).
```

Choosing the block containing a fixed root gives exactly

```text
P_empty=1,
P_S(y)=y sum_{B subseteq S, root in B}w(B)P_{S-B}(y).       (3.1)
```

Let `A_S(y,z)=P_S(y)P_S(z)`, and let `C_S` retain only pairs of
partitions whose join is indiscrete.  Choosing the join-component containing
the root gives

```text
A_S=sum_{U subseteq S, root in U}C_U A_{S-U},
C_S=A_S-sum_{proper U subset S, root in U}C_U A_{S-U}.      (3.2)
```

The associated bipartite incidence multigraph has `c` labelled edges and
`L+R` block vertices.  The join condition is connectedness, and on the
diagonal `L+R=c` it is exactly connected-unicyclic.  This proves that the
coefficient selected below has precisely M113's realizability condition.

## Field 4 — exact cycle-type formula and multiset aggregation

Let `lambda=(a_1,...,a_c)` be an integer partition of `d`, with `m_s` parts
of size `s`, and put `h(a)=a^a/(a-1)!`.  Its exact contribution to
`M[d,d-c]` is

```text
d!/[product_s s^m_s m_s!]
* product_i h(a_i)^2
* sum_{L=1}^{c-1}
    (d+c-2L)!(d-c+2L)!
    [y^L z^(c-L)]C_[c](y,z).                            (4.1)
```

The two factorials follow from `j=d+(c-L)-L`.  The first factor is exactly
the number of permutations of type `lambda`; the atom factor is independent
of the coarsenings.  Summing (4.1) over types with `c=d-r` proves the claimed
row.

For cycle-size multiplicities `nu`, grouping every root-containing subset by
its submultiset `b` introduces the exact factor

```text
binom(nu_q-1,b_q-1) product_{i!=q}binom(nu_i,b_i),      (4.2)
```

where `q` is the distinguished root type.  Applying (4.2) to both (3.1) and
(3.2) proves the optimized multiset engine.  It replaces `2^c` indexed subset
states by `product_i(nu_i+1)` submultiset states without altering a
coefficient.

## Field 5 — boundary repair and independent audit

The interrupted core admitted the impossible one-cycle type and depended on a
wrapper monkeypatch to avoid writing defect slot `d-1`.  This is repaired in
the core: a realizable key has positive left and right block counts and
`L+R=c`, hence necessarily `c>=2`.

`audit_recurrence.py` provides three exact checks:

- direct enumeration of 3,278 pairs of set partitions over all 13 cycle types
  with `2<=d<=5`, independently checking the connected polynomial;
- equality of the indexed-subset and multiset recurrences, plus 204 colour-
  symmetry entries;
- equality with every frozen M124 raw defect weight through `d=5` and the
  independently supplied primitive rows at `d=6,7`.

There are zero failures.  It also checks `M[2,*]=[1]`, exclusion of every
one-cycle record, exact integrality, and the `d=4` margins below.

## Field 6 — exact ULC refutation and finite stress

At `d=4`, the primitive exact row is

```text
(627,1520,1113).
```

ULC after division by `(1,2,1)` requires
`1520^2>=4*627*1113`, but

```text
1520^2-4*627*1113=-481004<0.                           (6.1)
```

Thus ULC is **REFUTED**.  The same expression is the discriminant of the
quadratic defect polynomial, so the real-rooted route is also refuted here.
Ordinary log-concavity is strictly weaker and survives, with margin

```text
1520^2-627*1113=1612549>0.                             (6.2)
```

The exact engine reproduces the frozen rows `d<=5`, the coordinator stress
rows `d=6,7`, and computes every row through `d=22`.  Every tested row is
unimodal and ordinarily log-concave.  The closest tested ordinary inequality
is at `(d,r)=(22,7)`, where the exact ratio

```text
M[22,7]^2/(M[22,6]M[22,8])
```

is approximately `1.0118053687`; its exact numerator and denominator are in
`exact_results.json`.  Its proximity to one is a warning against claiming a
uniform strengthened margin.  None of these finite signs proves the universal
statement.

## Field 7 — strict remaining coefficient reduction

Let `H[d,c]` be the sum of (4.1) over integer partitions of `d` with exactly
`c` parts.  Then `M[d,r]=H[d,d-r]`.  The first explicit stronger lemma is

```text
H[d,c]^2 >= H[d,c-1]H[d,c+1]
for d>=4 and 3<=c<=d-1.                               (7.1)
```

This is **UNRESOLVED**.  It is a strict, falsifiable coefficient reduction:
all terms are defined by (3.1), (3.2), and (4.1), and no symmetric-group
state or incidence key remains to classify.  The obstacle is equally
explicit: connected extraction (3.2) is subtractive, and ULC/real-rootedness
cannot supply positivity.  A proof of (7.1) would imply DEFECT NO-VALLEY;
failure of (7.1) would not alone refute the weaker no-valley claim.

## Field 8 — reproduction, provenance, and dependencies

From the repository root:

```text
python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/audit_recurrence.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/audit_results.json

python3 -B \
  experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/run_exact.py \
  --d 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-26/mission-M125-defect-mass-no-valley/exact_results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, `seed=null`.  Required project sources and the complete frozen
M113/M118/M120/M124 payloads were read; all four frozen checksum sets pass.
The audit uses M124's frozen `results.json` only as an external exact reference.

## Field 9 — final verdict and next proof obligation

The exact recurrence and the ULC obstruction are ready for fresh referee
audit.  Universal no-valley is not proved or refuted.  The next proof
obligation is (7.1), or a weaker direct single-crossing theorem for the ratios
`H[d,c-1]/H[d,c]`; any such proof must handle the subtractive connected
extraction rather than extrapolate from `d<=22`.

Even if DEFECT NO-VALLEY is later proved, M120 yields only a polynomial gap
for the one-dimensional defect projection.  A fixed-defect two-step gap and a
comparison back to `A_d` remain mandatory before M113's projection comparison
can be used, and the original heat-bath chain remains farther upstream.
