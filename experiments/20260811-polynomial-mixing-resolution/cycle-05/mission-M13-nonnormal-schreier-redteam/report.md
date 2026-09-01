# Cycle 05 M13 report: nonnormal-Schreier and genuine-bottleneck red team

## 1. Exact quantified claim and convention

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a displayed word
evaluates as `t_1...t_m`.  Put `M=binom(N,2)` and

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
K=(1/2)I
  +(1/(2|R_m|)) sum_{r in R_m}
      (1/(m-r+1)) sum_{i=1}^{m-r+1} H_{i,r},
R_m={3,4,5} intersect [m].
```

The target law is the global uniform law `pi` on `Omega(N,m)`, not a
Hurwitz-orbit conditional law.

No reducibility or superpolynomial-gap family was found.  The following two
original-`K` candidate-cut rejections are proved.

### Theorem A: the minimal full-support macro is not a bottleneck

For `N>=3`, let `m=2N-2`, `B=|R_m|`, and

```text
F_N={w in Omega(N,2N-2):
     the factorization graph is connected on all N labels}.
```

Then `F_N` is nonempty and proper and

```text
Q_K(F_N,F_N^c)
 >= pi(F_N)/[16 B N(m-2)M^2],

Phi_pm(F_N)
 :=Q_K(F_N,F_N^c)/min{pi(F_N),pi(F_N^c)}
 >=1/[16 B N(m-2)M^2]
 >=1/[48 N(m-2)M^2].                                  (1.1)
```

Its exact stationary mass is

```text
pi(F_N)
 = (2N-2)! N^(N-3)
   / [(1/N!) sum_{lambda partition N}
        (f^lambda)^2 c_lambda^(2N-2)],                 (1.2)
```

where `f^lambda` is the irreducible dimension and
`c_lambda=sum_{(i,j) in lambda}(j-i)`.  Moreover `pi(F_N)<1/2` for every
`N>=6`, with an explicit geometric upper bound proved below.  Thus
`(F_N)_{N>=6}` is a literal infinite smaller-side candidate, but (1.1)
rules it out.

### Theorem B: the first-join star coordinate is not a bottleneck

For every `N>=3`, every even `m>=4`, and fixed label `v`, let

```text
A_v={w in Omega(N,m):v is an endpoint of t_1}.
```

Then

```text
pi(A_v)=2/N,
Q_K(A_v,A_v^c)
 >= pi(A_v)/[2|R_m|(m-2)M^2],
Phi_pm(A_v)
 >=1/[2|R_m|(m-2)M^2].                                (1.3)
```

At minimal full support, `t_1` is the first join-tree edge, so this is the
star cut on a visible state-dependent coordinate of the nonnormal Hurwitz
Schreier orbit.

These are scoped nonterminal results.  They do not prove a gap lower bound for
`K`.

## 2. Full proof and construction

### 2.1 Exact global stationary mass

The checked minimal transitive identity-factorization count is

```text
|F_N|=(2N-2)!N^(N-3).                                  (2.1)
```

For completeness, the denominator in (1.2) follows from the central group
algebra element

```text
A=sum_{t in T_N} t.
```

On the irreducible representation indexed by `lambda`, `A` acts by the
content scalar `c_lambda`.  Fourier inversion in the regular representation
therefore gives, for every `m`,

```text
|Omega(N,m)|
 =[id]A^m
 =(1/N!) sum_{lambda partition N}(f^lambda)^2 c_lambda^m.   (2.2)
```

Equations (2.1)--(2.2) prove (1.2).  The cut is proper because
`e^m` is an identity word supported on one edge, while (2.1) is positive.

The trivial and sign representations have dimensions one and content scalars
`M` and `-M`.  Since `m=2N-2` is even, (2.2) implies

```text
|Omega(N,2N-2)| >= 2M^(2N-2)/N!,
pi(F_N) <= U_N
 :=(2N-2)!N^(N-3)N!/[2M^(2N-2)].                       (2.3)
```

Direct simplification gives

```text
U_6=114688/234375<1/2
```

and

```text
U_(N+1)/U_N
 = [8(2N-1)/N]
   (1-1/N)^(2N-2)(1+1/N)^(-(N+1)).                     (2.4)
```

Using
`log(1-x)<=-x-x^2/2` and
`log(1+x)>=x-x^2/2` gives, for `N>=6`,

```text
log(U_(N+1)/U_N)
 <= log 16-3+1/(2N)+3/(2N^2)
 <= log 16-23/8 <0.
```

Thus with `theta=16 exp(-23/8)<1`,

```text
pi(F_N)<=U_6 theta^(N-6)<1/2,  N>=6.                   (2.5)
```

This explicitly accounts for the exponentially small stationary mass rather
than treating it as evidence for a bottleneck.

### 2.2 Marked removable leaf-square bijection

For `w in F_N`, mark an adjacent square

```text
t_i=t_(i+1)=(uv)
```

together with an endpoint `v` when:

1. no other factor of `w` contains `v`; and
2. deleting the square leaves connected support on `[N]\{v}`.

Deletion produces a length-`2N-4` minimal connected identity word on the
remaining `N-1` labels.  Conversely, choose:

- the omitted label `v` in `N` ways;
- its neighbor `u` in `N-1` ways;
- a word in `F_(N-1)` on the fixed remaining label set; and
- one of the `2N-3` gaps of that word.

Inserting `(uv),(uv)` in the chosen gap preserves the product, connects
`v` as a leaf, and gives one marked state of `F_N`.  Deletion recovers all
four data, so this is a bijection of marked incidences.

Let `Z(w)` be the number of marks.  Uniformly on `F_N`,

```text
E_F Z
 = N(N-1)(2N-3)|F_(N-1)|/|F_N|
 = (1/2)((N-1)/N)^(N-4).                               (2.6)
```

For `N>=4`,
`log(1-1/N)>=-1/(N-1)`, so the last power is at least `e^-1`;
`N=3` gives `3/2` for that power directly.  In particular

```text
E_F Z>=1/8.                                             (2.7)
```

A fixed omitted label can define at most one mark, because it occurs in
exactly the displayed two positions.  Hence `Z<=N`, and without any
independence assumption,

```text
Pr_F(Z>=1) >= E_F Z/N >=1/(8N).                         (2.8)
```

### 2.3 One exact local exit from every certified state

Fix a marked square `e,e` omitting `v`.  Choose any transposition `f`
whose endpoints both avoid `v`; it exists because `N>=3`.

If the marked pair is not the last adjacent pair, use the length-three window
beginning at it and make the outcome

```text
(e,e,a) -> (f,f,a).
```

For the last pair use the boundary window ending at `m` and make the outcome

```text
(a,e,e) -> (a,f,f).
```

Both replacements preserve the exact ordered block product.  No outside
factor uses `v`, and the deleted base support is connected, so the output is
an identity word connected on only the other `N-1` labels.  It lies in
`F_N^c`.

For a fixed three-factor product, the first two transpositions determine the
third permutation uniquely.  Thus every length-three conditional fiber has
size at most `M^2`.  The exact probability assigned by `K` to this
specified outcome is at least

```text
q_N=1/[2B(m-2)M^2].                                    (2.9)
```

The factors are, in order: outer nontrivial mass `1/2`, uniform block-size
choice `1/B`, uniform length-three window `1/(m-2)`, and conditional
outcome probability at least `M^-2`.

Choose one mark deterministically whenever `Z>=1`.  Equations (2.8)--(2.9)
give

```text
E[K(w,F_N^c)|w in F_N]
 >=1/[16BN(m-2)M^2].
```

Multiplying by `pi(F_N)` proves the flow bound in (1.1).  Since
`min{pi(F_N),pi(F_N^c)}<=pi(F_N)`, the two-sided conductance bound follows
without a mass-orientation assumption.  The `r=4,5` terms and all other
`r=3` outcomes are nonnegative, so the displayed contribution is a lower
bound for the full original kernel, not for a modified or restricted chain.

### 2.4 First-join star cut

Global simultaneous conjugation preserves `Omega(N,m)` and is transitive on
the `M` possible first transpositions.  Hence `t_1` is exactly uniform and

```text
pi(A_v)=(N-1)/M=2/N.                                   (2.10)
```

Take `w in A_v`, write `a=t_1=(v,x)` and `b=t_2`, and retain `t_3`.

- If `b` avoids `v`, the right Hurwitz outcome
  `(a,b)->(b,bab)` has first factor outside the star.
- If `b=(v,y)` is a distinct star edge, the inverse Hurwitz outcome
  `(a,b)->(aba,a)` has first factor `aba=(x,y)`, outside the star.
- If `a=b`, choose an edge `f` avoiding `v` and use
  `(a,a,t_3)->(f,f,t_3)`.

Each is a positive outcome of the exact first length-three heat bath and
preserves its ordered product.  The same conditional-fiber bound gives

```text
K(w,A_v^c)>=1/[2|R_m|(m-2)M^2].
```

Averaging proves the flow statement in (1.3); division by the smaller
stationary side can only increase the ratio.  This handles `N=3`, where
`pi(A_v)=2/3`, as well as `N>=4`.

## 3. Probability, runtime, path, and congestion accounting

- The macro certificate uses exactly one `r=3` transition.  Its probability
  is (2.9), including laziness, block-size, window, and exact-fiber factors.
- The certificate-density loss is at most `8N`; it comes from the exact
  incidence expectation and `Z<=N`, not a heuristic typical-state claim.
- The star cut has no density loss: every state in the cut has one specified
  exit of probability at least (2.9), with general `m`.
- Duplicate target aggregation only increases transition probability.
  Contributions of `r=4,5` are explicitly nonnegative and are included in
  the exact finite full-boundary audit.
- Constructing the witness edge and block takes `O(N+m)` elementary work.
  Enumerating a length-three conditional fiber uses at most `M^2`
  candidates, polynomial in `N,m`.
- No comparison path, canonical hub, or diameter-to-gap inference is used, so
  there is no hidden path length or congestion.
- The exact verifier enumerates `M^m` words only in the three calibration
  cases and all conditional outcomes for every legal `r=3,4,5` window.  Its
  longest recorded case took about 2.4 seconds.  This is a finite falsifier,
  not a scalable algorithm or universal proof dependency.

## 4. Dependencies with status

1. **CITED AND CHECKED:** the Goulden--Jackson minimal transitive identity
   count `|F_N|=(2N-2)!N^(N-3)`, already convention-checked in the prior
   M13 report.
2. **PROVED HERE:** the character/content formula for `|Omega(N,m)|`, the
   trivial/sign mass upper bound, its geometric decay from `N=6`, the
   marked-square insertion/deletion bijection, the expectation and
   certificate-density bounds, both exact `H_3` exits, and all `K`
   normalizations.
3. **PROVED INHERITED, CONTEXT ONLY:** `F_N` is one Hurwitz orbit; normal
   braid quotients on project orbits are trivial; the connected Hurwitz
   diameter is polynomial.  None is needed to prove (1.1).
4. **EXACT FINITE:** `results.json` checks the character denominator,
   connected count, marked-incidence formula, both directed flows, every
   block-size contribution, and the 27/120/3936 calibrations.
5. **CONDITIONAL/OPEN:** inverse-polynomial embedded expansion for every
   subset of `F_N`; a uniform connected Hurwitz gap.
6. **EMPIRICAL:** none.  Decimal renderings accompany exact rational values
   only.

## 5. First unproved standalone proposition

> **Embedded nonnormal-Schreier isoperimetry.**  There exist universal
> `c>0,C<infinity` such that, with `m=2N-2`, for every `N>=3` and every
> nonempty `A subset F_N` satisfying `|A|<=|Omega(N,m)|/2`,
>
> ```text
> (1/|A|) sum_{x in A} K_(N,m)(x,Omega(N,m)\A)
> >=cN^(-C).                                            (5.1)
> ```

The left side is exactly `Q_K(A,A^c)/pi(A)`.  A superpolynomially small
sequence in (5.1) would be a literal Terminal-B conductance family for the
original `K`; a slow auxiliary Hurwitz or aligned-bridge mode would not.

Ordinary quotient facts do not decide (5.1): the orbit is `B_m/H` with
nonnormal stabilizer `H`, and trivial normal quotients exclude only
normal-coset coordinates.  Polynomial diameter also does not control edge
capacity; a barbell can have small diameter relative to its exponentially
large state count while all paths coalesce through a tiny interface.
Finally, the one-way domination of a Hurwitz restriction by `K` makes a
polynomial Hurwitz gap sufficient, but a slow Hurwitz cut may be crossed
rapidly by non-Hurwitz heat-bath outcomes.  Full `K` boundary remains
essential.

## 6. Strongest self-attack

The marked-square proof controls the whole macro `F_N` only after averaging.
It guarantees a certificate in merely an inverse-polynomial fraction of its
states.  A hidden subset could deliberately avoid all adjacent removable leaf
squares, so (1.1) gives no expansion for that subset.  The exact
`S_4,m=6` data already has 1704 of 2880 full-support states with no mark.
This is the strongest surviving failure mode and is exactly why (5.1) remains
open.

The exponentially small upper bound on `pi(F_N)` is not itself a
bottleneck: conductance divides the boundary flow by that same mass.  The
proof accounts for this cancellation explicitly.  Likewise, Theorem B
rejects only one visible first-join coordinate.  Neither theorem rules out an
arbitrary nonnormal Schreier barbell, a cut spanning several macros, or a
different density regime.

No claim here is Terminal A or Terminal B.

## 7. Calibration results

- Odd `m` is empty; `m=0` and `N=2` are singleton edge cases;
  original `m=2` is excluded.  The theorems use `N>=3`, even `m>=4`.
- At `m=4`, `R_m={3,4}`; the whole-word `H_4` term is retained in the
  exact flow.  At `m>=6`, all three block sizes are retained.
- `S_3,m=4`: `|Omega|=27`, `|F_3|=24`,
  `pi(F_3)=8/9`, marked-incidence total 18 and expectation `3/4`.
  Full flows are `2/81` from `r=3` and `2/81` from `r=4`, giving
  `Phi_pm(F_3)=4/9`.  The star cut has `pi=2/3`, `Phi_pm=1/4`.
- `S_4,m=4`: `|Omega|=120`.  The star cut has `pi=1/2`;
  its full flow is `3/100+1/16=37/400`, so `Phi=37/200`.
- `S_4,m=6`: `|Omega|=3936`, `|F_4|=2880`,
  `pi(F_4)=30/41`, marked-incidence total 1440 and expectation `1/2`.
  Its exact `r=3,4,5` flows are respectively
  `37/1640`, `513/17056`, and `55/1681`; total flow is
  `298449/3496480` and `Phi_pm=298449/938080`.
- Both directed flows agree exactly in every cut.  Conditional-fiber sizes,
  pair multiplicities, word ordering, support labels, both physical
  boundaries, and full kernel laziness are retained.
- Near-minimal doubled-tree hubs, the two previously rejected mountain/tree
  cuts, the failed `L=2` simulation, edge/degree parity, and raw uniform
  Cayley-tree assumptions are not used.

## 8. Artifacts and reproduction

Owned files:

- `plan.md`;
- `checkpoint.md`;
- `exact_cut_check.py`;
- `results.json`;
- this `report.md`.

Run from the repository root:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M13-nonnormal-schreier-redteam/exact_cut_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M13-nonnormal-schreier-redteam/results.json
```

The deterministic run uses Python `3.12.3`, no random seed or nonstandard
dependency, and records commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.  It states the universal claim
that a finite failure could falsify and does not infer an asymptotic theorem
from finite survival.

## 9. Verdict

PROVED

This verdict applies to Theorems A and B, the assigned candidate-cut
rejections.  The global terminal claim remains open at Proposition (5.1).
