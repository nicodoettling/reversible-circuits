# M91 final report: balanced two-step posterior cancellation

Date: 2026-08-12.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, convention, scope, and status

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Fix odd `n>=7` and `h=(0 1 ... n-1)`.  The target is the
uniform law on minimal length-`n-1` transposition factorizations of `h`, and
`bar K_n` is M73's exact rank-two pair-product kernel after quotienting by
simultaneous conjugation by `h`.

The assigned strict-edge claim

```text
TV(bar K_n^2(alpha,.),bar K_n^2(beta,.)) <= C/n^2
```

for every edge of M80's endpoint-sharing graph `Lambda_n` remains
**unresolved**.  This report proves a strict analytic reduction for the
accepted M83/M88 obstruction family.  For `n=3k`, odd `k>=3`, put

```text
A_k=(0,k,2k),          B_k=(0,1)(k,2k),
eta_k=bar K(B_k,.)-bar K(A_k,.).
```

The proved advance is:

1. an exact stationary posterior-score representation of `eta_k bar K`;
2. exact cancellation of the common middle-component schema block;
3. an exact two-channel measure-valued Abel transform whose scalar weights
   are conditioned-Borel split differences; and
4. reduction of `TV(eta_k bar K)=O(k^-2)` to one standalone explicit positive
   summation inequality `(BA2)` below.

This is a reduction, not an `O(k^-2)` proof or a counterexample.  It proves no
H0 gap, fixed-endpoint bridge gap, identity heat-bath gap, global mixing
claim, or Terminal conclusion.

## 2. Full proved argument

### 2.1 Posterior score with the balanced orbit stabilizer retained

For a supported raw product `g`, write

```text
A_g=F_(n-3)(g^-1h),       C(g,s)=F_(n-5)((gs)^-1h).
```

Let `O_g` be its cyclic orbit, `o_g=|O_g|`, and `a(g)=3` for an oriented
triangle or `2` for a noncrossing double.  M73's accepted formulas are

```text
bar pi(O_g)=o_g a(g)A_g/n^(n-2),
bar K(O_g,O_s)=a(s)A_g^-1 sum_(s' in O_s)C(g,s').      (2.1)
```

Define `f_k=eta_k/bar pi`.  Reversibility and `(2.1)` give, exactly,

```text
f_k(O_s)
 =bar K(O_s,O_B)/bar pi(O_B)-bar K(O_s,O_A)/bar pi(O_A)

 =n^(n-3)/A_s sum_(r=0)^(n-1)
    {C(s,theta^r B)/A_B-C(s,theta^r A)/A_A},           (2.2)

(eta_k bar K)(O_t)=bar pi(O_t)(bar K f_k)(O_t),
TV(eta_k bar K)=1/2 E_barpi |bar K f_k|.               (2.3)
```

The all-`n` phase sum in `(2.2)` is literal.  The balanced `A_k` orbit has
size `k`, so it repeats each orbit member exactly three times; this repetition
cancels its quotient orbit factor.  The ordered-lift factors also cancel only
after using literal orbit masses.  Thus neither the balanced stabilizer nor
the `3` versus `2` lift multiplicity is suppressed.

### 2.2 The common residual component cancels exactly

The residual cycles are

```text
A_k^-1h: C_-=(0,...,k-1), M=(k,...,2k-1),
          C_+=(2k,...,3k-1);

B_k^-1h: {0}, L=(1,...,k-1,2k,...,3k-1),
          M=(k,...,2k-1).                              (2.4)
```

Put `m=k-1`, `R=3m`, and `D=R(R-1)`.  Let `J` count how many of the first
two **ordered** completion factors use the exterior rank `2m` rather than
the common middle rank `m`.  The following are actual conditional-color
probabilities, not unnormalized schema coefficients:

```text
alpha_0=m(m-1)/D,
alpha_1=4m^2/D,
alpha_2=2m(2m-1)/D.                                  (2.5)
```

Let `H_(j,A),H_(j,B)` be the normalized quotient product laws conditional on
`J=j`, after summing all raw ordered factors.  For `J=0`, both laws are
literally the first-pair law `mu_M`.  Therefore

```text
eta_k=alpha_1(H_(1,B)-H_(1,A))
     +alpha_2(H_(2,B)-H_(2,A)).                        (2.6)
```

Here `H_1` is one exterior edge times an independent middle edge.  `H_(2,B)`
is the full first-pair law in the merged `(2k-1)`-cycle `L`, while `H_(2,A)`
is the full first-pair law in the two independent `k`-cycles `C_-,C_+` with
uniform color interleaving.  Equation `(2.6)` includes all first-step
`I3,IS,IN,X` schemas; it deletes only the identical `J=0` block.

### 2.3 Conditioned-Borel Abel identity

Let `w_d(s)` be M83's accepted probability of a specified chord with smaller
split `s` in a `d`-cycle.  Define normalized split laws

```text
p_s=(2k-1)w_(2k-1)(s),        1<=s<=k-1,
q_s=k w_k(s),                 1<=s<=(k-1)/2,
q_s=0 otherwise,
D_u=sum_(s<=u)(p_s-q_s).                               (2.7)
```

For `j=1,2`, let `Phi_(j,s)` be `H_(j,B)` conditioned on the merged exterior
first edge having smaller split `s`, and let `Psi_(j,s)` be `H_(j,A)`
conditioned on the separate exterior first edge having split `s`.  Every
`Phi,Psi` is a normalized probability measure on quotient products.  Its
fully explicit ordered-factor completion-count formula is given in
`posterior_cancellation.md`, equations `(4.4a)--(4.4b)`.

Ordinary Abel summation now gives the exact measure identity

```text
H_(j,B)-H_(j,A)
 =sum_(u=1)^(k-2)D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_(s=1)^((k-1)/2)q_s(Phi_(j,s)-Psi_(j,s)).        (2.8)
```

No absolute value occurs in `(2.6)` or `(2.8)`.  The first sum is the scalar
split-gradient part; the second retains the cyclic embedding and conditional
second-factor counterterm that residual sizes alone miss.

The conditioned-Borel formula proves, additionally,

```text
p_s<q_s                              (1<=s<=(k-1)/2),
D_u<0                                (1<=u<=k-2),
max_u |D_u|=Theta(k^-1/2),
sum_(u=1)^(k-2)|D_u|
 ~[(2-sqrt(2))/sqrt(pi)]sqrt(k).                       (2.9)
```

The last identity follows from the accepted smaller-fragment Riemann sum:
the sum of absolute cumulative differences is
`E_p[S]-E_q[S]`, asymptotic to the displayed constant.  Thus the Abel
coefficients themselves still carry the `k^-1/2` boundary scale.  Any proof
must obtain the remaining `k^-3/2` through the complete posterior difference,
not by claiming the Borel tail is smaller.

## 3. Probability, multiplicity, runtime, path, and cancellation accounting

- `bar K` is the exact nonlazy coordinate-correlation kernel for the uniform
  minimal long-cycle bridge.  No identity-bridge or global sampler law is
  substituted.
- The cyclic quotient uses literal orbit masses.  `O_A` has size `k`; all
  ordinary product orbits here have size `n`.  Raw lift multiplicities are
  `a=3` for triangles and `a=2` for doubles.
- The `alpha_j` in `(2.5)` sum to one and arise by sampling two ordered colors
  without replacement from total rank `3(k-1)`.
- Each `Phi,Psi` is a probability kernel.  Raw ordered edges and their
  completion counts are summed first; cyclic quotienting occurs afterward.
- The second row inside every target likelihood contains all four
  `I3,IS,IN,X` schemas.  The square in `(BA2)` and the absolute value in
  total variation occur only after both `j=1,2` channels have been combined.
- No comparison path or congestion argument is used.
- Exact `k=3` and `k=5` Borel--Abel certificates finished on this host in
  under one second and about seventeen seconds of process wall time,
  respectively.  The floating `k=3,5,7` energy suite took about forty seconds.
  All runs are deterministic (`seed=null`) under Python `3.12.3`; floating
  runs use NumPy `1.26.4`.

## 4. Dependencies, with controlling status labels

- **Accepted proved input (M73):** exact raw and quotient product kernels,
  literal stationary orbit masses, quotient reversibility, four residual
  schemas, and conditioned-Borel first-edge formula.
- **Accepted proved input (M80):** the strict endpoint-sharing graph and its
  diameter-four reduction.  M91 uses only the definition of its edges.
- **Accepted proved input (M83/M88):** adjacency of `A_k,B_k`, their residual
  cycles, the far-singleton one-step lower bound, exact split weights, and
  `TV(bar K(A_k,.),bar K(B_k,.))=Omega(k^-1/2)`.
- **Proved here:** posterior score `(2.2)--(2.3)` including the short balanced
  orbit; common-component cancellation `(2.6)`; normalized conditional laws;
  measure-valued Abel identity `(2.8)`; sign, maximum, and total size of its
  Borel cumulative coefficients `(2.9)`; the implication `(BA2)=>(5.1)`
  below; and a weighted-Fisher sufficient inequality recorded in the proof
  note.
- **Exact finite only:** rational formula audits at `k=3,5`.
- **Floating finite only:** BA2 and weighted-Fisher diagnostics at `k=3,5,7`.
- **Unresolved:** `(BA2)`, the balanced-family `O(k^-2)` TV estimate, the
  general strict-`Lambda_n` edge lemma, and every H0/gap/Terminal consequence.

All frozen manifests for M73, M80, and M83 pass from the repository root.
M88's `SHA256SUMS` passes from its own directory, which is the relative-path
convention encoded in that manifest.  No predecessor artifact was edited.

## 5. First unproved standalone explicit summation inequality

For a target orbit `O_t`, define the complete posterior likelihood

```text
G_t(O_s)=bar K(O_s,O_t)/bar pi(O_t)
 =n^(n-3)/A_s sum_(r=0)^(n-1)C(s,theta^r t)/A_t.
```

Evaluate the right side of `(2.8)` on `G_t`, calling the result
`cal A_(j,k)(t)`.  The exact pointwise identity is

```text
(bar K f_k)(O_t)
 =alpha_1 cal A_(1,k)(t)+alpha_2 cal A_(2,k)(t).       (5.0)
```

The single remaining balanced-family statement is:

> **BALANCED ABEL COLLISION `(BA2)` (unresolved).**  There is an absolute
> constant `C` such that, for every odd `k>=3`,
>
> ```text
> sum_(O_t) bar pi(O_t)
>   [alpha_1 cal A_(1,k)(t)+alpha_2 cal A_(2,k)(t)]^2
> <= C/k^4.                                            (BA2)
> ```

Every term in `(BA2)` is an explicit finite sum of Cayley completion counts,
conditioned-Borel weights, and cyclic phases.  The single square is outside
both merge-defect channels, both Abel sums, all cyclic embeddings, and all
four second-step schemas.  By `(2.3)`, `(5.0)`, and Cauchy--Schwarz, `(BA2)`
would prove

```text
TV(bar K^2(O_A,.),bar K^2(O_B,.))<=sqrt(C)/(2k^2).     (5.1)
```

Equivalently, the left side of `(BA2)` is the localized four-step collision
contrast

```text
bar K^4(B,B)/bar pi(B)+bar K^4(A,A)/bar pi(A)
-bar K^4(A,B)/bar pi(B)-bar K^4(B,A)/bar pi(A).        (5.2)
```

This is not a trace or a fixed-moment heuristic; it is exactly the squared
stationary norm of this one posterior score.

## 6. Strongest self-attack

1. `(BA2)` is stronger than the desired L1 estimate.  Rare target orbits
   could make it false even if `TV(eta_k bar K)=O(k^-2)` is true.  The exact
   direct-L1 version of `(5.0)` is the appropriate fallback if that occurs.
2. Abel summation is an identity, not a bound.  Equation `(2.9)` proves that
   its largest coefficient is still `Theta(k^-1/2)` and its total variation
   weight is `Theta(sqrt(k))`; the central smoothing estimate remains real.
3. The embedding terms `Phi-Psi` cannot be dropped.  Doing so would repeat
   the residual-size-lumping error refuted in M73.
4. The `j=1` and `j=2` channels cannot be triangle-bounded separately.
   Exact finite data show their post-`K` triangle sum already exceeds the
   complete signed answer.
5. The reduction exploits the special balanced geometry, namely an identical
   middle `k`-cycle and a merge of the two exterior cycles after deleting
   vertex `0`.  It does not prove the general strict-edge lemma.
6. Conditioning on `J` is not an orthogonal/Efron--Stein decomposition after
   the second kernel.  The exact stationary inner product between the
   `J=1` and `J=2` merge-defect images is strictly positive already at
   `k=3` and `k=5`; hence no proof may delete their cross term as zero.

## 7. Exact and finite falsification attempts

`balanced_abel_audit.py` reconstructs each complete quotient row directly
from ordered factors and exact completion counts.  At both `k=3` and `k=5`
it verifies:

- exact residual components and source orbit sizes;
- exact `alpha_0,alpha_1,alpha_2` normalization;
- exact reconstruction of both full rows;
- exact common `J=0` cancellation;
- exact `p,q` conditioned-Borel split laws;
- exact normalized `Phi,Psi` measures;
- both measure-valued Abel identities;
- equality after applying the full second kernel.

It reproduces

```text
k=3: TV(eta)=3196/5625,
     TV(eta K)=27708771860129/306307575000000;

k=5: TV(eta)=913205594792/2466218390625,
     exact two-step fraction stored in balanced_abel_exact_k5.json.
```

The independent posterior-score audit verifies `(2.2)--(2.3)` exactly at
`k=3` and in floating arithmetic at `k=5,7`.  Finite diagnostics are:

| `k` | `n` | quotient states | `k^2 TV(eta K)` | `k^4 E[(Kf)^2]` | `k^4` weighted-Fisher bound |
|---:|---:|---:|---:|---:|---:|
| 3 | 9 | 38 | 0.8141 | 5.2302 | 7.9188 |
| 5 | 15 | 213 | 0.6261 | 3.5773 | 13.9029 |
| 7 | 21 | 634 | 0.6222 | 4.2970 | 37.4078 |

The fourth column agrees with M83's two-step values.  The fifth merely fails
to falsify `(BA2)`.  The growing finite inflation in the last column warns
that applying Cauchy--Schwarz separately to Abel gradients is too lossy; it is
not an asymptotic refutation of that sufficient route.

The exact `k=3,5` certificates also compute the stationary L2 cross term of
the two complete merge-defect channels and find it strictly positive.  The
corresponding floating channel correlations at `k=3,5,7` are
`0.7370,0.7241,0.7495`.  This exactly refutes a universal orthogonality
shortcut at the first family member; it does not refute `(BA2)`, because the
smallness there comes from signed structure within the channel images.

Boundary cases: the family begins at `k=3,n=9`; `k=1,n=3` is excluded, and
`k` must be odd because `n` is odd.  Even `k`, `n=7`, identity endpoints,
`m=0,2`, and `N=2` are outside this family and no claim is made about them.

## 8. Artifacts, exact commands, hashes, and hygiene

Owned artifacts:

- `plan.md`, `checkpoint.md`, `posterior_cancellation.md`, `report.md`;
- `posterior_score_audit.py`, `posterior_score_exact_n9.json`,
  `posterior_score_float_n15.json`, `posterior_score_float_n21.json`;
- `balanced_abel_audit.py`, `balanced_abel_exact_k3.json`,
  `balanced_abel_exact_k5.json`;
- `abel_energy_diagnostic.py`, `abel_energy_k7.json`;
- `SHA256SUMS`.

Representative commands from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/posterior_score_audit.py --n 9 --exact --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/posterior_score_exact_n9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/posterior_score_audit.py --n 15 21 --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/posterior_score_float_n21.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/balanced_abel_audit.py --k 3 --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/balanced_abel_exact_k3.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/balanced_abel_audit.py --k 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/balanced_abel_exact_k5.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/abel_energy_diagnostic.py --k 3 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation/abel_energy_k7.json
```

All computations are deterministic.  JSON artifacts distinguish exact
rationals from floating diagnostics and state that finite values are not
asymptotic evidence.  `SHA256SUMS` freezes every owned artifact other than the
manifest itself.  No package was installed, no network or random input was
used, and no predecessor or coordinator file was changed.  Generated Python
cache is absent at freeze time.

## 9. Verdict

**STRICT BALANCED-FAMILY REDUCTION; GENERAL TWO-STEP LEMMA UNRESOLVED.**

The accepted `Omega(k^-1/2)` one-step obstruction is now localized exactly:
the common middle-component block cancels, and the rest is a two-channel
merge defect governed by one conditioned-Borel cumulative sequence.  The
absolute value remains outside the complete signed posterior.  The remaining
balanced obligation is the standalone collision inequality `(BA2)`, with all
weights and cyclic multiplicities explicit.  This is substantive proof
progress, but it does not prove `O(k^-2)`, the full strict-`Lambda_n` edge
bound, an H0 gap, or any Terminal claim.
