# M193 final report: coupled fresh actual-history `h=3` aggregate

Date: 2026-08-13 UTC.

## 1. Verdict

```text
FINAL VERDICT: PROMOTE STANDALONE FRESH h=3 SECTOR BOUND WITH FRESH REFEREE.
PROVED: h3<=27/125 for n=L-3>=1; separate n=0 bound h3<3/8.
OPEN: reset and h>=4 sectors; no total-AMV conclusion.
```

## 2. Target, law, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, displayed left-to-right. This
mission concerns only the normalized full unweighted reset excursion `F=H/q`
in the auxiliary nonlazy minimal-long-cycle parking projection, and only
fresh actual-history retained descendants of last-root height `h=3`.

## 3. Precise proved statement

For every `B,d>=1`, the accepted suffix-two actual-history envelopes obey

```text
sum_(a=0)^(d-1) S_a <= sum_a Sbar_(B,d,a) < d.
```

Combining this observation-averaged lemma with M185/M190's full three-mode
Loewner theorem `B_(d,a)<=(3/4)S_a` gives
`sum_a B_(d,a)<3d/4`. Therefore the exact fresh `h=3` sector is at most
`27/125` for `n>=1`. At `n=0`, the exact degree-one matrix yields the separate
bound `<3/8`.

## 4. Normalization and numbered self-objections

1. **Observation count:** retained values are exactly `a=0,...,d-1`, so
   there are `d`, not `d+1`, branches. The killed `a=d` remains absent.
2. **Bayes factor:** `pi_a=1/(d+1)` is already in `G_(d,a)` through
   `(eta/pi_a)E[L_a^2||Phi||^2]=eta E_child[L_a||Phi||^2`. No additional
   `pi`, survival conditioning, or `1/(d+1)` multiplies the branch sum.
3. **Average versus sum:** `1/d` appears only to prove the trace-average
   lemma. Multiplying it back produces the factor `d=r+1` in the exterior
   moment; no count is omitted.
4. **Pointwise obstruction retained:** the exact envelope at
   `(B,d,a)=(3,20,19)` is `10249528643/7684875000>1`; its degree average is
   `443845801/614790000<1`. The theorem does not reuse the refuted pointwise
   `Sbar<=1` route.
5. **Cross terms:** the accepted `3x3` matrix comparison retains all
   likelihood-weighted cross terms and covariance subtraction. No scalar,
   diagonal, finite-summary, Jensen, or generic-operator shortcut is used.

## 5. Analytic certificate

Exact beta-moment averaging gives the closed trace formula in
`coupled_trace_theorem.md`. For `B>=2`, `H0,H1<=1`, `y>=1/3`, and `b<=3/8`.
The relaxed average increases in `b`; its unconstrained quadratic maximum in
`q` is

```text
q*=y(d^2+11d+22)/[(d+2)(d+3)(4y+3)],
```

and that maximum decreases in `y`. At `b=3/8,y=1/3`, the slack numerator is
coefficient-positive after `d=1+e`, with coefficients

```text
4829,131535,1351327,6721029,16784028,18788964,5726736.
```

For `B=1`, inactive coordinates are deleted; the larger nominal envelope has
slack numerator
`51529d^4+779710d^3+4228095d^2+9411050d+7219256>0`.

## 6. Exterior and boundaries

For `n>=1`, `r=1,...,n`, `d=r+1`, including `r=n`,

```text
sum_r d eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2) <=36/125.
```

Multiplication by `3/4` gives `27/125`. At `n=0`, only `d=1,a=0` occurs,
`eta=9/16`, and the exact matrix norm is
`rho_1=(25+sqrt(415))/70<2/3`; the one-observation history envelope is
strictly below one. Thus the charge is
`<9(25+sqrt(415))/1120<3/8`. The reported `3/8` is deliberately loose.
`B=1` inactivity, `n=0`, and `r=n` are all explicit.

## 7. Dependencies and status labels

- **Proved here:** universal observation-averaged suffix-two trace lemma,
  exterior maximum `36/125`, fresh `h=3` bounds `27/125` and `<3/8`.
- **Accepted immutable inputs:** M109/M114, M115/M116, M117/M121,
  M147/M151, M157/M160, M162/M165, M173/M177, M179/M184, M185/M190.
- **Unresolved/out of scope:** reset, `h>=4`, total AMV, all `L`, ROOT-MEAN,
  any gap, original-chain mixing, Terminal A, and Terminal B.

## 8. Exact diagnostics and reproducibility

```text
command      | python3 -B exact_check.py --output exact_results.json
arithmetic   | Python 3.12.3 standard-library Fraction
parameters   | B in {1,2,3,8,16}; 1<=d<=30; 1<=n<=30
random seed  | null
imports      | no predecessor imports; standard library only
```

The checker matches direct beta integration to the closed average, retains
the individual `>1` obstruction, regenerates both integer certificates, and
checks the exterior identity including `r=n`. Finite checks are diagnostic;
the analytic certificate proves the universal claim.

## 9. Handoff and fresh-audit request

```text
candidate                  | fresh actual-history h=3 retained sector
claimed target             | h3<=27/125 (n>=1), h3<3/8 (n=0)
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | rational beta averages/exterior/certificates
verdict                    | promote standalone sector theorem, fresh audit
```

Request an immutable fresh referee to rederive the branch/exterior
multiplicities, verify that `pi_a` is internal and exactly `d` branches
remain, audit the closed averaged-trace formula and all sign certificates,
and check `B=1`, `n=0`, and `r=n`. The referee must not infer reset, `h>=4`,
total AMV, a gap, or either terminal.
