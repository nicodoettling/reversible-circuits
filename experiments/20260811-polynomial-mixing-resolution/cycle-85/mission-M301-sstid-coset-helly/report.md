# M301 final report: SSTID coset-Helly frontier

Date: 2026-08-14 UTC.

## Verdict

```text
KEEP: exact action-cover/residual-density equivalence.
REFUTED (exact finite, d=3): hereditary 2-Helly for actual subfamilies
                              contained in an M135 perfect matching.
UNRESOLVED: registered MT2H for whole pairwise-compatible matchings,
            MRAD for d>=6, polynomial literal representative length,
            and SSTID.
```

This is a strict obstruction to the first unqualified finite-action/coset-
Helly shortcut.  It is not an asymptotic counterexample to SSTID.

## Immutable gates and declared target

M296's frozen top digest reproduces as

```text
9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f,
```

and M299's as

```text
1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d.
```

Every row in both manifests passes.  The single diagnostic additionally
gates M135 at top digest
`8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358`
and its imported script at
`79ed378ae7fd7543c16bf12a1fa51e0144b817a938c91de196be960a2e6ad540`.

The auxiliary target is the uniform minimal connected identity sector
`Z_d`, with chronological signed right-Hurwitz action and
`(pq)(x)=p(q(x))`.  The ambient project target remains the uniform global
fixed-length identity bridge under the exact lazy `{3,4,5}` heat-bath kernel.
No kernel estimate is made here.

## Strongest proved analytic statement

For an actual M135 perfect matching `M`, let

```text
K_Q={a in A_d:a(w_Q)=tau_i(w_Q)},
E_a(M)={Q in M:a in K_Q},
kappa(M)=minimum number of E_a(M)'s covering M.
```

The number `kappa(M)` is exactly the minimum number of subfamilies partitioning
`M` such that each subfamily has a nonempty higher-arity fiber intersection.
Moreover, writing

```text
rho(U)=max_a |E_a(M) intersect U|/|U|,
```

one has the exact implications

```text
kappa(M)<=q  =>  rho(U)>=1/q for every nonempty U subset M,

rho(U)>=1/q for every nonempty U
  => kappa(M)<=ceil(q(1+ln|M|)).
```

Since an actual perfect matching has

```text
|M|=d^(d-3)(2d-2)!/d!,       ln|M|=O(d log d),
```

inverse-polynomial residual agreement density is polynomially equivalent to
the finite common-nonemptiness cover.  This replaces a false graph/Helly
shortcut by a precise higher-arity finite-action target.

Under transitivity of the finite Hurwitz action on `Z_d`, exact double
counting also gives

```text
average_(a in A_d) |E_a(M)|=1/d!.
```

Thus a polynomial cover requires rare, highly correlated agreement actions;
a generic action and pairwise moments do not supply them.

## Exact actual-edge obstruction

The pre-registered candidate MT2H concerned complete perfect matchings.  At
`d=3`, the diagnostic reconstructs

```text
|Z_3|=24, |A_3|=216, 4 global orbits, 12 H-orbits,
12 perfect matchings for each i=1,2,3, |K_Q|=9.
```

No complete perfect matching is pairwise compatible, so MT2H's premise is
false throughout this guard and MT2H is not refuted.

However, for `i=1`, actual matching `[0,1,2,9]` contains the actual-edge
subfamily `[0,2,9]` with

```text
K_0 intersect K_2={45},
K_0 intersect K_9={49},
K_2 intersect K_9={89},
K_0 intersect K_2 intersect K_9=empty.
```

The edge endpoints are `(0,1),(2,3),(3,2)`, hence the three edges form a
partial matching.  The source/target word certificate is recorded in
`coset_helly_obstruction.md` and `results.json`.  Therefore pairwise graph
independence does not imply one common action even inside an actual matching.

This is **exact finite**, not empirical.  It rules out only the hereditary,
unqualified 2-Helly shortcut.  It gives no `d>=6` counterexample and no lower
bound on a polynomial higher-arity refinement.

## First unresolved lemma

**MRAD** asks for a universal `C` such that, for every `d>=6`, every adjacent
index, every actual perfect matching `M`, and every nonempty `U subset M`,
some finite action agrees with at least `|U|/d^C` selected edges.  MRAD is
unresolved and is polynomially equivalent to the finite nonemptiness half of
SSTID.

Even MRAD is insufficient for SSTID: the chosen actions must have literal
signed braid representatives of length `d^O(1)`.  Finite action nonemptiness
and literal representative length remain separate exactly as required by
M296/M299.

## Reproduction and artifacts

Deterministic command, Python 3.12.3, dependencies `{}`, seed `null`:

```text
python3 -B mt2h_d3_diagnostic.py --output results.json
python3 -m compileall -q mt2h_d3_diagnostic.py
```

The second command is only a syntax check; its generated cache is not part of
the package.  The first command SHA-gates the frozen M135 dependency before
running.  Artifacts are:

- `plan.md`: pre-computation theorem candidate and decision rule;
- `checkpoint.md`: halfway checkpoint;
- `mt2h_d3_diagnostic.py`: the only finite diagnostic;
- `results.json`: machine-readable exact output;
- `coset_helly_obstruction.md`: proofs, witness, and MRAD;
- `audit_request.md`: fresh-referee obligations;
- `freeze_manifest.md`: frozen claim boundary.

No predecessor, coordinator, manuscript, source-of-truth, or skill file was
edited.  No every-color schedule, rank lift, voltage, congestion, gap, mixing,
Terminal A, or Terminal B inference is made.
