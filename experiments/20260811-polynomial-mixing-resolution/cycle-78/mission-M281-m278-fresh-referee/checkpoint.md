# M281 checkpoint

Date: 2026-08-14 UTC.

Status: substantive audit and clean-room guard complete; final referee
artifacts are being frozen.

The immutable referee scope was fixed in `plan.md` before any substantive
inspection.  `HANDOFF.md`, `GOAL_SPEC.md`, the project skill, its
`sampling-problem.md` and `experiments.md` references, and the relevant
problem/theory/graph manuscript sections have now been read completely.

## CP-1 — immutable source gate

M278's `SHA256SUMS` digest is exactly

```text
352834e6752233b90b04f4c4205ff141208a3781ac458e7f2bf14c119c6014ad
```

and all eight named payloads verify.  Before reading its theorem, checker, or
results, the following predecessor inventories were independently verified,
including every named payload:

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

The locked `/tmp/DuPoSc13.pdf` digest is exactly
`98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
Its RandomQuad Steps 3--4 and surrounding proof were extracted and read from
that verified object.  They state literal LIFO closure of consecutive equal-
label white/black half-edges at distance one or three, followed after a full
outer-face turn by matching the remaining `m` white half-edges to a new black
root vertex in stack order.

The independent reconstruction was then fixed in
`independent_reconstruction.md` before M278's theorem, checker, result, or
report was opened.

## CP-2 — independent analytic result

The canonical-slot map and complete-interval LIFO erasure yield exactly:

```text
i=2v-2<=m-4 : the same four-factor incidence window at both ranks;
i=m-2       : [a,b,a,g,k,k] -> [h,g,a,g,k,k]
                by two R_(m-3)^(-1) moves;
i=m-1       : [g,g,k,k] -> [g,gkg,g,k]
                by R_m^(-1).
```

Every cross-boundary first/second endpoint and final-root default was derived
in both regimes, all four internal incidence cases were exhausted, and the
inverse routes, unchanged factors, minimal `d=5` boundary, adjacent-edit
partition, and formal local maximum `4d-7` were checked.  No synchronized,
every-color, voltage, congestion, gap, mixing, or Terminal claim was inferred.

## CP-3 — frozen M278 comparison and finite guard

M278 agrees with every invariant endpoint, factor, sign, route, and length
claim.  Material objections: none.  One nonmaterial convention omission is
retained: its Section 5 names the order `alpha` then `gamma` for the two
last-seam distance-three rows but does not fix RandomQuad's permitted cyclic
start.  A second allowed root-side cut gives `gamma` then `alpha`; the
pairings/endpoints and Hurwitz chronology do not change.

The stdlib-only `cleanroom_fixed_edit_check.py` imports no M278 or predecessor
artifact, performs no route search, and checks only `d=5,6`.  All `141`
trees, `407` internal rows, `141` cross rows, and `141` last rows pass.  Its
four incidence counts and two seam-regime counts match M278 exactly.  It also
retains both allowed cyclic-cut orders with identical endpoint words.  The
normalized rank digest is

```text
f1cafde37bee35a4f2f0bbe116f45948f6b238efc5216332df52050398a00836.
```

M278's frozen guard was replayed to `/tmp`; the output is byte-identical to
the frozen result and has SHA-256
`5ef2469e0b09be4d8efa4053e09ef9056097019866591caf77ec0392f4d8f064`.

Provisional final disposition: **ACCEPT M278 WITH ONE NONMATERIAL CONVENTION
CORRECTION.**
