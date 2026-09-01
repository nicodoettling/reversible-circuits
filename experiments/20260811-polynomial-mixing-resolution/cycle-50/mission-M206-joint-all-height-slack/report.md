# M206 final report: joint all-height slack ladder

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
FINAL VERDICT: PROMOTE STRICT EXACT SLACK-LADDER REDUCTION FOR FRESH AUDIT.
PROVED: universal B=2 suffix-zero actual-history annihilation.
PROVED: at B=2,L=4, unused h1 slack alone pays reset+h>=4 excess.
REFUTED: universal terminal-only unused-slack transfer, at B=3,L=4.
PROVED FINITE: at B=3,L=4, cumulative h1+h2 slack pays the excess.
UNRESOLVED: universal cumulative h1+h2+h3 slack certificate.
```

## Field 2 — target, object, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, displayed factors left-to-right.
This mission concerns only fresh right-heavy parents in the normalized full
unweighted reset excursion `F=H/q` of the auxiliary nonlazy
minimal-long-cycle parking projection.

## Field 3 — immutable dependencies

Complete SHA ledgers passed for M173/M177 (`h=1`), M179/M184 (`h=2`),
M193/M197 (`h=3`), and M201/M204 (compatibility obstruction and fresh
audit). Every predecessor remained immutable. The compact checker verifies
the accepted M204 literal-composition engine's exact SHA before import.

## Field 4 — exact signed accounting

For actual sector charges `T_h`, compatible accepted bounds `U_h`, and

```text
Delta=1-q-U1-U2-U3,
S_h=U_h-T_h,
X=T_reset+sum_(h>=4)T_h-Delta,
```

the exact identity is

```text
(1-q)-T_1=S_1+S_2+S_3-X.
```

Thus positive `S_h` is unused lower-sector budget and positive `X` is the
reset/high-tail excess over the nominal residual. The history sectors are an
orthogonal direct sum; no hidden cross-sector Gram term exists. Amortization
must transfer residual budget rather than invoke vector cancellation between
sectors.

## Field 5 — universal B=2 structural step

The only compositions of two are `(2)` and `(1,1)`. Neither gives a live
child at bottom two, and the only possible reset cut has activity score one,
below the active threshold two. Hence

```text
Phi_(2,kappa,D,2)=0
```

for every valid `kappa,D`. Every fresh `B=2` height-one child is such a state,
so `T_h1=0` and `S_1=U_1` for every `L>=1`. This is a universal actual-history
fact, not a finite diagnostic.

## Field 6 — exact slack ladder at the two named rows

At `(B,L)=(2,4)`,

```text
S_1-X
=9103978211751469889/8339940489100500000000>0.
```

Thus terminal unused slack alone resolves the accounting of M201's decisive
witness.

At `(B,L)=(3,4)`,

```text
S_1-X
=-58850574391835735352420545363
  /1474064677007114895360000000000<0,

S_1+S_2-X
=183315802718619702462160882861
  /1474064677007114895360000000000>0.
```

The first line exactly refutes a universal terminal-only transfer. The second
is a finite positive `h=1,2` base row, not a universal theorem. Full true
slack at this row remains positive.

## Field 7 — numbered self-objections and logical reach

1. **Could the signs be reversed?** No. Direct expansion gives
   `(1-q)-T_1=sum S_h-X`; the exact checker asserts this equality in both
   rows.
2. **Could an omitted cross term transfer energy?** No. Reset and every
   branch occupy distinct orthogonal history copies before `T_1` is summed.
   Cross terms *inside* each likelihood-weighted child remain fully retained.
3. **Is `U_1` actual feature energy at `B=2`?** No. The feature is zero;
   positive `U_1` is unused operator-envelope budget. A homogeneous transfer
   of the actual terminal vector therefore cannot explain the payment.
4. **Does the `B=3,L=4` row refute contraction?** No. Its exact true slack is
   positive, about `0.30206004`.
5. **Does the `h=1,2` finite pass prove a uniform two-rung ladder?** No. No
   such inference is made.

## Field 8 — exact diagnostics and reproducibility

```text
command      | python3 -B slack_ladder_exact.py --output slack_ladder_results.json
arithmetic   | Python 3.12.3 standard-library Fraction
parameters   | exactly B=2,L=4 and B=3,L=4
seed         | null
history      | full literal-composition Gram recursion from frozen M204
hash gate    | M204 checker SHA verified before import
killed atom  | a=d omitted exactly by the accepted engine
```

During route selection, the analytically named terminal-only inequality was
also checked at the capped neighboring rows `(2,5)`, `(2,6)`, and `(3,5)`;
these guided no promoted universal claim and are excluded from the decisive
two-row artifact. No broader scan or `L>6` computation was run.

## Field 9 — handoff and fresh-audit request

The next lemma is **cumulative lower-height unused-slack dominates
reset/higher-tail**:

```text
X(B,L)<=sum_(h=1)^3 [U_h(B,L)-T_h(B,L)].
```

A proof must construct a recursive residual certificate from the full
observation-dependent Hilbert/Jacobi history. It cannot stop universally at
`h=1`, cannot treat an envelope residual as an actual vector, and must retain
killed `a=d`.

Request a fresh immutable referee to verify all M206 hashes, reprove the
`B=2` annihilation, independently reconstruct both named rows without M204
imports, and audit the exact signs and logical scope. No all-state, total-AMV,
gap, mixing, or Terminal inference is requested.
