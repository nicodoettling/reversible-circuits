# M151 final report: fresh referee audit of frozen M147

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and numbered objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTION NM-1: frozen report Field 4 has one extra `/q`
on the normalized reset symbol; the frozen proof artifact is correct.
```

M147 proves the exact all-suffix functional recurrence on `(kappa,D)`, the
infinite reachable failure of a deficit-blind pointwise scalar Bellman
closure, and the stated unrestricted fixed-moment non-identifiability result.

## Field 2 — immutable provenance

Before inspection, all six coordinator-supplied hashes matched exactly:

```text
e760b6b7620e0278c8a21969112cb5675e268217d64d2319230f9642baecee11  report.md
6084710041b5cb0797fefc05f477bc230bc70d893bb5e8ff2bb3dad9a9004d62  proof note
bcf02d860baf08f6774f858f44ab76c3307632de90d683434e355189fcf763b6  checker
441000e76bc60c12093355bda4272ee9fefc9b621c3e4b30b30d17bcb39cb06b  JSON
8989d0998e819a24dd6b22f50df75a2199b4860fede1dcdd2aacf67625a63cea  freeze manifest
3fddbaf63f38f9ff014ad5f1ee6f537e4ca994c85d8c4511da6f439f91b3c96c  SHA256SUMS
```

Rerunning M147's frozen checker to `/tmp` reproduced its JSON digest exactly
and reported zero failures.

## Field 3 — recurrence and root identities

Clean-room conversion of the accepted `(K,R)` law gives

```text
nu(j)=binom(d,j)(D)^(rise)_(d-j)(kappa-D)^(rise)_j
      /(kappa)^(rise)_d,
(kappa,D)->(kappa+d,D+d-j).
```

All `j=1,...,d` are retained. Only `j=0` and inactive targets are killed;
the latter are exactly `B+h-1<2`. Direct composition enumeration agrees with
M147's `2^L` literal support and grouped mass. An independent tree-EGF
calculation proves the normalized contextual root mean is one for arbitrary
`L`, not only for enumerated suffixes. Strict suffix descent makes the
recurrence finite.

## Field 4 — reset bound and NM-1

The correct normalized one-power bound is

```text
A_0/q <= q[C_s-sum_E a_E lambda_E]
          +sum_E theta_E^2/(q c_E).
```

Equivalently, with barred quantities it is
`A<=q[C_s-q sum abar_E lambda_E]+sum thetabar_E^2/cbar_E`, where
`A=A_0/q`. Frozen proof Section 5 states this correctly. Frozen report Field
4 writes `A/q<=` after using `A` as the normalized recurrence term; that
single extra `/q` is NM-1. It does not enter any calculation or conclusion.
The `C_s<3/4` substitution remains limited to `s>=100`.

## Field 5 — exact obstruction and reachability

At `(s,B,L)=(3,2,1)`, `q=3/8` and

```text
H/q=1/16+[2D/(K+1)-3/8]^2/4.
```

For `R=1`, equality with the `5/8` local budget occurs at exactly `K=31`
and strict failure occurs exactly for `K>=32`. At `K=32`,

```text
H_bad =175033/743424 >15/64,
H_good= 24313/743424 <15/64,
bad margin=793/743424.
```

The two states share `L,B,s,q,C_3,K,z` and every Cayley ratio, but differ in
`D`. Both are positive-probability branches of the degree-`K-1`, last-part-
four root of the fresh right-heavy parent `(K+2,1,0,2)`; the `j=1` branch
reaches the bad child with probability `1/K`. Thus the pointwise scalar
closure is genuinely refuted inside the reachable DAG. This does not refute
a nonlocal amortized potential.

## Field 6 — fixed-moment theorem

The parity measures on `{1,...,r+2}` are valid probabilities for every
`kappa>=r+4`. Their difference is an `n=r+1` finite difference: all
degree-`<=r` polynomial moments agree, while the degree-`n` rising-factorial
expectations differ by `(-1)^n n!/2^(n-1)`. Hence their averaged degree-`n`
`j=0` attachment masses differ.

Accept this only for unrestricted measure-compression schemes. The measures
are not claimed to arise from single parents or reachable mixtures. Exact
deterministic `(kappa,D)` tracking is unaffected.

## Field 7 — independent exact checks

Run from the M151 directory:

```text
python3 -B fresh_referee.py --output fresh_referee.json
```

Python 3.12.3, standard library only, exact `Fraction` arithmetic,
deterministic `seed=null`. The checker imports no predecessor code or data.
It reports zero failures across:

- 3,618 attachment entries, including transformed-law equality,
  normalization, child update, beta-binomial mean, and martingale checks;
- 6,370 literal root entries and 195 normalized root-mean cases;
- eight grouped-recursion cases, including minimal `B=1` boundaries;
- all 8,129 valid `L=1` states through `K=128`;
- the exact witness, threshold, `C_3`, and three reachability constructions;
- 13 parity pairs `r=0,...,12`, checking power, rising, and falling moments.

Checker SHA-256 and result SHA-256 are recorded in the freeze manifest.

## Field 8 — action and verified next route

Integrate M147 as an obstruction to the deficit-blind pointwise proof route,
with NM-1 corrected in coordinator prose. The first positive target remains a
deficit-aware amortized potential on `(kappa,D)` which is required to satisfy
the local budget only at right-heavy seeds.

For that next attempt, `X=d-j` is exactly
`BetaBinomial(d,D,kappa-D)`, and `D'/kappa'` is a martingale under the full
attachment law. This observation is independently verified but is only a
route suggestion; killed `j=0` mass must be charged explicitly.

## Field 9 — scope and hygiene

Accepted scope is the auxiliary unweighted full-reset excursion only. There
is no auxiliary gap, `ROOT-MEAN LIFT`, original-chain theorem, polynomial
mixing theorem, Terminal A, or Terminal B. No predecessor, coordinator,
manuscript, project-skill, or other worker file was edited. No package was
installed and no Python cache is retained.

