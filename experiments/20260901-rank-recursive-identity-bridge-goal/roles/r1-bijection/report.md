# R1 final report: positive stable-sort disintegration

Date: 2026-09-01 UTC

## Resolution

**Proved.**  Formula `(D)` is correct for every `N >= 2`, `L >= 0`, and
external endpoint `g in S_N`, under the convention fixed below.  For every
binary pattern there is an explicit product-preserving stable-sort bijection
and an explicit inverse.  The actual sorted star endpoint is `h^{-1}g`.

This resolves R1, including all requested boundary cases.  It does **not**
make the rank disintegration a polynomial-time sampler: drawing the weighted
branch and sampling the prescribed star fiber remain separate R2/R3
obligations.

## Convention and notation

Permutations are maps `[N] -> [N]`, with

```text
(alpha beta)(x) = alpha(beta(x)).
```

Thus the rightmost factor acts first.  A displayed word
`w=(t_1,...,t_L)` evaluates as `eval(w)=t_1 ... t_L`.  Let

```text
H   = {h in S_N : h(N)=N} ~= S_(N-1),
A_N = {(i j) : 1 <= i < j < N},
B_N = {(i N) : 1 <= i < N}.
```

An `A_N` factor is called old and a `B_N` factor is called star.  Write
`tau_i=(i N)`.  The group-algebra unit is `e`, and every element, including
the zero group-algebra element, has zeroth power equal to `e`.  In particular,
when `N=2`, `C_1=0` but `C_1^0=e`.

## The fixed-pattern theorem

**Theorem (proved).**  Fix integers `N >= 2`, `L >= 0`, a binary pattern
`p in {A,B}^L` having `k` symbols `B`, and `g in S_N`.  Let `W_p(g)` be the
set of length-`L` transposition words with type pattern `p` and endpoint `g`.
There is a bijection

```text
Phi_p : W_p(g) ->
  disjoint_union_(h in H)
    {u in A_N^(L-k) : eval(u)=h}
      x {v in B_N^k : eval(v)=h^(-1)g}.
```

The map and its inverse use at most `k(L-k)` adjacent rewrites, preserve the
relative order of the old-factor ancestors and of the star-factor ancestors,
and preserve the total product after every rewrite.

### Forward map

For every `a in H`, direct evaluation gives

```text
a tau_i = tau_(a(i)) a.                              (1)
```

Therefore an adjacent star-old pair can be rewritten as

```text
tau_i a -> a tau_(a^(-1)(i)).                        (2)
```

Repeatedly apply (2) until no star lies left of an old factor.  If

```text
I(p) = number of pairs (r,s) with r<s, p_r=B, p_s=A,
```

then every rewrite decreases `I` by exactly one.  Hence the procedure stops
after exactly `I(p) <= k(L-k)` rewrites, with all old factors on the left.
No rewrite exchanges two old ancestors or two star ancestors, so both orders
are stable.

The terminal relabeling is unique, not just terminating.  Consider an
original star `tau_i`, and list in original left-to-right order the old
factors strictly to its right as

```text
a_1, ..., a_s.
```

That star must cross those factors, and only those factors, in the forced
order `a_1,...,a_s`.  Its final lower endpoint is consequently

```text
a_s^(-1)(...a_2^(-1)(a_1^(-1)(i))...)
  = (a_1 ... a_s)^(-1)(i).                           (3)
```

Other stars never alter this label.  Formula (3) proves that all choices of
currently available adjacent inversion have the same terminal word.  Denote
that word by `u v`, with `u` old and `v` star, and set
`Phi_p(w)=(u,v)`.

Every application of (2) is an equality in `S_N`, so

```text
eval(w) = eval(u) eval(v).                           (4)
```

### Inverse map for every pattern

Given `(u,v)` and `p`, begin with the tagged concatenation `u v` and scan the
target pattern from left to right.

- If the next target symbol is `A`, leave the leftmost remaining old factor
  in that position.
- If it is `B`, locate the leftmost remaining star and move it left across
  every intervening old factor, one position at a time, using

  ```text
  a tau_j -> tau_(a(j)) a.                           (5)
  ```

Rule (5) is the exact inverse of (2), by (1).  It terminates after exactly
`I(p)` moves and produces the requested pattern.  A target star crosses
leftward, in reverse order, exactly the old factors that will lie to its
right.  If their product is `s=a_1...a_s`, its label changes from `j` to
`s(j)`; forward formula (3) changes it back to `j`.  Thus this construction
is both a left and right inverse to `Phi_p`.  This proves injectivity and
surjectivity, not merely equal cardinalities.

### Endpoint orientation

Let `h=eval(u)` and `q=eval(v)`.  Equation (4) says `g=hq`, whence

```text
q = h^(-1) g.                                        (6)
```

The order in (6) is a word-level statement.  For example in `S_3`, take

```text
h=(1 2), q=(1 3), g=hq=(1 3 2).
```

Then `h^{-1}g=(1 3)=q`, whereas `g h^{-1}=(2 3)`.

## Group-algebra disintegration

Put

```text
C_N     = sum_(t in T_N) t,
C_(N-1) = sum_(t in A_N) t,
J_N     = sum_(t in B_N) t.
```

Summing (1) over `i<N` shows `h J_N=J_N h` for every `h in H`; hence
`C_(N-1) J_N=J_N C_(N-1)`.  Also `C_N=C_(N-1)+J_N`.  The ordinary binomial
identity in the group algebra and coefficient convolution therefore give,
for every `g in S_N`,

```text
[g] C_N^L
 = sum_(k=0)^L binom(L,k)
     sum_(h in H)
       [h] C_(N-1)^(L-k) [h^(-1)g] J_N^k.            (D)
```

The fixed-pattern theorem gives a second, positive word-level proof.  For a
fixed `k`, all `binom(L,k)` patterns are bijective to the same old/star
Cartesian products; then one partitions those products by `h=eval(u)`.
Every summand in `(D)` is a nonnegative integer.

There is a useful audit warning.  A coefficient-only test cannot distinguish
`h^{-1}g` from `g h^{-1}` in this formula: these two permutations are
`H`-conjugate because

```text
g h^(-1) = h (h^(-1)g) h^(-1),
```

and `J_N^k` is invariant under conjugation by `H`.  The displayed `S_3` word
witness and the inverse map, rather than the coefficient totals, settle the
actual fiber orientation.

## Exact-uniform sampling corollary

**Corollary (proved, conditional only on access to the named primitives).**
Suppose `Omega(N,L;g)` is nonempty and one can make the following choices
exactly:

1. draw `(k,h)` with probability

   ```text
   binom(L,k) [h]C_(N-1)^(L-k) [h^(-1)g]J_N^k
   ------------------------------------------------;
                       [g]C_N^L
   ```

2. draw `u` and `v` independently and uniformly from the two nonempty fibers
   in the theorem;
3. draw uniformly one of the `binom(L,k)` binary patterns and apply the
   inverse map above.

Then the resulting word is exactly uniform on `Omega(N,L;g)`.  Indeed, a
target word has unique data `(k,h,p,u,v)`, and cancellation of the branch,
fiber, and pattern cardinalities gives probability exactly `1/[g]C_N^L`.

This is an exact correctness reduction, not a complexity result for steps 1
and 2.

## Feasibility and boundary audit

Let `c(g)` count all cycles of `g`, including fixed points, and put
`ell_T(g)=N-c(g)`.

**Proposition (proved).**  For `N>=2`, `Omega(N,L;g)` is nonempty exactly when

```text
sign(g)=(-1)^L  and  L >= ell_T(g).                  (7)
```

To prove necessity, start from the identity, which has `N` cycles.  Right
multiplication by a transposition changes the number of cycles by exactly one,
so reaching `c(g)` takes at least `N-c(g)` steps.  The sign identity supplies
the parity condition.  For sufficiency, a cycle
`(a_1 a_2 ... a_r)` has the rightmost-first factorization

```text
(a_1 a_r)(a_1 a_(r-1)) ... (a_1 a_2),
```

and combining the disjoint cycles gives a factorization of length
`N-c(g)`.  Condition (7) says `L-(N-c(g))` is a nonnegative even integer.
Append that many factors in adjacent cancelling pairs, for example copies of
`(1 2)(1 2)`.

The requested special cases follow.

- **`N=2`.**  `A_2` is empty, `H=S_1={e}`, and only the term `k=L` survives
  in `(D)`.  Since `J_2=(1 2)`, there is one word, ending at `e` for even `L`
  and at `(1 2)` for odd `L`.  Stable sorting is the all-star identity map.
- **`L=0`.**  The empty word is the unique word and has endpoint `e`.
  Formula `(D)` is `delta_(g,e)` under `C_1^0=J_N^0=e`.
- **Odd `L`.**  Identity fibers are empty.  Arbitrary odd endpoints are
  feasible precisely when their sign is odd and their transposition length is
  at most `L`.
- **Minimal length.**  At `L=ell_T(g)` the cycle factorization above proves
  existence; no shorter word exists by the cycle-count argument.
- **Pair padding.**  For any feasible word and any transposition `tau`,
  appending `tau tau=e` raises its length by two without changing its endpoint.
- **Extreme branches.**  `k=0` and `k=L`, as well as the all-old and all-star
  patterns, use the same theorem with an empty word on the other side.

The scheduled top-level length `L_N=2N^3` is just one even identity-feasible
instance; neither the theorem nor its inverse assumes that schedule.

## Exhaustive validation and falsification attempt

**Exact finite fact.**  The standard-library script
`check_disintegration.py` ran at repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993` with Python 3.12.3 and no
nonstandard dependencies.  Exact command:

```text
/usr/bin/time -v python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r1-bijection/check_disintegration.py --min-n 2 --max-n 5 --max-length 6 --output-dir experiments/20260901-rank-recursive-identity-bridge-goal/roles/r1-bijection > experiments/20260901-rank-recursive-identity-bridge-goal/roles/r1-bijection/run.log 2>&1
```

For every `2<=N<=5`, every `0<=L<=6`, and every `g in S_N`, it compared the
direct coefficient with `(D)` using independent exact endpoint dynamic
programs.  It also enumerated the full domain

```text
(binary pattern, old word, sorted star word)
```

for each rank and length, constructed the inverse word, and checked:

- leftmost-inversion stable sorting;
- rightmost-inversion stable sorting;
- equality with closed suffix formula (3);
- both inverse round trips;
- the exact inversion count and product at every case;
- endpoint case counts against the independent full-walk DP;
- feasibility criterion (7).

The universal statements tested here would have been falsified by any failed
endpoint coefficient, any collision/missing word exposed by a round trip, any
strategy-dependent normal form, any product mismatch, or any feasibility
mismatch.  Finite validation does not prove the theorem; the proof above does.

Results:

| exact check | count | failures |
|---|---:|---:|
| rank/length cases | 28 | 0 |
| all-endpoint coefficient/feasibility cases | 1,064 | 0 |
| actual fixed-pattern bijection cases | 1,168,198 | 0 |
| adjacent rewrite steps checked | 16,219,028 | 0 |

The coefficient path uses DP rather than enumerating the `10^6` length-six
words in `S_5`; the million-scale structured enumeration is used only for the
requested actual inverse-bijection check.  Wall time was 55.50 seconds and
peak resident memory was 20,480 KiB.

Artifacts and SHA-256 digests:

```text
b65f4740d10fb73dc946df0785ce232e31fb85a37980daff1a77ecb39eb1e16d  check_disintegration.py
8bcfa513ac070a2991d89eb25b5179dd273cd13e6b7cfb8a8731caa44274e8a0  results.jsonl
ab90216da1f86e24ef69efb2b1d6c7168cbda7aa1320ad49269db7b29216a9c6  summary.json
a164f4fdea6e6d3cac12ba2e0c7a152f606f444aefc5d8c9ec695c88fe0af985  run.log
```

## Dependencies, complexity, and note audit

The proof depends only on elementary permutation multiplication, the local
conjugation identity (1), and the cycle-count characterization of
transposition length, all proved above.  It has no literature dependency and
does not use the conditional identity-Hurwitz classification or any mixing
claim.

With factors represented by their two endpoints, the adjacent forward and
inverse maps use at most `k(L-k) <= L^2/4` constant-time lower-label updates
and `O(L)` working storage.  This is polynomial word-level overhead.  It says
nothing about the bit complexity of sampling `(k,h)` or `v`, and it does not
enumerate `H` as part of the proposed algorithm.

The consolidated note's formula and its `h^{-1}g` orientation need no
correction under the convention used here.  The note should, if later edited,
state the multiplication convention and add rules (2), (3), and (5); without
them, its phrase “invert the stable-sort bijection” is correct but not yet an
implementation specification.  No durable shared file was edited in this
worker run.

role: r1-bijection
claim: For every N>=2, L>=0, g in S_N, and every old/star binary pattern, the explicit stable-sort map is a product-preserving bijection with star endpoint h^{-1}g, and summing it proves (D).
status: proved
assumptions: Permutations are maps with (alpha beta)(x)=alpha(beta(x)); group-algebra zeroth powers equal the unit; the exact-uniform corollary assumes access to exact nonempty branch and fiber samplers.
evidence: Complete elementary proof above; check_disintegration.py; results.jsonl and summary.json give 1,064 all-endpoint coefficient checks and 1,168,198 exhaustive inverse-bijection cases through N=5,L=6 with zero failures.
independent_checks: Direct endpoint DP versus old/star convolution; leftmost versus rightmost rewriting; closed suffix formula; both inverse round trips; feasibility DP; fresh coordinator audit still required by the run protocol.
complexity: Forward and inverse word maps take O(k(L-k)) <= O(L^2) constant-time endpoint updates and O(L) storage; R1 alone does not solve the R2/R3 branch or star sampling complexity.
first_unproved_step: None inside R1; at sampler level, the first remaining step is a positive polynomial-time sampler for the weighted (k,h) branch together with prescribed-endpoint star fibers.
verdict: promote
