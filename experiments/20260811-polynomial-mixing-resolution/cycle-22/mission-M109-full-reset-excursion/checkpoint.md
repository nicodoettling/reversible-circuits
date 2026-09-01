# M109 checkpoint

Status: exact recurrence derived; full contraction proved on suffix excess
`L<=2`; universal global lemma remains unresolved.

- Owned path created; frozen M106 startup hashes remain
  `66deb693...` for `report.md` and `57afd0e4...` for its manifest.
- Project skill/core and accepted M90/M96/M98/M99/M103/M106 sources are the
  controlling inputs.
- Local one-step/nonfresh and global two-layer defect positivity are already
  refuted and will not be retried.

- The `q`-transformed exact recurrences are `H=A_0+QH` and `G=A+QG`, with
  every `j=1,...,k` retained and `j=0` killed. Besides accepted strict
  `P=s+K-R` descent, suffix excess `L=s-B` drops by at least one on every
  live deep edge. Thus depth is at most `L`.
- Fresh attachment is exactly uniform: `nu_(1,0,k)(j)=1/(k+1)` for
  `j=0,...,k`. At `B=s`, `Q=0`.
- Selected global lemma: complete unweighted right-heavy contraction
  `H(x)<=q_x(1-q_x)`, which implies weighted contraction term by term. This
  is an all-depth assertion and imposes no local defect signs.
- Proved a universal canonical-basin estimate
  `rho(B_e)/rho(e)<=degree(e)` and used it to prove the complete suffix-terminal
  sector `B=s` analytically for every reachable context. The exact bound is
  `A_0<=q^2(s-1)/(s+1)<=q(1-q)`.
- Extended the proof to every right-heavy context with suffix excess
  `L=s-B=1`. Only the unary deep group survives and lands in the suffix-terminal
  theorem. An explicit convex quadratic in `z=1/(K+1)` is nonpositive at
  both endpoints `z=0,1/2`; `s=2` is checked symbolically.
- For `L=2`, isolated all four nonzero contextual root compositions and both
  live deep groups. Charging their three live children by the proved `L=0/1`
  bounds gives an exact rational envelope `E_s(z)`. It has no interior
  maximum; exact Bernstein certificates prove both endpoints for all `s`.
  Thus the first unresolved boundary is now `L=3`.

“Suffix-terminal” here means only `L=0` in the reset DAG and is unrelated to
project Terminal A/B. No universal full-excursion theorem is claimed.

## Exact independent formula audit

`boundary_exact.py` imports no predecessor and implements the full all-`j`
`Fraction` recurrence. It matches four frozen full-resolvent calibrations
exactly:

```text
weighted   (8,1,0,4): .43715035400213015...
weighted  (11,1,0,5): .5391499615007582...
unweighted (8,1,0,3): .6210042669407680...
unweighted(11,1,0,4): .6947437905621655...
```

It also directly checks 60 right-heavy boundary rows, every `2<=s<=16` and
`K in {1,2,5,64}`, with exact zero failures for both `L=0` and `L=1`. The
largest actual unweighted `L=1` ratio in this targeted audit is
`.4658659015742390...` at `(16,1,0,15)`. These bounded values validate the
formulas only; the universal result is supplied by the proof above.

For `L=2`, it directly checks 56 rows through `s=16`, verifies actual
resolvent `<=` analytic envelope `<=` target exactly, and reproduces the
envelope polynomial identity. It stores the seven finite `s=3,...,9`
degree-four Bernstein certificates and the three asymptotic scalar Bernstein
certificates used for `s>=10`.

The interrupted broader binary64 discovery run reached only the targeted
fresh rows `s=35,B=9` and `s=40,B=11`, with unweighted ratios
`.8395444045...` and `.8474765622...` and weighted ratios `.7502804485...`
and `.7649862014...`. They are discovery-only survival values, not evidence
promoted to a theorem.
