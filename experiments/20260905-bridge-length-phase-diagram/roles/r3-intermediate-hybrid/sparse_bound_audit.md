# Fresh nonauthor audit: the minimal-component sparse sampler

Proposer: coordinator. Referee: `r3-intermediate-hybrid`. Initial independent
audit completed 2026-09-05 15:23 UTC. Verdict: **ACCEPT**, with the stated
domain `N>=2`, even `m<=N`, and expected polynomial-time exact random draws.
The derivation below independently checks the coordinator's incidence
argument. The finite checks in `results.json` are normalization/falsification
checks and are not the asymptotic proof.

## Statement

Let `m=2k<=N`. Let `A` be the identity words whose every nontrivial support
component on `v` labels has exactly `2v-2` factors. There is a polynomial-time
exact sampler for `U_(N,m)(.|A)`, and

```
d_TV(U_(N,m)(.|A), U_(N,m))
 = 1-|A|/|Omega(N,m)|
 <= min(1, k^4/[3(N-2k+1)^2])
 = min(1, m^4/[48(N-m+1)^2]).
```

The empty word, `m=2`, and `N=2` boundary laws are exact. For a requested
`0<epsilon<1`, the displayed inequality is a sufficient criterion for the
minimal sampler's output law to be epsilon-close to the global target. Its
endpoint is always exactly identity.

## Dependencies checked

1. Exact component/interleaving disintegration, proved independently in
   `report.md`.
2. DYZ Proposition 1 equation (13), normalized by
   `C(v,2v-2+2g)=v!(2v-2+2g)! h[g,v]`; coordinator reconciled the primary
   source, and the integer recurrence in `component_audit.py` independently
   matches direct enumeration. The elementary positive convolution argument
   gives `A_g(v)<=A_0(v)(v^3/12)^g`, where
   `A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!`. M12 records this same ratio bound.
3. DPS Proposition 3 / Theorems 4 and 5 give the exact minimal connected
   sampler. M119 independently audited the `v`-to-one root quotient; the
   present exact check re-enumerates all rooted inputs at `v=2,3,4`.

## Independent incidence proof

Drop the common final factor `m!` from every macro weight, and write `S_G`
for the sum of the resulting weights at total surplus `G`. In particular
`S_0=|A|/m!`. For each positive-surplus macro erase all its component
surpluses. The resulting labeled minimal macro `alpha` has base cost

```
K = sum_B(|B|-1) = k-G.
```

It has at most `2K` active labels. For this fixed `alpha`, summing over all
ways to distribute surplus `G` among its components gives weight at most

```
w(alpha) (sum_B |B|^3/12)^G <= w(alpha)(k^3/12)^G.   (1)
```

For the last inequality, put `a_B=|B|-1>=1`. Merging any two positive
`a,b` increases `(a+1)^3+(b+1)^3` to `(a+b+1)^3`, because the difference is
`3ab(a+b+2)-1>0`. Thus `sum |B|^3 <= (K+1)^3 <= k^3` when `G>=1` and the
base is nonempty. If `K=0`, the base has no components and cannot carry
positive surplus, so it contributes zero. This handles the apparent `G=k`
exception without inventing a genus sequence for an isolated label.

Now extend each base `alpha` by adding `G` pair components on distinct
previously isolated labels. If `n_iso` labels were isolated, the number of
unordered fresh matchings is `(n_iso)_(2G)/(2^G G!)`. Each added component
has normalized weight `A_0(2)=1/2`. Therefore the sum of extension weights
from `alpha` is exactly

```
w(alpha) (n_iso)_(2G)/(4^G G!)
 >= w(alpha) (N-2k+1)^(2G)/(4^G G!),                 (2)
```

because `n_iso>=N-2K=N-2k+2G`. Every final cost-`k` minimal macro is reached
at most `binom(k,G)` times: a preimage is determined by deleting `G` of its
size-two components, and it has at most `k` such components. The incidence
weight is exactly the final macro weight, so double counting (2) yields

```
sum_{base alpha} w(alpha)
 <= S_0 binom(k,G) 4^G G!/(N-2k+1)^(2G).
```

Combining this with (1) and `G! binom(k,G)<=(k)^G` proves

```
S_G/S_0 <= R^G,   R=k^4/[3(N-2k+1)^2].              (3)
```

If `0<=R<1`, write `x=sum_(G>=1)S_G/S_0`. Equation (3) gives
`x<=R/(1-R)`, and the actual TV error is `x/(1+x)<=R`. If `R>=1`, the
trivial TV bound gives the stated minimum. No unnormalized error sum is
mistaken for TV, and no labeled matching or `2!` weight is omitted.

## Implementation and boundary audit

- Exact global/minimal counts are `27/24`, `120/114`, `3936/2880` at
  `(N,m)=(3,4),(4,4),(4,6)`. Their exact conditional TV errors are
  `1/9`, `1/20`, and `11/41`.
- All 11 required/boundary exact cases have normalized per-word assembly
  probabilities. DPS rooted inputs have exactly `v` preimages per word.
- The closed bound is tested on every applicable row of the stored
  `N<=48,m<=96` certificate table. It is intentionally loose; finite data
  are not promoted to a stronger scale.
- The construction of a minimal connected word on `k+1` labels shows `A`
  is nonempty in this theorem's range. More generally, `A` is nonempty
  exactly for even `0<=m<=2N-2` when `N>=2`.
- Minimal-only sampling is not exact globally at `m=2N-2` for `N>=3`:
  the explicit `(3,4)` and `(4,6)` counts reject that claim.

No material objection remains. Any improved bound must stay in regimes not
excluded by the named-method forest obstruction in `report.md`: the
minimal-only sampler's TV error tends to one for every fixed
`m=Theta(N^alpha)`, `alpha>2/3`. Sharper control of the weighted
minimal-assembly moment `sum_B |B|^3` may improve the remaining sublinear
sparse range; it cannot yield a linear-length guarantee for this sampler.
