# M142 fresh referee report on M139

Date: 2026-08-13 UTC.

## Field 1 — verdict and numbered objections

Verdict: **ACCEPT** the frozen M139 package, relative to the already accepted
M125/M129 coefficient formula and M133/M136 positive unique-cycle expansion.

Blocking objections:

1. None.

Accepted as **PROVED** are the marked-pair recurrence, labelled-atom/cavity
translation, Lagrange and beta reductions, and the exact `c=2,3` formulas.
Accepted as **REFUTED** are shifted ULC, a universal H2 surplus `1+1/d`, and
the direct same-orientation TP2/PF route at raw `Phi`.  The ordinary H2
log-concavity theorem and every higher-core or mixing consequence remain
**UNRESOLVED**.

Non-blocking scope qualifications:

1. The TP calculation blocks only the stated same-orientation closure; it is
   not an impossibility theorem for every transform argument.
2. The positive H2 and higher-core-budget signs are finite facts only.
3. Nothing in M139 proves a gap for the original `{3,4,5}` heat-bath chain.

## Field 2 — target, convention, and dependency boundary

The target is the auxiliary M113/M118 incidence-key law

```text
rho(kappa)=|C_kappa|/Z_inc,       H[d,c]=M[d,d-c],
```

and its two-parallel-edge-core summand `H_2[d,c]`.  It is not the global
uniform law on identity words and not the lifted `bar_pi` law.  The inherited
permutation convention is `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right; M139 performs no new permutation operation.

This referee audited M139's reduction from the accepted M125/M129 and
M133/M136 inputs.  It did not reopen those predecessors or assume the
unresolved ordinary log-concavity statement.

## Field 3 — immutable integrity and reconciliation

All coordinator-supplied SHA-256 values match exactly, including:

```text
report                         3a9998104df900cc8385793acc74b6151784e7920486553a4b4382fbe3b73103
proof                          cb067b68ac404f60314f4d85bcb3894c15f55abae1b0276ac8a6e5a3238c6461
checker                        605e01db0ca51f2f5b7fd3a3dea4e6449fb546d9acb6a9c7f5bbfb41aaa9e085
results                        f2bdb9a2a43f88e943e59c303182914beede626fbd8a73cbb771e51ae2fd5873
analytic certificate           ce9d5b037f5a4214473f45b805719e323db611ad3a044ab894ee6e78a5946db6
curvature budget               82845e78055032c6c9f7099058eff8699d190ca94a51cf0e312b4e391b8a4bb6
manifest                       ddbcdc572626bfd72a210082866a967703310f1e6548cb49aff58e99fadbb12f
SHA256SUMS                     aaf23ad3ad94e96d592c5e0234a7432c22dc4790ad229a34880f7e2072db99dd
```

`sha256sum -c SHA256SUMS` returned `OK` for every one of the eleven frozen
M139 files.  The clean-room checker independently repeated this inventory
test with zero failures.  No interrupted, mutable, or temporary predecessor
output was used.

## Field 4 — marked-pair theorem and recurrence audit

Fix indexed cycle atoms.  On the connected diagonal `L+R=|E|`, the bipartite
incidence multigraph has `V=E`, hence one cycle.  Two atoms are co-blocked in
both colours exactly when their two labelled edges have the same left and
right endpoints.  They are therefore parallel and form a length-two cycle.
Uniqueness of the graph cycle makes the pair unique.  Conversely, the two
edges in a length-two core share both endpoints.  The iff and uniqueness
claims are correct.

For marks of sizes `a,b` and selected unmarked multiset `e`, their common
block has `2+|e|` incident atoms and therefore weight

```text
(a+b+||e||)^((2+|e|)-3)=(a+b+||e||)^(|e|-1).
```

Choosing its extra atoms contributes `binom(nu,e)`; all remaining blocks are
an ordinary partition.  This proves

```text
P^bullet_(a,b;nu)(y)
 = y sum_(e<=nu) binom(nu,e)
     (a+b+||e||)^(|e|-1) P_(nu-e)(y).
```

Because the two marks are already in the same join component, that component
is distinguished.  Choosing its unmarked atoms gives exactly one factor
`binom(nu,e) C^bullet_e A_(nu-e)`.  Removing all proper choices from
`A^bullet_nu` yields M139's connected recurrence with neither a missing root
factor nor an overcount.  Summation over unordered marked pairs then counts
each two-edge-core unicycle once.

Literal set-partition enumeration and independent leaf-peeling of the graph
two-core found zero iff/uniqueness failures through six atoms.  Literal
weighted rows through `d=5` equal the separate marked recurrence exactly.

## Field 5 — species, cavity, Lagrange, and `I_2` audit

For a type with multiplicities `m_a`, M125's multiplier satisfies

```text
n(lambda) product_i h(a_i)^2
 = d! product_a q_a^m_a/m_a!,
q_a=a^(2a+1)/(a!)^2.
```

Indeed `h(a)=a^(a+1)/a!`, while `n(lambda)` supplies one factor `a^-1`
per atom.  The clean-room checker verified this identity for all 66 integer
types through `d=8`.

At a planted vertex with one boundary edge of size `s` and `k` child edges,
the degree is `k+1`; its M125 weight is therefore
`(s+sum b_i)^(k-2)`.  The children are an unordered labelled SET, giving
`1/k!`, and every child crosses to the opposite colour.  This independently
gives the coupled equations

```text
T^L_a=y Phi_a(B^R),  B^L_a=xi_a T^L_a,
T^R_a=z Phi_a(B^L),  B^R_a=xi_a T^R_a.
```

At a core vertex there are two boundary edges, so the exponent becomes
`k-1`, exactly `Psi`.  The external `yz` marks the two core vertices.  The
factor `1/2` is correct for the unordered core pair: unequal sizes occur in
two ordered summands and equal sizes retain the required `1/2!`.  Exact test
coefficients were respectively `8=8` and `32=32`.

For `tau=v sum_b B_b exp(b tau)`, Lagrange inversion gives, for `k>=1`,

```text
[v^k] exp(s tau)/s
 = 1/k [w^(k-1)] exp(sw)(sum_b B_b exp(bw))^k,
```

which is the ordered-child coefficient divided by `k!`.  At `k=0`, both
sides are `1/s`; this term is present in M139.  Thus
`Psi_s(B)=exp(s tau_B)/s` is correct.  Multiplying the two core-vertex terms
leaves `(a+b)^-2`, so with `X=x exp(tau_L+tau_R)` the sum is exactly

```text
U_2=(u^2 yz/2) I_2(Q(X)^2).
```

Finally, scaling each child of size `b` by `t^b` and integrating against
`t^(s-1)` supplies `1/(s+sum b_i)`, changing the `Psi` exponent from `k-1`
to the `Phi` exponent `k-2`.  Two independent specializations through child
degree five, for `s=1,2,3,4`, had zero Lagrange, `k=0`, or `Phi` failures;
the direct `I_2` check had zero failures in degrees two through eight.

## Field 6 — beta transform and boundary audit

On a monomial `y^L z^R` with `L+R=c`, put

```text
j=d+c-2L=d+R-L.
```

After `y=(1-t)/t` and `z=t/(1-t)`, the external beta factor gives exponents

```text
t:       d+R-L = j,
1-t:     d+L-R = 2d-j.
```

Together with

```text
j!(2d-j)!=(2d+1)! integral_0^1 t^j(1-t)^(2d-j)dt,
```

this proves M139's cut transform, including its factorial powers.  All 84
bounded exponent/positivity cases through `d=8` passed.

Let `S_n=sum_(a=1)^(n-1)q_aq_(n-a)`.  With no off-core atom, the ordered core
sum, `1/2`, `(a+b)^-2`, and central beta integral give

```text
H_2[d,2]=(d!)^3 S_d/(2d^2).
```

With one off-core atom of size `d-n`, the unattached core vertex contributes
`1/n`, the leaf contributes `1/(d-n)^2`, and the two colour choices cancel
the unordered-core `1/2`; both cuts have factorials `(d-1)!(d+1)!`.  Hence

```text
H_2[d,3]=d!(d-1)!(d+1)!
 sum_(n=2)^(d-1)(S_n/n)q_(d-n)/(d-n)^2.
```

Both formulas matched every independently computed row for `2<=d<=16`.

## Field 7 — curvature and TP obstruction audit

The independent exact row at `d=4` is

```text
(H_2[4,2],H_2[4,3],H_2[4,4])=(80136,109440,44928),
```

and its shifted-ULC margin is exactly

```text
109440^2-4*80136*44928=-2424287232.
```

This is minimal because `d=4` is the first row with an interior index.  The
clean-room scan also reproduced all three stated `d=16` masses and

```text
16 H_2[16,12]^2-17 H_2[16,11]H_2[16,13]
=-12068184285817619472004173248675719963879857493070204183335383575630227635520668657140147159040000000000.
```

It is the first `1+1/d` failure in exhaustive `(d,c)` order through `d=16`.
No ordinary H2 or `1+1/d^2` failure occurred through that cap; those two
observations are **EXACT FINITE**, not universal claims.

For homogeneous child count `k`, write `p=k-2`.  With increasing `s` and
`S`, the determinant sign is the sign of

```text
r(S_2)^p-r(S_1)^p,   r(S)=(s_2+S)/(s_1+S),
```

and `r` is strictly decreasing.  Therefore the signs are positive for
`k=0,1`, zero for `k=2`, and negative for `k>=3`.  The exact test minors are
`17/5184, 1/72, 0, -1/36, -17/576`.  The scalar coefficients
`(1,1/2,1/2,2/3)` have first LC margin `-1/4`.  This validates precisely the
claimed mixed-orientation/raw-PF obstruction and no stronger impossibility.

## Field 8 — independent checks, reproduction, and hygiene

The retained checker is
`clean_room_audit.py`; its machine-readable output is `results.json`.
Decisive totals are:

- zero topology failures among connected unicycles through six atoms
  (`1,6,54,620,8760` cases by atom count);
- zero weight-translation failures in 66 integer types through `d=8`;
- zero literal-versus-marked row failures through `d=5`;
- zero independent-versus-frozen row failures for every `2<=d<=16`;
- zero boundary, formal-transform, `I_2`, or beta failures.

Reproduction from repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-33/mission-M142-m139-fresh-referee/clean_room_audit.py --max-d 16 --output experiments/20260811-polynomial-mixing-resolution/cycle-33/mission-M142-m139-fresh-referee/results.json
```

Environment: repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, standard
library only, deterministic exact arithmetic, `seed=null`.  The `d=16` cap
is present only to reach the claimed first inverse-linear counterexample; no
larger exploratory scan was run.

Retained pre-freeze hashes are:

```text
clean_room_audit.py  56c5abaf347bc72df91f6141824f8db16eee0366643ce59c180b423069e9f04c
results.json         6876c7b6c186c4920c816f507df9344558e9f0f8cdfab992959334d6d7f299ca
```

An initial local audit run stopped after reaching `d=16` because the referee
checker accidentally let a negative integer power become a float.  The
checker was corrected to use exact `Fraction` bases and rerun from scratch;
no output from the aborted run was retained.  No package, dependency,
commit, push, manuscript, skill, coordinator file, M139 file, or other worker
directory was changed.  A compile-only bytecode cache is removed before
freeze.

## Field 9 — accepted claim and downstream action

M139 should be promoted into the coordinator ledger as an independently
accepted **strict reduction**, not as a proof of log-concavity or mixing:

> The two-edge-core coefficient profile has the exact marked-pair recurrence,
> coupled `Phi` cavity, scalarized `I_2(Q^2)` core, positive beta cut
> transform, and exact first two boundaries stated by M139.

The first unresolved lemma remains coefficient log-concavity in `u`, at fixed
`x` degree, of the beta-integrated coupled `Phi` fixed point, together with a
quantitative surplus large enough to dominate the separate higher-core
correction.  Even that would only advance DEFECT NO-VALLEY and its conditional
projection consequence.  Fixed-defect expansion, `gap(A_d)`, the handle
projection, the original lazy exact `{3,4,5}` heat-bath gap, and both terminal
outcomes remain unresolved.
