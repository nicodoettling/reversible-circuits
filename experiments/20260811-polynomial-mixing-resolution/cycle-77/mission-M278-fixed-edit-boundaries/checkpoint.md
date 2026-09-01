# M278 checkpoint

## CP-0 — initialization

- Mission directory initialized before substantive work.
- Project skill read in full.
- Ambient target remains the global fixed-length uniform identity-word law
  for the lazy exact same-product `{3,4,5}` heat-bath chain; this mission is
  only a deterministic DPS/Hurwitz boundary calculation.
- Next: verify the immutable gate and extract the exact fixed-edit claims and
  tuple identities before deriving any boundary formula.

## CP-1 — immutable gate verified

All payload files named by each frozen inventory verify, and the top-level
`SHA256SUMS` digests are:

```text
M225 e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd
M228 d20259c79d993ef63f8aab8235afeb75792153be6948767a0552d84d70f12237
M231 63b6e790a86f1cfae2db971b28a46c1a173ad9c27560857ac60ce9c7ba0421db
M234 b5b5cb5f72be67efe92599a6381e23145eb34567a2ee75431ad087ba1ab903
M236 0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a
M237 d9abaf43e13c4eb9ee30815293540e58c0deb5b3744415d0c9a9caf587d8fd57
M240 2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242 49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663
M269 c36c8fd777808d6664b30525dda2e5f562dd41d57e288d391bf6154d803606eb
M271 ed22acab046adcc2af8960fd9690e1cb7e2bb20f5f337bb0fece53b64b7b1d73
M273 4413c0f077009a07bced6addb014c76741a47059b2ba78b0cb7e8803e6f5c550
M275 8f138666682868cb08a072d0be0ecc331eb1adb7e092f5bf4dcd6917db1932aa
DPS  98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2
```

The locked DPS source is `/tmp/DuPoSc13.pdf`.  Its RandomQuad Steps 3--4
give the LIFO local closure and final-root completion used below.

## CP-2 — analytic fixed-edit formulas frozen before any guard

Date: 2026-08-14 UTC.  Put `m=2d-2`,

```text
alpha=m-1, beta=m, gamma=m+1, delta=m+2,
g=(0,d-1), k=(0,d).
```

Hurwitz actions are chronological from left to right:

```text
R_j[x,y]=[y,yxy],       R_j^(-1)[x,y]=[xyx,x].
```

For the cross-boundary edit `i=m-2`, put

```text
h=(d-2,p(d-1)-1),  a=ghg,  b=aga,  j=m-3.
```

All unshown factors agree, and the exact old-padded source/new target at
positions `j,j+1,j+2,beta,gamma,delta` is

```text
N: [a,b,a,g,k,k]
A: [h,g,a,g,k,k].                                      (CP2.1)
```

The literal chronological calculation is

```text
[a,b,a] --R_j^(-1)--> [aba,a,a]=[g,a,a]
        --R_j^(-1)--> [gag,g,a]=[h,g,a].               (CP2.2)
```

This is unconditional because `b=aga` and `a=ghg`; it does not use the
false disjoint-transposition simplification rejected by M242.  If
`p(d-1)=1`, then `h` meets `g` and the move is nontrivial.  Otherwise
`h` and `g` are disjoint, `a=h,b=g`, and the two inverse moves return
the same triple.

For the last edit `i=m-1`, all unshown factors agree and

```text
N_(alpha,beta,gamma,delta)=[g,g,k,k],
A_(alpha,beta,gamma,delta)=[g,gkg,g,k].                (CP2.3)
```

Thus the single generator is at position `beta=m`:

```text
[g,k] --R_beta^(-1)--> [gkg,g].                        (CP2.4)
```

For an internal even edit `i=2v-2<=m-4`, set

```text
e=(v-1,p(v)-1),  f=(v,p(v+1)-1),
q=(i-1,i,i+1,i+2).
```

The old and new four-factor windows are literally equal to `D_v`, where

```text
p(v)=p(v+1): D_v=[e,f,fef,f];
p(v+1)=v:    D_v=[e,efe,e,f];
p(v)=v+1:    D_v=[c,e,c,f], c=fef=efe;
otherwise:   D_v=[e,f,e,f]  (e and f are disjoint).    (CP2.5)
```

These are the four exhaustive incidences of two distinct tree edges.  The
extension changes only `p(1)` and here `2<=v<=d-2`, so the same case and
same literal factors occur at both ranks.  Hence the route is identity.

Equations `(CP2.1)--(CP2.5)` are now frozen.  No `d=5,6` guard has yet
been written or run.  The full local-erasure proof and every root/new-child
and post-wrap endpoint row will be recorded next.

## CP-3 — guard predeclaration

The analytic theorem is fixed in `fixed_edit_boundary_theorem.md`.  The
allowed guard will:

1. import only the Python standard library and no predecessor code or data;
2. enumerate exactly the `4^2=16` root-leaf templates at `d=5` and the
   `5^3=125` templates at `d=6`;
3. reconstruct the DPS trace, LIFO distance-one/distance-three closure, and
   final-root completion directly from RandomQuad Steps 3--4;
4. test only the fixed edits `i=2,4,...,2d-6`, `2d-4`, and `2d-3`;
5. assert every literal window in `(CP2.1)--(CP2.5)`, equality of every
   unshown factor, and the stated chronological signed-Hurwitz replay; and
6. record the four internal incidence counts and the two
   `p(d-1)=1`/not-`1` boundary counts.

No route search, quotient enumeration, result-dependent formula selection,
or rank above `6` is allowed.

## CP-4 — guard complete

Command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M278-fixed-edit-boundaries/guard.py
```

Python `3.12.3`; verdict `PASS`.

```text
d=5: 16 trees, 32 internal rows, 16 cross-boundary rows, 16 last rows;
     internal incidence counts 8/8/8/8;
     p(d-1)=1/not-1 boundary counts 8/8.
d=6: 125 trees, 375 internal rows, 125 cross-boundary rows, 125 last rows;
     internal incidence counts common 75, disjoint 150,
     next-child 75, previous-child 75;
     p(d-1)=1/not-1 boundary counts 50/75.
```

Totals are `141` trees, `407` internal rows, `141` cross-boundary
rows, and `141` last-edit rows.  Every endpoint table, unshown-factor
equality, frozen tuple, and chronological signed route passed.  This remains
a post-proof falsifier and is not the all-rank proof.
