# M93 fresh referee report on frozen M91

Date: 2026-08-12.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, exact accepted claim, and scope

```text
ACCEPT M91's strict balanced-family reduction.
Material numbered objections: none.
```

The accepted result is only the following reduction for M73's cyclic
rank-two quotient correlation kernel.  Let `n=3k`, with odd `k>=3`, and

```text
A_k=(0,k,2k),             B_k=(0,1)(k,2k).
```

For the signed first-row difference
`eta=bar K(O_B,.)-bar K(O_A,.)`, M91 correctly proves:

1. the exact stationary posterior-score formula, with the size-`k` orbit of
   `A` and all ordered-pair lift multiplicities retained;
2. exact cancellation of the common `J=0` middle-component block;
3. exact normalized `J=1,2` conditional laws and their measure-valued
   conditioned-Borel Abel transform; and
4. equivalence of the remaining balanced `L2` obligation `(BA2)` to the
   localized, correctly denominated four-step contrast.

This accepts a **reduction only**.  `(BA2)` is unresolved.  So are the
balanced `O(k^-2)` two-step TV estimate, the general strict-`Lambda_n` edge
bound, an H0 gap, any fixed-endpoint or identity-bridge gap, polynomial mixing
of the lazy `{3,4,5}` heat-bath chain, and Terminal A/B.

## 2. Frozen provenance and package integrity

The assigned digests independently match:

| frozen M91 artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `df2983ca83c8fd92dec6406eb6341b4f07655304c491a7c74687649ceaa609ea` | match |
| `SHA256SUMS` | `0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703` | match |

Running `sha256sum -c SHA256SUMS` inside M91's directory returned `OK` for
all thirteen entries.  The frozen directory contained no `__pycache__` or
`.pyc` file.  No frozen M91, predecessor, coordinator, manuscript, skill, or
shared project file was edited.

## 3. Target, convention, kernel, and dependencies

Permutations compose as

```text
(pq)(x)=p(q(x)),
```

and displayed tuple factors multiply left-to-right.  The target here is
uniform on minimal length-`n-1` transposition factorizations of
`h=(0 1 ... n-1)`.  `bar K` is the nonlazy pair-product coordinate kernel
after quotienting by `theta(g)=h^-1 g h`.  It is not the global identity-word
law and not the lazy `{3,4,5}` heat-bath kernel.

For a supported raw rank-two product `g`, define

```text
A_g=F_(n-3)(g^-1 h),
C(g,s)=F_(n-5)((gs)^-1 h),
```

let `o_g=|O_g|`, and let `a(g)` be `3` for an oriented triangle and `2` for
a double.  The audited accepted M73 interface is

```text
bar pi(O_g)=o_g a(g) A_g/n^(n-2),
bar K(O_g,O_s)=a(s)/A_g sum_(s' in O_s) C(g,s').
```

M91 also uses accepted M83/M88 facts: `A_k,B_k` are strict neighbors, their
residual component sizes are `(k,k,k)` and `(1,k,2k-1)`, and the specified
chord split law is conditioned Borel.  No new external literature result is
invoked.  The finite checker below reconstructs these kernel interfaces
without importing M73, M83, or M91 code.

## 4. Posterior score, quotient stabilizer, and color cancellation audit

### 4.1 Orbit and lift factors — accepted

Detailed balance gives

```text
f(O_s):=eta(O_s)/bar pi(O_s)
 =bar K(O_s,O_B)/bar pi(O_B)
  -bar K(O_s,O_A)/bar pi(O_A).
```

For a general source orbit `O_g`, direct substitution gives

```text
bar K(O_s,O_g)/bar pi(O_g)
 =n^(n-2)/(o_g A_s A_g) sum_(g' in O_g)C(s,g').
```

The all-`n` phase sum visits each orbit member `n/o_g` times, hence

```text
(1/o_g)sum_(g' in O_g)C(s,g')
 =(1/n)sum_(r=0)^(n-1)C(s,theta^r g).
```

This proves M91's factor `n^(n-3)`.  In particular `o_A=k`, while `o_B=n`;
the three visits to each member of `O_A` are the stabilizer correction, not
an extra factor to remove.  The factors `a(g)` cancel only against the
literal stationary orbit mass after the target-orbit sum is kept.  The fresh
exact reconstruction verifies this identity at every quotient state for
`k=3,5`.

Finally, reversibility yields

```text
(eta bar K)(O_t)=bar pi(O_t)(bar K f)(O_t),
TV(eta bar K)=1/2 E_barpi |bar K f|.
```

The row/function orientations and stationary factor are correct.

### 4.2 `J=0` cancellation and `alpha` coefficients — accepted

Put `m=k-1`, `R=3m`, and `D=R(R-1)`.  The residual ranks are `(m,m,m)` on
the A side and `(2m,m,0)` on the B side.  Sampling the first two ordered
component colors without replacement gives

```text
alpha_0=m(m-1)/D,
alpha_1=4m^2/D,
alpha_2=2m(2m-1)/D.
```

These sum to one.  Conditional on `J=0`, both sources take their first two
factors from the same literal middle `k`-cycle, so both conditional product
laws are exactly `mu_M`.  Therefore only that identical block cancels:

```text
eta=alpha_1(H_(1,B)-H_(1,A))
   +alpha_2(H_(2,B)-H_(2,A)).
```

For `J=1`, the two color orders are already in `alpha_1`; exterior and
middle factors commute because their supports are disjoint.  For `J=2`, the
A-side law is the full ordered first-pair law of the two independent exterior
cycles, including same-color and different-color possibilities.  Thus no
schema, color order, or target micro-lift is discarded.

## 5. Conditional laws, Borel sign, and Abel identity audit

The explicit completion-count law

```text
N_Q(e,f)=F_(r(Q)-2)((ef)^-1Q)/F_(r(Q))(Q)
```

is the probability of the literal ordered prefix `(e,f)`.  Summing it before
passing `ef` to a cyclic product orbit retains all three ordered lifts of an
oriented triangle and both ordered lifts of a double.  On the two equal A
exterior components, the apparent missing `1/2` in M91's `Psi_(2,s)` formula
is already present in `N_(C_-C_+)`: the first factor lands in either rank-`m`
component with probability `1/2`.  Every displayed `Phi_(j,s)` and
`Psi_(j,s)` therefore has total mass one.

For an odd `d`-cycle, each smaller split `s<d/2` has exactly `d` chords, so

```text
p_s=(2k-1)w_(2k-1)(s),       1<=s<=k-1,
q_s=k w_k(s),                1<=s<=(k-1)/2
```

are normalized probability laws.  With `b_j=e^-j tau(j)` and
`r_j=b_(j-1)/b_j=e(1-1/j)^(j-2)`, `r_j` is strictly decreasing.  On common
support the likelihood ratio is

```text
p_s/q_s=(2k-1)/(2k)
  product_(i=0)^(s-1) r_(2k-1-i)/r_(k-i) <1.
```

Thus the sign `p_s<q_s` is correct.  With
`D_u=sum_(s<=u)(p_s-q_s)`, one has `D_0=D_(k-1)=0`, and summation by parts
gives, without an endpoint remainder,

```text
H_(j,B)-H_(j,A)
 =sum_(u=1)^(k-2)D_u(Phi_(j,u)-Phi_(j,u+1))
  +sum_s q_s(Phi_(j,s)-Psi_(j,s)).
```

The cumulative sequence is strictly negative through `u=k-2`; its largest
absolute value is the long-cycle tail beyond the support of `q`, hence
`Theta(k^-1/2)`.  Since `-sum_u D_u=E_p[S]-E_q[S]`, the accepted M83
smaller-fragment asymptotic gives M91's
`[(2-sqrt(2))/sqrt(pi)]sqrt(k)` total coefficient.  This is an exact
identity plus an accepted asymptotic input, not a smoothing bound.

## 6. `(BA2)`, stationary norm, and four-step denominators audit

Put `q_g(s)=1[s=g]/bar pi(g)`.  Reversibility gives

```text
f=bar K(q_B-q_A),
bar K f=bar K^2(q_B-q_A).
```

Self-adjointness then gives exactly

```text
||bar K f||_(2,bar pi)^2
 =<q_B-q_A,bar K^4(q_B-q_A)>_(bar pi)

 =bar K^4(B,B)/bar pi(B)+bar K^4(A,A)/bar pi(A)
  -bar K^4(A,B)/bar pi(B)-bar K^4(B,A)/bar pi(A).
```

The cross denominators are not interchangeable by inspection; they are
exactly as displayed.  Detailed balance makes their numerical contributions
equal.  The independent checker separately constructs all four `K^4`
entries from two-step rows and verifies that this denominated contrast equals

```text
sum_t (bar K^2(B,t)-bar K^2(A,t))^2/bar pi(t)
 =E_barpi[(bar K f)^2].
```

Consequently `(BA2) <= C/k^4` would imply
`TV(bar K^2(B,.),bar K^2(A,.))<=sqrt(C)/(2k^2)` by one stationary
Cauchy--Schwarz inequality.  Neither the audit nor M91 proves `(BA2)`.

The exact stationary inner product between the complete `J=1` and `J=2`
post-`K` channel images is strictly positive at both checked family members.
This refutes a universal orthogonality shortcut.  It does not refute `(BA2)`
or justify bounding the two channels separately.

## 7. Fresh exact certificates and falsification results

`independent_exact_audit.py` was written from scratch with only the Python
standard library and imports no M91 or predecessor implementation.  It
enumerates literal ordered transposition pairs, reconstructs the raw kernel
and cyclic quotient over `Fraction`, decomposes both residual pair laws by
`J`, conditions on the actual exterior split, performs Abel summation, and
checks the posterior phase formula, second row, stationary norm, and four-step
contrast.

| exact quantity | `k=3` | `k=5` |
|---|---:|---:|
| `n` | 9 | 15 |
| quotient states | 38 | 213 |
| source orbit sizes `(A,B)` | `(3,9)` | `(5,15)` |
| `alpha_0,alpha_1,alpha_2` | `(1/15,8/15,2/5)` | `(1/11,16/33,14/33)` |
| `TV(eta)` | `3196/5625` | `913205594792/2466218390625` |
| `TV(eta K)` | `27708771860129/306307575000000` | exact fraction in `independent_exact_k5.json` |
| channel cross inner product | strictly positive | strictly positive |

At `k=3`, positive completion products exhibit `3` A-side triangles and
`27` A-side doubles, and `11` B-side triangles and `40` B-side doubles.  At
`k=5`, the corresponding counts are `(30,330)` and `(94,622)`.  Every one
has exactly three or two literal ordered micro-lifts respectively.

For both `k`, every following check is exact: row normalization, stationary
detailed balance, source orbit size, full row reconstruction, common `J=0`
cancellation, conditioned split normalization, Borel weights and sign, both
Abel channel identities, the all-`n` posterior phase formula, the post-`K`
identity, the `K^4` contrast, and the positive channel cross term.  The fresh
values match all corresponding fields in M91's frozen exact JSON files.  A
separate execution of M91's frozen `balanced_abel_audit.py --k 3 5` also
completed and reproduced both certificates.

These finite results can falsify the formulas and the orthogonality claim;
they cannot prove `(BA2)` or any asymptotic rate.

## 8. Strongest self-attack, boundaries, artifacts, and hygiene

The strongest remaining attack is substantive rather than clerical: Abel
summation is only a re-expression, its total coefficient weight grows as
`Theta(sqrt(k))`, and the embedding defects `Phi-Psi` remain uncontrolled.
Moreover `(BA2)` is stronger than the desired `L1` estimate and could fail on
rare target orbits even if the balanced TV estimate holds.  Neither finite
bounded scaled energy nor the positive cross term settles that question.

Boundary scope is explicit.  The family starts at `k=3,n=9`; `k=1,n=3`,
even `k`, `n=7`, identity endpoints, `m=0,2`, and `N=2` are outside it.
No assertion about them is inferred.

Owned artifacts are `plan.md`, `checkpoint.md`,
`independent_exact_audit.py`, `independent_exact_k5.json`, this `report.md`,
and the final `SHA256SUMS`.  The principal fresh command, run from the
repository root, was

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M93-m91-fresh-referee/independent_exact_audit.py --k 3 5 --frozen-directory experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M91-h0-two-step-cancellation --output experiments/20260811-polynomial-mixing-resolution/cycle-18/mission-M93-m91-fresh-referee/independent_exact_k5.json
```

The run is deterministic (`seed=null`) under Python `3.12.3`; no package,
network access, or random input was used.  Generated Python cache is removed
before freeze.  `SHA256SUMS` freezes every owned artifact other than the
manifest itself.

## 9. Final verdict and first unproved obligation

**ACCEPT, with zero material numbered objections.**

M91 correctly localizes the accepted balanced one-step obstruction to a
signed two-channel posterior defect and isolates one narrower falsifiable
positive inequality.  The first unproved obligation is exactly `(BA2)`, or a
weaker direct signed-`L1` estimate proving the same balanced `O(k^-2)` row
contraction.  Until one of those is proved, the general H0 two-step lemma, an
H0 gap, the local heat-bath gap, and both Terminals remain **unresolved**.

