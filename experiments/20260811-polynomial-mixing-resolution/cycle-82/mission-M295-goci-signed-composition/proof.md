# M295 fixed-middle signed-composition obstruction

Date: 2026-08-14 UTC.

Status: the factorization and finite counterexample below are **proved**.
The proposed universal pairing `(FMCP_1)` is **refuted**.  Both accepted
gapped owner-correlation inequalities remain **unresolved**.

## 1. Scope and exact accepted formula

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, odd `k>=3`,
`n=3k`, and `2<=ell<=n-2`.  Put

```text
L=(1,...,k-1,2k,...,3k-1),     M=(k,...,2k-1),
C_-=(0,...,k-1),               C_+=(2k,...,3k-1),
F=C_-C_+.
```

For a supported product `s`, the accepted centered channel coefficients are

```text
beta_1(s)
 =sum_(ef=s; e in T(L),f in T(M))nu_L(e)nu_M(f)
  -1/2 sum_(C in {C_-,C_+})
        sum_(ef=s; e in T(C),f in T(M))nu_C(e)nu_M(f),

beta_2(s)
 =a(s)[F_(r-2)(s^-1L)/F_r(L)-F_(r-2)(s^-1F)/F_r(F)],
```

where `a(s)=3` for a triangle and `2` for a double.  There is no further
channel-two `1/2`.  With three/four positive composition representations
and no extra `n`, M285/M287 prove

```text
eta_j(F_ell)
 =1/3 sum_(r,g_1+g_2+g_3=n) beta_j(s_T(r,g))R_T(g,ell)
 +1/4 sum_(r,g_1+...+g_4=n)
   [beta_j(s_S(r,g))R_S(g,ell)
    +beta_j(s_N(r,g))R_N(g,ell)].                    (1.1)
```

On the admissible lags, each state response is exactly

```text
F_ell(s)=sum_x A_s(x)A_s(x+ell)
 +sum_(i:d_i>=3)delta_(d_i)C_ii^s(ell),             (1.2)
```

with nonnegative summands.  The signed coefficients, not the response
states, are the remaining difficulty.

## 2. Exact fixed-middle factorization

Channel one always uses one exterior chord `e` and one middle chord `f`.
Their supports are disjoint, and the product `ef` uniquely identifies which
factor is exterior and which is middle.  Define, with absent chord-law terms
zero,

```text
gamma_k(e)=nu_L(e)
 -1/2 1[e in T(C_-)]nu_(C_-)(e)
 -1/2 1[e in T(C_+)]nu_(C_+)(e).                    (2.1)
```

Then direct substitution in `beta_1` gives

```text
beta_1(ef)=gamma_k(e)nu_M(f),
sum_e gamma_k(e)=1-1/2-1/2=0.                       (2.2)
```

Consequently

```text
eta_1(F_ell)
 =sum_(f in T(M))nu_M(f) S_(k,ell)(f),
S_(k,ell)(f)=sum_e gamma_k(e)F_ell(ef).              (2.3)
```

This is also a literal grouping of the `S/N` positive compositions in
`(1.1)`: for each `ef`, the four support vertices determine exactly one of
the separated or nested compatible double topologies.  No triangle term is
present in channel one.

The predeclared candidate was

```text
(FMCP_1)  S_(k,ell)(f)>=0
```

for every middle chord.  It recombines *all* signed exterior coefficients
at fixed `f`; it is not atomwise positivity, response FOSD, conditioned
Borel monotonicity, or signed PSD.  Since every `nu_M(f)>0`, `(2.3)` proves
that `(FMCP_1)` would imply `(GOCI_1)`.

## 3. Why the interval proof cannot close

Expanding `(1.2)` at fixed `f` leaves a signed sum over the exterior chord.
The identity `sum_e gamma_k(e)=0` cancels only an `e`-independent baseline.
Both the `S/N` topology and the three owner sizes change with `e`, so the
remaining interval-overlap terms do not share a fixed coefficient or a
common positive direction.  The following exact counterexample shows this
is not merely a limitation of the attempted expansion.

## 4. Exact `k=5` counterexample

The candidate was frozen in `checkpoint.md` before computation.  The sole
new-rank calculation uses `k=5`, `n=15`, all twelve admissible lags, and the
ten middle chords.  It reconstructs all quantities as exact `Fraction`
values without importing predecessor code or data.

At

```text
f=(6,9),       ell=6,
```

the fully recombined fixed-middle cell is

```text
S_(5,6)((6,9))
 =-779985545058827083283361063988362608513
   /11367752922135489592720891699200000000000
 <0.                                                   (4.1)
```

The same value occurs at the reflected lag `ell=9`.  Thus `(4.1)` is an
exact counterexample to universal `(FMCP_1)`.  Across the 120 tested
`(ell,f)` cells, exactly 16 are negative.

The checker has four independent consistency layers:

1. each of the four chord laws has exact total mass one and
   `sum_e gamma_k(e)=0`;
2. the direct residual-cycle completion response equals the repaired
   owner-autocorrelation response on all admissible lags;
3. a separately implemented positive-composition `S/N` interval formula
   equals the direct response at every state and every circular lag;
4. after the required `nu_M` average, every channel-one lag total is
   positive and reflection is exact.

With

```text
alpha_1=16/33,
Lambda_15=129746337890625/1792160394037,
R_15=132,
```

the independently reconstructed minimum weighted channel value is

```text
469380953030255528575240193615921483304253622141733093283
/62593163860600167157006651607817304625660070187459136716800,
```

exactly the accepted frozen M274/M277 `k=5` value.  Therefore `(4.1)` is
not a GOCI/OCI counterexample: cancellation across different middle chords
keeps the full channel-one row positive at this rank.

## 5. Exact conclusion and next lemma

**Refuted:** a proof of `(GOCI_1)` cannot sign the fully recombined exterior
coefficient separately for every fixed middle chord.  Even after all
positive and negative exterior atoms are combined, cancellations between
middle-chord phases are essential already at `k=5`.

**Unresolved:** `(GOCI_1)`, `(GOCI_2)`, the weaker cross-channel
minority-mass bound, CP/OS+/MS/FCL1, every gap, mixing, and Terminal.

The first possible repair is a genuinely cross-middle grouping, for example
aggregation over every phase of one middle cut-size class before asking for
a sign.  No such statement is asserted or tested here.  Any future pairing
must retain at least this middle-phase cancellation and, for channel two,
the triangle/double and fair-component normalizations.

