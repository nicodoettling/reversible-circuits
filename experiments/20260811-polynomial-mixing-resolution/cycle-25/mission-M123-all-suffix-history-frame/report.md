# M123 final report: complete histories and the rank-five basin-frame obstruction

Date: 2026-08-13. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: PROMOTE THE EXACT OBSTRUCTION FOR FRESH REFEREE AUDIT.
PROVED/REFUTED ROUTE: the natural canonical-basin analysis frame is not <= I.
FIRST EXACT FAILURE: local rank s=5.
ALL-SUFFIX CONTRACTION AND EVERY GAP REMAIN OPEN.
```

The surrounding project target remains uniform on fixed-length identity
words in `Omega(N,m)`.  Permutations compose as `(pq)(x)=p(q(x))`; tuple
factors are displayed left-to-right.  This mission concerns only the
auxiliary right-heavy recurrence

```text
H=(I-Q)^(-1)A_0 <= q(1-q)
```

in the nonlazy minimal-long-cycle parking projection.  It proves no
auxiliary gap, ROOT-MEAN LIFT, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing, Terminal A, or Terminal B.

```text
candidate                  | complete-history category/Bessel frame
claimed target             | auxiliary right-heavy all-suffix contraction
identity ok                | not a sampler-generation claim
crosses Hurwitz components | not applicable to this auxiliary operator
exact diagnostics          | all-j DAG, literal marks, rational frame certificate
verdict                    | route refuted at s=5; target inequality unresolved
```

## 2. Precise strongest result and claim statuses

For ordered compositions `C` of `s`, let

```text
rho_s(C)=product_i w_(c_i)/[len(C)!w_(s+1)].
```

For each active canonical endpoint `e`, let `B_e` be the sources refining
its first part and `c_e=len(e)rho_s(e)`.  On `L2(rho_s)`, define

```text
v_e(C)=1[C in B_e]/sqrt(c_e).                       (2.1)
```

**Proved/refuted theorem.**  The universal assertion that the analysis frame
`{v_e}` has operator at most the identity is false.  At `s=5`, the Gram
matrix has an eigenvalue strictly greater than one, certified by an exact
four-coordinate rational Rayleigh quotient

```text
421891/418853 > 1.                                  (2.2)
```

If a full marked probability space forgets measure-preservingly to `rho_s`
and uses the same capacities, constant pullback is an isometry and preserves
this Gram matrix exactly.  Thus the natural full marked constant-pullback
frame, and any positive all-history frame containing its root coordinates,
also fails.

This result refutes a proof route, not the contraction itself.  A
success-weighted submeasure has a different operator; the current artifacts
do not identify it with `H` or decide its norm.

## 3. Complete-history mass and signed-frame equality

For `x=(s,K,R,B)`, M65's accepted contextual mean and attachment law give

```text
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B), t>B, j=1,...,k.                 (3.1)
```

Every attachment rank is retained, `j=0` is killed, and no child/parent
`alpha` ratio appears.  The phase `s+K-R` strictly descends.

Expanding terminal and deep successful histories defines a finite recursion
`S(x)`.  Induction using the accepted closed-mean identity proves

```text
S(x)=q_x=w_(s+1-B)w_B/w_(s+1)                     (3.2)
```

for every admissible context.  This is a universal normalized-mass theorem,
not merely a bounded check.  At `(3,1,0,1)`, the two tempting extra-alpha
normalizations give `15/16` and `7/16`, rather than `q=9/16`, so both are
exactly refuted.

For a basin current

```text
theta_e=sum_(C in B_e)rho_s(C)[h_x(C)-q_x],
A_0=sum_e theta_e^2/c_e,
```

expanding every square into ordered signed source pairs and then expanding
the nilpotent resolvent proves the complete signed two-copy equality for
`H`.  It supplies no positivity or Bessel inequality.

## 4. Exact category collision

The natural unique-active-reset-category assertion is false at

```text
x=(4,1,0,1), C=(1,1,1,1).
```

Here `h_x(C)=1`, `rho_4(C)=1/125`, and the canonical path meets both active
endpoints

```text
(2,1,1), (3,1).
```

Every successful finer mark above this source is therefore in two canonical
basins.  Assigning it only to the first active edge changes the second current
from `1647/15625` to `1098/15625` and changes the energy from

```text
true A_0       =1351279/28125000
partition value= 748477/28125000.                  (4.1)
```

The independent literal ambient witness uses `n=6,r=5`.  It enumerates five
source factor words, four scans per word, and every actual pair-fibre outcome.
The two favourable atoms have total raw rate `alpha_5=1/30`, normalized value
one, and both basin memberships.  Adding word, scan, outcome, shuffle, or
inverse-insertion marks cannot remove basin membership fixed by `C`.

## 5. Exact rank-five frame certificate

Put

```text
O_(e,f)=rho_s(B_e intersect B_f),
C_(e,f)=c_e 1[e=f].
```

The Gram matrix is `C^(-1/2)OC^(-1/2)`, so the frame is at most the identity
iff `C-O` is positive semidefinite.  For

```text
E={(1,3,1),(2,2,1),(3,1,1),(4,1)},
```

the exact principal matrix is

```text
[ 5/108       0        0       -5/216   ]
[    0     35/1296     0      -25/1296  ]
[    0        0      49/1296  -41/1296  ]
[ -5/216  -25/1296  -41/1296    4/81    ].         (5.1)
```

Its determinant is `-27125/235092492288`.  The rational vector
`a=(1/2,5/7,41/49,1)` gives

```text
a^T(C-O)a=-155/63504,
a^TCa=2094265/6223392,
a^TOa=2109455/6223392,                              (5.2)
```

and hence (2.2).  This is an exact sign certificate; no numerical
eigenvalue is needed.  Exact exhaustive principal-minor checks certify
`C-O>=0` for `s=2,3,4`.  At `s=5`, all 231 principal minors of size at most
three are nonnegative, and (5.1) is the first found four-coordinate failure.
Floating power iteration gives `lambda_max approximately 1.039533091512`
only as a calibration.

## 6. Marked pullback audit and the exact missing operator

If `kappa_*mu=rho_s`, the map `Uf=f composed with kappa` satisfies

```text
<Uv_e,Uv_f>_mu
 =rho_s(B_e intersect B_f)/sqrt(c_ec_f).            (6.1)
```

Thus measure-preserving full-space pullback really does preserve the Gram
matrix and nonzero Gram spectrum.  This statement is proved algebraically;
the earlier interrupted script was correct only under these explicit
hypotheses.

The qualification is substantive.  The complete-history recursion currently
aggregates only a successful submeasure of total `q`.  Its root pushforward
would be `eta_x(C)=rho_s(C)h_x(C)`, whose overlap matrix is

```text
O^succ_x(e,f)=sum_C rho_s(C)h_x(C)1_Be(C)1_Bf(C), (6.2)
```

not `O`.  It also does not construct failure atoms.  Since
`theta_e=eta_x(B_e)-q_x rho_s(B_e)`, (6.2) alone does not reproduce the
desired square as a Bernoulli Bessel coordinate.

For a full prefix-history space, the exact operator still missing from the
artifacts is

```text
V_(a,e)=1[R_a]1[kappa_a in B_e]/sqrt(p_a c_e),

G^hist_((a,e),(b,f))
 =mu(R_a intersect R_b intersect kappa_a^-1(B_e)
                    intersect kappa_b^-1(B_f))
  /sqrt(p_a p_b c_e c_f).                          (6.3)
```

If (6.3) is the intended frame, its root block is already (5.1), so it
fails.  A differently success-weighted construction must state its measure,
vectors, cross-prefix Gram entries, and exact equality to `H`; the coarse
certificate does not decide such an unstated operator.

## 7. Exact implementation and bounded diagnostics

`history_frame_search.py` is a standalone standard-library `Fraction`
implementation of the all-attachment recurrence.  The durable rerun used

```text
python3 -B history_frame_search.py --s-max 10 --multitype-s-max 8 \
  --results results.jsonl --summary summary.json
```

from this directory.  It reports:

- zero complete-history-mass failures;
- zero signed-frame-identity failures;
- zero right-heavy target failures for `2<=s<=10`, `K in {1,2,5}`, every
  `B`; the largest ratio is about `.6731838254` at `(10,1,0,4)`;
- zero stronger multitype-envelope failures through `s=8,K<=6`; the largest
  ratio is about `.6210042669` at `(8,1,0,3)`;
- every attachment label `(k,j)` reached in the tested closure;
- the exact category collision and both extra-alpha witnesses above.

These bounded target passes are falsification only and prove no all-suffix
inequality.  `micro_history_collision.py` produces the literal hidden-atom
witness.  `hidden_frame_spectrum.py` uses exact Gaussian determinants and
the rational Rayleigh certificate, replacing the interrupted factorial-time
characteristic-polynomial attempt.  Its durable command is

```text
python3 -B hidden_frame_spectrum.py --output hidden_frame_spectrum.json
```

All computations use Python 3.12.3, standard-library exact arithmetic, no
nonstandard dependencies, and `seed=null`.

## 8. Dependencies, statuses, and strongest self-attack

- **Accepted dependencies:** M50's root-composition law, canonical basins,
  and capacities; M65/M69's closed contextual mean, pointwise all-`j`
  inheritance, product restriction, and no-extra-alpha normalization;
  M109/M114's unweighted nilpotent reset recurrence.
- **Proved here:** complete success-history mass `q`; universal signed
  two-copy equality; the isometric pullback lemma; the exact composition
  frame obstruction; and the logical transfer to any full marked constant
  pullback with the stated marginal and capacities.
- **Refuted here:** unique canonical reset categories, first-active-edge
  partition equality, both extra-alpha normalizations, and the natural
  universal canonical-basin Bessel/frame bound.
- **Exact finite:** the literal ambient collision; finite target scans; and
  the complete small-rank principal-minor audits.
- **Unresolved:** a differently success-weighted history operator, a
  restricted inequality for the actual contextual-function family, `L=5`,
  all-`L` contraction, ROOT-MEAN LIFT, every auxiliary or original gap, and
  both terminal outcomes.

The strongest self-attack is that (5.2) uses an arbitrary frame-direction
coefficient vector.  It need not lie in the restricted family of contextual
centered functions generated by `(K,R,B)`.  Therefore it closes the generic
Bessel shortcut but does not provide an `H>q(1-q)` witness.  Also, mass `q`
does not turn the successful histories into a Bernoulli event without a
proved failure complement.  These are limitations, not hidden assumptions.

Original-chain exceptional cases `m` odd, `m=0`, `m=2`, and `N=2` do not
enter this auxiliary result and receive no new conclusion.

## 9. Artifacts, freeze, and final disposition

Owned artifacts are

```text
plan.md
checkpoint.md
history_frame_search.py
results.jsonl
summary.json
micro_history_collision.py
micro_collision.json
hidden_frame_spectrum.py
hidden_frame_spectrum.json
proof_notes.md
report.md
freeze_manifest.md
SHA256SUMS
```

The freeze manifest records the exact commands, current artifact hashes,
fresh `/tmp` payload comparisons, syntax checks, JSON parsing, whitespace,
and owned cache hygiene.  No predecessor, coordinator note, manuscript,
project skill, or shared source is edited.

```text
FINAL VERDICT: PROMOTE THE EXACT RANK-FIVE FRAME OBSTRUCTION FOR FRESH AUDIT.
ALL-SUFFIX CONTRACTION AND THE PROJECT TERMINALS REMAIN UNRESOLVED.
```
