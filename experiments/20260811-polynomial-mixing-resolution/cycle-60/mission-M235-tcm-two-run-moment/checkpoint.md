# Mission M235 checkpoint

Date: 2026-08-13 UTC

Status: substantive exact reconstruction complete; analytic proof route found.

The project skill, `HANDOFF.md`, `GOAL_SPEC.md`, the sampling reference, the
experiment standard, and coordinator entry `L-0284` have been read.  Every
file in frozen M192/M195, M199/M207, M211/M215, M217/M222, and M226/M229
passes its `SHA256SUMS` inventory.  M229's correction is retained:
`G_k(x)` is used only for `1<=x<=(3k-3)/2`.

Put `D=2k-1`, `R=2k-3`, `j=(k-1)/2`,
`K_R(r,d)=b_d b_(r-d)/(R b_r)`, and
`q_s=[k/(k-1)]b_s b_(k-s)/b_k`.  The exact reconstructed obligation is

```text
T_B(k,l)-T_A(k,l)=sum_(y=2)^l c^T_(k,y),
|T_B(k,l)-T_A(k,l)| <= C sqrt(l)/k,
3<=k odd, 2<=l<=(3k-1)/2.                    (TCM)
```

Here `T_B,T_A` are the q-averaged raw masses of the unique complementary
two-run face in the literal disjoint ordered-pair laws.  They retain both
channel-two kinds, all same/cross placements, both B seams, the A marked and
untouched cases, and repeated-size collisions with multiplicity.

The first exact geometric identity is now explicit.  In the B two-seam word,
for parent `r`, middle child `d`, retained length `t=r-d`, placement
`1<=a<=t-1`, and cyclic start `i`, let `E(i;r,d,a)` be the union of the
two retained boundary arcs.  If `beta,sigma` are respectively the large
and small seam edges, the two-run size is exactly

```text
y_B=t+k 1{beta in E}+1{sigma in E}.                 (B-size)
```

Thus seams and seam collisions remain literal.  Since `|E|=t`, averaging
over `i` gives the rigorous placement bound

```text
(1/D) sum_i 1{y_B<=l}
 <= 1{t<=l-k} + ((D-t)/D)1{t<=l}.                  (B-place)
```

The A law has two exact channels.  For a marked second edge in a parent
`r in {s,k-s}`, the retained union has size `t` with probability
`(k-t)/k` and size `t+2k` with probability `t/k`; only the first can
meet the allowed cutoff.  For a second edge in the untouched k-cycle, the
only allowed-cutoff configuration has first one-run size `k-s`, second
one-run size `k-c`, and two-run size `k+s+c`.  Consequently

```text
T_A^mark =
 sum_s q_s sum_(r in {s,k-s}) sum_(2<=t<=min(l,r-1))
   (t-1)K_R(r,t)(k-t)/k,

T_A^unt =
 sum_s q_s (s/k) sum_(1<=c<=l-k-s) c K_R(k,c).
```

These formulas expose a stronger route than signed cancellation: both
positive raw laws appear separately bounded by `C sqrt(l)/k`.  For B,
(B-place) splits the long-parent contribution into a small-`t` Borel
moment and a seam-excluded term; the latter's `t>r/2` tail gains
`(D-t)/D=(s+d)/D`.  For A, the marked terms reduce by the Borel convolution
to the truncated moment `sum_(t<=l)t b_t=O(sqrt(l))`, while the untouched
term is `O(1/k)`.  Therefore triangle inequality would prove TCM without
using sign.

The deterministic literal checker currently reconstructs every ordered
tuple and confirms the run/type classification at `k=3,5`.  The next step
is to certify the displayed closed formulas coefficient-by-coefficient at
`k=3,5,7`, then write the universal Borel-moment proof with all range
splits.  Finite checks remain calibration only.
