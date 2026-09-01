# M190 final report: fresh referee of frozen M185

Date: 2026-08-13 UTC.

## 1. Verdict

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

Frozen M185 correctly proves a strict fresh-`h=3` reduction: the exact
three-mode branch, an exact refutation of the `2/3` factor, and a universal
`3/4` Loewner comparison to full child trace.  It correctly leaves the
coupled observation-dependent trace aggregate unresolved.

## 2. Target and convention

The project target remains uniform fixed-length identity transposition
words, with `(pq)(x)=p(q(x))` and displayed factors left-to-right.  The
audited object is only `F=H/q` in the auxiliary nonlazy minimal-long-cycle
parking projection and only fresh retained descendants with last-root height
`h=3`.

## 3. Immutable integrity and provenance

Before conclusions, every M185 payload passed its complete frozen ledger;
the inventory matched its manifest.  M185's `SHA256SUMS` digest is

```text
9400d67948c99905bc1ce75081466d737247ed47af3fb42d7b7b5c2ae36b64b1.
```

All relevant accepted dependency ledgers M109/M114, M115/M116,
M117/M121, M147/M151, M157/M160, M162/M165, M173/M177, and M179/M184
also passed.  No predecessor was edited.

## 4. Exact branch audit

Suffix excess two makes the child feature exactly three-mode.  Independent
Bayes calculation confirms

```text
G_ij=E_child[L_a e_i e_j]-12pi_a z_i z_j,
z=(p-1/2,sqrt(v),0),       pi_a=1/(d+1).
```

The trace retains one likelihood after posterior conversion, all three
off-diagonal terms remain, and the parent covariance subtraction retains its
constant/linear cross term.  Killed `a=d` is absent with no survival
conditioning.

## 5. Loewner obstruction and theorem

Independent standard-library rational arithmetic gives

```text
det((2/3)I-G_(20,0))=-1731224299/244943654967<0,
```

so M185's `2/3` refutation is exact.  A clean symbolic derivation from beta
moments independently regenerates M185's universal `3/4` certificate:

- positive Jacobi norms for every `|2a-d|<=d`;
- positive first Sylvester minor;
- a concave second-minor quadratic with both endpoints positive;
- the exact positive determinant prefactor; and
- four Bernstein coefficient polynomials of degrees `14,14,13,12`, all
  strictly coefficient-positive after `d=1+e`.

The `d=1,a=0` boundary passes separately.  Therefore
`G_(d,a)<=(3/4)I_3` for every retained branch.

## 6. Actual-history trace audit

Independent support and normalization accounting reproduces

```text
S_a<=Sbar=R_2+D_0+(2/3)W_1,
```

where `R_2` contains the three exceptional reset-current squares, `D_0`
contains both retained height-one likelihood ratios with exterior `1/3`,
and `W_1` is the unary likelihood-weighted suffix-one trace with exterior
`2/3`.  This is a full actual-history trace envelope, not scalar `F`, child
`T_1`, Jensen, or a generic operator bound.

At `(B,d,a)=(3,20,19)`, exact integration gives

```text
Sbar=10249528643/7684875000>1.
```

This refutes only the envelope-cap-one route, not an unknown sharper bound on
the exact child trace.  M185 makes that distinction correctly.

## 7. Exterior and boundaries

The exterior independently simplifies to

```text
eta^(3)_(n,r)=(3/2)c(n,r)/[(r+1)!w_(n+4)].
```

The separate `n=0` row has `r=0,d=1,eta=9/16`.  For `n>=1`, the exact sum
includes `r=n` and equals

```text
(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).
```

The `B=1` exact history removes inactive rank-one coordinates; retaining
their nonnegative nominal terms leaves M185's displayed formula a valid
upper envelope.  All requested boundaries pass.

## 8. Numbered objections, dependencies, and scope

1. **Material objections: none.**
2. **Nonmaterial reproducibility note:** M185's own compact checker does not
   regenerate its universal Bernstein lists.  M190's clean symbolic checker
   independently regenerates them exactly, so no theorem correction is
   needed.
3. **Scope guard:** `Sbar>1` is not an exact-child counterexample.
4. **Scope guard:** nothing audited proves `S<=2`, a complete `h=3` sector
   bound, total AMV, a gap, original-chain mixing, or either terminal.

The first open lemma remains the coupled observation/degree actual-history
trace aggregation, with `n=0` separate.

## 9. Reproducibility and handoff

```text
candidate                  | frozen M185 fresh h=3 reduction
claimed target             | exact branch/matrix strict reduction only
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | Fraction rows plus exact symbolic certificate
verdict                    | ACCEPT; no material objections
```

Run:

```text
python3 -B independent_exact.py --output independent_results.json
python3 -B symbolic_certificate.py --output symbolic_results.json
```

Python is 3.12.3; the first script is standard-library only.  The symbolic
checker uses installed SymPy 1.12.  Both import no M185 code/data, use
`seed=null`, and perform no `L=7` or state-graph enumeration.
