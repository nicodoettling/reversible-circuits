# M79 final report: fresh M76 referee and reset-resolvent refutation

Date: 2026-08-12. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, frozen bundle, and exact scope

Frozen M76 report SHA256:
`376c27b991073c97899071e8c2f31ea5806179f0c15289a485d4e91faabec7ae`.
Frozen M76 manifest SHA256:
`be966da6865c2015dee7f585a9fa68a84582f084553643420dcfe5e427f5a2e1`.
Both hashes were independently reproduced.

**REFEREE VERDICT: ACCEPT. Numbered objections: none.** M76's proved claims,
conditional implication, and reduction are correctly scoped and normalized.
In particular, M76 explicitly labels its inverse-split-mass inequality (8.1)
as unresolved and explicitly warns that the finite `.761` margin could
reverse. It claims neither polynomial marked occupation, ROOT-MEAN LIFT, an
auxiliary `Pbar` gap, nor any result for the original identity-word chain.

**SEPARATE POST-REFEREE VERDICT: REFUTE M76'S OPEN INEQUALITY (8.1).** An
exact reachable seed violates it at rank 20, and a degree-two edge subfamily
gives an infinite linear lower bound. This is a new negative theorem, not an
objection to the frozen report.

All statements here use `(pq)(x)=p(q(x))`, with factors displayed
left-to-right, and concern only the full **nonlazy stationary-flow parking
projection** `Pbar_r` in the minimal long-cycle factorization sector. They do
not concern the original lazy `{3,4,5}` heat-bath kernel `K`.

## 2. Independent referee audit

### 2.1 Strict descent and reachability — accepted

For a deep child

```text
y=(t-1,K+k,R+j,B),    n=s-t>=k-1, j>=1,
```

the potential `P=s+K-R` satisfies

```text
P(x)-P(y)=n-k+j+1>=j>=1.
```

A canonical reset child

```text
y=(A+c_2-1,k-1,k-2,c_2)
```

has `P(y)=A+c_2<=s<P(x)`. Thus `D+J_can` is a finite DAG.

Every reset has `K-R=1`. Starting from `(1,0)`, a deep step with
`k=K'-1,j=R'` reaches every `K'>R'>=1`; conversely `j>=1` rules out
`R=0,K>1`. Hence the exact closure is

```text
{(1,0)} union {(K,R):K>R>=1}.
```

Independent exact-rational enumeration through `s=7,K<=6` checked 3,750
strict descents and 2,754 right-heavy reset children.

### 2.2 Fixed-power counterfamily — accepted

For `x_s=(s,s^2,s^2-1,s-1)`, the unary deep child has coefficient exactly
`s^2/(s^2+1)`. The degree-two edge `(s-1,1)->(s)` has reset coefficient
`p_s^2`, where

```text
p_s=rho_s(last part=1)>=w_(s-1)/(2w_(s+1))->e^-2/2.
```

Both children have `P=s`. Therefore every fixed-power `P^d u` one-step
certificate eventually exceeds one, while the logarithmic variant diverges.
This refutes only the one-step proof templates and not occupation itself.

### 2.3 Seed kernel and scaling — accepted

Independent expansion gives

```text
A_a=sum_(p-part compositions of a) product w/(p+1)!,
C_a=sum_(p-part compositions of a)(p+1)product w/(p+2)!.
```

For a seed `(K,R)=(1,0)`, summing the canonical basin yields exactly M76's

```text
M_B(t)=0                                      (t<B),
       =w_B A_(s-B)/w_(s+1)                  (t=B),
       =w_(t-B)w_B C_(s-t)/w_(s+1)           (t>B),

J_s(B,t)=[M_B(t)-q_Bp_t]^2/
          {[w_(s-t)w_t/w_(s+1)]q_B}.
```

There were 112 exact Fraction comparisons against direct composition-basin
enumeration through `s=7`, with exact difference zero. Under
`v_a=e^-a w_a`, `A_a,C_a` gain `e^-a`, while each of `p_t,M_B,Q_G` gains
one common `e^-1` and `q_B` is invariant. This confirms the frozen scaling
normalization.

### 2.4 Conditional occupation implication — accepted

If M76's proposed inequality

```text
K_reset h<=h,     K_reset=(I-D)^(-1)J_can, h=1/q,
```

held, then `mu_n=delta_x K_reset^n` would obey `mu_n h<=h(x)` and hence
`mu_n 1<=h(x)` because `h>=1`. Strict descent makes `mu_n=0` for `n>=P(x)`.
M71's base bound and pure-deep suffix occupation give

```text
b(x)<=eP^2(1+log P).
```

Together with M50's exact split bound

```text
h(x)<=3(s+1)^(3/2)/4<=3P^(3/2)/4,
```

this yields M76's

```text
sum_(n<P)mu_n b <=(3e/4)P^(9/2)(1+log P).
```

This was correctly stated as a conditional implication.

### 2.5 Raw versus eliminated normalization — accepted

The independently derived `h`-transform has the exact deep cancellation

```text
q_x D(x,y)/q_y=rho_s(k,t) nu_j.
```

A separate grouped implementation matches every exact-rational eliminated
value through rank 7. At `(s,K,R,B)=(14,4096,4095,1)` it gives

```text
raw transformed child row       1.085041110951...,
eliminated transformed row       .761048371831...,
```

matching M76. Pure-deep elimination is therefore essential and correctly
implemented in the frozen report.

## 3. New theorem: inverse split mass fails infinitely

Take the reachable seed

```text
x_s=(s,1,0,s).
```

Here the contextual root observable is one only on the unary composition
`(s)` and zero elsewhere, and `D=0` because no last part exceeds `B=s`.
Restrict the canonical residual kernel to degree-two edges

```text
(A,s-A)->(s),       1<=A<=s-1.
```

M50's basin identity and Lagrange inversion give the exact basin ratio

```text
beta_A=rho(basin_A)/rho(A,s-A)
      =(2/w_A)[z^A](e^T-1)/T
      =2A/(A+1).
```

Writing `q_s=w_s/w_(s+1)=(s/(s+1))^(s-1)`, the transformed contribution of
this edge is exactly

```text
q_s^3(A/(A+1))^2.
```

Therefore

```text
q_x [(I-D)^(-1)J_can h](x_s)
 >=q_s^3 sum_(A=1)^(s-1)(A/(A+1))^2
 =q_s^3[s-2H_s+H_s^(2)]
 >=(s-1)/108.                                      (3.1)
```

The last bound uses `q_s>=e^-1` and `A/(A+1)>=1/2`. Thus the ratio grows at
least linearly. This proves:

- M76's open inequality (8.1) is false infinitely often;
- every relaxation `ratio<=1+C/P` with fixed `C` is false;
- `P(ratio-1)=Omega(P^2)` on this family.

The full exact row already crosses one at `s=20`:

```text
s=19: .9843552830895422,
s=20: 1.0395701502029937,
s=21: 1.0949193740971426,
s=30: 1.5978651562744444,
s=40: 2.1637325166792154.
```

At `s=20`, the exact numerator minus denominator is

```text
1319315040996006533582695321065228519637911534141383378013775131343321661229366983304182798480404765424423014964179826086315118038022394345522881606506187979374519923727371694831731018692108333627571142876588105484156772290207777121>0.
```

The exact proof and all rational values are in `infinite_refutation.md` and
`terminal_exact_s18_s40.json`.

## 4. Surviving narrower occupation lemma

The counterexample exploits the inverse child split mass; the ordinary row
mass remains small. The correct next statement is

> **DEEP-ELIMINATED RESET SUBSTOCHASTICITY.** For every right-heavy reset
> seed `x=(s,K,K-1,B)`, prove
> ```text
> [(I-D)^(-1)J_can]1(x)<=1.                         (4.1)
> ```

If (4.1) holds, strict reset descent gives

```text
sum_(n<P)delta_x K_reset^n1<=P,
```

and hence, using `b<=eP^2(1+log P)`, separated marked occupation at most

```text
eP^3(1+log P).                                      (4.2)
```

This avoids inverse-`q` entirely and is sufficient for the same polynomial
unmarking route.

Finite evidence is materially stronger than M76's old rank-14 scan but is
still not a proof. An independent grouped kernel, validated against exact
Fraction enumeration, gives worst right-heavy row masses

```text
s=14: .6909242237587,
s=20: .7568304720189,
s=30 seed slice: .8081995911375.
```

Every maximum through rank 20 occurs at `K=1,R=0`; through rank 30 the worst
suffix is near `B=s/3`. An additional independent exact scan over **all**
contexts through `s=7,K<=6` supports the stronger multitype inequality

```text
K_reset1(x)<=(K-R)(1-q_x),                          (4.3)
```

whose right-heavy specialization is `<=1-q_x<1`.

The tempting raw induction is false. Both `(D+J)1<=1` and
`J1+D[(K-R)(1-q)]<=(K-R)(1-q)` have finite counterexamples. Hence a proof of
(4.1) or (4.3) must use the fully eliminated augmented-event filtration,
an orthogonal martingale/Haar decomposition after deep histories are
aggregated, or another global resolvent identity. No such proof is claimed.

## 5. Probability, normalization, runtime, and reproducibility

- Every quotient coefficient uses
  `theta_e^2/[Q_G(e)q_parent]`, with
  `Q_G(e)=rho(refined)*(root degree)`.
- Every deep coefficient uses stationary group mass, exact child split
  mean, and M65's negative-hypergeometric weight, divided by parent `q`.
- All exact checks use Python `fractions.Fraction`; no tolerance enters the
  rank-20 counterexample or infinite lower bound.
- `independent_audit.py --s-max 7 --k-max 6` ran in about `.2` seconds.
- The grouped rank-14 broad audit ran in `4.26` seconds; the grouped rank-20
  broad row scan ran in `52.44` seconds; the seed scan through rank 30 ran in
  `153.25` seconds.
- Python was `3.12.3`; all runs are deterministic with seed `null`.
- Floating grouped results are falsifiers/discovery diagnostics only; the
  promoted negative theorem is exact and analytic.

Representative commands:

```text
python3 -B independent_audit.py --s-max 7 --k-max 6 \
  --output independent_audit_s7.json

python3 -B terminal_exact_counterexample.py \
  --s-values 18 19 20 21 22 24 26 30 40 \
  --output terminal_exact_s18_s40.json

python3 -B terminal_asymptotic_probe.py \
  --s-values 20 30 40 60 80 120 160 200 \
  --output terminal_asymptotic_s200.json
```

## 6. Dependencies and claim ledger

- **Accepted frozen inputs:** M50 root-composition law, first-boundary basin
  identity and capacities, split lower bound; M56 contextual locality and
  norm cancellation; M65/M69 contextual mean and marked inheritance; M71
  canonical base bound, deep contraction, and one-shot label multiplicity.
- **Independently accepted from M76:** strict DAG descent, reachable closure,
  fixed-power counterfamily, exact seed kernel/scaling, and the conditional
  implication `(8.1)=>(4.4)`.
- **Proved here:** exact infinite refutation (3.1) of M76's open (8.1) and all
  fixed-`C/P` relaxations.
- **Exact finite:** all-context rank-7 audit and exact terminal-family values
  through rank 40.
- **Empirical finite:** grouped row scans through rank 20 broadly and the
  seed slice through rank 30.
- **Unresolved:** deep-eliminated reset substochasticity (4.1), the stronger
  augmented variance inequality (4.3), polynomial marked occupation,
  actual unmarked ROOT-MEAN LIFT, the `Pbar` gap, and every result for `K`.

## 7. Final handoff

**Accept frozen M76, but delete inequality (8.1) from the live proof route.**
Its inverse split weight turns a harmless ordinary reset row into a linearly
growing row on terminal seeds. The new first unproved lemma is (4.1), or
preferably the falsifiable augmented-event inequality (4.3). Either would
give the polynomial occupation bound (4.2) by strict reset descent. Neither
the new refutation nor the surviving lemma resolves the auxiliary `Pbar`
gap, and neither is terminal evidence for the original heat-bath chain.
