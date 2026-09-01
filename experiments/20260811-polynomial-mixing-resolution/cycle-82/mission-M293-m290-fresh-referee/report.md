# M293 fresh immutable referee report on M290

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT M290'S EXACT DEFECT-FIELD AND INVERSE-OWNER THEOREMS.
ACCEPT ITS COMPLETE 1/3--1/4 POSITIVE-COMPOSITION LAW.
ACCEPT ITS STRICT DOR <=> BODT REDUCTION.
MATERIAL OBJECTIONS: ZERO.
NONMATERIAL OBJECTIONS: ONE DOCUMENTATION-SCOPE CLARIFICATION.

BODT AND DOR REMAIN UNRESOLVED. NO DOWNSTREAM CLAIM FOLLOWS.
```

The M290 top digest is exactly
`85373b13ab4799f59d98dd20bf5b0496fa61d119b45b0ffe34900094564df687`.
Its ten payloads and all 117 payloads in the twelve cited predecessor
inventories pass. Actual directory inventories contain no unexpected files.

Independent algebra confirms the endpoint formula and exact defect-field
expansion. With three owners, each supported on at most two circular
intervals, `||U||_1<=12`, `TV(U)<=16 sum_i1/d_i`, and the standard
correlation-TV inequality prove

```text
sum_(ell=2)^(n-3)|Delta Q_ell(s)|
 <=C sum_(i:d_i>=2)1/d_i.
```

The `d=2` diagonal correction vanishes at all target lags because that owner
has at most one generic position; its first-order field is not discarded.

Every positive-composition triangle has exactly three anchor
representations. Every supported double has exactly four representations in
the combined `S/N` rows. Thus the factors `1/3` and `1/4` are correct, and
there is no extra `n`. The exact `T/S/N` owner intervals and all
kind/topology decorations survive the signed sum.

For states whose three owners all have size at least `(k+1)/2`, the
statewise bound is uniformly `O(1/k)`. Since `omega=P_B-P_A` has
`sum|omega|<=2`, their entire combined contribution is `O(1/k)`. The
complement is precisely the BODT boundary, so adding or subtracting the
proved interior vector gives the exact equivalence

```text
DOR = O(1/k)  iff  BODT = O(1/k).
```

This equivalence does not prove either bound on the boundary.

The sole clean-room exact guard ran at `k=9`. It exhaustively verified
261,924 endpoint identities, 273,312 defect identities, owner intervals, the
size-two exception, three/four multiplicities, 5,525 owner rows, source
normalization, reflection, and the declared finite sign row. Its exact
symbolic DOR equals DTR and matches M290's value
`0.2784019538957808...`. This is finite-only.

The one nonmaterial clarification concerns M290's audit-request wording:
BODT is a decorated-only `Delta Q` obligation, exactly as its proof and
report define it. Collision/decorated recombination belongs to the OCI
identity; the separate PBV route still needs CIBV together with DOR.

```text
M290 and twelve cited immutable boundaries              verified
null-owner endpoint formula                              proved exact
defect-field identity and d=2 target-lag exception       proved exact
statewise inverse-owner lag variation                    proved
1/3 triangle, 1/4 combined-double law; no extra n        proved exact
all-owner >=(k+1)/2 sector                               O(1/k), proved
DOR <=> BODT                                              proved reduction
k=9 DSR signs and DOR=DTR                                 exact finite only
BODT, DOR, DSR, DTR                                       unresolved
CIBV, SET, PBV, FD, FCL1, gap, mixing, Terminals          no inference
```

Final action: **accept and freeze M290 at exactly this scope.**
