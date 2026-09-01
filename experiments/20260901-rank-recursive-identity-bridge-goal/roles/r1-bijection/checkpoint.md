# R1 substantive checkpoint

Date: 2026-09-01 UTC

## Named claim

For maps composed by `(alpha beta)(x)=alpha(beta(x))` (rightmost factor acts
first), the candidate formula `(D)` has survived an independent proof audit.
The fixed-pattern map is governed by the mutually inverse local rules

```text
(i N) a  ->  a (a^{-1}(i) N),
a (j N)  ->  (a(j) N) a,
```

for every old factor `a in S_(N-1)`.  The first rule decreases the number of
old/star inversions by exactly one.  A given star crosses, in forced order,
exactly the old factors originally to its right.  If their word product is
`s`, its final lower endpoint is `s^{-1}(i)`.  Hence the terminal relabeling
does not depend on which currently available inversion is swapped first.

Starting from the sorted pair `(u,v)`, the inverse reads the desired binary
pattern left to right.  Whenever the next desired symbol is star, it moves the
leftmost remaining star left across the necessary old factors, applying the
second rule at every crossing.  This constructs a word of every fixed pattern
and reverses the suffix action above.

Each local rule preserves product, so if `h=eval(u)` and `q=eval(v)`, then
`g=eval(w)=h q`.  Therefore the actual star endpoint is

```text
q = h^{-1} g,
```

which confirms the orientation in `(D)`.

## Exact checkpoint

The standard-library harness `check_disintegration.py` completed the command

```text
/usr/bin/time -v python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r1-bijection/check_disintegration.py --min-n 2 --max-n 5 --max-length 6 --output-dir experiments/20260901-rank-recursive-identity-bridge-goal/roles/r1-bijection
```

with exit status zero under Python 3.12.3 at repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.  It checked all lengths `0..6`
and every endpoint for `N=2,3,4,5`:

- 28 rank/length cases;
- 1,064 exact all-endpoint coefficient comparisons using independent dynamic
  programs for `C_N`, `C_(N-1)`, and `J_N`;
- 1,168,198 structured fixed-pattern inverse-bijection cases;
- 16,219,028 local rewrite steps across leftmost sorting, rightmost sorting,
  construction, and round trips;
- zero coefficient, inverse, confluence, product, or feasibility failures.

The coefficient DP did not enumerate the `10^6` length-six `S_5` words.  The
million-scale enumeration was reserved for the requested actual word-level
bijection check.  Full endpoint rows are in `results.jsonl`; aggregate data
are in `summary.json`; resource use and stdout are in `run.log`.

## Orientation warning found during audit

The word proof, not coefficient equality alone, is necessary to establish the
orientation.  Replacing `h^{-1}g` by `g h^{-1}` gives the same *summed
coefficient* here because `J_N` commutes with `H`, but it generally gives the
wrong endpoint for the particular sorted star word.  In `S_3`, take

```text
h=(1 2), q=(1 3), g=hq=(1 3 2).
```

Then `h^{-1}g=q=(1 3)` whereas `g h^{-1}=(2 3)`.  The harness records this
witness at every tested `N>=3`.

## Boundary status and remaining work

`N=2` and `L=0` pass with the convention `X^0=e`, including `0^0` in the
group-algebra sense `C_1^0=e`.  Exact DP also confirms the general feasibility
criterion at all 1,064 tested endpoint cases.  The final report still needs a
written proof of the feasibility iff statement, the conditional exact-uniform
sampling consequence, full exceptional-case language, dependencies, hashes,
and the required return schema.

Checkpoint verdict: `keep`, pending final write-up and coordinator audit.
