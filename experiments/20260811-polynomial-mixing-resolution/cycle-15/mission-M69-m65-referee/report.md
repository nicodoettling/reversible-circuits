# M69 fresh referee report: M65 contextual quotient absorption

Date: 2026-08-12.  Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

**ACCEPT.**  I found no blocking mathematical, normalization, feasibility,
or scope error in the frozen M65 bundle.  Its exact refutations are valid
auxiliary statements for the nonlazy minimal-long-cycle parking projection.
They do not prove slow mixing for the full parking projection `Pbar` or for
the identity-word heat-bath chain `K`, and M65 states that limitation
correctly.

The frozen `report.md` has the assigned SHA-256

```text
f817b7dbd9f13101b805fb3a5134633bb5f7df9e252f9ab85f3b9ea7472e4b99
```

both before and after this review.  Running `sha256sum -c SHA256SUMS` in
the M65 directory accepted all 22 listed files.

## 1. Closed conditional-mean formula

I accept equation (2.1) of the frozen report.

After conditioning on the outer and inner macros, deleting all factors
except their attachment factors leaves a uniform shuffle of two ordered
chains of lengths `K` and `k`.  The retained positions form a uniform
`(K+k)`-subset of the `r` word positions.  Therefore a fixed consecutive
pair in the binary restriction is consecutive in the full word with
probability `(K+k)/r`.

At `t=B`, the active outer factor and `I_1` are adjacent exactly in the
two prefix classes

```text
O^R OI,   O^R IO.
```

Their binary-shuffle probability is

```text
2 binom(k+K-R-2,K-R-1) / binom(K+k,K).
```

Multiplication by full-word adjacency, scan probability `1/(r-1)`, and
the selected rank-two outcome probability `1/3`, followed by division by
`alpha_r=2/[3r(r-1)]`, gives

```text
K binom(k+K-R-2,K-R-1) / binom(k+K-1,K-1).
```

Thus there is neither a missing scan factor nor an extra factor two.

For `t>B`, continuation occurs exactly when `I_1` precedes
`O_(R+1)`.  Its complement has the first `R+1` symbols all outer, so

```text
P(I_1<O_(R+1))
 =1-binom(K,R+1)/binom(K+k,R+1).
```

The accepted root-composition split flow supplies
`w_(t-B)w_B/w_t`, proving the deep line.  The below-support line is forced
geometrically.  Independently summing all three lines against `rho_s`
gave exactly

```text
w_(s+1-B)w_B/w_(s+1)
```

for every `2<=s<=10`, `1<=K<=8`, all `R`, and all `B`; this is the
required root-split stationary mean.

## 2. Marked inheritance and repeated extreme context

I accept the negative-hypergeometric mixture and its pointwise
deletion/insertion proof.  If `J=j`, the prefix before the active outer
factor contains exactly `R` ordered outer and `j` ordered inner factors.
The prefix and suffix counts are therefore

```text
binom(R+j,j),
binom(K-R-1+k-j,k-j),
```

respectively, out of `binom(K+k,k)` shuffles.  This gives the stated
`nu_j`.  Retaining the marked scan site and rank-two outcome makes the
deletion/insertion map invertible; after the accepted orbit, scan, fibre,
and `alpha` cancellations, its only remaining multiplier is `nu_j`.
The `j=0` class is zero because the active factor precedes `I_1`.
Vandermonde then gives

```text
sum_(j>=1) nu_j
 =1-binom(K,R+1)/binom(K+k,R+1).
```

The rightmost class also recomputes exactly:

```text
R=K-1, j=k
  => nu_k=K/(K+k),
     (K,R)->(K+k,K+k-1).
```

For any successive degrees `k_1,...,k_d`, the persistence weights telescope
to `K_0/(K_0+sum k_h)`; in particular a unary spine has weight
`K/(K+d)`.  Hence the extreme marked geometry can recur and cannot be
charged as a one-time context loss.

The code-independent audit enumerated 693 binary-shuffle identities with no
failure.  A fresh exact-context rerun through ambient `r=5` had zero
failures in `1+7+36=44` nonvacuous inheritance checks.  The frozen
`r=7` artifact, whose hash verifies, records zero failures in 898 checks.

## 3. Exact absorption counterexample and ambient feasibility

I accept the infinite rank-two family.  For

```text
r=K+2,   b=(3,1^(K-1)),   s=2, B=1, R=K-1,
```

the two local compositions have masses `2/3,1/3`, normalized rates
`1,2`, and conditional means

```text
H((2))=K/(K+1),   H((1,1))=2/(K+1).
```

The mean is `2/3`.  With the standard positive Laplacian convention, the
two-state generator has nonzero eigenvalue `3`, so

```text
||H-EH||^2_(-1,G_2)
 =2(K-2)^2/[27(K+1)^2].
```

The terminal budget is `2/[3(K+1)]`, and their ratio is exactly

```text
(K-2)^2/[9(K+1)].
```

It is `121/126` at `K=13` and first exceeds one at `K=14`, where it
is `16/15`.  This proves the first failure in the displayed family occurs
at ambient rank `16`; all `K>=14` fail.  At `K=14`,
`delta+a=226/225`, and the limit is `10/9`.

As a separate finite check, I exhausted all 2,275 feasible tuples
`(s,K,R,B)` with minimal ambient rank `s+K<16`.  No earlier failure
appeared; the largest ratio was the exact rank-two value `121/126`, with
maximum reported CG residual below `1e-12`.  This exclusion of other
smaller contexts is a robust numerical finite check, not an interval or
rational certificate.

## 4. Uniform failure of `delta+a<=1+C/s`

I accept the universal constant-excess argument, including its
Dirichlet/Green normalization.

For `B=1,R=K-1`, put `Z={last part=1}`.  The only quotient edges crossing
`Z` toggle the final cut.  Summing either the split flow from
`last>1` or the reversible final-boundary merge flow from `Z` gives

```text
E_(G_s)(1_Z,1_Z)=m_s=w_s/w_(s+1).
```

The standard Dirichlet form contains the factor `1/2` over both directed
orientations, so this is one stationary crossing flow, not twice that flow.
Also

```text
m_s=(s/(s+1))^(s-1)>=e^-1.
```

The one composition `(s-1,1)` gives

```text
p_s=rho_s(Z)>=1/(3e^2)=p_0.
```

Writing `q_T=E[H1_Z]` and `x=q_T/m_s`, the Green variational principle
tested on `1_Z` yields

```text
A_s=||H-m_s||^2_(-1,G_s) >= m_s(p_s-x)^2.
```

Every terminal composition has at least two parts, and

```text
H=K/binom(K+k-1,k)<=2/(K+1),
```

so `x<=2e/(K+1)`.  Choosing the fixed integer `K` with
`K+1>=144e^5` gives `x<=p_0^2/8`.  Since `p_s<=1`,

```text
delta+a-1
 >=(p_s-x)^2-x
 >=5p_0^2/8
 =5/(72e^4).
```

This is uniform in every `s>=2`, so any proposed fixed constant `C` is
defeated by taking `s` large.  The family is genuinely ambient-feasible:
`r=s+K` and `b=(s+1,1^(K-1))` realize it with the large branch leftmost.

## 5. No unsupported slow-mixing lift

I accept M65's negative scope conclusion.  The synthetic pair `(K,R)`
records a marked attachment history, not an observable on an unmarked
parking macro; different histories can collide on the same state.  A local
dual Green cost therefore cannot be read directly as a global primal
Rayleigh function.

The most literal ambient fibre also has pointwise escape.  It has mass

```text
rho_r(b)=w_(s+1)/(K!Z_r),
```

and each of its `K-1` root boundaries merges at total rate
`alpha_r K`.  Thus every subset of that fibre has conductance contribution
at least

```text
alpha_r K(K-1)=2K(K-1)/[3r(r-1)],
```

which is inverse polynomial whenever nonzero.  Finally, a strict depth-`d`
unary marked history carries the additional stationary factor

```text
[K/(K+d)] [w_(s-d)/w_s],
```

which is exponentially small for `d=Theta(s)`.  These checks rule out the
naive literal fibre/corridor lift.  They do not prove that every possible
global lift is impossible, and M65 correctly leaves weighted marked source
recovery versus unmarked nested-Rayleigh consistency unresolved.

There is no stationary-flow comparison in the bundle from this parking
projection obstruction to the original fixed-endpoint bridge or `K`.
Accordingly the bundle is neither Terminal A nor Terminal B.

## 6. Objections and qualifications

1. **Blocking objections: none.**
2. **Wording qualification:** “first feasible failure is ambient `r=16`”
   is exact for the exhibited rank-two family.  The exclusion of every other
   context below `16` is supported here by a complete high-accuracy finite
   scan, but not by an exact rational certificate.  This does not affect the
   universal refutation, which needs only the exact `r=16` witness.
3. **Proof/computation qualification:** the `r<=7` macro enumerations are
   finite falsifiers.  The universal formula and inheritance claims rest on
   the multiset shuffle and marked deletion/insertion proofs, as M65 states.
4. **Scope qualification:** the failure to lift is a correct statement that
   no lift has been constructed and that the literal candidates fail; it is
   not a theorem that no different `Pbar` slow mode can exist.

## 7. Reproduction and artifacts

Environment: Python `3.12.3`, NumPy `1.26.4`, SciPy `1.11.4`; no
random seed is used.

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/independent_exact_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/independent_exact_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/closed_mean_formula.py --r-max 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/rerun_closed_mean_r5.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/marked_context_inheritance_audit.py --r-max 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/rerun_marked_inheritance_r5.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/feasible_ambient_scan.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M69-m65-referee/feasible_ambient_below16.json --rtol 1e-12 --maxiter 50000
```

The code-independent output has SHA-256
`b49b4ab60460686e8cc8e8115e653c10cf192896edd35c2807e878056b316010`;
the below-`16` scan output has SHA-256
`53c6d7556c399c59babb8da2e09237ccbeac14e8721aa42a650a37428c2c6b02`.
All generated files are confined to this referee directory, and the runs
created no `__pycache__`.
