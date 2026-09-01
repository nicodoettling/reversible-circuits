# M250 checkpoint

Status: **final theorem and strict reduction written; freeze in progress**.

## Locks and accepted input

- Mission directory was initialized before substantive proof work.
- M240/M242, M244, M247, and the locked DPS source have been read. The source
  PDF at `/tmp/m244-DuPoSc13.pdf` has the required digest
  `98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.
- Only M244 Theorem 3.1 is accepted from the rejected M244 package: canonical
  unedited colored one-open pruning. Frozen RSMI is not used.

## Literal metric recurrence fixed before finite checking

Write `S` for an actual surviving tree/closure side. DPS local closure is

```text
W^q S^e B_b^q -> S,      e in {1,3},
```

and records black endpoint `x_b` exactly when `e=3`.

The metric strengthening of M244's canonical pruning has the candidate exact
normal form

```text
E_a  ->  S W^{R_a} S S.                              (CMR-0)
```

For a canonical child `c` of `a`, put `q=R_c=L_c+1`. Once the suffix after
that child has reduced to one side, its two slot-label rows are literally

```text
W^q     S S S B_a^q     -> S,                       (CMR-1)
W^{q-1} S S S B_a^{q-1} -> S,                       (CMR-2)
```

and hence both faces record second endpoint `x_a`. Every ordinary label
between child blocks has row

```text
W^t S B_a^t -> S.                                   (CMR-3)
```

Processing children in reverse increasing `R_c` order leaves one reduced
suffix side; the initial parent side, survivor `W^{R_a}`, reduced suffix,
and final parent side give (CMR-0). This is a literal side-token recurrence,
not a color-count inference. It is the current proved-candidate induction to
line-audit; no finite row is used to derive it.

For the retained stopped path the candidate state is `O` (the reversed slot's
metric defect remains exposed) or `C` (sealed). Its exact transition table is:

```text
initial reversed x_v                         -> O
path step v>a and each later step a>b        O -> O
first path vertex a>v                        O -> C
first internal ascent a<b                    O -> C
larger direct child r>v,p(r)=v in state O    two root-open slot faces
canonical nonchild sector                    CMR-0..3, state unchanged
root in state C                              literal padded equality
root in state O                              exact IDL-d four-block
```

Here “root-open” means no distance-three partner before the final root black,
so the second endpoint is `x_d` at old rank and `x_(d+1)` after extension.
The same root-open assertion applies to the edited coordinate `2v-2`.
This table is now the object to falsify/prove; it is not yet a theorem.

## Predeclared tiny falsifier (four rows only)

Before attempting the stopped-path induction, test exactly these hand-picked
rank-seven rows and no census:

1. open multi-level path `4>3>2>1`, with direct child `5->4` and common
   nonchild `6->3`;
2. open empty-scan row `v=6`, path `6>1`;
3. closed late row `4->6->1`, retaining direct child `5->4`;
4. closed internal-ascent row `5->3->4->2->1`, retaining direct child `6->5`.

Each row checks the whole RSMI+ factor package: initial endpoint, open-only
larger child, common nonchild endpoint/disjointness, closed equality, open
four-block, and unnamed-coordinate equality as applicable. Passing is exact
finite calibration only; the first failure will freeze a counterexample.

The four predeclared rows were run twice deterministically. All four passed
all applicable repaired clauses, with zero failures and normalized row digest

~~~text
d285b53ae1646d9ab241c17f51c92a55d563ad5de2095d9f77dfdfc133e59c59.
~~~

This is finite calibration only.

Theorem 3.1+ in 'metric_pruning_root_seam_reduction.md' proves the literal
metric residual 'S W^(R_a) S S' and both distance-three child rows. Corollary
3.2 proves the open common-nonchild 'h_r^2' endpoint and disjointness. The
remaining edited/direct-child/sealed/root/unnamed package is isolated as the
exact Root-Seam Path Transducer (RSPT), equations (4.1)--(4.5), and remains
unresolved. Conditional coordinate exhaustion from RSPT to IDL is explicit.

Rejected M244 RSMI is not used. No IDL or downstream result is claimed.
