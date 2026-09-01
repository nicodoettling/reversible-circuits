# M281 fresh immutable proof audit of M278

Date: 2026-08-14 UTC.

## 1. Verdict and exact scope

```text
ACCEPT M278 WITH ONE NONMATERIAL CONVENTION CORRECTION.
MATERIAL OBJECTIONS: NONE.
```

M278 proves the arbitrary-rank fixed-edit routes for the local old-padded/new
rooted DPS row at every `d>=5`.  This is a deterministic Hurwitz endpoint
theorem, not an every-color or global routing assembly.  The ambient sampler
target remains the global fixed-length uniform law on `Omega(N,m)` for the
lazy exact same-product `{3,4,5}` heat-bath chain.

## 2. Immutable provenance

M278's inventory digest is exactly

```text
352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad
```

and all eight payloads verify.  Every payload in each cited inventory also
verifies; independently computed inventory digests are

```text
M225 e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M228 d20259c79d993ef63f8aab8235afeb75792153be6948767a0552d84d70f12237
M231 63b6e790a86f1cfae2db971b28a46c1a173ad9c27560857ac60ce9c7ba0421db
M234 b5b5cb5f72be67efe92599a6381e23145eb34567a2ee75431ad087ba1ab903
M236 0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a
M237 d9abaf43e13c4eb9ee30815293540e58c0deb5b3744415d0c9a9caf587d8fd57
M240 2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242 49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M250 243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254 77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M269 c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M271 ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73
M273 4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550
M275 8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa
```

The locked DPS source `/tmp/DuPoSc13.pdf` verifies at
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
RandomQuad Steps 3--4 and their proof were read from that exact object.

## 3. Canonical slots and all-rank locality

DPS Proposition 3 gives, at old rank,

```text
(L_1,R_1)=(m-1,m),
(L_h,R_h)=(2h-3,2h-2), 2<=h<=d-1.
```

After extension, child `d` occupies `(m-1,m)` and the new root occupies
`(m+1,m+2)`.  The first endpoint of slot `h` is `h-1`, and its two canonical
second endpoints are `p(h)-1`; the old root slot defaults to root `d`.

The complete-interval proof is valid.  Mark the two edited degree-two black
slots.  Every intervening tree-boundary excursion is nested or disjoint
because the underlying graph is a tree.  RandomQuad's LIFO rule erases a
leafmost excursion to one side; induction erases all unmarked excursions.
Unmarked path slots are removed by the same two-row complete-node macro.
Expanding a complete node reverses only its internal distance-one rows and
cannot change a marked label's last distance-three endpoint.  The one-leaf
extension lies in the outside root component and supplies only the accepted
appended square.  At the old cyclic seam, choosing the cut after the marked
excursion makes the same argument literal.  Thus this is an arbitrary-rank
proof; the finite guard is not being used as induction.

## 4. Internal even cases

For `i=2v-2<=m-4`, put

```text
e=(v-1,p(v)-1),   f=(v,p(v+1)-1).
```

The independently contracted four skeletons give exactly

```text
p(v)=p(v+1): [e,f,fef,f];
p(v+1)=v:    [e,efe,e,f];
p(v)=v+1:    [c,e,c,f], c=fef=efe;
otherwise:   [e,f,e,f], e and f disjoint.
```

Their second-black rows are respectively

```text
(r,r,v+1,r), (r,r,r,v), (s,v,s,s), (r,s,r,s).
```

The four cases exhaust two distinct tree edges.  Since `2<=v<=d-2`, the
two slots and parent relations are inherited unchanged, all outside complete
nodes agree, and the old/new words are literally equal.

## 5. Cross-boundary and last seams

Put

```text
j=m-3, h=(d-2,p(d-1)-1), g=(0,d-1), k=(0,d),
a=ghg, b=aga.
```

The independent old/new endpoint census agrees with every M278 table entry.
When `p(d-1)=1`, the old `j,alpha,beta` labels default to root `d` and
`j+1` records `d-1`; otherwise `j,alpha` record `p(d-1)` while `j+1,beta`
default.  At new rank, `j` records `p(d-1)`, `j+1,beta` record `1`,
`alpha` records `d` or `p(d-1)`, and `gamma,delta` default to `d+1`.
Thus

```text
N=[a,b,a,g,k,k],       A=[h,g,a,g,k,k].
```

For the last edit the old `alpha,beta` labels default to `d`.  At new rank
`alpha` records `1`, `beta` defaults to `d+1`, `gamma` records `d`, and
`delta` defaults to `d+1`, hence

```text
N=[g,g,k,k],           A=[g,gkg,g,k].
```

All unshown factors agree by complete-interval locality.

## 6. Hurwitz chronology, inverse routes, and `d=5`

Chronological action gives

```text
[a,b,a] --R_j^(-1)--> [g,a,a]
        --R_j^(-1)--> [h,g,a],
[g,k]   --R_m^(-1)--> [gkg,g].
```

The first calculation uses only `b=aga`, `a=ghg`, so it remains valid when
`h,g` are disjoint and does not invoke M242's rejected generic formula.
Reverse routes are `R_j,R_j` and `R_m`.  At `d=5`, the internal edits are
`2,4`, the cross route uses two `R_5^(-1)`, and the last route uses
`R_8^(-1)` on the length-ten word.  Every slot and generator exists.

## 7. Formal composition

The adjacent edit indices partition into ordinary odd, internal even,
cross-boundary, and last families.  Accepted M269/M271 plus M273/M275,
M250/M254, and M240/M242 give every ordinary route of length

```text
4(d-v-1)+5 <= 4d-7.
```

M278 supplies fixed lengths `0,2,1`; hence the complete local rooted-row
table has maximum length `4d-7`.  This does not supply synchronized tuple
routes, every-color coverage, voltage correction, recovery, or congestion.

## 8. Independent finite guard and replay

`cleanroom_fixed_edit_check.py` imports no M278/predecessor artifact, uses
only the standard library, performs no route search, and checks exactly
`d=5,6`.  All `141` trees, `407` internal rows, `141` cross rows, and `141`
last rows pass.  Incidence counts are `8/8/8/8` at `d=5` and
`75/150/75/75` at `d=6`; seam-regime counts are `8/8` and `50/75`.
The normalized result digest is

```text
f1cafde37bee35a4f2f0bbe116f45948f6b238efc5216332df52050398a00836.
```

M278's frozen guard replayed to `/tmp` is byte-identical to its frozen result,
SHA-256 `5ef2469e0b09be4d8efa4053e09ef9056097019866591caf77ec0392f4d8f064`.

## 9. Numbered objections and exact stop

1. **Material objections:** none.
2. **N-1, nonmaterial cyclic-start convention:** M278 Section 5 states the
   last-seam distance-three execution order as `alpha` then `gamma` and the
   inverse reopening order as its reverse, but DPS permits any initial
   half-edge and M278 does not declare a cut there.  The clean checker obtains
   `alpha,gamma` under one allowed cut and `gamma,alpha` under the root-side
   cut, with identical pairings, endpoints, and factor word.  State the cut
   if row execution order is retained.  The chronological Hurwitz routes in
   Section 6 are invariant and correct.

```text
PROVED AND ACCEPTED:
  every fixed local rooted edit; formal complete local all-edit table;
  maximum local route length 4d-7.

STILL OPEN / NOT INFERRED:
  synchronized tuple routes; every-color; voltage correction;
  other routing obligations; recovery and congestion;
  spectral gap; polynomial mixing; Terminal A/B.
```

