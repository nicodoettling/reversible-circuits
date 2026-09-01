# M28 halfway checkpoint: exact shell and a polynomial H5 escape

## 1. Exact shell characterization

Use `(pq)(x)=p(q(x))`, `M=binom(N,2)`, `m=4N^3+4`, and let

```text
U={w:c(w)>=2},
F={connected y:K(x,y)>0 for some x in U},
V=U union F.
```

For a nontrivial vertex bipartition `P`, call a factor *crossing* if its
endpoints lie in different blocks.

**Lemma.**  A word `w` lies in `V` iff there are a bipartition `P` and a
contiguous interval of at most five positions containing every crossing
factor of `w` across `P`.

If `w in U`, choose a cut between support components; there are no crossing
factors.  If connected `w in F`, it differs from a disconnected predecessor
inside one `r<=5` update window, so all crossing factors across a predecessor
component cut lie in that window.

Conversely, extend the witnessing interval to length five and call its
ordered product `h`.  Products to the left and right lie in
`H_P=S_A x S_(A^c)`, and the whole word is identity, so `h in H_P`.  Its
transposition length is at most five and has odd parity.  A minimal internal
factorization of `h` has length `1,3`, or `5`; pad it by internal squares to
length five.  Replacing the window by this factorization produces a
disconnected identity word, and the exact `H_5` heat bath connects the two
words.  This proves equality, not merely inclusion.

Equivalently, `V^c` consists of words whose support remains connected after
deleting every five-position interval.

## 2. Global mass orientation

Put

```text
j=m-6=4N^3-2,       E=binom(N-1,2).
```

Every length-five witness interval is contained in a length-six interval.
Fix a bipartition with smaller block size `s`, internal-edge count

```text
e_s=M-s(N-s),        h_s=s!(N-s)!.
```

After deleting a fixed six-window, the `j` outside factors are internal to
the cut.  For each of the `M^6` possible blocks, centrality of the internal
transposition sum and Cauchy--Schwarz at even time reduce the outside count
to an identity return.  The frozen exact trace estimate gives at most

```text
4 M^6 e_s^j/h_s                                      (C.1)
```

words for this cut and window.

The cut-size sum retains the factorial weights.  Relative to the isolate
cut, write

```text
Delta_s=E-e_s=(s-1)(N-s-1).
```

Then

```text
sum_P e(P)^j/h(P)
 <=[E^j/(N-1)!] sum_{s<=N/2}
      [binom(N,s)^2/N] exp[-j Delta_s/E]
 <=2N E^j/(N-1)!.                                    (C.2)
```

The `s=1` term is exactly `N`.  For `s>=2`, `j/E>=8N`,
`N-s-1>=N/4`, and `binom(N,s)<=N^s`, so each normalized term is at most
`exp[-N^2(s-1)]`; their sum is less than one.

There are `m-5` length-six windows.  Hence

```text
|V|<=8N(m-5)M^6 E^j/(N-1)!.                          (C.3)
```

The even bridge satisfies `|Omega(N,m)|>=2M^m/N!`, while `E/M=(N-2)/N`.
Thus

```text
pi(V)
 <=4N^2(m-5)(1-2/N)^j
 <=exp(-5N^2)<1/2.                                   (C.4)
```

This is the exact global orientation needed for conductance.

## 3. Many deletion-robust endpoint tails

Let `d=N-1`, still write `E=binom(d,2)`, and put `k=m-5=j+1`.  Fix the
transposition `q=(2,3)` on `[d]`.  Fourier inversion for the nonlazy uniform
transposition walk gives, at the parity-compatible odd endpoint,

```text
#{u in T_d^k:product(u)=q}>=(15/8)E^k/d!.             (C.5)
```

Indeed the trivial and sign representations contribute `2/d!`.  Every other
character ratio has absolute value at most `1-2/(d-1)`, and

```text
exp[-2k/(d-1)]<=1/(8d!)                               (C.6)
```

for `N>=5`.

Call a tail robust if deleting any five consecutive factors leaves connected
support on `[d]`.  A nonrobust tail has a vertex cut whose crossing factors
are confined to one five-window.  For each fixed cut/window, choose the five
window factors in at most `E^5` ways and bound the remaining internal words
crudely by `e_P^(k-5)`; this deliberately discards the endpoint constraint and
does not commute an arbitrary odd block through the cut subgroup.  A union
over at most `2^d` cuts shows that the nonrobust fraction is at most

```text
3k 2^d d! exp[-2(k-5)/d]<exp(-4N^2)<1/2.             (C.7)
```

For the last estimate, the logarithm of the prefactor is at most `3N^2`,
whereas `2(k-5)/d>=7N^2`.  Consequently the number `R` of robust `q`-tails
satisfies

```text
R>=(15/16)E^k/(N-1)!.                                 (C.8)
```

## 4. One actual H5 transition from the shell to its complement

Let `z=N`, `s=(z,1)`, and use the fixed prefix

```text
(s,q,q,q,s).                                          (C.9)
```

Since `s` and `q` are disjoint, this prefix has product `q`.  Append any
robust tail `u=(b_1,...,b_k)` of product `q`; the resulting word has product
identity.  Its only edges incident to `z` occur at positions one and five,
so it lies in `F subset V`.

Update positions five through nine.  Four right Hurwitz swaps replace

```text
(s,b_1,b_2,b_3,b_4)
```

by

```text
(b_1,b_2,b_3,b_4,g^{-1}s g),
g=b_1b_2b_3b_4.                                      (C.10)
```

The ordered product is unchanged.  Because every `b_i` fixes `z`, the last
factor in (C.10) is another edge incident to `z`.  The target therefore has
its two `z`-edges at positions one and nine.  No five-window deletes both,
and robustness of the tail keeps the other `N-1` labels connected after any
five-window deletion.  By the exact characterization, the target lies in
`V^c`.

A length-five product fiber has size at most `M^4`, so the specified full-K
transition has probability at least

```text
p=1/[6(m-4)M^4].                                      (C.11)
```

Combining (C.3), (C.8), and (C.11), with the orientation (C.4), gives

```text
Phi_pm^K(V)
 >=15E/[768N(m-5)(m-4)M^10]
 >=1/(4N^25).                                         (C.12)
```

The complete flow is `Q_K=Q_3+Q_4+Q_5`; (C.12) retains only the specified
subset of `Q_5`.  Every other transition is a nonnegative addition.

## Current conclusion

The shell is proper, globally very small, and polynomially leaky.  The next
candidate closure must contain at least the full deletion-robust targets
constructed above; a second-radius neighborhood alone is not yet analyzed.
