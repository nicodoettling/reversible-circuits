# M30 plan: second full-support shell

## Objective

For `N>=5`, `m=4N^3+4`, and the original lazy exact `r=3,4,5` chain, let

```text
V^(0)={c>=2},
V^(a+1)=V^(a) union {y:K(x,y)>0 for some x in V^(a)}.
```

Characterize or sharply sandwich `V^(2)`, prove it is proper, orient its
global stationary mass, and count all boundary flow.  Use
`(pq)(x)=p(q(x))` throughout.

## Structural sandwich

M28 proves `V^(1)` consists exactly of words admitting a vertex cut whose
crossing occurrences lie in one interval of length at most five.  For a
second update:

- overlapping witness/update windows put all crossings in one interval of
  length at most nine;
- separated windows have products in the cut subgroup individually, because
  the update window was factorwise internal before the update.

Define an overlapping halo `O_2` and a separated-product halo `D_2` from
these alternatives, and prove

```text
V^(2) subset O_2 union D_2 subset
{some cut's crossings are coverable by two five-windows}.
```

This is the requested rigorous substitute for an unwieldy exact equality.

## Mass and boundary strategy

1. Cover `O_2` by a ten-window.  For `D_2`, use two disjoint five-windows.
   In either case the outside length is the same even number `m-10`, and the
   relevant block products lie in the cut subgroup.  Centrality and the exact
   factorial cut-size sum retain the dominant isolate normalization.
2. Construct second-shell sources from two prefixes
   `(s,q,q,q,s)^2`, followed by an identity tail on `N-1` labels which stays
   connected after deletion of any union of two five-windows.
3. Prove a constant fraction of dense identity tails have this robustness by
   a direct cut/window union bound.
4. Push the fourth `s` through the first four tail factors in one actual
   `H_5`.  The incident-to-`z` positions change from `1,5,6,10` to
   `1,5,6,14`, which require at least three five-windows to cover.  Tail
   robustness excludes every other two-window cut.
5. Divide this exact boundary flow by the structural upper bound on
   `|V^(2)|`, retaining all `Q_3+Q_4+Q_5` terms.

## Failure modes

- Two-window coverability alone is not known to imply distance two; do not
  claim equality.
- Conductance is not monotone under shell enlargement.
- A separated update needs individual subgroup-product constraints; dropping
  them loses the factorial normalization.
- Odd block products cannot be commuted through a subgroup class sum unless
  they lie in that subgroup.
- Repairing the isolate cut is insufficient unless the tail is robust under
  two deleted windows for every internal cut.

## Computation

No computation is planned.  All claims are universal counting and
ordered-product arguments.
