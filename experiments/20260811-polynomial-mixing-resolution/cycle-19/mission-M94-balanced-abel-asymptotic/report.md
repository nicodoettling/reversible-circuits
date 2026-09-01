# M94 report: central-double obstruction to balanced `(BA2)`

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, convention, scope, and status

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Fix `n=3k`, with odd `k>=3`, and

```text
h=(0 1 ... n-1),
A_k=(0,k,2k),       B_k=(0,1)(k,2k).
```

The target is uniform on minimal length-`n-1` transposition factorizations
of `h`.  `bar K` is M73's nonlazy rank-two pair-product kernel modulo cyclic
conjugation by `h`; it is not the identity-word heat-bath kernel.

M91's balanced collision inequality

```text
(BA2)_k=||bar K(eta_k/bar pi)||_(2,bar pi)^2=O(k^-4),
eta_k=bar K(B_k,.)-bar K(A_k,.),
```

remains **unresolved**, but this report produces a sharply targeted
obstruction.  It proves:

1. an exact signed Borel-convolution formula for the complete two-step score;
2. sharp bulk and boundary asymptotics for M91's Abel coefficients;
3. an invariant central-double event `E_k` with exact stationary mass and
   `bar pi(E_k)=Theta(k^-1)`; and
4. the implication

```text
liminf k^2 |bar K^2(B_k,E_k)-bar K^2(A_k,E_k)|>0
   => (BA2)_k=Omega(k^-3),                            (1.1)
```

which would refute `(BA2)` but is compatible with direct signed
`L1=O(k^-2)`.

The scalar premise in `(1.1)`, called `(BD)` below, is **unresolved**.
No `(BA2)` refutation, direct L1 upper bound, general strict-edge estimate,
H0 gap, bridge gap, identity heat-bath gap, or Terminal conclusion is claimed.

## 2. Exact target-residual/Borel convolution

Put

```text
b_d=e^-d d^(d-1)/d!,
beta_3(x)=product_(C cycle of x^-1 h)b_|C|,
beta_5(x,y)=1[ell_T((xy)^-1h)=n-5]
              product_(C cycle of (xy)^-1h)b_|C|,
R_n=(n-3)(n-4),
c_n=(n-3)!e^n/n^(n-2).
```

Singleton cycles are included.  M73's exact completion counts become

```text
pi(x)=a(x)c_n beta_3(x),
K(x,y)=a(y)/R_n * beta_5(x,y)/beta_3(x),              (2.1)
```

where `a=3` for triangles and `a=2` for doubles.

Define the complete signed first-row defect

```text
d_k(s)=beta_5(B_k,s)/beta_3(B_k)
       -beta_5(A_k,s)/beta_3(A_k).                    (2.2)
```

For a target orbit `O_t`, let

```text
Q_t(s)=|O_t|^-1 sum_(t' in O_t)beta_5(s,t').          (2.3)
```

Directly expanding the intermediate quotient orbit gives the proved exact
posterior score

```text
z_k(O_t):=[bar K^2(O_B,O_t)-bar K^2(O_A,O_t)]/bar pi(O_t)

=1/[c_n R_n^2 beta_3(t)]
  sum_(s in X_n)a(s)d_k(s)Q_t(s)/beta_3(s).           (2.4)
```

The factor `|O_t|` in `(2.3)` retains every cyclic stabilizer, including the
size-`k` orbit of `A_k`.  Every triangle/double micro-lift remains in `a`.
The quotient and raw norms agree because `z_k` is orbit-invariant:

```text
(BA2)_k=E_pi[z_k^2],       2 TV=E_pi|z_k|.            (2.5)
```

For any invariant raw target event `E`, the target sum collapses exactly to

```text
Delta_k(E):=bar K^2(O_B,E)-bar K^2(O_A,E)

=1/R_n^2 sum_s a(s)d_k(s)/beta_3(s)
        sum_(t in E)a(t)beta_5(s,t).                  (2.6)
```

Equation `(2.6)` retains both M91 channels and all second-row schemas before
any estimate.  It is not a channelwise triangle bound.

## 3. Proved Abel and central-event asymptotics

For M91's split laws `p_s,q_s` and cumulative difference
`D_u=sum_(s<=u)(p_s-q_s)`, define

```text
P(x)=(2 pi)^(-1/2)x^(-3/2)(1-x/2)^(-3/2),
Q(x)=(2 pi)^(-1/2)x^(-3/2)(1-x)^(-3/2)1[x<1/2],
mathcal D(x)=integral_0^x(P-Q).
```

Uniform Stirling bounds and a boundary/bulk split prove

```text
sqrt(k)D_floor(kx) -> mathcal D(x)     (0<x<1, x!=1/2),

D_u ~ -3/[2 sqrt(2 pi)] sqrt(u)/k
                    (u->infinity, u=o(k)).            (3.1)
```

Thus the Abel weights genuinely retain a `k^-1/2` bulk scale.

Let `r_k=(k+1)/2`, and let `E_k` be the double-target orbits whose four
positive cyclic support gaps `(x,y,z,w)` all satisfy `>=r_k`.  This is
well-defined under all four colored encodings.  Its exact mass is

```text
bar pi(E_k)=n(n-3)!/n^(n-2)
 sum_[x+y+z+w=n; x,y,z,w>=r_k]
      tau(x)tau(z)tau(y+w),                           (3.2)
```

with `tau(d)=d^(d-1)/d!`.  A three-dimensional uniform Stirling/Riemann
calculation proves

```text
k bar pi(E_k) -> I/(6 pi),                            (3.3)

I=integral_[x,y,z,w>=1/6; x+y+z+w=1]
      [x z (y+w)]^(-3/2) dx dy dz,
```

where `0<I<infinity`.  Hence `bar pi(E_k)=Theta(k^-1)`.

## 4. Probability, multiplicity, runtime, and cancellation accounting

- `bar K` is the exact nonlazy quotient correlation kernel for the uniform
  minimal long-cycle bridge.
- All exact formulas use literal raw lift multiplicity and distinct cyclic
  orbit size.  No generic size-`n` substitution is made for `O_A`.
- The Borel rewrite is an algebraic identity:
  `F_r(q)=r!e^n product_C b_|C|` when the cycle sizes sum to `n`.
- `E_k` is invariant, so its four colored double-composition encodings are
  divided out exactly in `(3.2)`.
- The square in `(BA2)` and absolute value in TV occur after the complete
  signed convolution `(2.4)`; the `J=1,2` channels are never bounded
  separately.
- Exact `k=3,5` checks use Python `Fraction`; floating `k<=11` checks use
  NumPy `1.26.4`.  All are deterministic (`seed=null`) under Python
  `3.12.3`.

## 5. Dependencies and status labels

- **Accepted proved input (M73/M80):** raw and quotient rank-two kernels,
  orbit masses, reversibility, cyclic composition parameterization, and the
  `I3,IS,IN,X` row schemas.
- **Accepted proved input (M83/M88):** the balanced strict edge, its residual
  cycles, and conditioned-Borel split law.
- **Accepted proved input (M91/M93):** posterior score, common `J=0`
  cancellation, normalized `J=1,2` laws, the measure-valued Abel identity,
  and equivalence of `(BA2)` to the localized stationary L2 contrast.
- **Proved here:** `(2.4)--(2.6)`, Abel scaling `(3.1)`, exact event mass
  `(3.2)`, the positive finite limit `(3.3)`, stationary Cauchy obstruction
  `(1.1)`, the exact L1 shell decomposition below, and the uniform stationary
  shell envelope `bar pi(S_d)<=C d^(-3/2)`.
- **Exact finite only:** central-event formulas and Cauchy lower bound at
  `k=3,5`.
- **Floating finite only:** shell, channel, and event values through `k=11`.
- **Unresolved:** `(BD)`, `(BA2)`, the balanced direct L1 upper bound, the
  general strict edge, H0, and all sampler-gap/Terminal consequences.

No external literature theorem is added by this mission.

## 6. First unproved standalone obligations

The sharp refutation target is now one scalar:

> **CENTRAL DOUBLE BULK DEFECT `(BD)` (unresolved).**  There is an absolute
> `c>0` such that for all sufficiently large odd `k`,
>
> ```text
> |Delta_k(E_k)|>=c/k^2.                              (BD)
> ```

Stationary Cauchy--Schwarz gives, exactly,

```text
(BA2)_k >= Delta_k(E_k)^2/bar pi(E_k).                (6.1)
```

Together with `(3.3)`, `(BD)` proves `(BA2)_k=Omega(k^-3)` and therefore
refutes `(BA2)`.  Yet TV only satisfies `TV>=|Delta_k(E_k)|=Omega(k^-2)`,
so direct `O(k^-2)` remains possible.

M91's Abel identity sharpens `(BD)` without channel splitting.  Write the
complete event defect as

```text
Delta_k(E_k)=Gradient_k+Embedding_k,                  (6.2)
```

where both terms already combine `alpha_1` and `alpha_2`; `Gradient_k` is
the sum with coefficients `D_u`, and `Embedding_k` is the sum with
coefficients `q_s`.  A sufficient next proof is

```text
liminf k^2 Embedding_k > limsup k^2 |Gradient_k|.     (6.3)
```

Finite values at `k=5,7,9` are respectively

```text
k^2 Embedding_k:   0.05583,  0.05149,  0.04876,
k^2 Gradient_k:   -0.00874, -0.00829, -0.00659.
```

Every finite embedding split is positive in these checks, while gradient
splits have both signs.  This only identifies the proof interface; it does
not establish `(6.3)` asymptotically.

For the weaker direct L1 route, let `S_d` be the target shell with minimum
residual cycle size `d`, and let `z_k` be `(2.4)`.  The exact partition is

```text
2 TV=sum_(d=1)^k bar pi(S_d)E[|z_k| | S_d].           (6.4)
```

A falsifiable sufficient boundary-plus-bulk envelope is

```text
bar pi(S_d)E[|z_k| | S_d]
 <=C/k^2 [d^(-3/2)+(kd)^(-1/2)].                     (L1-envelope)
```

Both terms sum uniformly in `d`; this would prove direct `O(k^-2)`.  It is
unresolved.

## 7. Exact and finite falsification attempts

The exact central-event certificate gives:

| `k` | `k pi(E_k)` | `k^2 Delta_k(E_k)` | `k^4` event L2 | `k^4 Delta(E)^2/pi(E)` |
|---:|---:|---:|---:|---:|
| 3 | 0.074853 | 0.064391 | 0.174096 | 0.166175 |
| 5 | 0.074341 | 0.047084 | 0.187228 | 0.149106 |

Floating complete-kernel checks extend the first two columns:

| `k` | `k pi(E_k)` | `k^2 Delta_k(E_k)` | `k^4` event L2 | `k^4 Delta(E)^2/pi(E)` | `k^4 BA2` | `k^2 TV` |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 0.073149 | 0.043206 | 0.250573 | 0.178640 | 4.29699 | 0.62220 |
| 9 | 0.072240 | 0.042166 | 0.335286 | 0.221504 | 5.99740 | 0.68570 |
| 11 | 0.071572 | 0.042040 | 0.436481 | 0.271624 | 8.71656 | 0.80544 |

The `k=11` row is a deterministic complete-kernel floating computation over
2,646 quotient targets, not an exact rational certificate and not an
asymptotic theorem.  Its unscaled event values are
`pi(E_11)=0.006506561654677261` and
`Delta_11(E_11)=0.0003474359034435877`.

At `k=9`, the `k^4 BA2` contributions by minimum residual size are

```text
0.642,0.533,0.661,0.792,0.892,0.945,0.859,0.570,0.103.
```

Double targets contribute `4.5794` and triangles `1.4180`.  This distributed
bulk profile argues against a few rare outliers, but finite growth cannot
refute an asymptotic bound.  The exact event reduction is what makes the
signal falsifiable.

Strongest self-attack: `(BD)` could still fail through cancellation among
intermediate shells.  At a central `k=7` target, the minimum-one double
intermediate shell is negative while several subsequent shells are positive.
No uniform sign, limiting integral, or tail domination is proved.  Thus the
finite table is not promoted to an asymptotic obstruction.

Boundary scope: the family begins at `k=3,n=9`; `k=1`, even `k`, other odd
`n`, identity endpoints, `m=0,2`, and `N=2` are outside it.

## 8. Artifacts, commands, hashes, and hygiene

Owned proof artifacts are `plan.md`, `checkpoint.md`,
`bulk_obstruction.md`, and this report.  Reproducible scripts and compact raw
outputs are listed in the final `SHA256SUMS`.

Representative commands from the repository root are

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_exact.py --k 3 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_exact_k5.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/rare_orbit_diagnostic.py --k 3 5 7 9 --top 40 --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/rare_orbit_k9.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_channels.py --k 5 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_channels_splits_k7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/rare_orbit_diagnostic.py --k 11 --top 20 --include-all --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/all_target_scores_k11.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/compact_bulk_summary.py experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/all_target_scores_k5.json experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/all_target_scores_k7.json experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/all_target_scores_k9.json experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/all_target_scores_k11.json --output experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_float_k11.json
```

No package, network access, random input, commit, push, predecessor file,
coordinator file, manuscript, or skill was changed.  Redundant large finite
outputs and generated caches are removed before freeze.  The manifest freezes
every retained owned artifact except itself.  A final exact `k=3,5` rerun in
`/tmp` matched the retained rational result payload; all retained JSON parsed
and all owned Python files passed `ast.parse`.

## 9. Verdict

**STRICT OBSTRUCTION REDUCTION; `(BA2)` AND DIRECT L1 BOTH UNRESOLVED.**

The balanced collision route is now under a concrete asymptotic threat.  A
positive-mass central double region is proved to have mass `Theta(k^-1)`;
the finite rows are consistent with average score `Theta(k^-1)`, hence with
an `L2` contribution of order `k^-3` but an L1 contribution of order
`k^-2`.  That score scaling is not proved.  The signed scalar defect is
isolated exactly and strongly supported by finite checks, but `(BD)` remains
open, so `(BA2)` is **not asymptotically refuted**.  The highest-value next
step is `(6.3)`, equivalently `(BD)`.  Only if it succeeds should `(BA2)` be
declared refuted and the project continue on the direct signed-L1 envelope.
