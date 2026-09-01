# Independent referee: M09 surjective-support zipper lemma

## Frozen claim

For every finite group `G`, finite set `E`, surjection `p:E->G`, `l>=2`, and
`h in G`, let `Omega_h` be the uniform fiber of `E^l` with ordered image
product `h`.  Let `B_h` choose one of the `l-1` adjacent coordinate pairs
uniformly and heat-bath that pair uniformly conditional on its ordered image
product.  With the Poincare convention `gap=1-lambda_2`, the frozen claim is

```text
gap(B_h) >= 1/(l^3 |E|^3).
```

## Audit

### 1. Path legality and noncommutative invariant

At stage `i`, the current image word is

```text
y_1 ... y_(i-1) d_i x_(i+1) ... x_l = h.
```

The proposed defect

```text
d_(i+1)=y_i^{-1} d_i x_(i+1)
```

satisfies `y_i d_(i+1)=d_i x_(i+1)` with no commutation.  Surjectivity supplies
`c(d_(i+1)) in E`, so the stage update is in the exact two-coordinate
conditional fiber.  Left cancellation of the common prefix at the last stage
gives `d_(l-1)x_l=y_(l-1)y_l`.  Thus every intermediate word has endpoint
`h`, and the path has at most `l-1` nontrivial directed edges.

### 2. Complement formula

Put `a=x_1...x_(i-1)` and `b=y_(i+1)...y_l`.  The proposed complement image

```text
e_i=a^{-1} h b^{-1}
```

is in the correct noncommutative order because

```text
a e_i b = a(a^{-1} h b^{-1})b = h.
```

Hence
`(X_1,...,X_(i-1),c(e_i),Y_(i+1),...,Y_l)` really is in `Omega_h`.

### 3. Injective recovery, including repeated fibers

Fix a directed used edge and the stage index `i`.  Its tail and head jointly
give `Y_1,...,Y_i` and `X_(i+1),...,X_l`, also at the final stage.  The
complementary word gives `X_1,...,X_(i-1)` and
`Y_(i+1),...,Y_l`; the extra datum `X_i in E` completes the source.  Thus all
microstates of both `(x,y)` are recovered, not merely their images under `p`.
Multiple elements of `E` with the same image, duplicate canonical outputs,
and collisions between selected adjacent positions therefore do not break
the injection.  There are at most

```text
|Omega_h| (l-1)|E| <= |Omega_h| l|E|
```

data values per fixed directed edge.  The stage index also separates a path
which might encounter the same state-edge at different zipper positions.

### 4. Capacity and comparison normalization

For a selected adjacent position, the conditional two-coordinate fiber has
size at most `|E|^2`.  If a directed transition is supported at that position,
then, with `S=|Omega_h|`, its contribution to stationary directed capacity is

```text
Q_B(u,v) >= 1/[S(l-1)|E|^2].
```

If the same state transition is produced by several adjacent choices, their
probabilities aggregate, so this remains a valid lower bound.  Self-loops
have zero Dirichlet contribution and may be omitted.

The whole-fiber heat bath has directed flow `S^-2`, Poincare gap one, and
Dirichlet form exactly `Var_pi`.  For a fixed directed zipper edge, injective
recovery bounds the number of charged ordered source-target pairs by
`Sl|E|`; Cauchy--Schwarz contributes path length at most `l`.  Its comparison
load is therefore at most

```text
(Sl|E|) S^-2 l = l^2|E|/S.
```

Dividing by capacity gives

```text
l^2(l-1)|E|^3 <= l^3|E|^3.
```

The standard directed-flow comparison consequently proves the frozen gap
bound.  No missing factor two occurs: both Dirichlet forms carry the same
`1/2` over ordered pairs.  Although `B_h` is presented without added
laziness, it is an average of conditional-expectation projections, hence is
positive semidefinite; in any event the claimed Poincare gap concerns
`1-lambda_2`, not an absolute eigenvalue gap.

### 5. Project specialization and boundaries

- For `N=3,4`, products of two transpositions give respectively every
  element of `A_3` and `A_4` (identity, 3-cycles, and for `N=4` the double
  transpositions).  Thus `E=T_N^2`, `G=A_N`, `|E|=M^2` gives
  `gap>=1/(l^3M^6)` for every feasible endpoint.
- At `l=2`, the sole adjacent-pair update is the whole-fiber heat bath, so the
  bound is conservative.
- For `N>=5`, two transpositions do not cover `A_N`; the proof correctly stops
  because either zipper defect can lie outside `p(E)`.  The lemma makes no
  claim there.

## Objections

None.  Two presentation clarifications are advisable but nonblocking:

1. State explicitly that `gap` is the Poincare gap `1-lambda_2`.
2. In the recovery paragraph, say that the *tail and head jointly*, together
   with `i`, reveal the target prefix and source suffix.

## Verdict

**ACCEPT.**

