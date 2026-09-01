# M147 final report: all-suffix functional envelope and scalar nonclosure

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and proved claims

```text
FINAL VERDICT: PROMOTE FOR FRESH REFEREE AUDIT.
PROVED: exact all-suffix functional recurrence on (kappa,D).
PROVED: deficit-blind pointwise scalar Bellman closure is impossible.
UNRESOLVED: a deficit-aware uniform renewal/contraction inequality.
```

The accepted finite `L<=5` pattern does extend abstractly, but only as a
functional recursion carrying the attachment deficit `D=K-R`.  It does not
extend as a scalar right-heavy induction.  An infinite reachable family
shows that omitting `D` identifies a contracting state with a state that
strictly exceeds the same local budget.

This is a proof-route obstruction, not a bottleneck or slow mode for the
original chain.

## Field 2 — target, convention, candidate, and scope

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, with factors displayed
left-to-right.  This mission concerns only the unweighted full reset excursion
of the auxiliary nonlazy stationary-flow parking-degree projection in the
minimal-long-cycle sector.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| all-suffix auxiliary functional envelope | pointwise right-heavy excursion budget | N/A: no sampler | N/A: auxiliary projection | exact recurrence, infinite witness, capped audits | functional recurrence kept; deficit-blind scalar closure refuted |

No auxiliary gap, ROOT-MEAN LIFT, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing, Terminal A, or Terminal B is claimed.  M145 owns explicit
`L=6` enumeration; none was duplicated here.

## Field 3 — exact all-suffix recurrence

Put `s=B+L`, `kappa=K+1`, `D=K-R`, and

```text
q_(B,L)=w_(L+1)w_B/w_(B+L+1).
```

For last-part height `h`, root degree `d`, and retained attachment rank `j`,
the exact law and child update are

```text
nu_(kappa,D,d)(j)
 =binom(d,j)(D)^(rise)_(d-j)(kappa-D)^(rise)_j
   /(kappa)^(rise)_d,

(kappa,D,L) -> (kappa+d,D+d-j,h-1).
```

The normalized root-group mass is

```text
mbar_(L,B)(h,d)
 =c(L-h,d-1)/[d! w_(L+1)(w_B/w_(B+h))].
```

Consequently `F=H/q` obeys the exact finite recursion

```text
F_(B,L)(kappa,D)
 =A_(B,L)(kappa,D)
  +sum_(h=1)^L 1[B+h-1>=2]
    sum_d mbar_(L,B)(h,d)
    sum_(j=1)^d nu_(kappa,D,d)(j)q_(B,h-1)
      F_(B,h-1)(kappa+d,D+d-j).
```

Every positive rank is retained; only `j=0` and rank-one children are killed.
Suffix excess and the accepted phase strictly descend, so the recurrence is
nilpotent.  The proof note derives the `2^L` root support and contextual means
from definitions without extrapolating finite tables.

## Field 4 — corrected exceptional-current envelope

For each supported exceptional endpoint normalize

```text
cbar_E=c_E/q, abar_E=a_E/q, thetabar_E=theta_E/q,
lambda_E=b_E/c_E.
```

The correct reset bound is

```text
A/q <= q[C_s-q sum_E abar_E lambda_E]
       +sum_E thetabar_E^2/cbar_E.
```

It subtracts one power of `lambda_E`; the rejected M131 two-power display is
not used.  Recursively inserting this reset bound into the exact recurrence
defines a rigorous all-suffix functional majorant
`E_(B,L)(kappa,D)`.  M140/M144's accepted theorem allows `C_s<3/4` for
`s>=100`.

This prescription is finite and exact as a majorant, but the exceptional
currents and arbitrary-deficit descendants prevent scalar closure.

## Field 5 — infinite exact nonclosure family

At `(s,B,L)=(3,2,1)`, `q=3/8` and the complete excursion is exactly

```text
H(3,K,K-D,2)/q
 =1/16+[2D/(K+1)-3/8]^2/4.                         (5.1)
```

For the right-heavy state `D=1`, (5.1) is strictly below
`1-q=5/8` for every `K>=1`.  For the same `K` but `R=1,D=K-1`, it is
strictly above `5/8` iff `K>=32`; equality holds at `K=31`.

At the first strict pair,

```text
H(3,32,31,2)=24313/743424 < 15/64,
H(3,32, 1,2)=175033/743424 > 15/64,
bad margin       =793/743424.
```

Both states have identical `L,B,s,q,C_3=9/32,K,z` and the entire Cayley-ratio
sequence.  They differ only in `D`.  Therefore no state summary omitting `D`
and using the named scalar data can determine the exact Bellman value.  Nor
can it both dominate every reachable child and remain below the pointwise
local budget `1-q`.

## Field 6 — reachability and first missing statistic

For every `K>=32`, start at the fresh right-heavy parent

```text
(s,K_parent,R_parent,B)=(K+2,1,0,2).
```

The positive root group of degree `K-1`, last part four, and prefix
`(1,...,1)` has a `j=1` attachment branch of probability exactly `1/K`.
Its child is `(3,K,1,2)`, the bad state above.  Thus the obstruction occurs
inside the accepted reachable closure at unbounded parent suffix excess.

The first necessary extra coordinate is

```text
D=K-R, equivalently p=D/(K+1).
```

The exact sufficient attachment state is `(kappa,D)`.  A deterministic child
updates it by `(kappa+d,D+d-j)`.

## Field 7 — fixed-moment obstruction and limitation

For every fixed `r`, two explicit binomial-parity probability measures on
valid deficits agree on all polynomials of degree at most `r` but differ on
the rising factorial of degree `r+1`.  Attachment with root degree `r+1`
queries precisely that factorial.  Hence no fixed truncation of deficit
moments determines the exact all-degree attachment operator.

This is rigorously a statement about unrestricted moment-compression schemes.
The two constructed measures are not claimed to be the attachment laws of
two individual parents.  Tracking deterministic `(kappa,D)` avoids the
moment obstruction.

The strongest self-attack is equally important: the infinite pair refutes an
exact or pointwise budget-preserving deficit-blind Bellman proof.  It does
not refute a nonlocal amortized potential that permits selected children to
exceed `1-q` and pays their aggregate charge from a right-heavy parent.

## Field 8 — exact checks and reproducibility

Run from this mission directory:

```text
python3 -B all_suffix_exact.py --output all_suffix_exact.json
```

The standalone checker imports no predecessor code or output.  It uses
Python 3.12.3, standard-library exact `Fraction` arithmetic, and `seed=null`.
The capped run verifies:

- 270 exact attachment-law normalizations through degree six;
- eight exact normalized recurrence identities, including three minimal
  `B=1` (`L+1=s`) boundaries;
- eleven `L=1` boundary rows with `K` through 4096;
- `C_3=9/32`, the `K=31` equality, and every first-witness fraction;
- three positive-probability reachability constructions; and
- nine finite-difference moment pairs for `r=0,...,8`.

It reports zero failures.  These computations audit the formulas; the
algebraic derivations and infinite family prove the claims.

## Field 9 — dependencies, next lemma, artifacts, and hygiene

Accepted dependencies are M109/M114's all-rank nilpotent recurrence and
lower boundary results; M115/M116 and M117/M121's arbitrary-deficit
lower-excess envelopes; and M140/M144's scalar `C_s` theorem, corrected
one-power subtraction, and accepted right-heavy `L=5` theorem.  M131 is
negative provenance only.

The first unresolved positive lemma is:

> Construct a nonnegative deficit-aware potential
> `V_(B,L)(kappa,D)` satisfying the corrected reset-plus-descendant recursion
> at every reachable state, and prove
> `V_(B,L)(kappa,1)<=1-q_(B,L)` on right-heavy seeds.  Values at
> non-right-heavy children may exceed their local budgets, but their aggregate
> charge must be amortized by the parent.

Owned artifacts are `plan.md`, `checkpoint.md`,
`all_suffix_functional_obstruction.md`, `all_suffix_exact.py`,
`all_suffix_exact.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  No predecessor, coordinator, manuscript, project-skill,
M145, or other worker file was edited.  Original-chain cases `m` odd,
`m=0,2`, and `N=2` do not enter this separated auxiliary lemma and receive no
new conclusion.

