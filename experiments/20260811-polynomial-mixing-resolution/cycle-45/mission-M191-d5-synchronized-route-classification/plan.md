# M191 plan: exact d=5 synchronized-route classification

## Objective

Classify synchronized signed-Hurwitz quotient-component membership for all 54
named `d=5`, width-two target tuples independently reconstructed and accepted
append-only by M188. This is a clean replacement mission, not an amendment to
M187.

## Scope and conventions

Let `m=8`, `Z_5` be the connected product-one transposition words of length
eight, and `Q_5=Z_5/S_5`. The fixed source tuple is

```text
V=(01)^2(02)^2(13)^2(04)^2,
U=(01)^2(02)^2(03)^2(04)^2.
```

Permutations compose as `(p q)(x)=p(q(x))`. Signed right-Hurwitz symbols act
chronologically. The theorem target is exact finite component membership for
the 54 named targets only. There is no probability distribution or Markov
kernel in this structural mission.

## Immutable and exclusion gate

Verify M181/M183 and M188 manifests before use. Treat their accepted results
as immutable. M187's superseded geometric all-`d` claims are explicitly
excluded; only M188's independently reconstructed finite target list may
inform the computation.

## Exact route

1. Independently construct `Q_5` and the signed-generator action, with exact
   cardinality and bijectivity checks.
2. Build a Schreier tree from the first source quotient `V`.
3. Generate its action stabilizer by literal Schreier words. Apply those words
   to the second source `U` to obtain the exact stabilizer orbit.
4. For each target `(v',u')`, use the stored tree transporter for `v'` to
   reduce diagonal membership to stabilizer-orbit membership of the adjusted
   second coordinate.
5. Archive a chronological braid word for every positive target. For every
   negative target, archive its adjusted second-coordinate ID and the exact
   finite stabilizer-orbit complement certificate.
6. Replay every positive word and independently check all negative
   certificates. No radius cutoff decides membership.

## Resource cap and falsifiers

Enumerating the single exact `Q_5` quotient (expected size 8,400) and one
stabilizer orbit is allowed. Do not enumerate the full Cartesian quotient or
use a radius-limited pair BFS. Use Magma only if the exact Python
Schreier computation becomes infeasible.

## Deliverables

Write a halfway checkpoint, proof/classification note, compact checker and
machine-readable certificates, nine-field report with ACCEPT/REJECT/
INCONCLUSIVE, freeze manifest, and hashes. No all-`d`, every-color, polynomial
length, gap, mixing, or Terminal inference.
