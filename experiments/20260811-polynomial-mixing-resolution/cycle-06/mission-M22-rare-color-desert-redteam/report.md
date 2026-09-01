# M22 final report: rare-color deserts are not full-chain bottlenecks

## 1. Exact claim, quantifiers, kernel, and convention

Permutations multiply as `(pq)(x)=p(q(x))`, and a word has ordered product
`t_1...t_m`.  Put `M=binom(N,2)`.  In the family below `m>=6`, so the exact
kernel under review is

```text
K = (1/2)I
  + (1/6) sum_{r=3}^5 [1/(m-r+1)] sum_{i=1}^{m-r+1} H_{i,r},
```

where `H_{i,r}` is uniform on the complete length-`r` transposition fiber
with the current ordered product.

**Theorem (proved, scoped rejection).**  For every integer `N>=5`, set

```text
L=N^3,                 m=4(L+1).
```

Let `D_N` contain every global identity word whose support graph has exactly
two labeled connected components, one of size three and weight four and the
other of size `N-3` and weight `4L`, and whose four small-component factors
have at least `L` large-component factors between every consecutive pair.
The endpoint gaps are unrestricted.  Then

```text
pi_{N,m}(D_N) <= (1/2) exp(-15N^2) < 1/2,             (1.1)

Phi_pm^K(D_N)
 := Q_K(D_N,D_N^c)/min(pi(D_N),pi(D_N^c))
 >= 2/[3(L+4)(m-2)M^2]
 >= 4/(15N^10).                                       (1.2)
```

If `R_N` is the more rigid subset with exact color word `(A B^L)^4`, then

```text
Phi_pm^K(R_N) >= 1/[6(m-2)M^2] >= 2/(15N^7).          (1.3)
```

Thus neither the exact-color obstruction nor its natural separation-threshold
thickening is a superpolynomial-conductance family for the original chain.
This refutes this proposed Terminal-B route only; it is not a lower bound on
the global spectral gap.

## 2. Full argument

### 2.1 Exact global stationary mass

Let `C_v(k)` denote the number of connected-support identity transposition
words of length `k` on a fixed labeled `v`-element set, and let
`Z_N(m)=|Omega(N,m)|`.  The small component has exactly

```text
C_3(4)=27-3=24                                           (2.1)
```

internal words: among the 27 identity words in `S_3` of length four, exactly
the three fourth powers of one edge have smaller support.

Write the numbers of `B` factors before the first and after the last `A` as
`b_0,b_4>=0`, and the three internal gaps as `b_i=L+c_i`, `c_i>=0`.  Since
there are `4L` total `B` factors,

```text
b_0+b_4+c_1+c_2+c_3=L.                                 (2.2)
```

There are therefore `binom(L+4,4)` desert color words.  The standard
component-interleaving bijection is exact here: choose the labeled small
component, its internal word, the large internal word, and a color word;
interleave while retaining each internal order.  Disjoint components commute,
so every output is an identity word, and all four inputs are uniquely
recoverable.  Hence

```text
|D_N|
 = binom(N,3) 24 C_{N-3}(4L) binom(L+4,4),             (2.3)

pi(D_N)=|D_N|/Z_N(m).                                  (2.4)
```

This remains injective when `N=6`, because the size-three component of weight
four is distinguished from the size-three component of weight `4L`.

For even `m`, let `P` be the uniform random-transposition kernel.  Its
`m/2`-step law is supported on one parity coset of size `N!/2`.  Symmetry and
Cauchy--Schwarz give the global return-count bound

```text
Z_N(m)/M^m
 = P^m(e,e)
 = sum_g P^{m/2}(e,g)^2
 >= 2/N!,

Z_N(m)>=2M^m/N!.                                      (2.5)
```

This argument is valid whether `m/2` is even or odd; only the parity coset
changes.

Put `M_B=binom(N-3,2)`.  The connected large-component count is at most the
number of all transposition words on that component,
`C_{N-3}(4L)<=M_B^{4L}`, and
`24 binom(L+4,4)<=m^4`.  Equations (2.3)--(2.5) imply

```text
pi(D_N)
 <= [N! N^3 m^4/(2M^4)] (M_B/M)^{4L}.                 (2.6)
```

Now

```text
1-M_B/M = 6(N-2)/[N(N-1)] >= 9/(2N),
```

so `(M_B/M)^{4L}<=exp(-18N^2)`.  Also `m<=8N^3`,
`N!<=N^N`, and for `N>=5`,

```text
(N+15)log N+12log 2 <=3N^2.                            (2.7)
```

Dropping the favorable factor `M^{-4}` in (2.6) proves (1.1).  In
particular, this is a rigorous global orientation; no conditional-macro mass
is substituted for `pi_{N,m}`.

### 2.2 Exact boundary layer

Within (2.2), impose `c_1=0`, meaning that the first internal gap has exactly
`L` large-component factors.  This leaves four nonnegative variables summing
to `L`, so the number of such color words is `binom(L+3,3)`.  Every color word
in `D_N` has the same number of choices of label set and internal words.
Therefore the exact stationary fraction of this boundary layer within `D_N`
is

```text
binom(L+3,3)/binom(L+4,4)=4/(L+4).                     (2.8)
```

More generally, for four rare factors in a word of length `m`, the analogous
fraction at any feasible separation threshold `h` is

```text
4/(m-3h).                                               (2.9)
```

Thus thickening a fixed color word by a separation inequality merely moves an
inverse-polynomial boundary layer.

### 2.3 A specified genuine heat-bath exit

Fix a state in the layer (2.8).  At the start of the first tight gap, the
first three factors are `(a,b,c)`, with `a` in the small component and `b,c`
in the large one.  The two support components are disjoint, so `ab=ba` and

```text
abc=bac.                                                (2.10)
```

Consequently `(b,a,c)` is a member of the exact same-product `H_3` fiber.
This update retains the labeled weighted component macro and each within-color
subsequence, but it leaves only `L-1` `B` factors between the first two `A`
factors.  It therefore exits `D_N`.

For every product `g`, a length-three transposition fiber has size at most
`M^2`: after its first two transpositions are chosen, the third permutation is
forced, and only some choices make it a transposition.  The full-chain
probability of this one specified outcome is therefore at least

```text
[1/(2|{3,4,5}|)] [1/(m-2)] M^{-2}
=1/[6(m-2)M^2].                                        (2.11)
```

Averaging (2.11) over the exact fraction (2.8), and using (1.1) to orient the
conductance denominator, proves the first inequality in (1.2).  Finally,

```text
L+4<=2N^3,       m-2<=5N^3,       M^2<=N^4/4,
```

proves its second inequality.  The same update is available from every state
of the rigid color word, proving (1.3).

### 2.4 Full `r=3,4,5` and merge/split accounting

Let `K_r=(m-r+1)^{-1}sum_i H_{i,r}`.  Since the lazy identity term has no
boundary flow, the exact decomposition is

```text
Q_K(D_N,D_N^c)
 = (1/6) [Q_{K_3}(D_N,D_N^c)
          +Q_{K_4}(D_N,D_N^c)
          +Q_{K_5}(D_N,D_N^c)]

 = Q_{3,designated-swap}
   +Q_{3,residual}+Q_{4,all}+Q_{5,all}.                (2.12)
```

Every term on the last line is nonnegative.  Component merges, splits,
weight changes, and label repartitions produced by any block length are in
the residual terms and therefore increase the flow.  The proof keeps only
the designated swap term.  This is legitimate for the lower bound (1.2);
discarding these terms would be illegitimate in an attempted conductance
*upper* bound.  Thus all transition normalizations and all three block sizes
are accounted for without assuming that macro-changing updates vanish.

The exact `N=5,m=24,L=5` audit makes their magnitude concrete.  From the
representative `(ABBBBB)^4`, the probabilities below already include the
full coefficient `1/6` for the selected block length:

| `r` | merge to full support | two-component macro change | split to `>=3` | same-family macro, non-desert | stays |
|---:|---:|---:|---:|---:|---:|
| 3 | 0.1131907308 | 0.0441176471 | 0 | 0.0037878788 | 0.0055704100 |
| 4 | 0.1335111823 | 0.0305122049 | 0 | 0.0015589569 | 0.0010843226 |
| 5 | 0.1527644615 | 0.0135666347 | 0 | 0.0002157239 | 0.0001198466 |

The total exact one-step exit probability is

```text
1454531591/2949019920 = 0.4932254208035326.             (2.13)
```

There is no split outcome from this particular representative; the harness
explicitly checks and records the zero category rather than conflating it
with unexamined flow.  Other states can have different macro-change profiles.
The finite calculation is falsification-only; the asymptotic rejection is the
proof (2.3)--(2.12).

## 3. Probability, runtime, path length, and congestion accounting

- Worst-case designated exit from the tight boundary layer:
  `1/[6(m-2)M^2]`.
- Exact fraction of the cut on which that designated exit is charged:
  `4/(L+4)`.
- Resulting conductance lower bound: (1.2), with no hidden conditioning or
  renormalized restriction.
- The comparison path has length one: one actual `H_3` outcome.  No hub,
  routing, or multicommodity congestion is used.
- The exact harness enumerates `M^r` local words for `r=3,4,5`, then every
  target in the 63 selected window fibers.  Runtime is `O(M^5+m M^5)` under
  its deliberately simple implementation, polynomial for fixed block size;
  observed wall time was about 1.4 seconds under Python 3.12.3.
- The proof requires no new sampler.  The inherited exact conditional sampler
  has polynomial per-update cost for `r<=5`.

## 4. Dependencies, with status

1. **Proved here:** exact color-gap composition count, equations
   (2.2)--(2.3).
2. **Proved here:** the global even-time return lower bound (2.5) by
   Cauchy--Schwarz.
3. **Proved here:** global mass orientation (1.1).
4. **Proved here:** ordered-product identity (2.10), exact boundary-layer
   ratio (2.8), and full normalized exit bound (2.11).
5. **Proved/inherited and rechecked in the argument:** disjoint support
   components commute and interleave bijectively.
6. **Proved/inherited:** exact same-product heat bath is reversible for the
   global uniform law.  This report only needs its stated uniform-fiber
   transition probabilities.
7. **Exact finite, not asymptotic evidence:** `results.json` and the three
   calibration identity-word counts.
8. **No conditional dependency:** no connected-Hurwitz gap, mean-lift bound,
   fresh-square lemma, character asymptotic, or unrecorded experiment is used.

## 5. First unproved standalone proposition

> **RARE-MACRO-CLOSURE.**  For an explicit infinite sequence, determine the
> globally oriented conductance of a set containing the *entire* macro with
> one size-three weight-four component, together with whatever adjacent
> merge/split macros are necessary to absorb all polynomial same-macro color
> exits.  Either prove inverse-polynomial boundary flow or prove a
> superpolynomial upper bound after exactly accounting for the stationary mass
> of this closure.

This proposition is not the exact-color/desert obstruction rejected here.

## 6. Strongest self-attack

The theorem rejects one precise and natural lift, plus every analogous
same-macro separation-threshold thickening through (2.9).  It does **not**
rule out a more elaborate cut that includes the tight color layer and a large
collection of neighboring component macros.  The lower bound is averaged over
an exact boundary layer, not pointwise over every desert state.  It therefore
cannot be promoted to a global spectral-gap lower bound, and failure of this
cut is not evidence that Terminal B is false.

The set itself has exponentially small stationary mass.  That causes no
orientation error in this rejection because (1.1) is exact enough to identify
`min(pi,1-pi)=pi`, and conductance divides by that same mass.  It would matter
critically if one tried to infer a bottleneck without this calculation.

## 7. Calibration

- Odd `m`: `Omega` is empty; not claimed.  The family has even `m`.
- `m=0`, `N=2`: singleton cases; outside the quantified family.
- `m=2`: excluded and not used.
- The exact harness reproduces `|Omega(3,4)|=27`,
  `|Omega(4,4)|=120`, and `|Omega(4,6)|=3936`.
- At `m=4`, `H_4` is a whole-word heat bath.  The theorem is not stated in
  that regime and makes no normalization claim that drops it.
- The rare component is genuinely near-minimal: size three, length
  `2(3-1)=4`.  The large component is feasible because its even length `4N^3`
  exceeds `2((N-3)-1)`.
- Ordered color interleavings, not unordered graph data, produce the exact
  factor `binom(L+4,4)`.
- No edge-multiplicity or vertex-degree parity characterization is invoked.
- The proof uses one actual length-three update, not the known-false `L=2`
  simulation claim.
- The global mass denominator and all `Q_3+Q_4+Q_5` boundary terms are
  explicitly treated.
- The source finite pattern `(ABBBBB)^4` is checked with all exact local
  fibers; the finite result is not used as asymptotic proof.

## 8. Artifacts, reproduction, and repository state

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `exact_desert_audit.py`
- `results.json`
- `report.md`

Reproduce from this directory with:

```bash
python3 exact_desert_audit.py --output results.json
```

The run is deterministic (no seed), uses only the Python standard library,
records Python `3.12.3`, repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, the exact command, fiber sizes,
rational probabilities, and the convention in `results.json`.

No external literature is required for this report.

## 9. Verdict

REFUTED

The verdict concerns the named exact-color/desert Terminal-B construction,
not the global polynomial-mixing question.
