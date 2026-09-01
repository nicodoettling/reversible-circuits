# M229 clean-room proof audit of immutable M226

Date: 2026-08-13 UTC.

Verdict: **ACCEPT**, with one nonmaterial domain qualification. M226's exact
scalar reduction is correct on the full WBE parameter range. YCM, TCM, WBE,
and DE remain unresolved.

## 1. Immutable gate

All seven files named by frozen M226 passed `sha256sum -c SHA256SUMS` before
use. Its checksum-file digest is exactly

    a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a.

The M217 and M222 inventories used only for the final conditional implication
also passed, with digests `7772f6ec...5557` and `d2a43d90...e7ccd`.
No predecessor was edited.

## 2. Independent B coefficient collection

Put `D=2k-1`, `R=2k-3`, `j=(k-1)/2`, and

    Q_s=[k/(k-1)]b_s b_(k-s)/b_k.

For the WBE cutoff let `L=(3k-1)/2`. Every argument of `G_k` actually used
in M226's seam formulas lies in `1<=x<=L-1`. On this range, the coefficient
of `F_ell(x)` in the q-averaged raw B numerator has exactly three sources:

1. `h(D-s)F_ell(s)` at `s=x`, contributing
   `1{x<=j}Q_x h(D-x)`;
2. `W_s(F_ell)` for `s>x`, contributing
   `Q_s(s-x-1)K_R(s,x)`; and
3. `W_(D-s)(F_ell)` for every `1<=s<=j`, contributing
   `Q_s(D-s-x-1)K_R(D-s,x)`.

Since `x<=L-1<D-s` throughout the third source, every displayed kernel is
in its valid domain. Summing gives exactly M226 (2.1):

    G_k(x)=1{x<=j}Q_x h(D-x)
      +sum_(s=x+1)^j Q_s(s-x-1)K_R(s,x)
      +sum_(s=1)^j Q_s(D-s-x-1)K_R(D-s,x).          (2.1)

The remaining surviving term `h(s)F_ell(D-s)` is invisible in the complete
cutoff range: for `x=D-s`, the smallest two-seam ambient gap is `2k-s`, at
least `L+1`. Thus it supplies no coefficient of a size `y<=L`.

## 3. Independent seam collection

For `x<k`, the exact atoms of `F_ell(x)` have sizes and multiplicities

    (x,D-2x), (x+1,x), (x+k,x).

For `x>=k`, putting `c=D-x`, the only atom that can have size at most `L`
is `x+1`, with multiplicity `c=D-x`. Therefore:

- if `2<=y<k`, size `y` comes from `x=y` and `x=y-1`, giving

      B^Y_(k,y)=((D-2y)/D)G_k(y)+((y-1)/D)G_k(y-1);

- if `y=k`, only `x=k-1` contributes, giving

      B^Y_(k,k)=((k-1)/D)G_k(k-1);

- if `k<y<=L`, the short-arc atom comes from `x=y-k`, while the long-arc
  small atom comes from `x=y-1`, giving

      B^Y_(k,y)=((y-k)/D)G_k(y-k)
                +((2k-y)/D)G_k(y-1).

These are M226 (2.2)--(2.3), including both seam cases and endpoints.

## 4. Independent A convolution

Extend `Q_r=k b_r b_(k-r)/[(k-1)b_k]` symmetrically to
`1<=r<k`. Pairing the two marked parent sizes `s,k-s` converts their union
to all `r=1,...,k-1`. Fix `2<=y<k` and put `m=k-y`. The coefficient of the
cutoff atom at `y` has:

- marked plus untouched surviving mass

      (m/k)Q_m[h(m)+u]
       =[b_y b_m/(R b_k)]
         [m+(m-1)(m-2)/(k-1)];                     (4.1)

- marked fragmentation mass

      (m/k)sum_(r>y)Q_r(r-y-1)K_R(r,y).             (4.2)

Writing `t=r-y`, the only convolution needed in (4.2) is

    sum_(t=1)^(m-1)(t-1)b_t b_(m-t)
      =[(m-1)(m-2)/m]b_m.                           (4.3)

Indeed symmetry gives
`sum t b_t b_(m-t)=(m/2)sum b_t b_(m-t)=(m-1)b_m`,
and subtraction of
`sum b_t b_(m-t)=2(m-1)b_m/m` proves (4.3). Hence (4.2) equals

      [b_y b_m/(R b_k)](m-1)(m-2)/(k-1).            (4.4)

- untouched fragmentation mass

      mK_R(k,y)=m b_y b_m/(R b_k).                  (4.5)

Adding (4.1), (4.4), and (4.5) proves

    A^Y_(k,y)=[2b_y b_(k-y)/(R b_k)]
       [(k-y)+(k-y-1)(k-y-2)/(k-1)].                (4.6)

For `y>=k`, `J_ell` and the untouched child cutoff have no such atom, so
the coefficient is zero. This independently proves M226 (2.4).

## 5. Exact prefix and two-run identities

The cutoff indicator is `sum_(y=2)^ell 1{size=y}`. Finite linearity and the
coefficient identities above therefore give

    S_Y+K_Y=sum_(y=2)^ell(B^Y_(k,y)-A^Y_(k,y)).     (5.1)

For every literal ordered disjoint pair, the residual has three face atoms
with multiplicity. `Y_ell` counts precisely its one-run atoms in the cutoff,
while `X_ell` counts both one- and two-run atoms. Thus `X_ell-Y_ell` counts
the two-run atoms, including any equal-size collision separately. Keeping
the original ordered tuple and q weights also keeps every same/cross kind
and both seams. Consequently

    (S_X+K_X)-(S_Y+K_Y)
      =sum_(y=2)^ell(T^B_(k,y)-T^A_(k,y))           (5.2)

with the exact B-minus-A sign. This verifies M226 (3.1).

## 6. Conditional implications only

Assume YCM and TCM, with constants `C_Y,C_T`. Equation (5.1) gives WBE for
Y. Equations (5.1)--(5.2) and one triangle inequality give

    |S_X+K_X|<=|S_Y+K_Y|+|sum_(y<=ell)c^T_(k,y)|
               <=(C_Y+C_T)sqrt(ell)/k.

Thus YCM+TCM imply WBE for both observables. This does not prove either
moment lemma or WBE.

Conditionally on WBE, the already audited M217/M222 identity
`DE_Z=S_Z+K_Z+N_Z`, with `N_Z=O(k^-2)`, gives DE because `k>=3, ell>=2`
allow the remainder to be absorbed into `C sqrt(ell)/k`. This does not prove
DE or any later statement.

## 7. Clean-room exact checks and shortcut witness

`checker.py` imports no M226 code or data. At `k=3,5` it independently:

- compares the direct three-source B coefficient with (2.1) on every
  argument used by the seam formulas;
- compares direct B and four-source A atoms with (2.2)--(2.4);
- reconstructs literal ordered tuples and verifies the one-run/two-run/total
  identity coefficient by coefficient.

All checks pass.

At `k=5`, choose B first edge `{3,10}`. The post-first parent
`(1,2,10,11,12,13,14)` has size seven. Among disjoint second edges with
unordered child size one, exactly these five have two-run face size at most
`ell=7`:

    edge {1,2}: size 7,     edge {1,14}: size 6,
    edge {11,12}: size 7,   edge {12,13}: size 7,
    edge {13,14}: size 7.

Thus the proposed count is five, whereas `4 min(7,1)=4`. This independently
reproduces M226's exact refutation.

## 8. Numbered objections

1. **Material objections:** none.
2. **Nonmaterial domain qualification:** M226 introduces (2.1) “for
   `x>=1`” and calls it the complete coefficient. It should restrict the
   formula to `1<=x<=L-1`, the full range used by (2.2)--(2.3). Outside
   that range some displayed kernels leave their domain and the invisible
   long surviving source is omitted. For example, at `k=7,x=L=10`, that
   source has coefficient `Q_3 h(3)=320/26411`; nevertheless
   `F_ell(10)=0` for every allowed `ell<=10`, and no seam formula invokes
   `G_k(10)`. The qualification changes no coefficient, lemma, or implication
   in M226's reduction.

Final verdict: **ACCEPT** the strict reduction with this domain qualification.
Keep YCM, TCM, WBE, DE, J2, and all downstream claims open.

