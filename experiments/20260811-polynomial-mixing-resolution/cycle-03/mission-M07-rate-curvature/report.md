# M07 final report: Hurwitz rate curvature

Date: 2026-08-11  
Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## 1. Exact claim, quantifiers, and conventions

For a fixed labeled `v`-set, let `C(v,k)` be the number of connected-support
transposition words of length `k` whose ordered product is the identity.  The
convention is `(pq)(x)=p(q(x))`, and words are `t_1...t_k`.  Put

```text
k=2(v-1)+2g,
a_v(g)=C(v,k)/k!,
rho_v(0)=0,
rho_v(g)=a_v(g-1)/a_v(g)  (g>=1).
```

The assigned universal claim is that there are constants `c>0,A<infinity`
such that

```text
rho_v(g+1)-rho_v(g) >= c(v+g+1)^(-A)                    (1.1)
```

for every `v>=2,g>=0`.  Ordinary genus log-concavity is the nonquantitative
part of (1.1).  It is distinct from the already-refuted ultra-log-concavity
inequality.

I did not prove or refute (1.1) globally.  I proved these exact subclaims:

1. For every `v>=2`, the occupancy-zero increment is at least `12/v^3`.
2. For `v=2,3,4`, all increments have explicit positive lower bounds.
3. If `v>=3`, `M=binom(v,2)`, and `k-2>=4M log(2v)` (natural logarithm),
   then

   ```text
   rho_v(g+1)-rho_v(g) >= (2k-2/k)/M^2 >= k/M^2.         (1.2)
   ```

In particular (1.2) is inverse-polynomial in the requested variables.  The
unresolved set is now exactly contained in

```text
v>=5, g>=1, 2(v-1)+2g-2 < 4 binom(v,2) log(2v).          (1.3)
```

## 2. Full argument and construction

The complete proof of (1.2) is in `dense_curvature.md`.  Its central steps
are as follows.  The regular-character trace formula for all identity words
is

```text
Z_v(j)=(1/v!) sum_lambda (f^lambda)^2 nu_lambda^j.
```

For even `j`, the trivial and sign terms contribute `2M^j/v!`; every other
content sum obeys `|nu_lambda|<=M-v`.  A disconnected support has a cut of
size `q(v-q)` across which no transposition occurs.  A union bound, even
after dropping the identity condition, yields

```text
C_v(j)=(2M^j/v!)(1+e_j),
|e_j| <= (v!/2)e^(-jv/M)+v!2^(v-1)e^(-j(v-1)/M).         (2.1)
```

At `j=k-2>=4M log(2v)`, the right side of (2.1), and the corresponding
errors at `k,k+2`, are at most `1/(4k)`.  Therefore both adjacent count
ratios are within `4/(4k)` of their leading values.  Keeping these three
errors rather than using unrelated constant-factor asymptotics gives

```text
M^2[rho_v(g+1)-rho_v(g)]
 >=4k+2-(2k^2+2k+2)/k=2k-2/k.
```

This explicitly subtracts disconnected support; it is not an inference from
an unconditioned walk gap to a bridge gap.

`boundary_curvature.md` gives the remaining proved boundary statements.  The
inherited positive DYZ recurrence gives the all-`v` first increment.  The
DYZ fixed-degree polynomials yield elementary all-genus proofs for `v=3`
and `v=4`; `v=2` is the one-transposition calculation.  In particular the
special `v=2,g=0` increment is `12`; the formula `4k+2` applies only to
increments with `g>=1`.

`dyz_fixed_degree_audit.md` records the most plausible surviving exact
route.  DYZ Theorem 1, equations (14)--(15), gives

```text
C_v(x)=gamma_v(4sinh^2(x/2))/v
```

with a positive polynomial recurrence for `gamma_v`.  The associated
positive quadratic genus recurrence is DYZ Proposition 1, equation (13).
Neither currently supplies a quantitative consecutive-ratio comparison.

Two tempting closure arguments were rigorously rejected:

- ordered-split sequences in (13) are not pairwise synchronized (first exact
  negative cross term: `v=3,g=5`);
- positive log-concave coefficients in `s` are not generally preserved by
  the central-factorial substitution and factorial normalization.  The exact
  counterexample `s+s^2/5000` has a negative log-concavity determinant at
  coefficient index six.

These refute proof shortcuts, not (1.1).

## 3. Probability, runtime, path length, and congestion accounting

The result is enumerative and introduces no Markov transition, path, or
flow, so there is no new path length or congestion bound.  In the inherited
fixed-partition projection, the exact source/destination allocation rate is

```text
E_i E_j rho_(v_i)(g_i)/[M m(m-1)],
```

and comparison to the same-stationary-law uniform-destination zero-range
chain carries the separately inherited action-rate factor.  The relevant
zero-range theorem needs the rate increment at **every** occupancy `g>=0`.
Thus (1.2) does not close that theorem even at high total surplus: one
component can remain in the unresolved low-occupancy range.

The exact scanner uses the DYZ polynomial recurrence and

```text
D_x^2 s^r=r^2s^r+2r(2r-1)s^(r-1),
s=4sinh^2(x/2),
```

entirely in integer/rational arithmetic.  The largest run
`2<=v<=80,0<=g<=500` took `208.54` seconds on CPython 3.12.3 and found no
nonpositive increment.  This measured runtime is reproducibility metadata,
not a worst-case sampler runtime.  No random seed is needed because all
runs are deterministic.

## 4. Dependencies

- **Cited, hypotheses checked:** Boris Dubrovin, Di Yang, Don Zagier,
  *Classical Hurwitz numbers and related combinatorics*, Proposition 1
  equation (13), Theorem 1 equations (14)--(15), and its corollary equation
  (18):
  <https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>.
  Their `h_(g,v)=H_(g,v)/k!`; multiplying by `v!` gives this project's
  fixed-labeled `a_v(g)`, so all genus ratios agree.
- **Proved in this mission:** the character/support estimate (2.1), dense
  curvature (1.2), all-genus `v=2,3,4`, the exact transform counterexample,
  and the synchronization counterexample.
- **Proved inherited, argument rechecked:**
  `rho_v(g)>=12/v^3`, from the positive DYZ recurrence and convolution-ratio
  lemma.
- **Conditional/inherited:** a positive uniform increment bound feeds the
  named zero-range Poincare theorem and then the fixed-partition projection
  comparison.  Its hypotheses are not yet met because (1.3) remains.
- **Empirical/exact finite only:** no failure in the rectangle
  `v<=80,g<=500`.  Exact positivity in a finite rectangle does not prove a
  universal statement.

The DYZ corollary is not a positive moment representation: its integer
coefficients have both signs (already `b_(3,1)=-9,b_(3,3)=1` after common
scaling).  Moreover `a_v(g)` itself cannot be a Stieltjes moment sequence in
general, since Stieltjes moments are log-convex while the exact `v=4`
sequence is strictly log-concave at `g=1`.

## 5. First unproved standalone proposition

> **LOW-AND-INTERMEDIATE-GENUS HURWITZ RATE CURVATURE.**  There exist
> universal `c>0,A<infinity` such that, for every `v>=5` and `g>=1`
> satisfying
>
> ```text
> 2(v-1)+2g-2 < 4 binom(v,2) log(2v),
> ```
>
> one has
>
> ```text
> rho_v(g+1)-rho_v(g) >= c(v+g+1)^(-A).
> ```

An exact DYZ-specific central-factorial transform inequality is the most
focused formulation: generic positivity, coefficient log-concavity,
real-rootedness, Stieltjes moments, and pairwise synchronization are all
insufficient or false.

## 6. Strongest self-attack

The dense theorem begins only at individual genus of order
`v^2 log v`; the observed smallest increments occur much earlier, near
`g≈v/3`.  Consequently it does not control the empirically hardest regime
and cannot be substituted into the zero-range theorem by averaging over
components.  The exact scans, despite being substantially larger than the
calibration suite, have no asymptotic force.  Finally, a proof of mere
monotonicity would still be insufficient unless it gives a polynomial
margin; integrality of the exact rational determinant alone could yield an
exponentially tiny lower bound.

## 7. Calibration

- Odd word lengths are empty and never enter `a_v(g)`; all lengths here are
  `2(v-1)+2g`.
- `v=2` is handled explicitly, including the special occupancy-zero
  increment.  The globally excluded `m=2` chain is not used as a mixing
  claim.
- `C_0(2)=1,C_0(3)=24,C_0(4)=2880` and
  `rho_4(1)=16/13,rho_4(2)=195/82` are reproduced exactly.
- `g=0` is the doubled-tree/minimal connected regime and its first departure
  increment is covered by `12/v^3`.
- A zero-total-surplus allocation space is a singleton; nevertheless the
  rate theorem correctly includes `rho(1)-rho(0)` for possible departures
  when surplus is present elsewhere.
- The `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` global counts concern mixtures of
  support partitions; this fixed-connected-component theorem does not
  assert those global counts or gaps.
- The `m=4` whole-word heat bath, color interleavings, the `L=2` simulation
  failure, and local `K` normalization do not enter this enumerative ratio
  proof.  No edge/degree parity characterization is used.
- No canonical hub, bottleneck cut, or stationary-mass claim is used, so the
  canonical-hub and boundary-flow warnings are not bypassed.

## 8. Artifacts, reproduction, and citations

Artifacts in this directory:

- `dense_curvature.md`: full dense theorem;
- `boundary_curvature.md`: all-`v` first increment and all-genus degrees
  `2,3,4`;
- `dyz_fixed_degree_audit.md`: exact theorem forms, signed-moment audit, and
  failed closure principles;
- `curvature_scan.py` and three machine-readable scan outputs;
- `recurrence_sync_scan.py` and `recurrence_sync_results.json`;
- `plan.md` and `checkpoint.md`.

Reproduction commands, from this directory:

```bash
python3 curvature_scan.py --v-max 24 --g-max 240 \
  --output curvature_results_v24_g240.json
python3 curvature_scan.py --v-max 60 --g-max 300 \
  --output curvature_results_v60_g300.json
python3 curvature_scan.py --v-max 80 --g-max 500 \
  --output curvature_results_v80_g500.json
python3 recurrence_sync_scan.py --d-max 18 --g-max 30 \
  --output recurrence_sync_results.json
```

The primary citation is the DYZ PDF linked in Section 4, specifically
Proposition 1 (13), Theorem 1 (14)--(15), and the corollary (18).  No
secondary-source theorem is used.

## 9. Verdict

**OPEN AT A NAMED STEP: LOW-AND-INTERMEDIATE-GENUS HURWITZ RATE CURVATURE.**

This verdict concerns the assigned sufficient route.  It is neither a proof
nor a refutation of the global polynomial-mixing goal.

