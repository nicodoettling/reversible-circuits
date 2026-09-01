# M300 halfway checkpoint

Date: 2026-08-14 UTC.

## Exact finite status

The sole predeclared rank `k=7`, `n=21` has completed under exact
`Fraction` arithmetic. All 54 `(u,ell)` middle cut-length phase-orbit
coefficients are strictly positive:

```text
u=1 minimum: ell=10 (and 11), approximately 0.13368963165833617
u=2 minimum: ell=6  (and 15), approximately 0.10149412086894180
u=3 minimum: ell=7  (and 14), approximately 0.11078794736347130
```

The exact global minimum is the `u=2, ell=6,15` value

```text
18391884160007872512505581390057340062886183764340384475832641580678550316483694546164031922299480179423171
/181211325370827177616731812976270118138716435331141156018616780003928170444373248989640785920000000000000000.
```

This positivity is not inherited from fixed-middle cells. Exactly 44 of 378
such cells are negative. The minimum occurs at cut class `u=2`, phase `6`,
middle edge `(8,13)`, and reflected lags `ell=8,13`:

```text
-47887190399462218030782332438763438434346238035631961416543569973932853169
/920408972596550617862664784704103676980180079269295528017920000000000000000.
```

Every fully middle-weighted `eta_1(F_ell)` is also positive. This is exact
finite evidence only: `(MCLP_1)` and `(GOCI_1)` remain unresolved.

## Guards passed

- all four cycle chord laws have exact mass one;
- `sum_e gamma_k(e)=0`;
- the cut-length phase classes partition every middle chord exactly once and
  `sum_u k w_(k,u)=1`;
- literal residual-cycle and repaired owner-autocorrelation responses agree
  for every admissible state/lag;
- statewise, classwise, and full-lag reflection are exact;
- the direct full middle average equals the cut-class reconstruction.

## Analytic progress after the run

The exterior signed law has a complete Hahn support classification. Let
`D=2k-1`, `A={1,...,k-1}`, and `P={2k,...,3k-1}`. Then:

- every cross chord in `A x P` has `gamma=nu_D>0`;
- every seam chord `{0,i}`, `i in A`, has `gamma=-nu_k/2<0`;
- every chord internal to `A` or `P`, of cycle separation `c`, has
  `gamma=nu_D(c)-nu_k(c)/2<0`.

The last strict sign follows from the decreasing ratios
`tau(d-1)/tau(d)`:

```text
2nu_D(c)/nu_k(c)
 =[tau(D-c)/tau(D)]/[tau(k-c)/tau(k)] < 1.
```

There are exactly `k(k-1)` positive cross chords and `k(k-1)` negative
internal/seam chords, and their total masses agree because `sum gamma=0`.
The next step is to write the complete middle-phase response against these
two normalized exterior laws and expose the residual exterior cut-size Abel
coefficients. No pointwise response order is being assumed.
