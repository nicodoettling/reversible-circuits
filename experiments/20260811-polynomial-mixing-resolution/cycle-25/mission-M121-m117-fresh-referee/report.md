# M121 final report: fresh referee audit of M117

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The project target remains uniform on fixed-length identity words in
`Omega(N,m)`. Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are
displayed left-to-right.

The accepted claim is only the complete right-heavy reset-excursion
contraction at auxiliary suffix excess `L=4`:

```text
H(s,K,K-1,s-4) <= q(1-q),  s>=5, K>=1.
```

Together with the accepted positive-history comparison this gives `G<=H<=U`
for that right-heavy auxiliary seed. It proves no auxiliary gap, ROOT-MEAN
LIFT, original lazy `{3,4,5}` heat-bath gap, polynomial mixing, Terminal A,
or Terminal B. The first unresolved suffix excess is `L=5`.

```text
candidate                  | full auxiliary reset excursion at L=4
claimed target             | right-heavy unweighted/weighted contraction
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | independent definitions, DAG, certificates
verdict                    | ACCEPT L=4; all-L and every gap remain open
```

## 2. Frozen provenance gate

All supplied immutable M117 hashes matched before audit:

```text
report    65213fb22e677c0a8fb1c23f41b769390cf42a684d0484d9b352d4e4bb8b8044
proof     e9a1d5ca3080b1cb16308f201b83329131a13f8db50b98e863761dc3ed2c5398
script    13f37f60de522485919fe6a272b416805dd05374397ea10285bd30aa0c65763d
JSON      e4acb81c4add5108101e1703c9b70a845fbf8c9ac2caa15f2cb9f332fc20af94
manifest  93b420a9a30829a00ebac02446668a77ea1e8c97c5de86d3488517db546c801a
```

No M117 or predecessor artifact was edited.

## 3. Support and basin reconstruction

The fresh checker imports no M117 or predecessor code or output. Direct
ordered-composition enumeration gives exactly 16 supported root rows. Their
individual masses and contextual means equal every displayed formula in
M117, their weighted mean is `q`, and they occupy exactly 11 positive `(k,t)`
groups.

Literal first-prefix basin generation gives exactly 15 exceptional basins.
Every supported-source nesting, normalized current, and normalized capacity
equals the closed formula in M117. Four exceptional endpoints begin `(1,1)`
and are inactive; 11 are active. The supported exceptional path mass is
exactly

```text
q[369/625+37/(125x)+4/(25xy)+12/(125xyv)].
```

A second reset implementation aggregates first-prefix refinements by the
forest-weight identity. It agrees with literal enumeration at all 213 states
in the tested recursive closure. Thus M117's reset envelope has no missing
composition, basin, current, capacity, or inactivity qualification.

## 4. Arbitrary-deficit `L=2` proposition

The fresh derivation independently finds the four supported rows, all three
exceptional basins, and both descendant groups. Their currents and capacities
give exactly the three squares in `R_2`. Rank-by-rank descendant accounting
gives exactly

```text
(1-d_0)(1-Y)/3 +(2/3)(1-p)F_1(a,Y,H_1;p').
```

The audit covers all 252 contexts
`3<=S<=9`, `2<=K_0<=9`, `1<=R_0<K_0`. Literal and grouped resets agree, and
both the reset and resolvent bounds pass. At `S=3`, the two nominal terminal
children have auxiliary rank one and are absent, while `Y=1` makes their
displayed envelope charge exactly zero. The proposition is correctly scoped
as a bound on `H/q_0`, not arbitrary-deficit contraction.

## 5. Every live group and exact DAG checks

Exactly seven root groups send retained deep mass. The fresh implementation
retains every `j=1,...,k`, verifies the closed right-heavy attachment law
against the defining binomial law, checks
`deficit=k+1-j` and child suffix excess `h-1`, and only then aggregates.
The rank sum equals M117 equation (5.1) exactly.

For all 15 roots `5<=s<=9`, `K in {1,2,5}`, the literal and grouped full
resolvents agree and satisfy

```text
exact reset <= reset envelope,
exact H <= q E_4 <= q(1-q).
```

The literal active-basin counts at `s=5,...,9` are
`11,23,47,95,191`. These finite rows audit implementation; they are not the
universal proof.

## 6. Independent universal certificate

After clearing by

```text
Delta(z)^2 = prod_(a=1)^4(1+az)^2,
```

the slack is polynomial of multidegree at most `(2,2,2,2,2,10)`. Exact
generic slices show every bound is sharp. The referee derives Bernstein
coefficients using in-interval endpoint grids, a rational Vandermonde inverse,
power-to-Bernstein conversion, and tensor axis transforms. This differs from
M117's integer-node Lagrange implementation.

For `s=5,...,21`, all 187 degree-ten coefficients are positive. The exact
minimum is

```text
71734022477173585947/9023189417984000000000
```

at `s=7`, coefficient zero. All interpolants pass exact off-grid identities.

For `s>=22`, monotonicity of
`b_n=(n/(n+1))^(n-1)`, the bound `b_n>1/3`, and the exact inequality
`b_18<2/5` place all five ratios in `[1/3,2/5]`. Each of the three path
heights enters the envelope affinely with a positive coefficient, so replacing
them by one is pessimistic. On the resulting box
`[1/3,2/5]^5 x [0,1/2]`, all 2673 tensor coefficients are positive, with
exact minimum

```text
742081/227812500 at (2,2,2,2,0,0).
```

The tensor passes an independent exact off-grid identity. This is a universal
algebraic sign certificate, not finite-rank extrapolation.

## 7. Post-hoc frozen-output comparison

The fresh mathematical output was completed without reading M117 output. A
subsequent read-only comparison found exact numerator/denominator equality
for:

- all 187 finite Bernstein coefficients;
- all 2673 tail tensor coefficients;
- every reset, full-resolvent, and envelope ratio in the 15 common DAG rows;
- every reset and resolvent ratio in all 252 arbitrary-deficit rows.

No discrepancy was found.

## 8. Reproducibility and owned hashes

The durable command, from this directory, is

```text
python3 -B independent_m117_referee.py --output independent_m117_referee.json
```

It uses Python 3.12.3, standard-library exact `Fraction` arithmetic, no
nonstandard dependency, and `seed=null`. A fresh `/tmp` rerun of the final
source was byte-identical to the durable JSON and had zero failures.
Pre-report owned hashes are

```text
plan        3c167b4854088f117480ef7c07d3bbbcf3f1da1f90e5bf5e6e5400668a50f4ea
checkpoint  c58e2590c7376d368a4ce0abca30743af8b83637c578c603baf031f6396d7b40
proof       b25f2234e762706866e45d623d817283bd83cba747d4dc2211d5ae1c863cd0ef
script      f6bdb901a0f65be8b0bc059f600dfe5b57d072c495486cf60e96b1ce5c91ab3d
JSON        ddae82ca0c62a44bd5606deca778c1942d2a058c99479f2b367acf8f2f8730aa
```

The final `SHA256SUMS` records the report and all owned artifacts. Cache
hygiene is clean.

## 9. Dependencies, limitations, and final disposition

Accepted dependencies remain M109/M114's recurrence, finite descent,
canonical-basin estimate, positive-history comparison, all-deficit `L=0`,
and right-heavy `L<=2`; and M115/M116's arbitrary-deficit `L=1` envelope and
right-heavy `L=3` theorem.

M117's new `L=4` step, including its arbitrary-deficit `L=2` child envelope,
survives a fresh proof and exact-computation audit. It does not organize
general `L`; exceptional-basin growth remains the structural limitation.

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
FIRST OPEN BOUNDARY: auxiliary right-heavy suffix excess L=5.
```
