# M197 final report: fresh immutable referee of M193

Date: 2026-08-13 UTC.

## 1. Verdict

```text
FINAL REFEREE VERDICT: ACCEPT FROZEN M193.
PROVED/AUDITED: fresh h=3<=27/125 for n>=1; separate n=0 charge <3/8.
MATERIAL OBJECTIONS: none.
```

## 2. Target, law, and scope

The target remains uniform fixed-length identity transposition words, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right. This audit covers only
the fresh actual-history `h=3` retained sector of normalized `F=H/q` in the
auxiliary nonlazy minimal-long-cycle parking projection. No reset, `h>=4`,
total AMV, all-`L`, gap, original-chain, mixing, or terminal inference follows.

## 3. Immutable integrity gate

All eight M193 payload hashes pass, its exact nine-file inventory matches its
manifest, and its ledger digest is
`aff1302508bfc61727e47649f0810183ff7fc7f28e7840bc3bbc239e828af0b2`.
All recorded checksums for eighteen cited dependencies pass. M193 and every
predecessor remained unchanged.

## 4. Normalization and exact average

The retained set `a=0,...,d-1` contains exactly `d` observations; killed
`a=d` is absent. Bayes gives
`(eta/pi_a)E[L_a^2||Phi||^2]=eta E_child[L_a||Phi||^2]`, so `pi_a=1/(d+1)`
is internal to `G` and `eta` is outside the branch sum. A clean-room symbolic
sum of the raw accepted history over `D=a+1=1,...,d` exactly reproduces
M193's closed `A_(B,d)=(1/d)sum_a Sbar_(B,d,a)`.

## 5. Universal certificate and `B=1`

For `B>=2`, the audit regenerates `y>=1/3`, `b<=3/8`, the positive `b`
derivative, strict `q` concavity and its exact vertex, the seven positive
`y`-derivative rows, and every shifted slack coefficient. For `B=1`, accepted
activity accounting justifies deleting inactive coordinates, and independent
substitution regenerates the positive nominal slack polynomial. Thus
`sum_a S_a<d` universally.

## 6. Exterior and boundaries

The exact sum, with `r=n` included, is

```text
sum_r(r+1)eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2)<=36/125.
```

Combining `sum_a B_(d,a)<3d/4` yields `27/125`; no `d`, `d+1`, or `pi_a`
factor is missing. At `n=0`, exact diagonalization gives
`rho_1=(25+sqrt(415))/70`, so the one-history charge is
`<9(25+sqrt(415))/1120<3/8`. The `B=1`, `n=0`, and `r=n` cases pass.

## 7. Numbered objections

1. **Material objections: none.** Every audited mathematical claim passes.
2. **External hygiene caveat only:** old immutable M117, M162, and M165 have
   unledgered bytecode-cache directories. Their ledgered payloads hash
   correctly and M193 is clean; this is not an M193 objection.
3. **Scope guard:** ACCEPT does not combine this sector with any other sector
   or imply total AMV, a gap, mixing, or a terminal.

## 8. Exact reproducibility

```text
command      | python3 -B independent_symbolic.py --output independent_results.json
arithmetic   | SymPy 1.12 exact symbolic arithmetic
random seed  | null
imports      | no M193 code/data imports
enumeration  | no L=7 or state graph
```

The checker independently derives the average from raw beta moments and
regenerates all decisive coefficient and boundary certificates.

## 9. Scope table and disposition

```text
candidate                  | frozen M193 fresh actual-history h=3 theorem
claimed target             | h3<=27/125 (n>=1), h3<3/8 (n=0)
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | clean-room beta/symbolic/exterior certificates
verdict                    | ACCEPT; eligible for coordinator ledger promotion
```
