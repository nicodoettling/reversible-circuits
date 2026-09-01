# M309 fresh proof audit of frozen M306

Date: 2026-08-14 UTC.

## Verdict

```text
FINAL VERDICT: ACCEPT M306 AT ITS STATED NONTERMINAL SCOPE.
```

## 1. RCOM identity and implication

Fix an actual matching `M`, a nonempty `U subset M`, and an anchor `P in U`.
Transitivity of the accepted finite action makes every endpoint fiber have
the common nonzero size `k_d=|A_d|/|Z_d|`.  With

```text
r_U(a)=|{Q in U:a in K_Q}|,
```

finite double counting gives

```text
sum_(a in K_P) r_U(a)
 =sum_(a in K_P)sum_(Q in U)1[a in K_Q]
 =sum_(Q in U)|K_P intersect K_Q|.
```

Division by `|K_P|=k_d` is exactly the conditional expectation of `r_U`
under the uniform law on `K_P`.  An average is no greater than
`max_a r_U(a)`, so an RCOM lower bound of `|U|/d^C` produces an action with
that agreement and proves `RCOM => MRAD` with the same exponent.  No Helly
step occurs.

Summing over anchors also gives

```text
sum_(P,Q in U)|K_P intersect K_Q|=sum_a r_U(a)^2,
sum_a r_U(a)=|U|k_d,
```

so M306's size-biased second-moment normalization is exact.

## 2. WRAD and the fractional-cover LP

Let `B_(Q,a)=1[a in K_Q]`.  M306's fractional cover is the finite primal

```text
min 1^T x  subject to Bx>=1, x>=0.
```

Its exact dual is

```text
max 1^T lambda  subject to B^T lambda<=1, lambda>=0,
```

and `(B^T lambda)_a=W_lambda(a)`.  The primal is feasible because all
fibers are nonempty, and it is bounded below.  Thus finite strong LP duality
applies.  Scaling a nonzero weight vector by `max_a W_lambda(a)` is safe:
that maximum is positive because some positive-weight edge has a nonempty
fiber.  The zero vector is trivial.  Consequently

```text
tau*(M)<=q
iff for every lambda>=0 some a has
    W_lambda(a)>=||lambda||_1/q.
```

There is no missing edge constraint or action variable.

## 3. Exact harmonic MRAD--WRAD comparison

`WRAD_q => MRAD_q` follows by taking `lambda=1_U`.  Conversely assume every
nonempty residual set has agreement at least `1/q`.  For nonzero weights,
sort `lambda_1>=...>=lambda_N` and put

```text
B=max_j j lambda_j.
```

Then `lambda_j<=B/j`, hence `||lambda||_1<=BH_N`.  At a maximizing `j`,
MRAD on the top `j` edges yields one action covering at least `j/q` of them,
each of weight at least `lambda_j`.  Therefore

```text
W_lambda(a)>=j lambda_j/q=B/q
             >=||lambda||_1/(qH_N).
```

This proves `MRAD_q => WRAD_(qH_N)`.  Zero weights again are immediate.
The reverse implication loses no factor.

For the accepted matching cardinality

```text
N=|M|=d^(d-3)(2d-2)!/d!,
```

one has `H_N<=1+ln N` and

```text
ln N=(d-3)ln d+sum_(t=d+1)^(2d-2)ln t=O(d ln d).
```

Thus the harmonic loss is polynomial, as stated.  The exact LP equivalence
and these two implications establish polynomial equivalence among MRAD,
WRAD, and fractional action-cover size; they do not establish any one of
those properties for the actual family.

## 4. Symmetric/alternating score-two obstruction

For the identity matching on an `N`-point natural action, the identity lies
in every point-fixing fiber `K_x`, so the integral cover has size one and
MRAD density is one.  The fractional optimum is also exactly one: assigning
weight one to the identity is feasible, while any one fiber constraint
forces the total nonnegative weight to be at least one.

For `Sym(N)`,

```text
|K_x|=(N-1)!,  |K_x intersect K_y|=(N-2)!  (x!=y).
```

For `Alt(N)` and `N>=4`, the respective sizes are `(N-1)!/2` and
`(N-2)!/2`; the `N=4` two-point stabilizer has size one, exactly as the
formula states.  Hence every full-family anchored score equals

```text
1+(N-1)/(N-1)=2.
```

On a subset of size `s` containing the anchor it is
`1+(s-1)/(N-1)<=2`, although the identity covers all `s` constraints.
The optional factorial-moment statement is also correct: a prescribed
ordered `j`-tuple is fixed with probability `1/(N)_j` in `Sym(N)`, and in
`Alt(N)` while at least two points remain, i.e. `j<=N-2`.

Taking the degree to be the accepted
`N_d=d^(d-3)(2d-2)!/d!` gives `N_d>=d^(d-3)`.  For every fixed exponent
`C`, therefore, `2<N_d/d^C` for all sufficiently large `d`.  This supplies
an abstract family with an exact one-action cover but no polynomial RCOM
bound on the full family.  It refutes generic `MRAD => RCOM`; it neither
realizes nor refutes RCOM in the actual M135 action.

## 5. Finite guard and stopping lines

The sole no-import replay confirms the actual `d=3` witness: fiber sizes
nine, three singleton pair intersections, empty triple intersection, RCOM
score `11/9` at every anchor, and maximum agreement exactly two.  It also
confirms that complete-matching MT2H has a false premise throughout this
guard.  No Helly or all-rank inference is available.

The actual theorem starts at `d>=6`.  M306 correctly leaves actual RCOM,
WRAD, and MRAD unresolved there.  It also preserves M296/M299's separate
literal-length obligation: finite-action nonemptiness does not control the
shortest signed braid representative.

## 6. Numbered objections and freeze

1. **Material objections:** none.
2. **Nonmaterial objections:** none.

Accepted content is limited to the exact conditional identities and
implication, the LP duality and harmonic polynomial equivalence, the
abstract score-two obstruction, and the exact finite guard.  There is no
inference to actual MRAD, SSTID, routing, voltage correction, congestion, a
spectral gap, mixing, or Terminal.

