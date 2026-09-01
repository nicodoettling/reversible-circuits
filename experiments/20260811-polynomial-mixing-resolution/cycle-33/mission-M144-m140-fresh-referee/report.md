# M144 fresh-referee report on frozen M140

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The immutable M140 payload proves the scalar bound
`C_s<74969/100000<3/4` for every `s>=100`, and, relative only to
the accepted recurrence and lower-excess inputs named below, proves the
corrected auxiliary right-heavy suffix-excess-five inequality for every
`s>=6,K>=1`. The rejected M131 two-power display is not used.

## Field 2 — target, convention, and scope

The project target remains uniform on fixed-length identity transposition
words. Permutations compose as `(pq)(x)=p(q(x))`, with factors displayed
left-to-right. The accepted claim is only

```text
H(s,K,K-1,s-5)<q(1-q),
q=w_6 w_(s-5)/w_(s+1).
```

It is not an auxiliary gap, ROOT-MEAN LIFT, original-chain gap, polynomial
mixing theorem, Terminal A, or Terminal B.

## Field 3 — immutable provenance and dependencies

All supplied M140 hashes matched before inspection: report
`4b724f49...0946f3`, proof `d8e49d7e...94bb6`, scalar checker/results
`11ca05a8...3e12` / `d2066038...650`, certificate checker/results
`b9330081...4bac` / `16a816cd...937`, manifest
`22ee3150...32b`, and inventory `fa0e3278...68e`.

The recorded M109/M114, M115/M116, M117/M121, and M138 dependency hashes
were independently recomputed and all matched M140's manifest. M131 remains
negative provenance only.

## Field 4 — tree EGF and exact first moment

Fresh derivation confirms that `T=z exp(T)` gives
`[z^n]T^p=p n^(n-p-1)/(n-p)!`, and that
`w_A p(A)_p/A^p=c(A,p)`. Substitution gives

```text
sum_A m_s(A,k)lambda(A,k)
 =P[Bin(s-1,1/(s+1))>=k-1].
```

The clean-room checker confirms all 435 rows for `2<=s<=30`. There is no
index or endpoint shift.

## Field 5 — Poisson, integral, and scalar correction

The coupling direction is correct: each Bernoulli is the positivity
indicator of `Pois(-log(1-p))`, hence the binomial is dominated by a
Poisson sum of parameter
`(s-1)log(1+1/s)<1`, and then by `Pois(1)`.

The beta integral and tail generating function independently reduce the
majorant to

```text
U=sum_(n>=1)2/[n(n+2)n!]
 <41554847/50803200<409/500.
```

The endpoint ratio, uniform logarithmic error
`23612897/2962759680<1/100`, rational bound
`e<31967/11760<87/32`, nine selected lambdas, and
`D_0=78988317872/1121447071575>69/1000` all check exactly. Retaining the
`99/100` mass factor gives
`409/500-(99/100)(69/1000)=74969/100000<3/4`.

## Field 6 — corrected reset and smallest boundary

For every literal occurrence checked at `s=6,7`,
`a_E<=b_E=c_E lambda_E`. The ordinary contribution is
`q b_E lambda_E`, so the safe subtraction is exactly
`q a_E lambda_E`, leaving `q(b_E-a_E)lambda_E>=0`.
Only one power of `lambda_E` occurs; `a_E lambda_E^2` is explicitly
rejected and unused.

At `s=6`, the boundary has 17 structurally retained child triples after
the rank-one `t=2` boundary is removed. One retained lower envelope charge
can vanish; the decisive slack remains strict. Its minimum Bernstein
coefficient is
`13461835439971/11861248695609600>0`.

## Field 7 — independent exact certificates

The M144 checker imports no predecessor code or data. It reconstructs the
recurrence from definitions, interpolates at rational nodes into the
monomial basis, and converts monomials directly to Bernstein coefficients.
This differs structurally from M140's Bernstein-evaluation-matrix inversion.

- All 1,222 finite coefficients for `s=6,...,99` are positive. The minimum
  is `5307578203959502651/4736091661711441920000` at `(s,i)=(7,0)`;
  digest `733243ff...84f7`.
- All 4,212 tail coefficients of multidegree
  `(1,1,2,2,2,2,12)` are positive. The minimum is
  `4360847276079323/50118750000000000000` at
  `(1,1,2,2,2,0,0)`; digest `2c1aa847...22f`.
- Independent finite and tensor off-grid interpolation identities pass.

Both canonical digests and both exact minima equal M140.

## Field 8 — reproducibility

Run from this directory:

```text
python3 -B fresh_referee.py --output fresh_referee.json
```

Python 3.12.3, standard library only, exact `fractions.Fraction`
arithmetic, deterministic `seed=null`. The result reports zero failures.

## Field 9 — disposition, limitations, and hygiene

Accept M140's scalar Lemma C and corrected auxiliary `L=5` theorem within
their explicit dependency boundary. Do not infer a weighted auxiliary
contraction, spectral gap, ROOT-MEAN LIFT, original-chain gap, polynomial
mixing, or project terminal.

No package was installed and no predecessor, coordinator, manuscript,
project-skill, or other worker file was edited. No Python cache remains.
