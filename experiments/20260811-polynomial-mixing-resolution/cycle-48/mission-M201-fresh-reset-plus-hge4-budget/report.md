# M201 final report: fresh reset plus high-tail compatibility

Date: 2026-08-13 UTC.

## 1. Verdict

```text
FINAL VERDICT: PROMOTE EXACT STRICT ROUTE OBSTRUCTION WITH FRESH REFEREE.
REFUTED: independent reservation of accepted h1-h3 bounds followed by a
         reset+h>=4 bound against the nominal leftover.
NOT REFUTED: the true fresh-parent T1<=1-q inequality.
OPEN: joint all-height actual-history slack/amortization.
```

## 2. Target, law, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, displayed left-to-right. This
mission concerns only the normalized full unweighted reset excursion `F=H/q`
in the auxiliary nonlazy minimal-long-cycle parking projection, at fresh
right-heavy parents.

## 3. Precise obstruction

At the first high-tail state `(B,L)=(2,4)`, the compatible same-parent
accepted reservations are

```text
U1=(1-q0)A1(3)=3299/56250,
U2=(2/3)M2(2)=24/125,
U3=(3/4)M3(1)=27/125.
```

With `q=3750/16807`, their residual budget is
`Delta=293289307/945393750`. The exact actual-history values satisfy

```text
T1_reset=6628367198857337/21450464220937500,
T1_h4=1735419680239/29524500000000,

T1_reset+T1_h4-Delta
=480024264873449410111/8339940489100500000000>0.
```

Thus even same-`L` exterior coefficients and exact `q0` do not make separate
sector reservations compatible with an independent reset-plus-tail proof.

## 4. Numbered objections and self-attacks

1. **Not incompatible global constants.** `U1,U2,U3` use the exact same-`L`
   operator/exterior coefficients; only their established history envelopes
   remain upper bounds.
2. **Not a normalization artifact.** The checker keeps `eta` outside, `pi_a`
   inside each branch, exactly `a<d`, and no survival factor.
3. **Not a scalar or diagonal witness.** Exact Gram `T_1` retains the full
   vector history, every Jacobi cross term, and covariance subtraction.
4. **Not a contraction counterexample.** Exact total
   `T_1=422384074903914714287/1042492561137562500000`, while
   `1-q=13057/16807`; the true slack is positive by about `0.3717112101`.
5. **Logical reach:** only the independent-reservation proof architecture is
   refuted. A coupled proof may succeed.

## 5. Exact compatible budget

For general `L`, define `U1,U2,U3` with their actual boundary cases and exact
exterior moments as in `compatibility_obstruction.md`. The residual is

```text
Delta_(B,L)=1-q_(B,L)-U1(B,L)-U2(L)-U3(L).
```

This formula retains `q0`, distinguishes `n=0` from `n>=1`, includes `r=n`,
and restores the exact number of retained observations through each exterior
first moment.

## 6. Surviving lemma

The first open statement is the joint all-height actual-history
slack/amortization lemma

```text
T_reset+sum_(h>=4)T_h-Delta
 <=sum_(h=1)^3(U_h-T_h).
```

It must preserve observation dependence, all Hilbert/Jacobi modes, cross
terms, and killed atoms. M201 proves the right-side slack cannot be discarded.

## 7. Dependencies and scope

- **Accepted immutable:** M173/M177 (`h=1`), M179/M184 (`h=2`), M193/M197
  (`h=3`), plus their accepted vector-history dependencies.
- **Proved here:** exact compatible slack and the minimal `B=2,L=4` route
  obstruction.
- **Unresolved/out of scope:** the surviving amortization lemma, nonfresh
  states, total AMV, all-`L`, gap, original-chain mixing, Terminal A/B.

## 8. Exact diagnostics and reproducibility

```text
command      | python3 -B exact_obstruction.py --output exact_results.json
arithmetic   | Python 3.12.3 standard-library Fraction
parameters   | one named minimal state B=2,L=4,kappa=2,D=1
random seed  | null
imports      | no predecessor imports
enumeration  | compositions at the named state; no range of L
```

The checker reconstructs reset currents, descendant history kernels, killed
observations, exact `T_1` by height, accepted coefficients, and both margins.

## 9. Handoff and fresh-audit request

```text
candidate                  | independent lower-sector reservation route
claimed target             | reset+h>=4 <= compatible residual Delta
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this quotient operator
exact diagnostics          | full-history Fraction check at minimal B=2,L=4
verdict                    | reject route; retain joint amortization lemma
```

Request a fresh immutable referee to verify all supplied hashes, independently
derive `U1,U2,U3,Delta` at the same parent, reconstruct the exact reset and
height-four `T_1` charges with killed observations, and confirm both the
positive obstruction margin and the positive true-budget slack. The referee
must not promote this route obstruction to a total-AMV counterexample, gap,
mixing, or terminal claim.
