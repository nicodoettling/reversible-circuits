# M225 halfway checkpoint: full child-contour candidate survives finite rank six

Date: 2026-08-13 UTC.

## Source lock and analytic-first stage

Every frozen payload in M214/M218 and M220/M223 passed its checksum inventory,
and all four top inventory digests match `immutable_gate.md`.  Before any
M225 endpoint replay, `candidate_descriptors.md` fixed exactly two nested
candidates and `symbolic_transport.md` derived the chronological five-move
carrier identity.  No third candidate is permitted.

Candidate A records the entire ordered larger-child bit vector and drives a
local sign automaton.  Candidate B was predeclared as a strict refinement:
it additionally records the whole stopped root path and every off-path child
incidence on that path, and assigns identity precisely to late-ancestor or
internal-contour-ascent cases.

## Complete finite outcome

The deterministic checker reconstructs the full 125-tree root-leaf template
at `d=6`, all nine edits, and all 1,125 endpoint pairs.  It performs no route
search, quotient enumeration, or predecessor import/data read.

```text
candidate   passes   failures   failures by edit
A             1109         16   edit 7 only
B             1125          0   none
```

Candidate A repairs all eleven edit-1 failures of M220, but it retains the 16
edit-7 failures.  Its first same-descriptor pair is the rank-six star and
`{{1,3},{1,4},{1,6},{2,3},{2,5}}`: the common five-move carrier passes the
star, while the second tree already has `N=A` and the carrier fails at factors
8 and 11.  Candidate B sees path `(5,2,3,1)`, detects its internal ascent, and
correctly assigns identity.

## Current finite theorem

Candidate B has 407 descriptor classes and 14 distinct assigned words.  Every
class has a common word by construction and all of its literal replays pass.
The length histogram is

```text
length       0    1    2    5    9   13   17
rows       568  125  125  108   84   65   50
```

Thus the exact finite maximum is 17.  The normalized complete-row digests are

```text
Candidate A 85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
Candidate B 80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
```

## Boundary

Candidate B's descriptor is deliberately rich and nearly records the whole
root contour.  The 407 classes collapse to 14 words because the displayed
formula uses only the edited vertex, child-sign vector, and the late/ascent
closure decision; the remaining contour incidence is retained to make that
decision and to prevent hidden collisions.  This finite collapse supplies no
all-rank sufficiency theorem or asymptotic route-length bound.

Next: freeze the exact finite theorem and request a clean-room immutable
audit.  No every-color, arbitrary-representative, voltage-corrected total
length, gap, mixing, or Terminal claim is made.
