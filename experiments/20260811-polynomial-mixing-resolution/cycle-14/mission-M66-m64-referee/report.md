# M66 fresh referee report: M64 exterior closures

Date: 2026-08-12. Repository commit recorded by the source and rerun:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`. Convention
`(pq)(x)=p(q(x))`; tuple products are left-to-right.

## Frozen source

```text
87556f69bc3e483f29b1b049c9d46effc94a320244b072e8b13940a8bdd5395d  M64/report.md
7e9d58ff6248d53b07ae20b285076973a2c24327a84c59df60521d8c7f47c124  M64/exact-n5-signature-closure.json
e5d6200de117e93392cd95f0dbd3571cb385d0cd76756ab8e4eea497cd88feb1  M64/exact_n5_signature_closure.py
```

I audited the immutable report with its inherited M60--M63 inputs and reran
the decisive `N=5` verifier into this directory.

## Audit findings

### 1. Breadth-first boundary identity and orientation: accepted

The positive off-diagonal graph of the exact heat bath is undirected. For a
fixed selected window, two words are adjacent precisely when their ordered
outside factors agree, and the two transition coefficients are the same.
With exterior graph distance measured from `A`, an exterior edge changes the
distance by at most one. Consequently every exterior edge leaving
`C_k=A union E_k` has source in `L_k` and target in `L_(k+1)`. Every other
boundary target is in `F_N minus A`. These categories are disjoint and
exhaustive, including all `H3,H4,H5` windows.

Thus

```text
Q(C_k,C_k^c)=W^(-1)[sum_(x in C_k)K(x,F_N minus A)
                    +sum_(x in L_k)K(x,L_(k+1))].
```

Since `pi` is uniform, division by
`min(pi(C_k),pi(C_k^c))=s_k/W` gives exactly the source's formula (1.4).
There is no orientation error when `C_k` exceeds one half.

### 2. Quantitative shell criterion and fixed-radius algebra: accepted

Every positive edge has a contribution

```text
1/[2|R_m|(m-r+1)|F_r(g)|]
 >=1/[2|R_m|(m-2)M^5]=p_min.
```

Every vertex of `L_(k+1)` has a predecessor in `L_k`, so selecting one edge
per target proves the claimed `p_min|L_(k+1)|` term without an injectivity
assumption on sources. The inherited M63 deletion-cell bound gives the other
term `alpha_N|A|`; its targets lie in `F_N minus A`, hence remain outside
every exterior halo.

The degree union bound has the correct indexing:

```text
|L_j|<=D_out^(j+1)|A|,
|E_k|<=|A| sum_(j=1)^(k+1)D_out^j.
```

Using `s_k<=|C_k|`, `D_out<=6NM^5<=N^11`,
`alpha_N>=1/(96N^6)`, and
`1+sum_(j=1)^(k+1)D_out^j<=3D_out^(k+1)` gives exactly
`1/[288N^(11k+17)]`. The exponent is explicitly fixed-radius and is not
misrepresented as uniform in growing `k`.

### 3. Exterior support-graph connectivity: accepted

For an exterior word with `c` labeled support components and component genera
`g_i`, the identity

```text
sum_i g_i=c-1
```

follows from `m=2N-2` and `k_i=2(v_i-1)+2g_i`. Hence, while `c>=3`, some
component has a surplus pair. The accepted quantitative Classification-H
input reaches an adjacent-pair representative inside the same macro. Replacing
a surplus square in that component by a cross-component square merges two
components and changes the merged genus to `g_U+g_V-1>=0`. The state stays
exterior until only two components remain.

Every Hurwitz pair move and every square replacement is a literal positive
`H3` edge: retain an adjacent factor on whichever side is available as
padding. The old and new triples have the same ordered product. Here
`m=2N-2>=8`, so padding always exists. No length-two simulation is assumed.

For the prescribed-label isolation step:

* If its component `W` has at least three vertices, choose `v` as a tree leaf
  and choose an internal tree edge `s` in `W minus {v}`. Replacing the leaf
  square by an extra `s` square isolates `v` and raises that remaining
  component's genus by one. Replacing the new extra `s` square by a cross
  square merges the two non-`v` components and lowers the combined genus by
  one, leaving genus one.
* If `|W|=2`, its only edge appears in one or two adjacent square copies
  according as `g_W=0` or `1`. Replacing all copies by squares on an internal
  edge of the other component creates two isolates and gives the other
  component genus two. Replacing one added surplus square by a cross square
  attaches the non-`v` isolate and leaves genus one. Every intermediate has at
  least two support components.

This checks the delicate size-two/genus-zero and genus-one cases. There are
at most `c-2` merge normalizations, one isolation normalization, and one final
normalization: at most `c` stages, each of length `50Nm^3`. There are at most
`c+1` square refreshes. Since `c<=N`, the source's
`R_ext=50N^2m^3+N+1` is valid.

Fixing one `e in E_0`, both `e` and any exterior `y` reach the same `q_v` in
at most `R_ext`, within the exterior. Thus exterior distance is at most
`2R_ext`, and the breadth-first indexing indeed gives
`E_k=F_N^c` for `k>=2R_ext`. At saturation the complement is `F_N minus A`;
reversibility and the accepted M62 bound yield `Phi_pm>=1/(24N^13)`.
Diameter is used only for exact saturation, not as a congestion argument.

### 4. Exact `N=5` signature-clique calculation: accepted

For a fixed `(r,i)`, the ordered outside factors determine the block product
from `P B S=id`. Conversely every length-`r` block with that product completes
an identity word. Thus an outside signature is exactly one conditional fiber,
not merely a superset.

For a clique of size `T` containing `a` cut states, the lazy global kernel
contributes

```text
a(T-a)/[6(m-r+1)T],
```

where `1/6=(1/2)(1/3)` is the laziness/block-size normalization. The code
uses this value for all three block sizes, computes the exact next-layer term
by signature intersections, and obtains the `F_N minus A` term by subtraction.
The cut/complement sizes and smaller-side denominators are correct.

The independent rerun reproduced every mathematical JSON field exactly after
removing only `argv` and `elapsed_seconds_before_write`. In particular:

```text
|A|=3,904,
|L_0|=314,771,
|L_1|=448,169,
L_2=empty,
Phi_pm(C_0)=0.27034185234304386...,
Phi_pm(C_1)=0.17792257098663075....
```

This remains a bounded falsifier and is not used as an asymptotic proof.

### 5. Thick midpoint formulas: accepted as a reduction only

Splitting a `2j`-factor identity word at `j=N-1` gives the exact mass
`sum_g a_j(g)^2/a_(2j)(id)`. Only windows crossing the midpoint can change
the prefix statistic. If `a` factors of a crossing window lie to the left,
then `X_j^-1X'_j=U^-1U'` and the transposition-length change is at most
`2a<=8`. The total selected-window action is at most

```text
sum_(r=3)^5 (r-1)/[6(m-r+1)] <=3/[2(m-4)].
```

This proves the stated boundary *upper* localization. M64 correctly leaves
the required asymptotic shell-mass estimate open.

## Numbered objections

1. None. The scoped Claims A--D and the midpoint reduction survive the
   requested convention, boundary, macro-surgery, normalization, and exact
   finite checks.

The acceptance uses the explicitly labeled inherited quantitative
Classification-H and M60--M63 results; it does not independently reprove
those already accepted inputs. It does not promote the open intermediate
layer inequality, infer flow from diameter, or assert Terminal A/B.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 -u experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M64-multistep-minimal-exterior-closure-redteam/exact_n5_signature_closure.py --max-radius 20 --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M66-m64-referee/exact-n5-signature-closure-rerun.json
```

The rerun is deterministic, uses Python 3.12.3, seed `null`, and no
nonstandard dependency. It can falsify the closure layers, full
`H3/H4/H5` split, or global denominator, but cannot prove asymptotic
expansion.

## Verdict

**ACCEPT**
