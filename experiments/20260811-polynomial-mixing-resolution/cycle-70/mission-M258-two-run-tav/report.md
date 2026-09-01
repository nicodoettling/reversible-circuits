# M258 report: literal two-run adjacent variation

Date: 2026-08-14 UTC.

## Verdict

```text
PROVED, SUBJECT TO FRESH INDEPENDENT AUDIT:
sum_(s=1)^(k-2) sqrt(s)|Theta_(s+1)(ell)-Theta_s(ell)|
 <=500sqrt(ell).

NO FULL-DV OR DOWNSTREAM INFERENCE.
```

The theorem holds uniformly for every odd `k>=3` and integer
`2<=ell<=(3k-1)/2`. The target is the unweighted normalized literal
B-side ordered-disjoint-double profile under uniform minimal factorizations.
There is no `q` or `qhat` averaging.

## Exact coefficient reduction

For retained set `E` of size `t`, let

```text
j=#{x in E:x+k in E mod D}.
```

Across cyclic starts, the four seam-pattern counts are exactly

```text
D-2t+j,     t-j,     t-j,     j.
```

The placement-summed cutoff coefficient is therefore

```text
(t-1)Q_ell(t)
 +[J_(r,t)/D](1{t=ell}-1{t=ell-k}).
```

This preserves both seams, simultaneous hits, both parent orientations,
every placement/kind, and repeated-size multiplicity. All placement geometry
is confined to the two signed overlap spikes.

## Reflected-head proof

The base operator is

```text
Wtilde_r(f)=sum_(t=2)^(r-1)(t-1)K(r,t)f(t).
```

It is the reflection of M251's forward `W_r`, not literally the same
operator. The proof does not import M251's forward increment lemma. Instead,
for fixed `t`,

```text
c_(r+1)(t)/c_r(t)=rho_(r+1)/rho_(r+1-t)<=1.
```

Thus a reflected head equals increasing `h(r)` until saturated and decreases
coefficientwise afterwards. Its total `r`-variation is at most `2u/R`, which
gives normalized paired head response `26sqrt(u)`. Constants annihilate
because `Wtilde_r(1)=h(r)` and the normalized constant response is one.

The explicit `Q_ell` has weighted cutoff variation at most `4sqrt(ell)`.
Finite Abel expansion consequently gives base response `104sqrt(ell)`.

## Overlap-spike proof

For short parents `r<=k-1`, `J_(r,t)=0`. For a long parent `r=k+c`, the
complete directed distance-`k` pair list in `[0,r)` has `2c+1` members. The
two complementary gaps show `J_(k+c,t)=0` for `t<=c`, and always
`J_(k+c,t)<=(t-1)(2c+1)`.

The universal bound `J<=t(t-1)` plus Stirling gives

```text
sum_(r=t+1)^(D-1) K(r,t)J_(r,t)/D <=16sqrt(t/k).
```

Positivity is used only after the exact short/long paired increment. The raw
weighted response is at most `32sqrt(t)`; the exact denominator and
normalization bounds give `160sqrt(t)` for one normalized spike.

The base and at most two spikes assemble as

```text
104+160+160=424<=500.
```

## Falsification and self-attack

`tav_exact_check.py` is standard-library only and is restricted to
`k=3,5,7`. It independently checks the four seam-pattern counts, literal
cyclic averages, overlap support, exact `Theta` decomposition, reflected
constant identity and unimodality, cutoff variation, spike bounds, and TAV.
All 4,960 assertions pass. The largest finite TAV ratio is approximately
`0.368261`. These computations are finite falsification only and do not prove
the universal theorem.

The main self-attack was the operator orientation: the base is reflected and
M251's forward `W` lemma cannot be reused verbatim. The independent
unimodality proof in `tav_theorem.md` resolves that issue.

## Dependencies, scope, and action

All frozen M199/M207, M235/M238, and M251/M255 inventories passed before
use. The proof uses their literal profile, exact two-seam geometry, exact
normalization identities, denominator bounds, and monotonicity of `rho`.

This mission proves only TAV. It does not assert full DV, conditional J2,
WPCR, SCBR, response, a spectral gap, polynomial mixing, or either Terminal.

Action: freeze M258 and request a fresh immutable audit focused on the
reflected-head orientation, exact seam-overlap coefficient, spike mass sum,
and quotient constants.

## Reproducibility

- Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`; standard library only; deterministic; `seed=null`.
- Exact command, from this mission directory:

```text
python3 tav_exact_check.py --output tav_exact_results.json
```
