# M100 fresh referee report on frozen M94

Date: 2026-08-12.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Decision, exact accepted claim, and scope

```text
ACCEPT M94's strict central-double obstruction reduction.
Material numbered objections: none.
```

For `n=3k`, odd `k>=3`, put

```text
h=(0 1 ... n-1),
A_k=(0,k,2k),                 B_k=(0,1)(k,2k).
```

The accepted result concerns the uniform law on minimal length-`n-1`
transposition factorizations of `h` and M73's nonlazy rank-two pair-product
kernel `bar K` modulo conjugation by `h`.  It correctly proves:

1. the exact orbit-aware Borel convolution for the signed two-step score;
2. the fixed-bulk and `1<<u<<k` boundary asymptotics of the conditioned-Borel
   Abel coefficients;
3. the exact mass and `Theta(k^-1)` asymptotic of the invariant central-double
   event `E_k`;
4. the conditional implication
   `|Delta_k(E_k)|=Omega(k^-2) => (BA2)_k=Omega(k^-3)`; and
5. the exact shell decomposition and uniform stationary shell-mass envelope
   used to formulate a separate direct-L1 obligation.

This accepts a **strict obstruction reduction**, not its unresolved premise.
`(BD)`, `(BA2)`, direct signed `L1=O(k^-2)`, the general strict-edge lemma,
H0, every fixed-endpoint or identity-bridge gap, polynomial mixing of the
lazy `{3,4,5}` identity heat-bath chain, and both Terminals remain unresolved.

## 2. Frozen provenance and package integrity

The assigned digests independently match:

| frozen M94 artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `eeceb389e145b094ab29c1be76f8f5e27078c93604e4ba4d051f436c4644338b` |
| `bulk_obstruction.md` | `2e86f0e3cb6c4449c16e83d16535f679deb1ed105c952c8d25aaee26556569be` |
| `bulk_event_float_k11.json` | `4d1ce5eae2314b03e2e668d81a63487c424e497144db5cc72e61edb78aacd373` |
| `SHA256SUMS` | `47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562` |

Running `sha256sum -c SHA256SUMS` inside M94's directory returned `OK` for
all thirteen entries.  No M94, predecessor, coordinator, manuscript, skill,
or shared project file was edited by this referee.

## 3. Target, convention, kernel, and dependencies

Permutations compose as

```text
(pq)(x)=p(q(x)),
```

and displayed tuple factors multiply left-to-right.  The target and kernel
are exactly the minimal-long-cycle bridge marginal and its nonlazy quotient
coordinate-correlation kernel.  They are not the global fixed-length identity
law and not the lazy `{3,4,5}` block heat-bath kernel.

The inherited proved inputs are M73's completion-count kernel and cyclic gap
parameterization, M83/M88's balanced strict edge and conditioned-Borel split
law, and M91/M93's two-channel Abel identity and definition of `(BA2)`.  M94
does not invoke a new literature theorem or the still-conditional identity
Hurwitz classification.

## 4. Raw kernel, quotient convolution, and stabilizer audit

Let `tau(d)=d^(d-1)/d!` and `b_d=e^-d tau(d)`.  If the residual cycle sizes
sum to `n`, then inclusion of singleton cycles gives exactly

```text
F_(n-3)(x^-1 h)=(n-3)! e^n beta_3(x),
F_(n-5)((xy)^-1 h)=(n-5)! e^n beta_5(x,y).
```

Thus, with `R_n=(n-3)(n-4)` and
`c_n=(n-3)!e^n/n^(n-2)`, the audited raw formulas are

```text
pi(x)=a(x)c_n beta_3(x),
K(x,y)=a(y)/R_n * beta_5(x,y)/beta_3(x).
```

The factors `a=3` for an oriented triangle and `a=2` for a double are literal
ordered-pair lift counts; neither can be suppressed.

For a target orbit `O_t`, the second-row likelihood

```text
beta_3(s)^-1 sum_(t' in O_t) beta_5(s,t')
```

is constant on the intermediate orbit of `s`.  Expanding the first quotient
row and only then replacing the intermediate-orbit sum by a raw-state sum
gives M94's formula.  Dividing by

```text
bar pi(O_t)=|O_t|a(t)c_n beta_3(t)
```

produces the average

```text
Q_t(s)=|O_t|^-1 sum_(t' in O_t) beta_5(s,t').
```

This is precisely where the target stabilizer belongs.  In particular the
orbit of `A_k` has size `k`, while the orbit of `B_k` and every double orbit
has size `n`; no generic size-`n` substitution occurs.  Aggregating the score
against raw `pi` is then identical to aggregation against quotient `bar pi`,
because the score is orbit invariant.  The same expansion over an invariant
raw event yields M94's event convolution without a channelwise absolute value.

The fresh exact checker independently verifies all nonzero raw Borel entries,
all quotient row sums, detailed balance, the source orbit sizes, the complete
score convolution for all 38 target orbits at `k=3` and six adversarial target
orbits at `k=5`, and the full event convolution at both values.  It imports no
M94 or predecessor code.

## 5. Abel asymptotics and uniform-error audit

Write

```text
R_D(s)=b_(D-s)/[(1-1/D)b_D].
```

Uniform Stirling expansion gives

```text
log b_j=-1/2 log(2 pi)-3/2 log j-1/(12j)+O(j^-3).
```

Consequently, uniformly for `s=o(D)`, Taylor expansion gives

```text
R_D(s)=1+(1+3s/2)/D+O((1+s^2)/D^2).
```

Taking `D=2k-1` and `D=k` therefore gives

```text
p_s-q_s=-b_s(1+3s/2)/(2k)
        +O(b_s(1+s^2)/k^2).
```

For `u->infinity`, `u=o(k)`, the error sum is
`O(u^(3/2)/k^2)`, whereas the leading sum is `Theta(sqrt(u)/k)`;
their ratio is `O(u/k)=o(1)`.  Since
`sum_(s<=u)s b_s~2(2 pi)^(-1/2)sqrt(u)`, M94's coefficient
`-3/[2sqrt(2 pi)]` is correct.

For fixed `x` away from `0,1` and the cutoff `1/2`, the same Stirling ratio
gives the displayed densities `P,Q`.  Near zero their leading
`x^-3/2` singularities cancel, leaving `O(x^-1/2)`.  The uniform bound
`|p_s-q_s|<=C b_s(s+1)/k` makes the omitted initial contribution
`O(sqrt(epsilon))` after multiplication by `sqrt(k)`.  Riemann convergence on
the remaining compact interval proves the claimed bulk limit.  Crossing the
single jump at `1/2` causes no problem; M94 excludes equality there.

As a finite falsification check, the fresh script obtains boundary ratios
`1.04845,1.01934,1.00847` at `k=101,401,1601` with `u=floor(sqrt(k))`, and
its scaled bulk cumulatives converge to independent numerical integrals at
`x=.25,.75`.  These values support only the already-audited formulas; they are
not used as proof.

## 6. Central event, Cauchy implication, and shell audit

For odd `n`, a nontrivial rotational stabilizer of a double would induce a
nontrivial odd-order action on two edges; it therefore fixes both edges, and
then their endpoints, which is impossible.  Every double orbit has size `n`.
Each orbit has four colored positive-composition encodings, two separated and
two nested.  The all-gap lower bound is invariant under their cyclic changes.
The separated and nested sums agree after rotation, so dividing the two-color
sum by four gives exactly

```text
bar pi(E_k)=n(n-3)!/n^(n-2)
 sum_[x+y+z+w=n; all >=(k+1)/2] tau(x)tau(z)tau(y+w).
```

The prefactor after extracting `e^n` is asymptotic to `sqrt(2 pi n)`.  Three
Borel factors give `(2 pi)^(-3/2)n^(-9/2)`, and the three-dimensional lattice
sum gives `n^3`.  Hence the mass is `(2 pi n)^-1 I(1+o(1))`; because `n=3k`,
`k bar pi(E_k)->I/(6 pi)`.  The integration domain stays a positive distance
from every singular face, so `0<I<infinity`.  An independent quadrature gives
`I/(6 pi)=0.0677328611`, consistent with but not proved by the finite rows.

Applying stationary Cauchy--Schwarz on this one event gives exactly

```text
(BA2)_k >= Delta_k(E_k)^2/bar pi(E_k).
```

Thus `(BD)` would refute `(BA2)`, but event total variation only gives
`TV>=|Delta_k(E_k)|`; an `Omega(k^-2)` event defect remains compatible with
a direct `O(k^-2)` signed-L1 target.  M94 preserves this distinction.

Finally, for the minimum-residual shell `S_d`, one has `d<=n/3`.  Fixing a
triangle component leaves, up to fixed encoding multiplicity,

```text
Gamma_n b_d sum_(i+j=n-d)b_i b_j.
```

For a double, the two cases correctly retain either the `(d-1)` choices that
split the fixed residual component or the `(j-1)` choices that split a
remaining component.  The exact identities

```text
sum_(i+j=N)b_i b_j=2(1-1/N)b_N,
sum_(i+j=N)(j-1)b_i b_j=(N-3+2/N)b_N
```

and `Gamma_n=O(sqrt(n))`, `N>=2n/3`, bound every case by `C b_d`, hence by
`C d^-3/2`.  This proves only the stationary shell envelope.  M94 correctly
labels the complementary score envelope and the resulting direct-L1 bound
unresolved.

## 7. Fresh exact certificates and compact-k11 check

`independent_bulk_audit.py` constructs the literal ordered-pair marginal and
completion-count quotient over `Fraction`.  It checked 2,036 nonzero raw
Borel entries at `k=3` and 147,387 at `k=5`.  The exact field-by-field values
of event mass, signed defect, event L2, Cauchy lower bound, full BA2, and TV
match M94's retained rational certificate:

| `k` | `k pi(E)` | `k^2 Delta(E)` | `k^4` event L2 | `k^4` Cauchy | `k^4 BA2` | `k^2 TV` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | .0748530881 | .0643913022 | .1740956922 | .1661750997 | 5.230225557 | .8141455422 |
| 5 | .0743407909 | .0470842462 | .1872283239 | .1491056401 | 3.577332647 | .6261351499 |

The retained compact payload for `k=5,7,9,11` passes independent exact
event-mass and event-orbit-count formulas, every displayed scaling relation,
normalization, zero signed total, Cauchy, and equality of its duplicated BA2
and TV aggregates.  In particular its `k=11` event mass is independently
reproduced as

```text
7791991875308363374934707892425924553181100
-------------------------------------------------
1197559062505319752526328759910069803075170283.
```

The large all-target source JSON files named by the compact payload were not
retained.  Therefore the `k=11` signed defect and full BA2 audit is a compact
arithmetic/provenance check, not a second end-to-end full-kernel rerun.  This
is a nonmaterial reproducibility limitation because M94 labels every such
number floating finite only, retains the generating code and exact command,
and bases no asymptotic conclusion on it.

## 8. Artifacts, commands, runtime discipline, and hygiene

M100 owns `plan.md`, `checkpoint.md`, `independent_bulk_audit.py`,
`independent_bulk_audit_k5.json`, this report, and the final `SHA256SUMS`.
The decisive retained command from the repository root is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-20/mission-M100-m94-fresh-referee/independent_bulk_audit.py --k 3 5 --compact experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M94-balanced-abel-asymptotic/bulk_event_float_k11.json --output experiments/20260811-polynomial-mixing-resolution/cycle-20/mission-M100-m94-fresh-referee/independent_bulk_audit_k5.json
```

It completed in about nineteen seconds on this host under Python `3.12.3`,
uses only the standard library, is deterministic, and has `seed=null`.  No
package, network access, random input, commit, push, or external literature
claim was used.  All retained JSON is parsed, the Python file passes
`ast.parse`, `git diff --check` is clean, and generated Python caches are
removed before freeze.  The final checksum manifest covers every retained
owned artifact except itself.

## 9. Verdict, numbered objections, and controlling next step

**ACCEPT: STRICT OBSTRUCTION REDUCTION; ZERO MATERIAL NUMBERED OBJECTIONS.**

M94's proved statements survive independent analytic and exact-finite audit.
Its finite central-event signal is a credible, sharply falsifiable threat to
the stronger stationary-L2 route, but it is not an asymptotic obstruction.
The controlling statuses are:

```text
exact Borel/orbit convolution                         proved
bulk and boundary Abel asymptotics                    proved
central-event exact mass and Theta(k^-1)              proved
Cauchy implication conditional on (BD)                proved implication
stationary shell envelope                             proved
(BD)                                                  unresolved
(BA2)                                                 unresolved
direct signed L1                                      unresolved
H0, bridge gaps, identity heat-bath gap, Terminals    unresolved
```

The highest-value next lemma remains M94's scalar `(BD)`, preferably through
the channel-combined dominance inequality `(6.3)`.  Only a proof of that
lemma would justify declaring `(BA2)` refuted; even then, the direct signed-L1
route would remain open.
