# Exact finite contour-compression theorem

Date: 2026-08-13 UTC. Status: **proved for the complete `d=6 -> 7`
ordinary odd-edit template only**.

## Symbolic literal-word lemma

For an ordinary odd edit `i=2v-3`, let `lambda` be the late-ancestor bit,
`alpha` the internal-path-ascent bit, and `epsilon` the full larger-child sign
vector. Define

```text
Z_2(T,v)=("closed",)                    if lambda OR alpha,
         ("open",v,epsilon)             otherwise.
```

For the frozen Candidate-B formula

```text
W_B(T,v)=identity                                  if lambda OR alpha,
         Q(v,epsilon) B_d Q(v,epsilon)^-1          otherwise,
```

`Z_2` is a complete invariant of the literal assigned word at fixed `d`:

```text
Z_2(T,v)=Z_2(T',v')  iff  W_B(T,v)=W_B(T',v')
```

for descriptor values that occur in the declared formula.

### Proof

The forward-exception bit, full stopped path, and off-path child lists do not
appear in `W_B`. The path affects the word only through
`lambda OR alpha`; the child vector affects it only through `epsilon`. Hence
equal `Z_2` gives equal literal words.

Conversely, identity is the unique word of length zero. An open word for
`L=d-v-1` has literal length `4L+5`, so open words at distinct `v` have
distinct lengths. At fixed `v`, distinct sign vectors differ at a first
transport pair and therefore give different signed-generator sequences.
Thus equal literal words give equal `Z_2`. This is a statement about the
declared word syntax; it does not prove endpoint correctness.

## Exact finite endpoint theorem

Let `T` range over all 125 trees on `[6]` in which root 6 is a leaf adjacent
to 1, and let `i` range over ordinary odd edits `{1,3,5,7}`. Under
chronological right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a),
```

the word assigned by `Z_2` sends

```text
N_(T,i)=F_6(T,s_i pi_6)(06)^2
```

exactly to

```text
A_(T,i)=F_7(T+{{1,7}},s_i pi_7)
```

for all 500 pairs `(T,i)`.

The full frozen `D_B` partition has 101 classes at each edit and 404 globally.
The readable quotient

```text
Z_1=(v,lambda,alpha,epsilon)
```

has respectively `12,7,6,2` classes, 27 globally. The route-normal `Z_2` has
respectively `6,4,3,2` classes and 12 globally. All classes of both quotients
are word-homogeneous and endpoint-correct.

The 12 `Z_2` classes are in bijection with the 12 occurring odd formula
words: one identity class and 11 open carrier classes. Internal even edits
reuse identity, while edits 8 and 9 add two fixed nonidentity words, recovering
the frozen 14-word full-table count.

## Exact class census

The single closed class contains 193 rows. The open classes are

```text
v=2: epsilon = --- , --+ , -+- , +-- , +-+ ; sizes 1,3,11,11,24
v=3: epsilon = --  , -+  , +-             ; sizes 5,14,46
v=4: epsilon = -   , +                    ; sizes 24,60
v=5: epsilon = empty                      ; size 108
```

Equivalently, the per-edit closed sizes are `75,60,41,17`. No
same-quotient different-word or pass/failure collision exists.

## Proof certificate

`contour_compression_check.py` has no input files. It independently:

1. verifies the five-move carrier on all 840 ordered distinct-symbol choices
   and the sign automaton on 21 initial-run cases;
2. constructs the complete 125-tree template in two Prüfer-equivalent ways;
3. computes `D_B`, `Z_1`, `Z_2`, and the formula word before constructing
   either endpoint;
4. builds all 500 endpoints by a DPS boundary rotation/closure algorithm,
   verifies identity products, and replays every signed generator;
5. groups rows by both quotients and checks literal route and pass/failure
   homogeneity.

The exact normalized digests are

```text
500 rows    43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3
Z_1 classes 50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2
Z_2 classes fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512
```

Consecutive runs reproduce the result artifact byte-for-byte.

## First unproved step and strict boundary

The remaining proof obligation is an all-rank DPS closure lemma showing that
`lambda OR alpha` and `epsilon` suffice for endpoint correction under every
one-leaf extension. The symbolic factorization alone proves only which word
the formula assigns, not that the formula is correct.

Accordingly, this theorem gives an exact finite descriptor reduction, not an
all-`d` invariant. It proves no every-color or arbitrary-representative route,
voltage-corrected or total length bound, spectral gap, mixing statement, or
Terminal claim.
