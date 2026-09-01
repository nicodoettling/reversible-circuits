# M65 final report: contextual quotient absorption

Date: 2026-08-12.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, quantifiers, and convention

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  Let `R_s` be the accepted nonlazy stationary-flow
root-composition quotient of the minimal-long-cycle parking projection,
and put

```text
G_s=R_s/alpha_s,       alpha_s=2/[3s(s-1)].
```

For a contextual suffix statistic `phi`, let
`H(C)=E[phi|root composition C]`, suffix size `B`, and stationary law

```text
rho_s(C)=Z_s^(-1) [1/(number of parts)!] product_i w_(c_i),
w_t=t^(t-1)/t!.
```

The assigned universal claim was

```text
||H-EH||_(-1,G_s)^2 <= E[H 1_(last part=B)].        (1.1)
```

This report **refutes (1.1)**.  It also refutes the proposed universal
repair `delta+a<=1+O(1/s)`.  These are auxiliary comparison statements;
neither refutation is a gap upper bound for the full parking chain or for
the identity-bridge chain `K`.

## 2. Full argument and constructions

### 2.1 Closed conditional mean

Let `K` be the number of external root attachments, `R` the number before
the active attachment, `C=(c_1,...,c_k)`, and `t=c_k`.  Uniform deletion of
all other factors leaves a uniform shuffle of the `K` external and `k`
inner attachment chains.  Exact marked adjacency counting gives

```text
H(C)=0,                                               t<B,

H(C)=K binom(k+K-R-2,K-R-1)/binom(k+K-1,K-1),        t=B,

H(C)=[w_(t-B)w_B/w_t]
     [1-binom(K,R+1)/binom(K+k,R+1)],                 t>B.      (2.1)
```

For `t=B`, the two possible adjacent orders have prefixes `O^R OI` and
`O^R IO`; the full-word adjacency probability `(K+k)/r`, the scan
`1/(r-1)`, and the three-state heat bath `1/3` give the first binomial
ratio with every normalization retained.  For `t>B`, the factor in square
brackets is `P(I_1<O_(R+1))`; the remaining marked sum is M50's exact
one-part split coefficient.  Full details are in
`closed_mean_formula.md`.

### 2.2 Exact rank-two refutation

For every `K>=1`, take ambient rank `r=K+2`, coarse composition

```text
b=(3,1,...,1)                 (K parts),
```

and split the leftmost branch as `3=2+1`.  Then `s=2`, `B=1`, and
`R=K-1`.  The two inner compositions have

```text
rho((2)),rho((1,1))=2/3,1/3,
G_2((2),(1,1))=1,       G_2((1,1),(2))=2,

H((2))=K/(K+1),         H((1,1))=2/(K+1).
```

Thus

```text
EH=2/3,
||H-EH||_(-1,G_2)^2=2(K-2)^2/[27(K+1)^2],
E[H 1_(last=1)]=2/[3(K+1)].                         (2.2)
```

The ratio in (1.1) is `(K-2)^2/[9(K+1)]`, first exceeding one at
`K=14`, where it is `16/15`.  Equivalently
`delta+a=226/225`; as `K->infinity`, it tends `10/9`.

### 2.3 Refutation of `1+O(1/s)`

Keep `B=1,R=K-1` at arbitrary local rank `s`.  Let
`Z={last part=1}`, `p_s=rho_s(Z)`, and

```text
m_s=EH=w_s/w_(s+1)>=e^-1.
```

The composition `(s-1,1)` gives `p_s>=1/(3e^2)`.  The indicator `1_Z`
has exact normalized Dirichlet energy

```text
E_(G_s)(1_Z,1_Z)=m_s,                               (2.3)
```

because its crossing edges toggle the fixed final cut.  If
`q_T=E[H1_Z]` and `x=q_T/m_s`, then the variational definition of the
Green norm gives

```text
||H-m_s||_(-1,G_s)^2 >=m_s(p_s-x)^2.                (2.4)
```

Every terminal state has at least two parts, so `H<=2/(K+1)` there and
`x<=2e/(K+1)`.  Fix `K+1>=144e^5`.  Then

```text
delta+a-1 >=(p_s-x)^2-x >=5/(72e^4)>0               (2.5)
```

for every `s>=2`.  Hence no fixed constant `C` can make
`delta+a<=1+C/s` universal.

### 2.4 Correct marked inheritance

The ordinary-child guess `(K,R)->(k,0)` is false first at ambient `r=4`.
The correct mark retains the full attachment rank.  If `J` is the number
of current inner attachments before the active outer attachment, then

```text
nu_j=P(J=j)
 =binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

On a deep fibre, pointwise in the last-branch macro `v`,

```text
Phi_(K,R)(u)=sum_(j=1)^k nu_j Phi_(K+k,R+j)(v).      (2.6)
```

This follows from a marked deletion/insertion bijection; conditioning on
`J=j` leaves `K+k` synthetic attachments and exactly `R+j` before the
same active factor.  The `j=0` class is geometrically impossible.  The
weights sum to the deep coefficient in (2.1).

Bad geometry can repeat: for `R=K-1,j=k`, the child is again rightmost and
has weight `K/(K+k)`.  Along a unary spine the mark product is `K/(K+d)`.
Thus it is neither an ordinary rightmost child nor a one-time arbitrary
cost.

### 2.5 Why this is not a slow-mode theorem

The synthetic attachment history is not an observable of an unmarked
parking macro; different histories collide on the same state.  The literal
ambient realization has `r=s+K`, `b=(s+1,1^(K-1))`, and

```text
rho_r(b)=w_(s+1)/(K!Z_r).
```

Any cut contained in this fibre has exact pointwise root-merge escape at
least

```text
alpha_r K(K-1)=2K(K-1)/[3r(r-1)],                  (2.7)
```

which is inverse polynomial.  A strict depth-`d` unary history has exact
stationary/mark weight

```text
[K/(K+d)] [w_(s-d)/w_s],                            (2.8)
```

exponentially small for `d=Theta(s)`.  No nonnegligible stationary cut or
consistent unmarked Rayleigh function results.

## 3. Probability, runtime, path, and congestion accounting

- Exact scan: `r-1` sites; nontrivial fibre: three states;
  `alpha_r=2/[3r(r-1)]`.  These factors appear explicitly in (2.1).
- Attachment rank `J` has the exact negative-hypergeometric law above;
  `sum_(j>=1)nu_j=D_(K,R)(k)`.
- The first feasible failure is ambient `r=16`; all larger `K` in the
  rank-two family fail.
- The fixed-cut test has energy exactly `m_s`, with the standard
  `1/2 sum rho P (difference)^2` Dirichlet normalization.
- The literal outer-fibre escape is (2.7); no path or congestion bound is
  claimed.
- Exact factorization enumeration through ambient `r=7` is exponential
  and is used only for falsification.  The sparse quotient scanner uses
  `2^(s-1)` states; through `s=13`, `K<=64` plus large-K probes, its largest
  CG residual was below `1e-11` and runtime was about 1.4 seconds on this
  machine.  Those numerical values prove no asymptotic statement.

## 4. Dependencies, labelled

- **Proved/accepted:** M50 root-composition law and rates, fixed-composition
  product restrictions, exact `alpha_s`; M56 contextual locality,
  `alpha/gamma` norm cancellation, and marked separated-capacity
  recurrence.
- **Cited with conventions checked in frozen inputs:** Stanley--Biane
  parking-multiset enumeration; Goulden--Yong factor-tree sufficiency.
- **Proved here:** closed mean (2.1); rank-two infinite refutation;
  uniform constant refutation (2.5); negative-hypergeometric marked
  inheritance (2.6); repeated extreme weight; outer-fibre escape and unary
  stationary factor.
- **Refuted here:** literal harmonic/committor and one-sign generator
  routes; canonical subgenerator repair; contextual quotient absorption;
  `1+O(1/s)` scalar repair; ordinary `(k,0)` child map; one-time
  arbitrary-context cost.
- **Empirical exact/numerical:** formula and inheritance audits through
  ambient `r=7`; sparse Green scans through `s=13`.  These are independent
  falsifiers/calibrations, not proof dependencies.
- **Unresolved:** actual-edge marked source recovery and a weighted
  contraction for the full history mixture.

## 5. First unproved standalone proposition

> **MARKED WEIGHTED GREEN CONTRACTION.**  Replace M56's maximum over child
> ranks by the exact negative-hypergeometric mixture (2.6) and the exact
> stationary descendant law.  Construct actual unmarked `Pbar` flows for
> all resulting contextual charges with polynomial total Green energy,
> while recovering every colliding history on each actual edge with only
> additive polynomial load.

For a counterexample route, the corresponding first missing statement is
UNMARKED NESTED-RAYLEIGH CONSISTENCY from `rayleigh_lift_audit.md`.  Without
one of these two lifts, the scalar obstruction has no full-chain spectral
consequence.

## 6. Strongest self-attack

The delicate proved point is (2.6): it requires marked word/outcome
counts, not only the binary support event.  The proof retains `J`, the
active rank, scan site, and inverse insertions; the exact audit has zero
failures in 898 nonvacuous checks through `r=7`.  A hidden normalization
error would first appear as a synthetic-child scaling mismatch, which the
audit explicitly tests.

The greatest risk of overinterpretation is opposite: (2.5) is a lower
bound on one quotient-disintegration coefficient, not a lower bound on a
mixing time.  Synthetic histories are auxiliary labels, and (2.7) shows
that the most literal state cut has polynomial escape.  No claim about a
full `Pbar` or `K` bottleneck is made.

## 7. Calibrations

- `s=1`: singleton, zero Green norm by convention.
- `s=2`: exact two-state generator; first absorption failure at `K=14`.
- Ambient feasibility is always retained: the rank-two family uses
  `r=K+2`, and the general extreme family uses `r=s+K`.
- Stars, paths, rare large root degrees, and balanced compositions are all
  included in the exact macro enumeration through `r=7`.
- The parent `(1,0)` to child `(1,0)` scalar map fails on the two local
  macros `(0,0),(0,1)`; the corrected mixture gives both values exactly.
- The rightmost extreme persists with weight `K/(K+k)`, while a linear
  unary corridor has exponentially small stationary weight; both sides of
  this calibration are retained.

## 8. Artifacts and reproduction

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-14/mission-M65-contextual-quotient-absorption/
```

Principal proofs are `closed_mean_formula.md`,
`absorption_refutation.md`, `relaxed_absorption_refutation.md`,
`marked_context_inheritance.md`, `repeated_extreme_analysis.md`, and
`rayleigh_lift_audit.md`.

Reproduction commands:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/closed_mean_formula.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/closed_mean_formula_r7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/marked_context_inheritance_audit.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/marked_context_inheritance_r7.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/absorption_scan.py --s-max 13 --K-max 64 --rtol 1e-11 --maxiter 20000 --output experiments/20260811-polynomial-mixing-resolution/cycle-14/mission-M65-contextual-quotient-absorption/absorption_scan_s13_K64.json
```

The JSON files record Python/SciPy versions, commit, exact commands, and
finite-scope warnings.  `SHA256SUMS` records all frozen artifact hashes.

## 9. Verdict

REFUTED
