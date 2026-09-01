# M88 fresh referee report on M83

Date: 2026-08-12.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Referee decision

```text
ACCEPT M83's balanced one-step theorem.
Material numbered objections: none.
```

The accepted statement is exactly this scoped theorem.

> Let `n=3k`, with odd `k>=3`.  In M73's cyclic quotient rank-two
> correlation kernel, the products
>
> ```text
> A_k=(0,k,2k),       B_k=(0,1)(k,2k)
> ```
>
> are strict endpoint-sharing neighbors.  There is a cyclic-invariant
> far-singleton event `F_k` such that `bar K(A_k,F_k)=0` and
> `bar K(B_k,F_k)>=p_k`, where
>
> ```text
> p_k ~ 4/[9e sqrt(pi k)]
> and p_k >= 2/[27e^2 sqrt(k)].
> ```

Consequently a uniform `O(1/n)` **one-step** influence bound on strict
`Lambda_n` edges is refuted.  This result neither proves nor refutes the open
`O(n^-2)` **two-step** estimate.  It proves no H0 gap, fixed-endpoint bridge
gap, identity heat-bath gap, or Terminal A/B conclusion.

## 2. Frozen provenance

The assigned immutable hashes independently match:

| M83 frozen artifact | required SHA-256 | observed |
|---|---|---|
| `report.md` | `6e7a42b0166dab0c1c7a46cb65844258ff8c5887de4d2e488d9cdd8749d06eee` | match |
| `freeze_manifest.sha256` | `87866cd283f860bb87bb0eeed7973daa5d78646ded5bb410114e6520b8a2d941` | match |

Running `sha256sum -c` from the repository root returned `OK` for all 24
manifest entries.  No frozen M83 or shared project file was edited.

The first attempted manifest check was run from inside M83's directory and
therefore could not resolve its repository-relative paths.  Rerunning from
the repository root—the path convention encoded in the manifest—passed every
entry; this was an invocation error, not a provenance defect.

## 3. Target, kernel, conventions, and accepted dependencies

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Here

```text
h=(0 1 ... n-1)
```

and the underlying target is uniform on minimal length-`n-1`
transposition factorizations of `h`.  Pair products are then compressed to
simultaneous-`h`-conjugacy orbits.  This is M73's invariant coordinate-
correlation kernel `bar K`, not the identity bridge or the `{3,4,5}` identity
heat-bath kernel.

For a supported rank-two product `g`, the accepted M73 inputs are

```text
A_g=F_(n-3)(g^-1 h),
B_(g,s)=F_(n-5)((gs)^-1 h),
K(g,s)=a(s)B_(g,s)/A_g,
```

where `a(s)=3` for an oriented 3-cycle and `a(s)=2` for a noncrossing
double.  The quotient row sums the raw `K(g,s)` over every raw state in a
target orbit and is self-adjoint.  M80's independent accepted input is the
definition of the strict endpoint-sharing graph `Lambda_n` and its diameter-
four bound.  The current theorem uses only adjacency, not that diameter.

## 4. Audit of the finite combinatorial interfaces

### 4.1 Strict adjacency and residual components — accepted

The ordered lifts

```text
A_k=((k,2k),(2k,0)),       B_k=((k,2k),(0,1))
```

have the displayed products under the stated convention.  They share their
first chord, and the differing chords share exactly endpoint `0`, so this is
a strict `Lambda_n` edge.  Direct tracing gives residual cycles

```text
A_k^-1 h: [0,...,k-1], [k,...,2k-1], [2k,...,3k-1],
B_k^-1 h: {0}, (1,...,k-1,2k,...,3k-1), (k,...,2k-1).
```

Their sizes are `(k,k,k)` and `(1,2k-1,k)`, as M83 states.

### 4.2 The entire A-side event is absent — accepted

Every factor in a minimal completion of `A_k^-1h` stays inside one of its
three contiguous length-`k` cycles.  Therefore both chords of any reachable
double target lie within those blocks.

For a noncrossing double with positive cyclic endpoint gaps `x,y,z,w`, the
separated and nested residual schemas have sizes

```text
(x,z,y+w),       (x+z,y,w).
```

A singleton entry is therefore a matched polygon-boundary gap.  After that
boundary edge is removed, the other target chord is still internal to a
contiguous length-`k` block.  One remaining residual part is at most `k-1`
(or the corresponding internal arc with the singleton gap removed).  Thus it
is impossible for both nonsingletons to be at least `k`.

The event

```text
F_k={double target orbits with residual sizes
     (1,u,3k-1-u), k<=u<=floor((3k-1)/2)}
```

depends only on cycle sizes, hence is cyclic invariant.  This establishes
the full quotient identity `bar K(A_k,F_k)=0`, not merely zero mass on the
selected B-side subset.

### 4.3 Selected B-side targets and no orbit overcount — accepted

For the nontrivial B residual cycles

```text
L=(1,...,k-1,2k,...,3k-1),       M=(k,...,2k-1),
```

select

```text
e=(i,j), 1<=i<=k-1, 2k<=j<=3k-1, k+1<=j-i<=2k,
f=(m,m+1), k<=m<=2k-2.
```

Their order is `i<m<m+1<j`, and direct gap tracing gives

```text
cycle sizes of (ef)^-1h = (1,j-i-1,3k-(j-i)).
```

The imposed range puts every selected target in `F_k`.  Writing
`r=j-i-k`, there are `r` long chords with split `r` for
`1<=r<=k-1`, and another `k-1` choices at `r=k`, whose smaller split is
again `k-1`.  Hence the exact multiplicities are

```text
M_s=s (1<=s<=k-2),       M_(k-1)=2(k-1).
```

A product of two disjoint transpositions uniquely identifies its two edges,
and the two B residual components distinguish `e` from `f`.  Thus no raw
target is duplicated.  Every selected double has exactly two ordered lifts;
these are precisely the two residual-color orders already included in

```text
c_k=2(2k-2)(k-1)/[(3k-3)(3k-4)].
```

No cyclic-orbit factor is missing: the quotient row is literally a sum over
raw target states, and the selected raw targets form a subset of the raw
union underlying the invariant event `F_k`.

There are `k-1` allowed M-boundary chords, each of weight `w_k(1)`.  The long
chord multiplicities give

```text
L_k=sum_(s=1)^(k-2)s w_(2k-1)(s)
       +2(k-1)w_(2k-1)(k-1),
```

and the selected mass is exactly

```text
p_k=c_k (k-1)w_k(1)L_k.
```

## 5. Conditioned-Borel identity and asymptotic — accepted

Put

```text
tau(d)=d^(d-1)/d!,       b_d=e^(-d)tau(d),
w_d(s)=(d-2)!tau(s)tau(d-s)/d^(d-2).
```

Cancellation of exponentials and `d!=d(d-1)(d-2)!` gives the exact identity

```text
d w_d(s)=b_s b_(d-s)/[(1-1/d)b_d].
```

For odd `d`, exactly `d` chords have any smaller split `s<d/2`; exact
summation therefore gives a probability law, without an anchor or orientation
factor left over.

Stirling gives `b_j~(2pi)^(-1/2)j^(-3/2)` with matching uniform upper and
lower power bounds.  With `x=s/d`, the rescaled summand
`d sqrt(d)s w_d(s)` converges to

```text
(2pi)^(-1/2)x^(-1/2)(1-x)^(-3/2)
```

and is bounded by `C x^(-1/2)` on `0<x<=1/2`.  The initial segment
`s<=epsilon d` contributes at most `2C sqrt(epsilon)`; away from zero,
ordinary uniform Riemann convergence applies.  Thus

```text
sqrt(d) sum_(s<d/2)s w_d(s)
 -> (2pi)^(-1/2) integral_0^(1/2)
          x^(-1/2)(1-x)^(-3/2) dx
  =sqrt(2/pi).
```

For `d=2k-1`, the central contribution is `O(k^-3/2)`, so

```text
sqrt(k)L_k ->1/sqrt(pi).
```

Finally, `c_k->4/9` and the exact identity

```text
(k-1)w_k(1)=((k-1)/k)^(k-2)->e^-1
```

give `p_k~4/[9e sqrt(pi k)]`.  The singular endpoint and the central chord
have both been controlled, so no unproved interchange remains in this limit.

## 6. Explicit lower bound — accepted

The critical Borel masses decrease because

```text
b_(j+1)/b_j=e^-1(1+1/j)^(j-1)<1.
```

The Borel identity then gives `d w_d(s)>=b_s`.  From
`s!<=e sqrt(s)(s/e)^s` one has `b_s>=e^-1s^-3/2`.  For `d=2k-1`,

```text
L_k >= [e(2k-1)]^-1 sum_(s=1)^(k-2)s^-1/2
    >= sqrt(k-2)/[e(2k-1)]
    >=1/[4e sqrt(k)].
```

The last step is equivalent after squaring to
`16k(k-2)>=(2k-1)^2`, true for `k>=3`.  Applying the same domination at
`s=1` gives

```text
(k-1)w_k(1)>=(1-1/k)b_1>=2/(3e),
```

while direct simplification gives

```text
c_k=4(k-1)/[3(3k-4)]>=4/9.
```

Their product is the claimed all-odd-`k>=3` bound

```text
p_k>=2/[27e^2 sqrt(k)].
```

## 7. Fresh exact computation

`independent_exact_audit.py` was written from scratch and imports no M83 or
M73 implementation.  For `k=3,5` it enumerates every ordered pair of raw
transpositions, retains every admissible rank-two product, reconstructs both
kernel rows over `Fraction`, and sums the **full** far-singleton event before
checking the selected subset.

```text
k  n   support  row A  row B  K_A(F)  K_B(F)
3   9       336     1      1       0  1732/5625
5  15      3185     1      1       0  119367232/730731375

k  selected targets  selected A  selected B = closed p_k
3                10           0  832/5625
5                56           0  1333643264/19729747125
```

It also checked exact strict adjacency, residual sizes, theta-invariance of
the full event, the split multiplicities, target uniqueness, two micro-lifts
per selected double, and the conditioned-Borel identity for every split in
the component sizes used.  Every check passed.  A separate rerun of M83's
frozen certificate into this directory reproduced the same two selected
rational masses.  Floating large-`k` evaluation is calibration only and is
not used to prove the limit.

Representative commands from the repository root are

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-18/\
mission-M88-m83-fresh-referee/independent_exact_audit.py \
  --k 3 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/\
mission-M88-m83-fresh-referee/independent_exact_k5.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-17/\
mission-M83-endpoint-sharing-influence/balanced_tail_certificate.py \
  --k 3 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-18/\
mission-M88-m83-fresh-referee/m83_certificate_rerun_k5.json
```

Both computations are deterministic (`seed=null`) under Python `3.12.3`.

## 8. Dependency ledger, self-attack, and logical scope

- **Accepted proved inputs:** M73's exact raw/quotient kernel and four-schema
  decomposition; M80's strict `Lambda_n` definition.
- **Proved by M83 and independently accepted here:** source adjacency,
  A-side zero event, selected B-side probability, conditioned-Borel identity,
  exact multiplicities, asymptotic constant, and explicit all-`k` bound.
- **Refuted:** a universal `O(1/n)` bound on one-step `bar K` influence along
  strict endpoint-sharing edges.
- **Exact finite only:** the enumerations at `k=3,5` and M83's other finite TV
  and cancellation diagnostics.
- **Unresolved:** `TV(bar K^2(alpha,.),bar K^2(beta,.))=O(n^-2)`, including
  its balanced signed-Abel subproblem; the H0 consequence; every bridge or
  identity-chain gap theorem.

The strongest self-attack is that the selected set itself is not asserted to
be an orbit union.  That causes no gap: it is used only as a raw subset of
the raw union defining the cyclic-invariant `F_k`, while the zero side is
proved for all of `F_k`.  Exact enumeration independently verifies both
facts.  The infinite subsequence `n=3k`, odd `k`, is sufficient to refute a
universal one-step `C/n` bound but carries no negative implication for other
ranks or for the second iterate.  The smallest family member `k=3,n=9`
satisfies both the exact formula and explicit bound; `k=1,n=3` is excluded.

## 9. Artifacts, hygiene, and final verdict

M88 owns only this directory.  Its artifacts are:

- `plan.md` and `checkpoint.md`;
- `analytic_audit.md`, containing the expanded independent proof;
- `independent_exact_audit.py` and `independent_exact_k5.json`;
- `m83_certificate_rerun_k5.json`;
- this `report.md` and the final freeze manifest.

No package was installed, no external network or random input was used, and
no M83, shared note, manuscript, `HANDOFF.md`, `GOAL_SPEC.md`, project skill,
or other worker artifact was changed.  The generated Python cache was removed
before freezing.  A final `git status --short` shows only the already broad
run-level untracked experiment/notes roots, so it cannot distinguish M88's
new files from the pre-existing shared run tree; the list above is the exact
M88-owned change set.

**Final verdict: ACCEPT M83's balanced one-step theorem with zero material
objections.  Promote the one-step obstruction only; retain the two-step
signed-cancellation estimate as unresolved.**
