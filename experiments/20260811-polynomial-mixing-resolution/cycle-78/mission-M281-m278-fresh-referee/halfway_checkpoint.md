# M281 halfway checkpoint

Date: 2026-08-14 UTC.

The immutable gate and independent all-rank reconstruction are complete.
Before opening M278's theorem/checker/results/report, the audit fixed:

```text
internal i=2v-2<=m-4 : identical four-case window, empty route;
cross i=m-2          : [a,b,a,g,k,k] -> [h,g,a,g,k,k]
                        by (R_(m-3)^(-1))^2;
last i=m-1           : [g,g,k,k] -> [g,gkg,g,k]
                        by R_m^(-1).
```

The canonical-slot lemma, complete-interval LIFO erasure, both
`p(d-1)=1`/not-`1` endpoint/default tables, inverse routes, `d=5`, and the
formal local all-edit length bound `4d-7` are recorded in
`independent_reconstruction.md`.

Line comparison with frozen M278 finds no material mathematical discrepancy.
One nonmaterial convention issue remains: the execution order of the two
last-seam distance-three closures rotates with RandomQuad's allowed starting
half-edge, while M278 states one order without fixing the cut.  Their pairing,
endpoints, source/target word, and Hurwitz route are invariant.

Next: finish the independent `d=5,6` falsifier, replay M278's guard only to
`/tmp`, and freeze the referee disposition.

