# M95 plan: fresh referee of M92

Date: 2026-08-12.

## Objective and target

Independently referee the frozen M92 reduction for the uniform law on
`Omega(N,m)` and the literal lazy exact same-product `{3,4,5}` heat-bath
kernel.  The audited intermediate walk is

```text
P_Gamma=(1/2)I+[1/(4(m-1))] sum_i (R_i+R_i^(-1))
```

on one two-component minimal exterior macro at `N>=5,m=2N-2`, with
`(pq)(x)=p(q(x))` and tuple factors multiplied left-to-right.

## Frozen inputs

```text
21662f10c53582e6fbf2fe18cc405ba7d92497948a76e7138d5a46f5a266678f  M92 report.md
6490d4cd0daae58bf0ff68cbdceedb2d432cb27d743e18f02bea05bc4dd2ffd0  M92 oblivious_cover_reduction.md
e2e6ab274adc9d9cf20a0047196770c14b58681846738af0c919db6196547edc  M92 freeze_manifest.md
```

## Audit obligations

1. Re-derive random-time hitting-to-endpoint and M75 endpoint coarea load.
2. Check the strong lump, equal projection fibers, product law, and mark
   measurability pointwise, without an omitted-word assumption.
3. Re-run M05's shuttle comparison on the projected coordinate and verify all
   gap exponents and constants.
4. Check the fixed-time total-variation calculation, marked density,
   `t_Gamma`, and final coarea normalization.
5. Trace dependencies to ensure the positive reductions do not use the
   conditional Classification-H source.
6. Check the tree--cotree homology proof and independently validate the exact
   metadata collision.
7. Check the all-`d` unmarked family and scope of transcript/root-load claims.

## Exact checks and expected failure modes

Write a standard-library-only independent checker for the two frozen
witnesses, Cayley-tree family through small `d`, pointwise projected Hurwitz
action, mark invariance under the omitted component, and M05 shuttle words.
Expected failures include a missing factor two in endpoint coarea, dependence
of the projected row on the omitted word, a non-bijective projected proposal,
an incorrect tree/cotree witness, or an overbroad root-occupation conclusion.
Finite checks can refute formulas but cannot prove an asymptotic gap.

## Deliverable

A nine-field `report.md` with `ACCEPT` or `REJECT`, numbered material
objections, exact scope, reproducible raw JSON, frozen hashes, and explicit
statement that `gamma_1`, uniform marked hitting, arbitrary-macro/full-`K`
mixing, and Terminal A/B remain open.
