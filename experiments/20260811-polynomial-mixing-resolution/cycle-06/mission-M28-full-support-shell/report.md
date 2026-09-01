# M28 final report: the one-step full-support shell is proper and polynomially leaky

## 1. Exact claim, quantifiers, convention, and kernel

Permutations multiply as `(pq)(x)=p(q(x))`; words evaluate as
`t_1...t_m`.  For every `N>=5`, put

```text
M=binom(N,2),                  m=4N^3+4,
U={w in Omega(N,m):c(w)>=2},
F={connected full-support y:K(x,y)>0 for some x in U},
V=U union F,                                             (1.1)
```

where `c` counts all support-graph components, including isolates.  The exact
chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)] sum_i H_{i,r}.          (1.2)
```

**Theorem (proved).**

1. `V` has the exact intrinsic description

   ```text
   V={w: some nontrivial vertex cut has all crossing-factor
         occurrences inside one interval of at most five positions}.       (1.3)
   ```

2. `V` is a proper, globally oriented cut and

   ```text
   pi_{N,m}(V)<=exp(-5N^2)<1/2.                         (1.4)
   ```

3. For the original full chain,

   ```text
   Phi_pm^K(V)
   >=15 binom(N-1,2)/
      [768N(m-5)(m-4)M^10]
   >=1/(4N^25).                                         (1.5)
   ```

Thus the full disconnected macro closure plus its exact one-step connected
halo is not a superpolynomial bottleneck.  The theorem is a scoped
anti-bottleneck result, not Terminal A and not a refutation of other possible
Terminal-B cuts.

## 2. Full proof and construction

### 2.1 Exact characterization of the shell

For a nontrivial bipartition `P={A,A^c}` of `[N]`, call a transposition
*crossing* when its endpoints are in different blocks.

Suppose first that `w in U`.  A cut between any union of support components
has no crossing occurrence, so it satisfies (1.3).  If connected `w in F`,
choose a disconnected predecessor `x` and an `r<=5` window in which `x,w`
differ.  Across a cut between components of `x`, every factor outside that
window is internal.  Hence every crossing occurrence of `w` is in the update
window, proving the forward inclusion.

Conversely, suppose all crossing factors across `P` lie in an interval of
length at most five.  Extend it to a length-five window and write the word as

```text
L h R=e,                                                (2.1)
```

where `h` is the window product.  Every factor of `L,R` lies in the direct
product subgroup

```text
H_P=S_A x S_(A^c),
```

so (2.1) implies `h in H_P`.  Since `h` is a product of five transpositions,
its transposition length is odd and at most five.  Its cycles remain within
the blocks of `P`, so it has an internal transposition factorization of its
minimal length `1,3`, or `5`.  If necessary, pad by internal adjacent squares
to obtain exactly five factors.  Such an internal edge exists because
`N>=5` and a bipartition has a block of size at least two.

Replacing the witness window by this internal factorization preserves its
exact ordered product and produces a disconnected identity word `x in U`.
The exact `H_5` heat bath gives `K(x,w)>0`; reversibility is not needed for
positivity because the two blocks lie in the same conditional fiber.  This
proves (1.3).

An equivalent formulation used below is

```text
w in V^c iff deleting every five-position interval
             leaves the support graph connected.        (2.2)
```

Deleting fewer consecutive positions is covered by extending them to a
five-window; restoring factors cannot destroy connectivity.

### 2.2 Even-outside count for the global shell

Put

```text
j=m-6=4N^3-2,                 E=binom(N-1,2).           (2.3)
```

Every interval of at most five positions is contained in one of the `m-5`
length-six intervals.  Fix such a six-window and a bipartition whose smaller
side has size `s`.  Write

```text
e_s=binom(s,2)+binom(N-s,2)=M-s(N-s),
h_s=s!(N-s)!.                                           (2.4)
```

The `j` outside factors are all internal to the cut.  Let `T_P` be the sum of
the `e_s` internal transpositions in the group algebra of `H_P`.  It is
central.  If the six-block product is `b`, the outside count is zero unless
`b in H_P`; otherwise, if the window has `a` factors to its left, it is the
identity coefficient of

```text
T_P^a b T_P^(j-a)=T_P^j b.                              (2.5)
```

Since `j` is even, Cauchy--Schwarz bounds every coefficient of `T_P^j` by its
identity coefficient.  The frozen parity-aware central-trace estimate applies
because `j/e_s>=4log(2N)`, and gives

```text
[e]T_P^j<=4e_s^j/h_s.                                  (2.6)
```

There are at most `M^6` six-block words, so a fixed cut/window contributes at
most `4M^6e_s^j/h_s` shell words.

It remains essential not to pay a naked `2^N` factor.  Sum by the smaller cut
size and compare with the isolate cut.  Since

```text
E-e_s=(s-1)(N-s-1),                                    (2.7)
```

the normalized sum is

```text
sum_P e(P)^j/h(P)
 <=[E^j/(N-1)!]
   sum_{s=1}^{floor(N/2)}
     [binom(N,s)^2/N]
     exp{-j(s-1)(N-s-1)/E}.                            (2.8)
```

The `s=1` term is exactly `N`.  For `s>=2`, use

```text
j/E>=8N,
N-s-1>=N/4,
binom(N,s)<=N^s,
log N<=N/2.
```

Each remaining summand is at most `exp[-N^2(s-1)]`, whose sum is less than
one.  Thus

```text
sum_P e(P)^j/h(P)<=2N E^j/(N-1)!.                     (2.9)
```

Combining the windows, blocks, and cuts gives

```text
|V|<=8N(m-5)M^6 E^j/(N-1)!.                           (2.10)
```

At even length, Cauchy--Schwarz for the random-transposition walk gives

```text
|Omega(N,m)|>=2M^m/N!.                                 (2.11)
```

As `E/M=(N-2)/N`, equations (2.10)--(2.11) imply

```text
pi(V)
 <=4N^2(m-5)(1-2/N)^j
 <=4N^2m exp(-2j/N)
 <=exp(-5N^2)<1/2.                                    (2.12)
```

For the last inequality, `log(4N^2m)<=2N^2` and
`2j/N=8N^2-4/N` for `N>=5`.  This proves the exact global orientation (1.4),
not merely a conditional mass estimate.

### 2.3 A constant-density family of robust endpoint tails

Let `d=N-1`, let the transposition alphabet on `[d]` have size
`E=binom(d,2)`, and put

```text
k=m-5=j+1=4N^3-1.                                      (2.13)
```

Fix `q=(2,3)`.  Let `B_d(k,q)` be the number of length-`k` transposition
words on `[d]` with product `q`.  Fourier inversion for the nonlazy uniform
transposition walk gives

```text
B_d(k,q)/E^k
 =d!^{-1} sum_lambda d_lambda chi_lambda(q)r_lambda^k.
```

Because `k` and `q` are both odd, the trivial and sign representations
together contribute `2/d!`.  Every other transposition character ratio
satisfies

```text
|r_lambda|<=1-2/(d-1),                                 (2.14)
```

the exact content bound attained at `(d-1,1)` and its conjugate.  Since
`|chi_lambda(q)|<=d_lambda` and the Plancherel dimensions sum to `d!`, the
absolute remaining contribution is at most

```text
exp[-2k/(d-1)]<=1/(8d!).                               (2.15)
```

The last inequality follows from
`2k/(d-1)>=log(8d!)`; the left side is at least `7N^2`, whereas
`log(8d!)<=3+N log N`.  Therefore

```text
B_d(k,q)>=(15/8)E^k/d!.                                (2.16)
```

Call such a tail *robust* when deleting every five consecutive factors leaves
connected support on `[d]`.  If it is not robust, some vertex cut has all
crossing occurrences in a five-window.  For a fixed cut/window, choose the
five window factors in at most `E^5` ways and bound the remaining internal
words crudely by `e_P^(k-5)`.  This intentionally discards the endpoint
constraint; it does **not** commute an arbitrary odd block product through the
cut subgroup.  Using at most `2^d` cuts and noting that the largest
disconnected internal alphabet has size `E(1-2/d)`, the nonrobust count
divided by the lower bound (2.16) is at most

```text
3k 2^d d! exp[-2(k-5)/d].                              (2.17)
```

Its logarithm is at most `3N^2-7N^2=-4N^2`, hence it is less than one half.
Consequently the number `R` of robust `q`-tails obeys

```text
R>=(15/16)E^k/(N-1)!.                                  (2.18)
```

In particular `R>0`, which will also prove that `V` is proper.

### 2.4 Explicit H5 boundary surgery

Let

```text
z=N,               s=(z,1),               q=(2,3).
```

For every robust tail `u=(b_1,...,b_k)` counted in (2.18), form

```text
y=(s,q,q,q,s,b_1,...,b_k).                             (2.19)
```

The prefix product is `s q^3 s=q`, because `q` is disjoint from `s`; the
tail product is also `q`.  Thus `y` is an identity word.  Its only factors
crossing the cut `{z}|[d]` are at positions one and five, so `y in F subset
V`.

Use the `H_5` window at positions five through nine.  Applying four right
Hurwitz identities

```text
(u,v)->(v,v^{-1}uv)
```

gives the same-product target

```text
(s,b_1,b_2,b_3,b_4)
 ->(b_1,b_2,b_3,b_4,g^{-1}s g),
g=b_1b_2b_3b_4.                                       (2.20)
```

Every `b_i` fixes `z`, so `g^{-1}s g` is another transposition incident to
`z`.  In the resulting word `y'`, the two `z`-edges are at positions one and
nine; no five-window removes both.  The tail factors retain their order, with
one `z`-edge inserted between `b_4,b_5`.  Any global five-window deletes at
most five consecutive tail factors.  Tail robustness leaves `[d]` connected,
and the surviving `z`-edge joins `z` to it.  Therefore every five-window
deletion leaves full support connected.  By (1.3),

```text
y' in V^c.                                              (2.21)
```

This proves properness and supplies `R` distinct boundary sources.

A fixed length-five product fiber has size at most `M^4`, because its first
four transpositions determine the fifth permutation.  Including laziness,
block-size choice, scan normalization, and the exact heat bath, the specified
transition has probability at least

```text
p=1/[6(m-4)M^4].                                       (2.22)
```

### 2.5 Conductance and all block sizes

For `r=3,4,5`, define the exact stationary boundary term

```text
Q_r(V,V^c)
 =pi(V)/[6(m-r+1)]
   E_{w|V}[sum_i H_{i,r}(w,V^c)].                      (2.23)
```

The lazy identity has zero boundary contribution, and

```text
Q_K(V,V^c)=Q_3+Q_4+Q_5.                                (2.24)
```

Retaining only the sources (2.19) and targets (2.20) inside `Q_5`, then
using (2.10), (2.18), (2.22), and the orientation (2.12), gives

```text
Phi_pm^K(V)
 >=[R/|V|]p
 >=15E/[768N(m-5)(m-4)M^10].                          (2.25)
```

Finally, for `N>=5`,

```text
E>=N^2/5,
(m-5)(m-4)<16N^6,
M^10<=N^20/1024,
```

so (2.25) is at least `1/(4N^25)`.  Every omitted `Q_3,Q_4,Q_5` transition
is nonnegative; no restriction or projected kernel has replaced the original
chain.

## 3. Worst probability, runtime, path, and congestion accounting

- Exact shell characterization: equation (1.3).
- Global shell mass: at most `exp(-5N^2)`.
- Robust boundary-source count: at least
  `(15/16)binom(N-1,2)^(m-5)/(N-1)!`.
- Specified transition probability: `1/[6(m-4)M^4]`.
- Conductance: the exact first bound in (1.5), hence at least `1/(4N^25)`.
- The boundary path has length one: one actual `H_5` heat-bath outcome.  The
  four Hurwitz identities describe that one target and incur no path or
  congestion loss.
- A supplied cut/window witness is verified in `O(m)`.  A supplied robust
  tail can be checked naively in `O(m^2+Nm)` by scanning five-deletions and
  support connectivity.  No recognition algorithm over all cuts is claimed.
- The exact `r<=5` heat-bath sampler retains inherited polynomial per-step
  cost.

## 4. Dependencies and statuses

1. **Proved here:** exact equality (1.3), properness, global mass bound,
   robust-tail lower bound, explicit boundary transition, and (1.5).
2. **Proved and frozen in Cycle-02 M12:** the parity-aware direct-product
   central trace bound used in the global shell estimate (2.6), with its
   density hypotheses.  The tail bad-set bound (2.17) is instead the explicit
   crude word count stated above.
   Source: `cycle-02/mission-M12-high-surplus/proof_final.md`, Lemma 2.1.
3. **Proved/audited in Cycle-04 M07 and rederived here:** the exact
   transposition character-ratio bound and parity-aware Fourier normalization.
4. **Inherited proved:** exact heat-bath reversibility/stationarity and
   polynomial exact block sampling.
5. **Not used:** macro reachability as a probability estimate, restriction
   gaps, finite representatives, canonical forms, length-two simulation, or
   graph-only dynamics.
6. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **SECOND FULL-SUPPORT SHELL.**  Let `V_N^(0)=U_N` and recursively
>
> ```text
> V_N^(a+1)={y:K(x,y)>0 for some x in V_N^(a)} union V_N^(a).
> ```
>
> Characterize `V_N^(2)` exactly for `m=4N^3+4`, determine whether it is
> proper, orient its global stationary mass, and prove inverse-polynomial
> conductance or a superpolynomial upper bound with all block sizes included.

The robust targets (2.20) lie in `V_N^(2)\V_N`, so the new proposition must
use more than one localized cut interval.

## 6. Strongest self-attack

The exponent 25 is intentionally crude but universal.  More importantly,
conductance is not monotone under taking larger neighborhoods: the theorem
does not control `V_N^(2)` or an adaptively selected subset of robust
full-support words.  The proof also uses the dense length `4N^3+4`; a
near-minimal shell can have very different mass and no robust-tail estimate of
this form.

The shell is exponentially small, but that does not itself refute it as a
bottleneck.  The decisive fact is the separately proved polynomial ratio of
boundary flow to its exact smaller-side mass.  No conclusion about the global
spectral gap follows from rejecting this one cut.

## 7. Calibration

- Odd `m`: the bridge is empty; no theorem is asserted.
- `m=0` and even `N=2`: singleton regimes.
- `m=2,N>=3`: excluded disconnected chain.
- `S_3,m=4`: 27 words and four macro/Hurwitz classes.  Because `H_4` is the
  whole-word heat bath, the analogous one-step shell is all of `Omega`; the
  present five-window characterization is not asserted.
- `S_4,m=4`: 120 words and 13 macro/Hurwitz classes; full support is
  infeasible and `H_4` is retained.
- `S_4,m=6`: 3936 words and 17 macro/Hurwitz classes.  No finite behavior is
  extrapolated to the dense theorem.
- Connected near-minimal doubled trees need not remain connected after a
  five-deletion; the proof instead counts dense robust tails and makes no
  near-minimal claim.
- Ordered positions are essential: the shell records the span of crossing
  occurrences, not merely the support graph.
- No edge/degree parity identity shortcut is used; parity appears only in the
  exact Fourier calculation.
- The boundary move is a genuine `H_5` outcome, not the false `L=2` local
  simulation.
- The exact global mass orientation precedes conductance division, and all
  `Q_3+Q_4+Q_5` terms remain in (2.24).

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was used.  Reproduction consists of checking the cut-subgroup
coefficient calculation (2.5)--(2.10), Fourier estimate (2.14)--(2.18), and
the explicit ordered-product surgery (2.19)--(2.25).  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns the inverse-polynomial conductance of the exact one-step
full-support shell, not either global terminal outcome.
